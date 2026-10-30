---
number: 146
status: Active
formerly:
- THEORY-tmpm45lu
title: 'In Holman and Bruner''s bandit model of honest Bayesian researchers whose beliefs funding cannot touch, who differ in method and whose influence and training of newcomers follow productivity, industry funding of those whose methods already favour its drug lowers, in the runs their figures report, the share of the community on the better treatment, and has no effect without methodological diversity; at the one setting reported, an independent funder that counts industry-funded trials toward its merit threshold lowers that share further, and one that excludes them raises it'
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Narrowed and promoted by the eleventh status review (ADR-057;
    ADR-047's ruling: one study read in full suffices for a title that
    claims no more than it showed). Read in full in NOTE-574. The title
    now says what the model and Figures 1–2 show. The old "only if" is
    dropped, since the paper compares two funder policies at one
    setting. The promote_when, evidence from real fields, asks for more
    than the title claims and moves to QUESTION-315. The old title: Industry can bias a scientific community toward a worse treatment without corrupting any individual, by selectively funding researchers whose methods already favour its product, provided researchers differ in method and both influence and the training of newcomers follow productivity; an independent funder counteracts this only if it discounts industry-funded work, and one that funds on productivity alone makes it worse. The old promote_when: Evidence from real research fields rather than models. Studies that trace methods through funding and training lineages, showing that researchers' methods were the same before and after industry funding, that funded researchers trained more of the next generation, and that a field's share of industry-favourable methods grew by that route. Also comparisons of funders whose merit assessments do or do not count industry-funded work. The account is in trouble if industry-favourable consensus in such fields arises mainly through funded individuals changing their methods or results. More simulations of the same model family, and further case histories read through the model, cannot settle it.
tags:
- philosophy-of-science
- epistemology
- network-science
date: '2026-10-05'
source:
- LIT-744
summary: >-
  Holman & Bruner (2017), [LIT-744](../literature.d/LIT-744.md). In a Zollman bandit model with
  methodological diversity, productivity-weighted influence and turnover,
  industry funding of agents whose methods favour the drug lowers the
  chance of converging on the better action, though no agent's beliefs
  respond to funding. A merit-based independent funder worsens it; one
  ignoring industry-funded trials counters it. Held as what the model
  shows; whether real fields work this way is QUESTION-315.
supports:
- CLAIM-276
- CLAIM-404
bears_on:
- QUESTION-047
- QUESTION-315
---
<!-- inactive-ok-file: LIT-751 — Unavailable; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: ADR-047 THEORY-1174 — ADR-047 Superseded by ADR-057, which keeps its evidence rulings; THEORY-1174 Proposed, the reading that keeps the old title without its "only if" -->
<!-- inactive-ok-file: THEORY-143 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-148 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-151 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->

# THEORY-146: In Holman and Bruner's bandit model of honest Bayesian researchers whose beliefs funding cannot touch, who differ in method and whose influence and training of newcomers follow productivity, industry funding of those whose methods already favour its drug lowers, in the runs their figures report, the share of the community on the better treatment, and has no effect without methodological diversity; at the one setting reported, an independent funder that counts industry-funded trials toward its merit threshold lowers that share further, and one that excludes them raises it

## Source

Holman & Bruner (2017), [LIT-744](../literature.d/LIT-744.md), read in [NOTE-574](../notes.d/NOTE-574.md). The authors'
2015 paper on intransigently biased agents, [LIT-751](../literature.d/LIT-751.md), is unread.

## What was actually shown

Holman and Bruner ([LIT-744](../literature.d/LIT-744.md)) give a historical case and a model.

- **The case.** In the antiarrhythmic drug disaster, industry funded
  researchers who already used a fast surrogate endpoint and stopped
  funding one who found deadly side effects. The funded researchers'
  views did not change; their productivity made them influential and
  their method the default.
- **The model.** Twenty agents in Zollman's bandit model, honest Bayesians
  whose beliefs are unaffected by funding. They differ in productivity
  (50–100 trials a round) and in methodological bias (measured success
  drawn around the true rate with variance σ²). Each round an agent leaves
  with probability 0.02, and the newcomer copies a method in proportion
  to its holder's productivity. The true rates are pA = .5 for no
  treatment and pB = .45 for the drug. Industry adds F trials a round to
  agents whose measured success for the drug exceeds .45 by more than T.
- **Results.** Methodological diversity alone lowers the share converging
  on the better action. Industry funding lowers it further, more as F
  grows. With no diversity, industry has no effect. An independent funder
  using a productivity threshold that counts industry-funded trials lowers
  reliability; one that excludes them raises it (read from the figures:
  about 56% with no independent funding, about 48–49% meritocratic, about
  77–81% selective).

## What this does not say

- **Not that conflicts of interest are harmless.** The authors set them
  aside "while not disregarding" them.
- **Not robust across parameters.** A few settings are reported, without
  run counts or the network used.
- **Not robust across networks, as shown.** That the qualitative results
  held on "both dense and sparse communication networks" rests on a single
  footnote, with no data.
- **Not that researchers never adapt.** In the model no agent changes its
  method, so the account says nothing about researchers who adjust to
  what funders reward.

## Connections

- **The Zollman effect ([THEORY-143](THEORY-143.md)).** If the footnote holds, the
  sparse communication that protects a community there does not protect it
  here, because industry acts on who is productive and who trains
  newcomers, not on who talks to whom.
- **Transient diversity ([THEORY-148](THEORY-148.md)).** Diversity of pursuit is what
  protects a learning group there; diversity of method is what a funder
  exploits here, and it lowers reliability even without one. The two
  accounts concern different diversities, which the record notes as a
  tension to keep in view rather than a contradiction.
- **Longino ([THEORY-151](THEORY-151.md)).** The case had venues for criticism and
  regulatory oversight and was steered anyway, through unequal influence
  gained from funding. That bears on her norm of tempered equality of
  intellectual authority. The reading is the record's.
- **The owner's essay.** §8.2's epistemic networks can be steered from
  outside without any member being captured; the remedy proposed is a
  community-level rule about how merit is counted.

## Note of 2026-10-30: the dropped clause

The old title said an independent funder counteracts industrial selection
"only if it discounts industry-funded work". That was imprecise. Holman and
Bruner compare two funder policies at one parameter setting (Figure 2) and
assert that a merit-based funder worsens the bias and one that discounts
industry-funded work counteracts it ([NOTE-574](../notes.d/NOTE-574.md), C4). They assert no
necessity, and no other policy is tested. The "only if" is not kept as a
proposal ([ADR-047](../decisions.d/ADR-047.md), kind 3). The rest of the old title, which the paper
asserts, is kept as the Proposed reading [THEORY-1174](THEORY-1174.md), with the funder
clause restated without the "only if".
