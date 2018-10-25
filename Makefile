init:
	pipenv install
	pipenv shell

test:
	echo "TESTING"

.PHONY: init test
