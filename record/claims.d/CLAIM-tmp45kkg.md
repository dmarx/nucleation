---
status: Active
title: 'A candidate structure is worth naming as a unit when its effect-to-noise ratio outruns the Occam cost of keeping it: reify when d''² exceeds the log prior-to-posterior variance ratio'
version: 1
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
role: thesis
defeated_if: >-
  A model family in which the rule and the Bayes factor disagree on the
  keep-or-prune decision near the threshold, where the decision is
  close. Disagreement in magnitude far from the threshold does not count:
  the rule is a criterion and not a score, and MOM-CLM-160 already
  reports that failure.
tags:
- model-comparison
- complex-systems
- individuation
date: '2026-10-11'
line: distributed-agency
complements:
- CLAIM-tmpjsasy
summary: >-
  Dual-filed from [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md) ([ADR-037](../decisions.d/ADR-037.md)). By the Savage–Dickey ratio,
  ln BF(keep) = ½(d'² − Occam), so a direction, block or sector is real
  enough to name exactly when δ/ε > τ with τ² = ln(s²/σ²), the information
  the data added about it. In this record it prices the boundary tests for
  a combined form: a near-decomposable block ([LIT-tmp6qp14](../literature.d/LIT-tmp6qp14.md)) earns a name
  when its gap beats its Occam factor. Re-checked here in the conjugate case.
---
<!-- inactive-ok-file: ADR-037 — Proposed; the decision this entry is filed under -->
<!-- inactive-ok-file: CLAIM-tmpygda8 — Proposed; the owner's claim this threshold makes decidable, open -->

# CLAIM-tmp45kkg: A candidate structure is worth naming as a unit when its effect-to-noise ratio outruns the Occam cost of keeping it: reify when d'² exceeds the log prior-to-posterior variance ratio

## The claim

From [MOM-CLM-160](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-160.md). For one candidate direction w, with a Gaussian prior of
variance s² and a Laplace posterior with mean μ and variance σ², pruning w
is a nested model. Its log Bayes factor is the Savage–Dickey ratio:

ln BF(keep) = ½ μ²/σ² − ½ ln(s²/σ²) = ½ (d'² − Occam).

So the rule is: **keep (reify) w if and only if d'² > Occam**, that is
δ/ε > τ with τ² = ln(s²/σ²). The threshold is not a taste parameter. It is
the prior-to-posterior information gain about w. In the conjugate Gaussian
case the rule is the Bayes factor exactly, not an approximation of it.

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
([CLAIM-tmpygda8](CLAIM-tmpygda8.md)) becomes a decidable question once the coupling is
measured. Simon's near-decomposability ([LIT-tmp6qp14](../literature.d/LIT-tmp6qp14.md)) says what to compare,
[CLAIM-tmpjsasy](CLAIM-tmpjsasy.md) says what the named object is, and this claim says how big
the gap must be. That bearing is this record's. MOM makes the same join for
its own spectral sectors.

## What it does not say

- **That the criterion is free of choices.** The prior variance s² and the
  candidate direction are inputs. The rule prices a candidate; it does not
  find one. The target-relativity of [CLAIM-tmp3qyzh](CLAIM-tmp3qyzh.md) applies.
- **That the magnitude is trustworthy.** Away from the threshold the Laplace
  form can understate the evidence badly (by ten nats in MOM's logistic
  case). It is a decision rule.
- **That any couple, firm or person has been measured.** Nothing here applies
  it to a real system.
