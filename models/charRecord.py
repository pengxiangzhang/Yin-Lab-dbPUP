from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class CharRecord(dtbs.Model):
	__tablename__ = 'characterize'
	number = dtbs.Column(dtbs.Integer)
	strain = dtbs.Column(dtbs.VARCHAR(100))
	protein_name = dtbs.Column(dtbs.VARCHAR(100))
	gene_name = dtbs.Column(dtbs.VARCHAR(100))
	uniq_id = dtbs.Column(dtbs.VARCHAR(100), primary_key=True)
	ec = dtbs.Column(dtbs.VARCHAR(100))
	substrate = dtbs.Column(dtbs.VARCHAR(100))
	production = dtbs.Column(dtbs.VARCHAR(100))
	pdb = dtbs.Column(dtbs.VARCHAR(100))
	km = dtbs.Column(dtbs.Float)
	vmax = dtbs.Column(dtbs.Float)
	kcat = dtbs.Column(dtbs.Float)
	doi = dtbs.Column(dtbs.VARCHAR(100))
	family = dtbs.Column(dtbs.VARCHAR(100))
	seq = dtbs.Column(dtbs.VARCHAR(1000))



