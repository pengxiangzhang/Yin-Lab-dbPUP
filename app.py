from data_analyzer import Data_analyzer
from flask import Flask, request, send_from_directory, flash, render_template, abort, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import InputForm
from models import charRecord, swiRecord, treRecord
import markdown, json, glob, os
from datetime import datetime
import pandas as pd

# Application configurations

app = Flask(__name__, static_url_path='/dbpup/static')

# read configurations
with open('config.json') as json_file:
    configs = json.load(json_file)

    # web info
    app.config['title'] = configs['website']['title']
    app.config['FullName'] = configs['website']['FullName']
    app.config['keywords'] = configs['website']['keywords']
    app.config['RECAPTCHA_PUBLIC_KEY'] = configs['recaptcha']['RECAPTCHA_PUBLIC_KEY']
    app.config['RECAPTCHA_PRIVATE_KEY'] = configs['recaptcha']['RECAPTCHA_PRIVATE_KEY']
    app.secret_key = configs['website']['key']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
def hello():
    return redirect("/dbpup/", code=301)


# Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/dbpup/')
def index():
    name = app.config['FullName'] + " (" + app.config['title'] + ")"
    title = ""
    c = open('content/Homepage.md', 'r', encoding='utf-8').read()
    return render_template('index.html', content=to_md(c), description="", title=title, name=name)


