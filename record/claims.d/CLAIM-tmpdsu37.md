---
status: Proposed
title: 'In the compressed diffusion-wavelet chain, where each level''s operator is the orthogonal compression of the square of the one before onto the columns kept, the distance between the subspace kept at a level and an invariant subspace of the same dimension is at most the accumulated truncation residual divided by the smallest singular value of the dyadic power on that subspace, so a level is definite when its kept spectrum stands well above the residual and not at a gapless threshold'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the proof below; or a run of the chain A_{i+1} =
  P_{i+1}A_i²P_{i+1}, from any T with ‖T‖₂ ≤ 1 and any orthogonal
  projectors P_{i+1}, in which ‖P_{j+1} − Π‖ exceeds (d_j + f_j)/σ_min(R^{2^j})
  for a T-invariant subspace of dimension rank P_{j+1}, or f_j exceeds the
  accumulation bound, beyond rounding. A bound that is only loose (the
  doubling per level never attained) does not defeat it.
tags:
- mathematics
- complex-systems
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
summary: >-
  A projection perturbation bound for the compressed diffusion-wavelet
  chain of Coifman and Maggioni, and for the selected-column chain of
  Sevi, Rilling and Borgnat, proved here and checked numerically
  (scratch/studies/lead-192). If the truncation at level j leaves column
  residual d_j = ‖(I − P_{j+1})A_j‖ and the chain's operator has drifted f_j
  = ‖T^{2^j} − A_j‖ from the true power, the kept subspace is within
  (d_j + f_j)/λ_k^{2^j} of the top-k eigenspace for symmetric T, and f_j ≤
  Σ_{i<j} 2^{j−i}d_i. With strong rank-revealing QR, d_j is at most p(k, n)
  times the first discarded singular value, so the bound is a relative
  gap (λ_{k+1}/λ_k)^{2^j} plus accumulated drift. A non-symmetric T needs a
  row residual as well, which column selection does not control. It gives
  CLAIM-164 a demonstrated step for the compressed chain. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
bears_on:
- QUESTION-218
- QUESTION-222
corroborates:
- CLAIM-164
---
<!-- inactive-ok-file: THEORY-tmpyi9zg LIT-tmpzikaq NOTE-tmpv196v — new, Unfetched and new; the directed construction read for this bound, the report it stands in for, and its reading, filed by the lead run of 2026-11-23 -->

# CLAIM-tmpdsu37: In the compressed diffusion-wavelet chain, where each level's operator is the orthogonal compression of the square of the one before onto the columns kept, the distance between the subspace kept at a level and an invariant subspace of the same dimension is at most the accumulated truncation residual divided by the smallest singular value of the dyadic power on that subspace, so a level is definite when its kept spectrum stands well above the residual and not at a gapless threshold

## The claim

NOTE-984 asks for an error bound for Coifman and Maggioni's compressed
algorithm across levels, "of the form ‖P_{Ṽ_j} − P_{V_j}‖ ≤
(something)·ε/gap_j", which "would settle what a level is numerically".
This is that bound. The "something" is the drift the chain accumulates,
and the "gap" is the smallest kept eigenvalue of the level's dyadic
power, which acts as a relative gap because the residual can never be
smaller than the first discarded one.

## Setting

T is a real n × n matrix with ‖T‖₂ ≤ 1. Every symmetric diffusion operator
with spectrum in [0, 1] qualifies (Coifman and Maggioni), and so does
T = Π^{1/2}PΠ^{−1/2} for a walk P with stationary measure π, since it is
similar through an isometry to P on ℓ²(V, π), where P contracts
(THEORY-tmpyi9zg).

The chain, written in ambient coordinates: A₀ = T, and for i ≥ 0 an
orthogonal projector P_{i+1}, of rank k_{i+1}, chosen by any truncation of
A_i, and

  A_{i+1} = P_{i+1} A_i² P_{i+1}.

