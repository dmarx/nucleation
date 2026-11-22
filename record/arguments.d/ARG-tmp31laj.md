---
status: Rejected
title: "Yang's pitchfork of a detached Gaussian-mixture probe, read as grounds, carries the threshold, pitchfork and local-coefficient dip of a factored feature under weight decay"
version: 1
form: evidence
grounds:
- THEORY-tmpu0f9k
concludes:
- CLAIM-807
tags:
- learning-theory
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
summary: >-
  CLAIM-807 listed Yang's preprint (LIT-2961) among its grounds while it
  was unread, from A42's citation of it as related work. Read
  (NOTE-tmpg5q4t), it is a parallel, not evidence: the same supercritical
  normal form and the same kind of parameter symmetry, but in a detached
  probe's precision rather than a factored feature under weight decay, and
  with nothing on local learning coefficients. Rejected as a ground;
  LIT-2961 leaves CLAIM-807's grounds, and the parallel stays as a dated
  note there. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
  Standing of the conclusion apart from this route: CLAIM-807 is a
  demonstrated claim and stands on its own derivation, checked step by
  step in its body; its caveat that the pitchfork is a symmetry of the
  parameters gains a second instance from this reading, held in the
  claim's note of 2026-11-22.
---
<!-- inactive-ok-file: CLAIM-807 THEORY-tmpu0f9k — Proposed; the claim and the reading this argument joins -->

# ARG-tmp31laj: Yang's pitchfork of a detached Gaussian-mixture probe, read as grounds, carries the threshold, pitchfork and local-coefficient dip of a factored feature under weight decay

## The inference

CLAIM-807 derives, for L(a, b) = ½(ab − s)² + (λ/2)(a² + b²), a threshold
q* = (s − λ)₊, a pitchfork in the parameters at s = λ, algebraic
relaxation there, a dip of the local coefficient from 1 to 3/4, and quiet
but consequential growth just above threshold. It cited Yang (LIT-2961)
among its grounds. Ground: THEORY-tmpu0f9k.

## Critical questions (evidence)

**Does the evidence bear on the conclusion's own subject?** No. Yang's
bifurcation parameter is the precision β of a Gaussian-mixture probe
whose gradients never reach the encoder ("the encoder's gradients never
see the probe", App. K). CLAIM-807's is the signal strength against the
weight decay in a factored predictor. The two systems share a normal form,
ε̇ = με − αε³, and nothing else.

**Does it bear on any step?** On none of the derivation. On the caveat,
only by analogy: in Yang the broken symmetry is which prototype takes
which direction ("any anti-symmetric w in component space", §3.2), a
symmetry of the probe's parameters; in CLAIM-807 it is the sign of
a = b. Both pitchforks are in parameters whose symmetric branches give
the same predictor up to relabelling. An analogy gets a note, not an
edge.

**Does it bear on the local coefficient?** No. The paper never mentions
singular learning theory, the RLCT or Watanabe, and below βc its merged
state is a nondegenerate minimum.

**Is weight decay's role the same?** No. In Yang's grokking runs the
crossing comes at steps 34–60 with or without weight decay; weight decay
sets only the escape time after the crossing. In CLAIM-807 weight decay
sets the threshold itself.

## Verdict

Rejected as a ground. LIT-2961 is removed from CLAIM-807's `grounds`; the
claim's dated note of 2026-11-22 records the parallel.
