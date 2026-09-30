import importlib
import unittest

import sublime
from SublimeLinter.lint import persist
from SublimeLinter.lint.linter import VirtualView


Linter = importlib.import_module('SublimeLinter-coffeelint.linter').Coffeelint


class TestColumns(unittest.TestCase):
    def test_issue_33_compiler_columns(self):
        source = 's = "😀😀" ; foo bar baz(\n'
        output = ('<issue line="1"\n        lineEnd="1"\n'
                  '        reason="[error] [stdin]:1:25: error: missing )\n'
                  's = &quot;😀😀&quot; ; foo bar baz(\n                        ^"\n')
        self.assertMatch(output, source, source.index('('), '(')

    def test_ascii_compiler_columns(self):
        output = '<issue line="1"\n lineEnd="1"\n reason="[error] [stdin]:1:4: error: missing )"\n'
        self.assertMatch(output, 'baz(\n', 3, '(')

    def test_ordinary_results_without_columns_still_highlight_the_line(self):
        output = '<issue line="1"\n lineEnd="1"\n reason="[warn] Class name should be UpperCamelCased"\n'
        settings = sublime.load_settings('SublimeLinter-coffeelint-test-columns.sublime-settings')
        settings.set('no_column_highlights_line', True)
        self.addCleanup(setattr, persist, 'settings', persist.settings)
        persist.settings = settings
        self.assertMatch(output, 'class foo\n', 0, 'class foo')

    def assertMatch(self, output, source, col, text):
        linter = Linter(sublime.View(0), {})
        match, = linter.find_errors(output)
        error = linter.process_match(match, VirtualView(source))
        self.assertIsNotNone(error)
        self.assertEqual({k: error[k] for k in ('line', 'start', 'region', 'offending_text')}, {
            'line': 0, 'start': col, 'region': sublime.Region(col, col + len(text)), 'offending_text': text,
        })
