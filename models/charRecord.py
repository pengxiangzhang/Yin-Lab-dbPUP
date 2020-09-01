from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class CharRecord(dtbs.Model):
	__tablename__ = 'characterize'
	number = dtbs.Column(dtbs.Integer)
	strain = dtbs.Column(dtbs.VARCHAR(60))
	protein_name = dtbs.Column(dtbs.VARCHAR(60))
	gene_name = dtbs.Column(dtbs.VARCHAR(30))
	uniq_id = dtbs.Column(dtbs.VARCHAR(30), primary_key=True)
	ec = dtbs.Column(dtbs.VARCHAR(50))
	substrate = dtbs.Column(dtbs.VARCHAR(60))
	production = dtbs.Column(dtbs.VARCHAR(60))
	pdb = dtbs.Column(dtbs.VARCHAR(30))
	km = dtbs.Column(dtbs.Float)
	vmax = dtbs.Column(dtbs.Float)
	kcat = dtbs.Column(dtbs.Float)
	doi = dtbs.Column(dtbs.VARCHAR(50))
	family = dtbs.Column(dtbs.VARCHAR(10))
	seq = dtbs.Column(dtbs.VARCHAR(1000))



