---
status: Proposed
title: 'Invoking a relationship differs from reusing a stored result in that the invocation can change the relationship it invokes, so one operation can reproduce, form or transform a contract, and a stored-work cost model that holds the store fixed between uses prices a contract''s lifecycle but not its invocation, which returns an act, a distribution of costs over the parties and the relationship''s next state'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that every effect an invocation has on a relationship is
  already priced by the stored-work model's existing terms with the store
  held fixed between uses (staleness, erosion and revision as exogenous
  rates), so that two relationships of matched per-use cost and output
  never part in later cost because of what their invocations did to them;
  or that composing the dispositional and stored-work entries this rests on
  gives no prediction beyond existing models of co-adaptation and
  coordination, so that "relational invocation" is only a vocabulary (A32
  §21's own defeater).
tags:
- operations-research
- society-and-governance
- complex-systems
date: '2026-11-24'
line:
- realizability
- dependence-and-domination
- formal-apparatus
rests_on:
- CLAIM-761
- CLAIM-569
- CLAIM-1156
bears_on:
- QUESTION-tmpb7fx7
uses:
- TERM-114
summary: >-
  A30 §§7, 8 and 16 and A32 §§14, 18, 19 and 21 of the exchange 'Memes,
  Contracts, and Systemic Normativity' (ChatGPT, 2026-11-24), at the owner's
  U21 and U22. "A cached result normally substitutes for a computation
  without intentionally changing the underlying problem. Contracts can
  change the problem." Invoke(q, C_t) → (a_t, C_{t+1}); A32 writes the
  relational kernel K_C(q) = Law(a, τ, κ, C′, S′ | do(q), C, S), extending
  [CLAIM-1156](CLAIM-1156.md)'s, and names reproductive, formative and transformative
  invocation. [ARG-tmpa5ped](../arguments.d/ARG-tmpa5ped.md) says what [CASE-326](../cases.d/CASE-326.md) prices; [LEAD-tmp14n26](../leads.d/LEAD-tmp14n26.md) is the
  test. The wording is A's (ChatGPT, in the exchange 'Memes, Contracts, and
  Systemic Normativity'); adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmpa5ped CASE-326 CLAIM-891 CLAIM-1095 CLAIM-1156 TERM-116 — Proposed or new; this filing's entries and the held entries it maps to, cited with their standing -->

# CLAIM-tmpsf9hp: Invoking a relationship differs from reusing a stored result in that the invocation can change the relationship it invokes, so one operation can reproduce, form or transform a contract, and a stored-work cost model that holds the store fixed between uses prices a contract's lifecycle but not its invocation, which returns an act, a distribution of costs over the parties and the relationship's next state

## The claim

A30 §7: "A cached result normally substitutes for a computation without
intentionally changing the underlying problem. Contracts can change the
problem. Every time a relationship is invoked, its participants may update
their expectations, alter their capacities, acquire obligations or revise
their understanding of its scope." It writes invocation as stateful,

    Invoke(q, C_t) → (a_t, C_{t+1}),   C_{t+1} = Φ(C_t, q_t, a_t, f_t),

with f_t the interaction's consequences and the parties' responses, and
lists effects: fulfilment strengthens expectations, repeated accommodation
expands practical jurisdiction, an accepted exception adds suspension
conditions, an unchallenged deviation can weaken a norm, repeated reliance
transforms future alternatives. "None of these effects follows
automatically ... The point is that invocation should be permitted to have
these effects in the model."

A32 §14 finds the kernel in [CLAIM-1156](CLAIM-1156.md), K_S(q) = Law(a, τ, c, S′ |
do(q), S), "almost precisely the extension", and makes the relationship
and the cost distribution explicit:

    K_C(q) = Law(a, τ, κ, C′, S′ | do(q), C, S),

with κ "the distribution of costs among the participating processes".
"Two relationships might produce the same ordinary responses at the same
immediate cost while differing in what those responses do to their
subsequent organization." Following [CLAIM-1095](CLAIM-1095.md), the comparison is made
on later response distributions under further probes, not on internal
post-states.

A32 §19 divides the one operation by its effect: reproductive invocation
"Exercises and maintains an existing relationship"; formative
"Participates in establishing a previously unformed relationship";
transformative "Modifies the specification or governance of an existing
relationship". "A single interaction can instantiate all three", so the
line between contracting and performing a contract can "emerge from the
relative magnitude and character of the relational changes induced by
interaction", and a run of formative invocations can cross a nucleation
threshold after which ordinary interaction is reproductive.

What the model therefore needs (A30 §§11 and 15): a contract as a
distinguished part of [TERM-114](../terms.d/TERM-114.md)'s architecture, not a new primitive;
costed Form, Maintain, Invoke, Verify, Repair, Revise and Exit, each
indexed by who bears it; and, as A30 says, "the critical test is whether
these require genuinely new cost terms, or merely richer state variables
and transition mechanisms within the existing model. I suspect the latter
will cover most of the cases."

## Admission

From A30 §16's and A32 §21's candidate syntheses, by a discriminating
prediction ([ADR-075](../decisions.d/ADR-075.md)): two relationships matched in per-use cost and output
under [CASE-326](../cases.d/CASE-326.md)'s terms part in their later costs, response and exit
profiles when one's invocations change it and the other's do not. The
components ([CLAIM-761](CLAIM-761.md), [CLAIM-569](CLAIM-569.md), [CLAIM-1156](CLAIM-1156.md)) leave open whether a
contract's store changes with use; this claim says it can and that the
pricing then differs. [LEAD-tmp14n26](../leads.d/LEAD-tmp14n26.md) would test it.

## Where the record stands

- [CLAIM-761](CLAIM-761.md) and [CLAIM-569](CLAIM-569.md) give the lifecycle; [CASE-326](../cases.d/CASE-326.md) and [CLAIM-891](CLAIM-891.md) price
  it with the store fixed between uses ([ARG-tmpa5ped](../arguments.d/ARG-tmpa5ped.md)).
- [CLAIM-1156](CLAIM-1156.md) holds that the same answers can differ in what answering
  does; this claim locates the change in the invoked relationship.
- [TERM-116](../terms.d/TERM-116.md) makes the revision cost directed, R(C, C′) ≠ R(C′, C), which A30
  §8 uses: "A relationship may be easy to enter, inexpensive to maintain and
  extremely expensive to leave."
- Implicit contracts and their formation were introduced earlier in the
  exchange (U14, U16); this claim adds their invocation.

## What it does not say

It does not say every invocation changes the relationship, nor that a
separate contract theory is needed: both A30 and A32 lean the other way.
It does not say what the right update rule Φ is.

## Standing

Proposed, in A's voice.
