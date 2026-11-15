---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpf8m60](../notes.d/NOTE-tmpf8m60.md)) from the arXiv preprint, v2 (§§1–4.4
  and §§5.2–5.3, Tables 3, 5, 6 and 7; Appendix A and the remaining
  appendices skipped). Accepted at ACL 2025 per the arXiv comment; not
  checked in the ACL Anthology. Worth reading here as the account of LoRA
  merge loss that puts it in data, not coordinates: summed LoRAs shift
  each other's outputs on each other's inputs (the term B2A2h1), and
  choosing each task's A before fine-tuning to avoid the other tasks'
  feature directions reduces it. Of the exchange's two sentences on this
  work and Chaves et al. together, the one on parameter subspaces and
  data distributions is this paper's. Bears on [THEORY-107](../theory.d/THEORY-107.md).
title: 'Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on how model merging fails, where A cites it with Chaves et al.
    (2026), LIT-tmpml2pq, under two joint sentences and gives the venue
    as unknown. Citation checked against the arXiv API: Haobo Zhang and
    Jiayu Zhou (University of Michigan); v1 2025-05-28, which is
    `published:`, v2 2026-05-28; comment "accepted by ACL 2025". The ACL
    Anthology was not searched. No email address was sent to any
    service.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2025-05-28'
arxiv: '2505.22934'
first_author: 'Zhang'
keywords:
- 'LoRA'
- 'model merging'
- 'orthogonal subspaces'
- 'data-parameter interplay'
- 'output shift'
- 'OSRM'
implementations: []
compared_against:
- LIT-675
summary: >-
  Zhang & Zhou (2025), ACL. Merged LoRA models lose accuracy, the paper
  argues, because each task's update shifts the layer outputs on the
  other tasks' inputs (the term B2A2h1), which data-free merging ignores.
  OSRM sets each task's A, before fine-tuning, to the smallest-variance
  eigen-directions of the other tasks' latent features, and plugs into
  task arithmetic, Fisher, RegMean, TIES and EMR. On Llama3-8B it lifts
  task arithmetic from 63.28 to 72.75 average but not TIES (53.01 to
  52.69); gains shrink with model size. Bears on [THEORY-107](../theory.d/THEORY-107.md) as a
  data-conditioned location for interference.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account of merge interference this reading bears on -->

# LIT-tmpwnkv8: Unraveling LoRA Interference: Orthogonal Subspaces for Robust Model Merging

Zhang, H. & Zhou, J. (2025). Unraveling LoRA Interference: Orthogonal
Subspaces for Robust Model Merging. *ACL 2025* (per the authors).
arXiv:2505.22934v2.

## Key takeaways

*From the reading, [NOTE-tmpf8m60](../notes.d/NOTE-tmpf8m60.md).*

- **The account** (abstract): "this issue arises from a previously
  overlooked interplay between model parameters and data distributions".
- **The term** (§4.1, Eq. 1): with LoRAs summed, W_m h1 = W1 h1 + B2A2 h1;
  "B2A2h1 can be viewed as a 'perturbation' induced by the knowledge
  learned for task T2".
- **The remedy** (abstract, §4): "constrain the LoRA subspace prior to
  fine-tuning, ensuring that updates relevant to one task do not
  adversely shift outputs for others". Since H1 "is typically full-rank
  in real scenarios", the norm ‖A_t H_¬tᵀ‖_F is minimized rather than
  zeroed.
- **Llama3-8B** (Table 5): task arithmetic 63.28 without and 72.75 with
  OSRM; TIES 53.01 without and 52.69 with.
- **Scale** (§5.2): "the performance gain from our method diminishes"
  with model size.

## Standing in the record

A, in the exchange, cites this paper and Chaves et al. (2026),
[LIT-tmpml2pq](LIT-tmpml2pq.md), together for two characterizations: one "studies conflicts
between task subspaces under distribution shift", one "emphasizes the
interaction between parameter subspaces and data distributions". The
second fits this paper, close to its abstract. The first does not: the
setting is in-distribution multi-task merging (GLUE), and "out-of-task
data" means another task's inputs, not a shifted distribution. That
sentence is Chaves et al.'s. A's "venue unknown" is corrected to ACL 2025,
on the authors' word.

Its account is first-order and layer-local. Zhu (2026), [LIT-tmpdc2rl](LIT-tmpdc2rl.md),
finds most of the activation cross-term in language-model merges carried
from earlier layers, which this account does not model; the two are
compatible and address different stages.
