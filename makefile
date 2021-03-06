SOURCE_VENV=. venv/bin/activate
DIR_ARGS = app/ controllers/ data/ tests/ scripts/ utils/

venv: requirements.txt
	python3 -m venv venv
	$(SOURCE_VENV) && pip install -r requirements.txt

clean:
	rm -rf venv/

typehint:
	$(SOURCE_VENV) && mypy $(DIR_ARGS)

test_parallel: 
	$(SOURCE_VENV) && pytest -n auto tests/

test_simple: 
	$(SOURCE_VENV) && pytest tests/

lint: 
	$(SOURCE_VENV) && pylint $(DIR_ARGS)

format: 
	$(SOURCE_VENV) && black  $(DIR_ARGS)

coverage: 
	$(SOURCE_VENV) && pytest --cov-report term-missing --cov=.  tests/

coverage_parallel: 
	$(SOURCE_VENV) && pytest --cov-report term-missing --cov=. -n 2 tests/

start_production: 
	$(SOURCE_VENV) && gunicorn app.app:app --workers 12 -k uvicorn.workers.UvicornH11Worker --bind 0.0.0.0 

start_development: 
	$(SOURCE_VENV) && gunicorn app.app:app --workers 1 -k uvicorn.workers.UvicornH11Worker --bind 0.0.0.0 --reload

start_local: 
	$(SOURCE_VENV) && uvicorn app.app:app --reload

soft_checklist: typehint coverage lint  
hard_checklist: format lint typehint test coverage
