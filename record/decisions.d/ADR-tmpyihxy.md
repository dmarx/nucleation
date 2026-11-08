---
status: Proposed
title: 'An account the record holds only in parts, for a line or a part of one, gets a SYNTHESIS that restates it, so the account has an address: it adds nothing, and its standing is its components''; there is one account per scope, an account may integrate the accounts of its parts, and a line whose parts barely relate is a candidate to split'
version: 3
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Before merge, at the owner's review: one account per scope, not per
    line; accounts may be built over part syntheses; a line whose parts
    barely relate is a candidate to split (ADR-tmpyb8vm), and the
    demonstration is the split line's syntheses.
- version: 3
  date: '2026-11-08'
  note: >-
    Restated at ADR-tmp72iro, which makes SYNTHESIS the scheme of
    accounts only: an account is no longer "unadmitted", it can be set
    Current once the owner has reviewed its mapping, and the view sets
    it out under its line rather than apart. Accounts over accounts name
    their parts in `integrates`; a link between parts that no part
    states is filed as a claim if it passes ADR-075's test, and the
    line's account integrates the claim. The choice, an account per
    scope with a split signal, is unchanged.
tags:
- record
date: '2026-11-07'
summary: >-
  [ADR-075](ADR-075.md) began from a filing gap: an integration left with no address, so
  the record could not say what its current account is, nor check a later
  synthesis for drift. The admission test it added guards against importing
  a source's broad summary as one more claim. [ADR-078](ADR-078.md)'s review reused that
  test to backfill the current-account view. There the common verdict was
  that a candidate's integration was already stated in its components'
  bodies and notes, and nothing was filed. That recreates the original gap:
  the nucleating-argument line has an account, scattered, and the view
  shows none. This decision gives such an account a SYNTHESIS
  (version 3: the scheme is now accounts only, ADR-tmp72iro). It
  restates a line's account as the record holds it, maps every
  component, and adds nothing; its standing is its components', and the
  view sets it out under its line. The review files one when a candidate fails the claim test only
  because the record already holds its integration, and never when it
  fails on a free parameter, an error or a contradiction. There is one
  account per scope, a line or a part of one, not one per line, and a
  line's account may integrate its parts' accounts. When a line's
  parts barely relate, that is a signal to split the line, which is
  decided separately. The demonstration is the former nucleating-argument
  line: its account, split into part syntheses and a line synthesis over
  them, after the split of the line (ADR-tmpyb8vm). Rejected:
  treating lines without a synthesis as findings only; admitting such
  accounts; a separate scheme.
---
<!-- inactive-ok-file: ADR-075 ADR-076 ADR-077 ADR-078 ADR-tmpyb8vm — Proposed; the audit, the scheme, the move rule and the review this amends -->

# ADR-tmpyihxy: An account the record holds only in parts, for a line or a part of one, gets a SYNTHESIS that restates it, so the account has an address: it adds nothing, and its standing is its components'; there is one account per scope, an account may integrate the accounts of its parts, and a line whose parts barely relate is a candidate to split

## Context

[ADR-075](ADR-075.md) named two costs of filing a source's syntheses as recaps mapped to
their turns: the record "can't say what its current account is", and "later
syntheses can't be checked for drift". Its admission test (versions 2 and 3)
was added against salience without work. A broad source summary filed as
one more claim gains standing it has not earned. For imports, which are
mostly recaps, a high rejection rate is the point.

[ADR-078](ADR-078.md) reused the test to backfill the current-account view ([ADR-076](ADR-076.md)) from
what the record already holds. Over three rounds on 2026-11-07, six of 36
candidates were admitted. The most common verdict on the opportunity arm was
that the integration is already stated in a component's body or dated
notes. The nucleating-argument line was audited in all three rounds, and
each time its account was found held in prose ([CLAIM-185](../claims.d/CLAIM-185.md)'s notes, [CLAIM-250](../claims.d/CLAIM-250.md)'s
note of 2026-10-15, [CLAIM-469](../claims.d/CLAIM-469.md) and [CLAIM-476](../claims.d/CLAIM-476.md)), so the view shows nothing for
it.

