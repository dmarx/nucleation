---
number: 732
status: Active
formerly:
- THEORY-tmpyjtkq
title: "For ReLU networks interpolated linearly between two endpoints, weak additivity and commutativity at every layer make each layer's features exactly the interpolation of the endpoints' features, output-layer linearity bounds the path's error by twice the endpoints', and for one hidden layer with interpolating minima linear mode connectivity alone gives the exact case"
version: 1
history:
- version: 1
  date: '2026-10-19'
  note: >-
    Split from THEORY-111 and filed Active at the owner's direction,
    carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-111.yaml, batch 016, ADR-047).
    THEORY-111's promote_when concerns its empirical regularity outside
    image classification and the step to many-model averages. The formal
    results held here were read with their proofs checked: LIT-674's
    Theorem 1 and Lemma 1 in NOTE-512, and LIT-669's Lemma 2 in NOTE-538.
    The one-line composition that gives the exact one-hidden-layer case is
    the record's, and is re-derived step by step under ADR-047 v2 (the
    owner's rule of 2026-10-19). THEORY-111 keeps the empirical regularity
    and the averaging clause, and extends this one.
tags:
- loss-landscapes
- representation-learning
date: '2026-10-19'
source:
- LIT-674
- LIT-669
summary: >-
  Zhou et al. (2023), [LIT-674](../literature.d/LIT-674.md), read in [NOTE-512](../notes.d/NOTE-512.md) with Appendix A's proofs
  checked: for an L-layer ReLU MLP on a finite dataset, weak additivity of
  ReLU over the two networks' pre-activations and the commutativity
  W_A H_B + W_B H_A = W_A H_A + W_B H_B at every layer make the interpolated
  network's features at every layer exactly the interpolation of the
  endpoints' features (Theorem 1). Output-layer linearity, at any positive
  scale, keeps the path's error within twice the endpoints' (Lemma 1).
  Lubana et al. (2022), [LIT-669](../literature.d/LIT-669.md), Lemma 2: for one hidden layer and
  interpolating minima, linear mode connectivity forces shared activation
  patterns, and with shared patterns the hidden features are linear along
  the path. It says nothing about when the conditions hold. That trained
  pairs satisfy them is [THEORY-111](THEORY-111.md)'s empirical claim.
extended_by:
- THEORY-111
---
<!-- inactive-ok-file: THEORY-111 — Proposed; the empirical account this was split from and that extends it, cited as open -->
<!-- inactive-ok-file: THEORY-116 — Proposed; named in Connections, nothing here rests on it -->

# THEORY-732: For ReLU networks interpolated linearly between two endpoints, weak additivity and commutativity at every layer make each layer's features exactly the interpolation of the endpoints' features, output-layer linearity bounds the path's error by twice the endpoints', and for one hidden layer with interpolating minima linear mode connectivity alone gives the exact case

## Source

- Zhou, Yang, Yang, Yan & Hu (2023), "Going Beyond Linear Mode
  Connectivity: The Layerwise Linear Feature Connectivity", [LIT-674](../literature.d/LIT-674.md), read
  in [NOTE-512](../notes.d/NOTE-512.md): Definitions 2–3, Lemma 1 and Theorem 1, with Appendix A's
  proofs checked line by line.
- Lubana, Bigelow, Dick, Krueger & Tanaka (2022), "Mechanistic Mode
  Connectivity", [LIT-669](../literature.d/LIT-669.md), read in [NOTE-538](../notes.d/NOTE-538.md): Lemma 2 and Definition 6 of
  Appendix F.3, with the proof read in full.

## What was actually shown

Write θ_α = αθ_A + (1 − α)θ_B for the linear path between two networks,
H_ℓ(θ) for layer ℓ's features on a finite dataset, with H_0 = X shared, and
Z_ℓ = W_ℓ H_{ℓ−1} for the pre-activations, biases folded into W. Layerwise
linear feature connectivity (Definition 2) is
c·H_ℓ(θ_α) = αH_ℓ(θ_A) + (1 − α)H_ℓ(θ_B) for some c > 0.

- **The conditions give it exactly (Theorem 1).** Suppose that at every
  layer weak additivity holds, ReLU(αZ_A + (1 − α)Z_B) = αReLU(Z_A) +
  (1 − α)ReLU(Z_B), and so does commutativity, W_A H_B + W_B H_A =
  W_A H_A + W_B H_B. Induct on ℓ. If H_{ℓ−1}(θ_α) = αH_A + (1 − α)H_B, then
  Z_ℓ(θ_α) = α²W_AH_A + (1 − α)²W_BH_B + α(1 − α)(W_AH_B + W_BH_A). By
  commutativity the cross term equals α(1 − α)(W_AH_A + W_BH_B), so
  Z_ℓ(θ_α) = αZ_A + (1 − α)Z_B. Weak additivity then gives
  H_ℓ(θ_α) = αH_A + (1 − α)H_B, with c = 1.
- **Output linearity bounds the path's error (Lemma 1).** If the output
  is linearly connected at any scale c > 0, each prediction on the path is
  the argmax of a convex combination of the endpoints' outputs. Where both
  endpoints rank the label first, so does every convex combination. So the
  path errs only where an endpoint errs, and if each endpoint errs on at
  most a fraction ε of the data, the path errs on at most 2ε. The layerwise
  property is therefore stronger than linear mode connectivity.
- **One hidden layer, exactly (Lemma 2, and the record's composition).**
  For f(x; W) = (1/N)1ᵀReLU(Wᵀx) with interpolating minimizers W_α and W_β
  that are linearly mode connected on the data, Lemma 2 gives
  ϕ′(W_αᵀx) = ϕ′(W_βᵀx) for every x in the data: each hidden unit is on in
  both endpoints or off in both. A pre-activation is linear in the
  weights. So a unit positive at both endpoints is positive at every point
  between them, and one non-positive at both is non-positive throughout.
  The pattern m(x) is therefore constant along the path, and
  ϕ(W_tᵀx) = m(x) ⊙ W_tᵀx = (1 − t)ϕ(W_αᵀx) + tϕ(W_βᵀx). Here the
  layerwise claim is a theorem, with no approximation. This composition is
  the record's, not a statement of either paper.

What could have failed is the algebra, and it does not fail. Each
condition is needed at every layer and for every α used. Drop
commutativity and the cross term does not collapse. Drop weak additivity
and ReLU does not pass through the convex combination.

## What this does not say

- **That trained networks satisfy the conditions.** Zhou et al. measure
  weak additivity and commutativity to hold approximately, and better for
  connected pairs than for independent ones. That measurement, and the
  regularity that connected image classifiers are layerwise connected in
  nearly every layer, is [THEORY-111](THEORY-111.md)'s, Proposed.
- **An approximate version.** Nothing bounds the feature error by the size
  of the residuals in the two conditions. Measured scales c ≠ 1 are
  attributed to such residuals without a theorem.
- **Anything about averages of many models.** Every statement here is
  about the segment between two endpoints. Soups and SWA are outside it.
- **Lemma 2 beyond one hidden layer.** The shared-pattern result is proved
  for f(x; W) = (1/N)1ᵀReLU(Wᵀx) with interpolating minimizers. It is not
  claimed for deeper networks or for non-interpolating minima.

## Connections

- **[THEORY-111](THEORY-111.md)** extends this. Its empirical claim is that pairs found
  linearly connected in practice satisfy these conditions closely enough
  for the conclusion to hold approximately, layer by layer.
- **[THEORY-116](THEORY-116.md)**'s converse half rests on Lemma 2's shared activation
  patterns. The one-hidden-layer case here is that lemma carried from which
  units are on to what the features are.
