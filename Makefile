.PHONY: test utest clean

test:
	tox

utest:
	find . -name "*.py" | grep -v venv/ | grep -v .tox/ | entr -c pytest --ignore=tests/integration/  -s tests/

clean:
	rm -r .tox
	find . -name "*.pyc" -delete
	find . -name "__pycache__" | xargs rm -r

