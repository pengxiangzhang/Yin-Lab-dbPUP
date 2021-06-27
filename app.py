from data_analyzer import Data_analyzer
from flask import Flask, request, send_from_directory, flash, render_template, abort
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_minify import minify
import markdown, json, glob, os, uuid, requests
from datetime import datetime
import pandas as pd

# Application configurations
app = Flask(__name__, static_url_path='/dbpup/static')
# cache = Cache(app, config={'CACHE_TYPE': 'FileSystemCache', 'CACHE_DIR': 'cache', 'CACHE_IGNORE_ERRORS': 'True',
#                           'CACHE_THRESHOLD': '500'})
# minify(app=app, html=True, js=True, cssless=True)

# read configurations
with open('config.json') as json_file:
    configs = json.load(json_file)

    # web info
    app.config['title'] = configs['website']['title']
    app.config['FullName'] = configs['website']['FullName']
    app.config['keywords'] = configs['website']['keywords']
    app.config['public_key'] = configs['captcha']['hcaptcha_public_key']
    app.config['private_key'] = configs['captcha']['hcaptcha_private_key']
    app.secret_key = configs['website']['key']

    # database
    connection_stat = "mysql+pymysql://" + configs['database']['username'] \
                      + ":" + configs['database']['password'] + "@" \
                      + configs['database']['hostname'] + "/" \
                      + configs['database']['db_name']
    print("Load connection information:")
    print(connection_stat)
    app.config['SQLALCHEMY_DATABASE_URI'] = connection_stat
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
dtbs = SQLAlchemy(app)


# routing
# Error Page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(410)
def page_not_found(e):
    return render_template('410.html'), 410


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


@app.route('/dbpup/')
def index():
    name = app.config['FullName'] + " (" + app.config['title'] + ")"
    title = "Database for Polyphenol Utilized Proteins from gut microbiota - "
    c = open('content/Homepage.md', 'r', encoding='utf-8').read()

    description = "dbPUP is the first exploratory database of polyphenol utilized proteins that have been experimentally validated to catalyze or modify a polyphenol substrate. The database contains 60 proteins from microbiome that characterized by heterologous or homologous expression with one or more specific polyphenol substrates. These data are recruited from scientific publications and search results on BRENDA. Each of the publications has been carefully vetted before inclusion in Characterized."
    return render_template('index.html', content=to_md(c), description=description, title=title, name=name)


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
    description = "dbPUP database team"
    return render_template('main.html', content=to_md(c), description=description, title=title, name=name)


@app.route("/dbpup/download")
def download():
    name = "Download"
    title = "Download - "
    try:
        with open('content/download.md', encoding='utf-8') as c:
            c = c.read()
    except Exception:
        pass
    description = "dbPUP data download"
    return render_template('main.html', content=to_md(c), description=description, title=title, name=name)

    
@app.route("/dbpup/uhgp_home")
def uhgp_home():
    name = "UHGP"
    title = "UHGP - "
    try:
        with open('content/uhgp_home.md', encoding='utf-8') as c:
            c = c.read()
    except Exception:
        pass
    description = "UHGP for dbPUP"
    return render_template('uhgp.html', content=to_md(c), description=description, title=title, name=name)


@app.route("/dbpup/cluster/<cluster_id>")
def cluster_detail(cluster_id):
    name = cluster_id
    title = "Cluster "+cluster_id+" - "
    try:
        with open('content/cluster/'+cluster_id+'.md', encoding='utf-8') as c:
            c = c.read()
    except Exception:
        abort(404)
    description = "Cluster Detail for "+cluster_id
    return render_template('main.html', content=to_md(c), description=description, title=title, name=name)


