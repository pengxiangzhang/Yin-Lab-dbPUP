from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()


class TreRecord(dtbs.Model):
    __tablename__ = 'trembl'
    number = dtbs.Column(dtbs.Integer)
    protein_enzyme = dtbs.Column(dtbs.VARCHAR(100))
    strain = dtbs.Column(dtbs.VARCHAR(100))
    db = dtbs.Column(dtbs.VARCHAR(2))
    uniq_id = dtbs.Column(dtbs.VARCHAR(10), primary_key=True)
    pdb = dtbs.Column(dtbs.VARCHAR(50))
    ec = dtbs.Column(dtbs.VARCHAR(50))
    family = dtbs.Column(dtbs.VARCHAR(20))
    seq = dtbs.Column(dtbs.VARCHAR(1000))
    type = dtbs.Column(dtbs.VARCHAR(10))
    web_id = dtbs.Column(dtbs.Integer)
