---
number: 886
status: Proposed
formerly:
- CLAIM-tmpdsv4t
title: 'No recovery against re-adapting residents'
statement: >-
  Symmetric competition with bounded niche adaptation does not secure
  recovery against residents that re-adapt: in a two-resource trade-off, a
  stable pair of specialists, each recovering when rare against a frozen
  partner, coexists with a stable lone generalist against which a removed
  specialist has negative growth, and a lone specialist leaves its corner
  for the vacated niche when c/B < a'(0)/a'(1)
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-049 at the
    coordinator's brief. The instance is computed in closed form here;
    that a lone specialist, once it leaves its corner, ends at the
    generalist is CASE-322's simulation, not part of this claim.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation for the stated instance: that the corner
  pair fails Theorem A's hypotheses of CLAIM-885 for B > c > 0 and
  a'(1) > a'(0); that the lone generalist at θ = 1/2 is not an
  equilibrium meeting those hypotheses for the stated a and c/B; that the
  specialist's growth there differs from c(1/(2a(1/2)) − 1); or that the
  lone specialist's outward margin at its corner is not a'(1)c − a'(0)B.
  Not defeated by trade-off shapes with a(1/2) < 1/2, for which the claim
  makes no negative-growth statement.
tags:
- ecology
- mathematics
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-132
rests_on:
- CLAIM-885
grounds:
- CASE-322
summary: >-
  The counterexample [LEAD-049](../leads.d/LEAD-049.md) asked for, within [CLAIM-885](CLAIM-885.md)'s class.
  Two resources with supply (B, B) and cost c. u(θ) = (a(θ), a(1 − θ)),
  θ in [0, 1], with a(0) = 0 and a(1) = 1. The specialists at θ = 1 and
  θ = 0, each with abundance B − c, are locally exponentially stable when
  B > c > 0 and a'(1) > a'(0). Each recovers at B − c against its frozen
  partner. But a lone specialist's margin at its corner is a'(1)c − a'(0)B.
  So when c/B < a'(0)/a'(1) it moves into the vacated resource. Against
  the symmetric lone generalist, a specialist's growth is
  c(1/(2a(1/2)) − 1). That is negative when a(1/2) > 1/2, when the
  generalist's total uptake beats a specialist's. For
  a(t) = t − ½t²(1 − t) + 3t²(1 − t)², with a'(0) = 1, a'(1) = 3/2 and
  a(1/2) = 5/8, the lone generalist is itself a stable state, and the
  removed specialist's growth there is −c/5. Differentiation then holds
  only while no specialist is lost long enough for its partner to
  re-adapt: an alternative stable state of entrenched generalism. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-885 CASE-322 — new, filed with this claim by LEAD-049 -->

# CLAIM-886: No recovery against re-adapting residents

## The claim

The instance is in [CLAIM-885](CLAIM-885.md)'s class. There are two resources with
supply b = (B, B), and two operators with cost c each. The niche map is
u(θ) = (a(θ), a(1 − θ)) on θ ∈ [0, 1], with a increasing, a(0) = 0 and
a(1) = 1. θ = 1 specializes on resource 1, θ = 0 on resource 2, and
θ = 1/2 is the symmetric generalist.

1. **The specialist pair is stable.** At θ = (1, 0), u = (e₁, e₂) and
   A = I, so n* = (B − c, B − c) and R = (c, c). The selection gradient
   at θ₁ = 1 is a'(1)c − a'(0)c, outward when a'(1) > a'(0), and
   symmetrically for θ₂ = 0. No trait is free, and H_F = A = I. So
   [CLAIM-885](CLAIM-885.md)'s Theorem A applies when B > c > 0 and a'(1) > a'(0).
2. **Each recovers against a frozen partner.** Theorem B gives
   λ = n*_i d_i² = B − c, since the niche vectors are orthogonal.
3. **A lone specialist may leave its corner.** Remove operator 2.
   Theorem C's orthogonal case applies: n₁ stays at B − c and
   R = (c, B). The margin at θ₁ = 1 is a'(1)c − a'(0)B. It turns inward
   when c/B < a'(0)/a'(1), and then the resident starts to take the
   vacated resource.
4. **Against the lone generalist, a specialist may not recover.** At
   θ = 1/2 with g = a(1/2), the selection gradient vanishes by symmetry,
   n = (2gB − c)/(2g²) and R = (c/2g)(1, 1). A returning specialist with
   u = (0, 1) grows at c/(2g) − c = c(1/(2a(1/2)) − 1). That is negative
   exactly when a(1/2) > 1/2.
5. **Both states are stable in one instance.** Take
   a(t) = t − ½t²(1 − t) + 3t²(1 − t)², which is increasing on [0, 1].
   Then a'(0) = 1, a'(1) = 3/2 and a(1/2) = 5/8. The pair is stable for
   every B > c > 0, by 1. For c/B in 0.1, 0.2, …, 0.9 the lone generalist
   has positive abundance, zero gradient and a positive definite Hessian
   on its free coordinates. Its smallest eigenvalue is 0.78 at every one
   of these points (scratch/studies/lead-049/generalist_check.py). By
   Theorem A it is a stable state of the one-operator system, and of the
   two-operator system with the specialist absent, since the specialist's
   growth there is −c/5 < 0.

So the class's two ingredients do not secure [QUESTION-132](../questions.d/QUESTION-132.md)'s recovery
condition once residents re-adapt. The record's two measurements, frozen
and trainable, part here. Against frozen residents the specialist
recovers at B − c. Against a resident that has had time to generalize it
declines, at −c/5. Below c/B = 2/3 a lone resident does start to move
(item 3). [CASE-322](../cases.d/CASE-322.md) finds that it then ends at the generalist and that
the removed specialist then fails to return. Above 2/3 the resident stays
put and the specialist returns. The generalist state remains, but removal
does not lead to it.

## What it does not say

- **That this is [QUESTION-132](../questions.d/QUESTION-132.md)'s third outcome as the question defines
  it.** The generalist is not held by an early advantage of one of several
  processes. It is an alternative stable state that removal can make the
  system fall into, with differentiation lost. Whether that counts as
  "entrenched asymmetry", a fourth outcome, or neither is the owner's to
  decide. The two readings are left open.
- **That re-adaptation always closes a niche.** With a(1/2) < 1/2 the
  lone generalist leaves room, and the specialist returns ([CASE-322](../cases.d/CASE-322.md)).
- **Anything for other trade-off shapes, more resources or more
  operators.** In [CASE-322](../cases.d/CASE-322.md)'s Gaussian-niche runs that met Theorem
  A, recovery against re-adapted residents stayed positive in all 64
  removals, though at a median 0.29 of the frozen rate.
