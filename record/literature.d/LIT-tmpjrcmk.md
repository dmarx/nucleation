---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmpm6c07](../notes.d/NOTE-tmpm6c07.md)) from the publisher's open-access
  PDF (CC BY 4.0); worth reading as a model of active learning to learn in
  causal induction: interventions chosen by a weighted sum of expected
  information gain about the functional form (an overhypothesis that
  transfers between tasks) and about the structure of the task at hand,
  tested in two preregistered blicket-detector experiments. Its main
  limits: averaged over participants, the ablation that does not transfer
  beat the full model, so transfer rests on a per-participant count of
  best models; the conjunctive transfer task of Experiment 1 showed no
  match effect, and several effects need an engagement filter; the
  information-gain decomposition is an acknowledged approximation, with
  normalized gains that make the weight scale-dependent; MTurk samples;
  the supplementary appendices were not read.
title: 'Actively Learning to Learn Causal Relationships'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science", written by
    another assistant (A), where it is cited in §2H. Citation checked
    against Crossref, OpenAlex and the arXiv API: Chentian Jiang and
    Christopher G. Lucas, Computational Brain & Behavior 7(1), 80–105
    (2024), doi:10.1007/s42113-023-00195-0, published online 5 January
    2024 (accepted 10 December 2023); A's attribution is correct.
    `published:` is the earliest exact date, the arXiv v1 of 20 June 2022
    (arXiv:2206.09777, same title and authors), not the journal's online
    date; the arXiv id is given as the preferred source and the DOI
    beside it. Read from the publisher's open-access PDF, 26 pages
    (https://link.springer.com/content/pdf/10.1007/s42113-023-00195-0.pdf);
    a PMC copy also exists (PMC13292816). Not read: the supplementary
    Appendices A and B.
tags:
- causality
- cognition
- probabilistic-modeling
date: '2026-11-04'
published: '2022-06-20'
arxiv: '2206.09777'
doi: '10.1007/s42113-023-00195-0'
first_author: 'Jiang'
keywords:
- 'Causal learning'
- 'Active learning'
- 'Transfer learning'
- 'Overhypotheses'
- 'Generalization'
implementations: []
summary: >-
  Jiang & Lucas (2024; arXiv 2022). A hierarchical Bayesian learner keeps
  a joint posterior over causal structures (which blocks are blickets) and
  functional forms (a grid of Lucas & Griffiths sigmoids), carries the
  marginal over forms into the next task, and chooses interventions by
  w·EIG(form) + (1−w)·EIG(structure). In two preregistered online
  experiments with 14 between-subjects conditions, training form changed
  the first transfer intervention (more blocks after conjunctive
  training), but match effects on accuracy were trends or nulls in the
  full data. Averaged over participants, the No-Transfer ablation
  predicted interventions best (.059 against .055 for the full model);
  per participant, the full model was best for the largest group, and
  among those participants 81.63% of fitted weights favoured form
  information. Fixed-form and
  structure-only learners barely beat random.
---
<!-- inactive-ok-file: THEORY-tmpbgkfv — Proposed and new; cited from the reading of Jiang & Lucas (2024) as open -->

# LIT-tmpjrcmk: Actively Learning to Learn Causal Relationships

Jiang, C. & Lucas, C. G. (2024). Actively learning to learn causal relationships. *Computational Brain & Behavior* 7(1): 80–105. doi:10.1007/s42113-023-00195-0. First posted as arXiv:2206.09777 (20 June 2022).

## Key takeaways

*From the reading, [NOTE-tmpm6c07](../notes.d/NOTE-tmpm6c07.md).*

- **Two levels of information.** Interventions are scored by a weighted
  sum of information gain about the functional form and about the
  structure; the weight w is fitted per participant.
- **Group level against the hypothesis of transfer.** "The No-Transfer
  ablation model had the highest mean predictive likelihood" (.059 ±
  .002, against .055 ± .003 for the full model).
- **Per participant, for it.** "our full model was the best predictor for
  the highest number of participants"; among those participants,
  "81.63% of fits have overhypothesis weight > 0.5", 45.41% at the
  boundary w = 1.
- **The strongest result.** Fixed-Form and Structure-Only-EIG both score
  .018, barely above random at .016: rich forms and seeking form
  information are needed, transfer less clearly.
- **Behaviour.** More blocks in the first transfer intervention after
  conjunctive than after disjunctive training; no significant match
  effect on the conjunctive transfer task.

## Standing in the record

Registered from A's synthesis, which characterizes it fairly but leaves
out the group-level result against transfer. It extends Lucas &
Griffiths (2010), [LIT-tmpzamp4](LIT-tmpzamp4.md), from passive to active learning. Its
intervention criterion is the expected information gain of Bayesian
experimental design ([LIT-1525](LIT-1525.md)). Filed from it: [THEORY-tmpbgkfv](../theory.d/THEORY-tmpbgkfv.md).
