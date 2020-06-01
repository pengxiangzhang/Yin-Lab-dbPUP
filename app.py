from flask import Flask, url_for, redirect
from flask import render_template
import json

app = Flask(__name__, static_url_path='', static_folder='static/')
app.config['TEMPLATES_AUTO_RELOAD'] = True

# read configurations
with open('config.json') as json_file:
	configs = json.load(json_file)
	app.config['title'] = configs['website']['title']
	app.config['data_base_info'] = configs['database']

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/index.html')
def index_html():
	return redirect(url_for('index'))

@app.route('/work')
def work():
	return render_template('work.html')

@app.route('/work.html')
def work_html():
	return redirect(url_for('work'))