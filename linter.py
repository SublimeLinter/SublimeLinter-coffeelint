#
# coffeelint.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Aparajita Fishman
# Copyright (c) 2015-2016 The SublimeLinterCommunity
# Copyright (c) 2013-2014 Aparajita Fishman
#
# License: MIT
#

"""This module exports the Coffeelint plugin class."""

from SublimeLinter.lint import Linter, persist
from json import load
import os


class Coffeelint(Linter):
    """Provides an interface to coffeelint."""

    syntax = ('coffeescript', 'coffeescript_literate')
    executable = 'coffeelint'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.4.0'
    regex = (
        r'^<issue line="(?P<line>\d+)"\s*\r?\n'
        r'\s*lineEnd="\d+"\s*\r?\n'
        r'\s*reason="\[(?:(?P<error>error)|(?P<warning>warn))\]\s+'
        r'(?:\[stdin\]:\d+:(?P<col>\d+):\s+error:\s+)?'
        r'(?P<message>[^"\n\r]+)["\n\r]'
    )
    multiline = True
    comment_re = r'\s*#'
    tempfile_suffix = '.coffee'

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = [self.executable_path, '--reporter', 'jslint']

        if persist.get_syntax(self.view) == 'coffeescript_literate':
            command.append('--literate')

        base_dir = os.path.dirname(self.view.file_name())
        coffeelint_json = self.get_config_file(base_dir)
        if coffeelint_json:
            command += ('-f', coffeelint_json)

        command.append('@')
        return command

    def get_config_file(self, path):
        path = os.path.normpath(path)
        config = self._get_config_from_dir(path)
        if config:
            return config
        else:
            config = self._get_config_from_package_json(path)
            if config:
                return config
            else:
                new_path = os.path.abspath(os.path.join(path, '..'))
                if new_path != path:
                    return self.get_config_file(new_path)
                else:
                    return None

    def _get_config_from_dir(self, path):
        config = os.path.join(path, 'coffeelint.json')
        if os.path.isfile(config):
            return config
        return None

    def _get_config_from_package_json(self, path):
        package_json = os.path.join(path, 'package.json')
        if not os.path.isfile(package_json):
            return None
        try:
            json = load(open(package_json))
            if 'coffeelintConfig' in json and json['coffeelintConfig']:
                coffeelintConfig = json['coffeelintConfig']
                if not os.path.isabs(coffeelintConfig):
                    coffeelintConfig = os.path.join(path, coffeelintConfig)
                if os.path.isfile(coffeelintConfig):
                    return coffeelintConfig
                return None
            return None
        except:
            return None
