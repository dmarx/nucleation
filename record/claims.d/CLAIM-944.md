---
number: 944
status: Proposed
formerly:
- CLAIM-tmp03h8w
title: 'The receiver-restricted informativeness order has results of its own without Blackwell''s garbling theorem: it is decided by inclusion of the receiver''s achievable sets and is the same under every full-support prior, a garbling can never hurt a receiver exactly when the receiver can apply it itself, so the garblings it respects form a monoid, no receiver does better with a garbling than the unrestricted one does with the source, and the order neither implies nor follows from garbling'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-100. The proofs
    are below; the numerical checks are CASE-361.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in one of the proofs below, or a finite experiment pair,
  receiver class and bounded loss that violates one of the six results as
  stated (with the receiver's rules closed under mixture and limits, as the
  definition takes them). A receiver class with no rules, an infinite
  medium, or a prior without full support does not count; the results are
  stated for finite media and full-support priors.
tags:
- information-theory
- mathematical-statistics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
uses:
- TERM-150
grounds:
- THEORY-1096
complements:
- CLAIM-199
- CLAIM-050
- CLAIM-455
bears_on:
- QUESTION-110
summary: >-
  [LEAD-100](../leads.d/LEAD-100.md) asked for a receiver-restricted order with its own results, the
  first of the two answers [CLAIM-225](CLAIM-225.md) names and [ARG-019](../arguments.d/ARG-019.md) says would settle it.
  [TERM-150](../terms.d/TERM-150.md) defines it: experiments are compared by the best risk the
  receiver's rule class attains, over every bounded loss and full-support
  prior. Six results are proved by elementary means, the only tools being
  associativity of kernels, Blackwell's easy direction ([THEORY-1096](../theory.d/THEORY-1096.md)) and
  separation of a point from a compact convex set. Result 3 makes exact
  [CLAIM-199](CLAIM-199.md)'s gloss that a garbling helps a receiver "only when they do
  work the receiver cannot". Result 5 is what restricting the rules costs.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: TERM-150 CASE-361 ARG-019 CLAIM-087 — Proposed or new; the term this is stated in, its checks, the argument it bears on and the improvement claim it formalises -->

# CLAIM-944: The receiver-restricted informativeness order has results of its own without Blackwell's garbling theorem: it is decided by inclusion of the receiver's achievable sets and is the same under every full-support prior, a garbling can never hurt a receiver exactly when the receiver can apply it itself, so the garblings it respects form a monoid, no receiver does better with a garbling than the unrestricted one does with the source, and the order neither implies nor follows from garbling

## Setting

As in [TERM-150](../terms.d/TERM-150.md): finite situations Θ with a full-support prior π, a
finite medium X, experiments P(x | θ), a receiver R giving for each finite
action set A a nonempty rule set R_A with closed convex hull R̄_A, usable
risk V_R(P; L, π), achievable sets Ach_{R,A}(P) = { Pδ : δ in R̄_A }, and
the order P ⪰_R P'. Kernels compose as matrices: Pδ is the kernel from
situations to actions that P followed by δ realises, and PG is P garbled by
a kernel G on X. A garbling into another medium is a kernel on the
disjoint union. The numerical checks of what follows are [CASE-361](../cases.d/CASE-361.md).

The risk of δ with P is the linear functional
ℓ_{L,π}(Pδ) = Σ_θ π(θ) Σ_a (Pδ)(θ, a) L(θ, a), so
V_R(P; L, π) = min over M in Ach_{R,A}(P) of ℓ_{L,π}(M). The infimum over
R_A equals the minimum over R̄_A because ℓ is linear and continuous and R̄_A
is compact.

## The results

**1. A preorder.** ⪰_R is reflexive and transitive, being defined by
inequalities between numbers for each (A, L, π). It is not antisymmetric:
[CLAIM-199](CLAIM-199.md)'s source and its exclusive-or are equivalent for the unrestricted
receiver.

