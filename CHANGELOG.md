# Changelog for `zorg`

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/


## [Unreleased](https://github.com/bbugyi200/zorg/compare/0.7.5...HEAD)

No notable changes have been made.


## [0.7.5](https://github.com/bbugyi200/zorg/compare/0.7.4...0.7.5) - 2024-06-21

### Added

* Add support to `action open` command for targeting ZIDs.
* Add support for relative dates (e.g. `0d`, `-2m`, `1y`).
* Add support for inline and bullet properties.
* Add support for link filters in queries.
* Add support for ZIDs to `zorg action open` command.


## [0.7.4](https://github.com/bbugyi200/zorg/compare/0.7.3...0.7.4) - 2024-05-26

### Added

* Add support for related file section to query pages.
* Add support for `f=GLOB` style file-filters in zorg queries.
* Add support for selecting files and tags using zorg queries.
* Auto-refresh query pages when they are open (e.g. via `action open`).

### Fixed

* Bug which caused modify date or ZID to not show in query pages.


## [0.7.3](https://github.com/bbugyi200/zorg/compare/0.7.2...0.7.3) - 2024-05-17

### Added

* Add support for the various new WHERE filters and new GROUP BY dimensions.
* Add ORDER BY support to zorg queries.


## [0.7.2](https://github.com/bbugyi200/zorg/compare/0.7.1...0.7.2) - 2024-05-05

### Added

* Implement basic functionality for `zorg query`. We can now SELECT notes with
  a (very limited ATM) WHERE filter and GROUP BY various dimensions (e.g. file,
  note type, projects).


## [0.7.1](https://github.com/bbugyi200/zorg/compare/0.7.0...0.7.1) - 2024-05-02

### Fixed

* Stop removing 'edit' vim commands with no args.


## [0.7.0](https://github.com/bbugyi200/zorg/compare/0.6.4...0.7.0) - 2024-05-02

### Changed

* *BREAKING CHANGE*: Expect final line of keep-alive file to be the full path
  of the file in the currently focused buffer.


## [0.6.4](https://github.com/bbugyi200/zorg/compare/0.6.3...0.6.4) - 2024-04-27

### Changed

* Add `zorg query` command that does nothing ATM.
* Stop generating ZIDs which use any of the following characters based on
  similarity to digits OR because the lowercase letter hangs over an underline: `SQgipqy`

### Fixed

* Allow ZIDs and priorities in note body.
* Strip zettel dir from sql.ZorgFile.path.


## [0.6.3](https://github.com/bbugyi200/zorg/compare/0.6.2...0.6.3) - 2024-04-19

### Fixed

* Fix bug where absolute filename was used to key file hash. This was causing
  the file hash map to not be portable across different machines.


## [0.6.2](https://github.com/bbugyi200/zorg/compare/0.6.1...0.6.2) - 2024-04-14

### Fixed

* Fix crash from trying to convert deleted entity.


## [0.6.1](https://github.com/bbugyi200/zorg/compare/0.6.0...0.6.1) - 2024-04-10

### Added

* Add `zorg db create` command that creates a sqlite database and updates all
  `*.zo` files by adding ZIDs to the notes they contain.


## [0.6.0](https://github.com/bbugyi200/zorg/compare/0.5.1...0.6.0) - 2024-03-31

### Changed

* *BREAKING CHANGE*: Stop injecting `one_day` template variable.
* Several improvements to the grammar used by `zorg compile`.
* A lot of changes were made to the grammar and application logic that powers
  the `zorg compile` command, which has not yet been integrated into a useful
  workflow (but will be).


## [0.5.1](https://github.com/bbugyi200/zorg/compare/0.5.0...0.5.1) - 2024-03-21

### Fixed

* Build ANTLR grammars before publishing a new release to PyPI.


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
