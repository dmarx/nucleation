---
number: 466
status: Active
formerly:
- CLAIM-tmpm0bix
title: 'Selection and self-scoring lock-in need two cures'
statement: >-
  Lock-in from selectively admitted evidence and lock-in from self-scoring
  need different remedies: weighting admitted evidence by known, positive
  admission probabilities undoes the first and leaves the second, so
  correcting for how evidence was selected is not correcting how it is
  scored
version: 5
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted at the twentieth status review (ADR-057), at the status
    review's ruling (the owner delegated these rulings), with its ground
    CASE-162, whose v1.3 figures were re-checked against the stored
    results. Nothing objects to it, and nothing in the record meets its
    defeated_if: in the self-scoring-only condition (c = 0.5, s = 0) the
    stored admission fraction is 1.0, so nothing was censored, and with
    every propensity 1 the inverse-propensity weights are all 1 and the
    correction is the identity. The body's "whose case is Proposed" is
    dropped. The claim is unchanged.
- version: 3
  date: '2026-11-23'
  note: >-
    Joins the work governance-of-possibility (ADR-144) at its
    membership pass of 2026-11-23, under ADR-104's rule: the revised
    manuscript in scratch/manuscripts/governance-of-possibility/ states
    its proposition or uses it as a step, in §4.1. No other change.
- version: 4
  date: '2026-11-25'
  note: >-
    Gains the line self-correction (atlas scope 10) under ADR-tmpd3ckn:
    the entry is in that scope's core fiber in the hyperarticle atlas v0.3
    (scratch/atlas/atlas-v0.3.md), and each atlas scope is documented as a
    line. No other change.
- version: 5
  date: '2026-11-25'
  note: >-
    Joins the work conditions-of-correction (ADR-tmp85hdc): Article 1 of
    A45 in the exchange "Hyper article interpretation" states its
    proposition or uses it as a step, in §5. No other change.
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
- self-correction
grounds:
- CASE-162
complements:
- CLAIM-404
- CLAIM-297
summary: >-
  Stated in [CASE-162](../cases.d/CASE-162.md)'s "What it can show" and held by no claim, found in
  the audit of 2026-10-27. In the lab's population, admission that depends
  on the record left the worse alternative in charge in 41 of 64 worlds,
  and exact inverse-propensity weighting brought that to 0 below full
  selectivity; with self-scoring alone (c = 0.5, nothing censored) 39 of 64
  stayed wrong and the correction changed nothing. [CLAIM-404](CLAIM-404.md) holds that
  the informational and evaluative routes are distinct; this says their
  remedies are too. The edge: the correction is an oracle's, with known
  propensities.
works:
- conditions-of-correction
- governance-of-possibility
---
<!-- inactive-ok-file: CLAIM-758 THEORY-1353 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-466: Selection and self-scoring lock-in need two cures

## The claim

[CASE-162](../cases.d/CASE-162.md)'s v1.3 results, as stored, worlds with a wrong incumbent out of
64, no self-scoring: at selectivity 0.5, 0.75 and 1, naive credit leaves
31, 41 and 41 wrong; exact inverse-propensity weighting leaves 0, 0 and 5,
the 5 where admission probabilities near zero break the correction's
positivity condition. At s = 0.75 selection reverses the sign of the
evidence: the raw cue mean is −0.193 and the admitted mean +0.184. And:
"Self-scoring alone, c = 0.5 with s = 0, leaves 39 of 64 wrong. Nothing is
censored there, so the correction changes nothing." With both, the
correction removes the part due to selection (at c = 0.25, s = 0.5, 41 to
0; at c = 0.5, s = 0.5, 41 to 34).

[CLAIM-404](CLAIM-404.md) says an organization can be governed from outside through the
evidence its procedures receive or through the criteria they weigh it by,
and that the two routes are distinct. The runs show the remedies are
distinct too: knowing how evidence was admitted repairs the first route
and is idle on the second, because a self-scored record is biased in what
it counts, not in what it was shown. [CLAIM-297](CLAIM-297.md)'s amplification without
fidelity is the self-scoring half; [CASE-156](../cases.d/CASE-156.md) the selection half.

## What it does not say

- **A procedure for unknown propensities.** The correction was given the
  exact admission probabilities, as an oracle ([CASE-162](../cases.d/CASE-162.md): "A procedure for
  unknown or zero propensities" is what it cannot show).
- **The remedy for self-scoring.** Independent scoring is the natural one
  ([CLAIM-342](CLAIM-342.md)'s evidence that does not pass through the interpretation it
  tests); the runs do not test it.
- **Anything beyond the stipulated population** of the case.

## Note of 2026-11-19: the exchange "Topological protection explained"

A71 §8 proposed three developmental traps for learners. A plasticity trap: the organization "is difficult to alter even when appropriate evidence is supplied". An inquiry trap: it "prevents the learner from seeking or recognizing the evidence required to alter it". An evaluation trap: the learner "can generate a better alternative but lacks a sufficiently independent mechanism for recognizing it". This claim already separates lock-in by selectively admitted evidence from lock-in by self-scoring, and shows their remedies differ; that is nearly A's inquiry/evaluation split, though A's inquiry trap also takes in recognizing evidence, which this claim puts on the scoring side. The plasticity trap is [THEORY-1353](../theory.d/THEORY-1353.md)'s site depletion, which more data cannot undo. A did not cite this claim.

A67 §8: "A learner can overfit not only to its training data, but to its own strategy for selecting training data", the selection half of this claim made endogenous to a learner. The overconsolidation claim filed from the same exchange, [CLAIM-758](CLAIM-758.md), takes these traps among its mechanisms.

No status change.
