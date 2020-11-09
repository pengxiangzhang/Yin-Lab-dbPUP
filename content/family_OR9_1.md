#  Oxidation/Reduction Reactions (ORs) Family 9 / Subfamily 1

<!--[TOC]在这里不可以用-->

<ul id="myTab" class="nav nav-tabs">
  <!-- active 指的是默认页 -->
  <li class="active">
    <!-- herf中名字于下文id对应 -->
    <!-- 这里只改herf和tab1 -->
    <a href="#tab1" data-toggle="tab">G2IMF2</a>
  </li>
  <li><a href="#tab2" data-toggle="tab">Q2G4H9</a></li>
</ul>
<div id="myTabContent" class="tab-content" markdown="1">
  <!-- 此处的id与上文herf对应 其他的不要改-->
  <div class="tab-pane fade in active" id="tab1" markdown="1">

##  Literature Information

| Title    | Discovery of pinoresinol reductase genes in sphingomonads    |
| :------- | :----------------------------------------------------------- |
| Author   | Y Fukuhara, N Kamimura, M Nakajima, S Hishiyama, H Hara, D Kasai, Y Tsuji, S Narita-Yamada, S Nakamura, Y Katano, N Fujita, Y Katayama, M Fukuda, S Kajita, E Masai |
| DOI      | [10.1016/j.enzmictec.2012.10.004](https://doi.org/10.1016/j.enzmictec.2012.10.004) |
| Abstract | Bacterial genes for the degradation of major dilignols produced in lignifying xylem are expected to be useful tools for the structural modification of lignin in plants. For this purpose, we isolated pinZ involved in the conversion of pinoresinol from Sphingobium sp. strain SYK-6. pinZ showed 43-77% identity at amino acid level with bacterial NmrA-like proteins of unknown function, a subgroup of atypical short chain dehydrogenases/reductases, but revealed only 15-21% identity with plant pinoresinol/lariciresinol reductases. PinZ completely converted ==racemic pinoresinol== to ==lariciresinol==, showing a specific activity of 46±3 U/mg in the presence of NADPH at 30°C. In contrast, the activity for lariciresinol was negligible. This substrate preference is similar to a pinoresinol reductase, AtPrR1, of Arabidopsis thaliana; however, the specific activity of PinZ toward (±)-pinoresinol was significantly higher than that of AtPrR1. The role of pinZ and a pinZ ortholog of Novosphingobium aromaticivorans DSM 12444 were also characterized. |

##  Experimental results

- **Enzyme**

Uniprot ID: [G2IMF2](https://www.uniprot.org/uniprot/G2IMF2)

Protein:  Putative oxidoreductase

Organism: *Sphingobium sp. (strain NBRC 103272 / SYK-6)*

Length: 316 AA

Taxonomic identifier: [627192](https://www.uniprot.org/taxonomy/627192) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=627192)]

- **Pfam**

| Source | Domain         | Start | End  | E-value (Domain) | Coverage |
| ------ | -------------- | ----- | ---- | ---------------- | -------- |
| Pfam-A | NAD_binding_10 | 11    | 193  | 3.4e-20          | 0.995    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

NAD_binding_10

[**Pfam**](https://pfam.xfam.org/family/NAD_binding_10)

No Pfam abstract.

[**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR016040/)

This entry represents NAD- and NADP-binding domains with a core Rossmann-type fold, which consists of 3-layers alpha/beta/alpha, where the six beta strands are parallel in the order 321456. Many different enzymes contain an NAD/NADP-binding domain, including:

 &triangleright;C-terminal domain of alcohol dehydrogenases[^1]

 &triangleright;Tyrosine-dependent oxidoreductases (also known as short-chain dehydrogenases)[^2]

 &triangleright;N-terminal domain of glyceraldehyde-3-phosphate dehydrogenase[^3]

 &triangleright;NAD-binding domain of formate/glycerate dehydrogenases[^4]

 &triangleright;N-terminal domain of sirohaem synthase[^5]

 &triangleright;N-terminal domain of lactate dehydrogenase[^6]

 &triangleright;N-terminal domain of 6-phosphogluconate dehydrogenase (the beta-sheet is extended to 8 strands)[^7]

 &triangleright;C-terminal domain of amino acid dehydrogenases (an extra N-terminal helix displaces the C-terminal helix[^8]

 &triangleright;NAD-binding domain of certain potassium channels[^9]

 &triangleright;C-terminal domain of the transcriptional repressor Rex[^10]

 &triangleright;Ornithine cyclodeaminase[^11]

 &triangleright;CoA-binding N-terminal domain of the alpha chain of succinyl-CoA synthetase[^12]

- **Reaction**

[pinoresinol](https://pubchem.ncbi.nlm.nih.gov/compound/pinoresinol) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [lariciresinol](https://pubchem.ncbi.nlm.nih.gov/compound/lariciresinol) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L1]pinoresinol.png" alt="[L1]pinoresinol" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[R1]lariciresinol.png" alt="[R1]lariciresinol" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]:Gibbons B J, Hurley T D. Structure of three class I human alcohol dehydrogenases complexed with isoenzyme specific formamide inhibitors[J]. Biochemistry, 2004, 43(39): 12555-12562.
[^2]:Thoden J B, Hegeman A D, Wesenberg G, et al. Structural analysis of UDP-sugar binding to UDP-galactose 4-epimerase from Escherichia coli[J]. Biochemistry, 1997, 36(21): 6294-6304.
[^3]:Isupov M N, Fleming T M, Dalby A R, et al. Crystal structure of the glyceraldehyde-3-phosphate dehydrogenase from the hyperthermophilic archaeon Sulfolobus solfataricus[J]. Journal of molecular biology, 1999, 291(3): 651-660.
[^4]:Lamzin V S, Dauter Z, Popov V O, et al. High resolution structures of holo and apo formate dehydrogenase[J]. Journal of molecular biology, 1994, 236(3): 759-785.
[^5]:Stroupe M E, Leech H K, Daniels D S, et al. CysG structure reveals tetrapyrrole-binding features and novel regulation of siroheme biosynthesis[J]. Nature Structural & Molecular Biology, 2003, 10(12): 1064-1073.
[^6]:Read J A, Winter V J, Eszes C M, et al. Structural basis for altered activity of M‐and H‐isozyme forms of human lactate dehydrogenase[J]. Proteins: Structure, function, and bioinformatics, 2001, 43(2): 175-185.
[^7]:Sundaramoorthy R, Iulek J, Barrett M P, et al. Crystal structures of a bacterial 6‐phosphogluconate dehydrogenase reveal aspects of specificity, mechanism and mode of inhibition by analogues of high‐energy reaction intermediates[J]. The FEBS journal, 2007, 274(1): 275-286.
[^8]:Yip K S P, Stillman T J, Britton K L, et al. The structure of Pyrococcus furiosus glutamate dehydrogenase reveals a key role for ion-pair networks in maintaining enzyme stability at extreme temperatures[J]. Structure, 1995, 3(11): 1147-1158.
[^9]:Jiang Y, Pico A, Cadene M, et al. Structure of the RCK domain from the E. coli K+ channel and demonstration of its presence in the human BK channel[J]. Neuron, 2001, 29(3): 593-601.
[^10]:Sickmier E A, Brekasis D, Paranawithana S, et al. X-ray structure of a Rex-family repressor/NADH complex insights into the mechanism of redox sensing[J]. Structure, 2005, 13(1): 43-54.
[^11]:Goodman J L, Wang S, Alam S, et al. Ornithine cyclodeaminase: structure, mechanism of action, and implications for the μ-crystallin family[J]. Biochemistry, 2004, 43(44): 13883-13891.
[^12]:Fraser M E, James M N G, Bridger W A, et al. A detailed structural description of Escherichia coli succinyl-CoA synthetase[J]. Journal of molecular biology, 1999, 285(4): 1633-1653.

  </div>
  <div class="tab-pane fade" id="tab2" markdown="1">

##  Literature Information

| Title    | Discovery of pinoresinol reductase genes in sphingomonads    |
| :------- | :----------------------------------------------------------- |
| Author   | Y Fukuhara, N Kamimura, M Nakajima, S Hishiyama, H Hara, D Kasai, Y Tsuji, S Narita-Yamada, S Nakamura, Y Katano, N Fujita, Y Katayama, M Fukuda, S Kajita, E Masai |
| DOI      | [10.1016/j.enzmictec.2012.10.004](https://doi.org/10.1016/j.enzmictec.2012.10.004) |
| Abstract | Bacterial genes for the degradation of major dilignols produced in lignifying xylem are expected to be useful tools for the structural modification of lignin in plants. For this purpose, we isolated pinZ involved in the conversion of pinoresinol from Sphingobium sp. strain SYK-6. pinZ showed 43-77% identity at amino acid level with bacterial NmrA-like proteins of unknown function, a subgroup of atypical short chain dehydrogenases/reductases, but revealed only 15-21% identity with plant pinoresinol/lariciresinol reductases. PinZ completely converted ==racemic pinoresinol== to ==lariciresinol==, showing a specific activity of 46±3 U/mg in the presence of NADPH at 30°C. In contrast, the activity for lariciresinol was negligible. This substrate preference is similar to a pinoresinol reductase, AtPrR1, of Arabidopsis thaliana; however, the specific activity of PinZ toward (±)-pinoresinol was significantly higher than that of AtPrR1. The role of pinZ and a pinZ ortholog of Novosphingobium aromaticivorans DSM 12444 were also characterized. |

##  Experimental results

- **Enzyme**

Uniprot ID: [Q2G4H9](https://www.uniprot.org/uniprot/Q2G4H9)

Protein:  NmrA-like protein

Organism: *Novosphingobium aromaticivorans (strain ATCC 700278 / DSM 12444 / CIP 105152 / NBRC 16084 / F199)*

Length: 305 AA

Taxonomic identifier: [279238](https://www.uniprot.org/taxonomy/279238) [[NCBI](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?lvl=0&id=279238)]

- **Pfam**

| Source | Domain         | Start | End  | E-value (Domain) | Coverage |
| ------ | -------------- | ----- | ---- | ---------------- | -------- |
| Pfam-A | NAD_binding_10 | 8     | 147  | 1.1e-20          | 0.804    |

Program: `hmmscan`

Version: 3.1b2 (February 2015)

Method: `hmmscan --domtblout hmmscan.tbl --noali -E 1e-5 pfam query.fa `

Date: Mon Jul 20 14:32:16 2020

Description:

NAD_binding_10

[**Pfam**](https://pfam.xfam.org/family/NAD_binding_10)

No Pfam abstract.

[**InterPro**](http://www.ebi.ac.uk/interpro/entry/InterPro/IPR016040/)

This entry represents NAD- and NADP-binding domains with a core Rossmann-type fold, which consists of 3-layers alpha/beta/alpha, where the six beta strands are parallel in the order 321456. Many different enzymes contain an NAD/NADP-binding domain, including:

 &triangleright;C-terminal domain of alcohol dehydrogenases[^1]

 &triangleright;Tyrosine-dependent oxidoreductases (also known as short-chain dehydrogenases)[^2]

 &triangleright;N-terminal domain of glyceraldehyde-3-phosphate dehydrogenase[^3]

 &triangleright;NAD-binding domain of formate/glycerate dehydrogenases[^4]

 &triangleright;N-terminal domain of sirohaem synthase[^5]

 &triangleright;N-terminal domain of lactate dehydrogenase[^6]

 &triangleright;N-terminal domain of 6-phosphogluconate dehydrogenase (the beta-sheet is extended to 8 strands)[^7]

 &triangleright;C-terminal domain of amino acid dehydrogenases (an extra N-terminal helix displaces the C-terminal helix[^8]

 &triangleright;NAD-binding domain of certain potassium channels[^9]

 &triangleright;C-terminal domain of the transcriptional repressor Rex[^10]

 &triangleright;Ornithine cyclodeaminase[^11]

 &triangleright;CoA-binding N-terminal domain of the alpha chain of succinyl-CoA synthetase[^12]

- **Reaction**

[pinoresinol](https://pubchem.ncbi.nlm.nih.gov/compound/pinoresinol) + [NADPH](https://pubchem.ncbi.nlm.nih.gov/compound/5884) + [H<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/1038) &rArr; [lariciresinol](https://pubchem.ncbi.nlm.nih.gov/compound/lariciresinol) + [NADP<sup>+</sup>](https://pubchem.ncbi.nlm.nih.gov/compound/15938972)

<figure>
<div class="linerow">
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L1]pinoresinol.png" alt="[L1]pinoresinol" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L2]NADPH.png" alt="nadph" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[L3]hydrogen cation.png" alt="h+" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/right_arrow.png" alt="right_arrow" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[R1]lariciresinol.png" alt="[R1]lariciresinol" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/common_symbol/plus.png" alt="plus" style="width:100%">
  </div>
  <div class="linecolumn">
    <img src="../static/images/chemical_structure/OR9/[R2]NADP+.png" alt="nadp+" style="width:100%">
  </div>
</div>
</figure>

## References

[^1]: Gibbons B J, Hurley T D. Structure of three class I human alcohol dehydrogenases complexed with isoenzyme specific formamide inhibitors[J]. Biochemistry, 2004, 43(39): 12555-12562.
[^2]: Thoden J B, Hegeman A D, Wesenberg G, et al. Structural analysis of UDP-sugar binding to UDP-galactose 4-epimerase from Escherichia coli[J]. Biochemistry, 1997, 36(21): 6294-6304.
[^3]: Isupov M N, Fleming T M, Dalby A R, et al. Crystal structure of the glyceraldehyde-3-phosphate dehydrogenase from the hyperthermophilic archaeon Sulfolobus solfataricus[J]. Journal of molecular biology, 1999, 291(3): 651-660.
[^4]: Lamzin V S, Dauter Z, Popov V O, et al. High resolution structures of holo and apo formate dehydrogenase[J]. Journal of molecular biology, 1994, 236(3): 759-785.
[^5]: Stroupe M E, Leech H K, Daniels D S, et al. CysG structure reveals tetrapyrrole-binding features and novel regulation of siroheme biosynthesis[J]. Nature Structural & Molecular Biology, 2003, 10(12): 1064-1073.
[^6]: Read J A, Winter V J, Eszes C M, et al. Structural basis for altered activity of M‐and H‐isozyme forms of human lactate dehydrogenase[J]. Proteins: Structure, function, and bioinformatics, 2001, 43(2): 175-185.
[^7]: Sundaramoorthy R, Iulek J, Barrett M P, et al. Crystal structures of a bacterial 6‐phosphogluconate dehydrogenase reveal aspects of specificity, mechanism and mode of inhibition by analogues of high‐energy reaction intermediates[J]. The FEBS journal, 2007, 274(1): 275-286.
[^8]: Yip K S P, Stillman T J, Britton K L, et al. The structure of Pyrococcus furiosus glutamate dehydrogenase reveals a key role for ion-pair networks in maintaining enzyme stability at extreme temperatures[J]. Structure, 1995, 3(11): 1147-1158.
[^9]: Jiang Y, Pico A, Cadene M, et al. Structure of the RCK domain from the E. coli K+ channel and demonstration of its presence in the human BK channel[J]. Neuron, 2001, 29(3): 593-601.
[^10]: Sickmier E A, Brekasis D, Paranawithana S, et al. X-ray structure of a Rex-family repressor/NADH complex insights into the mechanism of redox sensing[J]. Structure, 2005, 13(1): 43-54.
[^11]: Goodman J L, Wang S, Alam S, et al. Ornithine cyclodeaminase: structure, mechanism of action, and implications for the μ-crystallin family[J]. Biochemistry, 2004, 43(44): 13883-13891.
[^12]: Fraser M E, James M N G, Bridger W A, et al. A detailed structural description of Escherichia coli succinyl-CoA synthetase[J]. Journal of molecular biology, 1999, 285(4): 1633-1653.

  </div>
</div>