@app.route('/dbpup/uhgp/<name_id>')
def uhgp(name_id):
    if name_id == "Cluster":
        name = "UHGP " + name_id
        title = "UHGP " + name_id + " - "
        try:
            with open('content/uhgp.md', encoding='utf-8') as c:
                c = c.read()
        except Exception:
            pass
        description = "UHGP - " + name_id + " for dbPUP"
        records = ClusRecord.query.all()
        data_analyzer = Data_analyzer(records)
        pfam_dic = data_analyzer.pfam_dic()

        return render_template('uhgp_cluster.html', content=to_md(c), description=description, title=title, name=name,
                               records=records, pfam_dic = pfam_dic )
    else:
        name = "UHGP for Continent: " + name_id
        title = "UHGP for Continent: " + name_id + " - "
        try:
            with open('content/uhgp.md', encoding='utf-8') as c:
                c = c.read()
        except Exception:
            pass
        description = "UHGP - " + name_id + " for dbPUP"
        records = UhgpRecord.query.filter_by(continent=name_id)


        print("haha: "+name_id)
        return render_template('uhgp_continent.html', content=to_md(c), description=description, title=title, name=name,
                               records=records)


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
    description = "dbPUP is the first database to collect polyphenol utilization proteins that have been experimentally validated to catalyze or modify a polyphenol substrate. The database currently contains 60 proteins from gut microbiota that are manually curated from literature and enzyme database. These proteins have been characterized by different experimental approaches targeting one or more specific polyphenol substrates. These experimentally characterized proteins are also called seed proteins. Using these seed proteins, we also collected over 24,000 proteins that share conserved Pfam domains and significant sequence similarities with the seed proteins, and thus are potentially capable of metabolizing polyphenols. These proteins are also called computationally predicted proteins. All these seed proteins and computationally predicted proteins are compiled together and classified into protein families based on sequence homology and further categorized into classes according to EC numbers that the seed proteins have."
    return render_template('main.html', content=to_md(c), description=description, title=title, name=name)


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
    description = "Currently the dbPUP database contains, Characterized Proteins Statistics, General Statistics, Class Statistics. Database for Polyphenol Utilized Proteins from gut microbiota"
    return render_template('main.html', content=to_md(c), description=description, title=title, name=name)


@app.route('/dbpup/characterized')
def characterized():
    title = "Characterized - "
    name = "Characterized"
    records = CharRecord.query.all()
    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()
    sub, prod = data_analyzer.substrate_product_split()
    pfam_dic = data_analyzer.pfam_dic()

    description = "Characterization for Database for Polyphenol Utilized Proteins from gut microbiota"
    return render_template("characterized.html", records=records, rows=pdb_row, ec=ec_link, sub=sub, product=prod,
                           description=description, title=title, name=name, pfam_dic = pfam_dic)


@app.route('/dbpup/swissport/<family_id>', methods=['GET', 'POST'])
def swissport(family_id):
    title = "Swiss-Prot - " + family_id + " - "
    if is_family(family_id):
        allfamily_id = family_id + "%"
        records = SwiRecord.query.filter(SwiRecord.family.like(allfamily_id))
        subfamily = False
    elif is_subfamily(family_id):
        subfamily = True
        records = SwiRecord.query.filter_by(family=family_id)
    else:
        abort(404)

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()

    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            c.close()
    except Exception:
        name = family_id

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Swiss-Prot data for " + family_id
    return render_template('swissport.html', family_id=family_id, records=records, ec=ec_link, rows=pdb_row,
                           description=description, title=title,
                           name=name, subfamily=subfamily)


@app.route('/dbpup/Trembl/<family_id>', methods=['GET', 'POST'])
def trembl(family_id):
    title = "TrEMBL - " + family_id + " - "
    name = family_id
    if is_family(family_id):
        newfamily_id = family_id + "%"
        records = TreRecord.query.filter(TreRecord.family.like(newfamily_id))
        subfamily = False
    elif is_subfamily(family_id):
        records = TreRecord.query.filter_by(family=family_id)
        subfamily = True
    else:
        abort(404)

    data_analyzer = Data_analyzer(records)
    ec_link, pdb_row = data_analyzer.ec_pdb_split()

    try:
        with open('content/family_' + family_id + '.md', encoding='utf-8') as c:
            name = get_title(c)
            c.close()
    except Exception:
        name = family_id

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. TrEMBL data for " + family_id
    return render_template("trembl.html", family_id=family_id, records=records, ec=ec_link, rows=pdb_row,
                           description=description, title=title, name=name, subfamily=subfamily)


