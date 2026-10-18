---
number: 357
status: Proposed
formerly:
- CLAIM-tmpl8vsy
title: 'An organization''s failure to meet its demands is structural when no admissible transformation meets them all and a realization failure when an acceptable one exists and is not made effective, and governance-induced frustration is the part of realization failure due to the organization of influence, authority or selection, not to information, search, modelling or chance; aggregate performance does not tell structural from realization failure, and the multipliers that certify infeasibility are not the weights governance assigns'
version: 2
history:
- version: 2
  date: '2026-10-18'
  note: >-
    Retitled at the owner's third review: realization failure is the general case, and governance-induced frustration the part of it due to the organization of influence; Γ measures realization failure, not its cause. uses moves to TERM-tmp9p3s9, which supersedes TERM-060.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that every failure of actual updates to meet satisfiable
  demands is explained by known optimization mechanisms (step size,
  curvature, noise, conditioning, a fixed weighting rule) without
  modelling endorsement or the allocation of authority, so that the
  governance-induced category adds nothing an optimizer analysis does
  not already give. Not defeated by the formal facts that Γ ≥ 0 and that
  Φ certifies infeasibility, which it rests on, nor by cases where the
  two kinds occur together.
tags:
- self-governance
- agency
- operations-research
date: '2026-10-18'
line:
- distributed-agency
- will-organization
rests_on:
- CLAIM-365
- CLAIM-368
complements:
- CLAIM-297
- CLAIM-342
- CLAIM-330
uses:
- TERM-tmp9p3s9
summary: >-
  A34 §4 and A35 §3.3 of the exchange of 2026-10-17, restated at A39 §2C
  and A40 §3.4, from A33's "irreducible conflict" and "manufactured
  frustration". With Φ the best achievable worst shortfall and Γ the
  actual update's excess over it ([CLAIM-365](CLAIM-365.md)), structural frustration
  is Φ > 0 and realization failure is Φ ≤ 0 with the actual update
  failing. Governance-induced frustration is realization failure caused
  by the allocation of influence, which Γ alone does not show. Equal loss
  curves can hide either kind. A35: "Importantly, these dual multipliers
  are not endorsement weights." The sharp edge: the distinction is
  relative to the declared demands, the admissible set and the comparison
  solver, and it says nothing yet about whether real organizations fail
  by governance.
---
<!-- inactive-ok-file: TERM-060 — Superseded; named in the version 2 history as the term this claim moved from -->

# CLAIM-357: An organization's failure to meet its demands is structural when no admissible transformation meets them all and a realization failure when an acceptable one exists and is not made effective, and governance-induced frustration is the part of realization failure due to the organization of influence, authority or selection, not to information, search, modelling or chance; aggregate performance does not tell structural from realization failure, and the multipliers that certify infeasibility are not the weights governance assigns

<!-- ref::uses-file: TERM-tmp9p3s9 — structural frustration and realization failure, with its governance-induced part, are the cases the term distinguishes -->

## The claim

A33 §8 drew the line first: "Irreducible conflict exists when the
objective demands cannot be jointly improved under the relevant admissible
actions. Manufactured frustration exists when a common improvement is
available, but the governance rule, restricted representation, or
allocation of influence prevents the system from finding or using it."
"This is testable with an oracle or stronger solver for the same declared
objectives and update constraints."

[CLAIM-365](CLAIM-365.md) makes it exact for the local model. Let Φ be the smallest
worst-case shortfall of the declared improvements over the admissible set,
and Γ = max_i(ε_i + g_iᵀd^actual) − Φ ≥ 0 the excess of the update the
organization actually makes.

- **Structural:** Φ > 0. No admissible update meets all demands. A35 §3.3
  separates a **capacity-limited** case, where Φ_r > 0 for the current
  budget r but not for a larger one, from the case where no budget helps,
  as in [CASE-115](../cases.d/CASE-115.md), where Φ_r = ε for every r.
- **Realization failure:** Φ ≤ 0, and the actual update fails some
  demand, so Γ > −Φ ≥ 0. A satisfactory update exists and is not
  realized. A35: "A system could therefore have substantial observed
  frustration even when structural frustration is absent."
- **Governance-induced:** a realization failure whose cause is the
  organization of effective influence, authority or selection. Γ > 0
  does not say this by itself. A satisfactory update can also go
  unrealized through incomplete information, unsuccessful search, a
  poorly calibrated model or an unexpected event. A broad enough notion of
  governance may cover those, but the claim does not assume it does. The
  first filing equated realization failure with governance-induced
  frustration; the owner's third review separated them
  ([TERM-tmp9p3s9](../terms.d/TERM-tmp9p3s9.md)).

A40 §3.4 added a **representational** kind, where an available solution
is inaccessible to the organization's own models or search, and said the
categories "may overlap". A representational failure is a realization failure; whether it
is governance-induced depends on whether the organization's allocation of
influence is what keeps the solution out of reach.

**Aggregate performance does not separate them.** A35 §3.4: two systems,
one with Φ_r > 0, one with Φ_r < 0 and an optimizer that repeatedly
picks an unhelpful direction, "should not receive the same diagnosis
simply because their loss curves look equally poor". The same holds of a
zero aggregate gradient ([CLAIM-351](CLAIM-351.md)).

**The certificate's multipliers are not governance's weights.** The λ
that attains the dual of Φ picks out the combination of demands that
binds. A35: "Importantly, these dual multipliers are not endorsement
weights. They are mathematical certificates of difficulty or
infeasibility." A40 §4: "The weights assigned by actual governance need
not coincide with the multipliers", and the divergence "is a candidate
source of avoidable frustration". Whether they coincide is
[QUESTION-126](../questions.d/QUESTION-126.md).

## Why the record holds it

It is where the frustration account meets the operator model. [CLAIM-297](CLAIM-297.md)
says authority updated on the interpretation it helped make dominant can
amplify without gaining fidelity; [CLAIM-330](CLAIM-330.md) gives the instability
threshold βγ > (1 − α)(1 − δ) in [CASE-099](../cases.d/CASE-099.md)'s linearization; [CLAIM-342](CLAIM-342.md) says
what keeps such a loop honest is evidence that does not pass through the
interpretation it tests. A loop of that kind is a mechanism of
governance-induced frustration: the satisfactory update exists and the
captured allocation of influence does not choose it. A39's case study 2,
[CASE-099](../cases.d/CASE-099.md) with demands and a feasible-update oracle, would test it; A39
called it "the best candidate for an early discriminating experiment".

## What it does not say

- **That governance-induced frustration occurs in any real organization.**
  The claim gives the distinction and the measure, not an instance, and
  Γ measures realization failure, not its cause: telling a governance
  cause from a search or information failure needs an intervention on the
  allocation of influence with the search held fixed. The
  defeater is the result that would make the category idle.
- **That Γ is free of choices.** Φ is relative to declared demands and a
  declared admissible set, and computing it needs a solver that finds the
  minimum: an estimate from a weaker solver overstates Φ and understates
  Γ. A wider admissible set can turn structural into governance-induced.
- **That governance-induced is worse.** It says a better update existed by
  the declared standard. Whether the declared standard is the
  organization's own is [QUESTION-087](../questions.d/QUESTION-087.md)'s problem.
- **That λ should be the weights.** Governance may rightly weight demands
  by what matters, not by what binds.
