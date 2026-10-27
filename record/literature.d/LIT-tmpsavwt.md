---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpzb21n](../notes.d/NOTE-tmpzb21n.md)) in full, from arXiv v4, the CLeaR 2024
  version; worth reading for distributed interchange interventions and
  their training objective, for the exact example in which an algorithm
  fails in the neuron basis and holds after a rotation, and for the
  finding that BERT's entailment subspace decomposes into the two words'
  identities while an equality network's relation does not
  ([THEORY-tmpgqlal](../theory.d/THEORY-tmpgqlal.md)). Read it knowing that IIA is reported on the
  rotation's training data, that Table 2's brute-force row is a copy of
  Table 1's, that the learned subspaces are fixed only up to rotations
  within them, and that its random-network control reaches 0.64 at width
  4,096 ([THEORY-tmpqhbjf](../theory.d/THEORY-tmpqhbjf.md)).
title: 'Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked. Checked on
    2026-10-26 against the arXiv record: Atticus Geiger, Zhengxuan Wu,
    Christopher Potts, Thomas Icard and Noah D. Goodman, arXiv 2303.02536,
    v1 submitted 5 March 2023, which is `published:`; v4 of 21 February
    2024 carries the header of PMLR 236, the 3rd Conference on Causal
    Learning and Reasoning (CLeaR 2024). The summary follows the arXiv
    abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpzb21n) from arXiv v4: §§1–6 and Appendices A–D.
    Status Deferred → Active. Two accounts filed, both Active:
    THEORY-tmpgqlal and THEORY-tmpqhbjf. The summary is checked against
    the reading and given the numbers and the decomposition result.
tags:
- causality
- representation-learning
- anthology-candidate
date: '2026-10-26'
published: '2023-03-05'
arxiv: '2303.02536'
first_author: 'Geiger'
keywords:
- 'distributed alignment search'
- 'causal abstraction'
- 'interchange intervention'
- 'distributed representations'
- 'interpretability'
implementations: []
summary: >-
  Geiger, Wu, Potts, Icard & Goodman (2024; arXiv 2023), CLeaR 2024.
  Distributed alignment search (DAS) learns, by gradient descent, an
  orthogonal rotation of a layer such that swapping rotated subspaces
  between inputs reproduces a high-level causal model's counterfactuals,
  replacing brute-force search over disjoint neuron sets. In a network
  trained on hierarchical equality and in BERT fine-tuned on monotonicity
  NLI it finds alignments with interchange intervention accuracy 1.00
  where axis-aligned ones reach 0.73 and 0.51; BERT's entailment subspace
  decomposes into the identities of the two words, the equality network's
  relation subspace does not.
---
<!-- inactive-ok-file: THEORY-802 — Proposed; the account this work bears on most directly, cited as open -->

# LIT-tmpsavwt: Finding Alignments Between Interpretable Causal Variables and Distributed Neural Representations

Geiger, A., Wu, Z., Potts, C., Icard, T. & Goodman, N. D. (2024). Finding
alignments between interpretable causal variables and distributed neural
representations. *Proceedings of the Third Conference on Causal Learning
and Reasoning*, PMLR 236. arXiv:2303.02536 (5 March 2023).

Read in full on 2026-10-26 ([NOTE-tmpzb21n](../notes.d/NOTE-tmpzb21n.md)). Two accounts were drawn from
it: [THEORY-tmpgqlal](../theory.d/THEORY-tmpgqlal.md) and [THEORY-tmpqhbjf](../theory.d/THEORY-tmpqhbjf.md).

## Why this is here

The owner asked on 2026-10-26 how the record stood on neural circuit
theory; the answer found it held almost none of the core circuits
literature, and the owner said "go ahead and register and read those".
DAS is the method at the centre of the record's question on alignments:
[QUESTION-234](../questions.d/QUESTION-234.md) and [THEORY-802](../theory.d/THEORY-802.md) ask whether interchange interventions fix
the direction that mediates a variable, and the record held that debate
only through Makelov et al. ([LIT-968](LIT-968.md)), Wu et al.'s reply ([LIT-961](LIT-961.md)) and
MIB ([LIT-tmprlq7z](LIT-tmprlq7z.md)), all of which test or use DAS without the record
holding DAS itself. It also brings causal abstraction ([LIT-1310](LIT-1310.md)) to
trained networks, and its own example shows a verdict that changes with
the basis.
