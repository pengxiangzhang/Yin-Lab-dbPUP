# Introduction to dbPUP

**dbPUP** is a database of polyphenol utilization proteins (PUPs) that have been **experimentally characterized** to metabolize polyphenol substrates. Polyphenols are one of largest groups of secondary metabolites in plants and are present in a wide range of fruits, vegetables, cereals as well as plant-based food products. In recent years, [growing evidence](https://pubs.rsc.org/ko/content/articlehtml/2019/fo/c8fo01997e) has been shown that consumption of polyphenol-rich foods can lower the risk of various human diseases such as cardiovascular diseases, cancers, and metabolic syndromes. 

The core contents of **dbPUP** are [60 proteins](./characterized) that are biochemically characterized with one or more specific polyphenol substrates. We collected these 60 proteins and associated metadata by manually curating hundreds of peer-reviewed papers from PubMed and by searching over hundreds of polyphenolic substrates in the BRENDA database [BRENDA](https://www.brenda-enzymes.org/). We have classified these biochemically characterized PUPs into sequence families according to the conserved Pfam domains that they share. We have further expanded the PUP families by including sequence homologs from the [UniProt](https://www.uniprot.org/) database and the database of [Unified Human Gastrointestinal Protein (UHGP) catalog](https://www.nature.com/articles/s41587-020-0603-3).

We organized PUP seeds and homologs of **dbPUP** in a hiercharical classification: enzyme class (Enzyme database) -> protein family (Pfam domain) -> protein subfamily (sequence similarity network).

## Class

The [60 characterized PUP proteins (called seeds)](./characterized) are classified into 6 enzyme classes based on their EC numbers and functional annotations, including two proteins assigned to an unclassified class (UCs).

&#9658; [**Oxidation/Reduction Reactions (ORs)**](./classes/ORs): transfers of H and O atoms or electrons from one substance to another, including **23** PUP seeds.

&#9658;  [**Functional Group Transfer Reactions (FRs)**](./classes/FRs): transfers of a functional group from one substance to another, including **7** PUP seeds.

&#9658; [**Hydrolysis Reactions (HRs)**](./classes/HRs): breaks a chemical bond in order to divide a large molecule into two smaller ones, including **25** PUP seeds.

&#9658; [**Non-hydrolytic Cleaving Reactions (NCRs)**](./classes/NCRs): non-hydrolytic addition or removal of groups from substrates,  including  **1** PUP seed.

&#9658; [**Isomerization Reactions (IRs)**](./classes/IRs): has exactly the same atoms, but the atoms are rearranged, including **2** PUP seeds.

&#9658; [**Synthesis Reactions (SRs)**](./classes/SRs): joins together two large molecules by forming a new chemical bond, no PUP seeds.

&#9658; [**Translocation Reactions (TRs)**](./classes/TRs): assists in moving another molecule, usually across a cell membrane, no PUP seeds.

&#9658; [**Unclassified (UCs)**](./classes/UCs): only available for experimentally validated proteins without significant Pfam family, including **2** PUP seeds.

<figure class="fit">
    <embed type="image/svg+xml" src="./static/images/text_content/figures/family_count.svg" />
</figure>

## Family

In addition to the [60 PUP seeds](./characterized), dbPUP also contains PUP sequence homologs from [UniProt](https://www.uniprot.org/) and [UHGP](https://www.nature.com/articles/s41587-020-0603-3). To identify PUP homologs, we first identified conserved [Pfam](http://pfam.xfam.org/) domains in the 60 PUP seeds. According to the shared Pfam domains, PUP seeds of the same enzyme class were further classified into different families: OR class (9 families), FR class (4 families), HR class (8 families), NCR class (1 family), IR class (2 families), and UC class (2 families). 

![characterized_protein](./static/images/text_content/figures/characterized_protein.jpg){: .fit2 .rounded-border}

As each family has its own signature Pfam domain or domain combination (see each family page, e.g. [OR families](./classes/ORs#pfam-information)), PUP sequence homologs were then identified by search against UniProt (Swiss-Prot and TrEMBL) databases using `HMMER` or `PSI-BLAST` (for the two UC families). A phylogenetic tree was constructed (`FastTree`2.1.11) for homologs from Swiss-Prot in each family. Sequence homologs from TrEMBL were further filtered out by `PSI-BLAST` with the PUP seeds of the family as query using a unified threshold (E-value 0.001 and iteration number 5), because TrEMBL is too big and contains all computer-predicted proteins. 

We have followed the same procedure to collect PUP homologs from the UHGP database.

## Subfamily

To further classify PUP homologs from UniProt, an all-*versus*-all `BLASTP` was performed for each family using the [sequence similarity network (SSN) analysis](https://efi.igb.illinois.edu/efi-est/tutorial.php). The BLASTP result was then used as input for [Cytoscape](https://cytoscape.org/) to classify PUP seeds and homologs into clusters (subfamilies) based on a given similarity threshold. Results were lastly visualized with Cytoscape using the [yFiles organic layout](https://www.yworks.com/products/yfiles-layout-algorithms-for-cytoscape) and graphs were generated. Clusters with 10+ sequences were considered as a subfamily. 

## Physically linked PUP gene clusters (PGCs)

The [UHGP](https://www.nature.com/articles/s41587-020-0603-3) protein data are derived from the Unified Human Gastrointestinal Genomes (UHGG), which contain over 200,000 nonredundant genomes from the human gut microbiome. By locating the PUP homologs of UHGP in the genomes, we have identified physically linked PUP gene clusters (PGCs) in the gut microbiome, which potentially are involved in polyphenols utilization in human gut. The concept of PGCs is the same as the [polysaccharide utilization loci (PULs)](https://pubmed.ncbi.nlm.nih.gov/28138099/) or [CAZyme gene clusters (CGCs)](https://academic.oup.com/nar/article/46/W1/W95/4996582) for carbohydrate utilization. The idea/hypothesis is that for more efficient polyphenol utilization, PUP encoding genes might be clustered with each other and with other genes in the microbial genomes to form an operon or physically linked gene clusters for cooridinated gene expression. 

From the Pfam search, a nonredundant protein catalog with **51,157** UHGP sequence homologs of PUP seeds was yielded and presented in table (e.g., [uhgp/Africa](./uhgp/Africa)), together with metadata of the UHGP. Using a simple algorithm described in the [UHGP page](./uhgp_home) to locate the PUP homologs in the genomes, a total of **1074** [PGCs](./uhgp/Cluster) were identified from UHGG catalog with PGC sizes ranging from 2 kb to 11 kb.

