---
number: 813
status: Proposed
formerly:
- CLAIM-tmpcgvcp
title: 'Sloppiness and singularity are different properties of a statistical model: sloppiness is a spread of small but nonzero Fisher eigenvalues in a regular model, singularity is rank loss on a stratum of parameter space, so a model can be sloppy everywhere and singular nowhere or singular everywhere with no spread, and at a singular point the Fisher spectrum does not give the learning coefficient'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A model in which a spread of nonzero Fisher eigenvalues forces rank loss
  somewhere in the parameter space, so that sloppiness entails a singular
  stratum; or a rule that computes the real log canonical threshold at a
  singular point from the Fisher matrix at that point alone, checked on
  models whose loss differs only beyond second order (u² + v⁴ against
  u² + v⁶). A model that is both sloppy and singular does not defeat it:
  the claim is that the properties come apart, not that they never meet.
tags:
- information-geometry
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
rests_on:
- CLAIM-305
grounds:
- THEORY-087
- THEORY-082
- THEORY-774
- CASE-152
- CASE-302
- THEORY-2156
- THEORY-2155
uses:
- TERM-135
summary: >-
  A39 §§1, 3–4 of the exchange "Rich Get Richer Power Laws" (2026-11-21),
  answering the owner's U24: "A model can be highly sloppy without being
  singular at the current parameter values. And a singular model need not
  exhibit a long hierarchy of hyperribbon widths." With A37 §1's point
  that a parameter singularity is not a singularity of the data manifold,
  and the assistant's two separating examples, both checked. The wording
  is A's (the other assistant in the exchange "Rich Get Richer Power
  Laws", A39); adopting it is the owner's call.
---

<!-- inactive-ok-file: TERM-135 CASE-302 CLAIM-812 CLAIM-808 — Proposed or new, or Deferred works not yet read; filed with this claim -->
<!-- inactive-ok-file: ARG-133 THEORY-2155 THEORY-2156 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

<!-- inactive-ok-file: THEORY-tmpx26x7 — Proposed or new; the reading of the 2023 review by Quinn and colleagues, 2026-11-22 -->

# CLAIM-813: Sloppiness and singularity are different properties of a statistical model: sloppiness is a spread of small but nonzero Fisher eigenvalues in a regular model, singularity is rank loss on a stratum of parameter space, so a model can be sloppy everywhere and singular nowhere or singular everywhere with no spread, and at a singular point the Fisher spectrum does not give the learning coefficient

## The claim

Take predictions F(θ) observed with Gaussian noise, so the Fisher matrix
is I = JᵀJ/σ² (A39 §1). Two different things can make a direction weak.

- **Sloppiness.** J has full rank, but its singular values spread over
  many decades. The model is regular: the Fisher matrix is invertible, the
  learning coefficient is d/2 ([THEORY-087](../theory.d/THEORY-087.md)), and every direction is
  identified given enough data. The record holds the eigenvalue spread
  for a physics model ([THEORY-774](../theory.d/THEORY-774.md)); the hyperribbon reading of it, a
  hierarchy of widths of the model image ([TERM-135](../terms.d/TERM-135.md)), is in the Transtrum works
  registered from the exchange ([LIT-2977](../literature.d/LIT-2977.md), [LIT-3009](../literature.d/LIT-3009.md)), read on
  2026-11-21 ([THEORY-2156](../theory.d/THEORY-2156.md), [THEORY-2155](../theory.d/THEORY-2155.md); see the note below).
- **Singularity.** J loses rank on a set of parameters, a stratum, where
  some parameter change has no first-order effect on the predictions.
  The Fisher matrix is not invertible there ([THEORY-082](../theory.d/THEORY-082.md)), and the
  learning coefficient can fall below d/2 ([THEORY-087](../theory.d/THEORY-087.md)).

They come apart in both directions. The assistant's checks:

- **Sloppy everywhere, singular nowhere.** Polynomial regression on
  [0, 1], 50 points, is linear in its parameters, so its Fisher matrix is
  constant and never loses rank. Its eigenvalues span ratios of
  1.4 × 10⁴, 1.3 × 10⁷ and 1.2 × 10¹⁰ for 4, 6 and 8 coefficients.
- **Singular everywhere, no spread.** [CASE-152](../cases.d/CASE-152.md)'s Y ∼ N(ab, 1) has a
  Fisher matrix of rank at most 1 at every point: one zero eigenvalue
  everywhere, and an image that is a line, not a ribbon of graded
  widths.

