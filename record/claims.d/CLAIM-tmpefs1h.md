---
status: Proposed
title: 'A migration of the record''s grammar is faithful when it preserves the record''s accountability structure, not its old graph: where the old grammar forced a relation nobody asserted, a faithful migration removes it'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A migration that preserves every justified commitment, its grounds, its
  challenges and its revision history, and still loses something the
  record needed, such as an entry's meaning to a reader of its old
  citations, so that preserving the old graph or the old text was needed
  after all; or a migration that keeps the old graph and is not unfaithful
  in any respect the record cares about, where the old grammar forced a
  relation nobody asserted. Also defeated if it only restates CLAIM-250
  with nothing added about grammar changes. Not defeated by migrations
  that change no relation's meaning, such as a rename, where preserving
  the graph and preserving the accountability structure coincide.
tags:
- epistemology
- design-rationale
- databases
date: '2026-11-12'
line:
- records-of-inquiry
- record-as-apparatus
rests_on:
- CLAIM-250
grounds:
- CASE-131
bears_on:
- QUESTION-tmps5iou
summary: >-
  A's, at A25 §"A further inspiration from the translation line" of the
  exchange "luria experiment design" (2026-11-10), answering the owner's
  U9 ("you might also derive some inspiration from some of the lines of
  argument on the Nucleation record"). A asks "What should a migration
  preserve when the old schema was itself conceptually mistaken?" and
  offers, as "a new synthesis, not an established Nucleation result", that
  it should preserve the record's "justified commitments and
  accountability relationships". It carries CLAIM-250, which defines
  fidelity through revision of an argument's content over its
  accountability structure, to revisions of the grammar. CASE-131 is the
  instance where preserving the graph would have kept a false dependency
  (ARG-tmp8fx47). The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-tmp8fx47 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ADR-082 CLAIM-250 — Proposed; cited for what each holds, not as settled -->

# CLAIM-tmpefs1h: A migration of the record's grammar is faithful when it preserves the record's accountability structure, not its old graph: where the old grammar forced a relation nobody asserted, a faithful migration removes it

## The claim

From A25 of the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda). A:
"Preserving the original graph exactly would preserve the false dependency
in CASE-131. Simply preserving the text would not ensure that the revised
system retains the intended relationship."

When the record's grammar changes, existing entries are migrated: moved
between schemes (ADR-061's support judgements went from CLAIM to ARG),
relinked under a new relation (ADR-044), reassigned to a split line
(ADR-082). Two criteria of a faithful migration suggest themselves and
both fail:

- **Preserve the graph.** Keep every relation, renamed into the new
  grammar. Where the old grammar forced a relation nobody asserted, as
  CASE-131's link fixer wrote a `rests_on` from an evidential `supports`,
  this carries the false statement into the new grammar.
- **Preserve the text.** Keep every body and title. The relations, which
  say what follows when an entry is retired, are not in the text, so this
  does not keep them.

The criterion the claim proposes is CLAIM-250's, applied to the grammar:
keep what was asserted, by whom, on what grounds, how it was challenged,
and what justified each revision; let the relations the old grammar forced
without anyone asserting them go. A migration is then judged against the
argument as made, not against its old encoding.

## What it adds to CLAIM-250

CLAIM-250 is about a developing argument's content changing under a fixed
grammar. This is about the grammar changing under a fixed argument, and it
says what a migration may drop: a relation that encoded no one's
assertion. That needs a test of which relations were asserted, which the
record can apply only where the history shows how a relation came to be
written (CASE-131's came from a converse the tool wrote).

## What it does not say

- Not that migrations should be free to drop relations. A relation someone
  asserted is part of the accountability structure and survives, even if
  the new grammar would encode it differently.
- Not how to tell, in general, a forced relation from an asserted one.
  CASE-131's "What it does not show" holds that a forced move producing
  nothing false leaves no trace.
