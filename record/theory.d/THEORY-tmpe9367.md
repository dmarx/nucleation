---
status: Proposed
promote_when: >-
  An independent study, on a benchmark other than CIFAR100 or
  TinyImageNet and with several seeds, finds that a hyperbolic
  entailment-cone penalty between old and new embeddings improves
  cross-model retrieval compatibility over Euclidean alignment baselines
  without lowering the new model's own retrieval, with the largest gain
  when the architecture changes. Not met by a restatement that cites this
  paper. Not defeated by unbounded norm growth across updates, which the
  title does not deny.
title: "Bui and colleagues make an updated embedding model backward-compatible by lifting both models' embeddings into the Lorentz model and penalising each new embedding for leaving the entailment cone apexed at the same item's old embedding, beside an uncertainty-weighted contrastive loss, and on CIFAR100 and TinyImageNet this improves cross-model retrieval compatibility over Euclidean alignment baselines at little cost to the new model, most of all when the architecture changes"
version: 1
tags:
- representation-learning
- information-retrieval
date: '2026-11-22'
source:
- LIT-2989
summary: >-
  Bui, Yang, Chen, Neves, Ju, Ying, Shah & Zhao (2025), [LIT-2989](../literature.d/LIT-2989.md), read in
  [NOTE-tmpvu3vp](../notes.d/NOTE-tmpvu3vp.md). Temporal cone restriction as a soft regularizer, and it
  works. The sharp edges: the hinge is weighted 0.3 and cone satisfaction
  is never reported; the cones are per item, between two separately
  trained models; one run per configuration; and the clipping radius must
  rise at every update, which the authors list as a limitation and which
  follows from the cone geometry ([CLAIM-tmpxcy5s](../claims.d/CLAIM-tmpxcy5s.md)). Proposed until
  replicated.
---
<!-- inactive-ok-file: CLAIM-tmpxcy5s — Proposed; the assistant's derivation of the norm growth -->

# THEORY-tmpe9367: Bui and colleagues make an updated embedding model backward-compatible by lifting both models' embeddings into the Lorentz model and penalising each new embedding for leaving the entailment cone apexed at the same item's old embedding, beside an uncertainty-weighted contrastive loss, and on CIFAR100 and TinyImageNet this improves cross-model retrieval compatibility over Euclidean alignment baselines at little cost to the new model, most of all when the architecture changes

## Source

Bui, Yang, Chen, Neves, Ju, Ying, Shah & Zhao (2025), "Learning Along the
Arrow of Time: Hyperbolic Geometry for Backward-Compatible
Representation Learning", ICML 2025 (PMLR 267), arXiv 2506.05826,
[LIT-2989](../literature.d/LIT-2989.md), read in [NOTE-tmpvu3vp](../notes.d/NOTE-tmpvu3vp.md).

## What was actually shown

- **Observed:** over four update scenarios on two datasets, higher CMC@1
  and mAP compatibility than ℓ2, BCT, Hot-Refresh, AdvBCT and HOC, with
  P_up about unchanged (Table 1); averaged relative gains of 21.4% and
  44.8% over the strongest Euclidean baseline.
- **Observed:** removing the cone term costs most when the architecture
  changes (CIFAR100 CMC@1 P_com 0.937 against −0.178) and little when only
  the data grow (0.956 against 0.847).
- **Observed:** compatibility kept across five sequential updates, for
  every pair of earlier and later models (Fig. 5); gallery uncertainty
  falls with each update (Fig. 6).
- One run per configuration; HBCT's settings fixed while the baselines'
  were searched.

## What this does not say

- How many new embeddings actually lie inside their old cones.
- Anything about checkpoints of one training run, or about cones of
  concepts: each cone is one item's, between two models.
- That the norm-based uncertainty is calibrated against error.
