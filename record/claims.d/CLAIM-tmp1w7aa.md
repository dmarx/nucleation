---
status: Active
title: "For any classes with weights π_c and per-class factor matrices H_c and Δ_c, the class-wise Kronecker product Σ_c π_c H_c ⊗ Δ_c exceeds the product of the weighted averages H̄ ⊗ Δ̄ by exactly the weighted between-class covariance Σ_c π_c (H_c − H̄) ⊗ (Δ_c − Δ̄), so the two agree when either factor is the same in every class"
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Filed from THEORY-085 under ADR-032 (promotion audit, batches 047 and
    057). THEORY-085's summary says "the filer adds a line of algebra":
    the identity relating Papyan's class-wise CFAC to K-FAC is the
    record's own, stated by neither LIT-613 nor LIT-622. A result the
    record itself proves belongs in a CLAIM, as THEORY-005's became
    CLAIM-370, THEORY-080's CLAIM-384 and THEORY-019's CLAIM-385. The
    proof below is three lines of bilinearity, so the claim is filed
    Active, demonstrated. THEORY-085 keeps the mechanism (class gradient
    means approximately h_c ⊗ δ_c, inferred from spectra judged by eye)
    and stays Proposed.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below: weights π_c ≥ 0 summing to one and matrices
  H_c, Δ_c for which Σ_c π_c H_c ⊗ Δ_c − H̄ ⊗ Δ̄ differs from
  Σ_c π_c (H_c − H̄) ⊗ (Δ_c − Δ̄), with H̄ = Σ_c π_c H_c and
  Δ̄ = Σ_c π_c Δ_c; or a case where one factor is the same in every class
  and the two products differ.
tags:
- information-geometry
- mathematics
- learning-theory
- anthology-candidate
date: '2026-10-20'
line:
- formal-apparatus
grounds:
- LIT-613
- LIT-622
---
<!-- inactive-ok-file: THEORY-085 THEORY-078 THEORY-005 — Proposed; the account this was filed from, which keeps the mechanism, the account it extends, and the precedent named in the history; none is leaned on -->

# CLAIM-tmp1w7aa: For any classes with weights π_c and per-class factor matrices H_c and Δ_c, the class-wise Kronecker product Σ_c π_c H_c ⊗ Δ_c exceeds the product of the weighted averages H̄ ⊗ Δ̄ by exactly the weighted between-class covariance Σ_c π_c (H_c − H̄) ⊗ (Δ_c − Δ̄), so the two agree when either factor is the same in every class

## The claim

Let classes c = 1, …, C carry weights π_c ≥ 0 with Σ_c π_c = 1, and let
H_c (m × m) and Δ_c (p × p) be any matrices, one pair per class. Write
H̄ = Σ_c π_c H_c and Δ̄ = Σ_c π_c Δ_c. Then

Σ_c π_c H_c ⊗ Δ_c − H̄ ⊗ Δ̄ = Σ_c π_c (H_c − H̄) ⊗ (Δ_c − Δ̄).

In Papyan's notation for a classifier's layer
([LIT-613](../literature.d/LIT-613.md), Definitions 7.1–7.2), H_c and Δ_c are the class-c second
moments of the layer's input features and of its backpropagated errors,
π_c is the class frequency, the left-hand product is the class-wise
approximation CFAC and H̄ ⊗ Δ̄ is K-FAC's factorisation of the layer
Fisher ([LIT-622](../literature.d/LIT-622.md), Eq. 1–3). K-FAC's factors are averages over all
examples, so they are the π-weighted averages of the class moments, and
the identity reads CFAC − K-FAC = the weighted between-class covariance of
the two factors in the Kronecker sense. With balanced classes π_c = 1/C
and the weights become Papyan's "Ave_c".

## Proof

The Kronecker product is bilinear. Expanding the right-hand side,

Σ_c π_c (H_c − H̄) ⊗ (Δ_c − Δ̄)
= Σ_c π_c H_c ⊗ Δ_c − (Σ_c π_c H_c) ⊗ Δ̄ − H̄ ⊗ (Σ_c π_c Δ_c) + (Σ_c π_c) H̄ ⊗ Δ̄
= Σ_c π_c H_c ⊗ Δ_c − H̄ ⊗ Δ̄ − H̄ ⊗ Δ̄ + H̄ ⊗ Δ̄
= Σ_c π_c H_c ⊗ Δ_c − H̄ ⊗ Δ̄,

using Σ_c π_c = 1 in the last term. ∎

**Corollary.** If H_c = H̄ for every class (or Δ_c = Δ̄ for every class),
every term on the right vanishes and CFAC = K-FAC. Equivalently,
H̄ ⊗ Δ̄ = Σ_{c,c′} π_c π_{c′} H_c ⊗ Δ_{c′} contains all C² pairings of one
class's features with another's errors, CFAC contains only the C matched
pairings, and the identity says the cross pairings differ from the matched
ones by the covariance term alone.

**A check.** For C = 4 classes with Dirichlet weights and random positive
semidefinite 3 × 3 and 2 × 2 factors (numpy, seed 0), the two sides agree
to 6 × 10⁻¹⁵, and the difference CFAC − K-FAC has eigenvalues of both
signs (−5.26 and 5.51 at the extremes). So the covariance term is not in
general positive semidefinite: CFAC is not K-FAC plus a correction that
only adds curvature.

## What this does not say

- **Not that K-FAC misplaces a classifier's Fisher outliers.** That is
  [THEORY-085](../theory.d/THEORY-085.md)'s mechanism, which rests on Papyan's spectra judged by
  eye on one MLP and stays Proposed. The identity holds for any matrices
  and says nothing about which approximation is closer to the true layer
  Fisher.
- **Not a necessary condition.** Either factor being class-constant is
  sufficient for CFAC = K-FAC. The covariance term can also vanish in other
  ways, for example when the class deviations cancel in the weighted sum;
  the claim does not characterise when it does.
- **Not about the true Fisher.** Both sides are approximations. The true
  layer block is a weighted sum of Kronecker products over examples, not
  classes ([LIT-613](../literature.d/LIT-613.md), Eq. 7.5), and its distance from either side is not
  addressed here.
