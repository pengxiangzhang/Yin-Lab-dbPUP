from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class Record(dtbs.Model):
	__tablename__ = 'characterize'
	db = dtbs.Column(dtbs.String(30))
	uniq_id = dtbs.Column(dtbs.String(30), primary_key=True)
	entry_name = dtbs.Column(dtbs.String(30))
	protein = dtbs.Column(dtbs.String(30))
	organism = dtbs.Column(dtbs.String(40))
	organism_id = dtbs.Column(dtbs.Integer)
	gene = dtbs.Column(dtbs.String(30))
	protein_exist = dtbs.Column(dtbs.Integer)
	seq_versio = dtbs.Column(dtbs.Integer)
	seq = dtbs.Column(dtbs.VARCHAR(500))