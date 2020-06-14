from flask import Flask, url_for, redirect
from flask import render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
#from models.record import Record
from models import charRecord, swiRecord, treRecord
import json

# Application configurations

app = Flask(__name__, static_url_path='/static')
md = Markdown(app, extensions=['fenced_code'])

# read configurations
with open('config.json') as json_file:
	configs = json.load(json_file)

	# web info
	app.config['title'] = configs['website']['title']
	app.config['TEMPLATES_AUTO_RELOAD'] = configs['development']['TEMPLATES_AUTO_RELOAD']

	# database
	connection_stat = "mysql+pymysql://" + configs['database']['username'] \
					+ ":" + configs['database']['password'] + "@" \
					+ configs['database']['hostname'] + "/" \
				    + configs['database']['db_name']
	print("Load connection information:")
	print(connection_stat)
	app.config['SQLALCHEMY_DATABASE_URI'] = connection_stat

dtbs = SQLAlchemy(app)

# routing

@app.route('/')
def index():
	c = open('content/about.md', 'r').read()
	return render_template('index.html', content = c)

@app.route('/characteristic')
def characteristic():
	records = charRecord.CharRecord.query.all()
	return render_template('characteristic.html', records = records)

@app.route('/swissport')
def swissport():
	records = swiRecord.SwiRecord.query.all() 
	print(records)
	return render_template("swissport.html", records=records)

@app.route('/trembl')
def trembl():
        records = treRecord.TreRecord.query.all() 
        return render_template("trembl.html", records=records)


@app.route('/user/<username>/<firstname>')
def newUser(username, firstname):
	u = User(lastname=username, firstname=firstname)
	dtbs.session.add(u)
	dtbs.session.commit()
	return "inserted!"