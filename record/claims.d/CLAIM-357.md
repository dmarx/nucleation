---
number: 357
status: Active
formerly:
- CLAIM-tmpl8vsy
title: 'The frustration residual and governance regret separate structural infeasibility, realized violation and minimax suboptimality, and identify none of them as thwarting: a positive residual says no admissible update meets every declared requirement, a positive regret only that the actual update''s worst residual exceeds the best achievable, which can hold while every requirement is met, and actual violation needs regret above the negative residual; aggregate performance does not tell infeasibility from realized violation, and the multipliers that certify infeasibility need not be the weights governance assigns'
version: 5
history:
- version: 2
  date: '2026-10-18'
  note: >-
    Retitled at the reviews relayed by the owner on 2026-10-18. Φ, realized
    violation (m(d_actual) > 0, equivalently Γ > −Φ when Φ ≤ 0) and Γ are
    distinguished, with a counterexample in which Γ > 0 while every
    requirement is met. None of them establishes thwarting or a governance
    cause; governance-induced frustration is narrowed to shortfall the
    allocation of influence is shown to cause.
- version: 3
  date: '2026-10-25'
  note: >-
    A dated note added: Blackwell approachability as the repeated version of
    the worst residual, and the cost of averaging. The claim is unchanged.
- version: 4
  date: '2026-10-25'
  note: >-
    The note of 2026-10-25 checked against the reading of Kwon and Perchet
    (NOTE-1159): their target is exactly this claim's set and their
    distance the ℓ₂ norm of the positive parts of the average, so the
    caution about averaging is made exact. The claim is unchanged.
- version: 5
  date: '2026-10-30'
  note: >-
    Promoted to Active at the eighteenth status review (ADR-057), at the
    status review's ruling (the owner delegated these rulings). Its
    premises CLAIM-365 and CLAIM-368 and its term TERM-060 are Active, and
    no objection is filed. The formal clauses were re-derived
    (p18/cluster_da_checks.py): the counterexample, the identity
    m(d_actual) > 0 iff Γ > −Φ for Φ ≤ 0, and two systems with equal worst
    and mean residuals and opposite Φ. "Are not the weights governance
    assigns" narrowed to "need not be", as A40 says (ADR-047 kind 3). The
    defeat condition attacked the governance-induced category, which
    version 2 of the title no longer asserts. It is restated against the
    title. The old condition read: "A showing that every failure of actual
    updates to meet satisfiable demands is explained by known optimization
    mechanisms (step size, curvature, noise, conditioning, a fixed
    weighting rule) without modelling endorsement or the allocation of
    authority, so that the governance-induced category adds nothing an
    optimizer analysis does not already give. Not defeated by the formal
    facts that Γ ≥ 0 and that Φ certifies infeasibility, which it rests on,
    nor by cases where the two kinds occur together." That thesis, the
    record's own, is filed as CLAIM-tmp4u6xx (ADR-047 kind 2) with the old
    condition.
role: thesis
warrant: interpretive
defeated_if: >-
  An error in the distinctions: demands and an admissible set with Φ > 0
  under which some admissible update meets every declared requirement;
  with Φ ≤ 0, an actual update that violates a requirement while Γ ≤ −Φ,
  or meets every one while Γ > −Φ; or two systems that differ in whether
  Φ > 0 and cannot share every aggregate measure of performance. Or a
  showing that Φ or Γ, without an intervention on the allocation of
  influence, identifies the process that kept an update from being made.
  Not defeated by cases where the kinds occur together.
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
- TERM-060
summary: >-
  A34 §4 and A35 §3.3 of the exchange of 2026-10-17, restated at A39 §2C
  and A40 §3.4, from A33's "irreducible conflict" and "manufactured
  frustration". With m(d) the worst residual, Φ its minimum and Γ the
  actual update's excess over Φ ([CLAIM-365](CLAIM-365.md)): Φ > 0 is structural
  infeasibility; when Φ ≤ 0 the actual update violates a requirement
  exactly when Γ > −Φ. Positive governance regret establishes excess
  worst-case shortfall relative to the optimum, and can hold while every
  requirement is met. Neither quantity identifies an obstructing
  mechanism, a governance failure or active thwarting; governance-induced
  frustration needs an argument or intervention showing the allocation of
  influence responsible. A35: "Importantly, these dual multipliers are not
  endorsement weights."
---
<!-- inactive-ok-file: THEORY-947 — Proposed; Kwon and Perchet's rates as the paper states them, cited in the note of 2026-10-25 for the target and distance, nothing here rests on it -->

# CLAIM-357: The frustration residual and governance regret separate structural infeasibility, realized violation and minimax suboptimality, and identify none of them as thwarting: a positive residual says no admissible update meets every declared requirement, a positive regret only that the actual update's worst residual exceeds the best achievable, which can hold while every requirement is met, and actual violation needs regret above the negative residual; aggregate performance does not tell infeasibility from realized violation, and the multipliers that certify infeasibility need not be the weights governance assigns

<!-- ref::uses-file: TERM-060 — the diagnostics are stated against the term's structural and governance-induced cases, which this claim narrows -->

## The claim

