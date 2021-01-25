# https://blog.horejsek.com/makefile-with-python/

.PHONY: help venv

VENV_NAME=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate
PYTHON=${VENV_NAME}/bin/python3

.DEFAULT: help
help: 
	@echo Targets: venv, clean-venv, lint, clean, clean-pyc, dist, distclean

venv: $(VENV_NAME)/bin/activate
$(VENV_NAME)/bin/activate: setup.py
	test -d $(VENV_NAME) || virtualenv -p python3 $(VENV_NAME)
	${PYTHON} setup.py develop
	touch $(VENV_NAME)/bin/activate

clean-venv:
	rm -rf $(VENV_NAME) 

dist:
	$(PYTHON) setup.py sdist 

distclean:
	rm -rf build/ dist/ *.egg-info *.egg

lint: venv
	${PYTHON} -m pylint
	${PYTHON} -m mypy

clean: clean-venv distclean clean-pyc

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +


