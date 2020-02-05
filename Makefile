test:
	pytest -vv

format:
	isort -rc .
	black .

lint:
	mypy .
	flake8 .
