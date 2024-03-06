# Changelog for `zorg`

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog], and this project adheres to
[Semantic Versioning].

[Keep a Changelog]: https://keepachangelog.com/en/1.0.0/
[Semantic Versioning]: https://semver.org/


## [Unreleased](https://github.com/bbugyi200/zorg/compare/0.2.0...HEAD)

No notable changes have been made.


## [0.2.0](https://github.com/bbugyi200/zorg/compare/0.1.2...0.2.0) - 2024-03-06

### Added

* Added the 'new' subcommand, which can be used to render zorg templates from
  the command-line.

### Changed

* Renamed the 'day' command to 'edit'.


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