**2. The achievable-set criterion, and prior-freedom.** Fix A and a
full-support π. Then V_R(P; L, π) ≤ V_R(P'; L, π) for every bounded L on A
if and only if Ach_{R,A}(P') ⊆ Ach_{R,A}(P). So ⪰_R is the same order
whichever full-support prior is used.

*Proof.* If the inclusion holds, a minimum over the larger set is no
larger. If not, some M' in Ach_{R,A}(P') lies outside Ach_{R,A}(P), which is
compact and convex, being the image of R̄_A under a linear map. Strict
separation gives a matrix W with Σ W(θ,a) M'(θ,a) < min over M in
Ach_{R,A}(P) of Σ W(θ,a) M(θ,a). Put L(θ, a) = W(θ, a) / π(θ), which is
possible since π has full support. Then V_R(P'; L, π) ≤ ℓ_{L,π}(M') <
V_R(P; L, π). The criterion does not mention π. ∎

This is the receiver's counterpart of Blackwell's definition by attainable
risk vectors ([THEORY-1096](../theory.d/THEORY-1096.md)), and it is proved by a separation argument,
not by the garbling theorem.

**3. The garblings a receiver respects.** Say R respects a garbling G on X
when Gδ is in R̄_A for every δ in R_A and every A: the receiver can apply G
itself before any of its rules.

- (a) If R respects G, then P ⪰_R PG for every experiment P.
- (b) Conversely, if P ⪰_R PG for every experiment P on every finite set
  of situations, then R respects G. The identity experiment on Θ = X
  alone forces it.
- (c) The garblings R respects form a monoid Mon(R): it holds the identity
  and is closed under composition. For the unrestricted receiver Mon(R) is
  every garbling, and (a) is Blackwell's easy direction.

*Proof.* (a) The risk of δ with PG is ℓ(P(Gδ)), the risk of Gδ with P, and
Gδ is in R̄_A, so every risk the receiver attains with PG it attains with P.
(b) For the identity experiment I, Ach_{R,A}(I) = R̄_A and Ach_{R,A}(G) =
{ Gδ : δ in R̄_A }. By result 2, I ⪰_R G gives { Gδ } ⊆ R̄_A. (c) If G₁ and
G₂ map R_A into R̄_A, they map R̄_A into R̄_A by linearity and continuity,
so G₁G₂δ = G₁(G₂δ) is in R̄_A. ∎

So a rendering made without the situation can raise some receiver's usable
risk on some source exactly when it is a garbling the receiver cannot carry
out itself. This makes exact [CLAIM-199](CLAIM-199.md)'s gloss that garblings "help a
receiver only when they do work the receiver cannot": the gain is possible
for G exactly when G is outside Mon(R). It does not say the gain occurs for
a given source, nor who gains most ([CASE-062](../cases.d/CASE-062.md)'s reversal is untouched).

**4. The ceiling.** If P' = PK for any kernel K, then for every receiver R,
every L and π, V_R(P'; L, π) ≥ V_all(P; L, π), the unrestricted receiver's
risk with P.

*Proof.* V_R(P') ≥ V_all(P') since R̄_A is within all rules, and V_all(P')
≥ V_all(P) by Blackwell's easy direction ([THEORY-1096](../theory.d/THEORY-1096.md)). ∎

This is [CLAIM-199](CLAIM-199.md)'s ceiling, now a result about the order: Blackwell's
order bounds ⪰_R from outside without deciding it.

**5. No garbling theorem.** There are a receiver R and experiments P, P'
with P ≻_R P' strictly while P' is strictly more informative than P in
Blackwell's order: P is a garbling of P' and not conversely. So P ⪰_R P'
neither implies nor is implied by "P' is a garbling of P", and the orders
of nested receiver classes are not nested.

*Construction.* Θ = {0, 1} uniform, medium X = {0, 1}², and R the receiver
whose rules read one coordinate (the union of the two classes that factor
through a coordinate). P' is [CLAIM-199](CLAIM-199.md)'s source: x₁ a fair coin and
x₂ = θ ⊕ x₁. P reports x₁ = θ with probability 0.9 and draws x₂ as an
independent fair coin. Under R each coordinate of P' is independent of θ,
so Ach_{R,A}(P') holds only kernels constant in θ, all of which R attains
with P as well; and R guesses θ from P with risk 0.1 against 0.5 from P'.
For the unrestricted receiver P' reveals θ, so P is a garbling of it, and
guessing θ has risk 0 with P' against 0.1 with P. The one-coordinate class
is inside the unrestricted one, and they order P and P' oppositely. ∎

**6. Receivers that read through a fixed code.** If R_A = { Tδ' : δ' any
rule on Y } for a kernel T from X to a medium Y (the receiver reads the
rendering only through T, say a lexicon it has), then:

- P ⪰_R P' if and only if P'T is a garbling of PT; and
- Mon(R) = { G : GT = TH for some kernel H on Y }.

*Proof.* Ach_{R,A}(P) = { PTD : D a rule from Y to A }. If P'T = PTK, then
P'TD = PT(KD). Conversely take A = Y and D the identity: P'T lies in
Ach_{R,Y}(P'), hence in Ach_{R,Y}(P), so P'T = PTD for some D. For Mon(R),
GTD must be TD' for every D; with A = Y and D the identity this is GT = TH,
and GT = TH gives GTD = T(HD). ∎

A receiver whose restriction is one code thus has Blackwell's order on what
the code lets through, converse included, from result 2 and the identity
rule alone. The one-coordinate receiver of result 5 is a union of two such
receivers, and the union loses the converse.

## What it changes

- [CLAIM-225](CLAIM-225.md)'s first answer is supplied: "A receiver-restricted order, with
  decision rules limited to a stated class ... so it needs its own
  results." It has them, and result 5 shows that the loss of Blackwell's
  garbling theorem is real, not a gap in the proofs.
- [ARG-019](../arguments.d/ARG-019.md)'s open point moves. The order the line's receiver standard needs
  now exists with results; what is missing is which rule class real
  receivers have, which [CLAIM-199](CLAIM-199.md) already says it does not say. Whether
  this settles [ARG-019](../arguments.d/ARG-019.md) is the owner's call; its dated note of 2026-11-22
  sets out the readings.
- [CLAIM-087](CLAIM-087.md)'s improvement, if it occurs, is a garbling outside Mon(R) for
  the receivers' class (result 3), bounded by result 4.
- [CLAIM-050](CLAIM-050.md)'s ceiling is result 4 seen from the receiver's side, and its
  family Q gives ⪰_{R,Q}, for which results 1, 3(a), 3(c) and 4 hold as
  stated. Result 2 holds for Q only when Q contains every loss on an action
  set, and results 3(b) and 6 use such losses.
- [CLAIM-455](CLAIM-455.md)'s task-relativity concerns one task at a time; this order
  quantifies over every task, so it complements that claim and does not
  replace it.

## What it does not say

- It does not say which rule class any real receiver has, or that the
  classes of result 6 fit readers.
- It gives no approximate version (a receiver-restricted deficiency), and
  no cost of recovery, so [QUESTION-110](../questions.d/QUESTION-110.md) stays open.
- The results are for finite media and full-support priors. Results 1, 3(a)
  and 4 carry over to general spaces with [THEORY-1096](../theory.d/THEORY-1096.md)'s measure-theoretic
  care; results 2, 3(b) and 6 use finite-dimensional separation and were
  not checked beyond it.