And where they meet, the Fisher spectrum at the point does not decide
the learning coefficient. A39 §3: "At the singularity, the Fisher matrix
tells us that the first-order sensitivity vanishes. It does not reveal
that the remaining dependence is quartic." Losses u² + v⁴ and u² + v⁶
have the same Fisher matrix at the origin, rank 1, and learning
coefficients ½ + ¼ = 3/4 and ½ + ⅙ = 2/3. Resolution of singularities,
or a direct computation of the volume scaling, supplies what the point
spectrum lacks. It does so as a tool for computing the coefficient, not as
a change in what can be observed ([CLAIM-305](CLAIM-305.md)).

A37 §1 adds a third distinction the claim keeps: a singularity of the
parameter-to-prediction map is not a singularity of the image. In
[CASE-302](../cases.d/CASE-302.md) the image p ≤ s²/4 has a smooth edge while the map folds
along a = b. "The network's space of realizable functions is therefore
better understood as a stratified geometric object than as one globally
smooth manifold of fixed dimension" (A37 §1).

A39 §4's table states the division: a hyperribbon "characterizes the
shape of the model in prediction space", while singular learning theory
"characterizes the map from parameters to predictions, together with the
measure over parameters".

## What it does not say

It does not say the two are unrelated. [CASE-302](../cases.d/CASE-302.md) shows a sloppy
eigenvalue that is the shadow of a nearby stratum, and the textbook
sloppy model has such strata at its edges. Where they meet, and how a
learning coefficient measured at finite n confounds them, is
[CLAIM-812](CLAIM-812.md). Whether the connection is a good one is the owner's
[CLAIM-808](CLAIM-808.md).

## Note of 2026-11-21: Transtrum, Machta & Sethna (2010, 2011), read

Read in [NOTE-2240](../notes.d/NOTE-2240.md) and [NOTE-2247](../notes.d/NOTE-2247.md); the THEORYs replace the unread
LITs in the grounds ([ARG-133](../arguments.d/ARG-133.md)).

- **Supports the separating example.** Linear polynomial fitting, with its
  Hilbert-matrix Hessian, is among the 2011 paper's own sloppy examples
  (Fig. 2b), and its manifold is a hyper-ellipse with the Vandermonde
  singular values as axes when the coefficients are confined to a ball.
- **Qualifies the framing.** "Model boundaries correspond to points on the
  manifold where the metric is singular" (2011, p. 10): a bounded sloppy
  manifold's edges are loci of rank loss. Usually at parameters running to
  0 or ∞ ("boundaries typically do not exist (i.e. they lie at parameter
  values equal to ∞)"), sometimes on finite fold lines such as θ₁ = θ₂,
  generic when the data number fewer than twice the parameters. So the
  defeater, "a spread of nonzero Fisher eigenvalues forces rank loss
  somewhere in the parameter space", is pressed but not met: the forced
  singularities lie at infinity, and finite ones occur only in some
  models. The claim's "regular" is a property of the interior.
- **"The textbook sloppy model has such strata at its edges"** is the
  papers': the 2010 letter lists θ₁ = θ₂ among the two-exponential
  manifold's boundaries, and the 2011 paper calls it the "fold line", where
  "No parameters were at extreme values, but the model behavior was
  nonetheless singular".

## Note of 2026-11-21: Transtrum & Qiu (2014) and Amari, Park & Ozeki (2006), read

Two parallels, neither moving the claim.

- **Transtrum and Qiu** ([NOTE-tmphbnqd](../notes.d/NOTE-tmphbnqd.md)): the reduction method starts in a
  sloppy, regular interior and ends at a boundary where "the smallest
  eigenvalue ... approaches zero"; the reduced EGFR model shows "lack of
  small eigenvalues", regular and no longer sloppy. The two properties
  occur at different places on one path, which fits the claim.
- **Amari, Park and Ozeki** ([NOTE-tmptlwkf](../notes.d/NOTE-tmptlwkf.md)): in a perceptron the Fisher
  matrix loses rank on continua at finite parameters, "not isolated but
  form a continuum", which the claim's "rank loss on a stratum" describes;
  near such a set the model is not a sloppy regular interior. A case of
  singular without sloppy, of the kind the claim allows.

## Note of 2026-11-22: Quinn, Abbott, Transtrum, Machta & Sethna (2023), read

Corroborates ([NOTE-tmp3keyy](../notes.d/NOTE-tmp3keyy.md); [THEORY-tmpx26x7](../theory.d/THEORY-tmpx26x7.md) `corroborates` this claim).
The review separates what it studies, "practical identifiability, where
some parameter combinations are almost interchangeable, leading to the
small, sloppy eigenvalues", from structural non-identifiability, which
"would give eigenvalues of the metric exactly equal to zero" (§3). That is
the claim's line between small nonzero eigenvalues and rank loss, drawn by
the programme's authors. It adds, against the claim's "regular" side, that
the model manifold "is not strictly a manifold" and has singular points
inside it, "such as a the tip of a cone" (§4), so a sloppy model's
manifold can carry singular points away from its edges, as CLAIM-813
already allows.
