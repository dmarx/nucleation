---
status: Proposed
title: 'The integral operator with kernel w(u,v)/√(w(u)w(v)) to which the spectral contrastive analysis applies the spectral theorem is the conditional-expectation operator of the positive pairs carried to Lebesgue measure by multiplication by √w, so that kernel is square-integrable exactly when the positive-pair χ²-divergence is finite, with squared norm 1 + χ², and the two operators have one spectrum'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation below: a symmetric positive-pair density
  w(u,v) with marginal w(u) for which conjugating the conditional-expectation
  operator by multiplication by √w does not give the integral operator with
  kernel w(u,v)/√(w(u)w(v)) on L² of the support of w, or for which
  ∫∫ w(u,v)²/(w(u)w(v)) du dv differs from 1 + χ²(P⁺‖p⊗p). Not defeated by
  pair distributions without a density, which the claim does not cover.
tags:
- mathematics
- representation-learning
- information-theory
date: '2026-11-11'
line:
- formal-apparatus
- learned-structure
rests_on:
- CLAIM-291
- CLAIM-370
grounds:
- LIT-249
summary: >-
  [CLAIM-291](CLAIM-291.md) shows that a square-integrable kernel operator is self-adjoint
  exactly when its kernel is conjugate-symmetric, and names the use
  [THEORY-009](../theory.d/THEORY-009.md) makes of it: HaoChen et al. apply the spectral theorem to the
  kernel w(u,v)/√(w(u)w(v)) on L²(ℝᵈ). [CLAIM-370](CLAIM-370.md) shows that the
  conditional-expectation operator of the positive pairs on L²(p) has
  kernel K⁺ and is Hilbert–Schmidt exactly when χ² is finite. Neither says
  that these are one operator. They are: multiplication by √w is a unitary
  from L²(p) onto L² of the support of w that carries the one to the other,
  so the square-integrability [CLAIM-291](CLAIM-291.md) assumes for HaoChen's kernel is
  exactly [CLAIM-370](CLAIM-370.md)'s finite χ², the two self-adjointness arguments are one
  fact, and the eigenvalues coincide. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-005 — Proposed; the reading CLAIM-370 was split from, named, not leaned on -->
<!-- inactive-ok-file: ADR-075 ADR-084 SYNTHESIS-030 — Proposed; cited with its standing -->
<!-- inactive-ok-file: NOTE-227 — Superseded; cited with its standing -->

# CLAIM-tmpz1gnk: The integral operator with kernel w(u,v)/√(w(u)w(v)) to which the spectral contrastive analysis applies the spectral theorem is the conditional-expectation operator of the positive pairs carried to Lebesgue measure by multiplication by √w, so that kernel is square-integrable exactly when the positive-pair χ²-divergence is finite, with squared norm 1 + χ², and the two operators have one spectrum

## The claim

Let positive pairs (A, A′) on ℝᵈ have a joint density w(u,v) = w(v,u)
with respect to Lebesgue measure, and marginal density w(u) = ∫ w(u,v) dv.
Let S = {u : w(u) > 0}, p the law with density w, and
K⁺(u,v) = w(u,v)/(w(u)w(v)) on S × S.

1. **One operator.** The map U : L²(p) → L²(S, du), (Uf)(u) = √w(u) f(u),
   is unitary, and U T U⁻¹ is the integral operator with kernel
   k(u,v) = w(u,v)/√(w(u)w(v)), where T is [CLAIM-370](CLAIM-370.md)'s
   conditional-expectation operator, (Tf)(u) = E[f(A′) | A = u].
2. **One condition.** k ∈ L²(S × S, du dv) exactly when χ²(P⁺‖p⊗p) < ∞,
   and then ∫∫ k² du dv = 1 + χ²(P⁺‖p⊗p).
3. **One spectrum.** T and the operator with kernel k have the same
   eigenvalues with the same multiplicities, and f is an eigenfunction of T
   exactly when √w·f is one of the other. The self-adjointness [CLAIM-291](CLAIM-291.md)
   gives the kernel operator from k(u,v) = k(v,u) and the self-adjointness
   [CLAIM-370](CLAIM-370.md) gives T from the symmetry of P⁺ are the same fact.

