---
number: 298
status: Proposed
formerly:
- CASE-tmpoqr8p
title: 'A proposed study: track a newly learned identity in a text-to-image model across training checkpoints, measuring the best-of-N success of a face-match verifier against the single-sample rigidity of the identity, and probe for an identity-specific direction at the transition, to see when a capability reachable by sampling becomes reliable and whether reliability coincides with localization'
version: 1
standing: stipulated
kind: proposed-study
tags:
- representation-learning
- learning-theory
- individuation
date: '2026-11-19'
line:
- learned-structure
draws_on:
- THEORY-2085
bears_on:
- QUESTION-039
- QUESTION-497
summary: >-
  Requested by the owner on 2026-11-19, who offered the unfinished
  identity projects ([LIT-2875](../literature.d/LIT-2875.md), [LIT-2873](../literature.d/LIT-2873.md)) as a directional
  experiment for the difference between a capability achievable by
  sampling and reliable, persisted knowledge. The design is the filer's
  assembly of the owner's measure and hypothesis with [CLAIM-697](../claims.d/CLAIM-697.md)'s and
  [CLAIM-695](../claims.d/CLAIM-695.md)'s sampling route and [CLAIM-765](../claims.d/CLAIM-765.md)'s distinction. Not run.
---
<!-- inactive-ok-file: CLAIM-697 CLAIM-695 CLAIM-765 THEORY-2085 — Proposed or newly filed; cited in this filing -->

# CASE-298: A proposed study: track a newly learned identity in a text-to-image model across training checkpoints, measuring the best-of-N success of a face-match verifier against the single-sample rigidity of the identity, and probe for an identity-specific direction at the transition, to see when a capability reachable by sampling becomes reliable and whether reliability coincides with localization

## Design

1. **Learner and identities.** Fine-tune a text-to-image model (a LoRA or full fine-tune) on images of
identities it does not hold, with a held-out set of reference images per
identity; save checkpoints throughout.
2. **Two curves per identity and checkpoint.** Reachable by sampling: the best-of-N success of a face-match verifier on N
samples from the name prompt, for several N (the sampling route of
[CLAIM-697](../claims.d/CLAIM-697.md) and [CLAIM-695](../claims.d/CLAIM-695.md)). Reliable: the owner's identity strength, the
dispersion of samples from one prompt ([LIT-2873](../literature.d/LIT-2873.md)), and single-sample
verifier success.
3. **The transition.** The checkpoints at which best-of-N success rises, and those at which
single-sample reliability rises; the prediction is a gap, the identity
reachable by sampling well before it is reliable.
4. **Localization.** At each checkpoint, probe for an identity-specific direction in the text
encoder and the denoiser (a linear probe, or the direction a
concept-editing method would edit), and intervene on it: does removing it
remove reliability, sampling reachability, or both? This tests the owner's
sub-hypothesis ([THEORY-2085](../theory.d/THEORY-2085.md)) and asks whether reliable retention is
localized and sampled capability identifiable without being localized
([CLAIM-765](../claims.d/CLAIM-765.md)).
5. **Composition control.** Low-bias names against names carrying strong name-part biases, to separate
an identity composed from learned biases from one stored as unique (the
owner's pseudo-identity distinction).

## What it would show

Whether the move from accidental to reliable capability is a separate
event from acquisition reachable by sampling ([QUESTION-039](../questions.d/QUESTION-039.md)), whether it
coincides with an identity becoming localized ([QUESTION-497](../questions.d/QUESTION-497.md)), and how
many samples reliability is worth at each stage ([CLAIM-697](../claims.d/CLAIM-697.md)).

## What it would cost

Not yet estimated.
