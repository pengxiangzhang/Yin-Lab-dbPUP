## UHGG/UHGP

The Unified Human Gastrointestinal Protein (**UHGP**) was collated from the [Unified Human Gastrointestinal Genome (**
UHGG**) collection](https://www.nature.com/articles/s41587-020-0603-3), which contains 204,938 nonredundant prokaryotic
genomes from human gut microbiome. UHGG genomes were retrieved from different dataset (IMG, NCBI, PATRIC, HBC, CGR,
CIBIO, EBI and HGM). UHGP contains all the proteins from UHGG. The UHGG sequences, functional annotations, and metadata
are available from the [MGnify FTP site](http://ftp.ebi.ac.uk/pub/databases/metagenomics/mgnify_genomes/).

## UHGP Homologs

As described in the [homepage](http://bcb.unl.edu/dbpup/), the 31 Pfam signature domains of 60 seed proteins (including
2 proteins in UCs) were used to search against UHGP-90 using `HMMSEARCH` and `PSI_BLAST`. The obtained sequences were
further filtered by `PSI-BLAST` and in total **51,157** UHGP homologs are found.

The protein sequences, functional annotation, taxonomic lineage, and geographic metadata were extracted and presented.

<figure class="fit">
    <embed type="image/svg+xml" src="./static/images/text_content/figures/UHGP_count.svg" />
</figure>

## Physically linked PUP gene clusters (PGCs)

The [UHGP](https://www.nature.com/articles/s41587-020-0603-3) protein data are derived from the Unified Human
Gastrointestinal Genomes (UHGG), which contain over 200,000 nonredundant genomes from the human gut microbiome. By
locating the PUP homologs of UHGP in the genomes, we have identified physically linked PUP gene clusters (PGCs) in the
gut microbiome, which potentially are involved in polyphenols utilization in human gut. The concept of PGCs is the same
as the [polysaccharide utilization loci (PULs)](https://pubmed.ncbi.nlm.nih.gov/28138099/)
or [CAZyme gene clusters (CGCs)](https://academic.oup.com/nar/article/46/W1/W95/4996582) for carbohydrate utilization.
The idea/hypothesis is that for more efficient polyphenol utilization, PUP encoding genes might be clustered with each
other and with other genes in the microbial genomes to form an operon or physically linked gene clusters for coordinated
gene expression.

By locating the PUP homologs of UHGP in the genomes, we have defined physically linked PUP gene clusters (PGCs) using
the following algorithm:

- at least two UHGP homologs in the gene cluster
- no more than three other genes are allowed between two adjacent UHGP homologs
- all the intergenic lengths are less than 1 kb

Using the simple algorithm described above, a total of **1074** [PGCs](./uhgp/Cluster) were identified with PGC sizes
ranging from 2 kb to 11 kb.

| Gene cluster size | Number | Cluster ID                                                   |
| :---------------- | :----- | :----------------------------------------------------------- |
| 2                 | 679    | [PGC_1](http://bcb.unl.edu/dbpup/cluster/PGC_1) ~ [PGC_679](http://bcb.unl.edu/dbpup/cluster/PGC_679) |
| 3                 | 228    | [PGC_680](http://bcb.unl.edu/dbpup/cluster/PGC_680) ~ [PGC_907](http://bcb.unl.edu/dbpup/cluster/PGC_907) |
| 4                 | 151    | [PGC_908](http://bcb.unl.edu/dbpup/cluster/PGC_908) ~ [PGC_1058](http://bcb.unl.edu/dbpup/cluster/PGC_1058) |
| 5                 | 6      | [PGC_1059](http://bcb.unl.edu/dbpup/cluster/PGC_1059) ~ [PGC_1064](http://bcb.unl.edu/dbpup/cluster/PGC_1064) |
| 6                 | 5      | [PGC_1065](http://bcb.unl.edu/dbpup/cluster/PGC_1065) ~ [PGC_1069](http://bcb.unl.edu/dbpup/cluster/PGC_1069) |
| 7                 | 4      | [PGC_1070](http://bcb.unl.edu/dbpup/cluster/PGC_1070) ~ [PGC_1073](http://bcb.unl.edu/dbpup/cluster/PGC_1073) |
| 8                 | 1      | [PGC_1074](http://bcb.unl.edu/dbpup/cluster/PGC_1074)        |







