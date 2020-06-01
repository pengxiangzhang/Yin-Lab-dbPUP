use development;

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