
.PHONY: help venv

VENV_NAME=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python
SPHINX-APIDOC=${VENV_NAME}/bin/sphinx-apidoc
SPHINX-BUILD=${VENV_NAME}/bin/sphinx-build

SHELL:=/bin/bash

.DEFAULT: help
help: 
	@echo Targets: venv, clean-venv, lint, clean, test

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} setup.py develop
	touch $(VENV_NAME)/bin/activate

dev: venv $(VENV_NAME)/.dev
$(VENV_NAME)/.dev:
	${PYTHON} -m pip install -e .[dev]
	touch $(VENV_NAME)/.dev

test: dev
	 ${PYTHON} -m unittest discover tests/

doc: dev
	rm -rf docs/*
	${SPHINX-APIDOC} -o sphinx/ firstline/ --force
	${SPHINX-BUILD} sphinx/ sphinx/_build/
	find sphinx/_build/ -name "*.html" -type f -exec sh -c  'pandoc --lua-filter=sphinx/pandoc/links-to-rest.lua  "$${0}" -o "./docs/$$(basename $${0%.html}.rst)"' {} \;

clean: clean-venv clean-dist clean-pyc clean-tests clean-doc

clean-doc:
	rm -rf sphinx/_build/*
	rm -rf docs/*
	find sphinx/ -name *.rst ! -name index.rst -type f -exec rm {} \;

clean-tests:
	rm -f tests/test.log

clean-venv:
	rm -rf $(VENV_NAME) 

clean-dist:
	rm -rf build/ dist/ *.egg-info *.egg

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +

