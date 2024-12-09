binaries=htmlcov .coverage

.PHONY: clean test cover

default: test coverage

clean:
	rm -rf $(binaries)

test:
		coverage run -m pytest tests

coverage:
		coverage report
