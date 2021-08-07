
.PHONY: help venv

VENV_NAME=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python
SPHINX-APIDOC=${VENV_NAME}/bin/sphinx-apidoc
SPHINX-BUILD=${VENV_NAME}/bin/sphinx-build

SHELL:=/bin/bash

.DEFAULT: help
help:
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
	| grep -v -- -- \
	| sed 'N;s/\n/###/' \
	| sed -n 's/^#: \(.*\)###\(.*\):.*/\2###\1/p' \
	| column -t  -s '###'	

#: Create virtualenv
venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install --upgrade pip
	${PYTHON} setup.py develop
	touch $(VENV_NAME)/bin/activate

#: Set up development environment
dev: venv $(VENV_NAME)/.dev
$(VENV_NAME)/.dev:
	${PYTHON} -m pip install -e .[dev]
	touch $(VENV_NAME)/.dev

#: Run tests
test: dev
	${PYTHON} -m unittest discover tests/

#: pylint
lint: dev
	${PYTHON} -m pylint firstline --exit-zero

#: Generate documentation
doc: dev
	rm -rf docs/*
	${SPHINX-APIDOC} -o sphinx/ firstline/ --force -T -M -t sphinx/_templates
	rm -rf sphinx/modules.rst
	${SPHINX-BUILD} sphinx/ sphinx/_build/ 
	find sphinx/_build/ -name "*.html" ! -name search.html -type f -exec sh -c  'pandoc -t gfm --lua-filter=sphinx/pandoc/links-to-markdown.lua  "$${0}" -o "./docs/$$(basename $${0%.html}.md)"' {} \;
	# Hack to remove double backticks in module names
	#sed -i 's/.``/./' docs/*.md

test-doc: dev
	rm -rf docs/*
	rm -rf sphinx/modules.rst
	${SPHINX-BUILD} sphinx/ sphinx/_build/ 
	find sphinx/_build/ -name "*.html" ! -name search.html -type f -exec sh -c  'pandoc -t gfm --lua-filter=sphinx/pandoc/links-to-markdown.lua  "$${0}" -o "./docs/$$(basename $${0%.html}.md)"' {} \;

#: Clean up generated files
clean: clean-venv clean-dist clean-pyc clean-tests # clean-doc

#: Clean up docs
clean-doc:
	rm -rf sphinx/_build/*
	rm -rf docs/*
	rm -rf docs/.doctrees
	find sphinx/ -name *.rst ! -name index.rst -type f -exec rm {} \;

#: Clean up tests
clean-tests:
	rm -f tests/test.log
	rm -f config.json

#: Clean up virtualenv
clean-venv:
	rm -rf $(VENV_NAME) 

clean-dist:
	rm -rf build/ dist/ *.egg-info *.egg

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +

