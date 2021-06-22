# UHGP

## UHGG/UHGP

The Unified Human Gastrointestinal Protein (**UHGP**) was collated from the Unified Human Gastrointestinal Genome (**UHGG**) collection, which comprising 204,938 nonredundant prokaryotic genomes from human gut microbiome. All the genomes in UHGP were retrieved from different dataset (IMG, NCBI, PATRIC, HBC, CGR, CIBIO, EBI and HGM), and generated a nonredundant protein catalog from all coding sequences at 90% (UHGP-90, n=13,907,849) protein identity. The functional annotations, metadata and UHGP catalogs are available from the [MGnify FTP site](http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/).

## UHGP Hits

Initially, 31 Pfams and proteins in UCs were used to search against UHGP-90 dataset via `HMMSEARCH` and `PSI_BLAST`. The obtained sequences were further filtered by `PSI-BLAST` and generated a  nonredundant protein catalog with **12,180** sequences. 

All of the collated protein sequences alongside functional annotation, taxonomic lineage, geographic metadata were retrieved from UHGP and corresponding metadata.

## Clusters

Enzymes responsible for the utilization of polyphenols are often encoded by genes located within a cluster. Genes that were obtained from UHGP were manually curated using the following criteria:

- the number of CDS between genes from UHGP Hits was no more than three
- genes at both ends of a cluster were from UHGP Hits
- the intergenic length was less than 1 kb
- genes in a cluster on the same strand

As a result, a total of **103** clusters were yield regarding the above criteria, and the whole set of genes responsible for the utilization of polyphenols are encoded in a gene cluster spanning 2-11kb.

| Gene cluster size | Number | UHGP cluster ID                    |
| :---------------- | :----- | :--------------------------------- |
| 2                 | 53     | UHPG_cluster_1 ~ UHPG_cluster_53   |
| 3                 | 28     | UHPG_cluster_54 ~ UHPG_cluster_81  |
| 4                 | 16     | UHPG_cluster_82 ~ UHPG_cluster_97  |
| >= 5              | 6      | UHPG_cluster_98 ~ UHPG_cluster_103 |







