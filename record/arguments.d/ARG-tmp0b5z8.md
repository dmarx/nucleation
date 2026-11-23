---
status: Proposed
title: The miscalibrated-beacon arm of the record's simulated sensor network,
  as an existence case, shows that what a system is prevented from rewriting
  bounds what its correction can reach, and so narrows the owner's principle
  that self-correction depends on what the system cannot rewrite or reject
version: 1
form: existence
grounds:
- CASE-tmp33vf4
concludes:
- CLAIM-tmpw11e6
tags:
- society-and-governance
- epistemology
date: '2026-11-23'
line:
- distributed-agency
summary: 'The case: a protected but miscalibrated beacon (study_beacon_bias.py,
  40 seeds). The step: one system meeting the principle''s protection condition
  whose correction still converges on an error, and recovers only through
  a further protected channel. The conclusion is held in [CLAIM-tmpw11e6](../claims.d/CLAIM-tmpw11e6.md),
  which objects to and narrows the owner''s [CLAIM-tmp4h9rc](../claims.d/CLAIM-tmp4h9rc.md)
  without rejecting it. The wording is the assistant''s (Claude, in this session);
  adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-tmp4h9rc CLAIM-tmpvqmwc — Proposed or Open; cited in this filing of 2026-11-23 -->

# ARG-tmp0b5z8: The miscalibrated-beacon arm of the record's simulated sensor network, as an existence case, shows that what a system is prevented from rewriting bounds what its correction can reach, and so narrows the owner's principle that self-correction depends on what the system cannot rewrite or reject

## The argument

The owner's principle ([CLAIM-tmp4h9rc](../claims.d/CLAIM-tmp4h9rc.md)) names what a system is prevented
from rewriting or rejecting as a condition of self-correction. In the
network, the protected beacon meets that condition, and the network
corrects toward the beacon. When the beacon is miscalibrated, the
network's late error is the beacon's miscalibration (0.360 against
|δ| = 0.361). So meeting the condition does not secure correction toward
the truth, only toward the anchor. A further protected channel reduces
the error (0.122 with a survey every 100 steps).

## Critical questions

- **Is the case of the kind the principle speaks of?** Yes. The beacon
  arm is one of the principle's own instances ([CLAIM-tmpvqmwc](../claims.d/CLAIM-tmpvqmwc.md)), with one
  parameter changed.
- **Is the result robust in the model?** 40 of 40 seeds lie between 0.328
  and 0.393. The survey arms are monotone in the survey's rate.
- **Does it reject the principle?** No. It narrows the protection clause:
  protection enables correction relative to the anchor, and the anchor's
  own correctness is a further condition, met here only by another
  protected channel.
- **Could the network detect the miscalibration from inside?** Not in
  this model. The radius, its own consistency measure, is the same as
  with a correct beacon.
