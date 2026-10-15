---
number: 285
status: Proposed
formerly:
- CLAIM-tmpxuigm
title: 'An endorsement scheme can deny each operator control over its own authority and still reward it for delegating, because the authority an operator holds and how far its preferred policies are realized are different quantities'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A result showing that, for every aggregation rule that lets endorsement
  carry authority further than one hop, an operator that delegates in order
  to get its preferred policies realized thereby regains control over its
  own authority, so that the two conditions cannot be held together except
  by forbidding multi-hop delegation. Or a population model in which
  operators bound by the constraint stop delegating, or delegate no better
  than at random, so that the incentive the claim names does no work.
tags:
- self-governance
- social-ontology
date: '2026-10-13'
answers:
- QUESTION-090
works:
- self-as-recursive-ecology
line:
- distributed-agency
rests_on:
- CLAIM-282
uses:
- TERM-053
summary: >-
  The owner's design at U2 of the 2026-10-13 exchange: operators vote on
  one another's influence, cannot significantly manipulate their own, and
  gain by finding aligned operators and delegating authority to them. A2
  made it precise. Two conditions are imposed: each operator's own
  authority is insensitive to its own endorsements, and its payoff is how
  closely the collective decision matches what it would endorse. Under
  them, empowering a better-placed ally is a way to get one's policies
  realized without becoming more powerful. It does not say such schemes
  resist collusion, or that alignment makes delegation wise.
illustrated_by:
- CASE-079
- CASE-080
complements:
- CLAIM-272
- CLAIM-281
---
<!-- inactive-ok-file: THEORY-029 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# CLAIM-285: An endorsement scheme can deny each operator control over its own authority and still reward it for delegating, because the authority an operator holds and how far its preferred policies are realized are different quantities

## The claim

The owner, at U2: "dual to the 'meaning' canvas, we have an 'influence'
canvas that allows the denoising functions to essentially vote on how much
influence the other denoisers contribute to the decision making process.
this should be conditioned such that denoisers can't significantly
manipulate their own local influence, and are incentivized to identify
other agents with aligned policies who functionally amplify their own
influence by delegating authority to them."

A2 stated the two conditions. The first is that an operator's effective
authority g_i should not respond to its own outgoing endorsements:
|∂g_i/∂E_ij| ≈ 0 for every j ≠ i. The second is that its objective is
J_i = E[Q_i(a*, c)] − λ_i Cost(E_i), its evaluation of the collective
decision a*, not the authority it holds. A2 §6: "Consequently, denoiser i
may rationally endorse j even when doing so reduces i's direct control,
provided that j's increased authority makes the collective policy more
consistent with i's preferences." And, boxed: "Own influence ≠ Capacity to
realize one's preferred policies."

The two conditions are compatible because they constrain different
quantities. The first fixes how authority is computed. The second fixes
what an operator is rewarded for. An operator can raise J_i by moving its
endorsements toward an ally, because the move changes a* through the ally's
authority. It cannot raise its own g_i that way. Whether a given rule meets
the first condition is the subject of [CLAIM-282](CLAIM-282.md): one-hop allocation within
a governance epoch meets it exactly, and recursive delegation does not.
Endorsement here is any effect on another operator's share of future
influence ([TERM-053](../terms.d/TERM-053.md)), and explicit voting is one case of it.

A3 carried the idea through a case. A skeptical operator opposes an
emerging consensus but cannot overturn it. It endorses a third operator that
can generate alternative hypotheses. "The population can become more
epistemically robust precisely because a dissenting operator successfully
delegates authority to a different operator."

## What it does not say

- It does not say alignment makes delegation good. A2 §6: "A highly aligned
  but incompetent agent can worsen collective outcomes."
- It does not say the scheme resists collusion. A2 §6 again: "optimizing
  short-term policy realization alone can incentivize collusion, coalition
  formation, or systematic suppression of dissent." An operator can still
  change its own authority by moving others' endorsements, which is social
  feedback and not an accounting loop ([CLAIM-282](CLAIM-282.md)).
- It does not say this is how a person's processes are actually governed.
  It is a design for a model.
- It does not answer [QUESTION-054](../questions.d/QUESTION-054.md). It is one way governance could be "the
  interaction of the regimes themselves", and it shows that this needs an
  aggregation rule no regime controls. The rule is a fixed part of the
  architecture. Whether that rule is itself a governing level is the open
  question.
- The idea of endorsing an operator's role and not its conclusions (A2 §8),
  and of endorsing its judgement about whom to trust (A2 §9, "third-order
  endorsement"), is not filed. [THEORY-029](../theory.d/THEORY-029.md)'s regress is a warning against
  expecting authority to come from the order of an endorsement alone.
