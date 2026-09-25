---
number: 51
status: Skimmed
formerly:
- NOTE-tmpek3wm
paper: LIT-030
title: 'Cairo, counterexample to the Mizohata-Takeuchi conjecture'
version: 1
date: '2026-09-25'
summary: >-
  For every C² hypersurface in ℝ^d that is not contained in a hyperplane, there are f and a nonnegative weight w such that ∫_{B_R}|Ef|²w ≳ log R·‖f‖²·sup_ℓ∫_ℓ w. So the Mizohata–Takeuchi conjecture fails (with log R loss), Stein's conjecture as stated fails, and the Mizohata–Takeuchi route to loss-free endpoint multilinear restriction is closed.
---

<!-- inactive-ok-file: LIT-030 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-051: Cairo, counterexample to the Mizohata-Takeuchi conjecture

## Contribution

The paper proves a family of L^p estimates for the X-ray transform of positive measures in ℝ^d. It uses them to build a counterexample to the Mizohata–Takeuchi conjecture, with a log R loss, for every C² hypersurface that does not lie in a hyperplane. One consequence is that the endpoint multilinear restriction estimates cannot be sharpened directly via Mizohata–Takeuchi.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Conjecture 1.1 and Theorem 1.2: the conjecture bounds the weighted extension ∫|Ef|²w by ‖f‖²_{L²}‖Xw‖_∞ (X is the X-ray transform). The counterexample gives a log R lower-order violation on B_R(0) for any non-planar Σ.
- §1.1–1.4 give the stakes. Carbery–Hänninen–Valdimarsson showed that Mizohata–Takeuchi would give endpoint multilinear restriction without R^ε loss, and that route is now closed. Stein's conjecture (Conj. 1.4) implies Mizohata–Takeuchi, so it is false as stated. Stein's conjecture with Kakeya would give restriction, but only "up to a logarithmic factor", so a local version could still work. The historical origin is L²-well-posedness of first-order perturbations of Schrödinger (Takeuchi, corrected by Mizohata).
- §1.6 surveys prior progress: the radial case (Barceló–Ruiz–Vega), R^{1/4+ε} loss for the 3D cone (Ortiz), R^{(n−1)/(n+1)+ε} loss in general (Carbery–Iliopoulou–Wang), and Guth's talk showing decoupling axioms alone cannot beat that loss.
- §1.7 proposes a plausible replacement, a "Local Mizohata–Takeuchi" conjecture with R^ε loss (Conj. 1.5). It is open whether that holds or whether an R^{(n−1)/(n+1)}-loss counterexample exists.
- §3 construction: a lattice Q of subset-sums of N points ξ_i with |Q| ~ N^{−1/2}2^N, and a weight h made of R^{−1}-balls on Q. It uses heuristic "white lies" (the locally-constant principle), which are made rigorous later. The incidence-geometry lemma is proved in §4.

## Open questions

- It is pure harmonic analysis with no direct ML connection. It matters for the reading list only as a notable result: a decades-old conjecture refuted by a short argument.
- Check the status of the local conjecture (Conj. 1.5) and whether a journal version or follow-ups have strengthened the loss beyond log R.
