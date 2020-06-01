use development;

DROP TABLE characterize;
CREATE TABLE IF NOT EXISTS characterize(
	db CHAR(30),
    uniq_id CHAR(30),
    entry_name CHAR(30),
    protein CHAR(30),
    organism CHAR(40),
    organism_id INT,
    gene CHAR(30),
    protein_exist INT,
    seq_versio INT,
    seq VARCHAR(500),
    primary key (uniq_id)
);

INSERT INTO characterize(db, uniq_id, entry_name, protein, organism, organism_id, gene, protein_exist, seq_versio, seq)
value('some_db', 'aaa','asdf','asdf','asdf', 1 ,'asdf',2, 2 ,'asdfasdf');
INSERT INTO characterize(db, uniq_id, entry_name, protein, organism, organism_id, gene, protein_exist, seq_versio, seq)
value('some_db', 'bbb','asdf','asdf','asdf', 1 ,'asdf',2, 2 ,'asdfasdf');
INSERT INTO characterize(db, uniq_id, entry_name, protein, organism, organism_id, gene, protein_exist, seq_versio, seq)
value('some_db', 'ccc','asdf','asdf','asdf', 1 ,'asdf',2, 2 ,'asdfasdf');