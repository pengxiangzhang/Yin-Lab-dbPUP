import gzip

from flask import Flask, url_for, redirect, request, send_from_directory, make_response, flash, render_template
from flaskext.markdown import Markdown
from flask_sqlalchemy import SQLAlchemy
from models import charRecord, swiRecord, treRecord
import json
from flask_mail import Mail,Message
from forms import ContactForm

# Application configurations

app = Flask(__name__, static_url_path='/static')
md = Markdown(app, extensions=['fenced_code'])

# read configurations
with open('config.json') as json_file:
    configs = json.load(json_file)

	# web info
    app.config['title'] = configs['website']['title']
    app.config['keywords'] = configs['website']['keywords']
    #app.config['TEMPLATES_AUTO_RELOAD'] = configs['development']['TEMPLATES_AUTO_RELOAD']
    
    mail= Mail(app)
    app.config['MAIL_SERVER']=configs['email']['MAIL_SERVER']
    app.config['MAIL_PORT'] = configs['email']['MAIL_PORT']
    app.config['MAIL_USERNAME'] = configs['email']['MAIL_USERNAME']
    app.config['MAIL_PASSWORD'] = configs['email']['MAIL_PASSWORD']
    app.config['MAIL_USE_TLS'] = configs['email']['MAIL_USE_TLS']
    app.config['MAIL_USE_SSL'] = configs['email']['MAIL_USE_SSL']
    app.config['RECAPTCHA_PUBLIC_KEY'] = configs['recaptcha']['RECAPTCHA_PUBLIC_KEY']
    app.config['RECAPTCHA_PRIVATE_KEY'] = configs['recaptcha']['RECAPTCHA_PRIVATE_KEY']
    mail = Mail(app)
    app.secret_key = configs['website']['key']

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

# Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def index():
    ex_link =  'https://pubchem.ncbi.nlm.nih.gov/compound/phloretin;https://pubchem.ncbi.nlm.nih.gov/compound/4-Nitrophenyl%20sulfate'
    sub_links = ex_link.split(';')
    flag = len(sub_links)
    ex =  'phloretin;4-Nitrophenyl sulfate (quercetin/resveratrol/6-Hydroxyflavone)'
    subs = ex.split(';')
    length = len(subs)
    i = 0
    substrates = []
    while i < length:
        tuple = ["", "", ""]
        s_subs = subs[i].split('(')
        if len(s_subs) > 1:
            tuple[0] = s_subs[0]
            tuple[1] = "(" + s_subs[1]
        else:
            tuple[0] = s_subs[0]
        if i < flag:
            tuple[2] = sub_links[i]
        substrates.append(tuple)
        i += 1


    c = open('content/about.md', 'r').read()
    return render_template('index.html', content=c, description="")


@app.route('/evidence/<family_id>', methods=['GET', 'POST'])
def evidence(family_id):
    if request.method == 'POST':
        msg = request.get_data()
        family_id = json.loads(msg)['family_id']
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)

        return render_template('swissport.html', records=records,description="")
    else:
        row = {}
        ec_link = {}
        sub = {}
        prod = {}
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

                ec_sub_link = record.ec.split(';')
                ec = []
                for link in ec_sub_link:
                    ec.append(link)
                ec_link[record.number] = ec

                ex_link = record.pubchem_s #'https://pubchem.ncbi.nlm.nih.gov/compound/phloretin;https://pubchem.ncbi.nlm.nih.gov/compound/4-Nitrophenyl%20sulfate'
                sub_links = ex_link.split(';')
                flag = len(sub_links)
                ex = record.substrate #'phloretin;4-Nitrophenyl sulfate (quercetin/resveratrol/6-Hydroxyflavone); yes'
                subs = ex.split(';')
                length = len(subs)
                i = 0
                substrates = []
                while i < length:
                    tuple = ["", "", ""]
                    s_subs = subs[i].split('(')
                    if len(s_subs) > 1:
                        tuple[0] = s_subs[0]
                        tuple[1] = "(" + s_subs[1]
                    else:
                        tuple[0] = s_subs[0]
                    if i < flag:
                        tuple[2] = sub_links[i]
                    substrates.append(tuple)
                    i += 1
                sub[record.number] = substrates

                ex_link = record.pubchem_p
                sub_links = ex_link.split(';')
                flag = len(sub_links)
                ex = record.product
                subs = ex.split(';')
                length = len(subs)
                i = 0
                product = []
                while i < length:
                    tuple = ["", ""]
                    tuple[0] = subs[i]
                    if i < flag:
                        tuple[1] = sub_links[i]
                    product.append(tuple)
                    i += 1
                prod[record.number] = product



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

                ec_sub_link = record.ec.split(';')
                ec = []
                for link in ec_sub_link:
                    ec.append(link)
                ec_sub_link = record.ec.split(';')
                ec = []
                for link in ec_sub_link:
                    ec.append(link)
                ec_link[record.number] = ec

                ex_link = record.pubchem_s  #'https://pubchem.ncbi.nlm.nih.gov/compound/phloretin;https://pubchem.ncbi.nlm.nih.gov/compound/4-Nitrophenyl%20sulfate'
                sub_links = ex_link.split(';')
                flag = len(sub_links)
                ex = record.substrate #'phloretin;4-Nitrophenyl sulfate (quercetin/resveratrol/6-Hydroxyflavone); yes'
                subs = ex.split(';')
                length = len(subs)
                i = 0
                substrates = []
                while i < length:
                    tuple = ["", "", ""]
                    s_subs = subs[i].split('(')
                    if len(s_subs) > 1:
                        tuple[0] = s_subs[0]
                        tuple[1] = "(" + s_subs[1]
                    else:
                        tuple[0] = s_subs[0]
                    if i < flag:
                        tuple[2] = sub_links[i]
                    substrates.append(tuple)
                    i += 1
                sub[record.number] = substrates

                ex_link = record.pubchem_p
                sub_links = ex_link.split(';')
                flag = len(sub_links)
                ex = record.product
                subs = ex.split(';')
                length = len(subs)
                i = 0
                product = []
                while i < length:
                    tuple = ["", ""]
                    tuple[0] = subs[i]
                    if i < flag:
                        tuple[1] = sub_links[i]
                    product.append(tuple)
                    i += 1
                prod[record.number] = product
        return render_template("evidence.html", records=records, rows = row, ec = ec_link, sub = sub, product = prod, description="")


