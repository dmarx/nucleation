---
status: Proposed
title: 'Each directed relation is stored on one side only, the side a filer writes, and its converse is derived when the record is read; the sweep that removes the stored converses is this decision''s demonstration'
version: 1
tags:
- record
date: '2026-11-07'
summary: >-
  Every directed relation in the record was stored twice, once on each end,
  and `luria link --fix` kept the second copy in step. About 2,770 values in
  1,260 entries were such copies. Adding a relation to a new scheme, as the
  SYNTHESIS scheme needed, meant widening the stored converse on every
  target scheme. luria 1.10.0, which CI pins, can mark one side of a pair
  `derived`: only the other side is written, readers compute the converse,
  and `luria repair` moves anything written on the derived side to the
  primary side of the other entry. This decision marks the derived side of
  every directed pair, 32 field declarations, choosing the side the
  config's own blurbs already describe as written by `luria link --fix`.
  Symmetric relations (`complements`, `rivals`, `compared_against`) stay as
  they are, since luria never derives them. Rejected: keeping both sides;
  choosing the derived side pair by pair on a different principle; a
  partial switch.
---
<!-- inactive-ok-file: ADR-076 ADR-tmpdne5p — Proposed or new; the scheme and the decision whose converse widening prompted this -->

# ADR-tmp53l4u: Each directed relation is stored on one side only, the side a filer writes, and its converse is derived when the record is read; the sweep that removes the stored converses is this decision's demonstration

## Context

The record's relations come in converse pairs: `rests_on` and `supports`,
`illustrates` and `illustrated_by`, `superseded_by` and `supersedes`, and
sixteen more, nineteen directed pairs in all. Both sides were stored in front matter, and `luria link --fix`,
run by the pull request's CI, wrote whichever side a filer left out. On
2026-11-07 the stored converses came to about 2,770 values in about 1,260
entries. The largest were QUESTION `bearing`, CLAIM `supports` and TERM
`used_by`, at 280 each.

That cost showed in three ways.

- **Every edit touched two files.** A filing that cites a term, or grounds a
  claim on a reading, changed the cited entry too. The bot's repair commit
  made those second edits, and they conflicted with other branches.
- **Stored copies could disagree.** 129 values were written only on the
  converse side, most of them CLAIM `corroborated_by` naming a reading whose
  `corroborates` lacked the claim. Four more named codes that no longer exist
  (LIT-862, LIT-863, LIT-1542 and LIT-1171 carried old-style codes for
  LIT-860, LIT-002 and LIT-048).
- **A new scheme widened every target.** ADR-tmpdne5p gave SYNTHESIS
  `grounds`, `uses` and `corroborated_by`, and had to widen six stored
  converses on five other schemes to accept it.

luria 1.10.0 lets a pair mark one side `derived`. That side is never stored.
Readers compute it from the converse, and `luria repair` moves an entry
written on it to the primary side of the other document, or drops it where
the primary already holds it. Exactly one side of a directed pair may say so.
The owner asked for the switch on 2026-11-07.

## Decision

- **Mark the derived side of every directed pair**, 32 field declarations
  in `luria.yaml`. The primary side, the one a filer writes, is the side
  that states the relation from the entry that makes it:
  - `rests_on`, `grounds`, `uses`;
  - `illustrates`, `counterexample_to`, `concludes`, `undercuts`,
    `objects_to`;
  - `answers`, `bears_on`, `refines`, `extends`, `corrects`, `presupposes`,
    `corroborates`, `reported_in`, `variant_of`, `substitutes_for`;
  - `superseded_by`, which the status `Superseded` already requires.

  Their converses are derived. This is the side the config's own blurbs
  already called "written by `luria link --fix`", so no pair changes meaning.
- **Symmetric relations are unchanged.** `complements`, `rivals` and
  `compared_against` are their own converse; luria never derives them, and
  `link --fix` still writes both ends.
- **A derived field is still declared,** so the converse names every scheme
  that may hold the relation. A new scheme still widens those declarations,
  as ADR-tmpdne5p did; what changes is that nothing is stored there.
- **The sweep is the demonstration (ADR-071).** This pull request changes
  only the config and fixes the four broken codes. CI's `luria repair` then
  drops the stored converses that the primary side already holds, and
  moves the 129 that it does not onto the primary side of the entry
  named. That bot commit is the evidence that the switch loses nothing.
- **Filers write only the primary side.** The TERM template's comment on
  supersession now points to `superseded_by` on the replaced term. The
  `synthesis-review` skill no longer asks for `corroborated_by` to be
  carried.

## Alternatives considered

- **Keep both sides.** This costs nothing now, but every filing keeps
  editing two files, and stored copies keep drifting until a repair notices.
- **Choose the derived side pair by pair on another principle,** such as the
  side with fewer values. That would invert pairs whose stored side carries
  meaning: `superseded_by` is required by the status `Superseded`, and
  `concludes` is required on every ARG.
- **Switch only the largest pairs.** Some pairs would then be derived and
  others stored twice, and a filer would have to know which. The rule is
  simple only if it covers every directed pair.

## Consequences

- An entry's own front matter no longer lists what points at it. Its
  generated page, and any view, still shows the derived side. Reading the
  source alone, find the inbound edges with a search or with `luria`.
- The sweep is one large bot commit, about 1,260 files, mostly deletions,
  with additions to the entries that receive the 129 moved values.
  Branches open at the time will conflict wherever they edited a derived
  field. The resolution is to drop the derived-side lines and keep the
  primary side.
- `luria link --fix` now has little to write except symmetric pairs, so CI's
  repair commits on later pull requests should be smaller.
