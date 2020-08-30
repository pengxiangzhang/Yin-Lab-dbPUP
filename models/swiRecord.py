from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()

class SwiRecord(dtbs.Model):
        __tablename__= 'swiss'
        protein_enzyme = dtbs.Column(dtbs.String(30))
        strain=dtbs.Column(dtbs.String(30))
        database=dtbs.Column(dtbs.String(30))
        uniq_id=dtbs.Column(dtbs.String(30),primary_key=True)
        family=dtbs.Column(dtbs.String(30))
        ec=dtbs.Column(dtbs.String(30))
        seq = dtbs.Column(dtbs.VARCHAR(500))

