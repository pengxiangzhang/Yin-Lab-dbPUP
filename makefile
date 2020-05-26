development: app.py
	export FLASK_ENV=development
	flask run
	
production: app.py
	export FLASK_APP=app.py
	flask run --host=0.0.0.0