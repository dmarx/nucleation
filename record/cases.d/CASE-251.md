---
number: 251
status: Proposed
formerly:
- CASE-tmp8rg2s
title: 'A proposed study of curation completeness: an agent given a source and the record as it stood before a filing produces the filing''s accounting, scored against the filing together with its later corrections'
version: 1
standing: stipulated
kind: proposed-study
tags:
- epistemology
- design-rationale
date: '2026-11-12'
line:
- records-of-inquiry
- record-as-apparatus
bears_on:
- QUESTION-108
summary: >-
  The filer's own idea, offered after filing the exchange "luria experiment
  design" (2026-11-10) and accepted by the owner. A20 of that exchange
  proposed "curation completeness" as one task of an evaluation of the
  record: given a source discussion, identify what was filed, already
  represented or left unfiled. The record's own history supplies ground
  truth for it: filings whose accounting was later found incomplete, and
  the corrections that found the gaps. The documented part is those
  episodes; the study is stipulated and not run. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpssuha CLAIM-tmpj6pb6 — new; the curation-completeness pilot and the claim filed from it, cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: LIT-2293 — Superseded by LIT-1399; cited as the duplicate the episode's correction found -->
<!-- inactive-ok-file: LIT-1399 — Proposed, Unavailable; cited for what each holds, not as settled -->

# CASE-251: A proposed study of curation completeness: an agent given a source and the record as it stood before a filing produces the filing's accounting, scored against the filing together with its later corrections

## The case

[ADR-068](../decisions.d/ADR-068.md)'s seventh invariant is that nothing is dropped silently: whatever a
source contains is filed, mapped to a held code, or listed as left. Whether
a filer, or an agent equipped with the record, actually meets it can be
measured on episodes the record already holds.

**The episodes.** Filings whose accounting a later pass corrected. Three
from one week:

- The registration of 2026-11-10 (curation entry 2026/11/10/182452) of the
  works cited in "luria experiment design". The pass of 2026-11-12
  (curation entry 2026/11/12/021453) found 35 further works with
  verifiable identifiers that it neither registered nor listed as left:
  33 now registered, and two verified but held back for want of a topic
  word. The same entry's own correction found that one registered work,
  [LIT-2293](../literature.d/LIT-2293.md), duplicated [LIT-1399](../literature.d/LIT-1399.md), caught by lint once its DOI was added.
- The filing of "Individuation, Possibility, and Disposition" (curation
  entry 2026/11/07/015133), whose ARGs were filed only at the owner's
  review, because the filers' brief left out the rule that asks for them,
  and whose "left" section said syntheses were not filed when they had
  been; both corrections are recorded in the entry.

Others are found the same way: a curation entry with a dated correction,
or a later pass that registers works from a source an earlier pass
claimed to have accounted for.

**The task.** Give an agent the source and a checkout of the record at the
commit before the filing. Ask for the filing's accounting: each work and
idea of the source as held (with its code), to be filed, or left (with a
reason).

**The score.** Against the union of what the filing accounted for and what
its corrections added: omissions (items in neither the agent's three
lists), duplicates (an item proposed for filing that is held), and
misattributions (an owner's idea credited to the assistant or the
reverse). Arms: the agent with the record and the `read-and-file` skill,
the record without the skill, and the source with plain text search over
the record.

## What it can and cannot show

The ground truth is the record's own later corrections, so recall is
measured against a lower bound: an omission no later pass noticed is not
in it. That is [CLAIM-266](../claims.d/CLAIM-266.md)'s limit on any evaluation scored by the
evaluated system's own probes. The study therefore needs an independent
annotator's accounting of a sample of sources, against which the
corrections' own recall is measured first. Scored that way, it would
answer part of [QUESTION-108](../questions.d/QUESTION-108.md): whether the structured record makes the
operation of finding what is already held cheaper or more reliable than
search over the same text.

## Note of 2026-11-22: a pilot of this design

[CASE-tmpssuha](CASE-tmpssuha.md) ran a four-filing pilot for [LEAD-014](../leads.d/LEAD-014.md), on single arXiv
readings, because no exchange text is held in the repository. Replays
from the source and the record at the parent commit recovered 95 of 138
items the filings held and none of the 6 items their corrections added;
five of those needed works other than the source. The pilot bears on this
design in two ways. The ground truth is a lower bound, as said above: the
replays found items in neither, including an error [NOTE-645](../notes.d/NOTE-645.md) still repeats.
And the corrections of single-work readings are of accuracy, not omission
([CLAIM-tmpj6pb6](../claims.d/CLAIM-tmpj6pb6.md)), so the omission measure should be run on the exchange
episodes listed above, whose sources would have to be saved first. The
pilot's replays and scoring were by one assistant instance of the same
model family as the filers. The case is otherwise unchanged.
