# Introduction to dbPUP

**dbPUP** is the first exploratory database of polyphenol utilized proteins that have been **experimentally validated** to catalyze or modify a polyphenol substrate. The database contains 60 proteins from **gut microbiota** that characterized by heterologous or homologous expression with one or more specific polyphenol substrates.  These data are recruited from scientific publications and search results on [BRENDA](https://www.brenda-enzymes.org/). Each of the publications has been carefully vetted before inclusion in Evidence. 

## Class

Proteins in Evidence (seeds) are classified into corresponding class based on their EC numbers and annotations, while proteins have no significant Pfam will be assigned into class Unclassified(UCs).

&#9658; [**Oxidation/Reduction Reactions (ORs)**](./classes/ORs): EC 1.-.-.- in the EC number classification of enzymes.

&#9658;  [**Functional Group Transfer Reactions (FRs)**](./classes/FRs) : EC 2.-.-.- in the EC number classification of enzymes.

&#9658; [**Hydrolysis Reactions (HRs)**](./classes/HRs) : EC 3.-.-.- in the EC number classification of enzymes.

&#9658;​ [**Non-hydrolytic Cleaving Reactions (NCRs)**](./classes/NCRs) : EC 4.-.-.- in the EC number classification of enzymes.

&#9658;​ [**Isomerization Reactions (IRs)**](./classes/IRs) : EC 5.-.-.- in the EC number classification of enzymes.

&#9658;​ [**Synthesis Reactions (SRs)**](./classes/SRs) : EC 6.-.-.- in the EC number classification of enzymes.

&#9658;​ [**Translocation Reactions (TRs)**](./classes/TRs) : EC 7.-.-.- in the EC number classification of enzymes.

&#9658;​ [**Unclassified (UCs)**](./classes/UCs)

![family_count](./static/images/text_content/figures/family_count.jpg){: .fit}

## Family

Initially, Pfams were filtered out if they cannot individually prove their essential for biocatalysis of polyphenol. Subsequently, proteins in same class were further classified into different families based on Pfams in their sequences. Family then were extend by search against Swiss-Prot and TrEMBL datasets using `HMMER`. An approximately-maximum-likelihood phylogenetic tree was constructed (`FastTree`2.1.11) for sequences from Swiss-Prot in each family.  Sequences collected from TrEMBL were further filtered out by `PIS-BLAST` with a unified threshold  (E-value 0.001 and iteration number 5).

![characterized_protein](./static/images/text_content/figures/characterized_protein.jpg){: .fit}

## Subfamily

All-*versus*-all `BLAST` was performed for each family and then filtered sequences into clusters basing on a given similarity threshold. Results were visualized with Cytoscape using the yFiles organic layout. Cluster contains ten or more nodes were considered as a subfamily. 