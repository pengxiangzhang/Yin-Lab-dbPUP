from flask import Flask, url_for, redirect, request
from flask import render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
# from models.record import Record
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
    return render_template('index.html', content=c)


@app.route('/characteristic/<family_id>', methods=['GET', 'POST'])
def characteristic(family_id):
    if request.method == 'POST':
        msg = request.get_data()
        family_id = json.loads(msg)['family_id']
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)

        return render_template('swissport.html', records=records)
    else:
        amount = 0
        pdbSubLink = 0
        pdbSplitLink = 0
        if family_id == 'all':
            records = charRecord.CharRecord.query.all()
        else:
            records = charRecord.CharRecord.query.filter_by(family=family_id)
            for record in records:
                pdbSubLink = record.pdb.split(';')
                amount = len(pdbSubLink)
                pdbSplitLink = []
                for i in range(amount):
                    pdbSplitLink.append(pdbSubLink[i].split('[')[0])

        return render_template("characteristic.html", records=records, amount = amount, pdbSubLink = pdbSubLink, pdbSplitLink = pdbSplitLink )


@app.route('/swissport/<family_id>', methods=['GET', 'POST'])
def swissport(family_id):
    if family_id == 'all':
        records = swiRecord.SwiRecord.query.all()
    else:
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)
    return render_template('swissport.html', records = records)

@app.route('/trembl/<family_id>', methods=['GET', 'POST'])
def trembl(family_id):
    if family_id == 'all':
        records = treRecord.TreRecord.query.all()
    else:
        records = treRecord.TreRecord.query.filter_by(family=family_id)
    return render_template("trembl.html", records=records)

@app.route('/user/<username>/<firstname>')
def newUser(username, firstname):
    u = User(lastname=username, firstname=firstname)
    dtbs.session.add(u)
    dtbs.session.commit()
    return "inserted!"


@app.route("/detail/<unid>")
def detail(unid):
    records = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records =  treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        seq = None
    else:
        seq = records.seq
    return render_template('detail.html', seq=seq, unid=unid)

@app.route("/tree/<family_id>")
def tree(family_id):
    if family_id == 'all':
        treeData = None
    else:
        try:
            with open('data' + str(family_id) + '.json') as f:
                treeData = json.load(f)
        except Exception:
            treeData = None
            return render_template('tree.html', treeData = json.dumps(treeData))
    return render_template('tree.html', treeData = json.dumps(treeData))

@app.route("/family/<family_id>")
def family(family_id):
    return render_template('family.html', family_id=family_id)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
