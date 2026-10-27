---
status: Active
title: 'In Geiger et al.''s three-layer feed-forward network trained on hierarchical equality and in BERT fine-tuned on monotonicity inference, interchange interventions on subspaces found by a learned rotation aligned the hypothesised two-variable causal models with interchange intervention accuracy of 1.00 on the rotation''s training data, where the axis-aligned alignment closest to the learned rotation reached 0.73 and 0.51; in BERT, the learned lexical-entailment subspace was in turn aligned, at 0.97 to 0.98, with a model holding only the identities of the two words'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpzb21n, the reading of Geiger et al. (2024)
    in full. One study; the title claims no more than Tables 1 and 2
    report, names the training-data scoring, and leaves out the
    brute-force comparison for MoNLI, whose printed row is a copy of
    Table 1's (ADR-047 v3).
tags:
- causality
- representation-learning
date: '2026-10-26'
source:
- LIT-tmpsavwt
summary: >-
  Geiger, Wu, Potts, Icard & Goodman (2024), [LIT-tmpsavwt](../literature.d/LIT-tmpsavwt.md), read in
  [NOTE-tmpzb21n](../notes.d/NOTE-tmpzb21n.md). Layer 1 of the equality network (1.00 with |N| = 16 and
  two 8-dimensional subspaces) and layer 9 of BERT's [CLS] vector (1.00
  with two 256-dimensional subspaces). It does not say the networks
  implement the algorithms in any stronger sense than interchange
  accuracy on training pairs, nor that the learned subspaces are unique:
  every rotation within them gives the same interventions.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-tmpwr001 — Proposed; the account and claim this bears on, cited as open -->

# THEORY-tmpgqlal: In Geiger et al.'s three-layer feed-forward network trained on hierarchical equality and in BERT fine-tuned on monotonicity inference, interchange interventions on subspaces found by a learned rotation aligned the hypothesised two-variable causal models with interchange intervention accuracy of 1.00 on the rotation's training data, where the axis-aligned alignment closest to the learned rotation reached 0.73 and 0.51; in BERT, the learned lexical-entailment subspace was in turn aligned, at 0.97 to 0.98, with a model holding only the identities of the two words

## Source

Geiger, Wu, Potts, Icard and Goodman (2024), *Finding alignments between
interpretable causal variables and distributed neural representations*,
CLeaR 2024, arXiv 2303.02536, [LIT-tmpsavwt](../literature.d/LIT-tmpsavwt.md), read in full in
[NOTE-tmpzb21n](../notes.d/NOTE-tmpzb21n.md): §§3–5, Tables 1–2, Appendix A.

## What was actually shown

**Method.** A rotation R of one layer's activations is trained by
gradient descent, with network and causal model frozen, so that swapping
chosen subspaces of the rotated representation between a base and source
inputs reproduces the causal model's counterfactual outputs. IIA is the
share of such swaps on which network and model agree.

**Hierarchical equality.** A three-layer ReLU network trained to decide
(w = x) = (y = z), perfect on train and test. For the model with
intermediate variables w = x and y = z: IIA 1.00 at layer 1 with |N| = 16
and two 8-dimensional subspaces, 0.99 with |N| = 32; the closest
axis-aligned alignment 0.73. Layers 2 and 3 align poorly (0.67 and 0.53
at best).

**MoNLI.** BERT-base fine-tuned to perfect accuracy; [CLS] vector at
layer 9. For the model with variables for negation and for the lexical
relation between the two changed words: IIA 1.00 with 256-dimensional
subspaces; closest axis-aligned 0.51. A second rotation inside the
lexical-entailment subspace aligns a model holding the premise word's and
hypothesis word's identities at 0.97–0.98.

**What could have come out otherwise.** The rotated alignments could have
done no better than the axis-aligned ones, as they did not at layers 2–3
of the equality network; the entailment subspace could have resisted
decomposition, as the equality network's relation subspace did (about
0.5).

## What this does not say

- **Not held-out accuracy.** The tables report the rotation's training
  data.
- **Not that the alignment is unique.** The intervention depends on R only
  through the subspaces it selects, so all rotations within them tie; and
  whether other subspaces reach the same accuracy was not examined.
- **Not that the networks run the algorithm in a stronger sense.** At
  |N| = 16 the two subspaces fill the layer.
- **Not a comparison with brute force on MoNLI.** That row of Table 2
  duplicates Table 1's.
- **Not about large models or many variables.** Two small settings,
  binary variables, one token position.

## Connections

- **[THEORY-802](THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** A trained-network case in which the
  test's verdict depends on the basis: axis-aligned alignments fail where
  rotated ones succeed. It is not a tie between basis-related alignments
  that agree on every interchange, which is what [THEORY-802](THEORY-802.md)'s
  promote_when asks for. The MoNLI pair of models that both pass is a
  case of more than one correct abstraction at one site, related by
  refinement.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** In BERT the variable aligned with the label's
  decision decomposes into the inputs it is computed from.
