---
number: 85
status: Active
formerly:
- TERM-tmpsuzzj
title: 'correctability, of an institutional arrangement for a corrective objective: the chance that the arrangement, starting from the description of the problem it actually has, finds, authorizes, coordinates and carries out a plan achieving the objective before the deadline and within its resources'
version: 4
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Adopted at the twelfth status review (ADR-057), on the owner's
    ruling in the pull request, as a term of its own rather than a
    note widening TERM-055: it carries TERM-055 from a resource to a
    corrective objective, from an agent to an arrangement with no one
    in charge, and from a cue to the description of the problem, and
    six entries cite it. A paragraph, "Whose correctability", is
    added: the title reads the arrangement as what is corrected and
    the definition as what corrects, and G is now stated to hold both.
    CLAIM-464 is dropped from used_by; its measure is a least cost,
    which this term calls a separate question. The definition of the
    chance is unchanged.
- version: 3
  date: '2026-11-17'
  note: >-
    A dated note: A64 of the exchange "Assess Depp Heard Abuse"
    restricts the term to a claimant's own policies, requires relief
    before the claimant's resources run out, and first states a worst-
    case adversarial version with a vulnerability gap whose sign the
    definition does not fix. No other change. A dated note: A85 §7 of
    the exchange "Assess Depp Heard Abuse" sets a preventive-security
    quantity beside the term's correction. No other change.
- version: 4
  date: '2026-11-17'
  note: >-
    Correction from Shue's Basic Rights, skimmed: Shue's correlative
    duties are avoidance, protection and aid; "respect, protect and
    fulfil" is the UN treaty bodies' later wording.
tags:
- society-and-governance
- agency
- operations-research
date: '2026-10-27'
line: distributed-agency
complements:
- TERM-055
summary: >-
  A10's α_J, from the exchange of 2026-10-26, on the owner's U10 tying the
  "correctability frontier" to "if I can't find it, it isn't there". It is
  [TERM-055](TERM-055.md)'s operational availability with a corrective objective in
  place of a resource and an institutional arrangement in place of an
  agent: search, authorization, coordination and execution compete for
  the same time. Named because the exchange used the object in four turns (A7 to A10)
  under "remedial reach", "effective remedial capacity", "effective
  answerability" and "correctability frontier". Adopted 2026-10-29.

---

# TERM-085: correctability, of an institutional arrangement for a corrective objective: the chance that the arrangement, starting from the description of the problem it actually has, finds, authorizes, coordinates and carries out a plan achieving the objective before the deadline and within its resources

## Definition

A10: for a state s, a corrective objective J, remaining time H, budget
B, the description or cue q under which correction is sought, and the
institutional arrangement G,

α_J(s, q, H, B; G) = sup over π in Π(G, q, B) of Pr_s^π(T_J ≤ H),

where Π is the set of search-and-action policies available to the
arrangement and T_J the time J is achieved. "The search and implementation
procedures belong to the same policy. Planning is not free." The
correctability set at reliability 1 − δ is the set of objectives J with
α_J ≥ 1 − δ, and its boundary is A9's "correctability frontier", relative
to the declared time, resources, information, arrangement and reliability.

It is [TERM-055](TERM-055.md) carried over, item for item: the resource becomes a plan
for J, the agent–environment system becomes an arrangement of institutions,
the cue becomes the description under which the problem reaches them. A10
decomposed the time as discovery, verification, coordination and
execution, which overlap and compete, so "A sufficiently long search can
make an otherwise available remedy unusable", and further search can have
negative value.

[TERM-055](TERM-055.md)'s two notes carry over too. Hutchins's cockpit ([LIT-1066](../literature.d/LIT-1066.md)):
preparation moves the cost of search ahead of the deadline, and A10's
"precomputed search infrastructure" is custody records, standing channels
for executing orders and clear escalation, maintained beforehand. And the
supremum is the best available policy, not the one used; A10's three
levels are oracle feasibility, bounded-optimal capability and realized
organizational competence.

**Whose correctability.** G is the arrangement through which correction is
sought: the institutions that would find, authorize and carry out the plan,
and the one whose act or state J would correct. The correctability of an
arrangement is its capacity to correct a state of itself through its parts.
When a claim speaks of one institution's being correctable by others
([CLAIM-462](../claims.d/CLAIM-462.md)), G is the arrangement that holds both, and J a correction of the
first.

