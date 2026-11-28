---
number: 1368
status: Proposed
formerly:
- CLAIM-tmp6tc1j
title: 'Retention by observed use confirms itself'
statement: >-
  In a record that its own readers search, how often an entry is retrieved
  is partly produced by how available the record makes it, so a retention
  policy that grants availability by observed use confirms its own earlier
  allocations of attention, and a record that forgets solely by its own
  usage can optimize away the material its later development would need;
  retrieval frequency is to be kept apart from substantive use and both
  from independent importance, with some retrieval reserved for dormant
  material
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A record whose retrieval counts, after an entry's availability is
  changed at random, do not move with the change, so that use is not
  produced by availability; or a usage-based policy that, over the
  record's history, cooled nothing that later work needed.
tags:
- information-retrieval
- design-rationale
- network-science
date: '2026-11-26'
line:
- records-of-inquiry
- record-as-apparatus
bears_on:
- QUESTION-552
summary: >-
  A29 §8 of the exchange "Alignment consequences brainstorm" (ChatGPT,
  2026-11-26): "an AI research agent's requests are partly determined by
  what the memory system makes visible", so "the original allocation of
  attention becomes self-confirming"; "A knowledge system that forgets
  solely according to its own observed usage risks optimizing away the
  conditions of its intellectual development." A's remedy is a small
  exploration budget for dormant material, alternative perspectives and
  underexplored questions. Ordinary caches take requests as given; this is
  where the cache analogy breaks. The wording is A's (ChatGPT, in the
  exchange of 2026-11-26); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1223 CLAIM-1148 LIT-3271 LIT-3310 CLAIM-1369 — Proposed or Deferred; held claims and a work cited -->

# CLAIM-1368: Retention by observed use confirms itself

## The claim

A29 §8: "If Luria makes a claim prominent, agents may retrieve and cite it
more often. If prominence is then justified by citation frequency, the
original allocation of attention becomes self-confirming." After a figure:
"This is the attention economy problem recreated inside the research apparatus." So
"Nucleation should therefore distinguish retrieval frequency from
substantive use, and both from independent importance."

The remedy: "some protected retrieval opportunities for dormant material,
alternative perspectives, and underexplored questions. A small exploration
budget could help detect relevance that the normal retrieval policy
systematically misses."

## Where it sits in the record

- It is why the cache literature's admission and eviction policies
  ([LIT-3271](../literature.d/LIT-3271.md), [LIT-3310](../literature.d/LIT-3310.md)) do not carry over unchanged: they treat
  the access stream as exogenous.
- [CLAIM-1223](CLAIM-1223.md) is the same loop with people in it: a count taken from the
  record, used as a score, is shaped by those it scores. Here the loop
  runs through the record's own retrieval, with no one gaming it.
- [CLAIM-266](CLAIM-266.md) (Active) is the general form: a family of probes that
  supplies the training signal cannot also certify what is preserved.
  Usage that sets availability is such a signal.
- [CLAIM-1369](CLAIM-1369.md), filed from U17 to U19 of the same exchange, is a
  second source of unearned prominence: an entry repeated across many
  generated pages is met many times by an unrestricted search.
- The exploration budget is a form of [CLAIM-1148](CLAIM-1148.md)'s maintained nuclei
  applied to attention.

## How it could be tested

Change some entries' availability at random and watch their retrieval: if
use follows availability, the loop is real (the `defeated_if`).
Survival curves from the record's history ([LEAD-294](../leads.d/LEAD-294.md)) cannot show it
alone, since they observe
use under one availability policy.
