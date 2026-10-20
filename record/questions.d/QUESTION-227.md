---
number: 227
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpgenqn

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Does the widen-on-push, narrow-on-fetch rule for a cached interval's width converge to within a stated factor of the best fixed width, and does it hold its cost against the best fixed width and an adaptive cache-or-not rule on data other than its authors' traces?"

version: 1
tags:
- databases
- operations-research
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'distributed-agency'

summary: >-
  The promotion condition formerly on [THEORY-377](../theory.d/THEORY-377.md). [THEORY-377](../theory.d/THEORY-377.md) was narrowed to
  Olston, Loo and Widom's simulations and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md)
  v3). Whether their width-setting rule converges, and whether it holds up
  on other data, is open.

refines:
- QUESTION-114
---

# QUESTION-227: Does the widen-on-push, narrow-on-fetch rule for a cached interval's width converge to within a stated factor of the best fixed width, and does it hold its cost against the best fixed width and an adaptive cache-or-not rule on data other than its authors' traces?

## Why it is a question

[THEORY-377](../theory.d/THEORY-377.md) holds what Olston, Loo and Widom (2001) simulated. Their rule
widens a cached interval on a value-initiated refresh and narrows it on a
query-initiated one, with probabilities set by ρ = 2C_vr/C_qr. It settled
within 1% of the best fixed width on one random walk and within 5% over
eight walk settings. On one 50-host trace it almost matched a tuned
adaptive exact-caching rule. The claim that it converges to the best width
is argued from the balance condition ρ·P_vr = P_qr ([THEORY-386](../theory.d/THEORY-386.md)), not
proved, and every result is the authors' own simulation. Until 2026-10-20
this was [THEORY-377](../theory.d/THEORY-377.md)'s promote_when.

## What would answer it

- A proof that, under stated processes for value changes and query
  precision demands, the width the rule sets converges, in distribution or
  in time-average cost, to within a stated factor of the best fixed width.
- A trace study on data other than the authors', measuring the rule's cost
  against the best fixed width and against an adaptive cache-or-not rule.

What would not answer it: more simulations on random walks, or further
results on the authors' own traces.
