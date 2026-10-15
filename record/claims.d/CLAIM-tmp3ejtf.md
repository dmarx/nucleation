---
status: Proposed
title: 'Under a deadline, search can establish that an item is present by finding
  one, but can establish absence only by exhausting the collection, so "If I can''t
  find it, it isn''t there" is negation as failure, a closed-world assumption taken
  on a time bound: a default that is safe exactly when the arrangement makes retrieval
  complete within the deadline'
version: 1
role: thesis
defeated_if: >-
  A search procedure, under a deadline shorter than an exhaustive pass, whose failure
  to find an item entails its absence without a completeness assumption about the
  arrangement. Or a case in which the medic's rule was applied and no assumption
  that a present item would have been found was in play.
tags:
- logic
- information-retrieval
- cognition
date: '2026-10-15'
line: distributed-agency
uses:
- TERM-055
grounds:
- CASE-085
- CASE-tmpd5exw
complements:
- CLAIM-296
summary: >-
  The medic's "If I can't find it, it isn't there" ([CASE-085](../cases.d/CASE-085.md)) and the owner's "if
  I can't find it quickly enough, it may as well not be there" ([CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)) both
  act on a failed search as if it showed absence. One find shows presence. Absence
  can be shown only by checking everything, which a deadline forbids. Treisman and
  Gelade's target-absent scans are the cost of that asymmetry in the lab. Acting
  on failure to find is what database theory calls the closed-world assumption (Reiter
  1978) and logic programming negation as failure (Clark 1978). Both are sound only
  relative to a completeness assumption. So the rule is a default, and what makes
  it safe is an arrangement in which a present item would have been found in time.
  Proposed: Reiter and Clark are registered unread.
---
<!-- inactive-ok-file: CLAIM-296 — Proposed; open claims cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmpj4tnh LIT-tmpix3rp — Deferred; works registered unread, cited for what they would be read for, not leaned on -->

# CLAIM-tmp3ejtf: Under a deadline, search can establish that an item is present by finding one, but can establish absence only by exhausting the collection, so "If I can't find it, it isn't there" is negation as failure, a closed-world assumption taken on a time bound: a default that is safe exactly when the arrangement makes retrieval complete within the deadline

## The claim

**The asymmetry.** "Present" is shown by one find. "Absent" is shown only
by a pass that rules out every place it could be. The owner, in [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md):
"every brick in my collection is detectable if I have the time to go
through my entire collection, one at a time, checking every single brick."
With a deadline τ shorter than that pass, absence is never shown. The lab
form is Treisman and Gelade's target-absent trials ([LIT-tmp9g55n](../literature.d/LIT-tmp9g55n.md), read in
[NOTE-tmpe7gfj](../notes.d/NOTE-tmpe7gfj.md)). In serial search they took about twice the per-item time
of target-present trials, 67.1 against 28.7 ms per item, and even when a
present target popped out, absent responses grew with display size (25.1
against 3.1 ms per item).

**The rule acts on failure as if on absence.** The medic's "If I can't
find it, it isn't there" ([CASE-085](../cases.d/CASE-085.md)) is false of the inventory ([CLAIM-296](CLAIM-296.md))
and right of the decision ([TERM-055](../terms.d/TERM-055.md)). In database theory, treating what
cannot be derived as false is the closed-world assumption. In logic
programming, inferring not-p from a failed attempt to prove p is negation
as failure. Both are standardly described as sound only relative to a
completeness assumption: that whatever is true would have been found, the
database or program being complete for the relevant facts (Reiter 1978,
[LIT-tmpj4tnh](../literature.d/LIT-tmpj4tnh.md); Clark 1978, [LIT-tmpix3rp](../literature.d/LIT-tmpix3rp.md); registered here unread).

**So the rule is a default whose safety is a property of the
arrangement.** Let π be the prior that the item is present and h the
chance a search finds a present item within τ. Then, by Bayes,

P(present | not found by τ) = π(1 − h) / (π(1 − h) + 1 − π).

As h → 1 this goes to 0, and the closed-world inference becomes safe. An
arrangement that makes retrieval complete within the deadline (a labelled
compartment, a bin of one's own, [CLAIM-tmp6u639](CLAIM-tmp6u639.md)'s carve) is what turns a failed
search into evidence of absence. In [CASE-085](../cases.d/CASE-085.md) the unit was stocked and the
EMT knew it, so π was near 1 and h low. The posterior stayed high, and
"it isn't there" was a decision to stop searching, not a finding.

## Why it is Proposed

The asymmetry and the formula are elementary. The reading of the medic's
rule as the closed-world assumption is the record's. The two sources it
names for soundness conditions are registered and not read.

## What it does not say

- That the medic was wrong to move on. Under a deadline, stopping is part
  of using a resource ([CLAIM-296](CLAIM-296.md); A17 §4 in [CASE-085](../cases.d/CASE-085.md)).
- That absence can never be established. A complete arrangement, or an
  exhaustive pass in time, establishes it.
