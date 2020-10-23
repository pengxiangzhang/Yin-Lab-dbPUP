#  Oxidation/Reduction Reactions (ORs) Family 3

<!--[TOC]在这里不可以用-->

<ul id="myTab" class="nav nav-tabs">
  <!-- active 指的是默认页 -->
  <li class="active">
    <!-- herf中名字于下文id对应 -->
    <!-- 这里只改herf和tab1 -->
    <a href="#tab1" data-toggle="tab">A0A0U1WKA6</a>
  </li>
  <li><a href="#tab2" data-toggle="tab">E1CIA4</a></li>
  <li><a href="#tab3" data-toggle="tab">F7V1S0</a></li>
  <li><a href="#tab4" data-toggle="tab">H3JUE4</a></li>
  <li><a href="#tab5" data-toggle="tab">M9NZ71</a></li>
  <li><a href="#tab6" data-toggle="tab">V9P074</a></li>
</ul>
<div id="myTabContent" class="tab-content" markdown="1">
  <!-- 此处的id与上文herf对应 其他的不要改-->
  <div class="tab-pane fade in active" id="tab1" markdown="1">

##  Literature Information

| Title    | Reduction of soy isoflavones by use of *Escherichia coli* whole‐cell biocatalyst expressing isoflavone reductase under aerobic conditions |
| :------- | :----------------------------------------------------------- |
| Author   | Y.‐N. Gao  Q.‐H. Hao  H.‐L. Zhang  B. Zhou  X.‐M. Yu  X.‐L. Wang |
| DOI      | [10.1111/lam.12594](https://doi.org/10.1111/lam.12594)       |
| Abstract | Soy isoflavone metabolites are currently receiving much attention due to the stronger and wider bioactivities than that of isoflavones. Therefore, biosynthesis of isoflavone metabolites by isolated isoflavone biotransforming bacteria is important. However, the biosynthesis process must be under obligate anaerobic conditions due to the reduction reactions catalysed by isoflavone biotransforming bacteria. In this study, we cloned the daidzein and genistein reductase gene (*dgr*) from *Slackia* sp. AUH‐JLC159. The recombinant *Escherichia coli* (*E. coli*) whole‐cell was used for the first time as the biocatalyst for aerobic biosynthesis of ==dihydrodaidzein (DHD)== and ==dihydrogenistein (DHG)== from soy isoflavones daidzein and genistein. Our results indicated that the recombinant *E. coli* whole‐cell was able to reduce daidzein and genistein to DHD and DHG under aerobic conditions, while the maximal concentration of the substrate daidzein or genistein that the *E. coli* whole‐cell was able to convert efficiently was only 0.4 mmol l<sup>−1</sup>. Under the optimized conditions, the maximal concentration of daidzein or genistein that the *E. coli* whole‐cell was able to convert efficiently was increased to 1.4 mmol l<sup>−1</sup>. Our results demonstrated that *E. coli* whole‐cell is an efficient biocatalyst for biosynthesis of isoflavone metabolites under aerobic conditions. |

##  Experimental results

- **Enzyme**

Uniprot ID: [A0A0U1WKA6](https://www.uniprot.org/uniprot/A0A0U1WKA6)

Protein: Daidzein and genistein reductase

Organism: *Slackia sp. AUH-JLC159*

Length: 644 AA

Taxonomic identifier: [1352935](https://www.uniprot.org/taxonomy/1352935) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1352935)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 384   | 601  | 1.3e-20          | 0.813    |
| Pfam-A | Oxidored_FMN | 15    | 338  | 9e-46            | 0.974    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:
   
   &triangleright; dimethylamine dehydrogenase
   
   &triangleright; trimethylamine dehydrogenase
   
   &triangleright; 12-oxophytodienoate reductase
   
   &triangleright; NADPH dehydrogenase
   
   &triangleright; NADH oxidase
   
- **Reaction**

[genistein](https://pubchem.ncbi.nlm.nih.gov/compound/genistein) &rArr; [dihydrogenistein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrogenistein)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/A0A0U1WKA6/[L1]genistein.png" alt="[L1]genistein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/A0A0U1WKA6/[R1]dihydrogenistein.png" alt="[R1]dihydrogenistein" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]:Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]:Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]:Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]:Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]:Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]:Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]:Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]:Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]:Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]:Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]:Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]:Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
  <div class="tab-pane fade" id="tab2" markdown="1">

##  Literature Information

| Title    | Cloning and Expression of a Novel NADP(H)-Dependent Daidzein Reductase, an Enzyme Involved in the Metabolism of Daidzein, from Equol-Producing *Lactococcus* Strain 20-92 |
| :------- | :----------------------------------------------------------- |
| Author   | Yoshikazu Shimada, Setsuko Yasuda, Masayuki Takahashi, Takashi Hayashi, Norihiro Miyazawa, Ikutaro Sato, Yasuhiro Abiru, Shigeto Uchiyama, Haretsugu Hishigaki |
| DOI      | [10.1128/AEM.01101-10](https://doi.org/10.1128/AEM.01101-10) |
| Abstract | Equol is a metabolite produced from daidzein by enteric microflora, and it has attracted a great deal of attention because of its protective or ameliorative ability against several sex hormone-dependent diseases (e.g., menopausal disorder and lower bone density), which is more potent than that of other isoflavonoids. We purified a novel NADP(H)-dependent daidzein reductase (L-DZNR) from *Lactococcus* strain 20-92 (*Lactococcus* 20-92; S. Uchiyama, T. Ueno, and T. Suzuki, international patent WO2005/000042) that is involved in the metabolism of soy isoflavones and equol production and converts ==daidzein== to ==dihydrodaidzein==. Partial amino acid sequences were determined from purified L-DZNR, and the gene encoding L-DZNR was cloned. The nucleotide sequence of this gene consists of an open reading frame of 1,935 nucleotides, and the deduced amino acid sequence consists of 644 amino acids. L-DZNR contains two cofactor binding motifs and an 4Fe-4S cluster. It was further suggested that L-DZNR was an NAD(H)/NADP(H):flavin oxidoreductase belonging to the *o*ld *y*ellow *e*nzyme (OYE) family. Recombinant histidine-tagged L-DZNR was expressed in *Escherichia coli*. The recombinant protein converted daidzein to (*S*)-dihydrodaidzein with enantioselectivity. This is the first report of the isolation of an enzyme related to daidzein metabolism and equol production in enteric bacteria. |

##  Experimental results

- **Enzyme**

Uniprot ID: [E1CIA4](https://www.uniprot.org/uniprot/E1CIA4)

Protein: Daidzein reductase

Organism: *Lactococcus garvieae*

Length: 644 AA

Taxonomic identifier: [1363](https://www.uniprot.org/taxonomy/1363) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1363)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 384   | 601  | 1.8e-20          | 0.813    |
| Pfam-A | Oxidored_FMN | 15    | 338  | 2.5e-46          | 0.974    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:

   &triangleright; dimethylamine dehydrogenase

   &triangleright; trimethylamine dehydrogenase

   &triangleright; 12-oxophytodienoate reductase

   &triangleright; NADPH dehydrogenase

   &triangleright; NADH oxidase

- **Reaction**

[daidzein](https://pubchem.ncbi.nlm.nih.gov/compound/daidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [(S)-dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/(S)-dihydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L1]daidzein.png" alt="[L1]daidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R1](S)-dihydrodaidzein.png" alt="(S)-dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]: Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]: Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]: Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]: Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]: Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]: Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]: Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]: Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]: Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]: Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]: Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]: Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
  <div class="tab-pane fade" id="tab3" markdown="1">

##  Literature Information

| Title    | The production of S-equol from daidzein is associated with a cluster of three genes in Eggerthella sp. YY7918 |
| :------- | :----------------------------------------------------------- |
| Author   | Yuika Kawada , Shinichiro Yokoyama , Emiko Yanase , Toshio Niwa , Tohru Suzuki |
| DOI      | [10.12938/bmfh.2015-023](https://doi.org/10.12938/bmfh.2015-023) |
| Abstract | ==Daidzein== (DZN) is converted to equol (EQL) by intestinal bacteria. We previously reported that Eggerthella sp. YY7918, which is found in human feces, is an EQL-producing bacterium and analyzed its whole genomic sequence. We found three coding sequences (CDSs) in this bacterium that showed 99% similarity to the EQL-producing enzymes of Lactococcus sp. 20-92. These identified CDSs were designated eqlA, eqlB, and eqlC and thought to encode daidzein reductase (DZNR), dihydrodaidzein reductase (DHDR), and tetrahydrodaidzein reductase (THDR), respectively. These genes were cloned into pColdII. Recombinant plasmids were then introduced into Escherichia coli BL21 (DE3) and DZNR, DHDR, and THDR were expressed and purified by 6×His-Tag chromatography. We confirmed that these three enzymes were involved in the conversion of DZN to EQL. Purified DZNR converted DZN to ==dihydrodaizein== (DHD) in the presence of NADPH. DHDR converted DHD to ==tetrahydrodaizein== (THD) in the presence of NADPH. Neither enzyme showed activities with NADH. THDR converted THD in the absence of cofactors, NAD(P)H, and also produced DHD as a by-product. Thus, we propose that THDR is not a reductase but a new type of dismutase. The GC content of these clusters was 64%, similar to the overall genomic GC content for Eggerthella and Coriobacteriaceae (56-60%), and higher than that for Lactococcus garvieae (39%), even though the gene cluster showed 99% similarity to that in Lactococcus sp. 20-92. Taken together, our results indicate that the gene cluster associated with EQL production evolved in high-GC bacteria including Coriobacteriaceae and was then laterally transferred to Lactococcus sp. 20-92. |

##  Experimental results

- **Enzyme**

Uniprot ID: [F7V1S0](https://www.uniprot.org/uniprot/F7V1S0)

Protein: NADH:flavin oxidoreductase

Organism: *Eggerthella sp. (strain YY7918)*

Length: 644 AA

Taxonomic identifier: [502558](https://www.uniprot.org/taxonomy/502558) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=502558)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 384   | 601  | 8.1e-21          | 0.813    |
| Pfam-A | Oxidored_FMN | 15    | 338  | 3.9e-46          | 0.974    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:

   &triangleright; dimethylamine dehydrogenase

   &triangleright; trimethylamine dehydrogenase

   &triangleright; 12-oxophytodienoate reductase

   &triangleright; NADPH dehydrogenase

   &triangleright; NADH oxidase

- **Reaction**

[daidzein](https://pubchem.ncbi.nlm.nih.gov/compound/daidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [(S)-dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/(S)-dihydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L1]daidzein.png" alt="[L1]daidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R1](S)-dihydrodaidzein.png" alt="(S)-dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]: Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]: Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]: Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]: Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]: Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]: Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]: Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]: Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]: Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]: Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]: Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]: Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
  <div class="tab-pane fade" id="tab4" markdown="1">

##  Literature Information

| Title    | Identification of an Enzyme System for Daidzein-to-Equol Conversion in *Slackia* sp. Strain NATTS |
| :------- | :----------------------------------------------------------- |
| Author   | Hirokazu Tsuji, Kaoru Moriyama, Koji Nomoto, Hideyuki Akaza  |
| DOI      | [10.1128/AEM.06779-11](https://doi.org/10.1128/AEM.06779-11) |
| Abstract | An *Escherichia coli* library comprising 8,424 strains incorporating gene fragments of the equol-producing bacterium *Slackia* sp. strain NATTS was constructed and screened for *E. coli* strains having daidzein- and dihydrodaidzein (DHD)- metabolizing activity. We obtained 3 clones that functioned to convert daidzein to DHD and 2 clones that converted DHD to equol. We then sequenced the gene fragments inserted into plasmids contained by these 5 clones. All of the gene fragments were contiguous, encoding three open reading frames (ORF-1, -2, and -3). Analysis of *E. coli* strains containing an expression vector incorporating one of the *orf-1*, *-2*, or *-3* genes revealed that (i) the protein encoded by *orf*-*1* was involved in the conversion of ==*cis/trans-*tetrahydrodaidzein== (*cis/trans-*THD) to ==equol==, (ii) the protein encoded by *orf*-*2* was involved in the conversion of DHD to ==*cis/trans-*THD==, and (iii) the protein encoded by *orf*-*3* was involved in the conversion of ==daidzein== to DHD. ORF-1 had a primary amino acid structure similar to that of succinate dehydrogenase. ORF-2 was presumed to be an enzyme belonging to the short-chain dehydrogenase/reductase superfamily. ORF-3 was predicted to have 42% identity to the daidzein reductase of *Lactococcus* strain 20-92 and belonged to the NADH:flavin oxidoreductase family. These findings showed that the daidzein-to-equol conversion reaction in the *Slackia* sp. NATTS strain proceeds by the action of these three enzymes. |

##  Experimental results

- **Enzyme**

Uniprot ID: [H3JUE4](https://www.uniprot.org/uniprot/H3JUE4)

Protein: Daidzein-to-DHD conversion enzyme

Organism: *Slackia sp. NATTS*

Length: 644 AA

Taxonomic identifier: [647703](https://www.uniprot.org/taxonomy/647703) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=647703)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 384   | 607  | 1.4e-23          | 0.827    |
| Pfam-A | Oxidored_FMN | 9     | 338  | 6.1e-53          | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:

   &triangleright; dimethylamine dehydrogenase

   &triangleright; trimethylamine dehydrogenase

   &triangleright; 12-oxophytodienoate reductase

   &triangleright; NADPH dehydrogenase

   &triangleright; NADH oxidase

- **Reaction**

[daidzein](https://pubchem.ncbi.nlm.nih.gov/compound/daidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [(S)-dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/(S)-dihydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L1]daidzein.png" alt="[L1]daidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R1](S)-dihydrodaidzein.png" alt="(S)-dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/E1CIA4_F7V1S0_H3JUE4/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]: Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]: Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]: Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]: Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]: Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]: Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]: Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]: Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]: Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]: Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]: Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]: Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
  <div class="tab-pane fade" id="tab5" markdown="1">

##  Literature Information

| Title    | Identification and expression of genes involved in the conversion of daidzein and genistein by the equol-forming *Slackia isoflavoniconvertens* |
| :------- | :----------------------------------------------------------- |
| Author   | Christine Schröder, Anastasia Matthies, Wolfram Engst, Michael Blaut, Annett Braune |
| DOI      | [10.1128/AEM.03693-12](https://doi.org/10.1128/AEM.03693-12) |
| Abstract | Gut bacteria play a key role in the metabolism of dietary isoflavones, thereby influencing the availability and bioactivation of these polyphenols in the intestine. The human intestinal *Slackia isoflavoniconvertens* converts the main soybean isoflavones daidzein and genistein to equol and 5-hydroxy-equol, respectively. Cell extracts of *S. isoflavoniconvertens* catalyzed the conversion of daidzein *via* dihydrodaidzein to equol and that of genistein to dihydrogenistein. Growth of *S. isoflavoniconvertens* in the presence of daidzein led to the induction of several proteins as observed by two-dimensional difference gel electrophoresis. Based on determined peptide sequences, we identified a cluster of eight genes encoding the daidzein-induced proteins. Heterologous expression of three of these genes in *Escherichia coli* and enzyme activity tests with resulting cell extracts identified the corresponding gene products as a daidzein reductase (DZNR), a dihydrodaidzein reductase (DHDR) and a tetrahydrodaidzein reductase (THDR). The recombinant DZNR also converted ==genistein== to ==dihydrogenistein== at higher rates than observed for the conversion of daidzein to dihydrodaidzein. Higher rates were also observed with cell extracts of *S. isoflavoniconvertens*. The recombinant DHDR and THDR catalyzed the reduction of dihydrodaidzein to equol, while the corresponding conversion of dihydrogenistein to 5-hydroxy-equol was not observed. The DZNR, DHDR and THDR were expressed as *Strep*-tag fusion proteins and subsequently purified by affinity chromatography. The purified enzymes were further characterized with regard to their activity, stereochemistry, quaternary structure, and content of flavin cofactors. |

##  Experimental results

- **Enzyme**

Uniprot ID: [M9NZ71](https://www.uniprot.org/uniprot/M9NZ71)

Protein: Daidzein reductase

Organism: *Slackia isoflavoniconvertens*

Length: 644 AA

Taxonomic identifier: [572010](https://www.uniprot.org/taxonomy/572010) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=572010)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 384   | 607  | 4e-23            | 0.827    |
| Pfam-A | Oxidored_FMN | 9     | 337  | 1.1e-52          | 0.988    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:

   &triangleright; dimethylamine dehydrogenase

   &triangleright; trimethylamine dehydrogenase

   &triangleright; 12-oxophytodienoate reductase

   &triangleright; NADPH dehydrogenase

   &triangleright; NADH oxidase

- **Reaction**

[genistein](https://pubchem.ncbi.nlm.nih.gov/compound/genistein) &rArr; [dihydrogenistein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrogenistein)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/A0A0U1WKA6/[L1]genistein.png" alt="[L1]genistein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/A0A0U1WKA6/[R1]dihydrogenistein.png" alt="[R1]dihydrogenistein" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]: Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]: Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]: Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]: Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]: Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]: Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]: Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]: Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]: Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]: Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]: Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]: Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
  <div class="tab-pane fade" id="tab6" markdown="1">

##  Literature Information

| Title    | An NADH-Dependent Reductase from *Eubacterium ramulus* Catalyzes the Stereospecific Heteroring Cleavage of Flavanones and Flavanonols |
| :------- | :----------------------------------------------------------- |
| Author   | Annett Braune, Michael Gütschow, Michael Blaut               |
| DOI      | [10.1128/AEM.01233-19](https://doi.org/10.1128/AEM.01233-19) |
| Abstract | The human intestinal anaerobe *Eubacterium ramulus* is known for its ability to degrade various dietary flavonoids. In the present study, we demonstrate the cleavage of the heterocyclic C-ring of flavanones and flavanonols by an oxygen-sensitive NADH-dependent reductase, previously described as enoate reductase, from *E. ramulus*. This flavanone- and flavanonol-cleaving reductase (Fcr) was purified following its heterologous expression in *Escherichia coli* and further characterized. Fcr cleaved the flavanones naringenin, eriodictyol, liquiritigenin, and homoeriodictyol. Moreover, the flavanonols taxifolin and dihydrokaempferol served as substrates. The catalyzed reactions were stereospecific for the (2*R*)-enantiomers of the flavanone substrates and for the (2*S*,3*S*)-configured flavanonols. The enantioenrichment of the nonconverted stereoisomers allowed for the determination of hitherto unknown flavanone racemization rates. Fcr formed the corresponding dihydrochalcones and hydroxydihydrochalcones in the course of an unusual reductive cleavage of cyclic ether bonds. Fcr did not convert members of other flavonoid subclasses, including flavones, flavonols, and chalcones, the latter indicating that the reaction does not involve a chalcone intermediate. This view is strongly supported by the observed enantiospecificity of Fcr. Cinnamic acids, which are typical substrates of bacterial enoate reductases, were also not reduced by Fcr. Based on the presence of binding motifs for dinucleotide cofactors and a 4Fe-4S cluster in the amino acid sequence of Fcr, a cofactor-mediated hydride transfer from NADH onto C-2 of the respective substrate is proposed. |

##  Experimental results

- **Enzyme**

Uniprot ID: [V9P074](https://www.uniprot.org/uniprot/V9P074)

Protein: Enoate reductase

Organism: *Eubacterium ramulus*

Length: 678 AA

Taxonomic identifier: [39490](https://www.uniprot.org/taxonomy/39490) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=39490)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | Pyr_redox_2  | 418   | 648  | 3.3e-21          | 0.840    |
| Pfam-A | Oxidored_FMN | 11    | 356  | 1.2e-50          | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

1. Pyr_redox_2

   [**Pfam**](https://pfam.xfam.org/family/Pyr_redox_2)

   This family includes both class I and class II oxidoreductases and also NADH oxidases and peroxidases. This domain is actually a small NADH binding domain within a larger FAD binding domain[^1].

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR023753/)

   FAD flavoproteins belonging to the family of pyridine nucleotide-disulphide oxidoreductases (glutathione reductase, trypanothione reductase, lipoamide dehydrogenase, mercuric reductase, thioredoxin reductase, alkyl hydroperoxide reductase) share sequence similarity with a number of other flavoprotein oxidoreductases, in particular with ferredoxin-NAD+ reductases involved in oxidative metabolism of a variety of hydrocarbons (rubredoxin reductase, putidaredoxin reductase, terpredoxin reductase, ferredoxin-NAD+ reductase components of benzene 1,2-dioxygenase, toluene 1,2-dioxygenase, chlorobenzene dioxygenase, biphenyl dioxygenase), NADH oxidase and NADH peroxidase [cite:PUB00003255], [cite:PUB00003296], [cite:PUB00004100] . Comparison of the crystal structures of human glutathione reductase and Escherichia coli thioredoxin reductase reveals different locations of their active sites, suggesting that the enzymes diverged from an ancestral FAD/NAD(P)H reductase and acquired their disulphide reductase activities independently[^2].

   Despite functional similarities, oxidoreductases of this family show no sequence similarity with adrenodoxin reductases[^3] and flavoprotein pyridine nucleotide cytochrome reductases (FPNCR)[^4]. Assuming that disulphide reductase activity emerged later, during divergent evolution, the family can be referred to as FAD-dependent pyridine nucleotide reductases, FADPNR.

   To date, 3D structures of glutathione reductase[^5], thioredoxin reductase[^2], mercuric reductase[^6], lipoamide dehydrogenase[^7], trypanothione reductase[^8] and NADH peroxidas[^9] have been solved. The enzymes share similar tertiary structures based on a doubly-wound alpha/beta fold, but the relative orientations of their FAD- and NAD(P)H-binding domains may vary significantly. By contrast with the FPNCR family, the folds of the FAD- and NAD(P)H-binding domains are similar, suggesting that the domains evolved by gene duplication[^10].

   This entry describes the FAD binding domain which has a nested NADH binding domain and is found in both class I and class II oxidoreductases.

2. Oxidored_FMN

   [**Pfam**](https://pfam.xfam.org/family/Oxidored_FMN)

   No Pfam abstract.

   [**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR001155/)

   The TIM-barrel fold is a closed barrel structure composed of an eight-fold repeat of beta-alpha units, where the eight parallel beta strands on the inside are covered by the eight alpha helices on the outside[^11]. It is a widely distributed fold which has been found in many enzyme families that catalyse completely unrelated reactions[^12]. The active site is always found at the C-terminal end of this domain.

   Proteins in this entry are a variety of NADH:flavin oxidoreductase/NADH oxidase enzymes, found mostly in bacteria or fungi, that contain a TIM-barrel fold. They commonly use FMN/FAD as cofactor and include:

   &triangleright; dimethylamine dehydrogenase

   &triangleright; trimethylamine dehydrogenase

   &triangleright; 12-oxophytodienoate reductase

   &triangleright; NADPH dehydrogenase

   &triangleright; NADH oxidase

- **Reaction**

[naringenin](https://pubchem.ncbi.nlm.nih.gov/compound/naringenin) + [NADH](https://pubchem.ncbi.nlm.nih.gov/compound/439153) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [phloretin](https://pubchem.ncbi.nlm.nih.gov/compound/phloretin) + [NAD<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/5892)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/V9P074/[L1]naringenin.png" alt="[L1]naringenin" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/V9P074/[L2]NADH.png" alt="NADH" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/V9P074/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/V9P074/[R1]phloretin.png" alt="[R1]phloretin" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR3/V9P074/[R2]NAD+.png" alt="[R2]NAD+" style="width:100%">
  </div>
</div>
</figure>


## References

[^1]: Mande S S, Sarfaty S, Allen M D, et al. Protein–protein interactions in the pyruvate dehydrogenase multienzyme complex: dihydrolipoamide dehydrogenase complexed with the binding domain of dihydrolipoamide acetyltransferase[J]. Structure, 1996, 4(3): 277-286.
[^2]: Kuriyan J, Krishna T S R, Wong L, et al. Convergent evolution of similar function in two structurally divergent enzymes[J]. Nature, 1991, 352(6331): 172-174.
[^3]: Hanukoglu I, Gutfinger T. cDNA sequence of adrenodoxin reductase: Identification of NADP‐binding sites in oxidoreductases[J]. European journal of biochemistry, 1989, 180(2): 479-484.
[^4]: Hyde G E, Crawford N M, Campbell W H. The sequence of squash NADH: nitrate reductase and its relationship to the sequences of other flavoprotein oxidoreductases. A family of flavoprotein pyridine nucleotide cytochrome reductases[J]. Journal of Biological Chemistry, 1991, 266(35): 23542-23547.
[^5]: Karplus P A, Schulz G E. Refined structure of glutathione reductase at 1.54 Å resolution[J]. Journal of molecular biology, 1987, 195(3): 701-729.
[^6]: Schiering N, Kabsch W, Moore M J, et al. Structure of the detoxification catalyst mercuric ion reductase from Bacillus sp. strain RC607[J]. Nature, 1991, 352(6331): 168-172.
[^7]: Mattevi A, Schierbeek A J, Hol W G J. Refined crystal structure of li[poamide dehydrogenase from Azotobacter vinelandii at 2.2 Å resolution: A comparison with the structure of glutathione reductase[J]. Journal of molecular biology, 1991, 220(4): 975-994.
[^8]: Kuriyan J, Kong X P, Krishna T S, et al. X-ray structure of trypanothione reductase from Crithidia fasciculata at 2.4-A resolution[J]. Proceedings of the National Academy of Sciences, 1991, 88(19): 8764-8768.
[^9]: Stehle T, Ahmed S A, Claiborne A, et al. Structure of NADH peroxidase from Streptococcus faecalis 10C1 refined at 2.16 Åresolution[J]. Journal of molecular biology, 1991, 221(4): 1325-1344.
[^10]: Schulz G E. Gene duplication in glutathione reductase[J]. Journal of molecular biology, 1980, 138(2): 335-347.
[^11]: Wierenga R K. The TIM-barrel fold: a versatile framework for efficient enzymes[J]. FEBS letters, 2001, 492(3): 193-198.
[^12]: Nagano N, Orengo C A, Thornton J M. One fold with many functions: the evolutionary relationships between TIM barrel families based on their sequences, structures and functions[J]. Journal of molecular biology, 2002, 321(5): 741-765.

  </div>
</div>