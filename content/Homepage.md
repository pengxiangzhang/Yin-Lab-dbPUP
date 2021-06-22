# Introduction to dbPUP

**dbPUP** is the first exploratory database of polyphenol utilized proteins that have been **experimentally validated** to catalyze or modify a polyphenol substrate. The database contains 60 proteins from **microbiome** that characterized by heterologous or homologous expression with one or more specific polyphenol substrates. These data are recruited from scientific publications and search results on [BRENDA](https://www.brenda-enzymes.org/). Each of the publications has been carefully vetted before inclusion in Characterized.

## Class

Proteins in Characterized (seeds) are classified into corresponding class based on their EC numbers and annotations, while
proteins have no significant Pfam family will be assigned into class Unclassified(UCs).

&#9658; [**Oxidation/Reduction Reactions (ORs)**](./classes/ORs): transfers of H and O atoms or electrons from one substance to another, including **23** characterized proteins.

&#9658;  [**Functional Group Transfer Reactions (FRs)**](./classes/FRs) : transfers of a functional group from one substance to another, including **7** characterized proteins.

&#9658; [**Hydrolysis Reactions (HRs)**](./classes/HRs) : breaks a chemical bond in order to divide a large molecule into two smaller ones, including **25** characterized proteins.

&#9658; [**Non-hydrolytic Cleaving Reactions (NCRs)**](./classes/NCRs)  : non-hydrolytic addition or removal of groups from substrates,  including  **1** characterized protein.

&#9658; [**Isomerization Reactions (IRs)**](./classes/IRs) : has exactly the same atoms, but the atoms are rearranged, including **2** characterized proteins.

&#9658; [**Synthesis Reactions (SRs)**](./classes/SRs) : joins together two large molecules by forming a new chemical bond, no characterized protein.

&#9658; [**Translocation Reactions (TRs)**](./classes/TRs) : assists in moving another molecule, usually across a cell membrane, no characterized protein.

&#9658; [**Unclassified (UCs)**](./classes/UCs) : only available for experimentally validated proteins without significant Pfam family, including **2** characterized proteins.

<figure class="fit">
    <embed type="image/svg+xml" src="./static/images/text_content/figures/family_count.svg" />
</figure>

## Family

Initially, Pfam families were filtered out if they cannot individually prove their essential for biocatalysis of polyphenols. Subsequently, proteins in same class were further classified into different families based on Pfams in their sequences. Family then were extend by search against Swiss-Prot and TrEMBL datasets using `HMMER` or `PSI-BLAST`. An approximately-maximum-likelihood phylogenetic tree was constructed (`FastTree`2.1.11) for sequences from Swiss-Prot in each family. Sequences collected from TrEMBL were further filtered out by `PSI-BLAST` with a unified threshold  (E-value 0.001 and iteration number 5).

![characterized_protein](./static/images/text_content/figures/characterized_protein.jpg){: .fit2 .rounded-border}

## Subfamily

All-*versus*-all `BLAST` was performed for each family and then filtered sequences into clusters basing on a given similarity threshold. Results were visualized with Cytoscape using the yFiles organic layout. Cluster contains ten or more nodes were considered as a subfamily. 

## Clusters

The Unified Human Gastrointestinal Genome (UHGG) collected over 200,000 nonredundant genomes from the human gut microbiome. Over 170 million protein sequences and corresponding functional annotations make it possible to find clusters involved in polyphenols utilization. After extended (`HMMSEARCH`and `PSI-BLAST`)and filtered (`PSI-BLAST`) the protein hits from UHGP,  a nonredundant protein catalog with **12,180** sequences was yielded and presented in tabular format, alongside functional annotation, source, and lineage. As a result, a total of **103** clusters were curated from UHGP catalog with different sizes range from 2 kb to 11 kb.

