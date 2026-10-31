---
status: Active
status_note: >-
  read 2026-10-31, the derivation appendices skimmed (NOTE-tmp1z319); it
  does not argue that SGD and the posterior trace one journey: it states
  "no necessary relation" between their transitions, proposes only that
  training's transitions have Bayesian antecedents, and its main Bayesian
  transition, 5-gon to 6-gon, was not seen in training (THEORY-tmpzcsl4).
title: 'Dynamical versus Bayesian Phase Transitions in a Toy Model of Superposition'
version: 2
history:
- version: 1
  date: '2026-10-31'
  note: >-
    Filed, not read, from A3 and A14 of the exchange "Analyze
    nucleation concepts" (2026-10-30 to 31). Citation checked
    against arXiv (v1 2023-10-10). A3 gave the venue as ICLR 2024;
    the arXiv record carries no venue and it was not confirmed. The
    summary follows the abstract and the exchange's description; a
    reading should check it first.
- version: 2
  date: '2026-10-31'
  note: >-
    Read from the arXiv preprint 2310.06301v1, 66 pp., in NOTE-tmp1z319:
    the main text and Appendices A–F and K in full, the derivations in
    Appendices G–J skimmed; status Deferred → Active. The PDF carries no
    venue either. The summary is rewritten from the text. v1's summary
    and "Why this is here" read the abstract's "journey" as a conjecture
    that SGD and Bayesian learning follow one course, and called it the
    opposite of A3's separation. The paper's §5.1 states the separation
    itself; its conjecture, the Bayesian antecedent hypothesis, is
    one-directional. Both are corrected below.
tags:
- learning-theory
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-10-31'
published: '2023-10-10'
arxiv: '2310.06301'
first_author: 'Chen'
keywords:
- 'singular learning theory'
- 'phase transitions'
- 'toy model of superposition'
- 'local learning coefficient'
- 'Bayesian antecedent hypothesis'
implementations: []
summary: >-
  Chen, Lau, Mendel, Wei & Murfet (2023). In Elhage et al.'s toy model of
  superposition with two hidden dimensions, in the high-sparsity limit,
  the population loss has a closed form and regular k-gons are critical
  points with derived local learning coefficients. The free energy formula
  predicts a Bayesian phase transition from the 5-gon to the 6-gon near
  n = 600, which MCMC confirms. SGD trajectories plateau at the same
  critical points and move to lower loss and higher estimated complexity,
  but the 5 → 6 transition was not observed in training. The paper states
  that there is no necessary relation between the two kinds of transition,
  and conjectures only that training's transitions have Bayesian
  antecedents.
---
<!-- inactive-ok-file: QUESTION-tmpiir0l — Open; the question this bears on -->

# LIT-tmpogi33: Dynamical versus Bayesian Phase Transitions in a Toy Model of Superposition

Chen, Z., Lau, E., Mendel, J., Wei, S., & Murfet, D. (2023). Dynamical versus Bayesian phase transitions in a toy model of superposition. arXiv:2310.06301.

Read in NOTE-tmp1z319, with the derivation appendices skimmed.

## Why this is here

A3 cited it to separate Bayesian and dynamical transitions. The paper does state that separation: "There is no necessary relation between these two kinds of transitions" (§5.1), and its main Bayesian transition, 5-gon to 6-gon, was never seen in training. What A3 left out is the rest: the two processes share their landmarks, the critical points, and their direction, from high loss and low complexity to low loss and high complexity; and the paper conjectures that training's transitions have Bayesian antecedents. That conjecture runs one way and does not say the two orders coincide. From the paper's numbers, the antecedents of one observed chain do fall in training order, while SGD trained on 1000 samples ends where the posterior at 1000 does not (THEORY-tmpzcsl4). Read with LIT-323, the toy model it studies. It bears on QUESTION-tmpiir0l.
