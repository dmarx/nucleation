---
number: 155
status: Active
formerly:
- THEORY-tmp0w0cu
title: 'Iterated learning by Bayesian agents who sample from the posterior converges, in an ergodic chain, to the shared prior'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, from the
    owner's promotion audit of 2026-10-19. The promote_when asked for a
    human transmission-chain experiment with an independently measured
    prior, which tests the theorem's application to people, not the
    theorem; the body already said the THEORY does not claim that
    application. The condition moves, unchanged, to QUESTION-tmpxheie, and
    the THEORY keeps the theorem. Checked again for this promotion: with
    Q(h′|h) = Σ_d P(h′|d)P(d|h), Σ_h Q(h′|h)P(h) = Σ_d P(h′|d)P(d) = P(h′), so
    the prior is stationary whatever the data space, as NOTE-599
    reads Eqs. 25–36. Convergence to it needs the chain to be ergodic,
    which the body stated and the title now does. The claim is otherwise
    unchanged.
tags:
- linguistics
- probabilistic-modeling
- cognition
date: '2026-10-09'
source:
- LIT-769
- LIT-771
summary: >-
  Griffiths & Kalish (2007), [LIT-769](../literature.d/LIT-769.md), read in [NOTE-599](../notes.d/NOTE-599.md): a chain
  of learners who share a prior and each sample a hypothesis from their
  posterior is a Gibbs sampler, so the probability a learner holds a
  hypothesis converges to its prior probability, whatever the amount of
  data passed on; with MAP learners the outcome centres on the prior's
  mode but depends on data amount and noise, and can amplify weak biases.
  It is a theorem about an idealized chain. It does not say human chains
  reach the prior, and Kirby, Cornish & Smith's laboratory chains,
  [LIT-771](../literature.d/LIT-771.md), are consistent with it without testing it. Whether human
  chains do is [QUESTION-tmpxheie](../questions.d/QUESTION-tmpxheie.md).
supports:
- CLAIM-066
- CLAIM-090
- CLAIM-234
- CLAIM-191
---

<!-- inactive-ok-file: NOTE-596 — Skimmed; cited for what Kirby, Cornish & Smith's chains do and do not test, not leaned on -->
<!-- inactive-ok-file: LIT-768 — Unavailable, no lawful full text; named as the classical case the claim would have to meet, not leaned on -->

# THEORY-155: Iterated learning by Bayesian agents who sample from the posterior converges, in an ergodic chain, to the shared prior

## Source

- Griffiths & Kalish (2007), [LIT-769](../literature.d/LIT-769.md), read in [NOTE-599](../notes.d/NOTE-599.md): Eqs.
  25–36 (the prior and the prior predictive are stationary), §4.2 (the
  Gibbs-sampler identification), §5.1 and Table 1 (the MAP case), §7
  (populations).
- Kirby, Cornish & Smith (2008), [LIT-771](../literature.d/LIT-771.md), skimmed in [NOTE-596](../notes.d/NOTE-596.md):
  human diffusion chains, cited for what they do and do not test.

## The claim

Let every learner in a chain share a hypothesis space H, a prior P(h) and
a likelihood equal to the production distribution P(d|h). Let each learner
see data from the previous learner, sample a hypothesis h from P(h|d), and
produce data from P(d|h). Then the sequence of (h, d) pairs is a Gibbs
sampler for P(d|h)P(h). If the chain is ergodic, the probability that the
n-th learner holds hypothesis h converges to P(h), and the distribution of
the data it produces converges to the prior predictive Σ_h P(d|h)P(h).
The amount of data passed between learners affects only the speed of
convergence, not where it ends.

When learners instead take the maximum a posteriori hypothesis, the chain
is stochastic EM with the transmitted data as the latent variable and no
observations. Its stationary distribution concentrates near the prior's
mode, and, unlike the sampling case, depends on how much data is passed
and how noisy it is. In the two-language case it is identical for every
prior strength α between 0.5 and 1 − ε, so a weak bias can give the same
outcome as a strong one.

## What was actually shown

For sampling, a proof by substitution: the prior satisfies θ = Qθ for the
transition matrix on hypotheses, and the prior predictive satisfies ρ = Rρ
on data, for any production algorithm. It could have failed: a learning
rule other than posterior sampling (MAP, or a likelihood that does not
match production) does not, in general, leave the prior stationary, and
the paper's MAP results show such a departure in closed form. In the
260-hypothesis compositionality simulation, long-run frequencies under
sampling matched the prior at every data size m from 1 to 10, while MAP
chains departed from it (no compositional languages at all with α = 0.01;
only compositional ones at α = 0.5 with m ≤ 2). Under equal fitness, the
same distribution is the stable equilibrium of an unbounded population.

## What this does not say

- **It does not say human languages, or human transmission chains,
  converge to human priors.** That is [QUESTION-tmpxheie](../questions.d/QUESTION-tmpxheie.md). That depends on whether people learn by
  something like posterior sampling, which the source calls unexplored for
  language, and on all learners sharing one prior and one likelihood
  matched to production.
- **It does not say the bottleneck is irrelevant to the emergence of
  structure.** Under sampling it is irrelevant to the endpoint. Under MAP,
  which covers the minimum-description-length learners of earlier iterated
  learning simulations, the amount of data passed on changes the outcome.
- **It does not say structure is innate.** The prior is whatever makes a
  hypothesis easier to adopt, from any source; the source declines the
  innate reading.
- **It does not cover selection.** With unequal fitness, or a filter on
  what is transmitted, the prior need not be stationary. Kirby, Cornish &
  Smith's Experiment 2, [LIT-771](../literature.d/LIT-771.md), applies exactly such a filter
  (homonyms removed from training), so its compositional outcome is
  neither a confirmation nor a refutation of this claim.
- **Kirby, Cornish & Smith do not test it.** Their unfiltered chains lose
  colour distinctions in every chain, an outcome shaped by learner bias as
  the claim would lead one to expect, but no participant's prior was
  measured, and the paper does not use the Bayesian analysis.
- **It does not extend by itself to stories, norms or beliefs.** The
  source's closing extrapolation to "legends, religious concepts, and
  social norms" is not analysed there. Bartlett's serial reproduction of a
  folk tale ([LIT-768](../literature.d/LIT-768.md)) is the classical case it would have to meet,
  and the record has not read Bartlett.
