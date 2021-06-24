## UHGG/UHGP

The Unified Human Gastrointestinal Protein (**UHGP**) was collated from the [Unified Human Gastrointestinal Genome (**UHGG**) collection](https://www.nature.com/articles/s41587-020-0603-3), which contains 204,938 nonredundant prokaryotic genomes from human gut microbiome. UHGG genomes were retrieved from different dataset (IMG, NCBI, PATRIC, HBC, CGR, CIBIO, EBI and HGM). UHGP contains all the proteins from UHGG. From UHGP (n=???), protein sequences were processed to remove redundancy at 90% sequence identity to create UHGP-90 database (n=13,907,849). The UHGG sequences, functional annotations, and metadata are available from the [MGnify FTP site](http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/).

## UHGP Homologs

As described in the [homepage](http://bcb.unl.edu/dbpup/), the 31 Pfam signature domains of 60 seed proteins (including 2 proteins in UCs) were used to search against UHGP-90 using `HMMSEARCH` and `PSI_BLAST`. The obtained sequences were further filtered by `PSI-BLAST` and in total **12,180** UHGP homologs are found. 

The protein sequences, functional annotation, taxonomic lineage, and geographic metadata were extracted and presented.

<figure class="fit">
    <embed type="image/svg+xml" src="./static/images/text_content/figures/UHGP_count.svg" />
</figure>

## Physically linked PUP gene clusters (PGCs)

The [UHGP](https://www.nature.com/articles/s41587-020-0603-3) protein data are derived from the Unified Human Gastrointestinal Genomes (UHGG), which contain over 200,000 nonredundant genomes from the human gut microbiome. By locating the PUP homologs of UHGP in the genomes, we have identified physically linked PUP gene clusters (PGCs) in the gut microbiome, which potentially are involved in polyphenols utilization in human gut. The concept of PGCs is the same as the [polysaccharide utilization loci (PULs)](https://pubmed.ncbi.nlm.nih.gov/28138099/) or [CAZyme gene clusters (CGCs)](https://academic.oup.com/nar/article/46/W1/W95/4996582) for carbohydrate utilization. The idea/hypothesis is that for more efficient polyphenol utilization, PUP encoding genes might be clustered with each other and with other genes in the microbial genomes to form an operon or physically linked gene clusters for cooridinated gene expression. 

By locating the PUP homologs of UHGP in the genomes, we have defined physically linked PUP gene clusters (PGCs) using the following algorithm:

- all genes in the cluster are on the same strand
- at least two UHGP homologs in the gene cluster
- no more than three other genes are allowed between two adjacent UHGP homologs
- all the intergenic lengths are less than 1 kb

Using the simple algorithm described above, a total of **103** [PGCs](./uhgp/Cluster) were identified with PGC sizes ranging from 2 kb to 11 kb.


| Gene cluster size | Number | UHGP cluster ID                    |
| :---------------- | :----- | :--------------------------------- |
| 2                 | 53     | UHPG_cluster_1 ~ UHPG_cluster_53   |
| 3                 | 28     | UHPG_cluster_54 ~ UHPG_cluster_81  |
| 4                 | 16     | UHPG_cluster_82 ~ UHPG_cluster_97  |
| >= 5              | 6      | UHPG_cluster_98 ~ UHPG_cluster_103 |







