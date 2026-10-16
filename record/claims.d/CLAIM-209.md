---
number: 209
status: Proposed
formerly:
- CLAIM-tmp7gigk
title: 'Probes and statistical models recover only the distinctions identifiable from the relational evidence they are given, and a signature sufficient for a stated family of communicative decisions outside the observed probes can be identified when the full latent factorization is not'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  For the multi-view, context-indexed observation systems the line uses,
  it is shown that no signature sufficient for a stated family of
  decisions outside the observed probes is identified when the latent
  factorization is not; or the signatures recovered fail, on held-out
  realizations, media or languages, to predict the decisions they were
  claimed sufficient for.
tags:
- mathematical-statistics
- philosophy-of-science
date: '2026-10-10'
line:
- pragmatic-transport
- formal-apparatus
answers:
- QUESTION-027
complements:
- CLAIM-135
- CLAIM-142
- CLAIM-148
- CLAIM-193
- CLAIM-213
summary: >-
  The assistant's second thesis at U62 (A240 T2), the positive answer to
  [QUESTION-027](../questions.d/QUESTION-027.md). It has now been asserted four times: A214 §7, A218 (RQ3
  and the priority theorem target), A232 (§3.2 and F2) and A240. Filed
  with [QUESTION-027](../questions.d/QUESTION-027.md)'s scope: the unrestricted claim is answered by
  standard results, so its content is in decisions outside the observed
  probes. No signature is yet named. A proposal; the owner argued none of
  it.
---
<!-- inactive-ok-file: CLAIM-135 CLAIM-142 CLAIM-129 — Proposed; open, and cited as the negative results and restatements this thesis sits beside, not as settled -->
<!-- inactive-ok-file: CLAIM-204 CLAIM-216 CLAIM-215 — Proposed; the revised October thesis, and the entries filed with this one on 2026-10-10, open -->
<!-- inactive-ok-file: CLAIM-193 THEORY-005 THEORY-009 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

# CLAIM-209: Probes and statistical models recover only the distinctions identifiable from the relational evidence they are given, and a signature sufficient for a stated family of communicative decisions outside the observed probes can be identified when the full latent factorization is not

## The claim

A240 T2, "Restricted recoverability of relational distinctions":

> **Claim:** Observational probes and statistical models recover only those
> distinctions identifiable from their available relational evidence. A
> communicatively important signature can be recoverable and
> decision-sufficient even when the complete underlying factorization is not
> uniquely identifiable.
>
> **Status:** Mathematical research thesis; proposed.
>
> **Qualification:** Existing matrix factorization, topic-model
> identifiability, and statistical sufficiency results provide the starting
> point. The proposed contribution concerns communicative, multi-view,
> context-sensitive observational systems.
>
> **Challenge:** Show that the relevant signatures cannot be identified under
> the proposed conditions, or that apparently recovered distinctions fail to
> generalize beyond the observations used to construct them.

This is the fourth time the exchange has put it forward. A214 §7, as
[QUESTION-027](../questions.d/QUESTION-027.md) quotes it: "**decision-sufficient structure may be recoverable
even when the full underlying model is not identifiable**". A218 made it RQ3
and its priority theorem target. A232 §3.2: "Conversely, a task-sufficient
prediction may be identifiable even when the complete latent model is not."
A232's F2: "**F2 — Identifiable task-sufficient signatures:** Characterize
functions of relational models identifiable from restricted observations even
when full latent decompositions are not identifiable." The record has held it
as a question. This entry files the answer the exchange keeps giving, so that
it has a defeat condition.

## Where its content is

- **The first sentence restates held claims.** That a probe family recovers
  only what it identifies is [CLAIM-142](CLAIM-142.md) (observational equivalence is
  relative to the probes) and [CLAIM-129](CLAIM-129.md) (a factorization recovers only the
  structure visible in the relations it is fitted to). Read strictly it is
  close to a definition: a distinction not identified by the evidence is not
  recovered from it.
- **The unrestricted second sentence is already true.** [QUESTION-027](../questions.d/QUESTION-027.md): "Its
  unrestricted form is answered by standard results". Gauge-invariant
  functionals of a factorization are identified whenever the reconstruction
  is ([CLAIM-148](CLAIM-148.md)), matrix completion identifies missing entries without
  identified factors under incoherence and enough random samples, and a decision whose risk depends only on the law of the
  observed probes has an identified sufficient signature by construction. T2's
  qualification grants the starting point.
- **So the thesis is the restricted clause.** It says that, for decisions
  outside the observed probes (new probes, interventions, a target after
  transport) and for the multi-view, context-indexed systems the line uses,
  such a signature can be identified. That is what [QUESTION-027](../questions.d/QUESTION-027.md) asks, and
  what A240's "communicative, multi-view, context-sensitive observational
  systems" points at. T2's challenge, distinctions that "fail to generalize
  beyond the observations used to construct them", is the empirical half of
  the same scope.

A232 §3.2 also says how it is to be tested: "The empirical test must compare
these signatures with models fitted directly to response profiles, including
strong supervised predictive models." That comparison is the second disjunct
of [CLAIM-204](CLAIM-204.md)'s defeat condition. Here it is a test of T2 alone.

## What it does not say

- It does not name a signature, a family of decisions or a class of
  transformations. Until one is stated, the thesis is a research target,
  and its first defeat disjunct, a proof that no such signature exists for
  the line's systems, is hard to meet. The second, failure on held-out
  realizations, media or languages, does most of the work.
- It does not say the identified signature is the kind. Identification is the
  second of [CLAIM-135](CLAIM-135.md)'s three steps, and constitution is the third. The
  gauge of [CLAIM-148](CLAIM-148.md) is not a symmetry of the relational system either way.
- It does not say the result is new. A240's qualification places the
  starting point in existing results, and the novelty lies only in the
  restricted clause.
- It does not rest on the ontological thesis ([CLAIM-215](CLAIM-215.md)). A240: "the
  mathematical claims in T2 and T3 can remain useful independently of either
  empirical outcome" ([CLAIM-216](CLAIM-216.md)).

## Note of 2026-10-12: a named candidate

The summary says "No signature is yet named". [QUESTION-052](../questions.d/QUESTION-052.md), filed on main
after PR [#121](https://github.com/dmarx/nucleation/issues/121) branched, names a first candidate: the top eigenspace of the
operator defined by a distribution over same-kind pairs of realizations.
It holds [THEORY-007](../theory.d/THEORY-007.md), [THEORY-005](../theory.d/THEORY-005.md) and four other THEORYs as partial answers,
and leaves open the directed case, for which [THEORY-009](../theory.d/THEORY-009.md) found no account.
[CLAIM-193](CLAIM-193.md) is the linear-case form of this thesis's first clause: a linear
probe family separates only what the normalized kernel separates. The two
are now related by `complements`.
