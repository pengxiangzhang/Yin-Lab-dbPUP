from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class CharRecord(dtbs.Model):
	__tablename__ = 'characterize'
	number = dtbs.Column(dtbs.VARCHAR(5))
	strain = dtbs.Column(dtbs.VARCHAR(60))
	protein_name = dtbs.Column(dtbs.VARCHAR(60))
	gene_name = dtbs.Column(dtbs.VARCHAR(30))
	uniq_id = dtbs.Column(dtbs.VARCHAR(30), primary_key=True)
	ec = dtbs.Column(dtbs.VARCHAR(50))
	substrate = dtbs.Column(dtbs.VARCHAR(60))
	product = dtbs.Column(dtbs.VARCHAR(60))
	pdb = dtbs.Column(dtbs.VARCHAR(60))
	km = dtbs.Column(dtbs.VARCHAR(10))
	vmax = dtbs.Column(dtbs.VARCHAR(10))
	kcat = dtbs.Column(dtbs.VARCHAR(10))
	family = dtbs.Column(dtbs.VARCHAR(10))
	seq = dtbs.Column(dtbs.VARCHAR(1000))
	doi = dtbs.Column(dtbs.VARCHAR(50))
	tax_id = dtbs.Column(dtbs.VARCHAR(10))
	type=dtbs.Column(dtbs.VARCHAR(10))
	pubchem_s=dtbs.Column(dtbs.VARCHAR(300))
	pubchem_p=dtbs.Column(dtbs.VARCHAR(300))
	