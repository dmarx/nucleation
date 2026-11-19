---
status: Proposed
title: 'Smith, Friston and Whyte show, in a tutorial simulation of an explore–exploit task with a costly hint, that an active-inference agent learning which option is better takes the hint early and less often as its Dirichlet counts grow, takes it less the more precisely it prefers the larger win, and returns to it after unexpected losses'
version: 1
source:
- LIT-tmppd2x6
tags:
- neuroscience
- probabilistic-modeling
date: '2026-11-19'
promote_when: >-
  A rerun of the tutorial's explore–exploit simulation
  (Step_by_Step_AI_Guide.m, Sim = 2) reproducing Fig. 10's pattern: hint-
  taking that declines over 30 trials with RS = 3, a single hint with RS =
  4, and renewed hint-taking after unexpected losses.
summary: >-
  From the reading of LIT-tmppd2x6 in NOTE-tmpmq8mz. Smith, Friston and
  Whyte (2022), Journal of Mathematical Psychology 107, 102632, DOI
  10.1016/j.jmp.2021.102632 (open access; PMC8956124). A practical
  tutorial on discrete-state active inference: building POMDPs, simulating
  with SPM's routines, Dirichlet learning and its novelty term, the neural
  process theory, hierarchical models, and fitting models to choices with
  recoverability checks and Bayesian model comparison. Its running example
  is an explore–exploit task with a costly hint. There information-seeking
  fades as Dirichlet counts grow, falls as the preference for the larger
  win sharpens, and returns after surprises. Here because the exchange
  recommended it as the first reading for U31. It is a ready template for
  the Bayesian baseline and the fitting of CASE-153, though it has no
  second process with authority over action and no structure learning.
  Read in its NOTE (skimmed in part).
---

# THEORY-tmphnbs9: Smith, Friston and Whyte show, in a tutorial simulation of an explore–exploit task with a costly hint, that an active-inference agent learning which option is better takes the hint early and less often as its Dirichlet counts grow, takes it less the more precisely it prefers the larger win, and returns to it after unexpected losses

## The account

In the tutorial's POMDP, the context (left or right machine better) is hidden. The agent can take a hint, which reveals the context but halves the payout from $4 to $2, or choose a machine at once. Expected free energy combines the epistemic value of the hint with the preference for winning, and the novelty term shrinks as Dirichlet counts on the context prior accumulate. With a moderate preference (RS = 3) the agent takes the hint for several trials and then gradually stops. With a stronger one (RS = 4) it takes the hint once and commits. Unexpected losses send it back to the hint.

## What it does not show

- No empirical behaviour is fitted in the paper's examples, which use simulated participants. It is not evidence that people behave this way.
- Single-agent, single-process. No competing process can veto the information action, as CASE-153 needs.
- No structure learning: only parameters of a fixed model are learned.
