---
status: Proposed
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
- CASE-tmpb2gly
- LIT-tmpd3swn
- LIT-tmpzkxka
uses:
- TERM-tmp5z2du
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

<!-- inactive-ok-file: TERM-tmp5z2du CASE-tmpb2gly CLAIM-tmpcg4uu CLAIM-tmpa8hb2 LIT-tmpd3swn LIT-tmpzkxka — Proposed or new, or Deferred works not yet read; filed with this claim -->

# CLAIM-tmpcgvcp: Sloppiness and singularity are different properties of a statistical model: sloppiness is a spread of small but nonzero Fisher eigenvalues in a regular model, singularity is rank loss on a stratum of parameter space, so a model can be sloppy everywhere and singular nowhere or singular everywhere with no spread, and at a singular point the Fisher spectrum does not give the learning coefficient

## The claim

Take predictions F(θ) observed with Gaussian noise, so the Fisher matrix
is I = JᵀJ/σ² (A39 §1). Two different things can make a direction weak.

- **Sloppiness.** J has full rank, but its singular values spread over
  many decades. The model is regular: the Fisher matrix is invertible, the
  learning coefficient is d/2 (THEORY-087), and every direction is
  identified given enough data. The record holds the eigenvalue spread
  for a physics model (THEORY-774); the hyperribbon reading of it, a
  hierarchy of widths of the model image (TERM-tmp5z2du), is in the Transtrum works
  registered from the exchange (LIT-tmpd3swn, LIT-tmpzkxka), not yet read.
- **Singularity.** J loses rank on a set of parameters, a stratum, where
  some parameter change has no first-order effect on the predictions.
  The Fisher matrix is not invertible there (THEORY-082), and the
  learning coefficient can fall below d/2 (THEORY-087).

They come apart in both directions. The assistant's checks:

- **Sloppy everywhere, singular nowhere.** Polynomial regression on
  [0, 1], 50 points, is linear in its parameters, so its Fisher matrix is
  constant and never loses rank. Its eigenvalues span ratios of
  1.4 × 10⁴, 1.3 × 10⁷ and 1.2 × 10¹⁰ for 4, 6 and 8 coefficients.
- **Singular everywhere, no spread.** CASE-152's Y ∼ N(ab, 1) has a
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
a change in what can be observed (CLAIM-305).

A37 §1 adds a third distinction the claim keeps: a singularity of the
parameter-to-prediction map is not a singularity of the image. In
CASE-tmpb2gly the image p ≤ s²/4 has a smooth edge while the map folds
along a = b. "The network's space of realizable functions is therefore
better understood as a stratified geometric object than as one globally
smooth manifold of fixed dimension" (A37 §1).

A39 §4's table states the division: a hyperribbon "characterizes the
shape of the model in prediction space", while singular learning theory
"characterizes the map from parameters to predictions, together with the
measure over parameters".

## What it does not say

It does not say the two are unrelated. CASE-tmpb2gly shows a sloppy
eigenvalue that is the shadow of a nearby stratum, and the textbook
sloppy model has such strata at its edges. Where they meet, and how a
learning coefficient measured at finite n confounds them, is
CLAIM-tmpcg4uu. Whether the connection is a good one is the owner's
CLAIM-tmpa8hb2.
