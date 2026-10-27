---
status: Active
title: 'The record''s own rates: over its first fifty days, measured from git, an entry''s prose is revised about once in 22 days once drafting is over, its status once in 128, an authored relation gained or lost once in 132 and an authored relation retracted once in about 600, while no relation type has been redeclared; the layers'' event rates are ordered as the exchange guessed, but only after the first day, when all of them change together, and the grammar is slow to revise without being slow to grow'
version: 2
history:
- version: 2
  date: '2026-10-27'
  note: >-
    Revised at the owner's review of the pull request: the title said the
    layers "separate" after the first day, which reads as a separation of
    time scales. It now says their event rates are ordered; a section
    distinguishes what the rates show from a dynamical hierarchy, and the
    "What it shows" bullets are worded as rates. The measurements are
    unchanged.
standing: documented
kind: executed-study
tags:
- design-rationale
- complex-systems
date: '2026-10-27'
illustrates:
- CLAIM-tmpoe0v5
- CLAIM-tmpmx2ql
line: nucleating-argument
summary: >-
  Run on 2026-10-27 at the owner's request ("run your measurements against
  the record"), for the rate reading A12 and A13 gave luria's layers and
  that [CLAIM-tmpl228b](../claims.d/CLAIM-tmpl228b.md) left untested. Every non-merge commit to this record,
  read by scratch/formal/record_rates.py at commit a357048. The ordering
  (prose, then standing, then relations, then the grammar's types) holds in
  aggregate rates, by one to two orders of magnitude. It does not hold in
  the first day after filing, or for every scheme, and the machine's
  validation runs at the rate of the edits it follows, not on a scale of its
  own.
---
<!-- inactive-ok-file: CLAIM-tmpoe0v5 CLAIM-tmpmx2ql CLAIM-tmpl228b — Proposed or new; the claims the measurement bears on -->

# CASE-tmpqou64: The record's own rates: over its first fifty days, measured from git, an entry's prose is revised about once in 22 days once drafting is over, its status once in 128, an authored relation gained or lost once in 132 and an authored relation retracted once in about 600, while no relation type has been redeclared; the layers' event rates are ordered as the exchange guessed, but only after the first day, when all of them change together, and the grammar is slow to revise without being slow to grow

## The case

A12 of the exchange "Field Existence Question" read luria's layers (prose
edits, validation, standing, relations, schema) as processes on separate time
scales, and warned: "There's no guarantee these processes possess numerically
well-separated timescales. That would need measurement." This is that
measurement, for this record.

**Method.** scratch/formal/record_rates.py reads every non-merge commit from
the initial commit (2026-09-07) to a357048 (2026-10-27): 1434 commits, 1019
authored and 415 by the docs bot. For each of the 5034 documents of a
declared scheme it follows identity through renames and concretization
(`formerly:`), and classes each commit's change to it:

- **body**, the prose below the frontmatter;
- **status**;
- **edge**, an authored relation field gaining or losing a target. Converses
  the fixer writes are excluded, and so are the bot's edge changes, which
  are mechanical;
- **body (bot)**, the docs bot's repairs, which is the record's validation.

A layer's rate is its changes after filing per object-day; τ is its
inverse. 44% of authored body changes fall within a day of filing, which is
drafting, so a settled τ is given over the time after that day. In
luria.yaml, a scheme, relation type or field is filed when it first appears
and changes when it is redeclared.

**Results**, all schemes (settled τ in parentheses):

| layer | changed after filing | τ | settled τ |
|---|---|---|---|
| body, authored | 64% | 12.9 d | 21.8 d |
| body, bot repair | 99% | 11.1 d | |
| status | 27% | 55.6 d | 127.5 d |
| edge gained or lost | 11% | 90.8 d | 131.9 d |
| edge retracted | 149 of 6632 | about 600 d | |
| field declared in luria.yaml | 3 of 39 | 58.5 d | |
| relation type declared in luria.yaml | 0 of 68 | none in 1317 type-days | |
| scheme declared in luria.yaml | 0 of 10 | none in 251 scheme-days | |

By scheme the ordering is not uniform:

- **LIT** status (settled τ 72 d) moves faster than its edges (1627 d),
  since a work's status is its reading life cycle.
- **CLAIM** edges (23 d) move far faster than its status (654 d). A claim
  gains `rests_on` and `grounds` as the argument around it grows, and its
  credence almost never changes.
- **QUESTION** and **CASE** status almost never changes at all.

The 149 retracted edges lived a median of 0.18 days: they are drafting
corrections, not revisions.

