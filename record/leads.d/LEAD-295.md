---
number: 295
status: Open
formerly:
- LEAD-tmpeqy94
title: 'Compare retention policies on a frozen snapshot of the record: complete corpus, standing-filtered retrieval, availability tiers, tiers with condensation and aggressive removal, on tasks drawn from the record''s own work, with a historical replay'
version: 1
stage: idea
priority: high
method:
- empirical
- historical
tags:
- information-retrieval
- databases
- design-rationale
date: '2026-11-26'
line:
- records-of-inquiry
- record-as-apparatus
advances:
- QUESTION-552
- CLAIM-1440
- CLAIM-1365
- CLAIM-1403
- CLAIM-1380
- CLAIM-184
summary: >-
  A27 §14 and A29 §VII of the exchange "Alignment consequences brainstorm"
  (ChatGPT, 2026-11-26): "Nucleation as a controlled experiment in
  forgetting". Five organizations of one frozen snapshot, scored on tasks
  from the record's own work for precision, recall, cost, repeated
  derivations, correction completeness, success on unfamiliar directions,
  reactivation cost and the apparatus's own upkeep; then a replay from an
  earlier date of what a candidate policy would have cooled. A says the
  replay scores only the trajectory the inquiry took, so "A prospective
  experiment would still be needed." The wording is A's (ChatGPT, in the
  exchange of 2026-11-26); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1440 CLAIM-1365 CLAIM-1403 CLAIM-1380 CLAIM-184 TERM-186 — Proposed; the claims this would test, filed from the same exchange on 2026-11-26, and a held claim -->

# LEAD-295: Compare retention policies on a frozen snapshot of the record: complete corpus, standing-filtered retrieval, availability tiers, tiers with condensation and aggressive removal, on tasks drawn from the record's own work, with a historical replay

## What to do

1. **Freeze** the tree at one commit.
2. **Build five organizations** (A27 §14):

   | Condition | Record organization |
   |---|---|
   | A | Existing complete corpus |
   | B | Standing-filtered retrieval |
   | C | Independent hot/warm/cold tiers |
   | D | Tiering plus governed condensation |
   | E | More aggressive relevance-based removal |

   C needs a tier assignment ([TERM-186](../terms.d/TERM-186.md)), set by a rule fixed in
   advance; D needs condensed representations of some lines.
3. **Draw tasks from the record's own work**: "ordinary questions, finding
   relevant previous results, detecting repeated arguments, reconstructing
   justification, propagating corrections and developing unfamiliar
   research directions". The filings in the curation log, replayed from
   the state before each, are a supply of tasks with known answers.
4. **Measure** (A27 §14): relevant retrieval precision and recall; time and
   tokens to resolution; repeated derivations; correction completeness;
   novel inquiry success; reactivation cost; maintenance burden.
   A29 VII adds counterparts of a collector's measures: throughput (useful
   work per resource unit), pause time (interruption by maintenance
   reviews), memory overhead (size and upkeep of the working corpus),
   promotion rate (formation of durable reusable structures), cache miss
   (recovery from outside the working set) and premature collection
   (costly re-derivation or a lost distinction).
5. **Replay.** "At an earlier date, identify entries that a candidate
   retention policy would have cooled. Then inspect their actual
   subsequent role in the inquiry." [LEAD-294](LEAD-294.md), filed from U17 to U19
   of the same exchange, is this step worked out on A34's terms, with
   policies simulated at past dates from what was known then. [CLAIM-184](../claims.d/CLAIM-184.md)'s
   own check (citations of each Superseded entry after its retirement, as
   history or not) is one arm of it.

## Its pilots

Three leads filed from U17 to U19 of the same exchange run single
conditions of this design: [LEAD-307](LEAD-307.md) is C against A on one line,
working views standing in for tiers; [LEAD-293](LEAD-293.md) is D on one argument
cluster; [LEAD-294](LEAD-294.md) is step 5. This lead is the full comparison they
would feed, and the place where E, removal, is tested against the rest.

## What it would move

- [CLAIM-1440](../claims.d/CLAIM-1440.md): B and C against A test the owner's claim that keeping
  costs retrieval.
- [CLAIM-1365](../claims.d/CLAIM-1365.md): whether C, which sets availability apart from standing,
  beats B, which uses standing alone.
- [CLAIM-1403](../claims.d/CLAIM-1403.md): whether a cost-chosen tiering beats one chosen by use.
- [CLAIM-1380](../claims.d/CLAIM-1380.md): D against C on novel inquiry success separates the
  abstraction hypothesis from the retrieval hypothesis.

## Cautions

A27: replay "evaluates retrieval against the inquiry's realized trajectory,
not every trajectory that could have developed under an alternative memory
arrangement." And the agent doing the tasks must use the retrieval surface
under test; one that greps the tree undoes the condition.
