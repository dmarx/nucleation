---
number: 995
status: Proposed
formerly:
- CLAIM-tmpym9ng
title: 'The record''s checks are conservative'
statement: >-
  The record's own checks, lint, docs-check and review, are conservative:
  each passes only what it can show passes, so a failed check does not by
  itself say the entry is at fault; the fault may lie in the entry, in the
  vocabulary the check can express, or in the check, and telling them apart
  is a separate step
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A check of the record that is exact for what it tests, so that every
  entry it fails does fail the predicate it stands for; or a record of
  failed checks in which the fault was in the entry every time, with no
  case traced to the vocabulary or the check.
tags:
- epistemology
- software-engineering
date: '2026-11-22'
line:
- record-as-apparatus
- formal-apparatus
grounds:
- THEORY-2262
complements:
- CLAIM-975
- CLAIM-984
uses:
- TERM-153
- TERM-151
summary: >-
  Offered by the Liquid Types reader and filed under the dialectic regime,
  2026-11-22. Rondon, Kawaguchi and Jhala trace a failed check to "an
  inappropriate choice of qualifiers or the conservativeness of our
  notion of subtyping" as well as to the program ([THEORY-2262](../theory.d/THEORY-2262.md);
  [CLAIM-975](CLAIM-975.md) for their system). This carries that three-way ambiguity
  to the record's own checks. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2262 CLAIM-975 CLAIM-984 — Proposed; the reading and entries this is stated against -->

# CLAIM-995: The record's checks are conservative

## The claim

A liquid-type checker fails a safe program when its qualifiers cannot
state the invariant or its subtyping is too weak to prove it, and the
paper leaves telling these apart from a real fault to future work. The
record's checks have the same shape:

- **The entry**: a code in a title, a missing source, a tag outside the
  vocabulary. The usual case, and the one the check is for.
- **The vocabulary**: a closed list without the word the entry needs.
  CLAUDE.md already says such a word is added by decision, "never
  replaced by the nearest wrong one": a vocabulary failure, handled as
  one.
- **The check**: a guard that misfires; the luria repository's own rule
  that a guard catching the same mistake twice is a bug report on the
  workflow.

So a failed check is evidence about three things, not one, and the move
that makes it pass is outside the check, as in all three systems read
for [LEAD-215](../leads.d/LEAD-215.md): fix the entry, extend the vocabulary by decision, or
repair the check.

## Bearing

[CLAIM-984](CLAIM-984.md) says a closed vocabulary is what lets a check infer; this
says the same closure is a source of failures that are not the entry's.