For an orthonormal basis Φ_{i+1} of Ran P_{i+1} this is Coifman and
Maggioni's T_{i+1} = Φ_{i+1}ᵀA_{i+1}Φ_{i+1} = M_iM_iᵀ (their (4.16)), so
A_i represents T_i, and level i+1 is read off A_i ≈ T^{2^i}, as THEORY-758
derives. For a non-orthogonal basis Φ of the same space,
Φ^†A_{i+1}Φ is Sevi et al.'s pseudo-inverse compression; the projector,
and so everything below, is the same whichever basis is kept. Nesting
Ran P_{i+1} ⊆ Ran P_i is not needed for the bound.

Write M = 2^j, and

- d_i = ‖(I − P_{i+1})A_i‖, the column residual the truncation controls;
- d′_i = ‖A_i(I − P_{i+1})‖, the row residual;
- f_i = ‖T^{2^i} − A_i‖, the drift of the chain from the true power.

## Proof

**Lemma 1.** ‖A_i‖ ≤ 1 and ‖T^{2^i}‖ ≤ 1. *Proof.* ‖A_{i+1}‖ ≤ ‖A_i‖², and
‖T^m‖ ≤ ‖T‖^m.

**Lemma 2 (accumulation).** f₀ = 0 and

  f_{i+1} ≤ (‖T^{2^i}‖ + ‖A_i‖) f_i + ‖A_i‖ (d_i + d′_i) ≤ 2 f_i + d_i + d′_i.

*Proof.* T^{2^{i+1}} − A_{i+1} = (T^{2^i}T^{2^i} − A_iA_i) + (A_i² − P A_i² P),
with P = P_{i+1}. The first term is T^{2^i}(T^{2^i} − A_i) + (T^{2^i} − A_i)A_i.
The second is (I − P)A_i·A_i + P A_i·A_i(I − P), of norm at most
‖A_i‖(d_i + d′_i). Lemma 1 gives the second inequality.

Hence f_j ≤ Σ_{i<j} 2^{j−1−i}(d_i + d′_i). For symmetric T every A_i is
symmetric, d′_i = d_i, and f_j ≤ Σ_{i<j} 2^{j−i}d_i ≤ (2^{j+1} − 2)·max_i d_i.

**Theorem 3 (the kept subspace).** Let 𝒰 be a T-invariant subspace of
dimension k = k_{j+1}, Q an orthonormal basis of it, and R = QᵀTQ, so that
T^MQ = QR^M. If σ_min(R^M) > 0, then

  ‖P_{j+1} − QQᵀ‖ = ‖(I − P_{j+1})Q‖ ≤ (d_j + f_j) / σ_min(R^M).

*Proof.* (I − P_{j+1})QR^M = (I − P_{j+1})T^MQ
= (I − P_{j+1})A_jQ + (I − P_{j+1})(T^M − A_j)Q, of norm at most d_j + f_j.
And ‖XR^M‖ ≥ ‖X‖σ_min(R^M) for any X. The equality on the left holds
because the two projectors have the same rank: both sides are the sine of
the largest principal angle between the subspaces.

For symmetric T with eigenvalues λ₁ ≥ λ₂ ≥ … ≥ 0, take 𝒰 the span of the
top k eigenvectors. Then σ_min(R^M) = λ_k^{2^j}:

  ‖P_{j+1} − Π_k‖ ≤ (d_j + f_j) / λ_k^{2^j} ≤ (Σ_{i≤j} 2^{j−i}d_i) / λ_k^{2^j}.

**Corollary 4 (graded).** For an eigenvector ξ of T with eigenvalue λ > 0,
‖(I − P_{j+1})ξ‖ ≤ (d_j + f_j)/λ^{2^j}. The same proof with Q = ξ. The
slowest modes are kept far more accurately than those near the cut.

