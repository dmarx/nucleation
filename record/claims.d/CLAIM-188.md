---
number: 188
status: Active
formerly:
- CLAIM-tmpczjuu
title: 'Where the model with a candidate structure is singular at the parameters that switch the candidate off, with real log canonical threshold λ below d/2 and multiplicity m, the reification rule''s Gaussian Occam term overcharges keeping the candidate by (d/2 − λ) log n + (m − 1) log log n to leading order, so near the threshold the rule prunes candidates the Bayes factor keeps, and its derivation holds only where that model stays regular'
version: 4
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-188.yaml, batch 003,
    ADR-047). The title put the singularity in the model left after the
    candidate is removed. It is in the model with the candidate, at the
    parameters where the candidate's contribution is zero: for an MLP, an
    output weight of zero (THEORY-082). The reduced model is typically
    regular. The title is restated in that form, and as the conditional the
    argument supports: it holds where λ < d/2. "Misprices" becomes
    "overcharges", the direction the body already derives. The sentence on
    removing blocks is corrected to match. The status stays Proposed until
    THEORY-087's singular half is held as a proof or the claim's own test is
    run.
- version: 3
  date: '2026-10-29'
  note: >-
    THEORY-079 moved from grounds to corroborated_by (ADR-058): the
    claim's title is about CLAIM-154's rule, not Bayesian model reduction,
    which THEORY-079 is about, and THEORY-082 supplies the premise that
    the candidates are the singular kind. THEORY-087, its other ground, was
    promoted by the same review. The claim is unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Promoted by the eleventh status review (ADR-057; ADR-047's ruling on
    re-derivations). The status had waited on THEORY-087's singular half
    or on the claim's own test. THEORY-087 was promoted by the tenth
    review, and the test is run in the note of this date on CASE-152's
    model: near the threshold the exact Bayes factor keeps candidates the
    regular count prunes, at every n from 10² to 10¹². The scripts were
    written by the reviewer and re-run by the reviewing session, and
    reproduce the figures. CLAIM-154 is narrowed to write this in. The
    title adds the log log n term and the multiplicity, and replaces
    "exact only where that model stays regular", since even in regular
    models the rule is exact only in the conjugate case. CASE-152 is
    added under illustrated_by. The old title: Where the model with a candidate structure is singular at the parameters that switch the candidate off, with real log canonical threshold λ below d/2, the reification rule's Gaussian Occam term overcharges keeping the candidate by a term that grows as (d/2 − λ) log n, so the rule is exact only where that model stays regular.
role: counter
warrant: demonstrated
tags:
- model-comparison
- individuation
date: '2026-10-11'
line:
- distributed-agency
- formal-apparatus
objects_to:
- CLAIM-154
grounds:
- THEORY-087
- THEORY-031
- THEORY-082
corroborated_by:
- THEORY-079
illustrated_by:
- CASE-152
summary: >-
  A narrowing of [CLAIM-154](CLAIM-154.md), filed on 2026-10-11 from a synthesis review
  that found the record already held the readings that limit it.
  [CLAIM-154](CLAIM-154.md)'s rule prices a candidate with a Gaussian Occam factor, which
  is exact in the conjugate case it was re-checked in. The candidates it
  is meant for (blocks, sectors, couplings with hidden structure) are
  often singular where they are switched off. There THEORY-087 puts the
  penalty at λ log n − (m − 1) log log n, not (d/2) log n. On CASE-152's
  product model the rule prunes, near the threshold, candidates the
  exact Bayes factor keeps. CLAIM-154 is narrowed to models that stay
  regular at the switch-off.
---
<!-- inactive-ok-file: CLAIM-174 CLAIM-175 THEORY-079 — Proposed; open, and cited as open: under test, not settled -->

# CLAIM-188: Where the model with a candidate structure is singular at the parameters that switch the candidate off, with real log canonical threshold λ below d/2 and multiplicity m, the reification rule's Gaussian Occam term overcharges keeping the candidate by (d/2 − λ) log n + (m − 1) log log n to leading order, so near the threshold the rule prunes candidates the Bayes factor keeps, and its derivation holds only where that model stays regular

## The claim

[CLAIM-154](CLAIM-154.md) says to keep a candidate direction, block or sector when
d'² exceeds the Occam term ln(s²/σ²), with a Gaussian prior and a Laplace
posterior. "In the conjugate Gaussian case the rule is the Bayes factor
exactly", and that case was re-run here. Its own caveat is about
magnitude far from the threshold: "Away from the threshold the Laplace
form can understate the evidence badly."

The limit this claim adds is about the kind of model, not the distance
from the threshold:

- **The penalty depends on regularity.** In a regular model the Occam
  factor comes from the curvature at the optimum and grows as (d/2) log n.
  In a singular model, where the Fisher information is degenerate at the
  optimum, it grows as λ log n, with λ the real log canonical threshold,
  and λ falls below d/2 when the prior is positive on the optimal set
  ([THEORY-087](../theory.d/THEORY-087.md), from MacKay and Watanabe).
- **Laplace-based pruning misprices singular reductions.** [THEORY-079](../theory.d/THEORY-079.md) says
  Bayesian model reduction under the Laplace approximation charges the
  reductions of a singular parent with a Gaussian Occam factor, so its
  evidence differences can be wrong by a term that grows with log n. The
  same arithmetic is in [CLAIM-154](CLAIM-154.md)'s rule.
