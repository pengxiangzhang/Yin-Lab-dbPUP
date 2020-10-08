from flask_sqlalchemy import SQLAlchemy

dtbs = SQLAlchemy()


class TreRecord(dtbs.Model):
    __tablename__ = 'trembl'
    number = dtbs.Column(dtbs.Integer, primary_key=True)
    protein_enzyme = dtbs.Column(dtbs.VARCHAR(150))
    strain = dtbs.Column(dtbs.VARCHAR(150))
    db = dtbs.Column(dtbs.VARCHAR(2))
    uniq_id = dtbs.Column(dtbs.VARCHAR(20))
    pdb = dtbs.Column(dtbs.VARCHAR(500))
    ec = dtbs.Column(dtbs.VARCHAR(50))
    family = dtbs.Column(dtbs.VARCHAR(20))
    seq = dtbs.Column(dtbs.VARCHAR(5500))
    type = dtbs.Column(dtbs.VARCHAR(20))
    web_id = dtbs.Column(dtbs.VARCHAR(500))
