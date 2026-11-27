---
status: Proposed
title: 'The record keeps distinctions as DISTINCTIONs, which bind two or more TERMs or CLAIMs by what separates them in theory and the observation that tells them apart, and a TERM characterizes one concept'
version: 1
tags:
- record
- taxonomy
date: '2026-11-26'
summary: >-
  At the owner's word of 2026-11-26: "let's add a DISTINCTION object to the
  luria scheme. might make it easier to map our operationalization to our
  theory", and then "we can use the DISTINCTION object to bind TERMS through
  their explicit distinction. we should move the distinction bit out of the
  TERM blurb and make it the explicitly a home for characterizing concepts",
  and "any terms that have multiple senses to dismbiguate can merit from a
  distinction, as can claims that were split, etc.".
  A new scheme, DISTINCTION, in record/distinctions.d. It binds two or more
  TERMs or CLAIMs (`between`, required; converse `distinguished_by`, derived
  on both), for a term's senses, a term's neighbours, or a split claim. It states a `criterion`, what separates them in theory, and
  `tells_apart`, the observation, measure, case or computation on which one
  side holds and the other does not. It has a credence and a `defeated_if`.
  Cases that witness it are `witnessed_by` (converse `witnesses` on CASE).
  Claims that rely on it name it in `uses`, and leads `advance` it. TERM is
  now the home for characterizing one concept: its blurb and template drop
  the distinction, and the template's "What it is not" section becomes
  "Distinctions", which cites them. First application: [DISTINCTION-tmpvz9hk](../distinctions.d/DISTINCTION-tmpvz9hk.md),
  between [TERM-076](../terms.d/TERM-076.md) and a new [TERM-tmpk4a7y](../terms.d/TERM-tmpk4a7y.md), used by [CLAIM-tmpi0oub](../claims.d/CLAIM-tmpi0oub.md).
  Rejected: a claim role; distinctions as TERM prose; sides as readings.
---
<!-- inactive-ok-file: DISTINCTION-tmpvz9hk TERM-tmpk4a7y TERM-076 CLAIM-tmpi0oub — Proposed or new; the first application -->

# ADR-tmp5grqg: The record keeps distinctions as DISTINCTIONs, which bind two or more TERMs or CLAIMs by what separates them in theory and the observation that tells them apart, and a TERM characterizes one concept

## Context

The record states distinctions everywhere and has nowhere to put them. A
TERM's template called a term "a concept or distinction the argument is
stated in", and gave each term a "What it is not" section. Claims draw
distinctions in prose: [CLAIM-tmpi0oub](../claims.d/CLAIM-tmpi0oub.md) separates two senses of "valence",
[CLAIM-tmphyvh3](../claims.d/CLAIM-tmphyvh3.md) separates valence unobserved from valence absent, and
[CLAIM-548](../claims.d/CLAIM-548.md) separates activation, granted authority and efficacy. None of
these says, in a place a reader or a lint can find, what observation would
tell the sides apart. That is where operationalization meets theory, and it
is the owner's reason for the scheme. A distinction stated on one term is
also only half there: the neighbouring term does not know it.

## Decision

- **A new scheme, DISTINCTION**, in record/distinctions.d, rendered to
  docs/distinctions. Statuses are those of claims, Active in force.
- **It binds TERMs or CLAIMs.** `between` names two or more and is
  required; TERM and CLAIM gain `distinguished_by`, derived. Three uses, on
  the owner's word:
  - a term with several senses to disambiguate, each sense its own TERM;
  - a term and a neighbour it must not be confused with;
  - a claim that was split, or two claims easily run together, where the
    distinction says what the split separated and what would show it.

  A side drawn from a reading gets a TERM that `draws_on` the reading
  first, so that every side is something the record holds in its own
  voice.
- **Two required fields carry the mapping.** `criterion` says what
  separates the sides in theory. `tells_apart` says what observation,
  measure, case or computation gives one side and not the other, or names
  the one the record lacks.
- **It has a credence.** `defeated_if` is required: typically, a showing
  that every observation the record can make gives the sides the same
  value. A distinction that has collapsed is Rejected or Superseded, not
  deleted.
- **Its relations.** `witnessed_by` names the CASEs that dissociate the
  sides (converse `witnesses` on CASE). `rests_on` names claims it
  depends on, and `bears_on` names questions. A CLAIM's `uses` may name a
  DISTINCTION beside its TERMs (converse `used_by`), so that a collapse
  finds the claims that kept the sides apart. A LEAD may `advance` one, by
  finding or running the observation that tells its sides apart.
- **TERM is the home for characterizing one concept.** Its blurb says so
  and says that what holds two terms apart is a DISTINCTION. Its template
  drops "or distinction", and its "What it is not" section becomes
  "Distinctions", citing the DISTINCTIONs that bind it.

## Alternatives considered

- **A claim role, "distinction".** Lighter, but a claim has no sides, so
  nothing derives on the terms, and no field holds the observation that
  tells them apart.
- **Distinctions as prose on TERMs.** The status quo. It states each
  distinction on one side only and leaves the operational test unwritten.
- **Sides as readings (THEORY).** This was the first draft. The owner's
  "bind TERMS" settles it: a reading's sense gets a TERM first.
- **Splits recorded only by supersession.** A claim split in two already
  names both successors in `superseded_by`. That says the split happened,
  not what it separated or how the halves are told apart.
- **A second reading of the owner's word.** "Make it the explicitly a home
  for characterizing concepts" is read here with "it" as TERM. It can also
  be read with "it" as DISTINCTION: concepts are characterized by their
  distinctions, and a TERM only names what its distinctions fix. On that
  reading, a TERM's definition would be expected to be stated through its
  distinctions, and a TERM bound by none would be a gap. The scheme is the
  same on both readings. Only the TERM blurb would change, and the choice
  is the owner's.

## Consequences

- Existing "What it is not" sections and the distinctions drawn in claims
  are not migrated. A sweep that files them as DISTINCTIONs is a separate
  unit, waiting on the owner. A rough count on this branch: 79 TERMs carry
  `complements`, a different sense of the same subject; 53 TERMs mention
  senses; 52 claims mention a split, and 3 name two or more successors
  ([CLAIM-053](../claims.d/CLAIM-053.md), [CLAIM-072](../claims.d/CLAIM-072.md), [CLAIM-229](../claims.d/CLAIM-229.md)). Others named in the exchange:
  [CLAIM-tmphyvh3](../claims.d/CLAIM-tmphyvh3.md) (unobserved and absent), [CLAIM-548](../claims.d/CLAIM-548.md) (activation, authority
  and efficacy), and the affect, valence and emotion split of
  [QUESTION-544](../questions.d/QUESTION-544.md)'s alternatives.
- `tells_apart` may name an observation the record does not have. Those
  are natural LEADs.
- docs/record.md lags luria.yaml on this branch until it is regenerated on
  the default branch.
