from flask import Flask, url_for, redirect
from flask import render_template
app = Flask(__name__, static_url_path='', static_folder='static/')
app.config['TEMPLATES_AUTO_RELOAD'] = True

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