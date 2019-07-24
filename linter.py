from SublimeLinter.lint import NodeLinter, util


class Coffeelint(NodeLinter):
    regex = (
        r'^<issue line="(?P<line>\d+)"\s*\r?\n'
        r'\s*lineEnd="\d+"\s*\r?\n'
        r'\s*reason="\[(?:(?P<error>error)|(?P<warning>warn))\]\s+'
        r'(?:\[stdin\]:\d+:(?P<col>\d+):\s+error:\s+)?'
        r'(?P<message>[^"\n\r]+)["\n\r]'
    )
    multiline = True
    defaults = {
        'selector': 'source.coffee',
        'working_dir': '${file_path}'
    }

    def cmd(self):
        """Return a tuple with the command line to execute."""

        command = ['coffeelint', '--reporter', 'jslint', '--stdin']

        if util.get_syntax(self.view) == 'coffeescript_literate':
            command.append('--literate')

        return command
