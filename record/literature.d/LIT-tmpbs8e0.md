---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md)) from the arXiv v2, the version published
  in J. Chem. Phys., main text in full and appendices skimmed; worth
  reading as the dictionary between a chemist's disconnectivity graph and
  zero-dimensional sublevelset persistence, and for what the higher
  dimensions add: alternative transition paths and critical points of every
  index. Its main limits: one model family, the alkane torsional landscape,
  chosen because it is a sum of identical one-dimensional terms; simplified
  physics; MD sampling inadequate from hexane on. One scalar energy only:
  multi-parameter persistence is mentioned once, in a citation, and not
  treated.
title: 'Representations of Energy Landscapes by Sublevelset Persistent Homology: An Example With n-Alkanes'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (pasted 2026-11-04,
    written by another assistant), where it is cited as R6 only as an arXiv paper on sublevel-set persistent homology of molecular energy landscapes, without title or authors. The reader identified it by two arXiv
    searches, each returning this single matching work; the identification
    rests on the description matching its title and subject. Citation
    checked against the arXiv metadata and Crossref: Joshua Mirth, Yanqin
    Zhai, Johnathan Bush, Enrique G. Alvarado, Howie Jordan, Mark Heim, Bala
    Krishnamoorthy, Markus Pflaum, Aurora Clark, Yang Zhang and Henry Adams,
    The Journal of Chemical Physics 154(11), 114114; Crossref online 18
    March 2021; arXiv 2011.00918, v1 2 November 2020, which is
    `published:`. Correction: Crossref and the PDF print the tenth author as
    "Y Z"; the arXiv metadata gives Yang Zhang. Read from the arXiv v2 PDF
    of 19 March 2021 (https://arxiv.org/pdf/2011.00918v2), which states it
    is the published version. Status Active.
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
published: '2020-11-02'
arxiv: '2011.00918'
doi: '10.1063/5.0036747'
first_author: 'Mirth'
keywords:
- 'persistent homology'
- 'sublevelset'
- 'potential energy landscape'
- 'disconnectivity graph'
- 'Morse theory'
- 'n-alkanes'
- 'barcode distances'
implementations: []
summary: >-
  Mirth, Zhai, Bush, Alvarado, Jordan, Heim, Krishnamoorthy, Pflaum, Clark,
  Zhang & Adams (2021). Sublevelset persistent homology records how the
  topology of the set of configurations below an energy threshold changes
  as the threshold rises. Its zero-dimensional part is fixed by the
  disconnectivity graph (minima and the lowest barriers merging them); the
  higher dimensions record transition paths the graph omits and count
  critical points of every index. For the alkane torsional landscape, a sum
  of butane terms on a torus, the authors prove the barcode in every
  dimension, and they use barcode distances to measure how well MD sampling
  recovers a landscape.
---
<!-- inactive-ok-file: THEORY-tmpqzxwh — Proposed; cited from the reading of Mirth et al. (2021) as open -->

# LIT-tmpbs8e0: Representations of Energy Landscapes by Sublevelset Persistent Homology: An Example With n-Alkanes

Mirth, J., Zhai, Y., Bush, J., Alvarado, E. G., Jordan, H., Heim, M., Krishnamoorthy, B., Pflaum, M., Clark, A., Zhang, Y. & Adams, H. (2021). Representations of Energy Landscapes by Sublevelset Persistent Homology: An Example With n-Alkanes. *The Journal of Chemical Physics* 154(11): 114114. doi:10.1063/5.0036747. arXiv:2011.00918.

## Key takeaways

*From the reading, [NOTE-tmpwvb9j](../notes.d/NOTE-tmpwvb9j.md). Sections are the arXiv v2's.*

- **Merge level.** Two configurations are connected at a threshold "if
  there is a path between the configurations that does not exceed the
  chosen energy barrier" (introduction); "the disconnectivity graph of an
  EL completely determines its 0-dimensional sublevelset persistent
  homology" (§II.B).
- **What the graph omits.** Disconnectivity graphs "do not represent
  multiple transition pathways"; so "the timescale computed from a
  disconnectivity graph alone will be an overestimate to a certain degree".
- **Critical points.** Bars count critical points of every index (§IV.A).
- **A closed form.** Theorems 1 and 2 give the barcode of every alkane
  landscape in every dimension.
- **Comparison.** Barcode distances compare landscapes "of different
  dimensionality" and expose poor sampling.

## Standing in the record

Cited in the pasted synthesis on constraint architectures as R6, an
unidentified arXiv paper; identified here as this one. The synthesis's
bottleneck over paths is exactly this paper's zero-dimensional merge
level, which keeps only the lowest barrier; the paper's higher dimensions
keep the alternative paths. The synthesis's budgets over several
resources at once would need multi-parameter persistence, which the paper
does not treat. Filed from it: [THEORY-tmpqzxwh](../theory.d/THEORY-tmpqzxwh.md). No instruction for
machine-learning practice; nothing for the anthology.
