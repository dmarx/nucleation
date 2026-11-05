---
status: Active
status_note: >-
  main text read in full 2026-11-05 (NOTE-tmp52g52) from the publisher's
  open-access PDF (CC BY 4.0); worth reading as the extension of rigidity
  control by facet planarity from Miura-ori to origami with arbitrary
  polygonal facets: planarity of an n-gon takes exactly n − 3
  constraints, triangular facets add none, and the critical density at
  which half the runs reach minimum degrees of freedom depends on the
  facet-selection rule, the number of candidates sampled per step and the
  fraction of triangular facets. Its main limits: infinitesimal rigidity
  at one folded configuration, a fitted (not derived) formula for the
  critical density, a fixed-size statistic called "rigidity percolation",
  and only illustrative paper models. The Supplementary Notes were not
  read.
title: 'Rigidity control of general origami structures'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (the pasted synthesis
    on constraint architectures, written by another assistant, A, in the
    same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), which cites it as O8: Li & Choi 2026, Communications
    Physics, doi:10.1038/s42005-026-02640-5. Citation checked against
    Crossref: Rongxuan Li and Gary P. T. Choi (Department of Mathematics,
    The Chinese University of Hong Kong), Communications Physics 9, article
    217, open access under CC BY 4.0; received 18 August 2025, accepted 10
    April 2026, published online 25 April 2026, which is `published:`. A's
    attribution is right. No arXiv version was found. Copy: the
    publisher's PDF, https://www.nature.com/articles/s42005-026-02640-5.pdf
    (11 pp.), fetched without obstacle and extracted by pdftotext. The
    Supplementary Notes 1–4 and Movies were not read.
tags:
- mathematics
- natural-sciences
date: '2026-11-05'
published: '2026-04-25'
doi: '10.1038/s42005-026-02640-5'
first_author: 'Li'
keywords:
- 'origami'
- 'rigidity control'
- 'facet planarity'
- 'rigidity percolation'
- 'power of choices'
- 'explosive percolation'
- 'triangular facets'
- 'degrees of freedom'
implementations: []
summary: >-
  Li & Choi (2026). Nine origami patterns (periodic, rotational,
  perforated) and one irregular pattern start maximally floppy, every
  facet free to bend along its triangulation; planarity constraints are
  added facet by facet and the infinitesimal DoF, 3V − rank(A) − 6,
  computed after each step. Planarity of an n-gon takes exactly n − 3
  sub-planarity constraints (proved), so triangular facets add none.
  Facets are chosen by "power of choices" rules from explosive
  percolation: of k sampled candidates, the one lowering the DoF most
  (Most Efficient) or least (Least Efficient). Larger k narrows the
  transition, the triangular-facet ratio governs it, and the critical
  density ρ* (half the runs at minimum DoF) is fitted by a tanh model in
  the rule, log k and that ratio.
---
<!-- inactive-ok-file: THEORY-tmp6nzru — Proposed or new; cited from the reading of Li & Choi (2026) as open -->

# LIT-tmpiean9: Rigidity control of general origami structures

Li, R. & Choi, G. P. T. (2026). Rigidity control of general origami structures. *Communications Physics* 9: 217. doi:10.1038/s42005-026-02640-5.

## Key takeaways

*From the reading, NOTE-tmp52g52.*

- **Planarity as the control.** "the rigidity of a wide range of origami
  structures can be controlled by enforcing or relaxing the planarity
  condition of selected facets." (Abstract.)
- **n − 3 per facet.** "The number of sub-planarity constraints required
  to control the planarity of an n-sided polygonal facet is exactly n − 3."
  Hence "imposing planarity on triangular facets does not reduce the global
  DOF".
- **Triangles govern the transition.** "in all origami structures, the
  rigidity control is highly relevant to the presence of triangular
  facets." (Discussion.)
- **Choice narrows it.** "the standard deviation across simulations
  decreases as k increases, indicating that the power of choices has a
  strong effect, leading to a narrower transition width in rigidity
  percolation."

## Standing in the record

The pasted synthesis on constraint architectures cites it as O8, for
planarity constraints on selected facets and critical densities where
rigidity changes. That is right but thin. A does not mention that the
transition depends on the selection rule and the candidate-pool size, or
that the triangular-facet ratio is the governing variable. A also does not
say that the predictive formula is fitted, or that the paper's "rigidity
percolation" is a fixed-size statistic. The paper extends Chen, Choi and
Mahadevan (2020), LIT-tmpge2xj, which A cites as O7 without noting the
link. Filed from it: THEORY-tmp6nzru.
