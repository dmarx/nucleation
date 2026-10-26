---
status: Active
title: 'On frozen randomly initialized feed-forward networks at chance on hierarchical equality, with 16 input dimensions, distributed alignment search for the two-equality causal model reached interchange intervention accuracy of 0.50 to 0.51 at hidden sizes up to 256 but 0.55 at 1,028 and 0.64 at 4,096, so in a hidden layer much wider than the input a learned rotation can produce above-chance interchange accuracy for an algorithm the network does not implement'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpzb21n. One study read in full; the title
    claims only the five numbers of its Figure 3 and the reading that
    they bear, and nothing in the record contradicts it (ADR-047 v3). The
    authors draw the opposite emphasis, that DAS "cannot construct
    entirely new behaviors from random structure".
tags:
- causality
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpsavwt
summary: >-
  Geiger, Wu, Potts, Icard & Goodman (2024), LIT-tmpsavwt, §4.4, read in
  NOTE-tmpzb21n. A random network cannot implement hierarchical equality,
  so any IIA above 0.5 is made by the search. At widths near the input's
  there is none; at 4,096 there are 14 points. It does not say DAS
  results on trained networks are artefacts: the trained equality network
  reached 1.00 at width 16, where the random one stayed at 0.50.
---
<!-- inactive-ok-file: THEORY-802 — Proposed; a neighbouring account, cited as open -->

# THEORY-tmpqhbjf: On frozen randomly initialized feed-forward networks at chance on hierarchical equality, with 16 input dimensions, distributed alignment search for the two-equality causal model reached interchange intervention accuracy of 0.50 to 0.51 at hidden sizes up to 256 but 0.55 at 1,028 and 0.64 at 4,096, so in a hidden layer much wider than the input a learned rotation can produce above-chance interchange accuracy for an algorithm the network does not implement

## Source

Geiger, Wu, Potts, Icard and Goodman (2024), LIT-tmpsavwt, read in full
in NOTE-tmpzb21n: §4.4 and Figure 3.

## What was actually shown

Randomly initialized networks of the equality architecture, frozen at
chance accuracy (50%), with four 4-dimensional input vectors (16 input
dimensions) and hidden sizes 16, 64, 256, 1028 and 4096, intervention
subspaces of half the layer (k = 8 to 2048). DAS trained a rotation for
the two-equality causal model at layer 1. IIA: 0.50, 0.50, 0.51, 0.55,
0.64. The authors: "in small networks, there is no ability to increase
interchange intervention accuracy. However, as we increase the size of
the hidden representation to be orders of magnitude larger than the input
dimension of 16, the interchange intervention accuracy increases."

**What could have come out otherwise.** IIA could have stayed at chance at
every width, which would have shown that the search adds nothing a
network does not have.

## What this does not say

- **Not that trained-network results are artefacts.** The trained network
  reached 1.00 at width 16, where the random control is at 0.50.
- **Not how the effect scales** in trained wide models such as language
  models, whose layers are far wider than this input; one task, and the
  paper does not say how many seeds or which data the figure scores.
- **Not a mechanism.** Why width helps (more random features for a
  rotation to combine) is the authors' hypothesis, not tested.

## Connections

- **THEORY-tmp4lqc8.** MIB's best causal-variable method is DAS, trained
  against the model it is scored on; this is the only measured bound in
  the record on how much such training can manufacture.
- **LIT-968 (NOTE-782).** Makelov et al.'s illusion is a mechanism by
  which a learned subspace patch can change behaviour without the
  variable being there; this control shows the size of the effect grows
  with width.
- **THEORY-802.** An abstraction that passes only because the search is
  expressive is one more way an interchange test underdetermines what the
  network computes.
