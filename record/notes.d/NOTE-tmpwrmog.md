---
status: Read
paper: LIT-tmpagqou
title: 'Chen and colleagues — Skill-it! A Data-Driven Skills Framework for Understanding and Training Language Models'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full on 2026-11-19 from arXiv 2307.14430v1, with the NeurIPS
    2023 version compared for its changed tables. Read on 2026-11-19 by a
    delegated reader, with running notes on the branch claude/readers/data-
    scheduling; quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Skills defined by data and a prerequisite relation defined by a fixed-
  budget mixture test. At equal total steps, a mixture of a target skill's
  data with its prerequisites' reaches a loss threshold in 32 to 36 per
  cent fewer steps on synthetic tasks, and lowers loss by 4 to 11 per cent
  on Natural Instructions categories. No prerequisite is trained first; a
  sequential skill curriculum does no better than random, and gains on
  real corpora are small.
---
<!-- inactive-ok-file: CLAIM-756 — Proposed; the entry this reading bears on -->

# NOTE-tmpwrmog: Chen and colleagues — Skill-it! A Data-Driven Skills Framework for Understanding and Training Language Models

## Key results

1. **Skill and edge (Def. 2.1, 2.2).** An edge from s_i to s_j holds "if the amount of data needed to learn sj when uniformly sampling from Dsi ∪ Dsj is no more than the amount of data needed" "when sampling only from Dsj". The prerequisite is mixed in, not acquired first, and the total budget is fixed.
2. **The savings (§2.2, §4.2).** On LEGO, "in 35.9% fewer training steps, training on a balanced" mixture reached "the same validation loss of 0.01 as training solely on Xs3"; on addition, "in 32% fewer training steps". The online sampler reached the same loss "in 38.1% fewer steps" and "in 59% fewer steps"; on Natural Instructions it lowered "validation loss on Spanish question generation by 5.3% and Stance Detection by 13.6%".
3. **Edges are not the task's logic (App. D.1).** "the reasoning graph does not necessarily equal the skills graph".
4. **Many groupings give no order (§2.1).** Alpaca's types give "a nearly complete estimated skills graph (97.4% dense)", Pile of Law's sources one "3.9% dense".
5. **Sequential curricula do not help (App. D.3.1).** A skill curriculum trained groups in order "with mixing of previously seen groups to avoid forgetting"; without mixing, "resulted in forgetting". On LEGO it was no better than random, on addition far worse.
6. **Real corpora (Tables 7–9).** Small or mixed gains: on RedPajama with a 3B model, 64.2 against 64.4 average accuracy.
7. **The graph's own cost (proceedings, App. E.5.1).** Counted, it is recouped on LEGO: "the random baseline does not outperform" the sampler given the graph-learning steps.

## Bearing on the record

- **[CLAIM-756](../claims.d/CLAIM-756.md).** Evidence for its premise with the earlier acquisition's cost inside the comparison, at a fixed total budget: adding a prerequisite's data lowers the steps a target needs. Not the claim's sequence (acquire one, then the other), and no step with a negative return of its own. The sampler, which weights a skill by the losses of the skills it influences, is a working analogue of valuing an acquisition by its effect on others, but on present losses, not later costs.
- **[LEAD-tmp5lpoy](../leads.d/LEAD-tmp5lpoy.md)** described it as ordering data by prerequisites; it mixes and reweights, and its own sequential curriculum fails.
- **[QUESTION-039](../questions.d/QUESTION-039.md) and [QUESTION-217](../questions.d/QUESTION-217.md).** The order of benefit is set by the data and departs from the task's dependency order.

## Limitations

The existence results carry no stated variance; small models, all continual pretraining; small effects on real data.
