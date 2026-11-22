---
status: Proposed
title: 'An alternative to the stop-word half of the owner''s truncated-band account: top spectral directions that track the data''s leading principal components, its common high-variance structure, may be a mark of under-trained or large-step regimes that learning reorganizes away from, rather than a standing feature of a learned spectrum'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  In trained language models, the unembedding's top singular directions
  tracking token frequency, or another common high-variance structure of
  the data, as strongly in well-trained checkpoints at moderate step sizes
  as in early checkpoints or large-step runs, so that the common-structure
  signature does not fade with training and does not depend on the regime.
  Not met by a strong frequency correlation measured in one checkpoint of
  one regime, which both readings allow.
tags:
- representation-learning
- learning-theory
date: '2026-11-22'
line:
- learned-structure
objects_to:
- CLAIM-tmp2r6ur
grounds:
- THEORY-tmphbp5a
uses:
- TERM-tmpf5ymd
summary: >-
  A rival reading, in the assistant's voice, of one part of the owner's
  CLAIM-tmp2r6ur: the part that says the top directions carry common,
  weakly discriminating structure, as stop words do. It does not rival the
  floor or the band. From Park and colleagues' Fig. 16 (THEORY-tmphbp5a,
  NOTE-tmpzethm): in first-layer weights of a ReLU MLP on UTKFace, the
  leading learned direction overlaps the data's first principal component
  at 0.68 and 0.64 only in the large-step regimes, which converge to a
  worse minimum, and at 0.056 in the well-trained phase, whose leading
  modes "capture nontrivial structure in the data that deviates from the
  principal components". If that transfers, the stop-word signature is a
  stage or regime, not a standing property. Marked as an alternative to
  the owner's account; the other alternative is CLAIM-tmpufbx6, which
  rivals the floor and the band instead. ARG-tmpun4nl argues the transfer.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp2r6ur THEORY-tmphbp5a TERM-tmpf5ymd CLAIM-tmpufbx6 ARG-tmpun4nl LEAD-tmptgrc7 — Proposed or new; the owner's claim this rivals, its grounds, the other alternative and the test -->

# CLAIM-tmp9atj9: An alternative to the stop-word half of the owner's truncated-band account: top spectral directions that track the data's leading principal components, its common high-variance structure, may be a mark of under-trained or large-step regimes that learning reorganizes away from, rather than a standing feature of a learned spectrum

**Which part it rivals.** The owner's CLAIM-tmp2r6ur has three parts: the
top directions carry common, weakly discriminating structure (stop words);
the extreme bottom carries low-signal outliers (rare words); the bottom of
the retained band is the most discriminating. This reading rivals only the
first, and only as a standing property of a learned spectrum. It is
**alternative (a)**; CLAIM-tmpufbx6 is alternative (b), on the other two
parts. The owner chooses.

**The reading.** Top directions that carry the data's common, high-variance
structure, the analogue of stop words, are what a network shows when its
training signal is weak or incoherent: early in training, or at step sizes
large enough that the supervised part of the gradient averages out. As
learning proceeds in a good regime, the top directions are reorganized
toward task-relevant structure that departs from the data's principal
components.

**Where it comes from.** Park and colleagues (THEORY-tmphbp5a, §V C,
Fig. 16), UTKFace, first-layer weights:

| regime | overlap of leading learned feature with PCA-1 |
|---|---|
| ferromagnetic (well trained) | 0.056 |
| disordered | 0.003 |
| mixed paramagnetic–disordered | 0.642 |
| paramagnetic, convergent (large step, worse minimum) | 0.681 |

In the large-step regime "learning is dominated by the principal covariance
directions of the data rather than by task-relevant nonlinear
representations"; their explanation is that the supervised part of the
backpropagated error is "effectively incoherent" there, so the weights
inherit the input covariance.

**What it does not say.** Not that the unembedding behaves so: the
evidence is one MLP regressor's first layer, and an unembedding is read
against next-token targets whose frequency structure is itself the task in
part (ARG-tmpun4nl). Not that the owner's account is wrong for a
well-trained language model; the two readings predict differently only
across training stage and step size, which is why LEAD-tmptgrc7 now asks
for both to be recorded.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
