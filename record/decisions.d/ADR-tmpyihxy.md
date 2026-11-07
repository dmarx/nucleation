---
status: Proposed
title: 'A line whose account the record holds only in parts gets an unadmitted SYNTHESIS that restates it, so the account has an address: it adds nothing, cannot be set Current, and the current-account view lists it apart from the admitted integrations'
version: 1
tags:
- record
date: '2026-11-07'
summary: >-
  ADR-075 began from a filing gap: an integration left with no address, so
  the record could not say what its current account is, nor check a later
  synthesis for drift. The admission test it added guards against importing
  a source's broad summary as one more claim. ADR-078's review reused that
  test to backfill the current-account view. There the common verdict was
  that a candidate's integration was already stated in its components'
  bodies and notes, and nothing was filed. That recreates the original gap:
  the nucleating-argument line has an account, scattered, and the view
  shows none. This decision uses the scheme's existing `admission:
  unadmitted` for such accounts. An unadmitted SYNTHESIS restates a line's
  account as the record holds it, maps every component, and adds nothing.
  It has no route and cannot be set Current, and its standing is its
  components'. The view lists these accounts under "Accounts held in
  parts". The review files one when a candidate fails admission only
  because the record already holds its integration, and never when it
  fails on a free parameter, an error or a contradiction. The
  demonstration is the nucleating-argument line's account. Rejected:
  treating lines without a synthesis as findings only; admitting such
  accounts; a separate scheme.
---
<!-- inactive-ok-file: ADR-075 ADR-076 ADR-077 ADR-078 — Proposed; the audit, the scheme, the move rule and the review this amends -->

# ADR-tmpyihxy: A line whose account the record holds only in parts gets an unadmitted SYNTHESIS that restates it, so the account has an address: it adds nothing, cannot be set Current, and the current-account view lists it apart from the admitted integrations

## Context

ADR-075 named two costs of filing a source's syntheses as recaps mapped to
their turns: the record "can't say what its current account is", and "later
syntheses can't be checked for drift". Its admission test (versions 2 and 3)
was added against salience without work. A broad source summary filed as
one more claim gains standing it has not earned. For imports, which are
mostly recaps, a high rejection rate is the point.

ADR-078 reused the test to backfill the current-account view (ADR-076) from
what the record already holds. Over three rounds on 2026-11-07, six of 36
candidates were admitted. The most common verdict on the opportunity arm was
that the integration is already stated in a component's body or dated
notes. The nucleating-argument line was audited in all three rounds, and
each time its account was found held in prose (CLAIM-185's notes, CLAIM-250's
note of 2026-10-15, CLAIM-469 and CLAIM-476), so the view shows nothing for
it.

That is the gap ADR-075 was written to close. The record has made the
integration and given it no address. The scheme already has the slot: an
unadmitted SYNTHESIS (ADR-076, version 2) keeps its components' standing
derived, takes revisions and cannot be Current. The view left such entries
out.

The owner was asked whether the current-account view is for novelty, only
integrations that earn standing, or for coverage, each line's account
stated somewhere. The owner chose coverage, with unadmitted entries shown
apart.

## Decision

- **An unadmitted SYNTHESIS can be a line account.** It restates a line's
  account as the record holds it:
  - every component in `integrates`, with code, voice and status in the
    body;
  - only those it cannot stand without in `premises`;
  - each link it states attributed to the entry that states it.

  It adds nothing. A link no component states goes under "Not stated on the
  record", where filing it would need admission. It has no `route`, which
  the scheme already forbids while unadmitted. Its `role` is `thesis` and
  its `warrant` is `interpretive`.
- **What shows it wrong is fidelity, not a countermodel.** Its `defeated_if`
  names:
  - a component misstated or misattributed;
  - an in-force component of the line left out;
  - a link it states that no component states.

  Its standing is its components'.
- **It cannot be set Current.** ADR-076's `current_but_unadmitted` already
  enforces this. A line account that should become the adopted account has
  to be admitted first, by a route.
- **The view lists it apart.** `docs/current-account.md` gains a closing
  section, "Accounts held in parts", where each entry is set out with its
  components' live standing. The sections by line still show admitted
  syntheses only.
- **The review files one when admission fails only because the record
  already holds the integration.** This applies to a line, or a major part
  of one, that has no admitted synthesis. A candidate that fails for any
  other reason gets no line account, because an account that absorbs every
  case is not an account:
  - a free parameter;
  - a component stated wrongly;
  - a contradiction with a component.
- **Revise, don't duplicate (ADR-075 step 7).** A line has at most one line
  account. A later review or filing that changes the line revises it as a
  new version. If an admitted synthesis later covers the line, the line
  account is Superseded by it.
- **Demonstration (ADR-071):** the nucleating-argument line's account, filed
  with this decision.

## Alternatives considered

- **Lines without a synthesis are findings only.** This is the earlier
  reading, under which a line held in parts shows nothing. It keeps the view
  strict, but leaves exactly the accounts ADR-075 set out to give an address
  without one. Nothing then catches a later synthesis that drifts from them.
- **Admit such accounts.** A route that admits "already held" would give a
  recap the salience the admission test exists to withhold, and would let
  it be set Current.
- **A separate scheme for line accounts.** The SYNTHESIS scheme already
  separates the account's status from its admission (ADR-076, version 2).
  A second scheme would duplicate the components, relations and view.

## Consequences

- Every line can show an account, of one of two kinds, and the view says
  which.
- A line account is only as good as its mapping. It has to be revised when
  its components change, and a stale one misleads. The review checks line
  accounts against their components, as it checks admitted syntheses.
- The salience guard is kept: a line account cannot be Current, is labelled
  as held in parts, and states nothing new.
