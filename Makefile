
init:
	pip install -r requirements.txt

test:
	PYTHONDONTWRITEBYTECODE=1 py.test --cov=hello tests

clean:
	find . -name "*.pyc" -delete
