import json

from data_analyzer import Data_analyzer
from flask import Flask, request, send_from_directory, flash, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from forms import ContactForm, InputForm
from flask_mail import Mail, Message
from models import charRecord, swiRecord, treRecord
import markdown
# Application configurations

app = Flask(__name__, static_url_path='/static')

# read configurations
with open('config.json') as json_file:
    configs = json.load(json_file)

    # web info
    app.config['title'] = configs['website']['title']
    app.config['keywords'] = configs['website']['keywords']
    mail = Mail(app)
    app.config['MAIL_SERVER'] = configs['email']['MAIL_SERVER']
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
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


# Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/')
def index():
    name = app.config['title']
    title = ""
    c = open('content/nothing.md', 'r').read()
    return render_template('index.html', content=to_md(c), description="", title=title, name=name)


@app.route('/evidence/<family_id>', methods=['GET', 'POST'])
def evidence(family_id):
    title = " - Evidence"
    name = "Evidence"
    if request.method == 'POST':
        msg = request.get_data()
        family_id = json.loads(msg)['family_id']
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)

        return render_template('swissport.html', records=records, description="", title=title,name=name)
    else:
        if family_id == 'all':
            records = charRecord.CharRecord.query.all()
            data_analyzer = Data_analyzer(records)
            ec_link, pdb_row = data_analyzer.ec_pdb_split()
            sub, prod = data_analyzer.substrate_product_split()

        else:
            records = charRecord.CharRecord.query.filter_by(family=family_id)
            data_analyzer = Data_analyzer(records)
            ec_link, pdb_row = data_analyzer.ec_pdb_split()
            sub, prod = data_analyzer.substrate_product_split()
        return render_template("evidence.html", records=records, rows=pdb_row, ec=ec_link, sub=sub, product=prod,
                               description="", title=title,name=name)


@app.route('/swissport/<family_id>', methods=['GET', 'POST'])
def swissport(family_id):
    title = " - Swissport - " + family_id
    name=family_id
    subfamily=False
    if '_' in family_id:
        subfamily=True
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)
    else:
        family_id = family_id + "%"
        records = swiRecord.SwiRecord.query.filter(swiRecord.SwiRecord.family.like(family_id))

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()
    return render_template('swissport.html', records=records, ec=ec_link, rows=pdb_row, description="",title=title,name=name,subfamily=subfamily)


@app.route('/Trembl/<family_id>', methods=['GET', 'POST'])
def trembl(family_id):
    title = " - Trembl - " + family_id
    name=family_id
    subfamily=False
    if '_' in family_id:
        subfamily=True
        records = treRecord.TreRecord.query.filter_by(family=family_id)
    else:
        family_id = family_id + "%"
        records = treRecord.TreRecord.query.filter(treRecord.TreRecord.family.like(family_id))

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()
    return render_template("trembl.html",family_id=family_id, records=records, ec=ec_link, rows=pdb_row, description="",title=title,name=name,subfamily=subfamily)


@app.route("/detail/<unid>")
def detail(unid):
    title = " - Sequence - " + unid
    name = "Sequence for "+unid
    records = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records = treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        seq = None
    else:
        seq = records.seq
    return render_template('detail.html', seq=seq, unid=unid, description="", title=title,name=name)


@app.route("/tree/<family_id>")
def tree(family_id):
    title = " - Tree - " + family_id
    name =family_id
    if family_id == 'all':
        treeData = None
    else:
        try:
            with open('static/materials/tree/' + family_id + '.json') as f:
                treeData = json.load(f)
        except Exception:
            treeData = None
            return render_template('tree.html', treeData=json.dumps(treeData), description="")
    return render_template('tree.html', treeData=json.dumps(treeData), description="", title=title,name=name)


