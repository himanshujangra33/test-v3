PYTHON=python3

install:
	$(PYTHON) -m venv .venv
	. .venv/bin/activate && pip install -r requirements.txt

run:
	bash ./start.sh

test:
	pytest tests/ -v --tb=short

seed:
	$(PYTHON) seed.py
