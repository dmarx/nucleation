---
number: 802
status: 'Proposed'
formerly:
- THEORY-tmpmojjf
promote_when: 'A demonstration in a trained network, not a constructed one, of two alignments of the same high-level variable that differ by a change of basis crossing component boundaries and agree on every interchange intervention drawn from the data distribution, together with a showing that some further intervention, or nothing, separates them. Or a proof that, for a stated class of networks and high-level models, alignments that agree on all such interventions for every aligned variable are unique up to a stated symmetry. The first would confirm the account in trained models; the second would bound it, and a bound that leaves no ties in the class that matters would refute it there. What cannot settle it: further cases where one alignment scores higher, since the account is about ties under a fixed set of interventions.'
title: 'In trained networks as in constructed ones, interchange interventions on a fixed set of variables can be satisfied equally by alignments related by a change of basis, so which internal direction mediates a high-level variable is fixed only relative to a chosen decomposition into units, and complex models will generally have several distinct, fully correct abstractions'
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: the circuits works read on 2026-10-26 give a
    trained-network case of refinement, not of a change of basis;
    constructed and instrument-level cases of the thesis's shape;
    the source of the basis freedom in transformers; and its form
    for dictionaries, filed as QUESTION-tmpidxeb. None meets the
    promote_when. Status, title and promote_when are unchanged.
tags:
- causality
- philosophy-of-science
- representation-learning
date: '2026-10-20'
source:
- LIT-961
- LIT-968
summary: >-
  The general reading that [THEORY-243](THEORY-243.md) held before the promotion audit narrowed it to the three-unit network it proves (batch 062). Wu et al. (2024), [LIT-961](../literature.d/LIT-961.md), conjecture that complex models have "multiple distinct fully correct abstractions" and that the causal-abstraction framework cannot settle structural equivalence; Makelov et al. (2023), [LIT-968](../literature.d/LIT-968.md), §8, grant that crossing component boundaries makes "illusory" tenuous, and answer by privileging components. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis evidence can confirm or reject. Its only support is the constructed tie.
extends:
- THEORY-243
answers:
- QUESTION-234
---
<!-- inactive-ok-file: THEORY-tmpz7jrx — Proposed; the sparse-autoencoder resolution account, cited as open -->


# THEORY-802: In trained networks as in constructed ones, interchange interventions on a fixed set of variables can be satisfied equally by alignments related by a change of basis, so which internal direction mediates a high-level variable is fixed only relative to a chosen decomposition into units, and complex models will generally have several distinct, fully correct abstractions

## Source

Wu et al. (2024), [LIT-961](../literature.d/LIT-961.md), Appendix A, read in [NOTE-809](../notes.d/NOTE-809.md): after the rotated
identity network, "there are still likely to be multiple distinct fully
correct abstractions" for complex models, offered as a conjecture.
Makelov, Lange and Nanda (2023), [LIT-968](../literature.d/LIT-968.md), read in [NOTE-782](../notes.d/NOTE-782.md), §8 ("The
importance of correct model units"): if activation spaces may be
re-parametrized across component boundaries, calling a subspace
"illusory" is much more tenuous, and they hold that components should be
privileged because they do qualitatively different work.

## What is asserted, and by whom

The thesis is that the tie [THEORY-243](THEORY-243.md) proves in a constructed network is
the general case: interchange interventions on a fixed set of variables
leave the mediating direction underdetermined up to a change of basis,
so the direction is fixed only once a decomposition into units is
chosen, and trained models of any complexity will have several correct
alignments. Wu et al. assert it as a conjecture. Makelov et al. accept the
premise for the toy and dispute only the conclusion drawn about units.

## What the record holds toward it

- [THEORY-243](THEORY-243.md) (Active): the exact tie in the network
  x ↦ x(1, 0, 1) ↦ (0, 2, 1)·h, re-derived and checked on 1000 input pairs.
  It is an existence result, which is all this thesis has.
- Wu et al. note that intervening on further variables separates the two
  alignments in the toy. If that holds generally, the thesis survives
  only for interventions on a fixed, small set of variables.

## What would confirm or reject it

A trained-network tie of the kind the promote_when describes confirms
it. A uniqueness bound up to a stated symmetry, for a class of networks
that includes the trained models at issue, rejects it there. [QUESTION-234](../questions.d/QUESTION-234.md)
asks the same thing as a question; this entry is the answer Wu et al.
propose.

## Note of 2026-10-27: the circuits works, and dictionaries

The core circuits works, read on 2026-10-26 at the owner's request, bear
on this thesis without meeting its promote_when.

- **A trained-network case, of refinement rather than of a change of
  basis.** In BERT on MoNLI, Geiger et al.'s DAS (LIT-tmpsavwt) finds the
  entailment variable at one site and finds it decomposing there into the
  two input words' identities (THEORY-tmpgqlal). Two high-level models
  pass at one site, but they are related by refinement, not by a change of
  basis crossing component boundaries, so this is not the tie the
  promote_when asks for.
- **The verdict changes with the basis.** DAS's boolean toy fails in the
  neuron basis and passes once rotated back (NOTE-tmpzb21n), and its
  learned rotations reach IIA 1.00 where the closest axis-aligned
  alignments reach 0.73 and 0.51 (THEORY-tmpgqlal). That supports "fixed
  only relative to a chosen decomposition into units"; it is the converse
  of THEORY-243, where a change of basis leaves the score unchanged.
- **Several sufficient circuits, at the level of components.** A greedy
  pruner of the ACDC kind keeps one input of a redundant OR gate, chosen
  by the order it visits edges (THEORY-tmp1bwxc): the thesis's shape for
  subgraphs rather than directions, in a constructed case.
- **Instruments that cannot see a tie.** Causal scrubbing scores a
  hypothesis only through the partition of the data it induces
  (THEORY-tmpblgxz), and sparse feature circuits score nodes by their
  effect on one metric under one family of contrasts (NOTE-tmpr0gdc).
  Basis-related alignments that induce the same partitions, or the same
  effects, tie under both by construction.
- **Where the freedom comes from in transformers.** Elhage et al.'s
  framework (LIT-tmp9dono, NOTE-tmpx60d8) states it: the residual stream
  has no privileged basis, and rotating it together with every matrix
  that reads from or writes to it leaves the model unchanged. Its path
  expansion (THEORY-tmphm85g) is built from products that the rotation
  leaves alone, so the non-uniqueness does not touch it.
- **Dictionaries.** Sparse-autoencoder features are a resolution set by
  dictionary width (THEORY-tmpz7jrx), and Ameisen et al. (LIT-tmpsuo6l)
  concede that "there's no guarantee that the CLT features are the most
  parsimonious way to split up the computation" (NOTE-tmpn9fx3). Whether
  two dictionaries of equal fidelity give the same validated circuit is
  this thesis asked of dictionaries; it is filed as QUESTION-tmpidxeb.

Status, title and promote_when are unchanged.
