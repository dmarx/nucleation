---
number: 73
status: Proposed
formerly:
- SYNTHESIS-tmp2gov9
title: 'Granger causality and transfer entropy are predictive quantities relative to a stated information set: complete measurement is not enough for an interventional reading, Granger causation from a macro variable to its micro base has no intervention to stand for, transfer entropy adds synergy to unique information and so is not flow from the source alone, and a ΦID verdict on three or more parts rests on which axiom of redundancy is dropped'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  the directed-information part of the formal-apparatus line left out
  without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- causality
- information-theory
- mathematical-statistics
date: '2026-11-11'
line:
- formal-apparatus
integrates:
- TERM-058
- TERM-057
- CLAIM-333
- CLAIM-334
- CLAIM-335
- CLAIM-343
---
<!-- inactive-ok-file: ADR-075 THEORY-497 — Proposed; components, decisions and accounts cited with their standing -->
<!-- inactive-ok-file: SYNTHESIS-075 SYNTHESIS-079 — Proposed; cited with its standing -->

# SYNTHESIS-073: Granger causality and transfer entropy are predictive quantities relative to a stated information set: complete measurement is not enough for an interventional reading, Granger causation from a macro variable to its micro base has no intervention to stand for, transfer entropy adds synergy to unique information and so is not flow from the source alone, and a ΦID verdict on three or more parts rests on which axiom of redundancy is dropped

*A part account of the formal-apparatus line: one of the line's eleven
small clusters, six entries, all first in formal-apparatus, filed from
the readings of Granger causality, transfer entropy and partial
information decomposition in October 2026. The line's account is built
over it and its sibling parts. No other account integrates any of them.*

## The account

- **The words.** [TERM-058](../terms.d/TERM-058.md) (the record's, defined from Barnett, Barrett
  and Seth, Seth, and Eichler and Didelez; Active): Granger causality is
  predictive and relative to an information set, its lags and its model
  class, and "not by itself the effect of an intervention". [TERM-057](../terms.d/TERM-057.md) (the
  record's, from Schreiber; Active): transfer entropy is
  I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}), stated with k, l, the conditioning
  set and the estimator, "not a measure of information flow and not an
  intervention effect". For jointly Gaussian processes Geweke's Granger
  causality is twice the transfer entropy ([TERM-057](../terms.d/TERM-057.md), [TERM-058](../terms.d/TERM-058.md)).
