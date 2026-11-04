---
status: Read
paper: 'LIT-tmpld7ct'
title: 'Mathys, Daunizeau, Friston & Stephan — A Bayesian foundation for individual learning under uncertainty'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the Europe PMC full-text XML of the
    open-access article,
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3096853/fullTextXML
    (the publisher's text in JATS), converted to text locally. Read: all
    prose sections (Introduction, Theory, Results on the variational
    energies, update equations, quadratic approximation, structural
    interpretation, simulations, perceptual uncertainty and continuous
    states, and the Discussion with its list of five properties),
    Equations 1–51 as linearized MathML, and the captions of Figures
    1–14. Not read: the figure images and the reference list. The
    Frontiers article page was fetched for metadata only. The reading was
    drafted by a delegated reader and its quotes rechecked against the
    text by the filer.
date: '2026-11-04'
summary: >-
  A generative model of one agent's learning under uncertainty: a binary
  state, a tendency whose logistic is its probability, and a
  log-volatility, each level above the first a Gaussian random walk whose
  step size is set by the level above. A mean-field variational
  approximation with a second-order expansion at the previous posterior
  mean gives closed-form one-step updates of Rescorla–Wagner form whose
  learning rate rises with inferred volatility. Individual differences are
  fixed coupling parameters (κ, ω, ϑ). Purely theoretical: simulations
  and a currency series, no human data and no fitting.
---
<!-- inactive-ok-file: THEORY-tmpjlua4 CLAIM-446 CASE-165 THEORY-882 THEORY-1182 THEORY-484 THEORY-070 — Proposed or new; cited from the reading of Mathys et al. (2011) as open -->

# NOTE-tmpwdo6q: Mathys, Daunizeau, Friston & Stephan — A Bayesian foundation for individual learning under uncertainty

## Contribution

A tractable, analytical, trial-by-trial approximation to Bayesian learning
in a hierarchy of volatility. Exact Bayesian learners need numerical
integration on every trial, and reinforcement-learning models assume
their learning rates. Here learning
rates and prediction errors fall out of the inversion, and the coupling
parameters are interpretable per agent. This is the model that
[LIT-tmpkft30](../literature.d/LIT-tmpkft30.md) later names the Hierarchical Gaussian Filter; this paper does
not use the name.

## Key insight

Put Gaussian random walks on every level but the first, let each level's
log-variance be linear in the level above, and approximate each level's
posterior by a Gaussian expanded around its previous mean: the result is
an update in which the weight given to a prediction error is the agent's
own uncertainty, and that uncertainty grows with its estimate of how
volatile the world is. In the authors' words, "the less confident the
agent is about what it knows, the greater the influence of new
information should be" (Structural interpretation). Individual differences
in learning are then differences in priors, not departures from Bayes.

## Assumptions

- **Generative model (Theory).** x1 binary, with p(x1 = 1) = s(x2), s the
  logistic; x2 a Gaussian random walk with variance exp(κx3 + ω); x3 a
  Gaussian random walk with constant variance ϑ.
- **Fixed parameters.** κ, ω and ϑ are fixed for each agent over an
  experiment: "we model the individual variability between agents by
  putting delta-function priors on the parameters" (Exact inversion).
  States change fast, parameters slowly or not at all.
- **Mean-field factorization** across levels, each posterior summarized
  by two moments, so Bernoulli or Gaussian by maximum entropy.
- **Quadratic approximation.** Each variational energy is expanded to
  second order around the previous posterior mean, not its mode, which
  differs from the Laplace approximation. The authors name this as the
  weak point.
- **Upward sweep.** Lower levels are updated using the higher levels'
  statistics from the previous trial.

## Key results

- **The model (Abstract).** "The model assumes Gaussian random walks of
  states at all but the first level, with the step size determined by the
  next highest level."
- **Scope (Introduction).** "To prevent any false expectations, we would
  like to point out that this paper is of a purely theoretical nature."
- **Update equations (Eqs 21–34).** Closed-form one-step updates of the
  form previous mean plus learning rate times prediction error. The
  level-2 learning rate is σ2, which depends on μ3; the level-3 learning
  rate is σ3κw2. The volatility prediction error is "simply a reflection
  of Bayes optimality that emerges on applying our variational update
  method" (Structural interpretation).
- **Simulations (Figures 5–8; 320 trials).** Reference agent: "As
  expected, a more volatile environment leads to a higher learning rate."
  Reduced ϑ: "this agent shows superficial (low-level) adaptability but
  has higher-level beliefs that remain impervious to new information."
  Reduced κ: "it makes it possible to have low learning rates in a highly
  volatile environment."
- **Perceptual uncertainty.** With a Gaussian-mixture likelihood at the
  first level, "Importantly, the update equations for the higher levels of
  the model are not affected by this introduction of perceptual
  uncertainty at the first level."
- **Continuous states.** The same scheme filters the 2010 USD–CHF exchange
  rate.
- **Changepoints (Discussion).** "a sudden event akin to a changepoint is
  detected without representations of changepoints being an explicit
  component of the model."
- **Efficiency (Discussion).** The simulations "each take about 5 ms on a
  standard laptop computer".

## Concepts

- **Volatility**: the variance of the random walk of x2, exp(κx3 + ω);
  x3 is "the log-volatility of the environment".
- **Informational and environmental uncertainty**: the two sources of
  uncertainty about x2, "informational, i.e., the lack of knowledge about
  x2 (represented by σ2), and environmental, i.e., the volatility of the
  environment".
- **Perceptual uncertainty** (narrow sense): a stochastic mapping from x1
  to the input. [LIT-tmpkft30](../literature.d/LIT-tmpkft30.md) uses the term more broadly.
- **Learning rate**: σ2 at level 2 and σ3κw2 at level 3; dynamic because
  they depend on the states, though the parameters are fixed.
- **Subjectively optimal**: optimal relative to the agent's own
  parameters, which may be maladaptive for the real environment.

## Connections

It is "an extension of the model proposed by Daunizeau et al. (2010b)" and
draws on the generative model of Behrens et al. (2007), a hierarchy of
Gaussian random walks. Against Bayesian models whose integrals need
"burdensome and time-consuming numerical calculations", and against
sampling, it chooses a variational scheme. Its update equations are
"similar to those of Rescorla–Wagner learning"; the Kalman filter is
cited as an earlier Bayesian scheme with RL-like updates. It links
precision-weighted prediction error to neuromodulation, dopamine above
all, as hypothesis. Mapping its states to responses or neural data, in
the manner of Daunizeau et al. (2010a,b), is left to future work. None
of Behrens et al. 2007, Daunizeau et al. 2010, Nassar et al. 2010 or Yu
& Dayan 2005 is held.

## Bearing on the record

- **The synthesis's characterization (its §3 and table).** Right that the
  model updates beliefs about outcomes and about environmental volatility,
  and that the learning rate is set by inferred uncertainty rather than
  fixed. Wrong in placement: the synthesis puts the hierarchical Gaussian
  filter in §3, "hierarchical Bayesian estimation of cognitive-process
  parameters across participants", beside HDDM's partial pooling ([LIT-563](../literature.d/LIT-563.md),
  [NOTE-466](NOTE-466.md)). That is the wrong sense of hierarchical. The hierarchy here
  is over levels of hidden states inside one agent's generative model,
  each level setting the step size of the one below; parameters are per
  agent and nothing is pooled across participants. The synthesis's own
  table row, "Hierarchical Bayesian filtering — how do beliefs and
  learning rates change over time?", is the right placement and
  contradicts its §3. Overstated: "how people update", since this paper
  fits no human data. The sentences the synthesis puts in quotation marks
  ("models how people update beliefs about both uncertain outcomes and the
  volatility of the environment itself"; "provides a principled account of
  how inferred uncertainty can influence learning") are not in the paper:
  they are A's paraphrase, and should not be cited as quotations. Missing:
  that the inversion is variational and approximate, the Rescorla–Wagner
  form of the updates, the coupling parameters as the "individual" of the
  title, and the speculative psychiatric and neuromodulatory mappings.
- **[QUESTION-325](../questions.d/QUESTION-325.md) and [CLAIM-446](../claims.d/CLAIM-446.md) (anxiety, uncertainty, avoidance).**
  Qualifies [QUESTION-325](../questions.d/QUESTION-325.md): the paper offers its reduced-κ agent as an
  anthropomorphic picture of anxiety, to "interpret underconfidence about
  estimates of environmental volatility (i.e., high σ3) as a possible
  cause of anxiety". That is a source of the uncertainty construct, drawn
  from one simulation, not evidence. It neither supports nor undermines
  [CLAIM-446](../claims.d/CLAIM-446.md)'s governance account.
- **[NOTE-1120](NOTE-1120.md), [LIT-1479](../literature.d/LIT-1479.md), [THEORY-910](../theory.d/THEORY-910.md) (Brown, Price & Dombrovski).** A
  formal source for the construction those entries use, noise against
  volatility with learning rates that should rise with volatility. It
  supports the construct and adds nothing to the empirical claim.
- **[THEORY-1182](../theory.d/THEORY-1182.md), [THEORY-897](../theory.d/THEORY-897.md), [QUESTION-329](../questions.d/QUESTION-329.md) (anxiety and learning-rate
  adjustment).** Related: the hierarchical Gaussian filter is one of the
  models such studies fit; this paper supplies the model, no evidence.
- **[LIT-1483](../literature.d/LIT-1483.md), [NOTE-1127](NOTE-1127.md) (Chou, Wilson & Smith).** Their split into
  informational and environmental uncertainty comes from this line of
  work.
- **[NOTE-1063](NOTE-1063.md), [THEORY-882](../theory.d/THEORY-882.md) (Laukkonen, Friston & Chandaria).** Those
  entries name the hierarchical Gaussian filter as the layer-wise precision
  model their account goes beyond; the reference statement is
  [LIT-tmpkft30](../literature.d/LIT-tmpkft30.md).
- **[CASE-165](../cases.d/CASE-165.md), [QUESTION-276](../questions.d/QUESTION-276.md), [LIT-1542](../literature.d/LIT-1542.md), [THEORY-484](../theory.d/THEORY-484.md), [THEORY-070](../theory.d/THEORY-070.md).** Unrelated:
  the hierarchy here is a fixed chain of volatilities, not inferred
  structure, latent features, options or control. The one tangent is that
  it offers a logistic random-walk alternative to [CASE-165](../cases.d/CASE-165.md)'s sticky
  logistic transition for a binary state with learned volatility.
- Filed: [THEORY-tmpjlua4](../theory.d/THEORY-tmpjlua4.md), the derivation and its update form.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **The quadratic approximation.** "The most important of these is that it
  depends on the variational energies being approximately quadratic." σ3
  can become negative (Eq. 29).
- **Anecdotal simulations.** "Clearly, the simulations shown in this paper
  are anecdotal and cannot fully demonstrate or establish the practical
  utility of our approach." And: "we have not yet demonstrated how our
  model can be inverted (fitted), given empirical measurements."
- **No check of the approximation** against exact inversion or sampling.
  Identifiability is deferred: some parameter settings give similar
  behaviour (Figures 6 and 8), and the authors argue, without showing,
  that the parameters are still identifiable.
- **Speculative mappings.** The psychiatric and dopaminergic readings are
  explicitly anthropomorphic or hypothetical.
- **A slip.** "Here, we stop at the fourth level" for a model with three
  state levels, presumably counting the input.

## Open questions

- How close are the variational updates to exact inversion of the same
  model, and where does the quadratic approximation break? The 2014 paper
  bounds the parameters rather than answering this.
- Can κ, ω and ϑ be recovered from behaviour? Taken up in [LIT-tmpkft30](../literature.d/LIT-tmpkft30.md).
