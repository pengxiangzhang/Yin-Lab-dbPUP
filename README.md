
# Database for Polyphenol Utilized Proteins from gut microbiota (dbPUP)
<img src="https://ucomm.unl.edu/images/brand-book/Our-marks/R-UNL-Hex.svg" alt="UNL" width="250"> <img src="https://i.loli.net/2020/12/28/JFs9E86SkdfGpvK.png" alt="dbpup" width="300">



## Introduction

This website is developed for [Yin's Lab](http://bcb.unl.edu/) located at
the [University of Nebraska - Lincoln](https://www.unl.edu) and founded by [NSF](https://www.nsf.gov/).

This website was written in python3, web framework is [Flask](https://flask.palletsprojects.com/en/1.1.x/) and template engine is [Jinja2](https://jinja.palletsprojects.com/en/2.11.x/).

This website also use Blast(https://blast.ncbi.nlm.nih.gov/Blast.cgi) to comparing primary biological sequence information and sequence analysis software Hmmer(http://hmmer.org/).

## Installation

1. Make sure you have python3, python3-pip and [hmmer](http://hmmer.org/) installed.
2. Make sure you have clone the website and ready to deploy.
3. run `pip3 install -r requirements.txt` to install all the requirement.
4. Put `TrEMBL.tar.gz`, `Swiss-Prot.tar.gz`, `Sequence_Similarity_Network.tar.gz` and `Characterization.tar.gz`
   into `static/Download/`
6. put [fam-A](ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam33.1/Pfam-A.hmm.gz) database to `pfam/` then
   run `hmmpress Pfam-A.hmm`
7. We recommand to serve pn Nginx, but here is the
   instruction: [Instruction to serve on nginx](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04)
   ; If serve on Apache we recommand to run it with [gunicorn](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-18-04) then use apache to forward the port instead of Nginx(Note a copy of gunicorn configurations is in `gunicorn.conf.py.example`).

## Testing and Contributing

1. run `make` if you are contributing; run `make production` if you are deploying.
2. open your browser and go to `localhost:5000` or the domain you bind with.

## Configurations

If you decide to host your own website, you will need to change the `config.json.example` to `config.json` and change
configurations accordingly. Remember that if you are developing the application, you should nevercommit sensitive
informations in the `config.json` in the version control system.

If you host it on Apache, you will need to change `gunicorn.conf.py.example` to `gunicorn.conf.py`and change configurations accordingly.

## Changing or Adding Content
When adding/modify sequences, add it directly to the database that you connected to. Note: Please make sure the following file contains the family or subfamily you added `/static/materials/family.txt` and `/static/materials/subfamily.txt`.

When adding/modify content, add it to `/content/`. Note: If you are adding subfamily make sure the following file contain the subfamily you added `/static/materials/subfamily_charactorized.txt`.