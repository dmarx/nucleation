---
status: Proposed
title: 'coverage, and which sense: deterministic coverage that treats a covering unit as always available, expected coverage that discounts it by its chance of being busy, and reliable coverage that requires a free unit with a stated probability'
version: 1
tags:
- operations-research
- probabilistic-modeling
- agency
date: '2026-11-04'
line:
- will-organization
summary: >-
  Filed at the owner's request on 2026-11-04, to account for a distinction
  the readings of the pasted bibliography on emergency readiness surfaced
  and the record lacked: it held no location model and no entry on
  coverage under congestion, and its readers judged each such model to
  qualify [TERM-055](TERM-055.md) without instantiating it. Sources: Mukhopadhyay and
  colleagues' review ([LIT-tmpv1cro](../literature.d/LIT-tmpv1cro.md)), for the sequence of senses; Daskin
  ([LIT-tmpt3a4i](../literature.d/LIT-tmpt3a4i.md), Unavailable) for expected coverage and ReVelle and Hogan
  ([LIT-tmpjzyct](../literature.d/LIT-tmpjzyct.md), Unavailable) for reliable coverage, both from their
  abstracts and neighbours. The wording is the filer's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: LIT-tmpt3a4i LIT-tmpjzyct — Unavailable; cited for their published abstracts, nothing here rests on them -->
<!-- inactive-ok-file: NOTE-tmpdnqqh — Skimmed; the reading the review's quotations come from -->
<!-- inactive-ok-file: THEORY-tmphqo3c TERM-tmpuc919 TERM-tmp4gc9h — Proposed; the review's account and the terms of the same filing, cited as filed -->

# TERM-tmplh56l: coverage, and which sense: deterministic coverage that treats a covering unit as always available, expected coverage that discounts it by its chance of being busy, and reliable coverage that requires a free unit with a stated probability

## Definition

A demand point is **covered** when a response unit can reach it within a
time standard. A claim that uses "coverage" should say which of three
senses it means, because they differ on whether a unit that can reach the
point is free to go.

1. **Deterministic coverage.** A point is covered if some unit is within
   the standard, and the unit is assumed free. Mukhopadhyay and colleagues
   ([LIT-tmpv1cro](../literature.d/LIT-tmpv1cro.md), skimmed in [NOTE-tmpdnqqh](../notes.d/NOTE-tmpdnqqh.md); [THEORY-tmphqo3c](../theory.d/THEORY-tmphqo3c.md)), §6.1: "Resources at a
   facility are considered to be always available". Covering a point
   twice is a hedge against busyness that does not remove the assumption,
   and "Accounting for such situations requires modeling facility
   availability explicitly".
2. **Expected coverage.** The expected demand for which at least one
   covering unit is free. Daskin's abstract ([LIT-tmpt3a4i](../literature.d/LIT-tmpt3a4i.md), unread): "The
   model is extended to account for the chance that when a demand arrives
   at the system it will not be covered since all facilities capable of
   covering the demand are engaged serving other demands." The neighbours
   add one system-wide busy probability and independent units.
3. **Reliable coverage.** A point counts only if a free unit is within
   the standard with at least a stated probability α. ReVelle and Hogan's
   abstract ([LIT-tmpjzyct](../literature.d/LIT-tmpjzyct.md), unread): the model maximizes "the population which
   will find a server available within a time standard with α
   reliability." The neighbours add busy fractions estimated by area from
   local demand.

## Its relation to the record's terms

Each sense is a chance of deployment by a deadline with unavailability
from congestion alone, so the second and third are fleet-level special
cases of operational availability ([TERM-055](TERM-055.md)) with the cue and the
procedure held fixed, and a busy covering unit is present but not
deployable ([CLAIM-296](../claims.d/CLAIM-296.md), [CLAIM-312](../claims.d/CLAIM-312.md)). The first sense is the one that makes
a fleet look ready by counting units, which is why the distinction is
worth a term: deterministic coverage can be complete while expected
coverage is poor.

## What it is not

- **Scenario-conditioned readiness** (A's term, [TERM-tmpuc919](TERM-tmpuc919.md)): the chance
  of an effective response to a specified contingency under a policy.
  Coverage in every sense here is a static count over ordinary demand, and
  says nothing of a response's effect.
- **The objective coverage stands for.** Coverage is a proxy objective
  ([TERM-tmp4gc9h](TERM-tmp4gc9h.md), filed the same day) for survival; which sense of
  coverage is used changes how far it is misaligned.

## What would settle it

A claim of the record's own stated in one of the senses, or readings of
Daskin and of ReVelle and Hogan confirming their objectives against the
abstracts. Adopting it is the owner's call.
