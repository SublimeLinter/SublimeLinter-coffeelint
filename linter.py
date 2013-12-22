#
# coffeelint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2013 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Coffeelint plugin class."""

import os
from SublimeLinter.lint import Linter, persist, util


class Coffeelint(Linter):

    """Provides an interface to coffeelint."""

    syntax = ('coffeescript', 'coffeescript_literate')
    executable = 'coffeelint'
    regex = (
        r'^<issue line="(?P<line>\d+)"\s*\r?\n'
        r'\s*lineEnd="\d+"\s*\r?\n'
        r'\s*reason="\[(?:(?P<error>error)|(?P<warning>warn))\] (?P<message>.+?)"\s*\r?\n'
    )
    multiline = True
    comment_re = r'\s*#'

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = [self.executable_path, '--jslint', '--stdin']

        if persist.get_syntax(self.view) == 'coffeescript_literate':
            command.append('--literate')

        config = util.find_file(os.path.dirname(self.filename), 'coffeelint.json')

        if config:
            command += ['-f', config]

        return command
