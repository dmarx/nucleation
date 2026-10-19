---
number: 37
status: Proposed
formerly:
- CLAIM-tmpaviuz
title: 'Formal contextuality is a failure of global extension, distinct from ordinary context dependence, and needs Contextuality-by-Default when marginals shift with context'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Split under ADR-043 at the owner's direction, carrying out the promotion
    audit's decision (record/promotion-audit/decisions/CLAIM-037.yaml, batch
    002, ADR-047). The coincidence of the two criteria on consistently
    connected systems, which NOTE-600 states as the reader's inference and
    which was the second disjunct of the defeat condition, is now
    CLAIM-374, demonstrated and Active, with a proof. This claim rests
    on it and keeps the methodological thesis, that formal contextuality
    "needs Contextuality-by-Default when marginals shift with context".
    LIT-843's causal-past route contests that "needs", so the warrant is
    interpretive. The defeat condition keeps its first disjunct. The title is
    unchanged, and the status stays Proposed.
role: thesis
warrant: interpretive
defeated_if: >-
  A pragmatic data set in which inconsistent connectedness is handled by
  the sheaf-theoretic test without loss.
tags:
- contextuality
- philosophy-of-language
date: '2026-10-09'
line:
- pragmatic-transport
- formal-apparatus
works:
- what-survives-translation
rests_on:
- CLAIM-374
grounds:
- THEORY-012
- LIT-016
- LIT-777
- LIT-842
- LIT-844
- THEORY-014
- THEORY-020
summary: >-
  The manuscript's §3 and §9. It separates three things: context
  dependence, stochastic noncommutativity, and contextuality as an
  obstruction to a global section. [CLAIM-069](CLAIM-069.md) names the version of
  CbD it should cite.
objected_by:
- CLAIM-069
complements:
- CLAIM-041
- CLAIM-044
- CLAIM-131
- CLAIM-141
- CLAIM-143
- CLAIM-310
illustrated_by:
- CASE-008
- CASE-035
- CASE-037
- CASE-095
---

# CLAIM-037: Formal contextuality is a failure of global extension, distinct from ordinary context dependence, and needs Contextuality-by-Default when marginals shift with context

## The claim

An observational scenario is a cover of observables by jointly accessible
contexts; an empirical model is noncontextual when a global law has the
contexts' laws as marginals (Abramsky and Brandenburger, [LIT-016](../literature.d/LIT-016.md)). The
manuscript insists that this is not every context effect: asking two questions
together may shift one's marginal, and then Contextuality-by-Default
(Dzhafarov and Kujala, [LIT-777](../literature.d/LIT-777.md)) is the right tool. Order effects (AB ≠ BA)
occur in classical Markov systems and establish no contextuality (§9).

## What it does not say

It does not claim pragmatic observables are contextual; the parity example
(solidarity, condemnation, humour) is offered as an obstruction pattern, not a
finding about judgements. [NOTE-600](../notes.d/NOTE-600.md)'s reader adds that for consistently
connected systems the two criteria coincide, and that this is the reader's
inference, not the paper's.

## Language data are signalling

In Wang et al. ([LIT-842](../literature.d/LIT-842.md)), every model estimated from the corpora is signalling.
The sheaf criterion could not be applied to any of them, and only
Contextuality-by-Default could. That is direct support for this claim.

Abramsky, Barbosa and Searle ([LIT-843](../literature.d/LIT-843.md)) offer a second route. In their
approach, signalling from a declared causal past becomes part of the
classical model.

## The BERT study, again

In Lo et al. ([LIT-844](../literature.d/LIT-844.md)) every instance signals unless all its probabilities are
½. The two criteria that allow for signalling then diverge widely: 71.1%
of instances are contextual by Contextuality-by-Default, 0.148% by the
sheaf criterion. That supports this claim.

## Note of 2026-10-12: evidence now linked

Two THEORYs now ground this claim:

- [THEORY-014](../theory.d/THEORY-014.md): in Contextuality-by-Default a signed maximally connected quasi-coupling always exists, signalling or not, and noncontextuality is the existence of a nonnegative one. This sharpens "global extension" here to mean nonnegative extension.
- [THEORY-020](../theory.d/THEORY-020.md): the Kochen–Specker failure cannot sit in any one context, only in the agreement where contexts overlap. It is the deterministic case of [THEORY-012](../theory.d/THEORY-012.md), which already grounds this claim.

## Note of 2026-10-19: split under [ADR-043](../decisions.d/ADR-043.md)

That the two criteria coincide on consistently connected systems is now
[CLAIM-374](CLAIM-374.md). It is proved there, for connections of any size, and it is
Active. The defeat condition's second disjunct, a consistently connected
system on which they disagree, now belongs to that claim, so it is removed
here. This claim keeps the thesis about systems whose marginals shift. It is
supported by [LIT-842](../literature.d/LIT-842.md) and [LIT-844](../literature.d/LIT-844.md), and contested by [LIT-843](../literature.d/LIT-843.md)'s causal-past
route, which folds signalling into the classical model instead. Per
[CLAIM-069](CLAIM-069.md), the version of Contextuality-by-Default it should name is the
one with multimaximal couplings, for observables in more than two contexts.
The thesis is interpretive until the record compares the two routes on a
signalling data set, or concedes "needs" to "can handle".
