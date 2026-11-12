---
status: Proposed
title: 'Because a LoRA module is an additive update to one set of frozen pretrained weights, amplifying directions already in them, replacing those weights leaves the module without the base it was defined on, so its effect on the new base is not guaranteed and has to be re-established, by transfer or by retraining'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Weakened at the owner's review of dmarx/nucleation#482: the module's
    being defined relative to W0 shows only that its effect on a new base
    is not guaranteed, not that it must be retrained. Transfer may degrade,
    survive or work well enough.
form: cause-to-effect
grounds:
- THEORY-tmp6v6q8
concludes:
- CLAIM-tmpnwq8a
tags:
- representation-learning
date: '2026-11-12'
line:
- distributed-agency
summary: >-
  The ground for [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md)'s premise after the reading of IP-Adapter
  carried less than it was cited for ([ARG-tmpu8x8a](ARG-tmpu8x8a.md)). LoRA's structure makes
  a module a change to particular weights; the claim needs that, and the
  paper gives it. The step from "defined on W0" to "useless on a different
  W" is the filer's, untested by the paper, and is what a transfer test
  would check. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6v6q8 CLAIM-tmpnwq8a ARG-tmpu8x8a — Proposed or Rejected; filed on the same branch -->

# ARG-tmp4icc1: Because a LoRA module is an additive update to one set of frozen pretrained weights, amplifying directions already in them, replacing those weights leaves the module without the base it was defined on, so its effect on the new base is not guaranteed and has to be re-established, by transfer or by retraining

## The inference

Hu et al. ([THEORY-tmp6v6q8](../theory.d/THEORY-tmp6v6q8.md)) define a module as ΔW = BA added to a frozen
W0, and switch tasks by recovering W0 "by subtracting BA"; §7.3 finds that
ΔW "amplifies some features that are already in W". So the module's effect
is defined relative to W0. Replace W0 by a different base and BA no longer
adds to the weights it was trained against, so whether the specialization
still works has to be re-established; transfer may degrade, survive or
work well enough, and where it fails it must be retrained. That possible
cost is the mechanism behind [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md)'s staleness.

## Critical questions

- **Is the mechanism operative here?** For character LoRAs on image
  models, the paper does not say: it is about language models. That LoRA is
  how character specializations are made is attested in the batch by
  InstantID ("LoRA necessitates individual training for each new
  character") and PhotoMaker. The mechanism holds wherever the module is a
  low-rank delta on one set of weights.
- **Could a confounder produce the same outcome?** The outcome, retraining
  at each new base, could also come from practice (new bases bring better
  results, so users retrain anyway). The inference is about whether the old
  module can be reused, not why users retrain. And a successor fine-tuned
  from its predecessor keeps much of W0, so the module may partly carry
  over; that is the claim's defeater and is untested. The ARG stays
  Proposed until a transfer test.
