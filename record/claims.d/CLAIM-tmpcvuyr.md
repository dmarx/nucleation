---
status: Proposed
title: 'A transformer''s depth orders its processing in coarse stages around a broad middle that is robust to intervention but not redundant, refining one prediction while its representation drifts, rather than ascending through levels of knowledge: early layers are distinct and sensitive, middle layers can be skipped, reordered or run in parallel with graceful loss though not replaced by copies of one layer, and an ordering of linguistic information by layer, overlapping in the middle and revised per example from above, is the main evidence against reading depth as refinement alone'
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Revised after the readings of 2026-11-21 of the four interpretability
    works and of Tensor Programs VI. Corrections: middle layers cannot be
    repeated (copies are catastrophic); the middle is uniform but not
    redundant; what is refined is one prediction, the representation's
    basis drifting; Tenney and colleagues' ordering is of overlapping
    regions, weak in the middle; robustness rests on two model families;
    and Depth-μP makes adjacent blocks maximally different, so the
    dynamics bullet is restated. Defeaters not met. Grounds move from the
    unread works to the readings, and THEORY-1030 and THEORY-1033 join
    them. Previous title: "A transformer's depth orders its processing in
    coarse stages around a broad middle whose layers are nearly
    interchangeable, refining one representation and its prediction rather
    than ascending through levels of knowledge: early and final layers are
    distinct and sensitive, middle layers can be skipped, swapped or
    repeated with modest loss, and an ordering of linguistic abstraction
    by layer is the main evidence against reading depth as refinement
    alone".
role: thesis
warrant: interpretive
defeated_if: >-
  Either of two results. (a) Interventions that delete, swap or reorder
  middle layers degrade trained transformers as much as interventions on
  early or final layers, across model families, so that the middle is not
  interchangeable. (b) Probes find, across the middle layers, a sequence of
  representational levels each of which later layers depend on and
  earlier ones lack, beyond the ordering Tenney and colleagues report, so
  that depth is an ascent through levels and not refinement within one
  representation.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-20'
line:
- learned-structure
rests_on:
- CLAIM-tmp2yj4t
- CLAIM-478
grounds:
- LIT-1534
- THEORY-tmpky55f
- THEORY-tmpuxsx9
- THEORY-tmpthk75
- THEORY-tmp3dee0
- THEORY-1030
- THEORY-1033
summary: >-
  The owner, 2026-11-20, after the session's results on rates and depth:
  an earlier thought that transformer depth corresponds to an epistemic
  hierarchy was "probably incorrect, which in retrospect I think is
  corroborrated by mech interp work". The suggestion was not on the record
  and is not filed. This is what the owner and the assistant judged
  warranted in its place: depth as coarse stages and refinement, with the
  evidence on both sides. Version 2, after the four works were read on 2026-11-21, rests on their
  readings, on Elhage and colleagues (LIT-1534) and on Geva and colleagues
  (THEORY-1030, THEORY-1033), with their corrections. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpky55f THEORY-tmpuxsx9 THEORY-tmpthk75 THEORY-tmp3dee0 THEORY-tmpbyw89 THEORY-1030 — Proposed; readings this claim now rests on -->
<!-- inactive-ok-file: CLAIM-tmp2yj4t CLAIM-478 LIT-tmp8pcca LIT-tmpi3ty1 LIT-tmp40ldm LIT-tmp166hz CLAIM-tmpmugkp CLAIM-tmpy75jv — Proposed or Deferred; the claims this rests on and the works read only by abstract -->

# CLAIM-tmpcvuyr: A transformer's depth orders its processing in coarse stages around a broad middle that is robust to intervention but not redundant, refining one prediction while its representation drifts, rather than ascending through levels of knowledge: early layers are distinct and sensitive, middle layers can be skipped, reordered or run in parallel with graceful loss though not replaced by copies of one layer, and an ordering of linguistic information by layer, overlapping in the middle and revised per example from above, is the main evidence against reading depth as refinement alone

