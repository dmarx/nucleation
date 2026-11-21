---
status: Proposed
title: 'A transformer''s depth orders its processing in coarse stages around a broad middle whose layers are nearly interchangeable, refining one representation and its prediction rather than ascending through levels of knowledge: early and final layers are distinct and sensitive, middle layers can be skipped, swapped or repeated with modest loss, and an ordering of linguistic abstraction by layer is the main evidence against reading depth as refinement alone'
version: 1
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
- LIT-tmp8pcca
- LIT-tmpi3ty1
- LIT-tmp40ldm
- LIT-tmp166hz
summary: >-
  The owner, 2026-11-20, after the session's results on rates and depth:
  an earlier thought that transformer depth corresponds to an epistemic
  hierarchy was "probably incorrect, which in retrospect I think is
  corroborrated by mech interp work". The suggestion was not on the record
  and is not filed. This is what the owner and the assistant judged
  warranted in its place: depth as coarse stages and refinement, with the
  evidence on both sides. It rests on four works read only by abstract
  (registered Deferred) and on Elhage and colleagues ([LIT-1534](../literature.d/LIT-1534.md)). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2yj4t CLAIM-478 LIT-tmp8pcca LIT-tmpi3ty1 LIT-tmp40ldm LIT-tmp166hz CLAIM-tmpmugkp CLAIM-tmpy75jv — Proposed or Deferred; the claims this rests on and the works read only by abstract -->

# CLAIM-tmpcvuyr: A transformer's depth orders its processing in coarse stages around a broad middle whose layers are nearly interchangeable, refining one representation and its prediction rather than ascending through levels of knowledge: early and final layers are distinct and sensitive, middle layers can be skipped, swapped or repeated with modest loss, and an ordering of linguistic abstraction by layer is the main evidence against reading depth as refinement alone

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
  writes to (Elhage and colleagues, [LIT-1534](../literature.d/LIT-1534.md)).
- Predictions decoded from each block's hidden state improve "layer by
  layer", read as "iterative inference" (the tuned lens, [LIT-tmp8pcca](../literature.d/LIT-tmp8pcca.md),
  abstract).
- "Middle layers have a surprising amount of uniformity", and some tasks
  survive "skipping layers, running the layers in an order different from
  how they were trained, or running the layers in parallel" (Layers as
  Painters, [LIT-tmpi3ty1](../literature.d/LIT-tmpi3ty1.md), abstract).
- Models keep "72-95% of their original top-1 prediction accuracy" when
  adjacent layers are deleted or swapped, and are "remarkably robust to
  dropping middle layers" (Lad and colleagues, [LIT-tmp40ldm](../literature.d/LIT-tmp40ldm.md), abstract).
- The dynamics give no reason for levels in depth. Under a depth-wise
  parameterization that makes blocks interchangeable increments to the
  stream ([CLAIM-tmp2yj4t](CLAIM-tmp2yj4t.md)), the rate differences between groups of blocks
  that [CLAIM-478](CLAIM-478.md) (version 5) and [CLAIM-tmpy75jv](CLAIM-tmpy75jv.md) require for levels are
  absent. That holds of the parameterization; training could still make
  stages.

**For an order of stages.**

- Early and final layers are distinct and the most sensitive to
  intervention ([LIT-tmpi3ty1](../literature.d/LIT-tmpi3ty1.md), [LIT-tmp40ldm](../literature.d/LIT-tmp40ldm.md)).
- Lad and colleagues hypothesize four stages: detokenization, feature
  engineering, prediction ensembling, and a final sharpening.
- Tenney and colleagues ([LIT-tmp166hz](../literature.d/LIT-tmp166hz.md), abstract) find BERT's regions for
  "POS tagging, parsing, NER, semantic roles, then coreference" appear "in
  the expected sequence", though the model "can and often does adjust this
  pipeline dynamically, revising lower-level decisions on the basis of
  disambiguating information from higher-level representations".

So depth has a coarse order, and it is not a ladder of levels of knowledge.
The order is of processing stages; the broad middle refines a shared
representation; and even the clearest ordering by abstraction is revised
from above.

## What it does not say

- Not that depth carries no hierarchy at all. Tenney and colleagues' ordering
  is one; whether it is "epistemic" depends on what the word means, and the
  claim does not use it.
- Nothing about "epistemic depth" in the sense of Laukkonen, Friston and
  Chandaria ([NOTE-1063](../notes.d/NOTE-1063.md)), which is recursive self-modelling, not layer depth.
- Not that the works say more than their abstracts. They are registered
  Deferred; the claim is Proposed until they are read.
