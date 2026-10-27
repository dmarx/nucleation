---
status: Proposed
title: 'Lock-in from selectively admitted evidence and lock-in from self-scoring need different remedies: weighting admitted evidence by known, positive admission probabilities undoes the first and leaves the second, so correcting for how evidence was selected is not correcting how it is scored'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A defect in CASE-162's v1.3 runs, such as a self-scoring condition in
  which evidence was in fact censored, so that the null effect of the
  correction there is an artefact; or an inverse-propensity correction
  shown to undo self-scoring in a model where nothing is censored.
tags:
- self-governance
- probabilistic-modeling
- epistemology
date: '2026-10-27'
line:
- distributed-agency
grounds:
- CASE-162
complements:
- CLAIM-404
- CLAIM-297
summary: >-
  Stated in CASE-162's "What it can show" and held by no claim, found in
  the audit of 2026-10-27. In the lab's population, admission that depends
  on the record left the worse alternative in charge in 41 of 64 worlds,
  and exact inverse-propensity weighting brought that to 0 below full
  selectivity; with self-scoring alone (c = 0.5, nothing censored) 39 of 64
  stayed wrong and the correction changed nothing. CLAIM-404 holds that
  the informational and evaluative routes are distinct; this says their
  remedies are too. The edge: the correction is an oracle's, with known
  propensities.
---

# CLAIM-tmpm0bix: Lock-in from selectively admitted evidence and lock-in from self-scoring need different remedies: weighting admitted evidence by known, positive admission probabilities undoes the first and leaves the second, so correcting for how evidence was selected is not correcting how it is scored

## The claim

CASE-162's v1.3 results, as stored, worlds with a wrong incumbent out of
64, no self-scoring: at selectivity 0.5, 0.75 and 1, naive credit leaves
31, 41 and 41 wrong; exact inverse-propensity weighting leaves 0, 0 and 5,
the 5 where admission probabilities near zero break the correction's
positivity condition. At s = 0.75 selection reverses the sign of the
evidence: the raw cue mean is −0.193 and the admitted mean +0.184. And:
"Self-scoring alone, c = 0.5 with s = 0, leaves 39 of 64 wrong. Nothing is
censored there, so the correction changes nothing." With both, the
correction removes the part due to selection (at c = 0.25, s = 0.5, 41 to
0; at c = 0.5, s = 0.5, 41 to 34).

CLAIM-404 says an organization can be governed from outside through the
evidence its procedures receive or through the criteria they weigh it by,
and that the two routes are distinct. The runs show the remedies are
distinct too: knowing how evidence was admitted repairs the first route
and is idle on the second, because a self-scored record is biased in what
it counts, not in what it was shown. CLAIM-297's amplification without
fidelity is the self-scoring half; CASE-156 the selection half.

## What it does not say

- **A procedure for unknown propensities.** The correction was given the
  exact admission probabilities, as an oracle (CASE-162: "A procedure for
  unknown or zero propensities" is what it cannot show).
- **The remedy for self-scoring.** Independent scoring is the natural one
  (CLAIM-342's evidence that does not pass through the interpretation it
  tests); the runs do not test it.
- **Anything beyond the stipulated population**, whose case is Proposed.
