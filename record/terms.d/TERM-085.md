---
number: 85
status: Active
formerly:
- TERM-tmpsuzzj
title: 'correctability, of an institutional arrangement for a corrective objective: the chance that the arrangement, starting from the description of the problem it actually has, finds, authorizes, coordinates and carries out a plan achieving the objective before the deadline and within its resources'
version: 2
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
used_by:
- CLAIM-462

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
problem it actually has" to legibility (TERM-064). Suppose two equally
likely failures need remedies that exclude each other, and the
description the arrangement corrects from has laws P₀ and P₁ under them.
Then no remedy, actuator or decision rule acting on that description picks
the right remedy with probability above (1 + TV(P₀, P₁))/2. It is ½ when
the description is the same under both. This is the two-point Bayes-risk
identity of Le Cam, the record's CLAIM-199 and CLAIM-503 applied to
correction, and it is not filed as a new claim. Its use: "no improvement
in the downstream corrective mechanism can recover that lost distinction
from those observations alone". A25's reading of CASE-154 is corrected.
That case restricts the observer to one coordinate, not the
representation to one bit. A25's table of correction stages extends
CLAIM-403's rungs for a contributor; CLAIM-349's split of access,
authority and action is the version for an organization's own signals. A
corrected judgment need not be a corrected organization. In CASE-124's
model, resetting the interpretation's state while its residue r₀ ≠ 0
remains regrows it at the next step (m₁ = ν·r₀), which then decays at the
slow rate (CLAIM-400).
