---
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Is Bruno and Chaudhuri's single-index online tuner within some constant, such as 3 + 2f, of the offline optimum on every workload whose per-statement savings and losses are at most a fraction f of the build cost?"

version: 1
tags:
- databases
- operations-research
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'distributed-agency'

# refines: [QUESTION-000]   # the broader question this sharpens

refines:
- QUESTION-114
summary: >-
  The promotion condition formerly on [THEORY-332](../theory.d/THEORY-332.md). [THEORY-332](../theory.d/THEORY-332.md) was promoted
  on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) for the lower bound its construction proves: with
  every step at most fB, Online-SI can cost nearly 3 + 2f times the optimum,
  and one step above B makes the ratio unbounded. Whether any constant bounds
  it from above on such workloads is open.
---

<!-- unresolved-ok-file: QUESTION-000 — the placeholder a new document replaces -->

# QUESTION-tmp7o5ig: Is Bruno and Chaudhuri's single-index online tuner within some constant, such as 3 + 2f, of the offline optimum on every workload whose per-statement savings and losses are at most a fraction f of the build cost?

## Why it is a question

[THEORY-332](../theory.d/THEORY-332.md) holds the lower bound. Bruno and Chaudhuri's single-index rule
builds once the would-be savings have risen by the build cost B above their
last low, and drops once they have fallen by B below their last high. On a
repeated workload whose steps are at most fB, it pays (B + fB) + B + (B + fB)
per cycle against the optimum's B. The paper's Theorem 2 claims a factor of
3 but proves only the lower bound. Until 2026-10-20 an upper bound was
[THEORY-332](../theory.d/THEORY-332.md)'s promote_when.

An answer is a proof that Online-SI costs at most c(f) times the offline
optimum, plus perhaps an additive constant, on every workload with steps
bounded by fB, in the paper's model (one index, fixed build cost, free drops,
no space limit), together with the best such c(f). The construction shows
c(f) ≥ 3 + 2f. Hill-climbing at f = 0.05 to 0.5 found nothing above it. A
later rent-or-buy analysis of two-sided threshold rules would do. More
random-workload simulations cannot settle it.
