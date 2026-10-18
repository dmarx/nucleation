---
status: Active
title: 'Equal controllability rank does not fix the cost of control: for x_{t+1} = x_t + b·u the least quadratic effort for a displacement Δ is Δ²/b², unbounded as b → 0 while the system stays controllable, and in general the least effort is Δxᵀ W_T^† Δx, set by the Gramian and not by its rank'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: an admissible input sequence that reaches
  the displacement at smaller cost under the stated quadratic norm, or a
  reachable displacement whose least cost differs from Δxᵀ W_T^† Δx. Not
  defeated by a change of input units or norm, which changes the
  problem, as the claim says.
tags:
- mathematics
- agency
date: '2026-10-18'
line:
- will-organization
- formal-apparatus
summary: >-
  A9 §2 and A12's Proposition 1 of the exchange of 2026-10-17, the step
  the owner's U9 "controllability of a system isn't binary" needs. For a
  scalar step x_{t+1} = x_t + b·u the cheapest input costs Δ²/b², so two
  systems that are both controllable can differ in cost by any factor.
  The general statement is the minimum-energy formula with the
  controllability Gramian. A9: "This is already a standard result from
  linear control theory." Proved here because the record holds no source
  for it. The sharp edge: the cost is relative to a fixed input norm, and
  rescaling the input makes every b cost the same, so comparing costs
  across systems needs inputs in common units.
---

# CLAIM-tmp1glr8: Equal controllability rank does not fix the cost of control: for x_{t+1} = x_t + b·u the least quadratic effort for a displacement Δ is Δ²/b², unbounded as b → 0 while the system stays controllable, and in general the least effort is Δxᵀ W_T^† Δx, set by the Gramian and not by its rank

## The claim

A9 §2: "Two systems may both be formally controllable but have radically
different minimum energies for the same change." A12's Proposition 1:
"For x_{t+1}=x_t+bu_t, any b≠0 gives one-step controllability. But
achieving a fixed displacement Δ with quadratic effort costs
E_min=Δ²/b². The required effort is unbounded as b→0, despite unchanged
controllability rank." A15 kept it, adding "proportional to b⁻²".

Rank is a yes-or-no summary: the system is controllable for every b ≠ 0
and not at b = 0. The cost varies continuously and without bound inside
the controllable range. That is the sense in which controllability "isn't
binary" (the owner, U9), and it is why CLAIM-tmpilfhr counts control cost
as a dimension of its own.

## Proof

**Scalar case.** Take x_{t+1} = x_t + b·u_t with b ≠ 0, one step, cost u².
Reaching x₁ = x₀ + Δ forces b·u₀ = Δ, so u₀ = Δ/b is the only admissible
input, and its cost is Δ²/b². For any two nonzero gains b₁, b₂ the costs
of the same Δ stand in the ratio (b₂/b₁)², which is any positive number.
As b → 0 the cost diverges. Over T steps the least cost is Δ²/(T b²): the
constraint is b·Σu_k = Δ, and by Cauchy–Schwarz Σu_k² ≥ (Σu_k)²/T, with
equality at equal inputs. It still diverges as b → 0.

**General case.** Take x_{t+1} = A x_t + B u_t over T steps, cost
Σ‖u_k‖². Then

  x_T = A^T x₀ + 𝒞U,  𝒞 = [A^{T−1}B, …, AB, B],  U = (u₀, …, u_{T−1}),

so the constraint is 𝒞U = Δx with Δx = x_T − A^T x₀. Write
W_T = 𝒞𝒞ᵀ = Σ_{k=0}^{T−1} A^k B Bᵀ (Aᵀ)^k, the finite-horizon
controllability Gramian. Its range is the range of 𝒞.

- Δx is reachable exactly when it lies in the range of 𝒞, that is, of W_T.
- Every solution splits as U = U* + N with U* in the range of 𝒞ᵀ and N in
  the kernel of 𝒞. The two are orthogonal, so ‖U‖² = ‖U*‖² + ‖N‖², and the
  least cost is at N = 0.
- U* = 𝒞ᵀ W_T^† Δx solves the constraint: 𝒞U* = W_T W_T^† Δx = Δx, since
  W_T W_T^† projects onto the range of W_T, which contains Δx. It lies in
  the range of 𝒞ᵀ.
- Its cost is U*ᵀU* = Δxᵀ W_T^† 𝒞𝒞ᵀ W_T^† Δx = Δxᵀ W_T^† W_T W_T^† Δx
  = Δxᵀ W_T^† Δx.

So E_min = Δxᵀ W_T^† Δx, which is A9's formula. The scalar case is
A = 1, B = b, T = 1, W_1 = b². The rank of W_T says which directions are
reachable. Its eigenvalues say what they cost: the cost along a unit
eigenvector of W_T is the reciprocal of its eigenvalue. Two systems with
Gramians of the same rank can have any eigenvalues, and so any costs.

## What it does not say

- **Not a fact about units.** The cost is for a fixed input and a fixed
  norm. Put v = b·u and every scalar system costs Δ². A comparison of b₁
  with b₂ is meaningful only when u means the same in both, a common unit
  of effort. That is the modelling step A9 names: "We would need to
  establish a defensible system model, interventions, units, and cost
  function before interpreting its values."
- **Not a psychological measure.** A9: "Importantly, a Gramian is not
  automatically a meaningful psychological measure." The claim is linear
  algebra. That a habit is costly to change in this sense is
  CLAIM-tmpilfhr's interpretive step, not this claim's.
- **Not new.** A9: "This is already a standard result from linear control
  theory." The record holds it as a proof because it holds no source for
  it.
- **Not constrained or nonlinear control.** With bounded inputs a costly
  displacement may be unreachable in T steps, and nonlinear systems have
  no Gramian in this form.
