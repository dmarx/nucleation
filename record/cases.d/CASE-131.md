---
number: 131
status: Active
formerly:
- CASE-tmp8jhbm
title: 'The graph that asserted an inference nobody made: filing one claim as supporting another made the record''s link fixer write that the other rested on it, and the record answered by adding a relation'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by record-as-apparatus, at the split of that
    line (ADR-082). No other change.
standing: documented
kind: specimen
tags:
- design-rationale
- epistemology
date: '2026-10-22'
line:
- record-as-apparatus
illustrates:
- CLAIM-181
summary: >-
  The record's own history, as A18 of the exchange of 2026-10-22 read it at
  the owner's prompting (U18): "the pre-existing representation didn't
  merely omit information; it positively misrepresented an inference". It
  is a move the grammar could not hold, caught and answered by amending the
  grammar. Not shown: that such moves are always caught.
---
<!-- inactive-ok-file: CLAIM-181 — Proposed; claims, questions, terms and readings cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: ARG-tmp8fx47 CASE-tmppm4do CLAIM-tmpefs1h — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->

# CASE-131: The graph that asserted an inference nobody made: filing one claim as supporting another made the record's link fixer write that the other rested on it, and the record answered by adding a relation

## The case

On 2026-10-15, while porting the LEGO material, a claim ([CLAIM-310](../claims.d/CLAIM-310.md)) was
filed with `supports: CLAIM-296`, because it gave evidence for [CLAIM-296](../claims.d/CLAIM-296.md).
`luria link --fix` wrote the converse, `rests_on`, onto [CLAIM-296](../claims.d/CLAIM-296.md). That
said [CLAIM-296](../claims.d/CLAIM-296.md) could not stand without the new claim, which was false:
[CLAIM-296](../claims.d/CLAIM-296.md) had been argued before it existed. The relation was removed
before the merge. [ADR-044](../decisions.d/ADR-044.md) added `corroborates`, for evidence one claim
gives another without the other depending on it, and kept it out of the
`argument` chain. [CLAIM-310](../claims.d/CLAIM-310.md) now corroborates [CLAIM-296](../claims.d/CLAIM-296.md).

## What it shows

The owner, at U18: "when we've encountered representational challenges,
we've generally interpreted those as a symptom of a represntational
weakness of the record and used that opportunity to mature the luria
configuration, featureset, or both." A18 found this the strongest
documented instance: "the pre-existing representation didn't merely omit
information; it positively misrepresented an inference."

So it is the kind of move [CLAIM-181](../claims.d/CLAIM-181.md) says is "either forced into one or
lost", and it was neither: it was forced, noticed because the forcing
produced a false statement, and the grammar was amended. That is the
evidence [CLAIM-419](../claims.d/CLAIM-419.md) rests on. It is also [CLAIM-181](../claims.d/CLAIM-181.md)'s evidence, since
the grammar did force the move before it was amended.

## What it does not show

That forcing is always noticed. This one was noticed because the false
converse was written somewhere visible. A move forced into a shape that
produces nothing false would leave no trace.

## Note of 2026-11-12: the case as the seed of a benchmark, and what a migration should keep, from "luria experiment design"

Every evaluation of governed schema change in the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) starts from this case,
and A's account of it is accurate: A27, A29 and A39 Study D (start before
[ADR-044](../decisions.d/ADR-044.md), score the semantic property, not the field name); A31 and A39
§5 D5 (three agents who meet the misfit from different sides); A36 E8 (an
object, a representational and a governance failure); and A45 §4, which
writes four versions of it: the relation exists and is misfiled; it is
absent; it is proposed and the acceptance procedure rejects new relations;
and the review procedure has been altered so it no longer catches false
inferred dependencies. [CASE-tmppm4do](CASE-tmppm4do.md) gathers the design.

A25 drew a further consequence: "Preserving the original graph exactly
would preserve the false dependency in CASE-131." That is filed as
[CLAIM-tmpefs1h](../claims.d/CLAIM-tmpefs1h.md), with [ARG-tmp8fx47](../arguments.d/ARG-tmp8fx47.md). This case's "What it does not show" is
also A25's methodological point: a schema history "cannot tell us how many
contributions were misclassified or abandoned because they did not fit".
