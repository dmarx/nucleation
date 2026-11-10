---
number: 550
status: Active
formerly:
- CLAIM-tmp8e3ye
title: 'A perspective''s tolerance of departure from what it maintains can be derived from its activation threshold: if its activation is z = b(c) + α(c)d, rising with discrepancy d (α > 0), and it acts with probability σ(κ(z − θ)), the discrepancy it tolerates while acting with probability at most ε is (θ + κ⁻¹ logit ε − b(c))/α(c); so one fixed threshold gives different tolerances across contexts through baseline and gain, a negative tolerance marks activation driven by something other than the discrepancy, and raising a threshold enlarges tolerance without relieving any demand'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Status Proposed → Active at the status review's ruling (the owner
    delegated these rulings), under ADR-057 and ADR-047's ruling on a
    checked re-derivation. Re-derived at the review: with κ > 0 and σ
    increasing, σ(κ(z − θ)) ≤ ε exactly when z ≤ θ + κ⁻¹ logit ε, and with
    α > 0 that is d ≤ (θ + κ⁻¹ logit ε − b)/α; the bound rises with θ at
    rate 1/α and is negative exactly when b > θ + κ⁻¹ logit ε. That
    raising θ is not relief is CLAIM-347's, its one premise, Active.
- version: 3
  date: '2026-11-10'
  note: >-
    Carries distributed-agency as well, at the sweep of ADR-tmpk61vy's
    rule followed to its end (2026-11-10, round 2): the entry takes part
    in that line's argument: distributed-agency, since it bears on
    QUESTION-372, which gained the line in an earlier round. No other
    change.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation. As a claim about perspectives, it is defeated
  by one whose tolerance, measured across contexts with baseline and gain
  measured too, departs from the derived value in a way that no monotone
  response of activation to discrepancy explains. Not defeated by
  activation that is nonlinear or depends on more than one discrepancy.
  There the general form T^ε(c) = {w : Pr(act | w, c) ≤ ε} replaces the
  scalar, and the claim does not say the scalar holds.
tags:
- motivation
- behavioral-integration
- mathematics
date: '2026-11-04'
line:
- will-organization
- formal-apparatus
- distributed-agency
rests_on:
- CLAIM-347
complements:
- CLAIM-534
- CLAIM-361
- CLAIM-548
- CLAIM-549
- CLAIM-553
bears_on:
- QUESTION-372
summary: >-
  The first link of the owner's chain at U19 of the exchange
  "Organizational Nucleation and SLT" (2026-11-04), "motivational threshold
  -> motivational tolerances". It follows the owner's U15, which read a
  perspective's tolerance as the "likelihood of communicating a complaint",
  and U17, "reframe 'complaint' as something closer to 'intervention
  threshold' or 'activation threshold'". A20 §2 derived τ = (θ − b)/α, and
  A26 §2 restated it. That is the ε = 1/2 case only. The reader of U26–U27
  gave the general ε form. [CLAIM-534](CLAIM-534.md) takes tolerances as given, and this
  derives them. The chain is the owner's. The wording is A's, sharpened by
  the reader; adopting it is the owner's call.
---

# CLAIM-550: A perspective's tolerance of departure from what it maintains can be derived from its activation threshold: if its activation is z = b(c) + α(c)d, rising with discrepancy d (α > 0), and it acts with probability σ(κ(z − θ)), the discrepancy it tolerates while acting with probability at most ε is (θ + κ⁻¹ logit ε − b(c))/α(c); so one fixed threshold gives different tolerances across contexts through baseline and gain, a negative tolerance marks activation driven by something other than the discrepancy, and raising a threshold enlarges tolerance without relieving any demand

## The claim

The owner's sequence of turns:

- U15: "assign each perspective a scalar tolerance measure that identifies
  likelihood of communicating a complaint".
- U17: "reframe 'complaint' as something closer to 'intervention
  threshold' or 'activation threshold'".