## What it is not

- **A remedy's existence, or its legality.** A10's four propositions,
  existence, knowability, findability and deployability, of which this is
  the last; [QUESTION-279](../questions.d/QUESTION-279.md) asks what would certify that it is zero.
- **Contestability.** A9 separated formal contestability (one is entitled
  to challenge), practical contestability (one can start and sustain a
  challenge) and effective answerability (the challenge can constrain or
  correct the exercise of authority), after Pettit ([LIT-1614](../literature.d/LIT-1614.md)).
  Correctability is about the last, and says nothing about the first two.
- **A score.** A9: "The relevant object is a structured attainable set, not
  a single accountability score." Costs of time, money, risk and lost
  capability are kept apart.
- **Exogenous.** A10: "the budget is itself partly an outcome of political
  and organizational decisions", so (B, G) evolve with the arrangement's own
  acts. The term measures what can be corrected now; how the arrangement
  came to have that capacity is a separate, historical question ([CLAIM-464](../claims.d/CLAIM-464.md)).
- **A unified agent's property.** The arrangement may span courts,
  agencies, enforcers and foreign governments with no one of them in
  charge, and coalitions can do what no member can ([CLAIM-457](../claims.d/CLAIM-457.md)).

A10 itself advised against "an entirely new TERM called *resource-bounded
availability*", since [TERM-055](TERM-055.md) "already covers the underlying concept",
and proposed questions instead. The term is filed anyway because the
object recurred under four names in A7 to A10 and the claims filed from
them need one; whether it should instead be a note widening [TERM-055](TERM-055.md)
is the owner's call.

## Note of 2026-10-31: correctability is bounded by legibility

At U25 of the exchange "Analyze nucleation concepts" the owner suggested
connecting corrigibility with the record's treatment of legibility. A25
gave the bound that ties this term's "starting from the description of the
problem it actually has" to legibility ([TERM-064](TERM-064.md)). Suppose two equally
likely failures need remedies that exclude each other, and the
description the arrangement corrects from has laws P₀ and P₁ under them.
Then no remedy, actuator or decision rule acting on that description picks
the right remedy with probability above (1 + TV(P₀, P₁))/2. It is ½ when
the description is the same under both. This is the two-point Bayes-risk
identity of Le Cam, the record's [CLAIM-199](../claims.d/CLAIM-199.md) and [CLAIM-503](../claims.d/CLAIM-503.md) applied to
correction, and it is not filed as a new claim. Its use: "no improvement
in the downstream corrective mechanism can recover that lost distinction
from those observations alone". A25's reading of [CASE-154](../cases.d/CASE-154.md) is corrected.
That case restricts the observer to one coordinate, not the
representation to one bit. A25's table of correction stages extends
[CLAIM-403](../claims.d/CLAIM-403.md)'s rungs for a contributor; [CLAIM-349](../claims.d/CLAIM-349.md)'s split of access,
authority and action is the version for an organization's own signals. A
corrected judgment need not be a corrected organization. In [CASE-124](../cases.d/CASE-124.md)'s
model, resetting the interpretation's state while its residue r₀ ≠ 0
remains regrows it at the next step (m₁ = ν·r₀), which then decays at the
slow rate ([CLAIM-400](../claims.d/CLAIM-400.md)).

## Note of 2026-11-12: the term adopted as an outcome measure, and read correctly, from "luria experiment design"

A34, A36, A39 and A45 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) make this term the integrating outcome of
the proposed evaluations of the record: whether a team achieves the
justified objective within its deadline and resources. A36 reads
the definition correctly and marks the gap between it and any study: the
measured rate "estimates the success rate of the *tested policy*, not
Nucleation's supremum over every possible policy", and "The outcome is
meaningful only if the correction objective is specified independently of
the system's own judgments." A36's funnel, detected, diagnosed, selected,
authorized, executed, verified, follows the term's finds, authorizes,
coordinates and carries out, with diagnosis and verification added as
stages. The definition is unchanged.

## Note of 2026-11-17: the claimant's correctability, sustained to relief, against an adversary, from "Assess Depp Heard Abuse"
<!-- inactive-ok-file: CLAIM-tmpyo35b CASE-tmphljcr CLAIM-tmpbqunx — filed from the exchange "Assess Depp Heard Abuse" on 2026-11-17, Proposed -->

