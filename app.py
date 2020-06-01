from flask import Flask, url_for, redirect
from flask import render_template
import json
from flaskext.markdown import Markdown
app = Flask(__name__, static_url_path='/static')
md = Markdown(app, extensions=['fenced_code'])
app.config['TEMPLATES_AUTO_RELOAD'] = True

# read configurations
with open('config.json') as json_file:
	configs = json.load(json_file)
	app.config['title'] = configs['website']['title']
	app.config['data_base_info'] = configs['database']

@app.route('/')
def index():
	c = open('content/about.md', 'r').read()
	return render_template('index.html', content = c)

@app.route('/work')
def work():
	return render_template('work.html')