**Corollary 5 (closure).** ‖(I − P_{j+1})T^MP_{j+1}‖ ≤ d_j + f_j, with no gap
in it. And for 𝒰 invariant of dimension k_{j+1},
‖(I − P_{j+1})TP_{j+1}‖ ≤ 2‖T‖·‖P_{j+1} − QQᵀ‖, since (I − Π)TΠ = 0 for
Π = QQᵀ and (I − P)TP − (I − Π)TΠ = (I − P)T(P − Π) + (Π − P)TΠ. So a level
closes at its own time step to within its residual whatever the
spectrum, and closes under one step of T only as well as its subspace is
definite. This is what NOTE-984's check saw on the circle: invariance
under T^{2^j} near 2–7 × 10⁻⁵, under T only near 10⁻².

**The gap.** With strong rank-revealing QR (Gu and Eisenstat, as Coifman
and Maggioni use it), d_j ≤ p(k, n)σ_{k+1}(A_j), and by Weyl's inequality
σ_{k+1}(A_j) ≤ λ_{k+1}^{2^j} + f_j for symmetric T. So

  ‖P_{j+1} − Π_k‖ ≤ p(k, n)(λ_{k+1}/λ_k)^{2^j} + (1 + p(k, n)) f_j / λ_k^{2^j}.

The first term is the relative gap at the cut; the second is the drift
the earlier levels left. Conversely, any truncation of rank k has
d_j ≥ σ_{k+1}(A_j) (Eckart–Young), so the bound cannot fall below about
(λ_{k+1}/λ_k)^{2^j} by choosing the truncation; with λ_{k+1} = λ_k it is
vacuous, as it must be, since the top-k space is then not defined. That
is CLAIM-164's point, now for the compressed chain.

**The constant per level is attained.** For T = diag(a, b) and a kept
direction at angle θ to the first axis, d = (a²sin²θ + b²cos²θ)^{1/2}, so
d/a → sin θ = ‖P − Π‖ as b/a → 0.

## Check

scratch/studies/lead-192 (lead192.py, test_lead192.py, results.txt) runs
the chain on Coifman and Maggioni's circle (n = 256, ε = 10⁻⁴, pivoted
QR), three Gaussian clouds, a prescribed gapped spectrum with a noisy
truncation, and a directed small-world walk T = Π^{1/2}PΠ^{−1/2}. Nine
pytest checks pass. At every level of every case the true subspace
error, the true drift and both closure defects are within their bounds,
and exact (SVD) truncation reproduces the spectral space (THEORY-758).

- Where a wide gap isolates the three clouds (levels 6–13 of 14), the
  error is 1.06 × 10⁻⁴ against a bound of 1.11–1.19 × 10⁻⁴ at levels 6–8:
  the bound with the true drift is tight.
- At the circle's gapless thresholds the error is 0.03–0.98 and the bound
  exceeds 1 at 9 of 12 levels: no definite subspace, as the bound says.
- The a priori drift bound doubles each level while the true drift stays
  near 10⁻⁴ (clouds) or 10⁻⁵ (gapped spectrum). The doubling is not
  attained in these cases.
- For the directed walk the row residual reached 0.13 while the column
  residual stayed near 2 × 10⁻⁴, and the drift rose to 3 × 10⁻²: the row
  residual is a separate quantity, and column selection leaves it
  uncontrolled.

## What it does not say

- **Not that the doubling is sharp.** Lemma 2's factor 2 per level comes
  from squaring errors along eigenvalues near 1. Whether a chain can
  attain it, or whether f_j stays near the largest single residual, is
  open; the check suggests the latter.
- **Not a bound in terms of ε alone.** It is stated in the residuals the
  truncation leaves, which a threshold rule keeps near ε up to p(k, n),
  and which exact arithmetic would make the discarded singular values.
- **Not a bound for a non-normal T in spectral terms.** There the
  denominator is σ_min(R^{2^j}), which can be far below the smallest
  kept |λ|^{2^j}, and the row residual must be bounded separately. What
  the biorthogonal report does about either is unknown: it is unread
  (LIT-tmpzikaq), and its neighbour (NOTE-tmpv196v) gives no bound.
- **Not about the basis inside a level.** The bound is on the subspace.
  Localization, and the conditioning a non-orthogonal basis costs, are
  separate.
