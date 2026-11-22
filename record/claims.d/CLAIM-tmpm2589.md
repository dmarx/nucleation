---
number: tmpm2589
status: Proposed
formerly:
- CLAIM-tmpm2589
title: 'At a fixed level and target the self-consistent factorizations into agents form a nested hierarchy of coarsenings of a unique finest partition: two factorizations can never disagree on co-grouping strongly-coupled regimes, so the only non-uniqueness is grain, which the admission test alone does not fix'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A fixed coupling matrix at a fixed level and target with two
  self-consistent factorizations into agents that crosscut: two regimes in
  one agent together and in different agents in the other, with neither
  factorization a coarsening of the other. Equivalently, a self-consistent
  family that is not a chain under refinement. A merely nested pair (one
  splits what the other merges) does not count: that is the grain
  multiplicity this claim reports, not a crosscut.
tags:
- individuation
- agency
- model-comparison
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
bears_on:
- QUESTION-032
- QUESTION-035
complements:
- CLAIM-170
- CLAIM-174
grounds:
- CASE-tmprh6pl
uses:
- TERM-tmpdlwl8
- TERM-044
- TERM-049
summary: >-
  The assistant's answer to LEAD-109, demonstrated in [CASE-tmprh6pl](../cases.d/CASE-tmprh6pl.md).
  Fix a level and target. The admission test's first condition
  ([CLAIM-157](CLAIM-157.md), [CLAIM-174](CLAIM-174.md)) admits a block only when it is a
  near-decomposable cluster; the partitions that clear it are exactly cuts
  of the coupling's single-linkage hierarchy, so any two are nested and
  none crosscut. Hence a fixed level and target CAN have several
  self-consistent factorizations, but only as coarsenings of one another
  about a unique finest partition, never as a crosscutting disagreement.
  [CLAIM-170](CLAIM-170.md)'s defeater (two factorizations disagreeing on which
  regimes each agent governs, nothing to choose) is not met in the strong
  sense; what remains is the choice of grain, which the level and target
  as stated do not fix. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-170 CLAIM-174 CLAIM-168 — Proposed; the admission test, the owner's thesis and the objections this claim settles a part of, open -->
<!-- inactive-ok-file: TERM-tmpdlwl8 CASE-tmprh6pl — new in this contribution; the distinction and the study this claim rests on -->

# CLAIM-tmpm2589: At a fixed level and target the self-consistent factorizations into agents form a nested hierarchy of coarsenings of a unique finest partition: two factorizations can never disagree on co-grouping strongly-coupled regimes, so the only non-uniqueness is grain, which the admission test alone does not fix

## The claim

Fix a level of description (a set of regimes and their coupling) and a
target. A factorization is self-consistent when every block passes the
admission test ([CLAIM-174](CLAIM-174.md)). Its binding condition is the first test:
a block is one system only when it is a near-decomposable cluster, strong
within and weak across, with a gap beating the Occam threshold
([CLAIM-157](CLAIM-157.md), [CLAIM-154](CLAIM-154.md)).

The partitions that clear that test are exactly the **cuts of the
coupling's single-linkage dendrogram** ([CASE-tmprh6pl](../cases.d/CASE-tmprh6pl.md)): a block
must be internally connected by couplings stronger than every coupling it
cuts, which is single linkage. Cuts of one dendrogram are **totally
nested**. Therefore:

1. **No crosscutting.** Two self-consistent factorizations can never
   disagree by placing a strongly-coupled pair in one agent and in
   different agents the other way. Any two are nested: one is a coarsening
   of the other ([TERM-tmpdlwl8](../terms.d/TERM-tmpdlwl8.md)).
2. **A unique finest factorization.** Under test 1 alone a lone regime is
   trivially one system, so the finest clearing partition is all
   singletons; adding tests 2–3 (an agent, not a device, [CLAIM-154](CLAIM-154.md)'s
   gate) raises that floor to the finest grouping whose every block earns
   agenthood. Either way the finest member is unique.
3. **Grain is the only multiplicity.** What a fixed level and target leave
   open is how coarse to go: a regime may be its own agent or a part of a
   larger one, and both can be self-consistent. Tests 2–3 only prune this
   chain; they never create a crosscut.

## What it settles, and what it leaves to the owner

- **LEAD-109.** A fixed level and target *can* carry several self-consistent
  factorizations (the open part of [CLAIM-168](CLAIM-168.md) and [CLAIM-174](CLAIM-174.md) is
  answered: the fixed-point condition has, in general, more than one
  solution). But the solutions are a nested hierarchy, not a crosscutting
  disagreement.
- **[CLAIM-170](CLAIM-170.md)'s `defeated_if`** asks for "two equally good factorizations
  into agents that disagree on which regimes each agent's will-organization
  governs, with nothing at that level to choose between them." Read as a
  crosscut, it is **not met**: the thesis survives. Read as a nested pair
  (one agent vs two), it *is* realized, and whether "nothing at that level
  chooses" is then a matter of what "level" fixes.
- **The owner's call.** Three ways to treat the surviving grain
  multiplicity, filed as alternatives, not chosen:
  - **(A) Fix the grain in "level".** Define a level of description to
    include its grain of partition, so the fine and coarse factorizations
    are *different* levels (as [CLAIM-170](CLAIM-170.md)'s room-vs-pair already reads).
    Then each level has a unique factorization and the defeater cannot
    arise. Cost: "level" must carry a grain parameter the record has not
    stated.
  - **(B) Add a selection rule to the admission test.** Keep one grain per
    level by a rule — the finest clearing partition, or the coarsening that
    maximizes total evidence (summed [CLAIM-154](CLAIM-154.md) margins). Cost: a new
    criterion, to be justified.
  - **(C) Accept the nested family as the level-relativity.** Hold, with
    [CLAIM-174](CLAIM-174.md), that coexisting nested grains are the predicted
    relativity, not a defect, and that uniqueness of co-grouping is all the
    thesis needs. Cost: "the agents" of a system is a hierarchy, not a
    single partition.

## What it does not say

- **That tests 2–3 are faithfully computed.** [CASE-tmprh6pl](../cases.d/CASE-tmprh6pl.md) enumerates
  test 1 exactly and stipulates per-block verdicts for tests 2–3; it does
  not run Orseau et al.'s or Kenton et al.'s comparisons on dynamics. The
  nesting result needs only that tests 2–3 are per-block gates (monotone
  filters on the test-1 chain), which they are as stated.
- **That coupling is symmetric or static in general.** The demonstration
  uses a symmetric non-negative matrix. One-way drive ([CLAIM-167](CLAIM-167.md)) and
  the storage route ([CLAIM-157](CLAIM-157.md)'s time-lagged case) are not covered; a
  directed coupling can break the single-linkage reading, which is named as
  a limit and a lead for later.
- **That grain multiplicity is harmless.** Whether it is tolerable is
  exactly the owner's choice above.