@app.route("/dbpup/about")
def about():
    name = ""
    title = "About - "
    try:
        with open('content/About.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        pass
    return render_template('main.html', content=to_md(c), description="", title=title, name=name)


@app.route('/dbpup/help')
def help():
    name = ""
    title = "Help - "
    try:
        with open('content/Helppage.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        pass
    return render_template('main.html', content=to_md(c), description="", title=title, name=name)


@app.route('/dbpup/statistics')
def statistics():
    name = ""
    title = "Statistics - "
    try:
        with open('content/Statistics_page.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        pass
    return render_template('main.html', content=to_md(c), description="", title=title, name=name)


@app.route("/dbpup/download")
def download():
    name = ""
    title = "Download - "
    try:
        with open('content/download.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        pass
    return render_template('main.html', content=to_md(c), description="", title=title, name=name)


@app.route('/dbpup/evidence/all')
def evidence():
    title = "Evidence - "
    name = "Evidence"
    records = charRecord.CharRecord.query.all()
    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()
    sub, prod = data_analyzer.substrate_product_split()

    return render_template("evidence.html", records=records, rows=pdb_row, ec=ec_link, sub=sub, product=prod,
                           description="", title=title, name=name)


@app.route('/dbpup/swissport/<family_id>', methods=['GET', 'POST'])
def swissport(family_id):
    title = "Swiss-Prot - " + family_id + " - "
    subfamily = False
    if '_' in family_id:
        subfamily = True
        records = swiRecord.SwiRecord.query.filter_by(family=family_id)
    else:
        allfamily_id = family_id + "%"
        records = swiRecord.SwiRecord.query.filter(swiRecord.SwiRecord.family.like(allfamily_id))

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()

    found = False
    for record in records:
        found = True
        break
    if not found:
        abort(404)
    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            c.close()
    except Exception:
        name = family_id

    return render_template('swissport.html', family_id=family_id, records=records, ec=ec_link, rows=pdb_row,
                           description="", title=title,
                           name=name, subfamily=subfamily)


@app.route('/dbpup/Trembl/<family_id>', methods=['GET', 'POST'])
def trembl(family_id):
    title = "TrEMBL - " + family_id + " - "
    name = family_id
    subfamily = False
    if '_' in family_id:
        subfamily = True
        records = treRecord.TreRecord.query.filter_by(family=family_id)
    else:
        newfamily_id = family_id + "%"
        records = treRecord.TreRecord.query.filter(treRecord.TreRecord.family.like(newfamily_id))

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()

    found = False
    for record in records:
        found = True
        break
    if not found:
        abort(404)
    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            c.close()
    except Exception:
        name = family_id
    return render_template("trembl.html", family_id=family_id, records=records, ec=ec_link, rows=pdb_row,
                           description="", title=title, name=name, subfamily=subfamily)


@app.route("/dbpup/detail/<unid>")
def detail(unid):
    title = "Sequence - " + unid + " - "
    name = "Sequence for " + unid
    records = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records = treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        records = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
    if records is None:
        abort(404)
    else:
        seq = records.seq
    return render_template('detail.html', seq=seq, unid=unid, description="", title=title, name=name)


@app.route("/dbpup/tree/<family_id>")
def tree(family_id):
    title = "Tree - " + family_id + " - "
    name = family_id
    try:
        with open('content/tree_page.md', encoding='utf-8') as c:
            c = c.read()
    except Exception:
        pass
    try:
        with open('static/materials/tree/' + family_id + '.json') as f:
            treeData = json.load(f)
    except Exception:
        abort(404)

    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as n:
            name = get_title(n)
            n.close()
    except Exception:
        name = family_id
    return render_template('tree.html', content=to_md(c), family_id=family_id, treeData=json.dumps(treeData),
                           description="", title=title, name=name)


@app.route("/dbpup/family/<family_id>")
def family(family_id):
    title = "Family - " + family_id + " - "
    amount = 0
    name = ""
    if not is_family(family_id):
        abort(404)
    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        c = open('content/nothing.md', 'r', encoding='utf-8').read()
        name = "Subfamily for " + family_id

    if family_id == 'OR4':
        amount = 4
    elif family_id == 'OR5':
        amount = 12
    elif family_id == 'OR7':
        amount = 5
    elif family_id == 'OR8':
        amount = 14
    elif family_id == 'OR9':
        amount = 7
    elif family_id == 'FR1':
        amount = 4
    elif family_id == 'FR3':
        amount = 4
    elif family_id == 'FR4':
        amount = 4
    elif family_id == 'HR2':
        amount = 3
    elif family_id == 'HR3':
        amount = 8
    elif family_id == 'HR4':
        amount = 11
    elif family_id == 'HR5':
        amount = 5
    elif family_id == 'HR7':
        amount = 5
    elif family_id == 'HR8':
        amount = 6
    elif family_id == 'UC1':
        amount = 13
    elif family_id == 'UC2':
        amount = 8
    return render_template('family.html', family_id=family_id, amount=amount, content=to_md(c), description="",
                           title=title, name=name)


@app.route("/dbpup/subfamily/<family_id>")
def subfamily(family_id):
    title = "Subfamily - " + family_id + " - "
    if not is_subfamily(family_id):
        abort(404)
    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        c = open('content/nothing.md', 'r', encoding='utf-8').read()
        name = "Subfamily for " + family_id
    return render_template('subfamily.html', content=to_md(c), family_id=family_id, description="", title=title,
                           name=name)


@app.route("/dbpup/network/<family_id>")
def network(family_id):
    title = "Network - " + family_id + " - "
    name = family_id
    mainfile = (glob.glob('static/images/SSN_figures/' + family_id + '.jpg'))
    subfile = (glob.glob('static/images/SSN_figures/' + family_id + '_?.jpg'))
    if subfile == []:
        subfile = (glob.glob('static/images/SSN_figures/' + family_id + '_??.jpg'))
    if subfile == [] and mainfile == []:
        abort(404)
    try:
        with open('content/ssn_page.md', encoding='utf-8') as c:
            c = c.read()
    except Exception:
        abort(404)
    finalfile = [s[26:][:-4] for s in subfile]
    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as n:
            name = get_title(n)
            n.close()
    except Exception:
        name = family_id
    return render_template('network.html', content=to_md(c), family_id=family_id, description="", finalfile=finalfile,
                           title=title, name=name)


@app.route("/dbpup/classes/<class_id>")
def classes(class_id):
    title = "Classes - " + class_id + " - "
    name = ""
    amount = 0
    try:
        with open('content/class_' + class_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        c = open('content/nothing.md', 'r', encoding='utf-8').read()
        name = "class_id"

    if class_id == 'ORs':
        amount = 9
    elif class_id == 'FRs':
        amount = 4
    elif class_id == 'HRs':
        amount = 8
    elif class_id == 'NCRs':
        amount = 1
    elif class_id == 'IRs':
        amount = 2
    elif class_id == 'SRs':
        amount = 0
    elif class_id == 'TRs':
        amount = 0
    elif class_id == 'UCs':
        amount = 2
    else:
        abort(404)

    return render_template('classes.html', class_id=class_id, content=to_md(c), description="", title=title, name=name,
                           amount=amount)


@app.route("/dbpup/blast", methods=["GET", "POST"])
def blast():
    form = InputForm()
    title = "Blast - "
    try:
        with open('content/blast_page.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        abort(404)
    if request.method == 'POST':
        sequence = request.form.get('id_sequences')
        file = request.form.get('id_file_text')
        function = request.form.get('job')
        print(file)
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('blast.html', content=to_md(c), name=name, form=form, title=title, description="")
        elif sequence == "" and file == "":
            flash('You need to at least have one input.')
            return render_template('blast.html', content=to_md(c), name=name, form=form, title=title, description="")
        elif sequence != "" and file != "":
            flash('You can only have one input.')
            return render_template('blast.html', content=to_md(c), name=name, form=form, title=title, description="")
        else:
            if sequence != "" and file == "":
                query = sequence
            elif sequence == '' and file != '':
                query = file
            if function == 'blastp':
                records = blastp(query)
            elif function == 'blastx':
                records = blastx(query)
            return render_template('result_blastp.html', records=records, title=title, description="")

    elif request.method == 'GET':
        return render_template('blast.html', content=to_md(c), name=name, form=form, title=title, description="")


def to_md(content):
    return markdown.markdown(content, extensions=['extra', 'toc', 'smarty', 'sane_lists', 'pymdownx.mark'])


@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}


def get_title(file):
    return file.readline()[2:]


subfamilyfile = open("static/materials/subfamily.txt", "r")
subfamily_list = (subfamilyfile.readline().split())
subfamilyfile.close()
familyfile = open("static/materials/family.txt", "r")
family_list = (familyfile.readline().split())
familyfile.close()


def is_subfamily(family_id):
    if family_id in subfamily_list:
        return True
    else:
        return False


def is_family(family_id):
    if family_id in family_list:
        return True
    else:
        return False


def blastp(query):
    with open('pup_blastp/search.fsa', 'w') as f:
        f.writelines(query)
    command = "./blast/blastp -db pup_blastp/PUP_db -query pup_blastp/search.fsa -out pup_blastp/results.blast -outfmt 6 -evalue 1e-5 -num_threads 2"
    # command = "./blast/blastp -db pup_blastp/PUP_db -query " + query + " -out pup_blastp/results.blast -outfmt 6 -evalue 1e-5 -num_threads 4"
    os.system(command)

    with open('pup_blastp/results.blast', 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            return []

    data = pd.read_csv('pup_blastp/results.blast', sep="\t", header=None)
    index = 0
    processed_blastp = []
    for unid in data[1]:
        char_record = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
        swis_record = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
        trem_record = treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
        if char_record != None:
            char_result = []
            char_result.append(data[0][index])
            char_result.append(unid)
            char_result.append(char_record.family)
            char_result.append(data[2][index])
            char_result.append(data[10][index])
            char_result.append(char_record.protein_name)
            char_result.append(char_record.strain)
            char_result.append("")
            processed_blastp.append(char_result)
        if swis_record != None:
            swis_result = []
            swis_result.append(data[0][index])
            swis_result.append(unid)
            swis_result.append(swis_record.family)
            swis_result.append(data[2][index])
            swis_result.append(data[10][index])
            swis_result.append(swis_record.protein_enzyme)
            swis_result.append(swis_record.strain)
            swis_result.append(swis_record.web_id)
            processed_blastp.append(swis_result)
        if trem_record != None:
            trem_result = []
            trem_result.append(data[0][index])
            trem_result.append(unid)
            trem_result.append(trem_record.family)
            trem_result.append(data[2][index])
            trem_result.append(data[10][index])
            trem_result.append(trem_record.protein_enzyme)
            trem_result.append(trem_record.strain)
            trem_result.append(trem_record.web_id)
            processed_blastp.append(trem_result)

        index += 1
    # for item in processed_blastp:
    #     print(item)
    return processed_blastp

def blastx(query):
    with open('pup_blastp/search.fsa', 'w') as f:
        f.writelines(query)
    command = "./blast/blastp -db pup_blastp/PUP_db -query pup_blastx/search.fsa -out pup_blastx/results.blast -outfmt 6 -evalue 1e-5 -num_threads 2"
    os.system(command)

    with open('pup_blastp/results.blast', 'r') as f:
        data = f.readlines()
        if len(data) == 0:
            return []

    data = pd.read_csv('pup_blastp/results.blast', sep="\t", header=None)
    index = 0
    processed_blastx = []
    for unid in data[1]:
        char_record = charRecord.CharRecord.query.filter_by(uniq_id=unid).first()
        swis_record = swiRecord.SwiRecord.query.filter_by(uniq_id=unid).first()
        trem_record = treRecord.TreRecord.query.filter_by(uniq_id=unid).first()
        if char_record != None:
            char_result = []
            char_result.append(data[0][index])
            char_result.append(unid)
            char_result.append(char_record.family)
            char_result.append(data[2][index])
            char_result.append(data[10][index])
            char_result.append(char_record.protein_name)
            char_result.append(char_record.strain)
            char_result.append("")
            processed_blastx.append(char_result)
        if swis_record != None:
            swis_result = []
            swis_result.append(data[0][index])
            swis_result.append(unid)
            swis_result.append(swis_record.family)
            swis_result.append(data[2][index])
            swis_result.append(data[10][index])
            swis_result.append(swis_record.protein_enzyme)
            swis_result.append(swis_record.strain)
            swis_result.append(swis_record.web_id)
            processed_blastx.append(swis_result)
        if trem_record != None:
            trem_result = []
            trem_result.append(data[0][index])
            trem_result.append(unid)
            trem_result.append(trem_record.family)
            trem_result.append(data[2][index])
            trem_result.append(data[10][index])
            trem_result.append(trem_record.protein_enzyme)
            trem_result.append(trem_record.strain)
            trem_result.append(trem_record.web_id)
            processed_blastx.append(trem_result)

        index += 1

    return processed_blastx

if __name__ == "__main__":
    app.run(host='0.0.0.0')
