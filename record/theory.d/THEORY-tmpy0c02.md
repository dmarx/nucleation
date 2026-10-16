---
status: Active
title: "Dewar's information-theoretic derivation of maximum entropy production does not reach the far-from-equilibrium regime where the principle is applied: the 2003 route needs a mean-field step and an unargued assumption about path counts, the 2005 route's orthogonality condition, which yields both maximum and minimum dissipation, holds only with linear constitutive relations, and the 2003 self-organized-criticality corollary is an artefact of a quadratic expansion"
version: 1
tags:
- thermodynamics
- information-theory
date: '2026-10-16'
source:
- LIT-525
- LIT-521
summary: >-
  Grinstein & Linsker (2007), [LIT-525](../literature.d/LIT-525.md), read in [NOTE-422](../notes.d/NOTE-422.md), against Dewar
  (2003), [LIT-521](../literature.d/LIT-521.md), read in [NOTE-426](../notes.d/NOTE-426.md). The self-organized-criticality point
  was checked against Dewar 2003 and is correct. The linearity point
  concerns Dewar 2005, which the record could not read; it is held on the
  Comment's account of its equations and on an exactly solvable spin
  chain, re-derived. The Comment removes one derivation and one
  application. It does not say MEP is false, and it says the existence of
  far-from-equilibrium extremal principles "has not been settled".
---

<!-- inactive-ok-file: THEORY-tmpxjvy1 — Proposed; named as the account whose derivation this finding examines, not leaned on -->

# THEORY-tmpy0c02: Dewar's information-theoretic derivation of maximum entropy production does not reach the far-from-equilibrium regime where the principle is applied: the 2003 route needs a mean-field step and an unargued assumption about path counts, the 2005 route's orthogonality condition, which yields both maximum and minimum dissipation, holds only with linear constitutive relations, and the 2003 self-organized-criticality corollary is an artefact of a quadratic expansion

## Source

Grinstein & Linsker (2007), *J. Phys. A: Math. Theor.* 40:9717–9720,
[LIT-525](../literature.d/LIT-525.md), read in full in [NOTE-422](../notes.d/NOTE-422.md) from the authors' submitted manuscript
(the published Comment was not seen). Dewar (2003), [LIT-521](../literature.d/LIT-521.md), read in full
in [NOTE-426](../notes.d/NOTE-426.md). Dewar's 2005 letter (*J. Phys. A* 38:L371), the target of the
Comment's first point, could not be read and is not filed.

## What was actually shown

**The 2003 route ([LIT-521](../literature.d/LIT-521.md), §4.2).** Maximum path entropy gives maximum mean
entropy production only within a mean-field approximation that ignores
fluctuations of the action (Eq. 23), and only if the number of paths with
irreversible action A^irr increases with A^irr (p. 14). The second is
assumed with no argument or model where it can be checked ([NOTE-426](../notes.d/NOTE-426.md)).

**The 2005 route ([LIT-525](../literature.d/LIT-525.md), §1).** A fluctuation theorem compares p(f) with
p(−f). A Gaussian approximation around the mean flux F describes p(f) only
near F. Both can hold at once only when f and −f are near F, so F near zero.
Dewar's Eq. 15, λ_k = Σ_j A_jk(F) F_j, needs his quadratic Eq. 14 for all
f. Differentiating gives ∂A_jk/∂F_n = 0 (Eq. 2): A is independent of F,
which is linearity, "contrary to Dewar's claim". The correct gradient of
the mean dissipation is ∂D/∂F_n = 2λ_n + 2Σ_k A_nk(F) F_k (Eq. 3,
re-derived in [NOTE-422](../notes.d/NOTE-422.md)). Dewar's orthogonality condition, ∂D/∂F_n = 4λ_n,
holds only when Σ_k A_nk F_k = λ_n, in particular when A is constant.

**Both principles fall together.** Dewar uses the orthogonality condition
to derive "maximum dissipation" and "minimum dissipation". Both
derivations therefore "do require 'the usual near-equilibrium assumption
of linear constitutive relations'" (p. 3), the inner phrase being Dewar's
own for what he claimed to avoid.

**The spin chain (§1.1).** Paths are τ spins of ±1/τ. Exactly, F =
tanh(λ/τ), λ(F) = τ artanh F and A(F) = τ/(1 − F²). The fluctuation
theorem holds exactly, and the quadratic expansion matches Dewar's Eq. 14
near F. But his Eq. 15 would need τ artanh F = τF/(1 − F²), which holds
only as F → 0. [NOTE-422](../notes.d/NOTE-422.md) checked each step.

**Self-organized criticality (§2).** In Dewar 2003 the variance of the
output flux, ⟨(F − ⟨F⟩)²⟩ ≈ 1/(8|g|F_ext²) (Eq. 28), diverges as the
drive F_ext → 0. It comes from expanding H = rF² + gF⁴ to quadratic order
about ⟨F⟩ and using that form for all F. The quadratic coefficient
vanishes like |g|F_ext². Keeping the quartic term gives ⟨F²⟩ ∝ 1/√|g|,
finite at F_ext = 0. [NOTE-422](../notes.d/NOTE-422.md) checked this against Dewar 2003, Eqs. 26–28.

**What could have come out otherwise.** In the spin chain the exact
λ(F) could have satisfied Dewar's Eq. 15 at large F. It does not. With the
quartic term kept, the variance could still have diverged. It does not.

## What this does not say

- **That MEP is false.** The Comment removes one derivation and one
  application, and offers no counterexample to MEP as an empirical
  principle. It says "the question of the existence of possible extremal
  principles … that might apply to far-from-equilibrium regimes … has not
  been settled".
- **That MEP and self-organized criticality are unrelated.** It calls the
  link "an intuitively appealing notion". Whether a MaxEP model shows
  self-organized criticality is set by the assumed large-F tail of p(F),
  of which "no conclusion … can be drawn" in the model as given (p. 5).
- **That Dewar 2005 was checked here.** The Comment's account of that
  letter's equations is taken as given. The failure is shown on one scalar
  model.
- **That the minimum principle is false.** Only that, derived through the
  orthogonality condition, it needs linear constitutive relations. That is
  consistent with treating it as a near-equilibrium result.
- **That Dewar's fluctuation theorem is wrong.** It is exact given his
  inferred path measure. What it does not show is that real path
  statistics follow that measure ([NOTE-426](../notes.d/NOTE-426.md)).

## Connections

- **The account it bears on** is maximum entropy production
  ([THEORY-tmpxjvy1](THEORY-tmpxjvy1.md)). This finding is why that account cannot be promoted
  on the strength of its derivation. Kleidon's review ([LIT-519](../literature.d/LIT-519.md)) cites the
  Comment only for its point about self-organized criticality ([NOTE-423](../notes.d/NOTE-423.md)).
- **Prigogine.** The minimum principle's own statement restricts it to the
  strictly linear regime ([LIT-516](../literature.d/LIT-516.md)), which is where this finding leaves
  Dewar's derivation of both principles.
- **The dynamical fluctuation theorems ([THEORY-tmp3uu1d](THEORY-tmp3uu1d.md))** do not depend on
  any of this. They are derived from microscopic reversibility, not from
  maximum-entropy inference.
