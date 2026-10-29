---
number: 154
status: Active
formerly:
- CLAIM-154
title: 'A candidate structure is worth naming as a unit when its effect-to-noise ratio outruns the Occam cost of keeping it: reify when d''² exceeds the log prior-to-posterior variance ratio, where the model with the candidate stays regular at the parameters that switch it off'
version: 3
history:
- version: 1
  date: '2026-10-11'
  note: >-
    Dual-filed from MOM-CLM-160 under ADR-037. Active here because the
    conjugate-Gaussian case was re-run independently on 2026-10-11: the
    exact Bayes factor, computed from the two marginal likelihoods, and
    the rule agreed to 9e-16 in eight settings (MOM's six and two new
    ones). MOM's non-conjugate logistic check (decision 16 of 16,
    magnitude not) was not re-run, and is taken as MOM reports it.
- version: 2
  date: '2026-10-14'
  note: >-
    Two cautions added under What it does not say, from NOTE-760
    (LIT-238 §6.3: Bayes and MDL can be inconsistent under
    misspecification) and NOTE-801 (THEORY-259, LIT-225: a
    modeller's prior gives the description-length penalty only for
    hypotheses random under it). The rule and its status are unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Narrowed by the eleventh status review (ADR-057, ADR-059) to concede
    CLAIM-188, promoted. Where the model with the candidate is singular
    at the parameters that switch it off, the Laplace posterior the
    derivation needs does not exist; the free-energy penalty there is
    λ log n − (m − 1) log log n, and the regular count overcharges it.
    On CASE-152's product model the rule prunes, near the threshold,
    candidates the exact Bayes factor keeps, which met the old
    defeated_if. THEORY-087 is added to grounds for the regular
    expansion that makes the rule Laplace-valid outside the conjugate
    case. The conjugate case was re-checked: agreement to 5 × 10⁻¹⁴ in
    five new settings; the reviewer's scripts were re-run by the
    reviewing session and reproduce the figures. The old title: A candidate structure is worth naming as a unit when its effect-to-noise ratio outruns the Occam cost of keeping it: reify when d'² exceeds the log prior-to-posterior variance ratio. The old defeated_if: A model family in which the rule and the
    Bayes factor disagree on the keep-or-prune decision near the
    threshold, where the decision is close. Disagreement in magnitude far
    from the threshold does not count: the rule is a criterion and not a
    score, and MOM-CLM-160 already reports that failure.
role: thesis
warrant: demonstrated
defeated_if: >-
  A model family, regular at the parameters that switch the candidate
  off, in which the rule and the Bayes factor disagree on the
  keep-or-prune decision near the threshold, where the decision is
  close. Disagreement in magnitude far from the threshold does not count:
  the rule is a criterion and not a score, and MOM-CLM-160 already
  reports that failure. Nor does a family singular there: CLAIM-188
  concedes that the rule overcharges such a candidate.
