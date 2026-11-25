---
status: Proposed
title: 'In a two-state model of one proposal, in which permission is granted only on the proposal''s own evidence and evidence is produced only under permission, the state with neither is absorbing and is reached with certainty from every state whenever review or investigation can fail; making review more lenient, even certain, never leaves it, and only permission not conditioned on the question''s evidence, as a standing grant gives, or evidence produced without permission, as seed evidence is, breaks it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  The computation is wrong: in the model as stated, with no standing
  grant and no seed evidence, the state with neither evidence nor
  permission can be left, or it is not reached with probability one from
  some state while review or investigation can fail; or some change of
  the review and investigation rates alone, with permission still
  conditioned on the proposal's own evidence and no evidence produced
  without permission, makes it non-absorbing. A richer model in which
  the circle does not close is not a defeater; it is outside the claim.
tags:
- society-and-governance
- probabilistic-modeling
- epistemology
date: '2026-11-25'
line:
- distributed-agency
- learning-and-inquiry
summary: >-
  The assistant's gap fill ([ADR-137](../decisions.d/ADR-137.md)) for the manuscript
  governance-of-becoming, Article 5's G5.3 (the audit of what was left
  out, 2026-11-25, B9): "No model of the circle between evidence and
  permission: no seed evidence, and no absorbing state." [CLAIM-1140](CLAIM-1140.md) (A56
  §5) argues the circle and [CLAIM-1016](CLAIM-1016.md) says how remedies break it, by
  changing the unit of authorization; neither models it. This is the
  smallest model that does, checked with python3 -I. It adds a second
  route [CLAIM-1016](CLAIM-1016.md) does not name: evidence produced outside the circle.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1140 CLAIM-1016 CASE-388 — Proposed; cited in prose with their standing, whatever it is -->

# CLAIM-tmp5ld2o: In a two-state model of one proposal, in which permission is granted only on the proposal's own evidence and evidence is produced only under permission, the state with neither is absorbing and is reached with certainty from every state whenever review or investigation can fail; making review more lenient, even certain, never leaves it, and only permission not conditioned on the question's evidence, as a standing grant gives, or evidence produced without permission, as seed evidence is, breaks it

## The model

One proposal, in discrete periods. Its state is (e, p): whether it holds
evidence this period, and whether it holds permission to investigate.

- **Permission is granted on the proposal's own evidence**: next period
  p = 1 with probability a if e = 1, and with probability g if e = 0.
  Question-by-question authorization, the form A56 §3 states, is g = 0.
- **Evidence is produced only under permission**: next period e = 1 with
  probability b if p = 1, and with probability s if p = 0. With s = 0,
  evidence needs the permission it is meant to justify ([CLAIM-1140](CLAIM-1140.md)).

g is a **standing grant**: permission not conditioned on this question's
evidence, paid once for a domain ([CLAIM-1016](CLAIM-1016.md)'s change of the unit of
authorization: exploratory budgets, protected time, staged approval). s is
**seed evidence**: evidence produced without permission, from slack,
outside work, or a contributor's record elsewhere.

## Admission ([ADR-075](../decisions.d/ADR-075.md)): a derivation

1. With g = s = 0, from (0, 0) next period p = 1 with probability g = 0
   and e = 1 with probability s = 0, so (0, 0) goes only to itself: it is
   absorbing. This holds for every a and b, a = 1 included: leniency of
   review acts only on proposals that already hold evidence.
2. If a < 1 or b < 1, every state reaches (0, 0) with positive probability
   (a failed review or a failed investigation, repeated). A finite chain
   with an absorbing state reachable from every state is absorbed with
   probability one. So in this model even a proposal that starts with
   evidence and permission is lost eventually, at an expected time that
   grows with a and b.
3. With g > 0 or s > 0, (0, 0) is left with probability
   1 − (1 − g)(1 − s) > 0 each period, so it is not absorbing; the chain
   is irreducible and the expected stay in (0, 0) is 1/(1 − (1 − g)(1 − s)).
4. Only a = b = 1 with g = s = 0 keeps a proposal that starts with both;
   then (1, 1) is absorbing as well, and where a proposal ends is fixed by
   where it started, which is [CLAIM-277](CLAIM-277.md)'s trust loop in its sharpest form.

## The check

Run with python3 -I on 2026-11-25 (the script is short enough to give):

```python
import numpy as np
S=[(0,0),(0,1),(1,0),(1,1)]
def P(a,b,g,s):
    M=np.zeros((4,4))
    for i,(e,p) in enumerate(S):
        pp=a if e else g; pe=b if p else s
        for j,(e2,p2) in enumerate(S):
            M[i,j]=(pe if e2 else 1-pe)*(pp if p2 else 1-pp)
    return M
def T(M):  # expected periods to reach (0,0)
    return np.linalg.solve(np.eye(3)-M[1:,1:],np.ones(3))
```

| a | b | g | s | P(leave (0,0)) | expected periods from (1,1) to (0,0) |
|---|---|---|---|---|---|
| 0.5, 0.9 or 1.0 | 0.8 | 0 | 0 | 0 | — |
| 0.90 | 0.80 | 0 | 0 | 0 | 9.6 |
| 0.99 | 0.95 | 0 | 0 | 0 | 49.4 |
| 1.00 | 0.99 | 0 | 0 | 0 | 299.0 |
| 0.90 | 0.80 | 0.05 | 0 | 0.05 (stay 20.0) | not absorbing |
| 0.90 | 0.80 | 0 | 0.05 | 0.05 (stay 20.0) | not absorbing |
| 0.90 | 0.80 | 0.05 | 0.05 | 0.0975 (stay 10.3) | not absorbing |

## What it adds

- **[CLAIM-1140](CLAIM-1140.md)'s inference is blocked in the model**: a proposal in (0, 0)
  fails to persuade whatever its worth, since nothing about the
  possibility behind it enters the chain. Its "failure to persuade does not
  show that the possibility behind it is worthless" holds by construction.
- **[CLAIM-1016](CLAIM-1016.md)'s remedies work as it says, by the unit**: g enters only
  through the rule's form. Raising a, a more lenient reviewer, never
  leaves (0, 0); a standing grant does.
- **A second route [CLAIM-1016](CLAIM-1016.md) does not name**: s, evidence produced
  outside the circle. It breaks the circle without any change to
  authorization. It is also how [CLAIM-406](CLAIM-406.md)'s established contributors
  escape: their evidence comes from elsewhere, so the loop that holds a
  newcomer at (0, 0) never holds them.

## What it does not say

- Nothing about how large g or s must be, or what they cost: a standing
  grant has "initial establishment and continuing maintenance" costs (A18,
  in [CLAIM-1016](CLAIM-1016.md)'s note of 2026-11-24) not in the model.
- Nothing about a proposal's value: there is no hidden worth, so the
  model cannot say which proposals the circle loses. [CASE-388](../cases.d/CASE-388.md)'s proposed
  study, with a hidden true value, would.
- The lag structure (each of e and p set from the other's last value) is
  the simplest closing of the circle; with evidence that persists between
  periods the absorbing state is the same and the times change.

## Standing

Proposed, demonstrated for the model as stated. In the assistant's voice;
adopting it is the owner's call.
