---
status: Proposed
promote_when: >-
  The compression identity (circular correlation as a sum of the
  subject–object tensor product over fixed partitions, computable in
  O(d log d) by FFT) and its non-commutativity are checked; and an
  independent reimplementation or a later benchmark paper, under the same
  filtered protocol, reports HolE ahead of TransE, TransR, ER-MLP and
  RESCAL on filtered MRR on WN18 and FB15k.
title: 'Nickel, Rosasco and Poggio score a knowledge-graph triple by σ(r_pᵀ(e_s ⋆ e_o)) with circular correlation ⋆, an operator that compresses the subject–object tensor product into d components at O(d) memory and O(d log d) time and is non-commutative, so it can model asymmetric relations; with all models reimplemented under one loss and optimizer it gave the highest filtered MRR on WN18 and FB15k against TransE, TransR, ER-MLP and RESCAL'
version: 1
tags:
- representation-learning
- information-retrieval
date: '2026-11-15'
source:
- LIT-tmp7xp5z
summary: >-
  Nickel, Rosasco & Poggio (2016), LIT-tmp7xp5z, read in full in
  NOTE-tmpmehz3 from arXiv v2, without the supplement. Filtered MRR 0.938
  on WN18 and 0.524 on FB15k; TransE leads FB15k Hits@10. The baselines
  are the authors' own reimplementations. Built on Plate's HRR,
  THEORY-tmp713mr, with composition by correlation and learned embeddings.
  The wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp713mr — Proposed or Skimmed entries of this filing -->

# THEORY-tmpcw54z: Nickel, Rosasco and Poggio score a knowledge-graph triple by σ(r_pᵀ(e_s ⋆ e_o)) with circular correlation ⋆, an operator that compresses the subject–object tensor product into d components at O(d) memory and O(d log d) time and is non-commutative, so it can model asymmetric relations; with all models reimplemented under one loss and optimizer it gave the highest filtered MRR on WN18 and FB15k against TransE, TransR, ER-MLP and RESCAL

Nickel, Rosasco & Poggio (2016), LIT-tmp7xp5z; read in NOTE-tmpmehz3.

## The result

HolE embeds entities and relations in R^d and scores (s, p, o) by the dot
product of the relation vector with the circular correlation of subject
and object, [a ⋆ b]_k = Σ_i a_i b_(k+i mod d). Each component sums a fixed
partition of the d² pairwise products, so memory is O(d) and time
O(d log d) through the FFT; a ⋆ b ≠ b ⋆ a. Trained with a ranking loss and
AdaGrad, with every baseline reimplemented under that protocol, HolE gave
filtered MRR 0.938 on WN18 (RESCAL 0.890, TransE 0.495) and 0.524 on FB15k
(TransE 0.463), and the best AUC-PR on the harder Countries settings
(S2 0.772, S3 0.697). The comparison could have gone the other way:
compression could have cost what RESCAL's full product gains.

## What it does not show

- That HolE leads on every metric: TransE is ahead on FB15k Hits@10 (74.9
  against 73.9).
- That it beats later models, or that WN18 and FB15k are sound
  benchmarks; neither is this paper's question.
- A capacity result for the compression: the partition is designed and
  not analysed, so it is not THEORY-1036's kind of superposition.
- That HolE is an associative memory: its authors draw the analogy to
  Plate's HRR and mark the difference, that the embeddings are learned and
  generalize.
