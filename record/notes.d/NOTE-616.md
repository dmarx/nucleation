---
number: 616
status: Read
formerly:
- NOTE-tmpb8ud3
paper: 'LIT-820'
title: 'Iterated learning (Kalish, Griffiths & Lewandowsky)'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the publisher's PDF of Psychonomic Bulletin &
    Review 14(2):288–294 (Springer, served without a login): the
    introduction and analysis, Method, Results, Discussion, author note,
    notes 1–2, the appendix on Bayesian linear regression and the
    reference list. The figures were read from their captions and the
    text; the plotted data were not re-measured. The companion analysis,
    Griffiths and Kalish (2007), was read for the record earlier
    (NOTE-599).
date: '2026-10-09'
summary: >-
  Puts Bayesian iterated learning to a laboratory test with a bias known
  beforehand: human function-learning chains converged on a positive
  linear function in 28 of 32 families, from positive linear, negative
  linear, U-shaped and random starting functions, as convergence to a
  prior favouring positive linear functions predicts. The prior was taken
  from earlier studies, three families settled on the negative linear
  function, and the authors do not claim the chains reached
  stationarity.
---

<!-- inactive-ok-file: THEORY-155 — Proposed; the account this reading bears on -->
<!-- inactive-ok-file: LIT-768 — Deferred; named as the classical case, not leaned on -->

# NOTE-616: Iterated learning (Kalish, Griffiths & Lewandowsky)

## Contribution

Before this paper, iterated learning was a body of simulations and one
analytical result (convergence to the prior for posterior-sampling
learners), and serial reproduction was Bartlett's uncontrolled stories and
pictures. This paper runs a transmission chain with human learners on a
task where the learners' bias had been characterised before the experiment
(function learning, where positive linear functions are favoured) and
shows that chains started from very different functions end, mostly, at
that favoured function. It also proposes iterated learning as a method for
revealing biases people cannot or will not report.

## Key insight

If what survives a chain of learners is what the learners were already
disposed to believe, then the endpoint of transmission is a portrait of
the transmitters, not of the source. Starting from a falling line, a
U-shape or noise, nine generations of learners drew a rising line.

## Assumptions

- **For the analysis:** all learners share one hypothesis space H, one
  prior p(h) and a likelihood p(d|h) equal to how data are produced; each
  samples h from p(h|d) (Eqs. 1–2); the Markov chain is ergodic
  ("fairly general conditions", citing Norris).
- **For the simulation (appendix):** hypotheses are lines y = β₁x + β₀ +
  ε with Gaussian noise σ_Y² = 0.0025, prior β ~ N((1, 0), 0.005 I),
  20 points per generation.
- **For the experiment:** the bias is "linear functions with a positive
  slope", from Brehmer (1971, 1974), Busemeyer et al. (1997) and Kalish,
  Lewandowsky and Kruschke (2004). Participants are not assumed, or shown,
  to be posterior samplers.

## Key results

- **Analysis.** p(h_n = i | h_{n−1} = j) = Σ_d p(h_n = i | d) p(d | h_{n−1}
  = j) defines a Markov chain whose stationary distribution is p(h); the
  data converge to the prior predictive p(d) = Σ_h p(d|h) p(h).
- **Simulation (Fig. 2).** Starting from 20 points on y = 1 − x, Bayesian
  learners with the stated prior produce a positive linear function within
  a few generations; the median correlation with y = x over 1,000 chains
  rises quickly.
- **Experiment (Figs. 3A–F).** Four conditions × 8 families × 9
  generations = 288 participants. 28 of 32 families converged to a
  positive linear function. 11 families produced a negative linear
  function at least once (all 8 negative-linear families, 2 random, 1
  nonlinear); 3 converged to it (2 negative, 1 random); 1 had not
  converged after nine generations. Median correlation with y = x rose
  across generations in the three non-ceiling conditions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Posterior-sampling Bayesian learners in a chain converge to their shared prior, and their data to the prior predictive | strong (proof, cited) | analysis section, citing Griffiths and Kalish |
| C2 | Human function-learning chains converge to a positive linear function regardless of the first learner's training function | moderate | 28 of 32 families; Fig. 3F medians |
| C3 | The human chains converge to the learners' prior | weak | the prior is inferred from earlier studies, not measured here; stationarity not established, by the authors' own statement |
| C4 | The stationary distribution includes the negative linear function with some weight | weak | 3 families ending there; interpretation only |
| C5 | Serial-reproduction results such as Bartlett's reveal people's biases; cultural forms are tailored to biases | not supported here | discussion; no stories or norms were transmitted |

## Concepts

- **iterated learning**: each learner learns from data produced by the
  previous learner and produces the data for the next.
- **family**: one chain of nine learners sharing a starting function.
- **inductive bias**: here, the prior p(h); the paper treats a prior as
  any source of preference, and note 1 declines to read it as innate or
  language-specific.

## Connections

The analysis is Griffiths and Kalish's ([LIT-769](../literature.d/LIT-769.md), read in [NOTE-599](NOTE-599.md)), whose
proof this paper summarises without new theory. The experimental lineage
is Bartlett's serial reproduction ([LIT-768](../literature.d/LIT-768.md), Deferred), with Bangerter
(2000) and Barrett and Nyhof (2001); the simulation lineage is Kirby,
Brighton and Smith. Kirby, Cornish and Smith's laboratory chains ([LIT-771](../literature.d/LIT-771.md))
came a year later and use no Bayesian analysis.

## Bearing on the record

- **[THEORY-155](../theory.d/THEORY-155.md)** (posterior-sampling chains converge to the prior). This is
  the nearest test the record holds: a human chain run against a bias
  stated before the experiment, with the endpoint independent of the
  start, as the theory would lead one to expect. It does not meet
  [THEORY-155](../theory.d/THEORY-155.md)'s `promote_when`: the prior was neither measured on these
  learners nor set by manipulation, the long-run distribution was not
  compared with it, and the authors say stationarity is unconfirmed. Nor
  can it separate sampling from MAP learners: a strong positive-linear
  mode would be reached either way. It supports the weaker claim that
  human transmission chains forget their starting point and settle on
  what learners favour, in this task.
- **Against [LIT-771](../literature.d/LIT-771.md).** Kirby, Cornish and Smith measured no bias and used
  an experimenter's filter. This experiment has no filter and a bias known
  in advance; its weakness is the opposite one, a task (one-dimensional
  function learning) far from language.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- One task, with a one-dimensional input and output, and undergraduates
  from one university.
- The prior is a qualitative description ("favours positive linear"),
  not a distribution; so "converges to the prior" is tested only as
  "converges to the prior's mode".
- Nine generations; three families ended on the negative function and one
  did not converge. The paper reports medians and representative chains,
  with no test statistics.
- Responses were produced by adjusting a slider within 5 units of the
  target counting as correct in training; motor and response noise is
  part of what is transmitted, and is not modelled.

## Open questions

- Would measuring each participant's prior first (for example by their
  first-generation responses to uninformative data) let the chains'
  long-run distribution be compared quantitatively with it, as
  [THEORY-155](../theory.d/THEORY-155.md)'s `promote_when` asks?
- Does the outcome depend on how much data passes between generations,
  as the MAP analysis predicts and the sampling analysis denies? The
  paper fixes it at 50 points.
