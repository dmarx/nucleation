---
number: 685
status: Active
formerly:
- THEORY-tmpyi9lt
title: "The Mizohata–Takeuchi conjecture fails for every compact C² hypersurface with a point of non-zero curvature: for each large R a function and a weight violate it by a factor of order log R, which refutes Stein's conjecture as stated and closes the Mizohata–Takeuchi route to loss-free endpoint multilinear restriction"
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-030
summary: >-
  Cairo (2025), [LIT-030](../literature.d/LIT-030.md), read in full in [NOTE-051](../notes.d/NOTE-051.md), which checked the
  counting and exponent bookkeeping. The paper states the theorem for any
  C² hypersurface not lying in a hyperplane; the proof needs a curved
  point, which a connected such surface has. The incidence lemma (§4) is
  the step a non-specialist could not verify. The loss is log R, not a
  power, and the counterexample is a family indexed by R. It does not
  refute endpoint multilinear restriction itself. Its proposed local
  replacement has since been refuted with power loss on a dense family of
  surfaces, per the abstract of a later paper.
---

# THEORY-685: The Mizohata–Takeuchi conjecture fails for every compact C² hypersurface with a point of non-zero curvature: for each large R a function and a weight violate it by a factor of order log R, which refutes Stein's conjecture as stated and closes the Mizohata–Takeuchi route to loss-free endpoint multilinear restriction

## Source

Cairo (2025), "A Counterexample to the Mizohata-Takeuchi Conjecture",
arXiv:2502.06137v2, [LIT-030](../literature.d/LIT-030.md), read in full in [NOTE-051](../notes.d/NOTE-051.md).

## What was actually shown

**The conjecture.** Mizohata–Takeuchi (Conj. 1.1) says ∫|Ef|²w ≲ ‖f‖²₂ ·
sup_ℓ ∫_ℓ w for every non-negative weight w, where E is the extension
operator of a hypersurface Σ and the sup is over lines. It had been proved
for radial weights and with power losses (R^{(n−1)/(n+1)+ε} in general,
Carbery–Iliopoulou–Wang).

**The counterexample (Thm 1.2 via Prop. 3.1).** For each R ≥ 1 there are
f ∈ L²(Σ) and h with supp ĥ ⊂ B_{CR} such that ‖h * f dσ‖²₂ ≳ log R ·
‖f‖²₂ · ‖P_νh‖²_{L²(L¹)} for every direction ν. With w = |ĥ|² and the X-ray
estimate of Theorem 2.1, this violates the conjecture by a factor of order
log R. The construction takes N ≍ log R points on Σ, places R⁻¹-balls on the
middle-layer subset sums Q of those points, and chooses the points so that
no hyperplane meets more than 2^{d−1} of the balls (Lemma 3.5). The ratio of
the two sides is then N. [NOTE-051](../notes.d/NOTE-051.md) checked this bookkeeping by hand.

**Consequences.** Stein's conjecture (Conj. 1.4) implies Mizohata–Takeuchi
in one line (p. 2), so it fails too (C4). Carbery, Hänninen and
Valdimarsson had shown that Mizohata–Takeuchi plus endpoint multilinear
Kakeya gives endpoint multilinear restriction with no R^ε loss; that route
is now closed (C5).

**Why curvature.** It lets the projections of the chosen points lie in
separated dyadic scales in every direction at once. A flat piece projects
to a point in its normal direction.

**What could have come out otherwise.** Some hyperplane could have met many
of the balls around Q, which would have cancelled the gain. Lemma 3.5 says
none does.

## What this does not say

- **That the theorem holds for every surface not in a hyperplane.** The
  paper states it so, but the proof (Lemma 4.4) needs a point where the
  second fundamental form is non-zero. A connected surface not in a
  hyperplane has one. A compact union of flat pieces in different
  hyperplanes does not, and for it the conjecture holds with constant equal
  to the number of pieces ([NOTE-051](../notes.d/NOTE-051.md)'s argument, C6).
- **That the loss is a power.** This paper gives log R. Cairo and Zhang
  (arXiv:2512.08064, read as an abstract only) give power-loss
  counterexamples to the local version on a C^k-dense family of
  hypersurfaces. Whether the sphere and paraboloid have a power loss was not
  checked.
- **That a single (f, w) violates the inequality by an infinite factor.**
  The counterexample is a family indexed by R.
- **That endpoint multilinear restriction is false.** The paper says only
  that it cannot be sharpened directly through Mizohata–Takeuchi.
- **That every step is checked.** Lemma 4.3's induction tracks its
  constants only up to ∼, and the overlap bound (3.8) is argued as a
  probability ([NOTE-051](../notes.d/NOTE-051.md), C3 and Method). The paper had no journal version
  when read.

## Connections

- No other work or THEORY in the record bears on Fourier restriction.
