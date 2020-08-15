use bio_test;

DROP TABLE IF EXISTS characterize;
CREATE TABLE IF NOT EXISTS characterize(
    number INT NOT NULL,
    strain CHAR(30),
    protein_name CHAR(30),
    gene_name CHAR(30),
    uniq_id CHAR(30),
    ec CHAR(30),
    substrate CHAR(30),
    production CHAR(30),
    pdb CHAR(30),
    km FLOAT,
    vmax FLOAT,
    kcat FLOAT,
    doi CHAR(30),
    family CHAR(30),
    seq VARCHAR(500),
    primary key (uniq_id)
);

DROP TABLE IF EXISTS swiss;
CREATE TABLE IF NOT EXISTS swiss(
    protein_enzyme CHAR(30),
    strain CHAR(30),
    gene_name CHAR(30),
    uniq_id CHAR(30) PRIMARY KEY,
    ec CHAR(30),
    family CHAR(30),
    seq  VARCHAR(1000)
);

DROP TABLE IF EXISTS trembl;
CREATE TABLE IF NOT EXISTS trembl(
    protein_enzyme CHAR(30),
    strain CHAR(30),
    gene_name CHAR(30),
    uniq_id CHAR(30) PRIMARY KEY,
    ec CHAR(30),
    family CHAR(30),
    seq  VARCHAR(1000)
);
