---
status: Proposed
promote_when: >-
  A reading of the published paper, or an independent computation on
  disordered spring networks, confirms that greedy removal of about one
  percent of bonds tunes a chosen source–target strain ratio with failure
  in only a few percent of networks, that several such responses can be
  tuned into one network at once, and that each bond's removal effect is
  computed from the self-stress and compatible-stress basis without
  re-solving the network.
title: 'Rocks and colleagues show that in disordered spring networks a chosen linear strain response between a distant pair of target nodes and a pair of source nodes, and several such responses at once, can be produced with near-total success by removing about one percent of the bonds, chosen greedily with an analytic update built from the network''s states of self-stress and compatible stress'
version: 1
tags:
- natural-sciences
- network-science
- complex-systems
date: '2026-11-05'
source:
- LIT-tmpf2n99
summary: >-
  Rocks, Pashine, Bischofberger, Goodrich, Liu and Nagel (2017; arXiv
  2016), LIT-tmpf2n99, read in NOTE-tmptvl7g from the arXiv v1 preprint;
  the PNAS text was not reached. Proposed for that reason and because the
  Supporting Information was not read. It is a linear, athermal result for
  central-force networks made rigid first: it does not say why the chosen
  bonds work, that the network could find them itself, or that allostery
  in proteins works this way.
---

# THEORY-tmpt2hyq: Rocks and colleagues show that in disordered spring networks a chosen linear strain response between a distant pair of target nodes and a pair of source nodes, and several such responses at once, can be produced with near-total success by removing about one percent of the bonds, chosen greedily with an analytic update built from the network's states of self-stress and compatible stress

## Source

Rocks et al. (2017; arXiv v1 2016-07-28), LIT-tmpf2n99; read in NOTE-tmptvl7g, of the preprint.

## What was actually shown

- **Tuning** (Computational Results): about 5 of 400 bonds in 2D and 4 of
  740 in 3D removed on average for η = ±1; failure under 2% (2D) and 1%
  (3D) for |η| up to 1, success meaning within 1% of the target ratio. It
  could have failed: at small ΔZ it often does, because removal would
  break rigidity.
- **Several responses** (Fig. 3): one source, three targets at different
  ratios; two independent source–target pairs in one network at ΔZ = 1.0.
- **The update** (Theoretical Approach, eq. 15): the effect of removing
  each bond follows from the SVD basis of the equilibrium matrix, split
  into states of self-stress and of compatible stress.
- **Specificity**: other node pairs are "essentially unaffected by the
  source strain".
- **Physical networks**: four laser-cut or printed realizations agree with
  simulation at C = 0.98 ± 0.02 on the removed bonds' node distances.

## What this does not say

- That the response holds beyond linear response, with temperature,
  prestress or bond bending; the experiments show it often survives, not
  always.
- Why particular bonds achieve the response; the authors leave it open.
- That the network adapts: an external algorithm with a full model
  chooses every bond.
- That this is how allostery arises in proteins; the authors offer it as
  a suggestion, from athermal networks.
