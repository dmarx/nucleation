---
number: 1365
status: Proposed
formerly:
- THEORY-tmpjlua4
promote_when: >-
  An independent re-derivation from the paper's generative model (a
  binary state with p(x1 = 1) = s(x2), x2 a Gaussian random walk with
  variance exp(κx3 + ω), x3 one with constant variance ϑ) and its two
  approximations (a mean-field factorization into Bernoulli and Gaussian
  marginals, and each variational energy expanded to second order at the
  previous posterior mean) reproduces the update equations (Eqs 21–34);
  confirms that each mean update has the form previous mean plus a
  learning rate times a prediction error; and confirms that, with κ, ω
  and ϑ fixed, the level-2 learning rate increases with the level-3
  volatility estimate. It is not met by simulations that look adaptive,
  by fits of the model to behaviour, or by evidence that the
  approximation is close to exact inversion, none of which the title
  asserts.
title: 'Mathys, Daunizeau, Friston and Stephan derive, by a mean-field variational approximation with each variational energy expanded to second order at the previous posterior mean, closed-form one-step updates for a hierarchy of Gaussian random walks whose step sizes are set by the level above; the updates take the Rescorla–Wagner form, their learning rate rises with the inferred volatility, and individual differences are carried by fixed coupling parameters'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Filed Proposed from NOTE-1552, the reading of LIT-2016,
    registered from the owner's pasted synthesis of 2026-11-04. The
    wording is the reader's; adopting it is the owner's call. Not
    re-derived for this filing.
tags:
- learning-and-conditioning
- probabilistic-modeling
date: '2026-11-04'
source:
- LIT-2016
summary: >-
  Mathys et al. (2011), [LIT-2016](../literature.d/LIT-2016.md), read in [NOTE-1552](../notes.d/NOTE-1552.md). A
  derivation with illustrative simulations: closed-form trial-by-trial
  updates for a three-level hierarchy of volatility, of Rescorla–Wagner
  form, with a learning rate that is the agent's posterior variance and
  grows with its volatility estimate, and with per-agent coupling
  parameters standing for individual differences. Proposed until the
  updates are re-derived. It says nothing about how close the
  approximation is to exact inversion, or about whether people learn this
  way. The wording is the reader's; adopting it is the owner's call.
---

# THEORY-1365: Mathys, Daunizeau, Friston and Stephan derive, by a mean-field variational approximation with each variational energy expanded to second order at the previous posterior mean, closed-form one-step updates for a hierarchy of Gaussian random walks whose step sizes are set by the level above; the updates take the Rescorla–Wagner form, their learning rate rises with the inferred volatility, and individual differences are carried by fixed coupling parameters

## Source

Mathys, Daunizeau, Friston and Stephan (2011), [LIT-2016](../literature.d/LIT-2016.md); read in
[NOTE-1552](../notes.d/NOTE-1552.md).

## What was actually shown

- **The model** (Abstract): "The model assumes Gaussian random walks of
  states at all but the first level, with the step size determined by the
  next highest level." x2's variance is exp(κx3 + ω); x3's is ϑ.
- **The derivation** (Results, Eqs 21–34): mean-field variational
  inversion, each variational energy expanded to second order at the
  previous posterior mean rather than at its mode, gives closed-form
  updates. Each mean update is the prediction plus a learning rate times a
  prediction error; at level 2 the learning rate is σ2, which depends on
  μ3: "the less confident the agent is about what it knows, the greater
  the influence of new information should be."
- **Individual differences**: "we model the individual variability
  between agents by putting delta-function priors on the parameters".
- **Illustration**: simulations of 320 binary trials under varied κ, ω
  and ϑ, perceptual uncertainty at the first level, and a currency series.
  "As expected, a more volatile environment leads to a higher learning
  rate." The simulations could have shown otherwise only as a check on
  the algebra, not on the world.

## What this does not say

- That the approximation is close to exact Bayesian inversion: it was not
  compared with exact inversion or sampling, and "it depends on the
  variational energies being approximately quadratic"; σ3 can go
  negative.
- That people learn this way: "this paper is of a purely theoretical
  nature", and fitting to data is left to later work.
- That the coupling parameters are identifiable from behaviour; the 2014
  paper, [LIT-2015](../literature.d/LIT-2015.md), finds κ confounded with the prior on
  x3.
- That the hierarchy is across participants. It is over states inside
  one agent; nothing is pooled across agents, unlike HDDM ([LIT-563](../literature.d/LIT-563.md)).
- Anything about anxiety or dopamine: those mappings are offered as
  anthropomorphic or hypothetical.
