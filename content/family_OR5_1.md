#  Oxidation/Reduction Reactions (ORs) Family 5 / Subfamily 1

<!--[TOC]在这里不可以用-->

<ul id="myTab" class="nav nav-tabs">
  <!-- active 指的是默认页 -->
  <li class="active">
    <!-- herf中名字于下文id对应 -->
    <!-- 这里只改herf和tab1 -->
    <a href="#tab1" data-toggle="tab">E7FL41</a>
  </li>
  <li><a href="#tab2" data-toggle="tab">F7V1S2</a></li>
  <li><a href="#tab3" data-toggle="tab">H3JUE3</a></li>
  <li><a href="#tab4" data-toggle="tab">M9NYU8</a></li>
</ul>
<div id="myTabContent" class="tab-content" markdown="1">
  <!-- 此处的id与上文herf对应 其他的不要改-->
  <div class="tab-pane fade in active" id="tab1" markdown="1">

##  Literature Information

| Title    | Identification of Two Novel Reductases Involved in Equol Biosynthesis in Lactococcus Strain 20–92 |
| :------- | :----------------------------------------------------------- |
| Author   | Shimada Y. ,· Takahashi M., · Miyazawa N. ,· Ohtani T., · Abiru Y., · Uchiyama S., · Hishigaki H. |
| DOI      | [10.1159/000335049](https://doi.org/10.1159/000335049)       |
| Abstract | *Lactococcus* strain 20–92 is a bacterium that produces equol directly from daidzein under anaerobic conditions. In this study, we reveal that the transcription of the gene encoding daidzein reductase in *Lactococcus* strain 20–92 (L-DZNR), which is responsible for the first stage of the biosynthesis of equol from daidzein, is regulated by the presence of daidzein. We analyzed the sequence surrounding the L-DZNR gene and found six novel genes, termed orf-US4, orf-US3, orf-US2, orf-US1, orf-DS1 and orf-DS2. These genes were expressed in *Escherichia coli,* and the resulting gene products were assayed for dihydrodaidzein reductase (DHDR) and tetrahydrodaidzein reductase (THDR) activity. The results showed that orf-US2 and orf-US3 encoded DHDR and THDR, respectively. DHDR in *Lactococcus* strain 20–92 (L-DHDR) was similar to the 3-oxoacyl-acyl-carrier-protein reductases of several bacteria and belonged to the short chain dehydrogenase/reductase family. THDR in *Lactococcus* strain 20–92 (L-THDR) was similar to several putative fumarate reductase/succinate dehydrogenase flavoprotein domain proteins. L-DHDR required NAD(P)H for its activity, whereas L-THDR required neither NADPH nor NADH. Thus, we succeeded in identifying two novel enzymes that are related to the second and third stages of the biosynthetic pathway that converts daidzein to equol. |

##  Experimental results

- **Enzyme**

Uniprot ID: [E7FL41](https://www.uniprot.org/uniprot/E7FL41)

Protein: Dihydrodaidzein reductase

Organism: *Lactococcus garvieae*

Length: 286 AA

Taxonomic identifier: [1363](https://www.uniprot.org/taxonomy/1363) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=1363)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | adh_short_C2 | 39    | 272  | 1.7e-45          | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

adh_short_C2

[**Pfam**](https://pfam.xfam.org/family/adh_short_C2)

This domain is found in Enoyl-(Acyl carrier protein) reductases.

[**InterPro**](http://www.ebi.ac.uk/interpro/)

No InterPro results.

- **Reaction**

[dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrodaidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [tetrahydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/tetrahydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L1]dihydrodaidzein.png" alt="[L1]dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R1]tetrahydrodaidzein.png" alt="[R1]tetrahydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

  </div>
  <div class="tab-pane fade" id="tab2" markdown="1">

##  Literature Information

| Title    | The production of S-equol from daidzein is associated with a cluster of three genes in Eggerthella sp. YY7918 |
| :------- | :----------------------------------------------------------- |
| Author   | Yuika Kawada , Shinichiro Yokoyama , Emiko Yanase , Toshio Niwa , Tohru Suzuki |
| DOI      | [10.12938/bmfh.2015-023](https://doi.org/10.12938/bmfh.2015-023) |
| Abstract | ==Daidzein== (DZN) is converted to equol (EQL) by intestinal bacteria. We previously reported that Eggerthella sp. YY7918, which is found in human feces, is an EQL-producing bacterium and analyzed its whole genomic sequence. We found three coding sequences (CDSs) in this bacterium that showed 99% similarity to the EQL-producing enzymes of Lactococcus sp. 20-92. These identified CDSs were designated eqlA, eqlB, and eqlC and thought to encode daidzein reductase (DZNR), dihydrodaidzein reductase (DHDR), and tetrahydrodaidzein reductase (THDR), respectively. These genes were cloned into pColdII. Recombinant plasmids were then introduced into Escherichia coli BL21 (DE3) and DZNR, DHDR, and THDR were expressed and purified by 6×His-Tag chromatography. We confirmed that these three enzymes were involved in the conversion of DZN to EQL. Purified DZNR converted DZN to ==dihydrodaizein== (DHD) in the presence of NADPH. DHDR converted DHD to ==tetrahydrodaizein== (THD) in the presence of NADPH. Neither enzyme showed activities with NADH. THDR converted THD in the absence of cofactors, NAD(P)H, and also produced DHD as a by-product. Thus, we propose that THDR is not a reductase but a new type of dismutase. The GC content of these clusters was 64%, similar to the overall genomic GC content for Eggerthella and Coriobacteriaceae (56-60%), and higher than that for Lactococcus garvieae (39%), even though the gene cluster showed 99% similarity to that in Lactococcus sp. 20-92. Taken together, our results indicate that the gene cluster associated with EQL production evolved in high-GC bacteria including Coriobacteriaceae and was then laterally transferred to Lactococcus sp. 20-92. |

##  Experimental results

- **Enzyme**

Uniprot ID: [F7V1S2](https://www.uniprot.org/uniprot/F7V1S2)

Protein: Uncharacterized protein

Organism: *Eggerthella sp. (strain YY7918)*

Length: 286 AA

Taxonomic identifier: [502558](https://www.uniprot.org/taxonomy/502558) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=502558)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | adh_short_C2 | 39    | 272  | 4e-45            | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

adh_short_C2

[**Pfam**](https://pfam.xfam.org/family/adh_short_C2)

This domain is found in Enoyl-(Acyl carrier protein) reductases.

[**InterPro**](http://www.ebi.ac.uk/interpro/)

No InterPro results.

- **Reaction**

[dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrodaidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [tetrahydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/tetrahydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L1]dihydrodaidzein.png" alt="[L1]dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R1]tetrahydrodaidzein.png" alt="[R1]tetrahydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

  </div>
  <div class="tab-pane fade" id="tab3" markdown="1">

##  Literature Information

| Title    | Identification of an Enzyme System for Daidzein-to-Equol Conversion in *Slackia* sp. Strain NATTS |
| :------- | :----------------------------------------------------------- |
| Author   | Hirokazu Tsuji, Kaoru Moriyama, Koji Nomoto, Hideyuki Akaza  |
| DOI      | [10.1128/AEM.06779-11](https://doi.org/10.1128/AEM.06779-11) |
| Abstract | An *Escherichia coli* library comprising 8,424 strains incorporating gene fragments of the equol-producing bacterium *Slackia* sp. strain NATTS was constructed and screened for *E. coli* strains having daidzein- and dihydrodaidzein (DHD)- metabolizing activity. We obtained 3 clones that functioned to convert ==daidzein== to DHD and 2 clones that converted DHD to equol. We then sequenced the gene fragments inserted into plasmids contained by these 5 clones. All of the gene fragments were contiguous, encoding three open reading frames (ORF-1, -2, and -3). Analysis of *E. coli* strains containing an expression vector incorporating one of the *orf-1*, *-2*, or *-3* genes revealed that (i) the protein encoded by *orf*-*1* was involved in the conversion of ==*cis/trans-*tetrahydrodaidzein== (*cis/trans-*THD) to ==equol==, (ii) the protein encoded by *orf*-*2* was involved in the conversion of DHD to *cis/trans-*THD, and (iii) the protein encoded by *orf*-*3* was involved in the conversion of daidzein to DHD. ORF-1 had a primary amino acid structure similar to that of succinate dehydrogenase. ORF-2 was presumed to be an enzyme belonging to the short-chain dehydrogenase/reductase superfamily. ORF-3 was predicted to have 42% identity to the daidzein reductase of *Lactococcus* strain 20-92 and belonged to the NADH:flavin oxidoreductase family. These findings showed that the daidzein-to-equol conversion reaction in the *Slackia* sp. NATTS strain proceeds by the action of these three enzymes. |

##  Experimental results

- **Enzyme**

Uniprot ID: [H3JUE3](https://www.uniprot.org/uniprot/H3JUE3)

Protein: DHD-to-equol conversion enzyme 2

Organism: *Slackia sp. NATTS*

Length: 282 AA

Taxonomic identifier: [647703](https://www.uniprot.org/taxonomy/647703) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=647703)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | adh_short_C2 | 36    | 269  | 5e-45            | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

adh_short_C2

[**Pfam**](https://pfam.xfam.org/family/adh_short_C2)

This domain is found in Enoyl-(Acyl carrier protein) reductases.

[**InterPro**](http://www.ebi.ac.uk/interpro/)

No InterPro results.

- **Reaction**

[dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrodaidzein) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [tetrahydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/tetrahydrodaidzein) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L1]dihydrodaidzein.png" alt="[L1]dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R1]tetrahydrodaidzein.png" alt="[R1]tetrahydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/E7FL41_F7V1S2_H3JUE3/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

  </div>
  <div class="tab-pane fade" id="tab4" markdown="1">

##  Literature Information

| Title    | Identification and expression of genes involved in the conversion of daidzein and genistein by the equol-forming *Slackia isoflavoniconvertens* |
| :------- | :----------------------------------------------------------- |
| Author   | Christine Schröder, Anastasia Matthies, Wolfram Engst, Michael Blaut, Annett Braune |
| DOI      | [10.1128/AEM.03693-12](https://doi.org/10.1128/AEM.03693-12) |
| Abstract | Gut bacteria play a key role in the metabolism of dietary isoflavones, thereby influencing the availability and bioactivation of these polyphenols in the intestine. The human intestinal *Slackia isoflavoniconvertens* converts the main soybean isoflavones daidzein and genistein to equol and 5-hydroxy-equol, respectively. Cell extracts of *S. isoflavoniconvertens* catalyzed the conversion of daidzein *via* dihydrodaidzein to equol and that of genistein to dihydrogenistein. Growth of *S. isoflavoniconvertens* in the presence of daidzein led to the induction of several proteins as observed by two-dimensional difference gel electrophoresis. Based on determined peptide sequences, we identified a cluster of eight genes encoding the daidzein-induced proteins. Heterologous expression of three of these genes in *Escherichia coli* and enzyme activity tests with resulting cell extracts identified the corresponding gene products as a daidzein reductase (DZNR), a dihydrodaidzein reductase (DHDR) and a tetrahydrodaidzein reductase (THDR). The recombinant DZNR also converted ==genistein== to ==dihydrogenistein== at higher rates than observed for the conversion of daidzein to dihydrodaidzein. Higher rates were also observed with cell extracts of *S. isoflavoniconvertens*. The recombinant DHDR and THDR catalyzed the reduction of ==dihydrodaidzein== to ==equol==, while the corresponding conversion of dihydrogenistein to 5-hydroxy-equol was not observed. The DZNR, DHDR and THDR were expressed as *Strep*-tag fusion proteins and subsequently purified by affinity chromatography. The purified enzymes were further characterized with regard to their activity, stereochemistry, quaternary structure, and content of flavin cofactors. |

##  Experimental results

- **Enzyme**

Uniprot ID: [M9NYU8](https://www.uniprot.org/uniprot/M9NYU8)

Protein: 3-oxoacyl-ACP reductase

Organism: *Slackia isoflavoniconvertens*

Length: 486 AA

Taxonomic identifier: [ 572010](https://www.uniprot.org/taxonomy/572010) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=572010)]

- **Pfam**

| Source | Domain       | Start | End  | E-value (Domain) | Coverage |
| :----- | :----------- | :---- | :--- | :--------------- | :------- |
| Pfam-A | adh_short_C2 | 39    | 272  | 1.3e-45          | 0.991    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

adh_short_C2

[**Pfam**](https://pfam.xfam.org/family/adh_short_C2)

This domain is found in Enoyl-(Acyl carrier protein) reductases.

[**InterPro**](http://www.ebi.ac.uk/interpro/)

No InterPro results.

- **Reaction**

*Recombined with [M9P0B3](https://www.uniprot.org/uniprot/M9P0B3)*

[dihydrodaidzein](https://pubchem.ncbi.nlm.nih.gov/compound/dihydrodaidzein) &rArr; [equol](https://pubchem.ncbi.nlm.nih.gov/compound/equol)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/M9NYU8/[L1]dihydrodaidzein.png" alt="[L1]dihydrodaidzein" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR5/M9NYU8/[R1]equol.png" alt="[R1]equol" style="width:100%">
  </div>
</div>
</figure>


  </div>
</div>