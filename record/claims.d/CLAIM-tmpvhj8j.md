---
status: Proposed
title: 'Where successful response requires several complementary capacities, the value of preserving one depends on whether the others remain deployable, so individual resource utilization need not track the organization''s response capability'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the stated construction: a case in which success is the
  conjunction E = C ∧ K ∧ M ∧ T, yet raising one component's probability
  raises R when another component is absent, or a component's marginal
  value is the same whatever the others' state. It is not defeated by
  organizations in which capacities substitute for one another; the
  construction assumes they are complements.
tags:
- operations-research
- complex-systems
- probabilistic-modeling
date: '2026-11-04'
line:
- distributed-agency
complements:
- CLAIM-422
- CLAIM-347
uses:
- TERM-tmpuc919
bears_on:
- QUESTION-tmpw46vw
- QUESTION-tmpmtvei
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 7 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)",
  demonstrated in a stated construction. When a response succeeds only if
  crew, proficiency, equipment and timely assembly all hold, readiness is a
  chain-rule product of conditional probabilities, and the value of
  keeping one capacity depends on the others. A: "the marginal value of a
  capability depends on the system in which it is embedded." The wording
  is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmpuc919 — Proposed or new; A's proposals of 2026-11-04 and the readings they cite, as open -->

# Where successful response requires several complementary capacities, the value of preserving one depends on whether the others remain deployable, so individual resource utilization need not track the organization's response capability

## The claim

**The construction.** An effective response is the event

  E = C ∧ K ∧ M ∧ T,

with C a qualified crew available, K knowledge and proficiency
maintained, M material resources operational, and T the response
assembled before the deadline. Readiness ([TERM-tmpuc919](../terms.d/TERM-tmpuc919.md)) is

  R = Pr(C ∩ K ∩ M ∩ T) = Pr(C) · Pr(K | C) · Pr(M | C, K) · Pr(T | C, K, M),

by the chain rule: a product of conditional probabilities, not in general
of four unconditional ones, since the capacities need not be independent.

**Complementarity.** If M is absent, Pr(M | C, K) = 0 and R = 0 whatever
K is: raising proficiency cannot produce success. If the other three hold
with high probability, raising K raises R nearly one for one, and
proficiency may be worth a great deal. So "the marginal value of a
capability depends on the system in which it is embedded."

**So** the utilization of one component, how often its crew trains or its
equipment runs, need not track R. A: "the object being produced is joint
response capability, not the activity of any single component."

[CLAIM-422](CLAIM-422.md) separates a corrective act, a procedure and a maintained
capacity; this claim adds that a maintained capacity is worth what the
capacities it works with let it deliver. [CLAIM-347](CLAIM-347.md) treats which of an
organization's demands can be satisfied together; this treats which
capacities must be present together for one demand to be met.

## What it does not say

- **Anything about organizational closure.** A asked that the reading on
  which these capacities produce one another be kept out. This is a
  conjunction at the time of response, not a claim about how the
  capacities are maintained.
- **That capacities never substitute.** Where one can stand in for
  another, success is not a pure conjunction and the result changes.
- **How much any capacity is worth.** It says the value is conditional,
  not what it is.
