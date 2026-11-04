---
status: Active
status_note: >-
  read 2026-11-04 (NOTE-tmpi89bb) from the publisher's typeset PDF posted
  on the first author's lab publications page; worth reading as the paper
  that carries Chinese-restaurant-process clustering from category
  learning into task-set learning, with a model, a corticostriatal network
  mapped onto it and a transfer paradigm that measures structure people
  build without being asked to. The model is an approximate learner, not
  Bayesian inference; positive transfer replicated in both experiments
  (N = 33 and N = 35) but is modest, negative transfer reached significance
  over the whole group only in Experiment 1, the model-fit differences are
  "small", and each subject's structure is read from a reaction-time
  switch-cost proxy.
title: 'Cognitive control over learning: Creating, clustering, and generalizing task-set structure'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    "Hierarchical probabilistic models in cognitive science", written by
    another assistant (A), which cites it by authors, year and title. The
    citation was checked against Crossref: Anne G. E. Collins and Michael
    J. Frank, Psychological Review 120(1), 190–229, doi 10.1037/a0030852
    (also printed on the article; supplement 10.1037/a0030852.supp), PMID
    23356780, PMCID PMC3974273. OpenAlex was not reached (429). Crossref
    gives the online and issue dates to the month only, 2013-01, so
    `published:` is 2013-01-01 under ADR-002's first-of-the-month rule;
    the Crossref record-creation date, 2013-01-28, is not a publication
    date. The article prints received 15 April 2012, accepted 12 October
    2012; there is no preprint. A's authors, year and title are right, but
    the sentence A puts in quotation marks as the paper's ("Behavioral
    experiments supported these predictions, and the model fit individual
    sequences of choices ...") is not in the paper: it is A's paraphrase.
    Read (NOTE-tmpi89bb) from the publisher's typeset PDF, 40 pages, posted
    on the publications page of the first author's lab
    (https://ccn.berkeley.edu/pdfs/papers/CollinsFrank2013PsychReview.pdf);
    the Europe PMC and PMC copies of the author manuscript met bot checks
    and were not retried. Not read: Appendices A–B, the online supplement
    and the references.
tags:
- cognition
- learning-and-conditioning
- probabilistic-modeling
date: '2026-11-04'
published: '2013-01-01'
doi: '10.1037/a0030852'
first_author: 'Collins'
keywords:
- 'task-set'
- 'cognitive control'
- 'reinforcement learning'
- 'nonparametric Bayesian'
- 'Chinese restaurant process'
- 'generalization'
- 'transfer'
- 'prefrontal cortex'
- 'basal ganglia'
implementations: []
summary: >-
  Collins & Frank (2013). People learning stimulus–action rules by
  reinforcement may also learn which abstract rule, or task-set, a context
  signals. The context–task-set (C-TS) model clusters contexts onto latent
  task-sets under a Chinese-restaurant-process prior, reusing a task-set in
  proportion to its popularity or creating a new one, but approximates
  rather than performs the inference, keeping one task-set assignment per
  trial. A two-loop corticostriatal network that learns by reinforcement
  alone behaves like it, and its parameters map onto the model's. In two
  experiments where flat learning is as good as structured during
  acquisition, a new context signalling an old task-set was learned faster
  (positive transfer), and a new context needing a partly overlapping rule
  drew errors correct under an old task-set (negative transfer),
  significant over the whole group in Experiment 1, a trend in Experiment
  2.
---
<!-- inactive-ok-file: THEORY-tmp34zny THEORY-484 — Proposed or new; cited from the reading of Collins and Frank (2013) as open -->

# LIT-tmpe9iv8: Cognitive control over learning: Creating, clustering, and generalizing task-set structure

Collins, A. G. E. & Frank, M. J. (2013). Cognitive control over learning: Creating, clustering, and generalizing task-set structure. *Psychological Review* 120(1): 190–229. doi:10.1037/a0030852.

## Key takeaways

*From the reading, NOTE-tmpi89bb. Page numbers are the journal's.*

- **Clustering contexts by what they predict.** The C-TS model is
  "inspired by nonparametric Bayesian methods" (p. 190): contexts are
  grouped onto latent task-sets by the stimulus–action–outcome
  contingencies they share, not by how they look, under a CRP prior.
- **Not optimal inference.** "We do not propose that humans solve the
  inference problem posed by such a generative model" (p. 194); the model
  keeps a single task-set assignment per trial and never revises it.
- **Two levels linked.** A nested corticostriatal gating network learns
  by reinforcement alone; fitting C-TS to its choices recovers its
  structure, and distinct network parameters move distinct model
  parameters (p. 206).
- **Structure that does not pay at first.** Structure building "does not
  seem optimal" for acquisition in this task (p. 215), yet people build
  it, and it shows later as positive and negative transfer.
- **Modest effects.** Positive transfer t = 2.37, p = .024 in Experiment
  1; in Experiment 2 "the interaction typical of negative transfer was not
  significant" (p. 214); the fit advantage of structure over flat models
  is "small" (p. 213).

## Standing in the record

Cited, by authors, year and title, in a pasted synthesis written by
another assistant, as the source of a model of inferring hidden task-sets
and reusing or creating them. That much is right. The synthesis's quoted
summary sentence is its own paraphrase, and the "related 2014 EEG study"
it adds, LIT-tmp199ym, re-analyses this paper's Experiment 2 participants
(N = 35), not a new sample. Filed from it: THEORY-tmp34zny. It bears on
QUESTION-276 as a worked case of inferring an unfixed number of latent
rules from behaviour, and on THEORY-484 by drawing a line between
state-space abstraction over task-sets and the options framework's
temporal abstraction; the double edge of reuse it shows has an analogue
in THEORY-688. No instruction for machine-learning practice.
