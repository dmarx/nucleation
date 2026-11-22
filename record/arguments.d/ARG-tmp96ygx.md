---
status: Proposed
title: 'Yang, Steinhardt and Hu''s coarse-label experiments, as an existence case, show a collapse measure saturating on coarse labels while the fine classes stay linearly decodable, so a geometric measure that rises with training is not a measure of what the representation has kept, as the claim on cone occupancy says'
version: 1
form: existence
grounds:
- THEORY-tmp8sxta
concludes:
- CLAIM-800
tags:
- representation-learning
- learning-theory
date: '2026-11-22'
line:
- learned-structure
summary: >-
  In Yang, Steinhardt and Hu (THEORY-tmp8sxta, NOTE-tmpl260d) NC1 goes to
  zero on five coarse labels while label-free clustering plus a linear
  probe recovers the ten original classes at over 93%: a concrete case of
  CLAIM-800's reason for measuring decodability level by level. It does not
  test the claim's chain-rule diagnostic, and the fine-before-coarse order
  it reports is in distances, not decodability. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-800 THEORY-tmp8sxta — Proposed or new; the claim this argues and the reading it uses -->

# ARG-tmp96ygx: Yang, Steinhardt and Hu's coarse-label experiments, as an existence case, show a collapse measure saturating on coarse labels while the fine classes stay linearly decodable, so a geometric measure that rises with training is not a measure of what the representation has kept, as the claim on cone occupancy says

## The inference

CLAIM-800, from A35 §4: occupancy rises under collapse "while
discriminative information falls", so "cone occupancy alone is not a
sufficient learning metric", and §6: fine structure can sit latent under
coarse labels, so both the information present and the information
accessible to restricted decoders should be measured. Yang, Steinhardt and
Hu: on coarse labels "Neural Collapse does happen", yet CLP can "achieve >
93% accuracy on the original CIFAR-10 test set", "even though only 5
coarse labels are provided the entire time."

## Critical questions

- **Is the case coherent?** Yes, as an empirical case: NC1 and NC2 are
  measured on the coarse labels and the probe on the original ten. It is
  single-run and architecture-dependent (VGG collapses fully), which
  limits how general it is, not whether it is a case.
- **Does it separate the very things the conclusion says can come apart?**
  It separates a collapse-type geometric measure (NC1, which saturates)
  from linear decodability of a finer level (which persists). It is not
  cone occupancy, so it supports the general point the claim draws, a
  geometric measure is not a learning measure, by a sibling measure. On the
  claim's §6 prediction it qualifies: under coarse supervision the fine
  clusters appear *before* the label-driven merging. That is an order in
  the distance geometry, not a decodability order, so it does not
  contradict a coarse-to-fine signature defined by decodability, but it is
  a case where a geometric order and the supervised hierarchy run opposite.

## Verdict

Supports CLAIM-800 as an existence case for its motivating point, and
shows that "recoverable by clustering" meant linearly decodable after
label-free clustering. It does not test the chain-rule diagnostic, since
the paper measures no level-wise information over time. Proposed.