@app.route("/family/<family_id>")
def family(family_id):
    title = " - Family - " + family_id
    amount = 0
    name = ""
    c = open('content/nothing.md', 'r').read()
    if family_id == 'OR1':
        c = open('content/family_OR1.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 1"
    elif family_id == 'OR2':
        c = open('content/family_OR2.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 2"
    elif family_id == 'OR3':
        c = open('content/family_OR3.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 3"
    elif family_id == 'OR4':
        c = open('content/family_OR4.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 4"
    elif family_id == 'OR5':
        c = open('content/family_OR5.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 5"
    elif family_id == 'OR6':
        c = open('content/nothing.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 6"
    elif family_id == 'OR7':
        c = open('content/nothing.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 7"
    elif family_id == 'OR8':
        amount = 2
        c = open('content/nothing.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 8"
    elif family_id == 'OR9':
        c = open('content/nothing.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 9"
    elif family_id == 'OR10':
        c = open('content/nothing.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family 10"
    elif family_id == 'FR1':
        amount = 3
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'FR2':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'FR3':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'FR4':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR1':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR2':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR3':
        amount = 4
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR4':
        amount = 2
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR5':
        amount = 2
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR6':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR7':
        amount = 4
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'HR8':
        amount = 2
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'NCR1':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'IR1':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'IR2':
        c = open('content/nothing.md', 'r').read()
    elif family_id == 'SR':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'TR':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'UC1':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    elif family_id == 'UC2':
        c = open('content/nothing.md', 'r').read()
        name = "null"
    else:
        abort(404)
    
    return render_template('family.html', family_id=family_id, amount=amount, content=to_md(c), description="", title=title,name=name)


@app.route("/subfamily/<family_id>")
def subfamily(family_id):
    title = " - Subfamily - " + family_id
    name = "Subfamily for "+family_id
    return render_template('subfamily.html', family_id=family_id, description="", title=title,name=name)


@app.route("/network/<family_id>", methods=['GET', 'POST'])
def network(family_id):
    title = " - Network - " + family_id
    name = family_id
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
            print("error with network")

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
    
    return render_template('network.html', networkData=json.dumps(networkData), description="", title=title, name=name)


@app.route("/classes/<class_id>")
def classes(class_id):
    title = " - Classes - " + class_id
    name =""
    if class_id == 'HRs':
        c = open('content/class_HRs.md', 'r').read()
        name = "Hydrolysis Reactions (HRs) Family Classification"
    elif class_id == 'SRs':
        c = open('content/class_SRs.md', 'r').read()
        name = "Synthesis Reactions (SRs) Family Classification"
    elif class_id == 'FRs':
        c = open('content/class_FRs.md', 'r').read()
        name = "Functional Group Transfer Reactions (FRs) Family Classification"
    elif class_id == 'IRs':
        c = open('content/class_IRs.md', 'r').read()
        name = "Isomerization Reactions (IRs) Family Classification"
    elif class_id == 'NCRs':
        c = open('content/class_NCRs.md', 'r').read()
        name = "Non-hydrolytic Cleaving Reactions (NCRs) Family Classification"
    elif class_id == 'ORs':
        c = open('content/class_ORs.md', 'r').read()
        name = "Oxidation/Reduction Reactions (ORs) Family Classification"
    elif class_id == 'TRs':
        c = open('content/class_TRs.md', 'r').read()
        name = "Translocation Reactions (TRs) Family Classification"
    elif class_id == 'UCs':
        c = open('content/class_UCs.md', 'r').read()
        name = "Unclassified (UCs) Family Classification"
    else:
        abort(404)
    return render_template('classes.html', class_id=class_id, content=to_md(c), description="", title=title,name=name)


@app.route("/about", methods=["GET", "POST"])
def about():
    title = " - About us"
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('about.html', form=form, title=title, description="")
        else:
            name = request.form.get('name')
            email = request.form.get('email')
            subject = app.config['title'] + " Contact Form - " + request.form.get('subject')
            contant = request.form.get('message')
            msg = Message(subject, sender=app.config['MAIL_USERNAME'], recipients=[app.config['MAIL_USERNAME']],
                          reply_to=email)
            msg.body = "Name: " + name + "\nEmail: " + email + "\nSubject: " + subject + "\nMessage: " + contant
            mail.send(msg)
            return render_template('successful.html', title=" - Contact Form Submitted")
    elif request.method == 'GET':
        return render_template('about.html', form=form, title=title, description="")

@app.route("/download")
def download():
    title = " - Download"
    return render_template('download.html', title=title, description="", name="Download")
@app.route("/blastx", methods=["GET", "POST"])
def blastx():
    form = InputForm()
    title = " - Blastx"
    if request.method == 'POST':
        sequence = request.form.get('id_sequences')
        file = request.form.get('id_file_text')

        if sequence != "" and file == "":
            records = search_record(sequence)

        if len(records) > 0:
            data_analyzer = Data_analyzer(records)
            ec_link, pdb_row = data_analyzer.ec_pdb_split()
            return render_template("result_blastx.html", records=records, ec=ec_link, rows=pdb_row,
                                   description="",
                                   title=title)
        else:
            flash("The sequence is not in the database.")
            return render_template('blastx.html', form=form, title=title, description="")

    elif request.method == 'GET':
        return render_template('blastx.html', form=form, title=title, description="")


def search_record(sequence):
    sequence = sequence.split(" ")[-1]
    records = []

    char_records = charRecord.CharRecord.query.filter_by(seq=sequence)
    if char_records is not None:
        for record in char_records:
            records.append(record)

    tre_records = treRecord.TreRecord.query.filter_by(seq=sequence)
    if tre_records is not None:
        for record in tre_records:
            record.protein_name = record.protein_enzyme
            flag = 0
            for item in records:
                if item.protein_name == record.protein_name:
                    flag = 1
                    break
            if flag == 0:
                records.append(record)

    swi_records = swiRecord.SwiRecord.query.filter_by(seq=sequence)
    if swi_records is not None:
        for record in tre_records:
            record.protein_name = record.protein_enzyme
            flag = 0
            for item in records:
                if item.protein_name == record.protein_name:
                    flag = 1
                    break
            if flag == 0:
                records.append(record)

    return records
    
def to_md(content):
    return markdown.markdown(content, extensions=['extra', 'toc', 'smarty', 'sane_lists'])
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
