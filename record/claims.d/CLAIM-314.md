---
number: 314
status: Proposed
formerly:
- CLAIM-tmpze74h
title: 'Reusing a filed argument has a recognition cost that a fixed per-use price leaves out: certifying that stored answers cover a new question is NP-complete even for conjunctive queries, grows with the number and size of the stored definitions rather than being a constant per item, and is undefined for an item filed without a statement of what it answers, so each filing raises the cost of later reuse and per-item break-even decisions are not independent'
version: 1
role: counter
warrant: interpretive
tags:
- design-rationale
- epistemology
- databases
date: '2026-10-15'
line: nucleating-argument
objects_to:
- CLAIM-308
grounds:
- THEORY-389
- THEORY-371
- THEORY-374
summary: >-
  Filed at the owner's request, from the readings on answering queries using
  views (Levy, Mendelzon, Sagiv and Srivastava 1995; Chandra and Merlin 1977;
  Halevy 2001). [CLAIM-308](CLAIM-308.md)'s guarantee needs a fixed, known per-use cost c_a;
  recognizing that a stored answer covers a new question is a search whose
  cost depends on everything stored, so filing one item changes the price of
  using the others. It undermines the premise [CLAIM-308](CLAIM-308.md) states, not its
  arithmetic. The hardness is worst case and over short definitions, partial
  reuse is cheap, and nothing here is measured on the record.
---
<!-- inactive-ok-file: CLAIM-303 CLAIM-308 — Proposed; the claim objected to, the claim it answers, and a survey's account cited as such -->

# CLAIM-314: Reusing a filed argument has a recognition cost that a fixed per-use price leaves out: certifying that stored answers cover a new question is NP-complete even for conjunctive queries, grows with the number and size of the stored definitions rather than being a constant per item, and is undefined for an item filed without a statement of what it answers, so each filing raises the cost of later reuse and per-item break-even decisions are not independent

## The claim

[CLAIM-308](CLAIM-308.md) applies the rent-or-buy rule to one filed argument at a time.
Its per-use cost once filed is c_a + u, access and verification plus
upkeep, fixed and known, and its guarantee of twice the hindsight
optimum needs exactly that. [CLAIM-308](CLAIM-308.md) already names the condition and
says reconstruction costs drift. This objection says one cost drifts in a
particular direction, and for a structural reason.

Using a filed answer for a new question first requires recognizing that
it answers the question. For the simplest formal case, conjunctive
queries with stored conjunctive definitions, that recognition is a
search: a stored view can serve a query exactly when its definition maps
homomorphically into the query's, and deciding whether the stored views
answer the query exactly is NP-complete in the size of the query and the
definitions ([THEORY-389](../theory.d/THEORY-389.md), from Levy, Mendelzon, Sagiv and Srivastava;
[THEORY-371](../theory.d/THEORY-371.md), from Chandra and Merlin). Two sources of difficulty are
independent: the number of ways each stored item could map into the
question, and which parts of the question the items jointly cover.

Three things follow for [CLAIM-308](CLAIM-308.md)'s accounting.

- **c_a is not a constant per item.** The search runs over every stored
  definition that might apply, so its cost grows with what has been filed,
  not with the item being used.
- **Filing has a cost that falls on other items.** Each new filing adds a
  candidate to every later recognition. That cost is paid at later uses of
  other arguments, so it appears in no single item's F, c_a or u, and a
  rule that decides item by item cannot see it. Per-item break-even
  decisions are therefore not independent. This is the same shape as
  upkeep that depends on what else is stored ([THEORY-350](../theory.d/THEORY-350.md)), where choosing
  one item at a time can go arbitrarily wrong.
- **Without a definition there is nothing to recognize.** Every result
  assumes each stored answer carries a statement of what it answers. For
  the record that is a claim's title or the question it answers. An item
  filed without one cannot be recognized at all, so writing that statement
  belongs inside F.

## What it does not say

- **That recognition is costly in practice.** The hardness is worst case,
  in the size of short definitions, and the stored data does not enter.
  The authors expect polynomial methods to cover many practical cases.
  Most of the record's reuse is a lookup by code, not a search for what
  covers a question.
- **That partial reuse is hard.** A maximally contained rewriting, using
  what the stored answers cover and redoing the rest, can be built in
  polynomial time ([THEORY-374](../theory.d/THEORY-374.md)). Only certifying exact coverage is
  hard. The cost then moves into reconstructing the remainder.
- **Anything about prose.** Conjunctive queries are a small positive
  language, which is why the problem is decidable at all. For arguments in
  prose, coverage is not shown to be decidable, let alone in NP. The
  formal case is a floor on the difficulty, not a model of it.
- **That [CLAIM-308](CLAIM-308.md)'s arithmetic is wrong.** Where recognition can be
  treated as fixed, for instance when an argument is reached by its code,
  the break-even rule and its guarantee stand.

## How [CLAIM-308](CLAIM-308.md) could answer

It could hold that the record's recognition is mostly lookup by code and
index, so c_a is close enough to fixed. Or it could fold the cost each
filing imposes on later recognition into u, as upkeep charged to the
store rather than the item, and ask whether a rent-or-buy rule over the
whole store keeps a bound. The readings give no such bound: the nearest,
[THEORY-350](../theory.d/THEORY-350.md), has guarantees only for restricted structures.

## Note of 2026-10-30: what holds it back

[CLAIM-308](CLAIM-308.md) concedes it at this review, and it keeps the status its
evidence gives it ([ADR-059](../decisions.d/ADR-059.md)). Its title says without condition that each
filing raises the cost of later reuse, while its body says most of the
record's reuse is lookup by code and that the conjunctive case does not
model prose. Nothing in the record measures the cost of recognizing what a
filed argument answers in the record's own reuse, or shows that coverage
for prose arguments is at least as hard as the conjunctive case.