The grammar grows in bursts. 17 commits changed a scheme, relation type or
field, 0.34 a day, and 43 changed a vocabulary (31 of them `topics`).
Relation types were added on days 18, 25, 28, 31, 37, 41 and 45 of the
history, 47 of the 68 on day 31 (the argument schemes, [ADR-032](../decisions.d/ADR-032.md)). None has
been redeclared since its filing.

**Checks.** Authored file modifications under claims.d number 1817 against
the 1472 the three layers can account for; the rest touch only frontmatter
outside them (title, summary, version, history). Bot modifications and
renames number 1110 against the 868 bot body changes counted.

**Limits.**

- Fifty days. Every τ longer than that is an extrapolation from few events,
  and "none" is not a rate.
- The authors are the owner and Claude sessions, often in long single
  sessions, so commit timing reflects sessions as much as layers.
- A commit is the unit: two edits in one commit count once.
- The grammar measured is this record's luria.yaml. luria's own code, which
  holds the grammar of the grammar, is not measured; its pin changed four
  times.

## What it shows

- **The ordering A12 and A13 guessed holds in aggregate.** Prose is
  revised about six times as often as status or edges once drafting is
  over. An edge, once written, is retracted about thirty times less often
  than prose is revised, and a relation type has not been redeclared at
  all. The rigidity [CLAIM-tmpoe0v5](../claims.d/CLAIM-tmpoe0v5.md) demonstrates from the grammar shows in the
  rates too.
- **The ordering holds in the settled regime only.** In the
  first day after filing, body, status and edges all change: 35% of edge
  changes, 44% of body changes and 59% of status changes fall there. Layers on separate
  clocks would not have a regime in which every layer moves at once. These
  have one, at birth.
- **Validation has no rate of its own.** The bot's repairs
  follow the authored edits at nearly the same rate (11.1 d against
  12.9 d), because every push triggers one. Validation is slaved to editing,
  not a slower process constraining it.
- **The grammar is slow to revise, not slow to grow.** It gained a field or
  relation type on nine of the 32 days since luria.yaml was written. What is
  slow is redeclaration: once filed, a type stays as declared. That fits "constraints over faster activity" only if the
  constraint is the declared type, not the grammar as a whole.

## What the rates are evidence of

Added at the owner's review of the pull request, which asked that event
frequencies be kept apart from dynamical time-scale separation. Three
readings of these numbers differ in support:

| reading | status |
|---|---|
| **The layers' events occur at different rates.** | Demonstrated for this record's first fifty days, with the limits above. |
| **The layers are separate operating regimes**, worked on by different activities and under different checks. | Plausible and partly supported. Revisions of the grammar come by decision and lint enforces the declared types, but they occur inside the same work as filing ([CASE-tmp0zvle](CASE-tmp0zvle.md)). |
| **The layers are a dynamically generated hierarchy of time scales**, slow modes constraining fast ones as in [CLAIM-tmpmx2ql](../claims.d/CLAIM-tmpmx2ql.md). | An interpretation, not shown. |

On the third reading:
- **An inverse event rate is not a relaxation time.** A layer that rarely
  changes need not be a slow mode, and nothing here measures a spectral
  gap or a relaxation.
- **The history is short and not stationary.** The rates fell over the
  month as the grammar settled.
- **The counts mix kinds of event.** Authoring, bot repair, status
  transitions and schema changes are counted alike.
- **The rare changes arrive in shared work.** [CASE-tmp0zvle](CASE-tmp0zvle.md) found the rarer
  changes arriving in the same pull requests as ordinary document work.
  That fits threshold-triggered revisions within one workflow better than
  distinct processes running on separate clocks.

A study that could separate the readings would:
- give uncertainty for each rate;
- compare matched cohorts of entries filed at the same time and of the same
  kind;
- record what triggered each schema revision.

## What would change it

A longer history, in which a relation type is redeclared or a scheme
retired, would give the grammar's revision a rate instead of a bound. A
second record measured the same way (the anthology, strata-g) would say
whether these numbers belong to luria or to this record's way of being kept.

## Note of 2026-10-27 (later): the grammar's growth, by level

"The grammar is slow to revise, not slow to grow" is refined by [CASE-tmp0zvle](CASE-tmp0zvle.md),
which measures growth at each level at the owner's direction. Terms, scheme
members, vocabularies, schemes and remote projects are added at rates falling
in that order. They are added in the same pull requests as the documents that
need them, and the rates fell over the month.
