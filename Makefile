init:
	poetry install

test:
	poetry run pytest


test-nox:
	poetry run nox

test-nox-oldest:
	poetry run nox --session "tests-3.8(pyyaml=True, django='3.2')"

publish:
	poetry publish --build

cs-test:
	poetry run poetry run python cs_test/manage.py runserver

cs-test-migrate:
	poetry run poetry run python cs_test/manage.py migrate

cs-test-shell:
	poetry run poetry run python cs_test/manage.py shell