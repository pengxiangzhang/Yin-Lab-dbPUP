from flask import Flask, url_for, redirect
from flask import render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
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
class Record(dtbs.Model):
	__tablename__ = 'characterize'
	db = dtbs.Column(dtbs.String(30))
	uniq_id = dtbs.Column(dtbs.String(30), primary_key=True)
	entry = dtbs.Column(dtbs.String(30))
	protein = dtbs.Column(dtbs.String(30))
	organism = dtbs.Column(dtbs.String(40))
	organism_id = dtbs.Column(dtbs.Integer)
	gene = dtbs.Column(dtbs.String(30))
	protein_exist = dtbs.Column(dtbs.Integer)
	seq_versio = dtbs.Column(dtbs.Integer)
	seq = dtbs.Column(dtbs.VARCHAR(500))

@app.route('/')
def index():
	c = open('content/about.md', 'r').read()
	return render_template('index.html', content = c)


@app.route('/work')
def work():
	return render_template('work.html')

@app.route('/user/<username>/<firstname>')
def newUser(username, firstname):
	u = User(lastname=username, firstname=firstname)
	dtbs.session.add(u)
	dtbs.session.commit()
	return "inserted!"