.ONESHELL:
development: app.py
	. bioenv/bin/activate
	export FLASK_APP=app.py
	export FLASK_DEBUG=1
	export FLASK_ENV=development
	flask run -h localhost -p 5001

.ONESHELL:
production: app.py
	. venv/bin/activate
	export FLASK_APP=app.py
	flask run --host=0.0.0.0
