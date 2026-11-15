---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpv6jne](../notes.d/NOTE-tmpv6jne.md)) from the arXiv preprint, v3: §§1–7,
  the statement of Theorem 6.1 and supplementary §§A and B.1; the proof
  skipped. Worth reading here as the layer-level, singular-vector account
  of merge loss within one pretrained start, a rival diagnosis to TIES's
  sign conflicts ([THEORY-107](../theory.d/THEORY-107.md)), and for its observation that collinear
  singular vectors double when they agree, which the spectral
  over-counting account ([LIT-tmpzk5vb](LIT-tmpzk5vb.md)) develops.
title: 'Task Singular Vectors: Reducing Task Interference in Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on model merging and task arithmetic as an instance of
    superposition in weight space. Citation checked against the arXiv API
    (authors, title, v1 date 2024-11-26, which is `published:`) and
    Crossref, queried without mailto (2025 IEEE/CVF CVPR, issued
    2025-06-10, doi:10.1109/cvpr52734.2025.01742). The IEEE copy was not
    fetched. No email address was sent to any service. Quotes rechecked
    by the filer against the downloaded text.
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
published: '2024-11-26'
arxiv: '2412.00081'
doi: '10.1109/cvpr52734.2025.01742'
first_author: 'Gargiulo'
keywords:
- 'model merging'
- 'task interference'
- 'task singular vectors'
- 'singular value decomposition'
- 'low-rank'
- 'whitening'
implementations: []
compared_against:
- LIT-tmpmqgjz
summary: >-
  Gargiulo et al. (2025, CVPR). Each layer's update from full fine-tuning
  of a CLIP ViT is close to low-rank: keeping 3% of its singular
  components costs 1.5% accuracy. Interference is measured from the
  overlap of different tasks' singular vectors, highest in early layers.
  Truncating each task's update and decorrelating the singular vectors
  across tasks (TSV-M) beats task arithmetic by about 15 points on
  ViT-B/32. Vision only. A rival diagnosis to TIES ([THEORY-107](../theory.d/THEORY-107.md)), with a
  layer-level relative of A's point that orthogonality of flattened
  updates is not enough.
---
<!-- inactive-ok-file: THEORY-107 — new tmp codes, or Proposed; this work's reading and neighbours, not leaned on -->

# LIT-tmpbknaa: Task Singular Vectors: Reducing Task Interference in Model Merging

Gargiulo, A. A., Crisostomi, D., Bucarelli, M. S., Scardapane, S., Silvestri, F. & Rodolà, E. (2025). Task Singular Vectors: Reducing Task Interference in Model Merging. In *2025 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. doi:10.1109/cvpr52734.2025.01742. arXiv:2412.00081.

## Key takeaways

*From the reading, [NOTE-tmpv6jne](../notes.d/NOTE-tmpv6jne.md).*

- **Low rank** (§3.2): "even when preserving only 3% of the singular
  components per task, the mean accuracy drops by merely 1.5%" (ViT-B/32,
  20 tasks).
- **Interference from overlap** (§3.3): "overlapping singular vectors
  suggest shared features in the weight space across tasks. Such overlap
  can introduce interference". For collinear vectors (supp. §A), "a
  double scaling effect when the vectors agree and complete cancellation
  when they disagree."
- **The merge** (Table 2): TSV-M reaches 85.86 against 70.79 for task
  arithmetic (ViT-B/32, 8 tasks), with no scaling coefficient to tune.
- **Depth** (§6.2): "STI is high in early layers sharing common knowledge
  and lower in more specialized ones."

## Standing in the record

Filed with the merging batch from the same turn ([LIT-tmpmqgjz](LIT-tmpmqgjz.md) is its
baseline; [LIT-tmpzk5vb](LIT-tmpzk5vb.md) builds on its observation).

A's characterization: "Low-rank task updates can be analyzed and merged
using their singular-vector interactions." The reader's verdict: it holds
in substance. The "low-rank task updates" are not LoRA adapters but full
fine-tuning updates that the paper finds approximately low-rank layer by
layer and then truncates. The evidence is vision only. That overlap
causes the loss rests on its association with accuracy over three task
sets and an ablation.

On A's toy: not stated. The paper's argument that flattened cosine
similarity is "coarse-grained" is a matrix-level relative of A's point:
flattened task vectors can be near-orthogonal while one layer's singular
vectors overlap.
