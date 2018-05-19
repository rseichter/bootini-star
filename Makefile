PSETUP = python setup.py -q

help:
	@echo "PyPI targets  : sdist wheel pypi"
	@echo "Other targets : cov pretty"

clean:
	[ -d dist ] && rm -r dist

sdist:
	$(PSETUP) sdist

wheel:
	$(PSETUP) bdist_wheel

pypi:	sdist wheel
	@echo -e '# twine upload dist/*'

pretty:
	autopep8 -i bootini_star/*.py tests/*.py
