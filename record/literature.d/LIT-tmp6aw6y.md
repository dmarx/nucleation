---
status: Active
status_note: >-
  read 2026-11-04 ([NOTE-tmpvyejl](../notes.d/NOTE-tmpvyejl.md)) from the publisher's Early View PDF
  posted on the first author's site; worth reading as a hierarchical
  Bayesian account of learning to learn in causal cognition, in which a
  causal schema, a partition of objects into categories with
  category-level causal powers, features and interactions, lets a new
  object's causal model be learned from one trial or from its features,
  with four adult experiments. Its comparison is qualitative and against
  two simple baselines, not rival causal-learning theories; one condition
  of Experiment 1 missed the predicted pattern and Experiment 4 shows the
  model overconfident; all the experiments use adults in one
  blocks-and-machine paradigm, the developmental claims resting on
  simulations.
title: 'Learning to Learn Causal Models'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 from the owner's pasted synthesis
    on hierarchical probabilistic models in cognitive science, written by
    another assistant (A), where it is item B of the cited works.
    Citation checked against Crossref: Charles Kemp, Noah D. Goodman and
    Joshua B. Tenenbaum, Cognitive Science 34(7), 1185–1243; PubMed
    21564248. Crossref gives online 23 August 2010, which is
    `published:`, and the issue September 2010; the paper prints received
    6 November 2008, revised 11 June 2010, accepted 14 June 2010. No
    correction needed. Read (NOTE-tmpvyejl) from the publisher-typeset
    Early View PDF, 59 pages paginated 1–59, posted on Charles Kemp's own
    site
    (https://www.charleskemp.com/papers/kempgt10_learningtolearncausalmodels.pdf)
    and linked from https://charleskemp.com/. Not read: the Appendix
    beyond the priors and the CRP, and the reference list.
tags:
- causality
- cognition
- probabilistic-modeling
date: '2026-11-04'
published: '2010-08-23'
doi: '10.1111/j.1551-6709.2010.01128.x'
first_author: 'Kemp'
keywords:
- 'learning to learn'
- 'causal learning'
- 'causal schema'
- 'hierarchical Bayesian models'
- 'categorization'
- 'one-shot learning'
- 'causal Bayes nets'
implementations: []
summary: >-
  Kemp, Goodman & Tenenbaum (2010). A three-level hierarchical Bayesian
  model of learning to learn causal models: a causal schema partitions
  objects into categories (a Chinese-restaurant prior) and gives each
  category a distribution over causal models (arrow, polarity, strength)
  and characteristic features, plus models for pairs of categories;
  below it sit object-level causal Bayes nets, and below those
  contingency and feature data. Four experiments on adults with blocks
  that activate a machine show one-shot learning shaped by the learned
  schema, overruling of it when a block is unlike the rest, zero-shot
  inference from features, and categories found from pairwise
  interactions alone. The model matches the curves qualitatively better
  than a bottom-up and an exemplar baseline, with two misfits; simulations
  extend it to children's perceptual-to-causal shift.
---
<!-- inactive-ok-file: THEORY-tmpablo5 CLAIM-543 — Proposed or new; cited from the reading of Kemp, Goodman and Tenenbaum (2010) as open -->

# LIT-tmp6aw6y: Learning to Learn Causal Models

Kemp, C., Goodman, N. D. & Tenenbaum, J. B. (2010). Learning to Learn Causal Models. *Cognitive Science* 34(7): 1185–1243. doi:10.1111/j.1551-6709.2010.01128.x.

## Key takeaways

*From the reading, [NOTE-tmpvyejl](../notes.d/NOTE-tmpvyejl.md). Page numbers are the Early View PDF's,
1–59; add 1184 for the issue's.*

- **The schema.** Members of a category are not given identical causal
  models; the authors "assume instead that members of the same category
  play similar causal roles" (p. 12).
- **The headline.** "Our results confirm that humans learn" rapidly about
  the causal powers of novel objects, and the framework accounts better
  "for our data than alternative models of causal learning" (p. 1).
- **What the alternatives were.** A bottom-up empirical-power model and an
  exemplar model; "Overall, neither baseline model can account for our
  results" (p. 24). No fit statistics; formal comparison for Experiments
  1–2 only.
- **Where it missed.** In one condition of Experiment 1 the human curve
  "does not match the bimodal curve predicted by the model" (p. 19); in
  Experiment 4 "the model is often extremely confident in cases where the
  mean human response appears to be a" U-shaped curve (pp. 37–38).
- **Given in advance.** Domains, events and "the existence of the
  hierarchy in Fig. 1A is known in advance" (p. 7); categories are a flat
  partition, and "Our model does not incorporate the notion of a causal
  hierarchy" (p. 49).

## Standing in the record

Registered from the owner's pasted synthesis of 2026-11-04, which cites it
for the claim that a hierarchical model accounted for adults' rapid causal
learning better than alternatives. The reading confirms the experiments
and narrows the comparison: two simple baselines, compared qualitatively.
It extends the overhypothesis programme of [LIT-tmplu70i](LIT-tmplu70i.md) from one or two
top-level parameters to a whole schema. Its Experiment 4 infers categories
from how objects interact, their number not fixed, which qualifies
[QUESTION-276](../questions.d/QUESTION-276.md) and [CLAIM-543](../claims.d/CLAIM-543.md); the categories still partition. Filed from it:
[THEORY-tmpablo5](../theory.d/THEORY-tmpablo5.md). No instruction for machine-learning practice; not an
anthology candidate, though it names transfer and multitask learning as
relatives.
