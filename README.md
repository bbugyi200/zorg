# zorg

**The zettel note manager of the future.**

_project status badges:_

[![CI Workflow](https://github.com/bbugyi200/zorg/actions/workflows/ci.yml/badge.svg)](https://github.com/bbugyi200/zorg/actions/workflows/ci.yml)
[![Coverage](https://codecov.io/gh/bbugyi200/zorg/branch/master/graph/badge.svg)](https://codecov.io/gh/bbugyi200/zorg)
[![Documentation Status](https://readthedocs.org/projects/zettel-org/badge/?version=latest)](https://zettel-org.readthedocs.io/en/latest/?badge=latest)
[![Package Health](https://snyk.io/advisor/python/zettel-org/badge.svg)](https://snyk.io/advisor/python/zettel-org)

_version badges:_

[![Project Version](https://img.shields.io/pypi/v/zettel-org)](https://pypi.org/project/zettel-org/)
[![Python Versions](https://img.shields.io/pypi/pyversions/zettel-org)](https://pypi.org/project/zettel-org/)
[![Cookiecutter: cc-python](https://img.shields.io/static/v1?label=cc-python&message=2024.01.16-4&color=d4aa00&logo=cookiecutter&logoColor=d4aa00)](https://github.com/python-boltons/cc-python)
[![Docker: pythonboltons/main](https://img.shields.io/static/v1?label=pythonboltons%20%2F%20main&message=2024.01.16&color=8ec4ad&logo=docker&logoColor=8ec4ad)](https://github.com/python-boltons/docker-python)


## Installation 🗹

### Using `pipx` to Install (preferred)

This package _could_ be installed using pip like any other Python package (in
fact, see the section below this one for instructions on how to do just that).
Given that we only need this package's entry points, however, we recommend that
[pipx][11] be used instead:

```shell
# install and setup pipx
python3 -m pip install --user pipx
python3 -m pipx ensurepath

# install zorg
pipx install zettel-org
```

### Using `pip` to Install

To install `zorg` using [pip][9], run the following
commands in your terminal:

``` shell
python3 -m pip install --user zettel-org  # install zorg
```

If you don't have pip installed, this [Python installation guide][10] can guide
you through the process.


## Command-Line Interface (CLI)

The following subsections have been auto-generated using [cog][14]:

### `zorg --help`

<!-- [[[[[kooky.cog
import subprocess

popen = subprocess.Popen(["zorg", "--help"], stdout=subprocess.PIPE)
stdout, _ = popen.communicate()
print("```", stdout.decode().strip(), "```", sep="\n")

for cmd in [
    "action",
    "action open",
    "compile",
    "db",
    "db create",
    "db reindex",
    "edit",
    "query",
    "template",
    "template init",
    "template list",
    "template render",
]:
    popen = subprocess.Popen(["zorg"] + cmd.split() + ["--help"], stdout=subprocess.PIPE)
    stdout, _ = popen.communicate()
    print(f"\n### `zorg {cmd} --help`\n")
    print("```", stdout.decode().strip(), "```", sep="\n")
]]]]] -->
```
usage: zorg [-h] [-c CONFIG_FILE] [-L [FILE[:LEVEL][@FORMAT]]] [-v]
            [--version] [-d ZETTEL_DIR]
            {action,compile,db,edit,query,template} ...

The zettel note manager of the future.

options:
  -c CONFIG_FILE, --config CONFIG_FILE
                        Absolute or relative path to a YAML file that contains
                        this application's configuration.
  -d ZETTEL_DIR, --dir ZETTEL_DIR
                        The directory where all of your notes are stored.
  -h, --help            show this help message and exit
  -L [FILE[:LEVEL][@FORMAT]], --log [FILE[:LEVEL][@FORMAT]]
                        This option can be used to enable a new logging
                        handler. FILE should be either a path to a logfile or
                        one of the following special file types: [1] 'stderr'
                        to log to standard error (enabled by default), [2]
                        'stdout' to log to standard out, [3] 'null' to disable
                        all console (e.g. stderr) handlers, or [4] '+[NAME]'
                        to choose a default logfile path (where NAME is an
                        optional basename for the logfile). LEVEL can be any
                        valid log level (i.e. one of ['CRITICAL', 'DEBUG',
                        'ERROR', 'INFO', 'TRACE', 'WARNING']) and FORMAT can
                        be any valid log format (i.e. one of ['color', 'json',
                        'nocolor']). NOTE: This option can be specified
                        multiple times and has a default argument of '+'.
  -v, --verbose         How verbose should the output be? This option can be
                        specified multiple times (e.g. -v, -vv, -vvv, ...).
  --version             show program's version number and exit

subcommands:
  {action,compile,db,edit,query,template}
    action              Used to interface with vim via an action protocol.
    compile             Compiles zorg (*.zo) files into zorc (*.zoc) files.
    db                  Commands for managing Zorg's SQL database.
    edit                Generate new day logs from templates and open the main
                        day log in your system's editor. This is the default
                        subcommand.
    query               Run a zorg query against your zettel directory.
    template            Commands for managing .zot templates.
```

### `zorg action --help`

```
usage: zorg action [-h] {open} ...

Used to interface with vim via an action protocol.

options:
  -h, --help  show this help message and exit

subcommands:
  {open}
    open      Open a zettel link if one exists on the provided zorg file line.
```

### `zorg action open --help`

```
usage: zorg action open [-h] zo_path line_number [option_idx]

Open a zettel link if one exists on the provided zorg file line.

positional arguments:
  line_number  The line number that your editor cursor is currently located
               on.
  option_idx   Used on a second 'action open' run to indicate which option was
               selected.
  zo_path      The file that your editor currently has open.

options:
  -h, --help   show this help message and exit
```

### `zorg compile --help`

```
usage: zorg compile [-h] zo_path

Compiles zorg (*.zo) files into zorc (*.zoc) files.

positional arguments:
  zo_path     Path to the zorg file you want to compile.

options:
  -h, --help  show this help message and exit
```

### `zorg db --help`

```
usage: zorg db [-h] {create,reindex} ...

Commands for managing Zorg's SQL database.

options:
  -h, --help        show this help message and exit

subcommands:
  {create,reindex}
    create          Create zorg's backend database from scratch.
    reindex         Reindex any changed files by adding them to the database.
```

### `zorg db create --help`

```
usage: zorg db create [-h]

Create zorg's backend database from scratch.

options:
  -h, --help  show this help message and exit
```

### `zorg db reindex --help`

```
usage: zorg db reindex [-h] [paths ...]

Reindex any changed files by adding them to the database.

positional arguments:
  paths       Reindex these specific paths. If this argument is not provided,
              we use a hashing approach to check which files have changed.

options:
  -h, --help  show this help message and exit
```

### `zorg edit --help`

```
usage: zorg edit [-h] [zo_paths ...]

Generate new day logs from templates and open the main day log in your system's editor. This is the default subcommand.

positional arguments:
  zo_paths    The .zo files we want to open in an editor.

options:
  -h, --help  show this help message and exit
```

### `zorg query --help`

```
usage: zorg query [-h] query

Run a zorg query against your zettel directory.

positional arguments:
  query       The zorg query we will run.

options:
  -h, --help  show this help message and exit
```

### `zorg template --help`

```
usage: zorg template render [-h] template [variables ...]

Render a new .zo file using a .zot template.

positional arguments:
  template    Path to the .zot template.
  variables   A list of variable specs of the form of key=value.

options:
  -h, --help  show this help message and exit
```

### `zorg template init --help`

```
usage: zorg template init [-h] [-f] [-t TEMPLATE] new_path [variables ...]

Initialize a new file using a zorg template.

positional arguments:
  new_path              Path to the new file you would like to create.
  variables             A list of variable specs of the form of key=value.

options:
  -f, --force           Overwrite target file if the file already exists.
  -h, --help            show this help message and exit
  -t TEMPLATE, --template TEMPLATE
                        Optional path to the .zot template. If a template is
                        not provided, we will infer what template to use based
                        off of the new file's name.
```

### `zorg template list --help`

```
usage: zorg template list [-h]

List all zorg template files.

options:
  -h, --help  show this help message and exit
```

### `zorg template render --help`

```
usage: zorg template render [-h] template [variables ...]

Render a new .zo file using a .zot template.

positional arguments:
  template    Path to the .zot template.
  variables   A list of variable specs of the form of key=value.

options:
  -h, --help  show this help message and exit
```
<!-- [[[[[end]]]]] -->

<!-- [[[[[kooky.cog
from pathlib import Path

lines = Path("./docs/design/design.md").read_text().split("\n")
if any(L.strip() for L in lines):
    fixed_lines = [L.replace("(.", "(./docs/design") if L.startswith("![") else L for L in lines]
    print("## Design Diagrams\n")
    print("\n".join(fixed_lines))
]]]]] -->
<!-- [[[[[end]]]]] -->


## Useful Links 🔗

* [API Reference][3]: A developer's reference of the API exposed by this
  project.
* [cc-python][4]: The [cookiecutter][5] that was used to generate this project.
  Changes made to this cookiecutter are periodically synced with this project
  using [cruft][12].
* [CHANGELOG.md][2]: We use this file to document all notable changes made to
  this project.
* [CONTRIBUTING.md][7]: This document contains guidelines for developers
  interested in contributing to this project.
* [Create a New Issue][13]: Create a new GitHub issue for this project.
* [Documentation][1]: This project's full documentation.


[1]: https://zettel-org.readthedocs.io/en/latest
[2]: https://github.com/bbugyi200/zorg/blob/master/CHANGELOG.md
[3]: https://zettel-org.readthedocs.io/en/latest/modules.html
[4]: https://github.com/python-boltons/cc-python
[5]: https://github.com/cookiecutter/cookiecutter
[6]: https://docs.readthedocs.io/en/stable/
[7]: https://github.com/bbugyi200/zorg/blob/master/CONTRIBUTING.md
[8]: https://github.com/bbugyi200/zorg
[9]: https://pip.pypa.io
[10]: http://docs.python-guide.org/en/latest/starting/installation/
[11]: https://github.com/pypa/pipx
[12]: https://github.com/cruft/cruft
[13]: https://github.com/bbugyi200/zorg/issues/new/choose
[14]: https://pypi.org/project/cogapp/
