# Changelog for `zorg`

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/


## [Unreleased](https://github.com/bbugyi200/zorg/compare/0.5.0...HEAD)

No notable changes have been made.


## [0.5.0](https://github.com/bbugyi200/zorg/compare/0.4.0...0.5.0) - 2024-03-17

### Added

* Added the `zorg compile` command, which will be used to compile zorg (\*.zo)
  files into zorc (\*.zoc) files.
* New `ZorgFile.g4` ANTLR4 grammar and auto-generate corresponding parser, lexer, and
  listener as apart of CI.

### Changed

* *BREAKING CHANGE*: Removed `zorg action open` command's column number
  positional argument.


## [0.4.0](https://github.com/bbugyi200/zorg/compare/0.3.0...0.4.0) - 2024-03-11

### Changed

* *BREAKING CHANGE*: Replace the OPEN\_LINK string constant with the `zorg
  action open` subcommand.


## [0.3.0](https://github.com/bbugyi200/zorg/compare/0.2.1...0.3.0) - 2024-03-10

### Added

* Add support for changing the paths opened in vim by writing those file paths
  to `/tmp/zorg_keep_alive`.
* Add the `zorg action` command.
* Add the `zorg template init` command.

### Changed

* *BREAKING CHANGE*: Renamed the `zorg new` command to `zorg template render`.


## [0.2.1](https://github.com/bbugyi200/zorg/compare/0.2.0...0.2.1) - 2024-03-07

### Added

* Add support for touching a "keep alive" file (e.g. `/tmp/zorg_keep_alive`) to
  signal to `zorg edit` that the same vim command should be re-run after the
  current vim instance exits.
* Add support `zorg edit` to accept file paths and/or file group names (e.g.
  `@foo`) as CLI arguments.


## [0.2.0](https://github.com/bbugyi200/zorg/compare/0.1.2...0.2.0) - 2024-03-06

### Added

* Added the 'new' subcommand, which can be used to render zorg templates from
  the command-line.

### Changed

* *BREAKING CHANGE*: Renamed the 'day' command to 'edit'.


## [0.1.2](https://github.com/bbugyi200/zorg/compare/0.1.1...0.1.2) - 2024-01-21

### Added

* Add support for initial template # comments. These comments MUST be followed
  by a blank line and are NOT included in generated files (which is the point).
  Comments that we want to be included in generated files should use ## instead
  of #.


## [0.1.1](https://github.com/bbugyi200/zorg/compare/0.1.0...0.1.1) - 2024-01-20

### Added

* Add 'day' sub-command that generates my daily logs (day, habit, and done) and
  opens my day log in vim.


## [0.1.0](https://github.com/bbugyi200/zorg/releases/tag/0.1.0) - 2024-01-15

* First release.
