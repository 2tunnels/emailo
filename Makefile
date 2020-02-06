test:
	pytest -vv --cov=emailo

format:
	isort -rc .
	black .

lint:
	mypy .
	flake8 .