@app.route('/swissport/<family_id>', methods=['GET', 'POST'])
def swissport(family_id):
    fname = family_id
    ec_link = {}
    row = {}
    amount_row = 0
    if '_' in family_id:
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)
    else:
        family_id = family_id + "%"
        records = swiRecord.SwiRecord.query.filter(swiRecord.SwiRecord.family.like(family_id))

    for record in records:
        ec_sub_link = record.ec.split(';')
        ec = []
        for link in ec_sub_link:
            ec.append(link)
        ec_sub_link = record.ec.split(';')
        ec = []
        for link in ec_sub_link:
            ec.append(link)
        ec_link[record.number] = ec

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
    return render_template('swissport.html', records = records, ec = ec_link, rows = row, fname=fname, description="")

@app.route('/trembl/<family_id>', methods=['GET', 'POST'])
def trembl(family_id):
    ec_link = {}
    fname = family_id
    row = {}
    amount_row = 0
    if '_' in family_id:
        records = treRecord.TreRecord.query.filter_by(family=family_id)
    else:
        family_id = family_id + "%"
        records = treRecord.TreRecord.query.filter(treRecord.TreRecord.family.like(family_id))

    for record in records:
        ec_sub_link = record.ec.split(';')
        ec = []
        for link in ec_sub_link:
            ec.append(link)
        ec_sub_link = record.ec.split(';')
        ec = []
        for link in ec_sub_link:
            ec.append(link)
        ec_link[record.number] = ec

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

    return render_template("trembl.html", records=records, ec = ec_link, rows = row, fname=fname, description="")



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
    return render_template('detail.html', seq=seq, unid=unid, description="")

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
            return render_template('tree.html', treeData = json.dumps(treeData),description="")
    return render_template('tree.html', treeData = json.dumps(treeData),description="")

@app.route("/family/<family_id>")
def family(family_id):
    amount = 0
    if family_id == 'FR1':
        amount = 3
    if family_id == 'HR3':
        amount = 4
    if family_id == 'HR4':
        amount = 2
    if family_id == 'HR5':
        amount = 2
    if family_id == 'HR7':
        amount = 4
    if family_id == 'HR8':
        amount = 2
    if family_id == 'OR8':
        amount = 2
    c = open('content/family_OR1_test.md', 'r').read()

    return render_template('family.html', family_id=family_id, amount = amount, content = c, description="")

@app.route("/subfamily/<family_id>")
def subfamily(family_id):
    return render_template('subfamily.html', family_id=family_id, description="")

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

    return render_template('network.html', networkData = json.dumps(networkData),description="")

@app.route("/classes/<class_id>")
def classes(class_id):
    c = open('content/class_ORs.md', 'r').read()
    return render_template('classes.html', class_id=class_id, content = c,description="")
    

@app.route("/about", methods=["GET", "POST"])
def about():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
          flash('All fields are required.')
          return render_template('about.html', form = form)
        else:
            name=request.form.get('name')
            email = request.form.get('email')
            subject=app.config['title'] +" Contact Form - "+request.form.get('subject')
            contant = request.form.get('message')
            msg = Message(subject,sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']],reply_to=email)
            msg.body = "Name: "+name+"\nEmail: "+email+"\nSubject: "+subject+"\nMessage: "+contant
            mail.send(msg)
            return render_template('successful.html')
    elif request.method == 'GET':
        return render_template('about.html', form = form)


if __name__ == "__main__":
    app.run(host='0.0.0.0')