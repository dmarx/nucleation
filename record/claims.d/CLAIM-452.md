---
number: 452
status: Active
formerly:
- CLAIM-tmpa8ttt
title: 'For an organization whose response in each probe context is the authority-weighted mixture of its processes'' known response profiles, the authority shares are identifiable from a set of contexts exactly when the processes'' stacked profiles over those contexts are affinely independent; because the response is linear in the shares, local and global identifiability coincide, the condition is that the Fisher information of any design supported on those contexts is positive definite on the simplex''s tangent space, and with binary outcomes at least one context fewer than there are processes is needed'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed at the owner's direction, from the derivation proposed by the
    reader of Bartók et al., Kwon & Perchet and Chaloner & Verdinelli
    (2026-10-25). Checked numerically on 20,000 random mixtures, with
    duplicated and affinely dependent profiles included: the affine
    condition and the positive-definiteness of the design's Fisher
    information agreed in every case.
role: thesis
warrant: demonstrated
defeated_if: >-
  A mixture of known profiles in which two distinct share vectors give the
  same response law in every context of C although the stacked profiles
  over C are affinely independent, or the reverse; or a design supported on
  C whose Fisher information is positive definite on the tangent space
  while the profiles over C are affinely dependent.
tags:
- mathematical-statistics
- self-governance
date: '2026-10-25'
line:
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-444
grounds:
- CASE-159
- THEORY-956
- THEORY-954
answers:
- QUESTION-272
summary: >-
  When an organization's response in context c is p_π(·|c) =
  Σᵢ πᵢ pᵢ(·|c), the mixture [CLAIM-444](CLAIM-444.md) reduces the replicator model to,
  which probe contexts reveal its authority shares π? Exactly those over
  which the profiles are affinely independent. The response is linear in
  π, so there is no gap between local and global identifiability, and the
  condition is the Fisher information of [CASE-159](../cases.d/CASE-159.md)'s pullback being
  positive definite on the tangent space of the simplex. Each binary
  context adds at most one rank, so k processes need at least k − 1
  contexts. It is a condition checkable before any data, which is what
  [QUESTION-031](../questions.d/QUESTION-031.md) asks for; none of the three works read on 2026-10-25 states
  it.
---

# CLAIM-452: For an organization whose response in each probe context is the authority-weighted mixture of its processes' known response profiles, the authority shares are identifiable from a set of contexts exactly when the processes' stacked profiles over those contexts are affinely independent; because the response is linear in the shares, local and global identifiability coincide, the condition is that the Fisher information of any design supported on those contexts is positive definite on the simplex's tangent space, and with binary outcomes at least one context fewer than there are processes is needed

## The claim

Let k processes have known response profiles pᵢ(·|c) over the outcomes
of each context c in a set C, and let the organization's response be the
mixture p_π(·|c) = Σᵢ πᵢ pᵢ(·|c), with π in the simplex Δ_k ([CLAIM-444](CLAIM-444.md)'s
reduction). Then:

1. **Identifiability.** π is identified from the response laws on C iff
   there is no nonzero v with Σᵢ vᵢ = 0 and Σᵢ vᵢ pᵢ(·|c) = 0 for every
   c ∈ C. Equivalently, the stacked profile vectors (pᵢ(·|c))_{c∈C},
   i = 1, …, k, are affinely independent.
2. **Local is global.** p_π is linear in π, so two shares π, π′ give the
   same laws iff v = π − π′ satisfies the condition in 1, and the
   condition does not depend on where in the simplex π lies.
3. **The Fisher form.** For any design ξ with support C and π in the
   interior of Δ_k with every response probability strictly between 0 and
   1, the Fisher information G_ξ = Σ_c ξ(c) G_c of [CASE-159](../cases.d/CASE-159.md) is
   positive definite on the tangent space {v : Σvᵢ = 0} iff the condition
   in 1 holds. G_c is the pullback of the response law's Fisher metric
   through the linear map v ↦ Σᵢ vᵢ pᵢ(·|c), so v is in its kernel iff
   that map sends v to 0.
4. **A count.** With binary outcomes each context contributes one
   dimension (pᵢ(1|c); pᵢ(0|c) is fixed by it), so the k − 1 dimensions of
   the tangent space need at least k − 1 contexts.

## Proof

1 and 2: the laws on C agree for π and π′ iff Σᵢ (πᵢ − π′ᵢ) pᵢ(·|c) = 0
for all c, and π − π′ ranges over the nonzero sum-zero vectors as π ≠ π′
range over Δ_k (for any sum-zero v, π + tv stays in Δ_k for small t when
π is interior, and the condition is linear in v). 3: G_c(v, v) =
Σ_y (Σᵢ vᵢ pᵢ(y|c))² / p_π(y|c), a sum of nonnegative terms that vanishes
iff Σᵢ vᵢ pᵢ(y|c) = 0 for every y; summing over c with ξ(c) > 0 gives 1's
condition. 4: the tangent space has dimension k − 1 and each binary
context is one linear constraint.

## How it was checked

20,000 random mixtures with k from 2 to 5 processes and 1 to 6 binary
contexts, with profiles uniform on [0.05, 0.95], 30% with a duplicated
profile and 20% with one profile the midpoint of two others. In every
case the affine condition and the positive-definiteness of G_ξ under the
uniform design agreed, and no case with fewer than k − 1 contexts was
identified. In [CASE-159](../cases.d/CASE-159.md)'s three-process example, the two contexts
that the D-optimal design weights (½ each) identify π, and the two that
it leaves out do not.

## What it does not say

- **Not unknown profiles.** The profiles are known. With profiles also
  estimated, identification is of a mixture model in the usual sense and
  can fail where this succeeds.
- **Not accessibility.** It says which contexts would identify π, not
  that they can be run. A probe the organization never meets is an action
  outside the probe set, as in [THEORY-962](../theory.d/THEORY-962.md)'s partial-monitoring
  terms ([CLAIM-446](CLAIM-446.md)'s note).
- **Not how well.** Identifiability is all or nothing. How precisely a
  design estimates π is the design criterion's question ([THEORY-956](../theory.d/THEORY-956.md),
  [THEORY-954](../theory.d/THEORY-954.md)), and depends on π because the problem is nonlinear in
  Chaloner and Verdinelli's sense.
- **Not beyond the mixture.** If the organization's response is not the
  authority-weighted mixture, as when legibility keeps memory
  ([CLAIM-444](CLAIM-444.md)'s conditions), the condition is for the null model only.
