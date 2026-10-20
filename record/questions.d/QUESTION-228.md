---
number: 228
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpbgam3

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Run on real systems, does Kenton et al.'s interventional procedure give the verdicts its definition of agency predicts, for a thermostat with and without its design process, an RL policy with and without its training loop, and a human, and does it separate an accidentally optimal input-output system from an agent where a compression test does not, under a principled choice of variables?"

version: 1
tags:
- agency
- causality
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'distributed-agency'
summary: >-
  The promotion condition formerly on [THEORY-527](../theory.d/THEORY-527.md). [THEORY-527](../theory.d/THEORY-527.md) was narrowed
  to Kenton et al.'s recovery theorem, stated on their definition of
  agents, and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2). Whether that definition
  picks out agency, and whether the procedure can be run on real systems,
  is open.


refines:
- QUESTION-032
answered_by:
- THEORY-tmpmmfpx
---

# QUESTION-228: Run on real systems, does Kenton et al.'s interventional procedure give the verdicts its definition of agency predicts, for a thermostat with and without its design process, an RL policy with and without its training loop, and a human, and does it separate an accidentally optimal input-output system from an agent where a compression test does not, under a principled choice of variables?

## Why it is a question

[THEORY-527](../theory.d/THEORY-527.md) holds that, if agents are the systems that would adapt their
policy were their actions to affect the world differently, then in
mechanised causal games meeting five assumptions the game graph is
recovered from interventions on mechanisms. The theorem is proved and was
re-derived on promotion. It cannot settle whether the definition is the
right one. Kenton et al. argue its verdicts in prose: a thermostat is not
an agent but is one together with its design process, an RL training
process is one but its learnt policy generally is not. Those verdicts are
relative to the variables chosen (their §5.1), and [THEORY-249](../theory.d/THEORY-249.md) presses that
frame dependence. Until 2026-10-20 this was [THEORY-527](../theory.d/THEORY-527.md)'s promote_when.

## What would answer it

- The procedure run, not described: mechanism interventions actually
  performed on a thermostat with and without its design process, an RL
  policy with and without its training loop, and a human, with the
  verdicts coming out as the definition says.
- The procedure separating an accidentally optimal input-output system
  from an agent where a compression test ([THEORY-624](../theory.d/THEORY-624.md)) does not.

Against it: natural choices of variables giving opposite verdicts on the
same system with no principled way to choose, or the five assumptions
failing for the systems that matter.

What would not answer it: the recovery theorem itself, which holds.
