---
status: Proposed
title: 'Performative stability is the Campbell effect with the Goodhart effect retrained away'
statement: >-
  A ranking retrained on the web its last version induced removes, at a
  performatively stable point, its Goodhart effect, since a stable ranking is
  optimal for the web it faces, while it keeps the Campbell effect, since the
  web it faces is the one it induced; so convergence of the arms race is no
  evidence that the web is good, only that the ranking ranks accurately the
  web written for it, and the gap between that stable point and the ranking
  that would do best given publishers' response grows with how strongly they
  respond
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A performatively stable ranking that is not accurate on the distribution
  it induces, so that retraining does not remove the Goodhart effect; or one
  whose induced web is no different from the web the ranking found, so that
  no Campbell effect remains at stability.
tags:
- search-and-ranking
- learning-theory
- society-and-governance
date: '2026-11-27'
line:
- learned-structure
- organizational-normativity
answers:
- QUESTION-tmpqba7g
rests_on:
- CLAIM-tmp8hi2v
uses:
- TERM-tmp56tms
- TERM-tmpn32ez
grounds:
- THEORY-839
- THEORY-861
summary: >-
  The owner, 2026-11-27: "relate SEO to performative prediction". It reads
  [DISTINCTION-tmpnbw70](../distinctions.d/DISTINCTION-tmpnbw70.md)'s two effects in the terms of Perdomo and colleagues'
  framework ([LIT-1336](../literature.d/LIT-1336.md)), as the record holds it in [THEORY-839](../theory.d/THEORY-839.md) and [THEORY-861](../theory.d/THEORY-861.md).
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp8hi2v TERM-tmp56tms TERM-tmpn32ez DISTINCTION-tmpnbw70 CLAIM-tmpe27ub — Proposed, Open or new; the claim it rests on, the terms and distinction it uses, and the question -->

# CLAIM-tmph131t: Performative stability is the Campbell effect with the Goodhart effect retrained away

## The claim

In performative prediction a deployed model θ changes the distribution D(θ)
it is scored on. Read search that way:

- **The Goodhart effect** ([TERM-tmp56tms](../terms.d/TERM-tmp56tms.md)) is the ranking's accuracy decaying
  under its own deployment. A ranking fitted to yesterday's web is scored on
  the web its deployment produced, and there its signals mean less.
- **The Campbell effect** ([TERM-tmpn32ez](../terms.d/TERM-tmpn32ez.md)) is D(θ) differing from the web
  nobody optimized: the web written for the ranker.

Repeated retraining fits each new ranking to the web the last one induced.
At a performatively stable point, which [THEORY-861](../theory.d/THEORY-861.md) says retraining reaches
when publishers' response is weak enough, the ranking is optimal for the web
it faces. Its Goodhart effect is retrained away. But that web is the one it
induced, so its Campbell effect is built in. Stability means the ranking
ranks accurately a web written for it.

## Why stability is not success

[THEORY-839](../theory.d/THEORY-839.md) says a stable point need not minimize the risk the model actually
incurs. It lies within 2L_zε/γ of the performative optimum, the model that
would do best given how the population responds. In the biased-coin example
the record holds, the stable point is µ/(1 − ε) and the optimum µ/(1 − 2ε).
They are equal only when the prediction has no effect. Both gaps grow with ε,
publishers' responsiveness. So the arms race has two outcomes, and neither
is good:
- **No convergence**, where ε is large ([CLAIM-tmp8hi2v](CLAIM-tmp8hi2v.md)).
- **Convergence on a web written for the ranker**, an accurate ranking of
  degraded content.

## What it does not say

That every stable point is a degraded web. If the ranking reads effects of
quality that cost as much to forge as to earn ([CLAIM-tmpe27ub](CLAIM-tmpe27ub.md)), the web it
induces is a web of quality, and stability is success.
