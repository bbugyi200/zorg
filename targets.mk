.DELETE_ON_ERROR:
.SHELLFLAGS := -eu -o pipefail -c
.SUFFIXES:
MAKEFLAGS += --warn-undefined-variables
SHELL := /bin/bash

BUILD_GRAMMARS = $(SOURCE_VENV) ./bin/build_zorg_grammars
CRUFT = $(PYTHON) -m cruft
DOCS_SOURCE := ./docs/source
DOCS_BUILD_DIR := ./docs/build
MIN_TEST_COV := 80
PIP = $(PYTHON) -m pip
PIP_COMPILE = $(PYTHON) -m piptools compile --allow-unsafe --no-emit-index-url -q --no-emit-trusted-host
PIP_SYNC = $(PYTHON) -m piptools sync
PYTHON = $(SOURCE_VENV) python
PYTHON_VERSION := 3.10
RENDER_ALL_COGS = $(SOURCE_VENV) ./bin/render_all_cogs
SOURCE_VENV = source $(VENV_ACTIVATE);
SPHINX_APIDOC = $(SOURCE_VENV) sphinx-apidoc
SPHINX_BUILD = $(SOURCE_VENV) sphinx-build
TOX = $(SOURCE_VENV) tox
VENV := .venv
VENV_ACTIVATE = $(VENV)/bin/activate

define sync_dev_requirements
	$(PIP_SYNC) requirements-dev.txt
endef

define runtests
	$(TOX) -e $(1) -- \
		-vv \
		--cov=src/zorg \
		--cov-config=setup.cfg \
		--cov-fail-under=$(MIN_TEST_COV) \
		--cov-report=xml:coverage.xml \
		--cov-report=term-missing \
		--cov-branch \
		--doctest-modules \
		--doctest-report ndiff \
		# Don't remove this comment!
endef

.PHONY: all
all:  ## Build the package, build the docs, run all tests, and run all linters.
all: build build-docs cogs lint test

.PHONY: cogs
cogs: sync-dev-requirements
	$(RENDER_ALL_COGS)

.PHONY: lint
lint: black isort pydocstyle flake8 mypy pylint quick-lints  ## Run all linting checks.

.PHONY: quick-lints
quick-lints: sync-dev-requirements  ## Run miscellaneous linting tasks.
	$(SOURCE_VENV) ./bin/quick-lints

.PHONY: black
black: sync-dev-requirements  ## Run black checks.
	$(PYTHON) -m black --diff --check -q --color src
	$(PYTHON) -m black --diff --check -q --color tests

.PHONY: isort
isort: sync-dev-requirements  ## Run isort checks. 
	$(PYTHON) -m isort --check-only src
	$(PYTHON) -m isort --check-only tests

.PHONY: pydocstyle
pydocstyle: sync-dev-requirements  ## Run pydocstyle checks.
	$(PYTHON) -m pydocstyle src
	$(PYTHON) -m pydocstyle tests

.PHONY: flake8
flake8: sync-dev-requirements  ## Run flake8 checks.
	$(PYTHON) -m flake8 src
	$(PYTHON) -m flake8 tests

.PHONY: mypy
mypy: sync-dev-requirements  ## Run mypy checks.
	@# HACK: Because mypy's cache has been terrible lately.
	@rm -rf .mypy_cache
	$(PYTHON) -m mypy src
	@# HACK: Fixes weird numpy error that seemed to happen randomly.
	bash -c "$(SOURCE_VENV) { python -m mypy tests || python -m mypy tests; }"

.PHONY: pylint
pylint: sync-dev-requirements  ## Run pylint checks.
	$(PYTHON) -m pylint src
	$(PYTHON) -m pylint tests

.PHONY: test
test: build-grammars sync-dev-requirements  ## Run this project's test suite.
	$(call runtests,ALL)

### Test a single python version.
#
# Examples:
#   // run tests on python3.8 _only_
#   make test-py38
test-%: sync-dev-requirements
	$(call runtests,$*)

build-grammars: sync-dev-requirements
build-grammars:  ## Generate parsers, lexers, and listeners for all Zorg ANTLR4 grammars.
	$(BUILD_GRAMMARS)

