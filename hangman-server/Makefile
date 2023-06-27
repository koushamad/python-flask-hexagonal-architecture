install:
	virtualenv --python=python3 venv; source venv/bin/activate; pip install -r requirements.txt

test:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)/src"; source venv/bin/activate; python -m pytest tests -v

style:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)/src"; source venv/bin/activate; flake8 src; flake8 tests

style-fix:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)/src"; source venv/bin/activate; black src; black tests

security:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)/src"; source venv/bin/activate; bandit -r src

start:
	export PYTHONPATH="${PYTHONPATH}:$(shell pwd)/src"; source venv/bin/activate; python src/server.py
