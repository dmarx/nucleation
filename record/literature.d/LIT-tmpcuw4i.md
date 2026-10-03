---
status: Proposed
status_note: 'read in full 2026-10-03 ([NOTE-tmppzhcy](../notes.d/NOTE-tmppzhcy.md)); watching, as the first claim of mode connectivity between independently trained generative and contrastive models: one pair of DDPMs on Flowers102 and one pair of NanoCLIP models on Flickr30k, joined by a chain of checkpoints along which the training loss stays below a threshold, where AutoNEB''s paths rise steeply on NanoCLIP. The path is built by moving layer groups towards the far end, rescaling each layer''s variance, and retraining with AdamW until the loss is under threshold, so every anchor is a retrained model. What would settle it: more than one pair per model, a barrier measure along the whole path rather than at the anchors, and a reason to think a path made of retrained anchors says more about the landscape than that retraining works. It is a preprint of 31 August 2026.'
title: 'Mode Connectivity Beyond Classifiers: Evidence from Generative and Contrastive Models'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1 (31 August 2026), main text and
    Appendices A–E. No venue is given. Filed with the owner's batch on mode
    connectivity and model merging (ADR-027). Not held in the Anthology of
    the SOTA: a grep of its record for the arXiv id and "Beyond
    Classifiers" found nothing.
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
published: '2026-08-31'
arxiv: '2608.30366'
first_author: 'Yao'
keywords:
- 'mode connectivity'
- 'low-loss path'
- 'diffusion models'
- 'DDPM'
- 'contrastive learning'
- 'CLIP'
- 'variance sphere'
- 'layer-wise connectivity'
compared_against:
- LIT-tmp3kyq9
implementations: []
summary: >-
  Yao, Zhang & Tian (2026), preprint. Extends layer-wise path construction
  (LLPF, Tian et al. 2026) to a DDPM on Flowers102 and a NanoCLIP model on
  Flickr30k. Layers move towards the target mode in a dataflow order
  (symmetric encoder–decoder pairs for the U-Net, alternating vision and
  text blocks for CLIP); each layer is rescaled to a fixed variance; the
  point is retrained with AdamW until its loss is below a threshold. The
  resulting chains keep training loss below 0.04 (DDPM) and 0.09 (NanoCLIP),
  where AutoNEB's maximum NanoCLIP loss is 6.69. Intermediate DDPMs have
  worse FID than the endpoints at equal training loss.
---

<!-- inactive-ok-file: LIT-tmpqno1r — Proposed: the GNN study, named as a sibling test of connectivity outside image classifiers, not leaned on -->
<!-- inactive-ok-file: LIT-tmpqp2pi — Proposed: the ELBO study, named as a sibling test of connectivity outside image classifiers, not leaned on -->
<!-- inactive-ok-file: LIT-354 — Deferred: Watanabe's book is unread; named as the source of the singular-learning-theory argument the paper cites, with no relation claimed -->

# LIT-tmpcuw4i: Mode Connectivity Beyond Classifiers: Evidence from Generative and Contrastive Models

Chengzheyi Yao, Yongzhao Zhang and Yongding Tian (2026), arXiv preprint — [ARXIV-2608.30366](https://arxiv.org/abs/2608.30366)

## Key takeaways

- **Low-loss chains exist between independently trained DDPMs and between
  independently trained NanoCLIP models.** Two modes per architecture, from
  different seeds, are joined by a sequence of checkpoints whose training
  loss stays below 0.04 (DDPM denoising loss) and 0.09 (NanoCLIP
  contrastive loss), while layer-wise distance to the far mode falls by at
  least an order of magnitude (§5, Fig. 3). Dense linear interpolation
  between consecutive NanoCLIP checkpoints raises the maximum loss by under
  5.3% (App. B).
- **How the chain is built matters.** Moving all layers at once, or in
  forward-pass order, or refining with SGD instead of Adam(W), gives higher
  average loss along the path (Fig. 5). AutoNEB, run with 13 pivots, reaches
  a maximum NanoCLIP training loss of 6.69 and training accuracy as low as
  0.05 (Fig. 4).
- **Low loss is not good generation, and closeness is not flatness.** Along
  the DDPM chain, intermediate checkpoints have higher FID than the
  endpoints at about the same training loss (Fig. 6). Near the end mode, a
  checkpoint with layer-wise cosine similarity near one still shows a small
  bump on the straight line to it: maximum loss 0.038, against 0.034 on the
  path (App. E).

## Standing in the record

Filed with the owner's batch on mode connectivity and model merging, under
`loss-landscapes` ([ADR-027](../decisions.d/ADR-027.md)). `Proposed`, not `Active`: the evidence is one
pair of modes per architecture, and the path is a sequence of retrained
anchors. Each anchor is trained back under the loss threshold (up to 500
AdamW rounds for DDPM). So the claim shown is that one can walk from one
mode to the other in small steps and retrain at each, which is weaker than
the existence of a fixed low-loss curve found by optimising a path. App. B
checks the straight segments between anchors for NanoCLIP only.

It is measured against Draxler et al. ([LIT-tmp3kyq9](LIT-tmp3kyq9.md)): AutoNEB, adapted to
DDPM and NanoCLIP with a 14-cycle schedule (App. D, Table 3), is its only
run baseline, and its Fig. 4 compares the two along the path. It leaves out
Garipov et al.'s curve fitting ([LIT-tmpotq71](LIT-tmpotq71.md)), saying the released
implementation "contains an error". It builds on LLPF (Tian et al. 2026),
which the record does not hold; the relation that would be declared is
`extends`.

Its motivation cites singular learning theory (Watanabe 2009, held here as
[LIT-354](LIT-354.md), unread) for why non-isolated minima are to be expected; it does not
use the theory. Within the batch, it is one of three works that test whether
mode connectivity holds outside image classifiers, with the GNN study
([LIT-tmpqno1r](LIT-tmpqno1r.md)) and the ELBO study ([LIT-tmpqp2pi](LIT-tmpqp2pi.md)).