- U19: "motivational threshold -> motivational tolerances -> motivational
  compatibility -> psychological flexibility / organizational
  effectiveness".

A20 §2 made the first arrow a derivation. "We can now derive a notion of
tolerance rather than stipulating it independently." Let a perspective's
activation be z_i(w, c) = b_i(c) + α_i(c) d_i(w, c), with α_i(c) > 0, where
d_i is the discrepancy between the effective will w and what the
perspective would prefer. Let its probability of acting be
Pr(a_i = 1 | w, c) = σ(κ_i[z_i − θ_i]), with κ_i > 0.

**Derivation.** Pr(a_i = 1) ≤ ε holds exactly when
κ_i(b_i + α_i d_i − θ_i) ≤ logit ε. That holds exactly when

  d_i ≤ τ_i^ε(c) = (θ_i + κ_i⁻¹ logit ε − b_i(c)) / α_i(c).

A20 and A26 wrote τ_i(c) = (θ_i − b_i(c))/α_i(c). That is the case
ε = 1/2, where logit ε = 0. A20 itself noted that "a logistic response has
a 50% activation probability at its threshold, not zero". It wrote
T_i^ε(c) = {w : Pr(a_i = 1 | w, c) ≤ ε} beside τ_i as if they were one
object. For ε < 1/2 the two differ by the shift κ_i⁻¹ logit ε / α_i, which
depends on κ. If α_i < 0 the inequality reverses.

**Consequences.**

1. **Threshold is not tolerance.** A20: "A perspective can have a constant
   activation threshold but a changing tolerance because its baseline
   activation b_i(c) changes." Its example: the same disposition to defend
   a boundary is "more readily activated when exhausted, frightened, or
   already angry". A change in the gain α_i(c) does the same.
2. **Negative tolerance.** A20: "a perspective with τ_i(c) < 0 is already
   above threshold at zero discrepancy: activation is being driven by
   something beyond disagreement with the effective will." For general ε
   this happens when b_i > θ_i + κ_i⁻¹ logit ε.
3. **Raising a threshold is not relief.** τ_i^ε increases with θ_i. So
   raising a threshold enlarges the perspective's low-activation region,
   and enlarges every complex built on such regions. It does so without
   changing what the organization can attain, or what any demand requires.
   By [CLAIM-347](CLAIM-347.md) and [CLAIM-361](CLAIM-361.md), a change to the criteria being tested is not
   relief. A21 put the contrast as "Route 1: Increase tolerance" against
   "Route 2: Improve accommodation". [CLAIM-549](CLAIM-549.md) holds the complex-level
   form.

## Where it sits

- **[CLAIM-534](CLAIM-534.md)** speaks of demands "jointly met, within tolerances it can
  recognize", and [CLAIM-538](CLAIM-538.md) gives per-overlap tolerances δ_e. Both take
  tolerances as given. This claim gives one way they can arise: from the
  activation dynamics of the perspective that maintains the demand.
- **[CASE-112](../cases.d/CASE-112.md)** is the record's precedent for a threshold derived from
  dynamics. It is a regime switch at h_c = 2μ^{3/2}/(3√3), not the
  tolerance of a demand.
- **[CASE-156](../cases.d/CASE-156.md)** is a worked logistic with a baseline and a gain. In it one
  rule admits different fractions as these vary, which is the shape of
  consequence 1.

## What it does not say

- That a perspective's low-activation region is its acceptance set. A19:
  T_i "is a *nonactivation region*, not automatically an endorsement
  region".
- That real perspectives have linear activation or one discrepancy. The
  scalar form is the special case. A20: "A single scalar τ_i is sufficient
  only when a one-dimensional discrepancy adequately summarizes what
  activates the process."
- That higher tolerance is better. A20 §7: raising the defensive process's
  threshold "might reduce false alarms, while also preventing appropriate
  emergency responses."
- Anything about how baseline and gain are measured in persons.