That is the gap [ADR-075](ADR-075.md) was written to close. The record has made the
integration and given it no address. The scheme already has the slot: an
unadmitted SYNTHESIS ([ADR-076](ADR-076.md), version 2) keeps its components' standing
derived, takes revisions and cannot be Current. The view left such entries
out.

The owner was asked whether the current-account view is for novelty, only
integrations that earn standing, or for coverage, each line's account
stated somewhere. The owner chose coverage, with unadmitted entries shown
apart.

## Decision

- **A SYNTHESIS can be a line account.** It restates a line's account as
  the record holds it:
  - every component in `integrates`, with code, voice and status in the
    body;
  - each link it states attributed to the entry that states it.

  It adds nothing. A link no component states goes under "Not stated on the
  record", where filing it would be a claim's, under ADR-075's test.
- **What shows it wrong is fidelity, not a countermodel.** Its `defeated_if`
  names:
  - a component misstated or misattributed;
  - an in-force component of the line left out;
  - a link it states that no component states.

  Its standing is its components'.
- **It is set Current by the owner (version 3).** Version 2 forbade it,
  under ADR-076's admission field. Under ADR-tmp72iro an account's status is
  whether its mapping is right: Current once the owner has reviewed it,
  Proposed until then.
- **The view lists it under its line (version 3).** `docs/current-account.md`
  sets out each line's accounts with their components' live standing, and
  lists the lines with no account.
- **The review files one when a candidate fails the claim test only
  because the record already holds the integration.** This applies to a line, or a major part
  of one, that has no admitted synthesis. A candidate that fails for any
  other reason gets no line account, because an account that absorbs every
  case is not an account:
  - a free parameter;
  - a component stated wrongly;
  - a contradiction with a component.
- **One account per scope, not one per line (version 1 said one per
  line).** A scope is a line or a part of one: a group of its components
  that answer one of its questions. Two accounts never cover the same
  scope; a later review or filing revises the one there is ([ADR-075](ADR-075.md) step
  7).
- **Accounts can be built over accounts.** A line's account may integrate
  its parts' accounts. The links between parts are where something the
  parts leave open can live; such a link is filed as a claim if it passes
  ADR-075's test (ADR-tmp72iro), and the line's account integrates the
  claim.
- **A line that wants several unrelated accounts is a candidate to split.**
  When a line's parts barely relate, counted by the relations among their
  components (`scratch/formal/line_parts.py`), the review reports the line
  as a candidate for splitting into lines of its own, each with its own
  account. The split is a decision about the lines vocabulary, taken
  separately, and the review never forces one account over parts that do
  not hang together.
- **Demonstration ([ADR-071](ADR-071.md)).** The nucleating-argument line was first given
  one account. The counts showed that two of its five parts barely related
  to the rest, and the line was split ([ADR-tmpyb8vm](ADR-tmpyb8vm.md)). Each of the three
  lines now has its synthesis, and nucleating-argument's is built over the
  syntheses of its three parts.

## Alternatives considered

- **Lines without a synthesis are findings only.** This is the earlier
  reading, under which a line held in parts shows nothing. It keeps the view
  strict, but leaves exactly the accounts [ADR-075](ADR-075.md) set out to give an address
  without one. Nothing then catches a later synthesis that drifts from them.
- **Admit such accounts.** A route that admits "already held" would give a
  recap the salience the admission test exists to withhold. Under
  ADR-tmp72iro an account earns no standing at all, which is the same
  guard.
- **One account per line (this decision's version 1).** That forces an
  either-or where a line holds several inquiries. Choosing one account
  hides the others; merging them hides that they barely relate.
- **A separate scheme for line accounts.** The SYNTHESIS scheme already
  separates the account's status from its admission ([ADR-076](ADR-076.md), version 2).
  A second scheme would duplicate the components, relations and view.

## Consequences

- Every line can show an account, of one of two kinds, and the view says
  which.
- A line account is only as good as its mapping. It has to be revised when
  its components change, and a stale one misleads. The review checks line
  accounts against their components, as it checks admitted syntheses.
- The salience guard is kept: a line account states nothing new, and its
  status vouches for its map, not for its components.