A33 §8 drew the line first: "Irreducible conflict exists when the
objective demands cannot be jointly improved under the relevant admissible
actions. Manufactured frustration exists when a common improvement is
available, but the governance rule, restricted representation, or
allocation of influence prevents the system from finding or using it."
"This is testable with an oracle or stronger solver for the same declared
objectives and update constraints."

[CLAIM-365](CLAIM-365.md) makes it exact for the local model. Demand i requires
ε_i + g_iᵀd ≤ 0 of an update d. Define the worst residual of an update,
the frustration residual and the governance regret:

  m(d) = max_i(ε_i + g_iᵀd),  Φ = min_{d∈U} m(d),
  Γ = m(d_actual) − Φ ≥ 0.

- **Structural:** Φ > 0. No admissible update meets all demands. A35 §3.3
  separates a **capacity-limited** case, where Φ_r > 0 for the current
  budget r but not for a larger one, from the case where no budget helps,
  as in [CASE-115](../cases.d/CASE-115.md), where Φ_r = ε for every r.
- **Realized violation:** Φ ≤ 0, so a jointly satisfactory update
  exists, and the actual update violates at least one requirement. That
  holds exactly when m(d_actual) > 0, equivalently Γ > −Φ. The actual
  update meets every requirement exactly when m(d_actual) ≤ 0,
  equivalently Γ ≤ −Φ. A35: "A system could therefore have substantial
  observed frustration even when structural frustration is absent."

**Positive regret is not failed satisfaction.** Γ measures how much worse
the actual update's worst-case residual is than the best achievable one.
It can be positive when the actual update meets every declared
requirement. Take one demand with ε = 1 and g = 1, and admissible updates
U = [−2, 0]. Then m(d) = 1 + d, Φ = −1 at d = −2. The actual update
d = −1 has residual m(−1) = 0, so it meets the requirement, yet Γ = 1 > 0
because a more favourable update was available. Γ > 0 establishes
suboptimality relative to the chosen minimax objective, not that any
requirement went unmet. Actual violation needs the further comparison
Γ > −Φ when Φ ≤ 0. Four claims are kept apart: structural infeasibility
(Φ > 0), realized violation (m(d_actual) > 0), minimax suboptimality
(Γ > 0), and causal governance failure, which neither quantity
identifies.

**What the diagnostics do not show.** The first filing called the second
case governance-induced frustration. It is not, by itself. Neither Φ nor
Γ identifies an obstructing mechanism, a governance failure or active
thwarting. An available update can go
unmade because no process pursued it, because it was not recognized,
through error, or through an unexpected event. None of these requires
anything to have blocked it. Γ does not say whether a demand was actively
thwarted, which process did it, or whether the demand was legitimately
subordinate to another. Governance-induced shortfall is the case where
the allocation of influence is what kept the update from being made, and
showing that needs an intervention on the allocation with search and
information held fixed. Φ > 0 is structural frustration of the declared
improvement demands in [CLAIM-347](CLAIM-347.md)'s sense. How a realized violation
relates to operative thwarting is [QUESTION-131](../questions.d/QUESTION-131.md)'s question.

A40 §3.4 added a **representational** kind, where an available solution
is inaccessible to the organization's own models or search, and said the
categories "may overlap".

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
That the governance-induced kind does work an optimizer analysis does not
is filed apart as [CLAIM-tmp4u6xx](CLAIM-tmp4u6xx.md).

## What it does not say

- **That governance-induced frustration occurs in any real organization.**
  The claim gives the distinction and the measure, not an instance. The
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

## Note of 2026-10-25: the repeated version, and what averaging costs

From A29–A31 of the exchange of 2026-10-24, continued. This claim's worst
residual m(d) = maxᵢ(εᵢ + gᵢᵀd) is a one-shot test against the target set
{z : zᵢ ≤ 0 for every i}. Blackwell approachability asks the repeated
version: whether a learner can drive dist((1/T)Σ f_t, C) → 0 for a vector
of demand residuals f_t against disturbance or opposition. Kwon and Perchet
(2017, [LIT-1526](../literature.d/LIT-1526.md), read in [NOTE-1159](../notes.d/NOTE-1159.md)) treat it under partial feedback.
Their target is exactly this claim's {z : zᵢ ≤ 0}, and the distance they
use is ‖(ḡ_T)₊‖₂, the ℓ₂ norm of the positive parts of the average
([THEORY-947](../theory.d/THEORY-947.md)). A requirement violated by 1 on alternate stages and met
by 1 on the others has average 0 and is approached perfectly.
Two cautions from the replies. First, averaging is compensatory:
"violating a safety requirement today may not be remedied by outperforming
it tomorrow" (A30), and a rolling-window requirement "is stronger than
merely achieving a suitable long-run average and is not directly
guaranteed by ordinary approachability results" (A31). Second, "measuring
*distance* to the acceptable set introduces choices of normalization and
geometry" (A30), a scale this claim does not otherwise need.
Approachability is already in the record as the engine of Hart and
Mas-Colell's proof ([NOTE-1142](../notes.d/NOTE-1142.md)): regret matching is approachability of
the negative orthant by the regret vector. The claim is unchanged.