## Proof

P⁺ ≪ p⊗p: where w(u) = 0, w(u,v) = 0 for almost every v, since
w(u) = ∫ w(u,v) dv. So K⁺ is the density [CLAIM-370](CLAIM-370.md) uses.

(1) ‖Uf‖² = ∫_S w f² du = ‖f‖²_{L²(p)}, and U⁻¹g = g/√w is defined on all
of L²(S, du), so U is unitary. For g ∈ L²(S, du),

  (U T U⁻¹ g)(u) = √w(u) ∫ K⁺(u,v) (g(v)/√w(v)) w(v) dv
               = ∫ w(u,v)/√(w(u)w(v)) g(v) dv.

(2) ∫∫ k² du dv = ∫∫ (w(u,v)/(w(u)w(v)))² w(u)w(v) du dv
= ∫∫ K⁺² d(p⊗p) = 1 + χ²(P⁺‖p⊗p), the last step [CLAIM-370](CLAIM-370.md)'s (2).

(3) Unitary equivalence keeps the spectrum, multiplicities and
self-adjointness.

**A check.** On finite spaces with counting measure in place of Lebesgue,
for random symmetric joint laws on 3, 5 and 8 points (numpy, seed 0):
the matrix diag(√p) T diag(1/√p) equals [w(u,v)/√(w(u)w(v))], the squared
Frobenius norm equals 1 + χ², and the sorted eigenvalues agree.

## Admission

The route is a derivation ([ADR-075](../decisions.d/ADR-075.md), step 5, as amended by [ADR-084](../decisions.d/ADR-084.md)).

- **Not held.** [CLAIM-291](CLAIM-291.md)'s "Where it is used" applies its step 4 to
  "a square-integrable kernel k(u,v) = w(u,v)/√(w(u)w(v))" and does not say
  when that kernel is square-integrable. [CLAIM-370](CLAIM-370.md) says HaoChen et al.
  "get the Hilbert–Schmidt property from K⁺ ≤ B, which is sufficient and
  strictly stronger", comparing their assumption with its condition
  without writing their operator as its T. [THEORY-719](../theory.d/THEORY-719.md) says the spectral
  loss "needs K⁺ ∈ L²(p⊗p), which is finite χ²", a statement on L²(p⊗p),
  not about HaoChen's kernel on Lebesgue measure. [NOTE-227](../notes.d/NOTE-227.md) records that
  under Assumption F.1 "this kernel is square-integrable". No entry states
  the unitary equivalence or the exact condition for k.
- **Nontrivial.** It joins two demonstrated claims that sit in different
  lines' accounts ([CLAIM-291](CLAIM-291.md) in learned-structure's [SYNTHESIS-030](../syntheses.d/SYNTHESIS-030.md);
  [CLAIM-370](CLAIM-370.md) in none) and turns a sufficient assumption the record reads in
  HaoChen et al. into an exact one.
- **Free parameters.** None: the measure (Lebesgue, or any reference
  measure w is a density for), the support and the unitary are fixed.
- **A realistic case.** Two views of a continuous input that are nearly
  deterministic functions of each other: χ² is infinite, so by (2)
  HaoChen's kernel is not square-integrable and [CLAIM-291](CLAIM-291.md)'s hypothesis
  fails. This is [CLAIM-370](CLAIM-370.md)'s own "What it does not say" case, and it is
  consistent with the claim; it does not meet the defeat condition.

## What it does not say

- That HaoChen et al.'s theorems hold under finite χ² alone. Their
  extension to infinite spaces is asserted, not written out ([NOTE-740](../notes.d/NOTE-740.md)), and
  [THEORY-005](../theory.d/THEORY-005.md) keeps that.
- Anything for pair laws without a density, or for asymmetric pairs, where
  k is not symmetric and only the composition with the adjoint is
  self-adjoint ([THEORY-009](../theory.d/THEORY-009.md)).
- What trained features span.
