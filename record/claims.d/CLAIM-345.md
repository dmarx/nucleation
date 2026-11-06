---
number: 345
status: Active
formerly:
- CLAIM-tmp1glr8
title: 'Equal controllability rank does not fix the cost of control: for x_{t+1} = x_t + b·u the least quadratic effort for a displacement Δ is Δ²/b², unbounded as b → 0 while the system stays controllable, and in general the least effort is Δxᵀ W_T^† Δx, set by the Gramian and not by its rank'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    A dated note added at the status review's ruling (the owner delegated
    these rulings): the reading of Rocks and Mehta in full (NOTE-1557
    version 2) qualifies the note that cited it, since which force excites
    a zero mode depends on prestress and not on stiffness. No status
    change.
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
supports:
- CLAIM-354
---
<!-- inactive-ok-file: CLAIM-tmp5iqbr — Proposed and new; the status review's own result from Rocks and Mehta, cited as checked, left for the next pass to rule on -->
<!-- inactive-ok-file: NOTE-1592 NOTE-1596 — Proposed or new; the constraint-architecture readings of 2026-11-05, cited as open -->
<!-- inactive-ok-file: CASE-214 — Proposed or new; entries of 2026-11-05 filed from the pasted synthesis on constraint architectures, cited as open -->

# CLAIM-345: Equal controllability rank does not fix the cost of control: for x_{t+1} = x_t + b·u the least quadratic effort for a displacement Δ is Δ²/b², unbounded as b → 0 while the system stays controllable, and in general the least effort is Δxᵀ W_T^† Δx, set by the Gramian and not by its rank

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
binary" (the owner, U9), and it is why [CLAIM-354](CLAIM-354.md) counts control cost
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
  [CLAIM-354](CLAIM-354.md)'s interpretive step, not this claim's.
- **Not new.** A9: "This is already a standard result from linear control
  theory." The record holds it as a proof because it holds no source for
  it.
- **Not constrained or nonlinear control.** With bounded inputs a costly
  displacement may be unreachable in T steps, and nonlinear systems have
  no Gramian in this form.

## Note of 2026-11-05: the constraint-architecture readings

Several readings from the pasted synthesis on constraint architectures support the claim's lesson, that equal nominal freedom does not fix cost, by mechanical analogy. In Hopkins's Freedom and Constraint Topologies ([NOTE-1592](../notes.d/NOTE-1592.md), [NOTE-1596](../notes.d/NOTE-1596.md), [NOTE-1580](../notes.d/NOTE-1580.md)), redundant constraints change stiffness and stability with the freedom space unchanged, and kinematically equivalent designs differ in "elastomechanics, dynamics, and manufacturability". Rocks and Mehta ([NOTE-1557](../notes.d/NOTE-1557.md)) and Damavandi et al. ([NOTE-1570](../notes.d/NOTE-1570.md)) find the like in spring networks: geometry fixes the zero-mode count, while which force excites a mode, and energetic stiffness, depend on stiffness and prestress. Krishnakumar and Suresh's designs ([NOTE-1582](../notes.d/NOTE-1582.md)) share an intended motion and differ in geometric and mechanical advantage as a weighting varies. All of this is structure, not control: none computes an effort or bears on Δ²/b².

Murray and Sastry ([NOTE-1622](../notes.d/NOTE-1622.md)) come closest, in kind: rank settles reachability, while motion along higher brackets takes more input cycles, so rank-equal systems can differ in cost; no cost is computed beyond the first-order case. Dollar and Howe ([NOTE-1575](../notes.d/NOTE-1575.md)) qualify the frame: which freedoms are left passive mattered there, not the cost of control.

Two entries filed from A's proposals bear on it. [CASE-214](../cases.d/CASE-214.md) is a constructed static analogue: two flexure stages with one freedom space, one with every constraint doubled, differing twofold in disturbance error and drive force. [CLAIM-562](CLAIM-562.md) complements the claim from the other side: in Stern, Pinson and Murugan's sheets, equal actuator counts do not fix the chance of folding correctly. No status changes.

## Note of 2026-11-06: Rocks and Mehta, read in full

The reading of Rocks and Mehta in full (NOTE-1557, version 2) qualifies one phrase of the note above. Which force excites a zero mode depends on prestress, not on stiffness. For a zero mode u the force is (T + λI)u, and stiffness drops out (CLAIM-tmp5iqbr, the status review's own result, checked by a second checker). Stiffness enters the rest of the response and the energetic stiffness. The analogy stands. No status changes.
