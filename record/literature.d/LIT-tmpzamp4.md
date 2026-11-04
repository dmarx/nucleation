---
status: Active
status_note: >-
  read in full 2026-11-04 ([NOTE-tmp8uiyl](../notes.d/NOTE-tmp8uiyl.md)) from the publisher's typeset PDF
  posted on Thomas Griffiths's lab publications page; worth reading as the
  standard formal account of how people learn the functional form of
  causal relationships (whether causes combine disjunctively or
  conjunctively, and how noisily) as abstract theories in a hierarchical
  Bayesian model, and transfer it to new objects, with five blicket-meter
  experiments behind it. Its main limits: a narrow, monotone two-parameter
  sigmoid theory space; small samples of Berkeley undergraduates; fits to
  condition means with the two hyperparameters tuned on the same ratings;
  weak rivals (fixed-form models that cannot predict any condition
  effect); one predicted contrast reversed (Experiment 2) and one key
  effect marginal (Experiment 3).
title: 'Learning the Form of Causal Relationships Using Hierarchical Bayesian Models'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    on hierarchical probabilistic models in cognitive science, written by
    another assistant (A), where it is cited in §2B beside Kemp, Goodman
    & Tenenbaum (2010). Citation checked against Crossref and OpenAlex:
    Christopher G. Lucas and Thomas L. Griffiths, Cognitive Science
    34(1), 113–147, doi:10.1111/j.1551-6709.2009.01058.x, PMID 21564208.
    Crossref gives online 7 January 2010, which is `published:` (received
    20 January 2009, accepted 3 June 2009; Europe PMC's "first
    publication date" of 2009-07-28 matches no other source and was not
    used). No arXiv or preprint version was found. Correction: A cites
    the work as by "Lucas and colleagues"; it has two authors, Lucas and
    Griffiths. Read from the publisher's typeset PDF (35 pages) posted on
    the Griffiths lab publications page
    (https://cocosci.princeton.edu/tom/papers/funcform.pdf); the Wiley
    open-access address OpenAlex lists returned a Cloudflare challenge and
    was not retried.
tags:
- causality
- cognition
- probabilistic-modeling
date: '2026-11-04'
published: '2010-01-07'
doi: '10.1111/j.1551-6709.2009.01058.x'
first_author: 'Lucas'
keywords:
- 'Causal reasoning'
- 'Bayesian networks'
- 'Bayesian models'
- 'Hierarchical models'
- 'Rational inference'
- 'Structure learning'
- 'Human experimentation'
- 'Computer simulation'
implementations: []
summary: >-
  Lucas & Griffiths (2010). Knowledge of how causes combine, the
  functional form of a causal relationship, is learned as a theory at the
  upper level of a hierarchical Bayesian model: the posterior over
  theories from one data set is the prior for a second data set about
  different objects. A two-parameter sigmoid (bias and gain in the number
  of blickets present), with two hyperparameters fit across all
  experiments, predicts mean ratings in five blicket-meter experiments
  (r = 0.98–0.99): conjunctive, noisy-disjunctive or deterministic
  training changes judgments of new objects in an identical test block,
  noise cues matter, and transfer is larger within a domain than across
  domains. The rivals it beats are mostly fixed-form models that cannot
  vary between conditions.
---
<!-- inactive-ok-file: THEORY-tmp1n0rh — Proposed and new; cited from the reading of Lucas & Griffiths (2010) as open -->

# LIT-tmpzamp4: Learning the Form of Causal Relationships Using Hierarchical Bayesian Models

Lucas, C. G. & Griffiths, T. L. (2010). Learning the form of causal relationships using hierarchical Bayesian models. *Cognitive Science* 34(1): 113–147. doi:10.1111/j.1551-6709.2009.01058.x.

## Key takeaways

*From the reading, [NOTE-tmp8uiyl](../notes.d/NOTE-tmp8uiyl.md).*

- **Theory-level transfer.** Evidence about one set of objects changes
  causal judgments about a disjoint set, which only a hierarchical model
  predicts, "because the events in d (1) do not involve any of the
  prospective causes in d (2)" (§5).
- **Close fits to means, against weak rivals.** Experiment 1: model MSE
  0.38 and r = 0.99, against 5.83 and 0.82 for ΔP and causal power and
  3.97 and 0.83 for the best training-blind predictions (§6.2). In
  Experiment 2 the training-blind baseline comes close (MSE 0.63, r 0.97).
- **A disjunction-favouring prior is needed** (§11.1): the prior on the
  bias must have a low mean; the gain's matters little.
- **Domain-specific.** Transfer is larger when training and test share a
  domain (Experiment 5, §10.2).
- **Not general.** The authors say their sigmoid model is not "a general
  purpose model that could explain all instances of learning of
  functional form" (§5).

## Standing in the record

Registered from A's synthesis, which miscredits it to "Lucas and
colleagues". The record held no work on human causal induction before
it; Jiang & Lucas (2024), [LIT-tmpjrcmk](LIT-tmpjrcmk.md), builds its active-learning model
on this paper's sigmoid theory space. Filed from it: [THEORY-tmp1n0rh](../theory.d/THEORY-tmp1n0rh.md).