- **Measurement is not enough.** [CLAIM-333](../claims.d/CLAIM-333.md) (the record's answer to the
  ΦID review's C5 as [NOTE-010](../notes.d/NOTE-010.md) records it; thesis, demonstrated, Active):
  measuring every relevant variable is necessary but not sufficient for
  an interventional reading. A two-series process with nothing hidden is
  Granger-noncausal from a to b, yet setting a(t) changes the mean of
  b(t + 1) by ργ. Under Eichler and Didelez's conditions "the two
  analyses agree on zero effects and share an estimand. They are still not
  one analysis."
- **Downward Granger causation.** [CLAIM-334](../claims.d/CLAIM-334.md) (the record's; disclaimed,
  demonstrated, Active): Seth's Granger causation from a macro variable
  to the micro variables it supervenes on is not evidence of an
  intervention effect, because supervenience leaves no intervention on
  the macro variable that holds its base fixed. "Here it fails for a
  different reason than the sampling step: the intervention is ruled out
  by the definition of M, not by the data."
- **Transfer entropy is not flow.** [CLAIM-335](../claims.d/CLAIM-335.md) (the record's position;
  thesis, demonstrated, Active, version 3): as a conditional mutual
  information, transfer entropy is unique plus synergistic information
  under any decomposition meeting the consistency equations, so it can
  credit a source with a bit carried only jointly and read zero from
  sources that jointly fix the target. Its summary: "This is a different
  failure from [CLAIM-333](../claims.d/CLAIM-333.md)'s, prediction against intervention."
- **Three or more parts.** [CLAIM-343](../claims.d/CLAIM-343.md) (the record's answer to the gap left
  by the PID filing; thesis, demonstrated, Active): on the Williams–Beer
  lattice from three sources up, no redundancy function satisfies both
  the identity axiom and nonnegative atoms, so "A ΦID verdict on three or
  more parts therefore rests on which axiom the analyst gave up." It
  leaves two-part ΦID untouched.

## The components

- [TERM-058](../terms.d/TERM-058.md), the record's, Active; formal-apparatus only.
- [TERM-057](../terms.d/TERM-057.md), the record's, Active; formal-apparatus only.
- [CLAIM-333](../claims.d/CLAIM-333.md), the record's, thesis, demonstrated, Active; formal-apparatus
  only; uses [TERM-058](../terms.d/TERM-058.md); grounds on [THEORY-704](../theory.d/THEORY-704.md); complements [CLAIM-335](../claims.d/CLAIM-335.md).
- [CLAIM-334](../claims.d/CLAIM-334.md), the record's, disclaimed, demonstrated, Active;
  formal-apparatus only; rests on [CLAIM-333](../claims.d/CLAIM-333.md); uses [TERM-058](../terms.d/TERM-058.md); grounds on
  [LIT-1170](../literature.d/LIT-1170.md) and [THEORY-704](../theory.d/THEORY-704.md).
- [CLAIM-335](../claims.d/CLAIM-335.md), the record's, thesis, demonstrated, Active; formal-apparatus
  only; uses [TERM-057](../terms.d/TERM-057.md) and [TERM-058](../terms.d/TERM-058.md); complements [CLAIM-333](../claims.d/CLAIM-333.md) and [CLAIM-343](../claims.d/CLAIM-343.md).
- [CLAIM-343](../claims.d/CLAIM-343.md), the record's, thesis, demonstrated, Active; formal-apparatus
  only; complements [CLAIM-335](../claims.d/CLAIM-335.md); grounds on [THEORY-713](../theory.d/THEORY-713.md) and [THEORY-714](../theory.d/THEORY-714.md).

## Links the components state, and where

Nine pairs are linked, all inside the cluster:

- **The terms and the claims.** [CLAIM-333](../claims.d/CLAIM-333.md) and [CLAIM-334](../claims.d/CLAIM-334.md) use [TERM-058](../terms.d/TERM-058.md);
  [CLAIM-335](../claims.d/CLAIM-335.md) uses both terms. [TERM-058](../terms.d/TERM-058.md)'s "What it must not be confused
  with" names [CLAIM-333](../claims.d/CLAIM-333.md) for the sampling interval and [CLAIM-334](../claims.d/CLAIM-334.md) for
  downward Granger causation, "A use of the term, not a kind of
  causation". [TERM-057](../terms.d/TERM-057.md) names [CLAIM-335](../claims.d/CLAIM-335.md) for flow, and "What [CLAIM-333](../claims.d/CLAIM-333.md) says
  of Granger causality and interventions holds for transfer entropy too."
  [TERM-057](../terms.d/TERM-057.md) and [TERM-058](../terms.d/TERM-058.md) name each other.
- **Two failures, kept apart.** [CLAIM-333](../claims.d/CLAIM-333.md) and [CLAIM-335](../claims.d/CLAIM-335.md) complement each
  other. [CLAIM-335](../claims.d/CLAIM-335.md)'s "What it does not say": "Prediction against
  intervention is [CLAIM-333](../claims.d/CLAIM-333.md)'s separate question." [CLAIM-333](../claims.d/CLAIM-333.md)'s
  counterexample has zero full-history transfer entropy and positive
  directed information, all in the instantaneous term, "That term is what
  Granger causality and transfer entropy leave out."
- **Supervenience as a second route.** [CLAIM-334](../claims.d/CLAIM-334.md) rests on [CLAIM-333](../claims.d/CLAIM-333.md): the
  step from complete measurement to an interventional reading "is exactly
  what [CLAIM-333](../claims.d/CLAIM-333.md) denies in general".
- **Two parts and more.** [CLAIM-343](../claims.d/CLAIM-343.md) and [CLAIM-335](../claims.d/CLAIM-335.md) complement each other.
  [CLAIM-343](../claims.d/CLAIM-343.md)'s "What it does not say": two-part ΦID is untouched, and "the
  record's transfer-entropy examples give the same values under all four
  two-source measures" ([CLAIM-335](../claims.d/CLAIM-335.md)).

## Links to other parts, stated

The community map found none; two mentions reach the cluster from other
parts:

- **To the effective-description account ([SYNTHESIS-075](SYNTHESIS-075.md)).** [QUESTION-252](../questions.d/QUESTION-252.md) lists [CLAIM-343](../claims.d/CLAIM-343.md) as a
  precedent: "Axiom-independence precedents: [CLAIM-343](../claims.d/CLAIM-343.md) and [CLAIM-353](../claims.d/CLAIM-353.md)."
- **To the intervention account ([SYNTHESIS-079](SYNTHESIS-079.md)).** [TERM-068](../terms.d/TERM-068.md) defines informational
  closure as "transfer entropy from the micro past with Z's whole history
  and no environment ([TERM-057](../terms.d/TERM-057.md) with k and l unbounded)".

[CLAIM-335](../claims.d/CLAIM-335.md)'s note of 2026-10-21 and [TERM-068](../terms.d/TERM-068.md) both cite [THEORY-820](../theory.d/THEORY-820.md), the
three-bit chain, outside the line. [CLAIM-333](../claims.d/CLAIM-333.md), [CLAIM-334](../claims.d/CLAIM-334.md) and [CLAIM-343](../claims.d/CLAIM-343.md)
leave [NOTE-010](../notes.d/NOTE-010.md)'s C4 and [THEORY-497](../theory.d/THEORY-497.md)'s interventional reading of ΦID's
atoms open.

## Where else these entries are integrated

Nowhere. All six are in formal-apparatus only.

## Not stated on the record

Tested by [ADR-075](../decisions.d/ADR-075.md)'s step 5 at this review and not filed:

- **Transfer entropy is neither necessary nor sufficient for influence
  from one source.** [CLAIM-333](../claims.d/CLAIM-333.md)'s process has zero transfer entropy and an
  intervention effect; [CLAIM-335](../claims.d/CLAIM-335.md)'s first example has a full bit of
  transfer entropy and no unique information. Already stated: [TERM-057](../terms.d/TERM-057.md)
  carries [CLAIM-333](../claims.d/CLAIM-333.md)'s point over to transfer entropy, and [CLAIM-335](../claims.d/CLAIM-335.md) states
  its own half. Nothing new.
- **A ΦID downward-causation verdict on three or more parts inherits the
  axiom choice.** [CLAIM-334](../claims.d/CLAIM-334.md) sets ΦID's downward atom aside; [CLAIM-343](../claims.d/CLAIM-343.md)
  says any ΦID verdict on three or more parts rests on the axiom dropped,
  which covers the downward atom. Held by [CLAIM-343](../claims.d/CLAIM-343.md). Nothing new.

## What it does not say

- That Granger analysis or transfer entropy is useless; [CLAIM-333](../claims.d/CLAIM-333.md) and
  [CLAIM-335](../claims.d/CLAIM-335.md) both disclaim it.
- Whether ΦID's quantities are interventional ([NOTE-010](../notes.d/NOTE-010.md)'s C4, [THEORY-497](../theory.d/THEORY-497.md)).