tags:
- model-comparison
- complex-systems
- individuation
date: '2026-10-11'
line:
- distributed-agency
- formal-apparatus
complements:
- CLAIM-164
- CLAIM-307
uses:
- TERM-046
summary: >-
  Dual-filed from [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md) ([ADR-037](../decisions.d/ADR-037.md)). By the Savage–Dickey ratio,
  ln BF(keep) = ½(d'² − Occam), so a direction, block or sector is real
  enough to name exactly when δ/ε > τ with τ² = ln(s²/σ²), the information
  the data added about it. In this record it prices the boundary tests for
  a combined form: a near-decomposable block ([LIT-905](../literature.d/LIT-905.md)) earns a name
  when its gap beats its Occam factor. Re-checked here in the conjugate case.
  Narrowed to candidates whose model stays regular where they are switched
  off; where it is singular the rule overcharges (CLAIM-188).
supports:
- CLAIM-157
- CLAIM-174
- CLAIM-332
objected_by:
- CLAIM-188
grounds:
- THEORY-081
- THEORY-087
---
<!-- inactive-ok-file: CLAIM-175 — Proposed; the owner's claim this threshold makes decidable, open -->

# CLAIM-154: A candidate structure is worth naming as a unit when its effect-to-noise ratio outruns the Occam cost of keeping it: reify when d'² exceeds the log prior-to-posterior variance ratio, where the model with the candidate stays regular at the parameters that switch it off

## The claim

From [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md). For one candidate direction w, with a Gaussian prior of
variance s² and a Laplace posterior with mean μ and variance σ², pruning w
is a nested model. Its log Bayes factor is the Savage–Dickey ratio:

ln BF(keep) = ½ μ²/σ² − ½ ln(s²/σ²) = ½ (d'² − Occam), in the notation of [TERM-046](../terms.d/TERM-046.md)<!-- ref::uses: TERM-046 -->.

So the rule is: **keep (reify) w if and only if d'² > Occam**, that is
δ/ε > τ with τ² = ln(s²/σ²). The threshold is not a taste parameter. It is
the prior-to-posterior information gain about w. In the conjugate Gaussian
case the rule is the Bayes factor exactly, not an approximation of it.

**Where it holds.** The derivation needs a Laplace posterior for w. That
needs the model with the candidate to be regular where w = 0: its Fisher
information non-singular there, so that no parameter attached to the
candidate goes unidentified when the candidate is switched off, and a
prior smooth and positive there. Outside the conjugate case the rule is
then Laplace's approximation of the same Bayes factor ([THEORY-087](../theory.d/THEORY-087.md)'s
regular expansion). Two candidates fail the condition: a coupling whose
effect is a strength times a responsiveness, and a hidden unit behind an
output weight ([THEORY-082](../theory.d/THEORY-082.md)). There the penalty is
λ log n − (m − 1) log log n, and the rule prunes near the threshold what
the Bayes factor keeps ([CLAIM-188](CLAIM-188.md), checked on [CASE-152](../cases.d/CASE-152.md)'s model).

## Why this record holds it

The re-check of 2026-10-11 used y ~ N(θ, 1) and θ ~ N(0, s₀²). The exact
log Bayes factor was computed from the marginal likelihoods of the mean
under each model, independently of MOM's derivation. It agreed with
½(d'² − Occam) to 9 × 10⁻¹⁶ in every setting, with the same keep and prune
decisions as MOM's table.

What it gives this record is the answer to a question that was left as a
matter of taste: *how much* stronger interaction inside a candidate system
must be than across its edge before the system earns a name. The owner's
claim that a dancing couple "merits some privileged nomenclature"
([CLAIM-175](CLAIM-175.md)) becomes a decidable question once the coupling is
measured. Simon's near-decomposability ([LIT-905](../literature.d/LIT-905.md)) says what to compare,
[CLAIM-164](CLAIM-164.md) says what the named object is, and this claim says how big
the gap must be. That bearing is this record's. MOM makes the same join for
its own spectral sectors.

## What it does not say

- **That the criterion is free of choices.** The prior variance s² and the
  candidate direction are inputs. The rule prices a candidate; it does not
  find one. The target-relativity of [CLAIM-152](CLAIM-152.md) applies.
- **That the magnitude is trustworthy.** Away from the threshold the Laplace
  form can understate the evidence badly (by ten nats in MOM's logistic
  case). It is a decision rule.
- **That any couple, firm or person has been measured.** Nothing here applies
  it to a real system.
- **That the threshold survives misspecification.** When every candidate
  model is misspecified, which a block or coupling model of a real system
  is, Bayes and MDL can prefer the wrong model for large n, and the remedy
  (Safe Bayes, η < 1) changes the effective Occam cost ([LIT-238](../literature.d/LIT-238.md) §6.3,
  [NOTE-760](../notes.d/NOTE-760.md)). The review cites that result and does not prove it.
  [CLAIM-188](CLAIM-188.md)'s singularity is a limit now written into the title; this is a
  separate caution.
- **That the Occam term is a description length.** Under a modeller's
  prior, the evidence penalty matches the description-length penalty only
  for hypotheses that are random under that prior ([THEORY-259](../theory.d/THEORY-259.md),
  [LIT-225](../literature.d/LIT-225.md), [NOTE-801](../notes.d/NOTE-801.md)). A hypothesis the prior treats as special is where
  the two rankings diverge.

## Note of 2026-10-12: evidence now linked

[THEORY-081](../theory.d/THEORY-081.md) now grounds this claim. The Savage–Dickey ratio is the point-mass case of a general identity for models that differ only in their prior. Its caveat, that Laplace forms are only as good as the full posterior, sits with [CLAIM-188](CLAIM-188.md).
