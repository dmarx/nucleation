---
number: 1246
status: Active
formerly:
- CLAIM-tmp8mpgs
title: 'Irreversibility gives waiting an option value'
statement: >-
  In a comparison of preserving an arrangement against transforming it,
  uncertainty about the alternative's costs together with an irreversible
  transition cost gives waiting to learn an option value, so transforming
  can beat preserving in expectation while waiting beats both; when the
  status quo irreversibly erodes the capacity to transform, the ranking can
  reverse, so symmetric scrutiny requires pricing irreversibility on both
  sides
version: 2
history:
- version: 2
  date: '2026-11-24'
  note: >-
    Active: an independent checker, who did not write it, reproduced every
    computation in it with its own code (2026-11-24). The owner left the
    promotion of verified entries to the assistant's discretion.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the worked comparison: that with the stated costs, transforming
  now does not beat preserving in expectation, or waiting a period to learn
  the alternative's cost does not beat transforming now, or, with the stated
  erosion, does not lose to it.
tags:
- society-and-governance
- operations-research
date: '2026-11-24'
line:
- readiness
- realizability
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A38 §3 of the exchange "Memes, Contracts, and
  Systemic Normativity" (2026-11-24), whose preservation-versus-transformation comparison "Excludes uncertainty" and concludes that "Our
  lifecycle cost model requires symmetrical scrutiny". A worked comparison,
  checked with python3 -I, after the real-options argument (Dixit and
  Pindyck). It is the formal side of the objection [CLAIM-1266](CLAIM-1266.md). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: CLAIM-1266 — Proposed, Deferred or Rejected; filed or cited in the filing of the exchange 'Memes, Contracts, and Systemic Normativity', whatever their standing -->

# CLAIM-1246: Irreversibility gives waiting an option value

## The gap

A38 §3 compares J_preserve = U + L + E with J_transform = R + U′ + L′ + E′,
and its widget compares (upkeep + losses) × horizon with transition cost +
alternative cost × horizon. Its caption: "Excludes uncertainty, discounting
and normative constraints." The conservative's reason for caution is
uncertainty about what a reform will do, with costs that cannot be undone.
A deterministic comparison cannot show whether that reason is any good.

## The comparison

Horizon T = 10 periods, no discounting. Preserving costs 15 a period: 150
in all. Transforming costs R = 40 once, sunk, and then c a period, where c
is 2 or 14 with equal probability (mean 8), learned after one period of
observation (a pilot, or watching another jurisdiction).

- **Preserve:** 150.
- **Transform now:** 40 + 10 × 8 = 120. Better than preserving.
- **Wait one period, then decide:** pay 15; if c = 2, transform (40 + 9 × 2
  = 58, total 73); if c = 14, keep the arrangement (9 × 15 = 135, total
  150). Expected 111.5. Better than transforming now.

Now let the status quo erode the capacity to transform: a period of waiting
raises R from 40 to 70 (expertise lost, dependants reorganized around the
arrangement). Waiting then gives c = 2: 15 + 70 + 18 = 103; c = 14: 150;
expected 126.5, worse than transforming now (120).

Checked with `python3 -I`, which reproduced 150, 120, 111.5 and 126.5.

## What it shows

- The conservative presumption, wait and learn before an irreversible
  change, can be the cost-minimizing policy even when the reform wins in
  expectation. It is not a conflation of persistence with value
  ([CLAIM-1266](CLAIM-1266.md)).
- Irreversibility cuts both ways. A40 §4.3 ("Inaction can be organizational
  transformation") is the other irreversibility: if the status quo erodes
  capacities, delay has its own sunk cost, and it can reverse the ranking.
- So A38's "symmetrical scrutiny" is right, and needs both
  irreversibilities priced: what the reform destroys that cannot be rebuilt,
  and what the delay destroys. The numbers are illustrative; the shapes are
  the textbook ones of real options under irreversibility.

## What it does not say

That either policy is right for any actual institution, or that every cost
in question can be put in one scalar; A38's own caption: "Moral rights and
standing cannot automatically be reduced to numerical costs." Nor does it
weigh whose losses the waiting costs are (A40 §4.4), which the totals here
ignore.
