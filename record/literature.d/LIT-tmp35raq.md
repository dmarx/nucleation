---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmpxqv1t](../notes.d/NOTE-tmpxqv1t.md)) from the CC BY version of
  record; worth reading as the active inference account in which a habit
  is one more policy, its transitions and prior probability learned by
  counting the agent's own behaviour, so that habits form from
  goal-directed choice and, once formed, survive devaluation. It gives the
  record a published analogue of a learned log prior beside a
  precision-weighted evaluation. Simulation of one T-maze task only; its
  learned prior grows by frequency, not by reward, its reaction times are
  simulation run times, and the authors concede that it makes probably no
  new behavioural predictions.
title: 'Active inference and learning'
version: 2
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-23/24, shared at
    https://chatgpt.com/share/6adc1ece-bb28-83e9-a8f6-cadf0f8b7113,
    where it is cited at turn U11. Citation checked against Crossref and
    PubMed (PMID 27375276) on 2026-10-24: Karl Friston, Thomas
    FitzGerald, Francesco Rigoli, Philipp Schwartenbeck, John O'Doherty
    and Giovanni Pezzulo, Neuroscience & Biobehavioral Reviews 68,
    862–879. Crossref gives only the issue month, September 2016; PubMed
    gives the online date, 29 June 2016, which is `published:`. The
    summary follows the abstract on PubMed.
- version: 2
  date: '2026-10-24'
  note: >-
    Read in full (NOTE-tmpxqv1t) from the version of record, Neuroscience
    and Biobehavioral Reviews 68 (2016) 862–879, the publisher's 21-page
    PDF with the notice "This is an open access article under the CC BY
    license", fetched from the University of East Anglia repository
    (ueaeprints.uea.ac.uk/id/eprint/61446/1/10_1016_j_neubiorev_2016_06_022.pdf),
    one of the open copies Unpaywall lists. Equations were read from
    rendered pages; Figures 3–7 from their captions. Status set to Active.
    The summary is accurate. "Why this is here" is corrected: the habit is
    a separate state-action policy whose transitions are learned, beside a
    prior over policies learned by counting, and neither is gated by
    reward.
tags:
- learning-and-conditioning
- neuroscience
- probabilistic-modeling
date: '2026-10-24'
published: '2016-06-29'
doi: '10.1016/j.neubiorev.2016.06.022'
first_author: 'Friston'
keywords:
- 'active inference'
- 'habit learning'
- 'goal-directed behaviour'
- 'Bayesian inference'
- 'epistemic value'
- 'dopamine'
- 'devaluation'
implementations: []
summary: >-
  Friston, FitzGerald, Rigoli, Schwartenbeck, O'Doherty & Pezzulo
  (2016). An active inference account of choice and learning, on how
  goal-directed and habitual behaviour contextualise each other. Habits
  emerge naturally from sequential policy optimisation in agents
  equipped with state-action policies, as learned prior beliefs over
  policies; epistemic, ambiguity-resolving behaviour enables pragmatic
  behaviour and then habit. The important distinction is between
  belief-free and belief-based schemes, not model-free and model-based;
  the scheme covers dopamine transfer, reversal learning, habit
  formation and devaluation, and reduces to a Bellman scheme without
  ambiguity.
supports:
- CLAIM-tmp0qupq
---
<!-- inactive-ok-file: CLAIM-tmp0qupq THEORY-tmpydeuq — Proposed; the claim that cites this and the account filed from the reading, named, nothing here rests on them -->

# LIT-tmp35raq: Active inference and learning

Friston, K., FitzGerald, T., Rigoli, F., Schwartenbeck, P., O'Doherty, J. & Pezzulo, G. (2016). Active inference and learning. *Neuroscience & Biobehavioral Reviews* 68: 862–879. doi:10.1016/j.neubiorev.2016.06.022.

## Key takeaways

*From the reading, [NOTE-tmpxqv1t](../notes.d/NOTE-tmpxqv1t.md). Page numbers are the journal's.*

- **A habit is one more policy.** It maps each state to the next whatever
  the time or context, and "Because habits are just another policy, the
  arbitration among habits and (sequential) policies rests on their
  posterior probability" (p. 869).
- **Learned by counting.** The habit's transitions and the prior over
  policies grow with how often they occur: "if a particular state or
  policy is encountered frequently, it will come to dominate posterior
  expectations" (p. 869).
- **Formed from goal-directed behaviour.** Habits "emerge naturally (and
  autodidactically)" from the agent observing itself (p. 862).
- **Insensitive to devaluation once formed.** "Despite this switch, the
  habit persists and, indeed, reinforces itself with repeated executions";
  devalued before the habit forms, the agent switches at once (p. 874).
- **Belief-based against belief-free.** The authors argue this, not
  model-based against model-free, is the distinction that matters, and
  that dynamic programming is the special case without ambiguity
  (pp. 870–871, 876).
- **Limits the authors state.** "At the level of behavioural predictions,
  the answer is probably no" (p. 876).

## Why this is here

The exchange cited it at turn U11 for active inference's treatment of habits as learned priors over policies: a repeated action becomes the expected one, and so the default. The abstract supports the habit claim; the phrase "prior over policies" is the paper's mechanism as standardly cited, not the abstract's wording.

**Corrected 2026-10-24, from the reading.** Right in substance, with one
correction. The paper has two learned things, not one: a habit, which is a
separate state-to-state policy whose transitions are learned, and a prior
over all policies, learned by counting which policies were pursued. Both
grow by frequency, not by reward. The habit competes with the sequential
policies by posterior probability on every trial, so it sits beside online
evaluation as [CLAIM-tmp0qupq](../claims.d/CLAIM-tmp0qupq.md) says; it shows persistence, not saved
computation. Filed from it: [THEORY-tmpydeuq](../theory.d/THEORY-tmpydeuq.md).
