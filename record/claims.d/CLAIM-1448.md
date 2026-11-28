---
number: 1448
status: Proposed
formerly:
- CLAIM-tmpwlw8t
title: 'Alternative support has no least retention requirement'
statement: >-
  A requirement that at least one of two alternative grounds be kept at a
  given availability has two minimal ways of being met, the one kept and
  the other let go, and their meet meets it in neither, so it has no least
  assignment and no per-entry join can compute it; a record that propagates
  retention requirements as joins either keeps both grounds, which
  over-retains, or must state requirements on sets of entries, as
  alternative support sets or hyperedges
version: 1
role: counter
warrant: demonstrated
objects_to:
- CLAIM-1389
tags:
- logic
- databases
- mathematics
date: '2026-11-26'
line:
- record-as-apparatus
- formal-apparatus
bears_on:
- QUESTION-552
summary: >-
  The assistant's fill for a gap between A29 §15 and §16 of the exchange
  "Alignment consequences brainstorm" (ChatGPT, 2026-11-26). §15 computes
  an entry's retention requirement as a join over its uses ([CLAIM-1389](CLAIM-1389.md));
  §16 observes that two independently sufficient grounds differ from two
  joint premises and that "redundant grounds are sometimes maintained
  corrective reserves", without saying that the join cannot represent
  them. It cannot: the requirement is disjunctive, its satisfying
  assignments are not closed under meet, and so it has no least element.
  Checked by enumeration with python3 -I. The record already separates the
  two kinds of support at the level of arguments: an ARG's premises work
  together, and a claim with two ARGs has two independent lines (the ARG
  scheme's `rests_on` and the CLAIM scheme's `argued_by`). The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-1389 THEORY-1778 — Proposed; the claim this objects to, filed 2026-11-26 -->

# CLAIM-1448: Alternative support has no least retention requirement

## The gap

A29 §15 lets each use of an entry impose a minimum requirement and takes
the join ([CLAIM-1389](CLAIM-1389.md)). A29 §16 then sets joint support (C needs A and
B) against alternative support (either A or B establishes C), and adds
that "retaining both grounds may be redundant for establishing the current
conclusion but valuable for resilience against future invalidation". It
leaves open how the join handles the second. It does not.

## The derivation

Order availability cold < warm < hot (0 < 1 < 2) and take assignments to
the pair (A, B) componentwise. Joint support imposes a requirement on each
of A and B separately, say hot on both; that is the join of two per-entry
lower bounds, and its least assignment is (hot, hot).

Alternative support, read as the requirement that C stays recoverable at
hot if at least one ground is hot, is the set of assignments with max(a, b) = 2. Its minimal
elements are (hot, cold) and (cold, hot). Their meet is (cold, cold), which
does not satisfy the requirement. So the set has no least element, and no
requirement of the form "a ≥ r_A and b ≥ r_B", which is what a per-entry
join produces, has exactly this set of solutions: the least per-entry
bounds compatible with both minimal assignments are (cold, cold), which
under-retains, and the only per-entry bounds that guarantee the requirement
whichever ground is let go are (hot, hot), which over-retains.

Checked with `python3 -I` by enumerating the nine assignments: the
satisfying ones are those with a 2; the minimal ones are (0, 2) and (2, 0);
their meet (0, 0) is not among them.

## What follows

- **Conservative propagation keeps both.** A29 §15's "unresolved
  classification could default to conservative retention" does this, and
  is safe; it is also the over-retention the owner's U15 is about.
- **Keeping one is a choice the lattice cannot make.** Which ground to let
  go is a judgment (which is cheaper, which is more likely to be
  invalidated), and §16's "corrective reserves" is the reason not to make
  it at all.
- **The record already marks the difference** where arguments are filed
  as ARGs: an ARG's premises work together, and a claim with two ARGs has
  two independent lines of support. A requirement could be stated per ARG
  ("keep enough of this ARG's premises to rerun it") and the alternatives
  read off `argued_by`. A claim's own `rests_on` list is conjunctive and
  carries no such distinction; [CLAIM-293](CLAIM-293.md) holds that the topology alone
  does not fix revision in any case.
- **A29 §16's remedy** ("hypergraphs or assumption-based
  truth-maintenance machinery") is the general form: de Kleer's labels
  are sets of minimal assumption sets ([THEORY-1778](../theory.d/THEORY-1778.md)), a disjunction of
  conjunctions, which is exactly what a disjunctive requirement needs.