A64 of the exchange "Assess Depp Heard Abuse" (https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b, 2026-11-16), formalizing the owner's U28 on litigation as siege ([CLAIM-tmpyo35b](../claims.d/CLAIM-tmpyo35b.md)), relays this term faithfully and adapts it twice. A64 §1 restricts the policies to the claimant's: α_J^B(s, q, H, K; G) = sup over π_B in Π_B(G, q, K) of Pr(T_J ≤ H), "restricted to the claimant's available litigation and enforcement strategies", renaming the budget K to free B for the claimant. A64 §9 adds an opponent and a survival condition: α̲_J = inf over u_A in 𝒰_A^adm of sup over π_B in Π_B(u_A) of Pr(T_J ≤ H, T_J < τ_B(u_A)), "the most obstructive opposing strategy within the specified set", with A's caution that it is "**not automatically a game-theoretic equilibrium**".

The second condition matters for this term's own limits. The term says it is about effective answerability and "says nothing about" formal or practical contestability, practical contestability being that "one can start and sustain a challenge". Requiring relief before the claimant's exhaustion time τ_B brings sustaining a challenge inside the measure. A64 §9 also defines a "contestability vulnerability gap", α_J^baseline − α̲_J, read as positive. It is nonnegative only if the baseline course is among the opponent's admissible strategies; as defined the baseline is a procedure, so the sign is not fixed (corrected in [CASE-tmphljcr](../cases.d/CASE-tmphljcr.md)). The robust quantity is filed, from A76 and A81, as [CLAIM-tmpbqunx](../claims.d/CLAIM-tmpbqunx.md) (F4), which fixes the order of quantifiers by what the corrector observes.

No status changes.

## Note of 2026-11-17: prevention beside correction, from "Assess Depp Heard Abuse"

A85 §7 of the exchange "Assess Depp Heard Abuse" (https://chatgpt.com/share/6afcb46d-83a8-83e9-9c85-4a0c3604405b, 2026-11-17) separates "**nonviolation**, **protection**, and **correction**" as different institutional achievements, and sets beside this term's quantity, C_r(G, s) = sup_π Pr_s^π(T_{J_r} ≤ H), a preventive one: S_r(G) = inf_σ Pr_G^σ(s_t ∉ V_r for all t ≤ H), the reliability with which an institution keeps out of the violation set V_r under a declared class of disturbances and adversarial strategies. "The distinction resembles the separation between safety and recovery in control theory." And: "**A government can recognize an inalienable right yet fail to develop or maintain the capabilities required to secure it.**"

The term covers recovery only. The record has no term for prevention; S_r is a candidate, and it is adversarial where this term is not (its robust corrective counterpart is [CLAIM-tmpbqunx](../claims.d/CLAIM-tmpbqunx.md)). A does not name the parallel in rights theory, the duties to respect, protect and fulfil (Shue's Basic Rights, 1980, and the UN treaty bodies' usage); A87 §7 later cites both. "Neither is a complete measure of justice. Some violations are irreversible, some duties are procedural rather than outcome-based".

No status changes.

## Note of 2026-11-17: Shue's triad is avoidance, protection and aid
<!-- inactive-ok-file: NOTE-tmpzchma THEORY-tmpwtcj0 — new readings and theory of 2026-11-18, Proposed or Skimmed -->

Shue, Basic Rights, skimmed ([NOTE-tmpzchma](../notes.d/NOTE-tmpzchma.md), [THEORY-tmpwtcj0](../theory.d/THEORY-tmpwtcj0.md)): the term says "the duties to respect, protect and fulfil (Shue's Basic Rights, 1980, and the UN treaty bodies' usage)". That runs two triads together. Shue's, by the book's index, is "correlative duties (of avoidance, protection and aid)", with a "tripartite analysis" at pp. 54–55 and entries "duty to aid", "to avoid deprivation", "to protect rights"; "respect, protect and fulfil" is the treaty bodies' later wording. A suggested repair: "the duties to avoid depriving, to protect and to aid (Shue, Basic Rights, 1980), and the UN treaty bodies' later duties to respect, protect and fulfil". The SEP entry "Human Rights" ([NOTE-tmp8pbdm](../notes.d/NOTE-tmp8pbdm.md)) gives a third list, "respect, protection, facilitation, and provision". Chapter 2, where Shue argues the triad, is unread, so his own wording of each duty is unconfirmed. The term's content does not depend on the attribution. No status changes.