## The claim

The owner, 2026-11-20: "my interpretation is that this means my suggestion
that transformer depth corresponded to epistemic hierarchy was probably
incorrect, which in retrospect I think is corroborrated by mech interp work".
The assistant answered that the result the owner drew on ([CLAIM-tmpmugkp](CLAIM-tmpmugkp.md))
is about the order of learning in training time and does not bear on depth,
that [CLAIM-tmp2yj4t](CLAIM-tmp2yj4t.md) does, and that the interpretability evidence is mixed.
The owner: "we can stick with what's warranted".

**For refinement.**

- The residual stream is a shared channel that every layer reads from and
  writes to (Elhage and colleagues, LIT-1534).
- Each layer reads as "performing an incremental update to a latent
  prediction of the next token", with "each successive layer achieving lower
  perplexity", and residual updates point down the loss gradient at every
  layer (the tuned lens, THEORY-tmpky55f). What is refined is the
  prediction: the hidden states' covariance drifts apart with layer
  separation, so each layer needs its own translator.
- "the middle layers seem to share a common representation space"; skipping,
  reordering or running them in parallel degrades benchmarks gracefully, but
  "sharing weights among middle layers is catastrophic, indicating that the
  middle layers are performing different functions": "some degree of
  uniformity (but not redundancy)" (Layers as Painters, THEORY-tmpuxsx9).
  Math and reasoning depend most on order, and Pythia is less robust than
  Llama2 and Mistral.
- Deleting or swapping one middle layer leaves most top-1 predictions
  unchanged in GPT-2 and Pythia, measured as agreement with the original
  model (Lad and colleagues, THEORY-tmpthk75).
- Geva and colleagues (THEORY-1030) find the residual stream refining the
  prediction from layer to layer.
- The parameterization gives no rate differences between groups of blocks
  (CLAIM-tmp2yj4t), which CLAIM-478 (version 5) and CLAIM-tmpy75jv require for
  levels. It does not make blocks alike: under Depth-μP adjacent blocks are
  maximally different, a rough path in depth (THEORY-tmpbyw89), and
  transformers' two-layer blocks have no optimal parametrization in that
  theory. Training can still make stages.

**For an order of stages.**

- The first layer is the most sensitive: intervening on it "is catastrophic
  for model performance for every model" (THEORY-tmpthk75), and skipping
  early layers is catastrophic where skipping middle ones is not
  (THEORY-tmpuxsx9). Final layers form a distinct class; whether they are as
  sensitive differs by family.
- Lad and colleagues hypothesize four stages: detokenization, feature
  engineering, prediction ensembling and residual sharpening, with a change
  about halfway "from iterative refinement to more specialized
  computations" and a first stage that lifts tokens into "higher-level
  representations". Their boundaries "are approximate".
- Tenney and colleagues (THEORY-tmp3dee0) order the layers at which a probe
  best extracts each kind of linguistic information, part of speech and
  constituents early, coreference late, but the middle tasks overlap and
  change order between metrics and models, and "for individual examples the
  model is free to and often does choose a different order". Geva and
  colleagues (THEORY-1033) find a shallow-to-semantic gradient across
  feed-forward layers.

So depth has a coarse order, and it is not a ladder of levels of knowledge.
The order is of processing stages around a middle that is robust without
being redundant; what is refined is a prediction; and the clearest ordering
by abstraction overlaps and is revised from above. The stages are closer to
ordered phases of processing than to pure refinement of one representation.

## What it does not say

- Not that depth carries no hierarchy at all. Tenney and colleagues' ordering
  is one; whether it is "epistemic" depends on what the word means, and the
  claim does not use it.
- Nothing about "epistemic depth" in the sense of Laukkonen, Friston and
  Chandaria ([NOTE-1063](../notes.d/NOTE-1063.md)), which is recursive self-modelling, not layer depth.
- Not beyond the families studied. Robustness to intervention rests on
  GPT-2, Pythia, Llama2, Mistral and BERT.
