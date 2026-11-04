---
status: Proposed
promote_when: >-
  An independent study shows, in renewal or latent-inhibition data, that a
  latent-cause model with an unbounded number of causes predicts the
  context effects better than models without cause inference, and that a
  manipulation preventing the inference of new causes (a hippocampal
  lesion or immaturity) removes those effects as the model predicts.
title: 'Gershman, Blei and Niv propose that animals in conditioning experiments assign trials to latent causes under a prior admitting an unbounded number of causes, so that extinction is learned as a new cause rather than erasing the conditioned one, and that renewal and the context-dependence of latent inhibition follow from this inference while hippocampal lesions and immaturity abolish them by preventing new causes from being inferred'
version: 1
tags:
- learning-and-conditioning
- probabilistic-modeling
- neuroscience
date: '2026-11-04'
source:
- LIT-tmpdnjkj
summary: >-
  Gershman, Blei & Niv (2010), LIT-tmpdnjkj, read in NOTE-tmpn30ni. A
  Chinese restaurant process mixture over trials, inferred online by a
  particle filter, reproduces acquisition, extinction, ABA and ABC renewal
  and context-specific latent inhibition in simulation; with the
  concentration set to zero it reproduces the loss of context-dependence
  after hippocampal lesions and in young rats. Proposed: the support is
  qualitative simulation beside replotted data from other labs, with no
  fitted parameters and no quantitative comparison with rival models. The
  wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpdnjkj NOTE-tmpn30ni — new; the reading of Gershman, Blei & Niv (2010) this account is filed from -->

# THEORY-tmp1zlbc: Gershman, Blei and Niv propose that animals in conditioning experiments assign trials to latent causes under a prior admitting an unbounded number of causes, so that extinction is learned as a new cause rather than erasing the conditioned one, and that renewal and the context-dependence of latent inhibition follow from this inference while hippocampal lesions and immaturity abolish them by preventing new causes from being inferred

## Source

Gershman, Blei & Niv (2010), LIT-tmpdnjkj; read in NOTE-tmpn30ni.

## What was actually shown

- **The model** (pp. 198–200, Appendix): each trial a vector of discrete
  features (reinforcement, cue, context) from one latent cause; a CRP
  prior with α = .1; a uniform Dirichlet over each cause's feature
  probabilities; a particle filter with 3,000 particles; responding
  proportional to the predicted probability of reinforcement.
- **Renewal** (p. 201): "our model predicts ABA renewal as a consequence of
  the animal’s inference that different latent causes are active during
  conditioning and extinction." ABC renewal also appears; testing in the
  extinction context gives none.
- **Latent inhibition** (p. 202): pre-exposure in another context is
  segregated from conditioning, so latent inhibition is context-specific,
  which Redish et al.'s prediction-error-gated model mispredicts (p. 204).
- **Lesions and development** (pp. 202–203): setting α to zero at the time
  of the lesion, or for young animals, removes the context-dependence, as
  in the replotted data of Ji & Maren (2005), Honey & Good (1993) and Yap &
  Richardson (2005, 2007).
- What could have come out otherwise: the simulated curves could have
  failed to match the direction of the replotted effects. They were not
  fitted to them.

## What this does not say

- That the model fits the data quantitatively, or better than rival
  accounts: no parameters were fitted and no model comparison was run.
- That animals infer transitions between causes: the model is a static
  mixture with no temporal dynamics, and it cannot produce spontaneous
  recovery or the partial-reinforcement extinction effect.
- That context is itself inferred: context is observed; the cause is
  inferred.
- That the particle filter is how animals compute it (p. 206).
- That the hippocampus implements cause inference: it is a proposal, and
  the lesion and developmental results rest on the single manipulation
  α = 0 chosen to produce them.
