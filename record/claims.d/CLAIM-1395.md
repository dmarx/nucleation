---
number: 1395
status: Proposed
formerly:
- CLAIM-tmpdkwbk
title: 'Cooling must leave dependencies visible'
statement: >-
  A governed record may take an entry out of ordinary discovery but not out
  of accountability: a cooled or condensed entry must still be found by the
  checks that follow dependencies, so that a change to its grounds still
  raises the review it would raise if the entry were in default retrieval,
  and the record can do this without rescanning what is cold by keeping an
  index of the references that cross from one tier to another, updated
  whenever a relation, a tier or a consolidation changes
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A case in which keeping dependencies on cold entries visible costs more
  than the corrections it enables, on the record's own history: retired or
  cold entries whose grounds changed and whose dependants needed no
  review; or a showing that an index of cross-tier references cannot be
  kept correct more cheaply than a rescan.
tags:
- design-rationale
- databases
- software-engineering
date: '2026-11-26'
line:
- record-as-apparatus
- records-of-inquiry
bears_on:
- QUESTION-552
uses:
- TERM-186
summary: >-
  A27 §11 of the exchange "Alignment consequences brainstorm" (ChatGPT,
  2026-11-26): "Exclude cold knowledge from ordinary discovery without
  excluding it from institutional accountability", or "archival becomes
  another mechanism for silencing inconvenient information". A cites
  luria's corollary "a suppression must not become a silence" ([LU-DP-001](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-1)),
  rightly. A29 §4 gives the mechanism, from generational garbage
  collection: remembered sets and write barriers, an index of references
  across tiers checked when a relation is added, a reference changes
  sense, an entry changes tier, a consolidation changes what satisfies a
  dependency, or a protected root changes. The wording is A's (ChatGPT, in
  the exchange of 2026-11-26); adopting it is the owner's call.
---

# CLAIM-1395: Cooling must leave dependencies visible

## The claim

A27 §11: "cooling an entry should not make Luria stop recognizing
dependencies on it. If the grounds of a warm or cold claim change, the
appropriate review obligation should still be discoverable, even if
determining its substance requires rehydrating the original material."

The record's retirement already works this way. Retiring an entry
"reports what rests on it and leaves whether each dependant falls to a
judgment" ([CLAIM-664](CLAIM-664.md)); a cooled entry is the same report at one remove,
where the dependant, not the retired entry, is the one out of the way. The
claim is that cooling must not be the exception to luria's first
principle ([LU-DP-001](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-1)): an acknowledgement that hides a warning is counted,
and a tier that hides a dependency must be too.

## The mechanism

A29 §4. A generational collector that collects only young objects must
know which old objects point at young ones; it keeps a remembered set,
maintained by a write barrier on every store that crosses generations.
"Suppose a cold claim is cited as a premise in a new hot claim. Luria need
not scan the entire cold archive during every maintenance pass. It can
maintain an index of cross-tier dependencies." The barrier is a check run
whenever:

- a new relation is added;
- an existing reference changes its semantics;
- an entry moves between retention tiers;
- a consolidation changes which representation satisfies a dependency;
- a protected root is added or removed.

A: "A small addition to the relation index might yield substantial savings
in maintenance work."

## A condition A states

A27 §13: tiers help only if the record's readers respect them. An agent
that greps the whole tree meets cold entries anyway, and one that reads
only the views would miss a dependency the views leave out. So the claim
needs luria to provide the retrieval surfaces, a search that honours tiers
and a dependency check that ignores them, "not merely conventions about how
agents ought to search".
