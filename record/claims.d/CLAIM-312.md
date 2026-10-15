---
number: 312
status: Active
formerly:
- CLAIM-tmpfpvgq
title: '"If I can''t find it, it isn''t there" asserts operational unavailability, that the item will not be put to use before the deadline, not absence: a search that fails by the deadline establishes unavailability outright, and licenses absence only with a certificate that the unsearched remainder cannot hold the item, from exhaustion, from an invariant of the arrangement, or from a closed-world default'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Evidence that users of the rule mean literal absence: that, told the item
  was present but out of reach by the deadline, they withdraw the statement
  rather than keep it, or that they act on it only in ways absence licenses
  (writing the item off, reordering, telling others not to look) and never in
  ways unavailability licenses (stopping, substituting, changing the request).
  Or a search that licenses absence from part of a collection with no
  certificate about the rest.
tags:
- logic
- databases
- cognition
date: '2026-10-15'
line: distributed-agency
uses:
- TERM-055
supersedes:
- CLAIM-306
rests_on:
- CLAIM-311
grounds:
- CASE-085
- CASE-094
- THEORY-341
- THEORY-340
- THEORY-363
- THEORY-374
complements:
- CLAIM-296
summary: >-
  Restates [CLAIM-306](CLAIM-306.md) at the owner's request, after [CLAIM-311](CLAIM-311.md) showed that
  absence can be established without exhausting a collection. The owner's own
  wording in [CASE-094](../cases.d/CASE-094.md), "it may as well not be there", is hyperbole for
  operational availability ([TERM-055](../terms.d/TERM-055.md)), not a claim about inventory. Read so,
  the rule reports an outcome and needs no default. [CLAIM-306](CLAIM-306.md)'s analysis
  survives as the account of the literal reading: what a failed search must be
  joined with before it licenses absence. The gap between the two readings is
  [CLAIM-306](CLAIM-306.md)'s Bayes term, and it matters when the statement is passed to
  someone who will act on presence.
---
<!-- inactive-ok-file: CLAIM-296 THEORY-374 — Proposed; an open claim cited as complementary, and a survey's account cited as such -->

# CLAIM-312: "If I can't find it, it isn't there" asserts operational unavailability, that the item will not be put to use before the deadline, not absence: a search that fails by the deadline establishes unavailability outright, and licenses absence only with a certificate that the unsearched remainder cannot hold the item, from exhaustion, from an invariant of the arrangement, or from a closed-world default

## The claim

**Three statements, not one.** Let C be the collection, x the item, τ the
deadline, and S_τ the part of C a search has examined by τ.

- **Present:** x ∈ C.
- **Found by τ:** x ∈ S_τ, and the searcher recognized it.
- **Available by τ:** the chance that the system, given the cue it has,
  deploys x for the task before τ ([TERM-055](../terms.d/TERM-055.md)'s α).

"If I can't find it, it isn't there" is said when Found by τ fails. The
owner's version in [CASE-094](../cases.d/CASE-094.md) says what is meant: "if I can't find it
quickly enough, it may as well not be there". That is a statement about
availability, put as a statement about presence for emphasis. [TERM-055](../terms.d/TERM-055.md)
already records the reading: "literally false as a claim about
inventory, but potentially correct as an operational equivalence."

**Read as unavailability, the rule needs no default.** A search that has
not found x by τ has not deployed it by τ. That is an outcome, not an
inference, and it is what the task needs to know: stop, substitute, or
change the request. It is also one observation of α for this request,
and repeated failures are evidence that α is low for this arrangement and
this cue.

**Read as absence, it needs a certificate.** Not found by τ licenses
x ∉ C only when something shows that x ∉ C \ S_τ. Three things can:

1. **Exhaustion.** S_τ = C. This is Clark's finite failure: negation as
   failure is sound only after "the exhaustive but unsuccessful search for
   a proof" ([THEORY-341](../theory.d/THEORY-341.md)).
2. **An invariant of the arrangement.** A sorted table, an index or a
   labelled compartment bounds what the remainder can hold, so part of a
   search can prove absence ([THEORY-340](../theory.d/THEORY-340.md), [THEORY-363](../theory.d/THEORY-363.md); [CLAIM-311](CLAIM-311.md)).
3. **A closed-world default.** Reiter's assumption that what is not
   entailed is false ([THEORY-341](../theory.d/THEORY-341.md)). It is a default, not a proof, and it is
   inconsistent when the database holds a disjunction such as "the drug is
   in one of these compartments". It is not even cheap in general: by
   Halevy's account of later work, deciding what follows from stored partial
   views is co-NP-hard under the closed-world assumption even for
   conjunctive views, where it is often polynomial under the open-world
   one ([THEORY-374](../theory.d/THEORY-374.md), from a survey's report).

[CLAIM-306](CLAIM-306.md) assumed only the first and third, and so concluded that absence
needs exhaustion and that the rule, read literally, is stronger than
either the closed-world assumption or negation as failure. Under the
literal reading with no certificate, that conclusion stands.

**When the gap between the readings matters.** By Bayes,
P(present | not found by τ) = π(1 − h) / (π(1 − h) + 1 − π), where π is
the prior that x is present and h the chance a search finds a present
item by τ. That is the probability that "it isn't there" is false as an
inventory claim while true as an availability claim. The hyperbole is
harmless when the act it prompts is one unavailability licenses. In
[CASE-085](../cases.d/CASE-085.md) the medic stopped searching and asked for something else. It
is harmful when the statement travels to someone who acts on presence,
such as the next shift, which then does not look, or a stock record,
which then reorders. The same sentence is then a closed-world claim made
on someone else's behalf.

## What it does not say

- That the medic was wrong to move on. Under a deadline, stopping is part
  of using a resource ([CLAIM-296](CLAIM-296.md); [CASE-085](../cases.d/CASE-085.md)).
- That availability is all that matters. Whether a further search could
  pay depends on presence, through π.
- That every speaker of the rule means availability. The claim is about
  the owner's usage and the medic's case, where the context makes the
  operational reading the natural one.
- That Reiter or Clark considered deadlines. The extension to search
  under a deadline is the record's.

## What it replaces

[CLAIM-306](CLAIM-306.md) is superseded. Its account of the two assumptions, of the
disjunction in [CASE-085](../cases.d/CASE-085.md), and of the Bayes term is kept above as the
analysis of the literal reading. Its claim that absence is shown "only by
exhausting the collection" is withdrawn ([CLAIM-311](CLAIM-311.md)).
