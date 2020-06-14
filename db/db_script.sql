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

INSERT INTO characterize(number, strain, protein_name, gene_name, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(1, 'asdf', 'adsf','asdf','aaa','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '1', 'asdf');
INSERT INTO characterize(number, strain, protein_name, gene_name, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(2, 'asdf', 'adsf','asdf','bbb','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '2', 'asdf');
INSERT INTO characterize(number, strain, protein_name, gene_name, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(3, 'asdf', 'adsf','asdf','ccc','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '3', 'asdf');

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

INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','aaa','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ddd','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','eee','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','fff','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','bbb','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ggg','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','hhh','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ccc','3','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','iii','3','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','jjj','3','qewr','qwer');

#value('Quercetin 2,3-dioxygenase','Bacillus subtills','qdol', 'P42106', '1.13.11.24', 'RTGFGSDFDSFADGFSDFGDFXCVXCV');

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
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','aaa','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ddd','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','eee','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','fff','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','bbb','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ggg','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','hhh','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ccc','3','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','iii','3','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, gene_name, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','jjj','3','qewr','qwer');
