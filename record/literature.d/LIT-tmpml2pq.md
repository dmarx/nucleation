---
status: Active
status_note: >-
  read 2026-11-15 (NOTE-tmpzye7e) from the arXiv preprint, v2 (§§1–5.2 in
  part: motivation, the method, Table 1 and the first analyses; the
  ablations, the conclusion and the appendices skipped). Published at
  CVPR 2026; a CVF open-access copy was located (HTTP 200) and not read,
  since the arXiv copy was. Worth reading here as a measurement that
  cuts against the intuition that merge conflict comes from dissimilar
  tasks: CLIP encoders fine-tuned on domains of one task share more of
  their singular subspaces than encoders fine-tuned on different tasks,
  and the paper treats that overlap as the conflict to remove. Of the
  exchange's two sentences on this work and OSRM together, the one on
  subspace conflicts under distribution shift is this paper's. Bears on
  THEORY-107's point that conflict frequency does not track cost.
title: 'Bridging Domains through Subspace-Aware Model Merging'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on how model merging fails, where A cites it with Zhang & Zhou
    (2025), LIT-tmpwnkv8, under two joint sentences. Citation checked
    against the arXiv API: Levy Chaves, Chao Zhou, Rebekka Burkholz,
    Eduardo Valle and Sandra Avila; v1 2026-03-06, which is `published:`,
    v2 2026-03-09; comment "Accepted at the IEEE/CVF Conference on
    Computer Vision and Pattern Recognition 2026 (CVPR)". The CVF open
    access page, https://openaccess.thecvf.com/content/CVPR2026/html/Chaves_Bridging_Domains_through_Subspace-Aware_Model_Merging_CVPR_2026_paper.html,
    answered HTTP 200, confirming A's "CVF open access". No email address
    was sent to any service.
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-03-06'
arxiv: '2603.05768'
first_author: 'Chaves'
keywords:
- 'model merging'
- 'domain generalization'
- 'subspace alignment ratio'
- 'task matrix'
- 'subspace conflicts'
- 'leave-one-domain-out'
- 'CLIP'
implementations: []
compared_against:
- LIT-675
summary: >-
  Chaves et al. (2026), CVPR. Merges CLIP image encoders fine-tuned on
  different source domains of one task and tests on a held-out domain,
  over eight benchmarks. Domain experts' task matrices share more of
  their top singular subspaces than multi-task experts' (pairwise SAR
  about 0.61–0.71 across DomainNet domains, 0.41–0.69 across eight vision
  tasks), which the paper reads as stronger conflict. SCORE projects each
  task matrix into a shared orthogonal basis and trims outlying
  off-diagonal couplings, data-free at λ = 1, and edges TIES and TSV on
  average by under a point. Bears on THEORY-107.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account of merge interference this reading bears on -->

# LIT-tmpml2pq: Bridging Domains through Subspace-Aware Model Merging

Chaves, L., Zhou, C., Burkholz, R., Valle, E. & Avila, S. (2026). Bridging
Domains through Subspace-Aware Model Merging. *IEEE/CVF Conference on
Computer Vision and Pattern Recognition (CVPR) 2026*. arXiv:2603.05768v2.

## Key takeaways

*From the reading, NOTE-tmpzye7e.*

- **The finding** (abstract): "merging models trained under different
  distribution shifts induces stronger conflicts between their subspaces
  compared to traditional multi-task settings".
- **Why** (§3.2): "Because these models solve similar classification
  problems, their delta weights tend to align along similar singular
  directions. This strong subspace overlap contrasts sharply with the
  diversity of multi-task learning." "This overlap leads to interference
  among singular directions during merging."
- **SCORE**: a shared orthogonal basis from the concatenated top singular
  vectors; keep the diagonal of each projected task matrix and the
  off-diagonal entries beyond mean ± 1.96 SD.
- **Table 1**: average held-out accuracy 65.69 on ViT-B-32 against 64.95
  for TSV and 64.84 for TIES; 73.04 on ViT-L-14 against 72.46 for TIES.
  Task arithmetic at λ = 1 collapses below zero-shot (DomainNet 5.40,
  ImageNet-R 4.65 on ViT-B-32).

## Standing in the record

A, in the exchange, cites this paper and Zhang & Zhou (2025), LIT-tmpwnkv8,
together for two characterizations: one "studies conflicts between task
subspaces under distribution shift", one "emphasizes the interaction
between parameter subspaces and data distributions". The first fits this paper:
it is close to its abstract. The second does not: the method is data-free
and never models how one model's parameters act on another domain's data.
It fits LIT-tmpwnkv8. Joining the two papers blurs that. A also leaves out
that the conflict here comes from overlap, shared singular directions,
the opposite of the intuition that conflict comes from tasks that differ.

On THEORY-107: TIES finds sign conflicts as frequent within one task as
across tasks; this paper finds the most subspace overlap among same-task
experts, yet merges them well. The two "conflicts" are different
measurements, and neither paper shows its measure causes the loss.
