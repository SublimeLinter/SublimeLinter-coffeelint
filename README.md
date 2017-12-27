SublimeLinter-coffeelint
=========================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-coffeelint.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-coffeelint)

This linter plugin for [SublimeLinter](http://sublimelinter.readthedocs.org) provides an interface to [coffeelint](http://www.coffeelint.org). It will be used with files that have the “CoffeeScript” and “CoffeeScript (Literate)” syntax.

## Installation

SublimeLinter must be installed in order to use this plugin. 

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

Before installing this plugin, you must ensure that `coffeelint` is installed on your system. To install `coffeelint`, do the following:

1. Install [Node.js](http://nodejs.org) (and [npm](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager) on Linux).

1. Install `coffeelint` by typing the following in a terminal:
   ```
   npm install -g coffeelint
   ```

1. If you are using `nvm` and `zsh`, ensure that the line to load `nvm` is in `.zshenv` and not `.zshrc`.

In order for `coffeelint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).


## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

You may configure `coffeelint`’s behavior using `coffeelint.json` configuration files, exactly as is described in the [coffeelint documentation](http://www.coffeelint.org/#usage).
