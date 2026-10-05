---
number: 146
status: Proposed
formerly:
- THEORY-tmpm45lu
promote_when: >-
  Evidence from real research fields rather than models. Studies that
  trace methods through funding and training lineages, showing that
  researchers' methods were the same before and after industry funding,
  that funded researchers trained more of the next generation, and that a
  field's share of industry-favourable methods grew by that route. Also
  comparisons of funders whose merit assessments do or do not count
  industry-funded work. The account is in trouble if industry-favourable
  consensus in such fields arises mainly through funded individuals
  changing their methods or results. More simulations of the same model
  family, and further case histories read through the model, cannot
  settle it.
title: 'Industry can bias a scientific community toward a worse treatment without corrupting any individual, by selectively funding researchers whose methods already favour its product, provided researchers differ in method and both influence and the training of newcomers follow productivity; an independent funder counteracts this only if it discounts industry-funded work, and one that funds on productivity alone makes it worse'
version: 1
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
  ignoring industry-funded trials counters it. Proposed: one case and a
  small simulation.
---
<!-- inactive-ok-file: LIT-751 — Deferred; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-143 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-148 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->
<!-- inactive-ok-file: THEORY-151 — Proposed; cited for context or as the source of this reading, nothing here rests on its being settled -->

# THEORY-146: Industry can bias a scientific community toward a worse treatment without corrupting any individual, by selectively funding researchers whose methods already favour its product, provided researchers differ in method and both influence and the training of newcomers follow productivity; an independent funder counteracts this only if it discounts industry-funded work, and one that funds on productivity alone makes it worse

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
