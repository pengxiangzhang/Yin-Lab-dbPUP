import gzip

from flask import Flask, url_for, redirect, request, send_from_directory, make_response
from flask import render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
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
    #app.config['TEMPLATES_AUTO_RELOAD'] = configs['development']['TEMPLATES_AUTO_RELOAD']

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

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

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
        row = {}
        amount_row = 0
        if family_id == 'all':
            records = charRecord.CharRecord.query.all()
            for record in records:
                amount_row += 1
                sub_row = []
                pdbSubLink = record.pdb.split(';')
                amount = len(pdbSubLink)
                for i in range(amount):
                    amount_row += 1
                    pdb_information = []
                    pdb_information.append(pdbSubLink[i])
                    pdb_information.append(pdbSubLink[i].split('[')[0])
                    sub_row.append(pdb_information)
                row[record.number] = sub_row

        else:
            records = charRecord.CharRecord.query.filter_by(family=family_id)
            for record in records:
                sub_row = []
                pdbSubLink = record.pdb.split(';')
                amount = len(pdbSubLink)
                for i in range(amount):
                    amount_row += 1
                    pdb_information = []
                    pdb_information.append(pdbSubLink[i])
                    pdb_information.append(pdbSubLink[i].split('[')[0])
                    sub_row.append(pdb_information)
                row[record.number] = sub_row

        return render_template("characteristic.html", records=records, rows = row)


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
            with open('static/materials/tree/' + family_id +'.json') as f:
                treeData = json.load(f)
                print(treeData)
        except Exception:
            treeData = None
            return render_template('tree.html', treeData = json.dumps(treeData))
    return render_template('tree.html', treeData = json.dumps(treeData))

@app.route("/family/<family_id>")
def family(family_id):
    amount = 0
    if family_id == 'FR1':
        amount = 3
    if family_id == 'FR2':
        amount = 1
    if family_id == 'FR3':
        amount = 1
    if family_id == 'FR4':
        amount = 1
    if family_id == 'HR1':
        amount = 1
    if family_id == 'HR2':
        amount = 1
    if family_id == 'HR3':
        amount = 4
    if family_id == 'HR4':
        amount = 2
    if family_id == 'HR5':
        amount = 2
    if family_id == 'HR6':
        amount = 1
    if family_id == 'HR7':
        amount = 4
    if family_id == 'HR8':
        amount = 2
    if family_id == 'IR1':
        amount = 1
    if family_id == 'IR2':
        amount = 1
    if family_id == 'NCR1':
        amount = 1
    if family_id == 'OR1':
        amount = 1
    if family_id == 'OR2':
        amount = 1
    if family_id == 'OR3':
        amount = 1
    if family_id == 'OR4':
        amount = 1
    if family_id == 'OR5':
        amount = 1
    if family_id == 'OR6':
        amount = 1
    if family_id == 'OR7':
        amount = 1
    if family_id == 'OR8':
        amount = 2
    if family_id == 'OR9':
        amount = 1
    if family_id == 'OR10':
        amount = 1

    return render_template('family.html', family_id=family_id, amount = amount)

@app.route("/subfamily/<family_id>")
def subfamily(family_id):
    return render_template('subfamily.html', family_id=family_id)

@app.route("/network/<family_id>",  methods=['GET', 'POST'])
def network(family_id):
    if request.method == 'POST':
        msg = request.get_data()
        node_name = msg.decode("UTF-8")
        try:
            with open('static/materials/network_data/uniprot_ssn/' + family_id + '.cyjs') as f:
                networkData = json.load(f)
                del networkData["format_version"]
                del networkData["generated_by"]
                del networkData["target_cytoscapejs_version"]
                del networkData['data']

                for node in networkData['elements']['nodes']:
                    if '_' in family_id:
                        node['data']['fill_color'] = node['data']['fill']
                    else:
                        node['data']['fill_color'] = node['data']['node']
                    del node['data']['node']
                    del node['data']['border']
                    del node['data']['shared_name']
                    del node['data']['SUID']
                    del node['data']['fill']
                    del node['data']['selected']
                    del node['selected']
                    names = node['data']['name'].split('|')
                    if (len(names) > 3):
                        node['data']['name'] = names[2]
                        node['data']['href'] = '/detail/' + names[2]
                        if names[2] == node_name:
                            node['data']['fill_color'] = '#92d9d0'

                    else:
                        node['data']['name'] = names[1]
                        node['data']['href'] = '/detail/' + names[1]
                        if node['data']['name'] == node_name:
                            node['data']['fill_color'] = '#92d9d0'

                    data = []
                    data.append(node['data']['id'])
                    data.append(node['data']['fill_color'])
                    data.append(node['data']['name'])
                    data.append(node['data']['href'])
                    node['data'] = data


                for edge in networkData['elements']['edges']:
                    del edge['selected']
                    del edge['data']['shared_name']
                    del edge['data']['shared_interaction']
                    del edge['data']['name']
                    del edge['data']['interaction']
                    del edge['data']['Column_3']
                    del edge['data']['SUID']
                    del edge['data']['selected']
        except Exception:
            print("error")

        return networkData

    try:
        with open('static/materials/network_data/uniprot_ssn/' + family_id + '.cyjs') as f:
            networkData = json.load(f)
            del networkData["format_version"]
            del networkData["generated_by"]
            del networkData["target_cytoscapejs_version"]
            del networkData['data']

            for node in networkData['elements']['nodes']:
                if '_' in family_id:

                    node['data']['fill_color'] = node['data']['fill']
                else:
                    node['data']['fill_color'] = node['data']['node']

                del node['data']['node']
                del node['data']['border']
                del node['data']['shared_name']
                del node['data']['SUID']
                del node['data']['fill']
                del node['data']['selected']
                del node['selected']
                names = node['data']['name'].split('|')
                if (len(names) > 3):
                    node['data']['name'] = names[2]
                    node['data']['href'] = '/detail/' + names[2]
                else:
                    node['data']['name'] = names[1]
                    node['data']['href'] = '/detail/' + names[1]
                data = []
                data.append(node['data']['id'])

                data.append(node['data']['fill_color'])

                data.append(node['data']['name'])
                data.append(node['data']['href'])
                node['data'] = data

            for edge in networkData['elements']['edges']:
                del edge['selected']
                del edge['data']['shared_name']
                del edge['data']['shared_interaction']
                del edge['data']['name']
                del edge['data']['interaction']
                del edge['data']['Column_3']
                del edge['data']['SUID']
                del edge['data']['selected']

    except Exception:
            networkData = None

    return render_template('network.html', networkData = json.dumps(networkData))

@app.route("/classes/<class_id>")
def classes(class_id):
    return render_template('classes.html', class_id=class_id)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
