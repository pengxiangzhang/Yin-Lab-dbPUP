from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()
class TreRecord(dtbs.Model):
        __tablename__= 'trembl'
        protein_enzyme = dtbs.Column(dtbs.VARCHAR(100))
        strain=dtbs.Column(dtbs.VARCHAR(100))
        database=dtbs.Column(dtbs.VARCHAR(100))
        uniq_id=dtbs.Column(dtbs.VARCHAR(100), primary_key=True) 
        family=dtbs.Column(dtbs.VARCHAR(100))
        ec=dtbs.Column(dtbs.VARCHAR(100))
        seq = dtbs.Column(dtbs.VARCHAR(1000))

