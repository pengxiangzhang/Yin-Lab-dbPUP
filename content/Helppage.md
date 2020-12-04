# Help page

[TOC]

## dbPUP

**dbPUP** is the first database to collect polyphenol utilization proteins that have been **experimentally validated** to catalyze or modify a polyphenol substrate. The database currently contains 60 proteins from **gut microbiota** that are manually curated from literature and enzyme database. These proteins have been characterized by different experimental approaches targeting one or more specific polyphenol substrates. These experimentally characterized proteins are also called seed proteins. Using these seed proteins, we also collected over 24,000 proteins that share conserved Pfam domains and significant sequence similarities with the seed proteins, and thus are potentially capable of metabolizing polyphenols. These proteins are also called computationally predicted proteins. All these seed proteins and computationally predicted proteins are compiled together and classified into protein families based on sequence homology and further categorized into classes according to EC numbers that the seed proteins have.

Workflow of dbPUP

![Workflow](./static/images/text_content/figures/Workflow.jpg){: .fit .rounded-border}

## Evidence Page (change this to Characterized Protein Page)

This page displays a table with all the seed proteins and associated metadata in dbPUP. Users can sort in ascending or descending order the number, strain, protein name, gene name, uniprot id, EC, substrate, product, PDB, Km, Vmax and Kcat.

Users can jump to a specific page looking for more details by clicking on blue text links in cell.
![help1](./static/images/text_content/figures/help1.png){: .fit2 .rounded-border}

## Class Page

In the navigation menu, clicking on Class link will expand to show the list of classes. Clicking on each class will open the page of each enzyme class page, where users can find essential information about introduction, reaction description, Pfam of seeds, subfamily and EC. Clicking the Family name (e.g. OR1) will redirect users to Family page, where exhibits experimental results in very detail.

![help2](./static/images/text_content/figures/help2.png){: .fit2 .rounded-border}

### Family Page

Each family have their corresponding Pfams and were extended by `HMMSEARCH` using raw HMM from Pfam website.

Metadata and general information about the seeds in this family, including literature information and Experimental results.

The Literature Information tab displays the title, authors, DOI and abstract of the corresponding publication. Polyphenols that involved in biochemical experiments are highlighted in abstract.

![help3](./static/images/text_content/figures/help3.png){: .fit2 .rounded-border}

Experimental results tab displays the entry, Pfam and reaction information based on the above literature. Clicking blue text links redirects users to corresponding pages for more details.

![help4](./static/images/text_content/figures/help4.png){: .fit2 .rounded-border}

![help5](./static/images/text_content/figures/help5.png){: .fit2 .rounded-border}

### Table for Swiss-Prot/TrEMBL result

Both Swiss-Prot and TrEMBL tables consist of seven major parts of protein name (a), strain (b), uniprot (c), PDB (d), family (e), EC (f) and sequence (g). Users view the taxa of interest in same table by clicking the buttons (h) above the table.

![help6](./static/images/text_content/figures/help6.png){: .fit2 .rounded-border}

### Phylogenetic tree

Family trait were totally depending on their seeds, which means sequences in a family should have all essential Pfams same with seeds. If seeds in a family only have one essential Pfam, the phylogenetic tree for this family will be constructed by sequence domain segments. However, for seeds have multiple essential Pfams, the phylogenetic tree were constructed by full length sequences.

Users can view a rectangular phylogenetic tree, if available, by clicking the tree button above the Swiss-Prot table. Features of the phylogenetic tree include:

- Simply click and drag with mouse to move the tree, 
- Adjust the display zoom level by mouse wheel.
- Click any internal tree node to collapse a clade.
- Highlighted seed id and its closed branches.

![help7](./static/images/text_content/figures/help7.png){: .fit .rounded-border}

### SSN visualization

Uses can find SSN visualization result for each family by clicking the network button above the TrEMBL table. 

Two tabs with two figures are available. The first figure is an overview of all the sequences in this family. Usually, edges represent an E-value threshold below 10-<sup>80</sup>. Nodes in dark color indicate a subgroup containing seeds, while the light ones indicates individuals that distant with seeds. 

The others are enlarged pictures for each subfamily. Nodes are filled by different color depending on their taxa. Additionally, nodes have a light yellow border indicate the seeds.

![help8](./static/images/text_content/figures/help8.png){: .fit .rounded-border}

## BLAST

Users can enter a protein sequence of interest in FASTA format to perform a BLAST search against dbPUP. This can be done in following ways:

1. Enter a protein or nucleotide sequence into the form field.
2. Upload a FASTA format file

figure

Results are displayed as a sortable table including protein information, scores and E-values obtained from BLAST. 

figure

## Download

All data for dbPUP are available for download. Data files for each zip file include:

- Characterization Data: Biochemically validated proteins in FASTA and UniProt format
- Sequence Similarity Network: `PSI-BLAST` results for each family
- Swiss-Prot Data: Protein sequences from Swiss-Prot dataset for each family
- TrEMBL Data: Protein sequences from TrEMBL dataset for each family

## Statistics

The Statistics page includes a basic table about current data in dbPUP.
