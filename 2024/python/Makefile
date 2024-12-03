binaries=htmlcov

.PHONY: clean test cover

default: test coverage

clean:
	rm -rf $(binaries)


test:
		pytest

coverage:
		coverage report
