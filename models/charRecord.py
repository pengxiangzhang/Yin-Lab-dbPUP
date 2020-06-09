from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class CharRecord(dtbs.Model):
	__tablename__ = 'characterize'
	number = dtbs.Column(dtbs.Integer)
	strain = dtbs.Column(dtbs.String(30))
	protein_name = dtbs.Column(dtbs.String(30))
	gene_name = dtbs.Column(dtbs.String(30))
	uniq_id = dtbs.Column(dtbs.String(30), primary_key=True)
	ec = dtbs.Column(dtbs.String(30))
	substrate = dtbs.Column(dtbs.String(30))
	production = dtbs.Column(dtbs.String(30))
	pdb = dtbs.Column(dtbs.String(30))
	km = dtbs.Column(dtbs.Float)
	vmax = dtbs.Column(dtbs.Float)
	kcat = dtbs.Column(dtbs.Float)
	doi = dtbs.Column(dtbs.String(30))
	family = dtbs.Column(dtbs.String(30))
	seq = dtbs.Column(dtbs.VARCHAR(500))



