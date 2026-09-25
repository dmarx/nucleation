---
status: Skimmed
paper: LIT-tmpx0pnd
title: 'Filip, Notes on the Multiplicative Ergodic Theorem'
version: 1
date: '2026-09-25'
summary: >-
  The Oseledets theorem (Lyapunov exponents and nested Lyapunov subspaces for products of matrices sampled along an ergodic system) is a noncommutative law of large numbers. It can be proved geometrically without Kingman's subadditive theorem, recast as geodesic tracking in symmetric spaces (Kaimanovich), and generalised to isometries of proper metric spaces via horofunctions (Karlsson–Ledrappier) and to mean versions in CAT(0) spaces.
---

<!-- inactive-ok-file: LIT-tmpx0pnd — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpv1zta: Filip, Notes on the Multiplicative Ergodic Theorem

## Contribution

The Oseledets multiplicative ergodic theorem is a basic result with many uses across dynamical systems. These notes introduce it and its later generalizations. They grew out of summer-school lectures in Brazil, France and Russia.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1: the random product C_n = ABAAB… of coin-flip-chosen matrices is the motivating example. The ordinary LLN gives the frequencies, and the noncommutative version gives Lyapunov exponents λ₁ ≥ … ≥ λ_d, with vectors in V^{≤λ_i} expanded by about e^{λ_i n}. The history runs through Furstenberg–Kesten, Oseledets, Pesin theory, Ledrappier–Young, Ruelle (Hilbert spaces), Karlsson–Margulis, Karlsson–Ledrappier and Gouëzel–Karlsson (semi-contractions).
- §1, applications to rigidity: Lyapunov flags give a boundary map in Margulis superrigidity (Zimmer's viewpoint). §5 reverses Monod's approach to get a mean ergodic theorem.
- §2: the classical theorem, with a proof "based on some geometric arguments" that avoids Kingman.
- §3: Kaimanovich's geometric form. Matrices act as isometries of symmetric spaces (Lie structure theory, §3.2–3.3), and the theorem says orbits track a geodesic (§3.5).
- §4: the general noncommutative ergodic theorem for proper metric spaces, where a horofunction detects linear divergence (Karlsson–Ledrappier, Theorem 4.3.1). Busemann functions are computed for SL_n(ℝ)/SO_n(ℝ) (§4.2.5), with an example in §4.5. §5 covers CAT(0) spaces, direct integrals of CAT(0) spaces, and mean MET and mean Kingman theorems.

## Open questions

- Lyapunov exponents of random matrix products underlie ML analyses of signal propagation in deep networks and of RNN/Jacobian-product stability, so this could serve as a rigorous background source. The anthology connection is indirect and would need a specific theory note to cite it.
- A deeper reading should focus on §2's Kingman-free proof and the Busemann-function examples if a note needs the statement at that level of generality.
