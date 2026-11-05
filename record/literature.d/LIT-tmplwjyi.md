---
status: Active
status_note: >-
  read 2026-11-05 ([NOTE-tmp3af4j](../notes.d/NOTE-tmp3af4j.md)) from the publisher's open-access PDF
  (CC BY 4.0), main text in full, later Methods and Supplementary
  Information skipped; worth reading as a coarse-grained model that reaches
  the whole folding timescale of DNA origami while keeping configuration,
  and for its argument that hybridization-state kinetic models can
  overpredict yield. Its main limits: simulation only, ten runs per design;
  no misbinding, helical topology, base stacking or annealing; the trapping
  is found in the large 32-helix bundle, while the small designs fold
  virtually defect-free; the paper does not call its mechanism nucleation.
title: 'Mechanism of DNA origami folding elucidated by mesoscopic simulations'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    FACT, rigidity, compliant mechanisms and origami (pasted 2026-11-04,
    written by another assistant), where it is cited as S5. The citation was
    checked by the reader against Crossref and OpenAlex: Marcello DeLuca,
    Daniel Duke, Tao Ye, Michael Poirier, Yonggang Ke, Carlos Castro and
    Gaurav Arya, Nature Communications 15, 3015; received 20 June 2023,
    online 8 April 2024; preprint bioRxiv 10.1101/2023.06.20.545758 of 20
    June 2023, which is `published:`. The synthesis's attribution is
    correct. Read from the publisher's PDF
    (https://www.nature.com/articles/s41467-024-46998-y.pdf), 13 pages,
    CC BY 4.0; also in PMC (PMC11001925). Status Active.
tags:
- natural-sciences
- complex-systems
date: '2026-11-05'
published: '2023-06-20'
doi: '10.1038/s41467-024-46998-y'
first_author: 'DeLuca'
keywords:
- 'DNA origami'
- 'self-assembly'
- 'mesoscopic model'
- 'Brownian dynamics'
- 'folding kinetics'
- 'kinetic traps'
implementations: []
summary: >-
  DeLuca, Duke, Ye, Poirier, Ke, Castro & Arya (2024). A bead model of DNA
  (8 nucleotides per bead) with a force field that switches with
  hybridization state simulates full isothermal folding of square-lattice
  origami up to 8192 nucleotides. A four-helix bundle folds
  hierarchically: staples bridge the scaffold, a cooperative zipping
  collapses it into a swollen, globally disordered precursor, and global
  order then grows slowly. Scaffold routing and long staples change the
  pathway. A 32-helix bundle folds slowly and variably, and some runs end
  with unfolded interiors in global topological traps that early progress
  did not predict. Simulation only.
---
<!-- inactive-ok-file: THEORY-tmpivh27 — Proposed; cited from the reading of DeLuca et al. (2024) as open -->

# LIT-tmplwjyi: Mechanism of DNA origami folding elucidated by mesoscopic simulations

DeLuca, M., Duke, D., Ye, T., Poirier, M., Ke, Y., Castro, C. & Arya, G. (2024). Mechanism of DNA origami folding elucidated by mesoscopic simulations. *Nature Communications* 15: 3015. doi:10.1038/s41467-024-46998-y.

## Key takeaways

*From the reading, [NOTE-tmp3af4j](../notes.d/NOTE-tmp3af4j.md).*

- **Hierarchical folding.** "zipping into a partially folded precursor
  followed by crystallization into the final structure" (abstract): the
  four-helix bundle "establishes local order before it establishes global
  order".
- **Traps in the large design.** The 32-helix bundle shows heterogeneous
  kinetics and trapping; the small designs fold "virtually defect-free".
- **Early progress predicts poorly.** "faster coalescence into a proto form
  early on is not a perfect predictor of overall folding performance".
- **Kinetic models may overpredict yield**, because one hybridization state
  can hold configurations with no viable path to the folded one.

## Standing in the record

Cited in the pasted synthesis on constraint architectures as S5, for
hierarchical folding and "frequent trapping in metastable states" in some
designs, both in the abstract's words. The reading qualifies the second:
the trapping is a simulation result, found in the large 32-helix bundle.
The paper does not call its mechanism nucleation, and the record files no
nucleation claim from it. Filed from it: [THEORY-tmpivh27](../theory.d/THEORY-tmpivh27.md). No instruction
for machine-learning practice; nothing for the anthology.
