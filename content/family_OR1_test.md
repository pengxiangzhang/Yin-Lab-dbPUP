# <font color=#074987>Oxidation/Reduction Reactions (ORs) Family 1</font>


[TOC]

## <font color=#074987>Literature Information</font>

|  Title   | Discovery of the curcumin metabolic pathway involving a unique enzyme in an intestinal microorganism |
| :------: | :----------------------------------------------------------- |
|  Author  | Azam Hassaninasab, Yoshiteru Hashimoto, Kaori Tomita-Yokotani, and Michihiko Kobayashi |
|   DOI    | [10.1073/pnas.1016217108](https://doi.org/10.1073/pnas.1016217108) |
| Abstract | Polyphenol curcumin, a yellow pigment, derived from the rhizomes of a plant (*Curcuma longa* Linn) is a natural antioxidant exhibiting a variety of pharmacological activities and therapeutic properties. It has long been used as a traditional medicine and as a preservative and coloring agent in foods. Here, curcumin-converting microorganisms were isolated from human feces, the one exhibiting the highest activity being identified as *Escherichia coli*. We are thus unique in discovering that *E. coli* was able to act on curcumin. The curcumin-converting enzyme was purified from *E. coli* and characterized. The native enzyme had a molecular mass of about 82 kDa and consisted of two identical subunits. The enzyme has a narrow substrate spectrum, preferentially acting on curcumin. The microbial metabolism of curcumin by the purified enzyme was found to comprise a two-step reduction, curcumin being converted NADPH-dependently into==**an intermediate product**==, ==**dihydrocurcumin**==, and then the end product, ==**tetrahydrocurcumin**==. We named this enzyme “NADPH-dependent curcumin/dihydrocurcumin reductase” (CurA). The gene (*curA*) encoding this enzyme was also identified. A homology search with the BLAST program revealed that a unique enzyme involved in curcumin metabolism belongs to the medium-chain dehydrogenase/reductase superfamily. |

---

## <font color=#074987>Experimental results</font>

- **Enzyme**

Uniprot ID: [B1XDG0](https://www.uniprot.org/uniprot/B1XDG0)

Protein:  NADPH-dependent curcumin/dihydrocurcumin reductase

Organism: *Escherichia coli (strain K12 / DH10B)*

Length: 345 AA

Taxonomic identifier: [316385](https://www.uniprot.org/taxonomy/316385) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=316385)]

- **Pfam**

| Source | Domain     | Start | End  | E-value (Domain) | Coverage |
| :----- | :--------- | :---- | :--- | ---------------- | :------- |
| Pfam-A | ADH_N_2    | 9     | 115  | 2.4e-43          | 0.981    |
| Pfam-A | ADH_zinc_N | 161   | 299  | 7.4e-19          | 0.946    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

- **Reaction**

[curcumin](https://pubchem.ncbi.nlm.nih.gov/compound/curcumin) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [dihydrocurcumin](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrocurcumin)[intermediate product] + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

[dihydrocurcumin](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrocurcumin)  [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [tetrahydrocurcumin](https://pubchem.ncbi.nlm.nih.gov/compound/tetrahydrocurcumin) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)


![Minion]("../static/images/chemical_structure/OR1/[L1]curcumin.png" alt="[L1]curcumin"）

<figure>
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="zoom:20%"/>
    <img src="../static/images/chemical_structure/OR1/[M1]dihydrocurcimin.png" alt="[M1]dihydrocurcimin" style="zoom:20%;"/>
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="zoom:20%"/>
    <img src="../static/images/chemical_structure/OR1/[R1]tetrahydrocurcumin.png" style="zoom:20%">
</figure>