@app.route("/dbpup/detail/<mode>/<unid>")
def detail(mode, unid):
    title = "Sequence - " + unid + " - "
    name = "Sequence for " + unid
    if mode == "char":
        records = CharRecord.query.filter_by(uniq_id=unid).first()
    elif mode == "trembl":
        records = TreRecord.query.filter_by(uniq_id=unid).first()
    elif mode == "swiss":
        records = SwiRecord.query.filter_by(uniq_id=unid).first()
    elif mode == "uhpg":
        records = UhgpRecord.query.filter_by(gene_id=unid).first()
    elif mode == "cluster":
        records = ClusRecord.query.filter_by(gene_id=unid).first()
    else:
        abort(404)

    if records is None:
        abort(404)
    else:
        seq = records.seq

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Sequence for " + unid
    return render_template('detail.html', seq=seq, unid=unid, description=description, title=title, name=name)


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

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Tree for Swiss-Prot " + family_id
    return render_template('tree.html', content=to_md(c), family_id=family_id, treeData=json.dumps(treeData),
                           description=description, title=title, name=name)


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

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Family for " + family_id
    return render_template('family.html', family_id=family_id, amount=amount, content=to_md(c), description=description,
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
        c = open('content/redirect.md', 'r', encoding='utf-8').read()
        name = "Subfamily for " + family_id

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Subfamily for " + family_id
    return render_template('subfamily.html', content=to_md(c), family_id=family_id, description=description,
                           title=title,
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

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Subfamily for " + family_id
    return render_template('network.html', content=to_md(c), family_id=family_id, description=description,
                           finalfile=finalfile,
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

    description = "Database for Polyphenol Utilized Proteins from gut microbiota. Class for " + class_id
    return render_template('classes.html', class_id=class_id, content=to_md(c), description=description, title=title,
                           name=name,
                           amount=amount)


@app.route("/dbpup/blast", methods=["GET", "POST"])
def blast():
    title = "Blast - "
    description = "The Basic Local Alignment Search Tool (BLAST) finds regions of local similarity between sequences. The program compares nucleotide or protein sequences to dbPUP databases and calculates the statistical significance of matches. We provide an integrated BLAST service to find homologs in our dbPUP and infer a putative family with your protein sequences."
    try:
        with open('content/blast_page.md', encoding='utf-8') as c:
            name = get_title(c)
            next(c)
            c = c.read()
    except Exception:
        abort(404)
    if request.method == 'POST':
        records = []
        sequence = request.form.get('id_sequences')
        file = request.form.get('id_file_text')
        function = request.form.get('job')
        db = request.form.get('db')
        evalue = request.form.get('evalue')
        captcha_response = request.form['h-captcha-response']
        if sequence == "" and file == "":
            flash('You need to at least have one input.')
            return render_template('blast.html', content=to_md(c), name=name, title=title,
                                   description=description, site_key=app.config['public_key'])
        elif sequence != "" and file != "":
            flash('You can only have one input.')
            return render_template('blast.html', content=to_md(c), name=name, title=title,
                                   description=description, site_key=app.config['public_key'])
        elif function not in ["p","x"]:
            flash('You must select a program to run.')
            return render_template('blast.html', content=to_md(c), name=name, title=title,
                                   description=description, site_key=app.config['public_key'])
        elif not is_human(captcha_response):
            flash('Please complete the captcha.')
            return render_template('blast.html', content=to_md(c), name=name, title=title, description=description,
                                   site_key=app.config['public_key'])
        elif db not in ["a","c","u"]:
            flash('You must select a database to run.')
            return render_template('blast.html', content=to_md(c), name=name, title=title,
                                    description=description, site_key=app.config['public_key'])
                                    
        elif evalue not in ["0.0001","0.001","0.01","0.1","1","10","100","1000"]:
            flash('You must select a vaild evalue.')
            return render_template('blast.html', content=to_md(c), name=name, title=title,
                                    description=description, site_key=app.config['public_key'])
        else:
            if sequence != "" and file == "":
                query = sequence
            elif sequence == '' and file != '':
                query = file.replace('\\n', '\n')
            hmmrecord = 0
            if function == 'p':
                records = blastp(query, db, evalue)
                hmmrecord = hmmscan(query)
                head = "Result of Blastp"
            elif function == 'x':
                records = blastx(query, db, evalue)
                head = "Result of Blastx"
            if records == 3:
                flash('Your input does not match any record in our database. Please check your input exist and make sure you are using the correct format. You can contact us if the problem persists.')
                return render_template('blast.html', content=to_md(c), name=name, title=title,
                                    description=description, site_key=app.config['public_key'])
            if hmmrecord == 3:
                flash('Your input does not match any record in our database. Please check your input exist and make sure you are using the correct format. You can contact us if the problem persists.')
                return render_template('blast.html', content=to_md(c), name=name, title=title,
                                    description=description, site_key=app.config['public_key'])
            if hmmrecord == "":
                hmmrecord = "Your input does not match any record in our database. Please check your input exist and make sure you are using the correct format. You can contact us if the problem persists."
            description = ""
            if db == "u":
                return render_template('result_blast_uhgp.html', records=records, title=title, description=description,
                                   head=head,
                                   hmmrecord=hmmrecord)
            else:
                return render_template('result_blast.html', records=records, title=title, description=description,
                                   head=head,
                                   hmmrecord=hmmrecord)

    return render_template('blast.html', content=to_md(c), name=name, title=title,
                           description=description, site_key=app.config['public_key'])


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
subfamilycharfile = open("static/materials/subfamily_charactorized.txt", "r")
subfamilychar_list = (subfamilycharfile.readline().split())
subfamilycharfile.close()


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


def is_family_char(family_id):
    if family_id in subfamilychar_list:
        return True
    else:
        return False


app.jinja_env.globals.update(is_family_char=is_family_char)


def blastp(query, db, evalue):
    try:
        uuidname = str(uuid.uuid1())
        with open('tmp/' + uuidname + '.fsa', 'w') as f:
            f.writelines(query)
        if db == "a":
            command = "./blast/blastp -db blastdb/pup_blastp/PUP_db -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        if db == "c":
            command = "./blast/blastp -db blastdb/characterzied/characterzied -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        if db == "u":
            command = "./blast/blastp -db blastdb/uhgp/uhgp_hits -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        os.system(command)

        with open('tmp/' + uuidname + '.blast', 'r') as f:
            data = f.readlines()
            if len(data) == 0:
                if os.path.exists('tmp/' + uuidname + '.fsa'):
                    os.remove('tmp/' + uuidname + '.fsa')
                if os.path.exists('tmp/' + uuidname + '.blast'):
                    os.remove('tmp/' + uuidname + '.blast')
                return 3

        data = pd.read_csv('tmp/' + uuidname + '.blast', sep="\t", header=None)
        index = 0
        processed_blastp = []
        for unid in data[1]:
            if db == "c":
                char_record = CharRecord.query.filter_by(uniq_id=unid).first()
            if db == "a":
                swis_record = SwiRecord.query.filter_by(uniq_id=unid).first()
                trem_record = TreRecord.query.filter_by(uniq_id=unid).first()
            if db == "u":
                uhgp_record = UhgpRecord.query.filter_by(gene_id=unid).first()
                
            if db == "c":
                if char_record != None:
                    char_result = []
                    char_result.append(data[0][index])
                    char_result.append(unid)
                    char_result.append(char_record.family)
                    char_result.append(data[2][index])
                    char_result.append(data[10][index])
                    char_result.append(char_record.protein_name)
                    char_result.append(char_record.strain)
                    char_result.append(char_record.web_id)
                    processed_blastp.append(char_result)
            if db == "a":
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
                elif trem_record != None:
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
            if db == "u":
                if uhgp_record!=None:
                    uhgp_result = []
                    uhgp_result.append(data[0][index])
                    uhgp_result.append(unid)
                    uhgp_result.append(uhgp_record.cluster_id)
                    uhgp_result.append(uhgp_record.family)
                    uhgp_result.append(data[2][index])
                    uhgp_result.append(data[10][index])
                    uhgp_result.append(uhgp_record.name)
                    processed_blastp.append(uhgp_result)
            index += 1

        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.blast'):
            os.remove('tmp/' + uuidname + '.blast')
        return processed_blastp

    except:
        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.blast'):
            os.remove('tmp/' + uuidname + '.blast')
        return 3


def hmmscan(query):
    try:
        uuidname = str(uuid.uuid1())
        with open('tmp/' + uuidname + '.fsa', 'w') as f:
            f.writelines(query)

        command = "hmmscan --domtblout tmp/" + uuidname + ".tbl --noali -E 1e-5 pfam/Pfam-A.hmm tmp/" + uuidname + ".fsa > tmp/" + uuidname + ".log"
        os.system(command)
        result = ""
        i = 0
        with open('tmp/' + uuidname + '.tbl', 'r') as hmmscan:
            for line in hmmscan:
                i += 1
                if i <= 3:
                    result += line
                elif not line.lstrip().startswith('#'):
                    result += line
        print(result)
        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.tbl'):
            os.remove('tmp/' + uuidname + '.tbl')
        if os.path.exists('tmp/' + uuidname + '.log'):
            os.remove('tmp/' + uuidname + '.log')
        return result

    except:
        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.tbl'):
            os.remove('tmp/' + uuidname + '.tbl')
        if os.path.exists('tmp/' + uuidname + '.log'):
            os.remove('tmp/' + uuidname + '.log')
        return 3


def blastx(query, db,evalue):
    try:
        uuidname = str(uuid.uuid1())
        with open('tmp/' + uuidname + '.fsa', 'w') as f:
            f.writelines(query)
        if db == "a":
            command = "./blast/blastx -db blastdb/pup_blastp/PUP_db -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        if db == "c":
            command = "./blast/blastx -db blastdb/characterzied/characterzied -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        if db == "u":
            command = "./blast/blastx -db blastdb/uhgp/uhgp_hits -query tmp/" + uuidname + ".fsa -out tmp/" + uuidname + ".blast -outfmt 6 -evalue "+evalue+" -num_threads 2"
        os.system(command)
        with open('tmp/' + uuidname + '.blast', 'r') as f:
            data = f.readlines()
            if len(data) == 0:
                if os.path.exists('tmp/' + uuidname + '.fsa'):
                    os.remove('tmp/' + uuidname + '.fsa')
                if os.path.exists('tmp/' + uuidname + '.blast'):
                    os.remove('tmp/' + uuidname + '.blast')
                return 3

        data = pd.read_csv('tmp/' + uuidname + '.blast', sep="\t", header=None)
        index = 0
        processed_blastx = []
        for unid in data[1]:
            if db == "c":
                char_record = CharRecord.query.filter_by(uniq_id=unid).first()
            if db == "a":
                swis_record = SwiRecord.query.filter_by(uniq_id=unid).first()
                trem_record = TreRecord.query.filter_by(uniq_id=unid).first()
            if db == "u":
                uhgp_record = UhgpRecord.query.filter_by(gene_id=unid).first()
                
            if db == "c":
                if char_record != None:
                    char_result = []
                    char_result.append(data[0][index])
                    char_result.append(unid)
                    char_result.append(char_record.family)
                    char_result.append(data[2][index])
                    char_result.append(data[10][index])
                    char_result.append(char_record.protein_name)
                    char_result.append(char_record.strain)
                    char_result.append(char_record.web_id)
                    processed_blastx.append(char_result)
            if db == "a":
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
                elif trem_record != None:
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
            if db == "u":
                if uhgp_record!=None:
                    uhgp_result = []
                    uhgp_result.append(data[0][index])
                    uhgp_result.append(unid)
                    uhgp_result.append(uhgp_record.cluster_id)
                    uhgp_result.append(uhgp_record.family)
                    uhgp_result.append(data[2][index])
                    uhgp_result.append(data[10][index])
                    uhgp_result.append(uhgp_record.name)
                    processed_blastx.append(uhgp_result)
            index += 1
        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.blast'):
            os.remove('tmp/' + uuidname + '.blast')
        return processed_blastx
    except:
        if os.path.exists('tmp/' + uuidname + '.fsa'):
            os.remove('tmp/' + uuidname + '.fsa')
        if os.path.exists('tmp/' + uuidname + '.blast'):
            os.remove('tmp/' + uuidname + '.blast')
        return 3


def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """
    secret = app.config['private_key']
    payload = {'response': captcha_response, 'secret': secret}
    response = requests.post("https://hcaptcha.com/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']


class CharRecord(dtbs.Model):
    __tablename__ = 'characterize'
    number = dtbs.Column(dtbs.VARCHAR(5))
    strain = dtbs.Column(dtbs.VARCHAR(150))
    protein_name = dtbs.Column(dtbs.VARCHAR(150))
    pfam = dtbs.Column(dtbs.VARCHAR(100))
    gene_name = dtbs.Column(dtbs.VARCHAR(30))
    uniq_id = dtbs.Column(dtbs.VARCHAR(30), primary_key=True)
    ec = dtbs.Column(dtbs.VARCHAR(50))
    substrate = dtbs.Column(dtbs.VARCHAR(100))
    product = dtbs.Column(dtbs.VARCHAR(200))
    pdb = dtbs.Column(dtbs.VARCHAR(100))
    km = dtbs.Column(dtbs.VARCHAR(30))
    vmax = dtbs.Column(dtbs.VARCHAR(30))
    kcat = dtbs.Column(dtbs.VARCHAR(30))
    family = dtbs.Column(dtbs.VARCHAR(20))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    doi = dtbs.Column(dtbs.VARCHAR(50))
    web_id = dtbs.Column(dtbs.VARCHAR(10))
    type = dtbs.Column(dtbs.VARCHAR(10))
    pubchem_s = dtbs.Column(dtbs.VARCHAR(300))
    pubchem_p = dtbs.Column(dtbs.VARCHAR(2000))
    pfam_link = dtbs.Column(dtbs.VARCHAR(500))


class SwiRecord(dtbs.Model):
    __tablename__ = 'swiss'
    number = dtbs.Column(dtbs.Integer, primary_key=True)
    protein_enzyme = dtbs.Column(dtbs.VARCHAR(150))
    strain = dtbs.Column(dtbs.VARCHAR(150))
    db = dtbs.Column(dtbs.VARCHAR(2))
    uniq_id = dtbs.Column(dtbs.VARCHAR(20))
    pdb = dtbs.Column(dtbs.VARCHAR(500))
    ec = dtbs.Column(dtbs.VARCHAR(50))
    family = dtbs.Column(dtbs.VARCHAR(20))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    type = dtbs.Column(dtbs.VARCHAR(20))
    web_id = dtbs.Column(dtbs.VARCHAR(500))
    lineage = dtbs.Column(dtbs.VARCHAR(500))
    number_pdb = dtbs.Column(dtbs.Integer)


class TreRecord(dtbs.Model):
    __tablename__ = 'trembl'
    number = dtbs.Column(dtbs.Integer, primary_key=True)
    protein_enzyme = dtbs.Column(dtbs.VARCHAR(150))
    strain = dtbs.Column(dtbs.VARCHAR(150))
    db = dtbs.Column(dtbs.VARCHAR(2))
    uniq_id = dtbs.Column(dtbs.VARCHAR(20))
    pdb = dtbs.Column(dtbs.VARCHAR(500))
    ec = dtbs.Column(dtbs.VARCHAR(50))
    family = dtbs.Column(dtbs.VARCHAR(20))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    type = dtbs.Column(dtbs.VARCHAR(20))
    web_id = dtbs.Column(dtbs.VARCHAR(500))
    lineage = dtbs.Column(dtbs.VARCHAR(500))
    number_pdb = dtbs.Column(dtbs.Integer)


class UhgpRecord(dtbs.Model):
    __tablename__ = 'uhgp'
    number = dtbs.Column(dtbs.Integer, primary_key=True)
    gene_id = dtbs.Column(dtbs.VARCHAR(50))
    name = dtbs.Column(dtbs.VARCHAR(200))
    cluster_id = dtbs.Column(dtbs.VARCHAR(50))
    type = dtbs.Column(dtbs.VARCHAR(50))
    lineage = dtbs.Column(dtbs.VARCHAR(200))
    country = dtbs.Column(dtbs.VARCHAR(50))
    continent = dtbs.Column(dtbs.VARCHAR(50))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    MGnify = dtbs.Column(dtbs.VARCHAR(200))
    family = dtbs.Column(dtbs.VARCHAR(10))


class ClusRecord(dtbs.Model):
    __tablename__ = 'cluster'
    number = dtbs.Column(dtbs.Integer, primary_key=True)
    cluster_id = dtbs.Column(dtbs.VARCHAR(50))
    gene_id = dtbs.Column(dtbs.VARCHAR(50))
    name = dtbs.Column(dtbs.VARCHAR(200))
    pfam = dtbs.Column(dtbs.VARCHAR(50))
    type = dtbs.Column(dtbs.VARCHAR(50))
    phylum = dtbs.Column(dtbs.VARCHAR(50))
    continent = dtbs.Column(dtbs.VARCHAR(50))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    pfam_link = dtbs.Column(dtbs.VARCHAR(255))
    mgnify = dtbs.Column(dtbs.VARCHAR(255))


if __name__ == "__main__":
    app.run(host='0.0.0.0')
