---
number: 1397
status: Proposed
formerly:
- CLAIM-tmpe27ub
title: 'SEO is adversarial and causal Goodhart, and a ranking escapes only by reading effects costly to forge'
statement: >-
  Of the variants into which Goodhart's law has been divided, search engine
  optimization is chiefly the adversarial and causal kinds: publishers
  optimize against the ranking, and they intervene directly on effects of
  quality, such as inbound links, cutting the causal path from quality to
  the signal; the regressional and extremal kinds follow without any gaming,
  since the top of a ranking by a noisy indicator over-represents pages whose
  indicator overstates them; so the escape CLAIM-1381 gives, reading
  effects of quality, holds only for effects whose forgery costs at least as
  much as the quality, since an effect of the truth, read, is reliable until
  it is forged
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A ranking signal that is an effect of quality, cheaper to forge than to
  earn, and that stays reliable under optimization pressure; or evidence that
  top-ranked pages are not over-represented among those whose signals
  overstate their quality when no one games the ranking.
tags:
- economics
- epistemology
date: '2026-11-27'
line:
- learned-structure
- organizational-normativity
answers:
- QUESTION-549
rests_on:
- CLAIM-1381
- CLAIM-1086
summary: >-
  Filed at the owner's request of 2026-11-27 to relate SEO to Goodhart's
  law. The division into regressional, extremal, causal and adversarial
  variants is Manheim and Garrabrant's (2018), from the assistant's memory
  and unregistered ([LEAD-311](../leads.d/LEAD-311.md)). It sharpens [CLAIM-1381](CLAIM-1381.md)'s ending
  condition using [CLAIM-1086](CLAIM-1086.md)'s point that forged smoke deceives anyone who
  knows fire by its smoke. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1381 CLAIM-1086 CLAIM-1420 — Proposed, Open or new; the claims it rests on, the question, and the lead -->

# CLAIM-1397: SEO is adversarial and causal Goodhart, and a ranking escapes only by reading effects costly to forge

## The claim

Manheim and Garrabrant, as the assistant recalls them, divide Goodhart's law
into four variants. SEO shows all four:

| Variant | The mechanism | In search |
|---|---|---|
| Regressional | selecting on a noisy indicator selects its noise too | the top results are over-represented by pages whose signals happen to overstate them, with no gaming at all |
| Extremal | the indicator–target relation that holds in the bulk fails in the tails | the relation between links and quality, fitted on ordinary pages, fails at the extremes rankings select from |
| Causal | intervening on a correlate does not move the target | buying links moves the signal without moving the quality that ordinarily causes links |
| Adversarial | agents optimize against the indicator | publishers, and link sellers serving them |

The causal variant is [CLAIM-1086](CLAIM-1086.md)'s distinction. A system that reads an effect
of the truth, as smoke is of fire, survives interventions on the truth, but
"forged smoke deceives anyone who knows fire by its smoke". Inbound links are
an effect of quality, and link-buying forges them.

## What it sharpens

[CLAIM-1381](CLAIM-1381.md) said the arms race ends where the ranking reads effects of
quality that cannot be manufactured more cheaply than the quality itself.
The variants say why both parts of that are needed:
- **An effect, not a correlate.** Otherwise the causal variant applies even
  without forgery.
- **Costly to forge.** Otherwise the adversarial variant forges the effect.

The regressional and extremal variants remain even then. They need no gaming,
so no ranking escapes them entirely. They are the cost of selecting by any
noisy indicator.

## What it does not say

That forgery cost can be made high everywhere. Where it cannot, the remaining
remedy is plurality of rankings ([CLAIM-1420](CLAIM-1420.md)), which raises the cost of
forging for all of them at once.