- **The candidates are the singular kind.** Models "with hierarchical
  layers or hidden variables are singular" ([THEORY-079](../theory.d/THEORY-079.md), citing Watanabe).
  [CLAIM-154](CLAIM-154.md) is put to work on near-decomposable blocks, on couplings
  ([CLAIM-174](CLAIM-174.md)) and on the owner's dancing couple ([CLAIM-175](CLAIM-175.md)). A model that
  contains a block or a coupling is singular where the coupling is switched
  off. There the parameters attached to it are not identified, because any
  value of them gives the same distribution once the coupling's strength is
  zero. When the reduced model is the truth, this is the case at the true
  parameter. [CASE-152](../cases.d/CASE-152.md)'s product model is such a family, and the note of
  2026-10-29 checks the rule on it.

The direction of the error follows from [THEORY-087](../theory.d/THEORY-087.md).
Where λ < d/2, the true penalty is smaller than the Gaussian term, so the
rule overcharges a candidate and prunes structure the exact Bayes factor
would keep. Because the gap grows with log n, more data does not wash it
out, and near the threshold it can flip the decision. That is the kind of
failure [CLAIM-154](CLAIM-154.md)'s own defeater counts.

[THEORY-031](../theory.d/THEORY-031.md) adds a smaller point. d' separates sensitivity from criterion
only for equal-variance normal signal and noise. The rule's "effect-to-noise
ratio" inherits that assumption.

## What it does not say

- It does not say [CLAIM-154](CLAIM-154.md) is wrong where it was checked. The conjugate
  case is exact, and nothing here touches it.
- It does not say the error always runs one way. λ < d/2 is the case
  [THEORY-087](../theory.d/THEORY-087.md) names. Other singular structures need their own λ.
- It does not prove Watanabe's Theorem 2 in general. It rests on
  [THEORY-087](../theory.d/THEORY-087.md), which holds the theorem as cited and checks its prediction
  exactly in singular models of known λ, and on the threshold computation
  in the note of 2026-10-29, which covers one family. That a candidate
  the rule keeps is kept by the Bayes factor too is shown there, not in
  general.
- d is the dimension of the model with the candidate, in the
  parametrization the prior is placed on. Singularity belongs to model
  and prior together. The uniform prior on [CASE-152](../cases.d/CASE-152.md)'s a and b induces on
  c = ab a density that diverges at zero; a Gaussian prior placed on c
  itself makes the model regular and the rule exact.
- [CLAIM-154](CLAIM-154.md) is dual-filed from the mathematics-of-meaning record
  ([MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md)). The same limit would apply there. Filing it there is
  that record's business.

## What would answer it

The rule and an exact or WBIC-estimated Bayes factor agree on keep or
prune near the threshold, across n, in a family where removing the
candidate makes the model singular.

## Note of 2026-10-12: an Active ground for the premise

[THEORY-082](../theory.d/THEORY-082.md) now grounds this claim. The Fisher of a multilayer perceptron "loses rank wherever an output weight is zero", and pruning a hidden unit is exactly that case. It supplies, from an Active THEORY, this claim's premise that the candidates are the singular kind.

## Note of 2026-10-14: a second ground for caution

Grünwald & Roos ([LIT-238](../literature.d/LIT-238.md) §6.3, read in [NOTE-760](../notes.d/NOTE-760.md)) give a second,
independent ground for the same caution. When every candidate model is
misspecified, as a block or coupling model of a real system is, Bayes and
MDL can prefer the wrong model for large n, and the remedy (Safe Bayes,
η < 1) changes the effective Occam cost. The review cites the result and
does not prove it. [THEORY-259](../theory.d/THEORY-259.md) ([LIT-225](../literature.d/LIT-225.md), [NOTE-801](../notes.d/NOTE-801.md)) adds that a
modeller's prior gives the description-length penalty only for hypotheses
that are random under that prior.

## Note of 2026-10-29: the check on a concrete family

[CASE-152](../cases.d/CASE-152.md)'s model, Y ~ N(ab, 1), with a uniform prior on [−1, 1]², against
a = 0, the model with no parameters. The data enter through
ĉ ~ N(ab, 1/n). With z = √n ĉ, the exact keep threshold z*², found by
quadrature, tracks log n − 2 log log n + 1.2. The regular two-parameter
count keeps only when z² > 2 log n − 2 ln(π/2).

| n | exact z*² | log n − 2 log log n | regular count's threshold |
|---|---|---|---|
| 10² | 2.75 | 1.55 | 8.31 |
| 10³ | 4.34 | 3.04 | 12.91 |
| 10⁴ | 6.08 | 4.77 | 17.52 |
| 10⁶ | 9.84 | 8.56 | 26.73 |
| 10⁸ | 13.83 | 12.59 | 35.94 |
| 10¹⁰ | 17.95 | 16.75 | 45.15 |
| 10¹² | 22.16 | 20.99 | 54.36 |

Between the two thresholds the decisions are opposite while both log
Bayes factors are modest. At n = 10⁴ and z² = 12 the exact ln BF is +2.85
and the regular count's −2.76; at n = 10⁶ and z² = 16, +3.03 and −5.36; at
n = 10⁸ and z² = 25, +5.55 and −5.47. Counting the candidate as one
direction, with threshold log n plus a constant, still overcharges, by a
gap in z² growing as 2 log log n (3.1, 4.6 and 5.5 at n = 10⁴, 10⁸ and
10¹²). That meets the "What would answer it" test above against the rule,
in a family where switching the candidate off makes the model singular.
The scripts were written by the reviewer, re-run by the reviewing
session, and are not in the record.
