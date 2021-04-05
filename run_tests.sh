# Just for now, we upgrade that after
coverage run --source=. -m unittest discover -s tests/
coverage report
coverage html