.PHONY: build
build: sync-dev-requirements
build:  ## Build python package using setuptools.
	$(PYTHON) setup.py build
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

.PHONY: build-docs
build-docs: sync-dev-requirements docs-clean
build-docs:  ## Build this project's documentation using sphinx.
	$(SPHINX_APIDOC) -f -M -e -o $(DOCS_SOURCE) src/zorg
	$(SPHINX_BUILD) $(DOCS_SOURCE) $(DOCS_BUILD_DIR)

.PHONY: docs-clean
docs-clean: sync-dev-requirements
	$(SPHINX_BUILD) -M clean $(DOCS_SOURCE) $(DOCS_BUILD_DIR)

requirements%.txt: export CUSTOM_COMPILE_COMMAND="make update-requirements"
requirements%.txt: $(VENV_ACTIVATE)
	$(PIP_COMPILE) --output-file=requirements-dev.txt requirements.in requirements-dev.in
	$(PIP_COMPILE) --output-file=requirements.txt requirements.in

.PHONY: sync-dev-requirements
sync-dev-requirements: requirements-dev.txt
	$(call sync_dev_requirements)

.PHONY: update-requirements
update-requirements: export CUSTOM_COMPILE_COMMAND="make update-requirements"
update-requirements: $(VENV_ACTIVATE)
update-requirements: ## Update all requirements to latest versions.
	$(PIP_COMPILE) --upgrade --output-file=requirements-dev.txt requirements.in requirements-dev.in
	$(PIP_COMPILE) --upgrade --output-file=requirements.txt requirements.in
	$(call sync_dev_requirements)

.PHONY: check-requirements
check-requirements: export CUSTOM_COMPILE_COMMAND="make update-requirements"
check-requirements: sync-dev-requirements
check-requirements: ## Check if requirements*.txt files are up-to-date.
	@echo "Checking requirements..."
	$(eval REQ_TEMPDIR := $(shell mktemp -d))
	$(PIP_COMPILE) --output-file=$(REQ_TEMPDIR)/requirements-dev.txt requirements.in requirements-dev.in
	$(PIP_COMPILE) --output-file=$(REQ_TEMPDIR)/requirements.txt requirements.in
	@diff requirements-dev.txt $(REQ_TEMPDIR)/requirements-dev.txt && \
	diff requirements.txt $(REQ_TEMPDIR)/requirements.txt || \
	{ echo "Requirements are not up-to-date: run 'make update-requirements' to fix them."; \
	echo "Expected requirements.txt:"; cat $(REQ_TEMPDIR)/requirements.txt; \
	echo "Expected requirements-dev.txt:"; cat $(REQ_TEMPDIR)/requirements-dev.txt; \
	exit 1; }

### Bootstraps virtual environment for first use.
$(VENV_ACTIVATE):
	python3 -m pip install --user virtualenv
	python3 -m virtualenv --python /pyenv/shims/python$(PYTHON_VERSION) $(VENV)
	$(PIP) install -U pip pip-tools

.PHONY: check-cc
check-cc: sync-dev-requirements  ## Check if this project needs to be synced with the cookiecutter that generated it.
	$(SOURCE_VENV) ./bin/check_cc

.PHONY: update-cc
update-cc: sync-dev-requirements
update-cc: ## Update the project to the latest version of the cookiecutter
	$(CRUFT) update --not-strict -c master

.PHONY: update-snapshots
update-snapshots: ## Update pytest snapshots
update-snapshots: sync-dev-requirements
	$(PYTHON) -m pytest -v --snapshot-update src tests

.PHONY: dev-shell
dev-shell: sync-dev-requirements  ## Launch a bash shell with the python environment for this project. If docker is enabled, this launches a shell inside the container.
	($(SOURCE_VENV) bash)

.PHONY: clean
clean: ## Remove build artifacts.
	$(RM) -r build/*
	$(RM) MANIFEST
	$(RM) -r dist/*
	$(RM) -r .pytest_cache
	$(RM) -r .coverage
	$(RM) -r .mypy_cache
	$(RM) -r $(package).egg-info
	$(RM) -r $(VENV)
	$(RM) -r .tox
	find . -type d -name '__pycache__' -exec rm -rf {} +
	find . -type f -name '*.pyc' -exec rm -rf {} +
