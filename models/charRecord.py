from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()


class CharRecord(dtbs.Model):
    __tablename__ = 'characterize'
    number = dtbs.Column(dtbs.VARCHAR(5))
    strain = dtbs.Column(dtbs.VARCHAR(150))
    protein_name = dtbs.Column(dtbs.VARCHAR(150))
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
    tax_id = dtbs.Column(dtbs.VARCHAR(10))
    type = dtbs.Column(dtbs.VARCHAR(10))
    pubchem_s = dtbs.Column(dtbs.VARCHAR(300))
    pubchem_p = dtbs.Column(dtbs.VARCHAR(2000))
