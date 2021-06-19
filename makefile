.ONESHELL:
development: app.py
	export FLASK_APP=app.py
	export FLASK_DEBUG=1
	export FLASK_ENV=development
	flask run --host=0.0.0.0

.ONESHELL:
production: app.py
	export FLASK_DEBUG=1
	export FLASK_APP=app.py
	flask run --host=0.0.0.0
