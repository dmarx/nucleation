---
number: 306
status: Active
formerly:
- CLAIM-tmp3ejtf
title: 'Under a deadline, search can establish presence by finding one item but
  absence only by exhausting the collection, so "If I can''t find it, it isn''t
  there" acts on an unfinished search as negation as failure acts on a finished
  one: a default stronger than either the closed-world assumption or negation as
  failure, safe only when the arrangement makes the full search finish within the
  deadline'
version: 1
role: thesis
defeated_if: >-
  A search procedure, under a deadline shorter than an exhaustive pass, whose failure
  to find an item licenses its absence with no assumption that the unsearched part
  would also have failed. Or a reading of Clark's soundness theorem on which a search
  cut off before every branch has failed counts as a failure.
tags:
- logic
- databases
- cognition
date: '2026-10-15'
line: distributed-agency
uses:
- TERM-055
grounds:
- CASE-085
- CASE-094
- THEORY-341
complements:
- CLAIM-296
summary: >-
  The medic's "If I can't find it, it isn't there" ([CASE-085](../cases.d/CASE-085.md)) and the owner's "if
  I can't find it quickly enough, it may as well not be there" ([CASE-094](../cases.d/CASE-094.md)) act
  on a failed search as if it showed absence. One find shows presence, but absence
  needs a check of everything, which a deadline forbids. First filed as negation
  as failure on a time bound, with Reiter and Clark unread. Both readings corrected
  it. The two assumptions are separate. Reiter's closed-world assumption is that
  the database is complete about the world. Clark's negation as failure is licensed
  only by finite failure: "the exhaustive but unsuccessful search for a proof".
  A search cut off by a deadline meets neither, so the rule is stronger than both.
  It assumes a closed world and that the unsearched part would have failed. It is
  safe when the full pass finishes in time. In [CASE-085](../cases.d/CASE-085.md) the EMT knew the drug was
  stocked, which is exactly where Reiter shows the closed-world assumption inconsistent.
  So there it was a decision to stop, not an inference.
---
<!-- inactive-ok-file: CLAIM-296 — Proposed; open claims cited as open, nothing here rests on their being settled -->

# CLAIM-306: Under a deadline, search can establish presence by finding one item but absence only by exhausting the collection, so "If I can't find it, it isn't there" acts on an unfinished search as negation as failure acts on a finished one: a default stronger than either the closed-world assumption or negation as failure, safe only when the arrangement makes the full search finish within the deadline

## The claim

**The asymmetry.** "Present" is shown by one find. "Absent" is shown only
by a pass that rules out every place it could be. The owner, in [CASE-094](../cases.d/CASE-094.md):
"every brick in my collection is detectable if I have the time to go
through my entire collection, one at a time, checking every single brick."
With a deadline τ shorter than that pass, absence is never shown. The lab
form is Treisman and Gelade's target-absent trials ([LIT-1082](../literature.d/LIT-1082.md), read in
[NOTE-897](../notes.d/NOTE-897.md)). In serial search they took about twice the per-item time
of target-present trials, 67.1 against 28.7 ms per item, and even when a
present target popped out, absent responses grew with display size (25.1
against 3.1 ms per item).

**Two assumptions, which the rule makes together.** Reiter's closed-world
assumption ([LIT-1088](../literature.d/LIT-1088.md), read in [NOTE-899](../notes.d/NOTE-899.md), from his 1977 workshop report)
adds the negation of every ground atom the database does not entail. The
convention "presumes total knowledge about the domain being represented".
His own illustration is close to the medic's: "If I fail to find an entry
indicating that Air Canada flight 103 connects Vancouver with Toulouse I
will conclude that it does not." Clark's negation as failure ([LIT-1087](../literature.d/LIT-1087.md), read in
[NOTE-894](../notes.d/NOTE-894.md), from the author's posted scan) takes not-P as a lemma only
after "the exhaustive but unsuccessful search for a proof of P". His
soundness theorem makes that a consequence of the completed database:
every branch must end in failure, and a branch that never ends licenses
nothing. So there are two assumptions:

1. **The world is closed.** What is there would be in the database.
   Reiter's.
2. **The search finished.** Every place has been tried and failed.
   Clark's, required outright, not assumed.

A search cut off by a deadline satisfies neither. "If I can't find it, it
isn't there" acts on an unfinished search as negation as failure acts on a
finished one. It assumes both a closed world and that the part not
searched would have failed too. It is therefore stronger than either
inference, not one of them on a time bound, as first filed.

**When it is safe.** Let π be the prior that the item is present and h the
chance a search finds a present item within τ. Then, by Bayes,

P(present | not found by τ) = π(1 − h) / (π(1 − h) + 1 − π).

As h → 1 this goes to 0. An arrangement in which the full search finishes
within the deadline turns the second assumption from a gamble into a fact,
and the rule becomes Clark's: a labelled compartment, a bin of one's own,
or [CLAIM-307](CLAIM-307.md)'s carve. That is the time-bounded counterpart of Clark's conditions
under which evaluation terminates.

**Where it is not an inference at all.** In [CASE-085](../cases.d/CASE-085.md) the unit had been
checked: the EMT knew the drug was stocked, somewhere among the
compartments. That is a disjunction, and Reiter's Example 5.1 shows the
closed-world assumption made inconsistent by one (from Pa ∨ Pb it adds
both ¬Pa and ¬Pb). With that knowledge in the database, a proof of
presence succeeds and negation as failure refuses "it isn't there". So in
[CASE-085](../cases.d/CASE-085.md), with π near 1 and h low, the rule was a decision to stop
searching and change the request, not a conclusion about the drug.

## Why it is Active

The asymmetry and the formula are elementary. The two sources are read,
and the reading of the rule against them is now theirs: Reiter's
definition and his Example 5.1, and Clark's soundness theorem and its
finite-failure condition. That the medic's rule is a decision under a
deadline, not an inference, is [CLAIM-296](CLAIM-296.md)'s reading, which this claim
complements.

## What it does not say

- That the medic was wrong to move on. Under a deadline, stopping is part
  of using a resource ([CLAIM-296](CLAIM-296.md); A17 §4 in [CASE-085](../cases.d/CASE-085.md)).
- That absence can never be established. A complete arrangement, or an
  exhaustive pass in time, establishes it.
- That Reiter or Clark considered deadlines. Neither did. For Reiter,
  whether the database entails an atom does not depend on time, and the
  extension to search under a deadline is the record's.
