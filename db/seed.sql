use bio_test;
INSERT INTO characterize(number, strain, protein_name, database, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(1, 'asdf', 'adsf','asdf','aaa','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '1', 'asdf');
INSERT INTO characterize(number, strain, protein_name, database, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(2, 'asdf', 'adsf','asdf','bbb','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '2', 'asdf');
INSERT INTO characterize(number, strain, protein_name, database, uniq_id, ec, substrate, production, pdb, km, vmax, kcat, doi, family, seq)
value(3, 'asdf', 'adsf','asdf','ccc','asdf', 'asdf', 'asdf', 'adsf', 1, 2, 3, 'asdf', '3', 'asdf');

INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','aaa','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ddd','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','eee','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','fff','1','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','bbb','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ggg','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','hhh','2','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ccc','3','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','iii','3','qewr','qwer');
INSERT INTO swiss(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','jjj','3','qewr','qwer');

#value('Quercetin 2,3-dioxygenase','Bacillus subtills','qdol', 'P42106', '1.13.11.24', 'RTGFGSDFDSFADGFSDFGDFXCVXCV');

INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','aaa','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ddd','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','eee','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','fff','1','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','bbb','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ggg','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','hhh','2','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','ccc','3','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','iii','3','qewr','qwer');
INSERT INTO trembl(protein_enzyme, strain, database, uniq_id, family,  ec, seq) 
value('some_eny','qwer','qewr','jjj','3','qewr','qwer');
