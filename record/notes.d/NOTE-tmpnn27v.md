---
status: Read
paper: 'LIT-tmpkft30'
title: 'Mathys et al. — Uncertainty in perception and the Hierarchical Gaussian Filter'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the Europe PMC full-text XML of the
    open-access article,
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4237059/fullTextXML,
    converted to text locally. Read: the Introduction, the theoretical
    framework (definition of the HGF, inversion with irregular intervals,
    MAP estimation, priors and transformed spaces), the examples and
    simulations (categorical outcomes and sensory uncertainty, the binary
    decision model, the inversion example, the one-armed bandit, the
    simulation study), the Discussion, Appendices A–F, the key equations
    (5, 9–16, 18, 44, 45) as linearized MathML, and the captions of
    Figures 1–10. Not read: the figure images, the loss table and the
    four-step list of the simulation procedure (list and table items the
    conversion did not render; the surrounding prose describes them), and
    the references. The Frontiers article page was fetched for metadata
    only. The reading was drafted by a delegated reader and its quotes
    rechecked against the text by the filer.
date: '2026-11-04'
summary: >-
  Generalizes the 2011 model to n levels and names it the Hierarchical
  Gaussian Filter. Each mean update at every level above the first is a
  precision-weighted prediction error, a value prediction error at level
  1 and a volatility prediction error above. Joined to a response model
  in the "observing the observer" framework, it yields per-subject MAP
  parameter estimates. Shown on simulated agents, one subject's data, and
  a simulation study in which four methods recover κ and decision noise ζ
  at low or moderate noise; κ is confounded with the prior on x3 unless
  one is fixed.
---
<!-- inactive-ok-file: THEORY-tmph6x8h THEORY-882 CLAIM-446 THEORY-1182 THEORY-1179 CASE-165 THEORY-484 THEORY-070 — Proposed or new; cited from the reading of Mathys et al. (2014) as open -->

# NOTE-tmpnn27v: Mathys et al. — Uncertainty in perception and the Hierarchical Gaussian Filter

## Contribution

It makes the model of LIT-tmpld7ct a general
framework: any number of levels, explicit update equations, a reading of
the updates as value and volatility prediction errors, a motivated
coupling between levels, irregular intervals between inputs, and a recipe
for joining it to a response model and estimating per-subject parameters
(the HGF toolbox in TAPAS). It also gives the first systematic simulation
evidence that its parameters can be recovered, and an analysis of what is
not identifiable.

## Key insight

The same update holds at every level: a prediction error weighted by how
precise the prediction below is relative to the new posterior. At the
bottom the error is about value, above it about volatility, how much the
level below has changed against how much it was expected to. The
filter is a model of perception; a separate response model turns beliefs
into choices, and the pair, inverted, says what a subject's coupling
parameters are. "The HGF furnishes a Bayesian foundation for these
heuristically derived models in that it provides learning rates that are
optimal given a particular agent's parameter setting." (Discussion)

## Assumptions

- **Coupling.** Each level's variance is exp(κi x(i+1) + ωi), exact if
  the true coupling is log-linear and otherwise a first-order expansion of
  the log of any positive coupling (Appendix A). The top level has
  constant variance ϑ.
- **Time.** Variances are multiplied by the time elapsed between inputs,
  to allow input "at irregular intervals".
- **Mean-field Gaussian posteriors** with nearly quadratic variational
  energies. Large ϑ or κ breaks this, so both get upper bounds in logit
  space: "In most cases, a choice of κi and ϑ with upper bounds at or
  below 2 will be sensible."
- **Independent priors** on the parameters, in log or logit spaces.
  Response models use quadratic loss.
- **Timing of choice.** Agents choose at trial k on beliefs from k − 1.

## Key results

- **n levels (Introduction).** "here, we extend the HGF explicitly to any
  number of levels".
- **Update form (Inversion, Eqs 9–16).** Updates yield "value prediction
  errors (VAPEs) at the first level, volatility (i.e., variance) prediction
  errors (VOPEs) at all higher levels"; "the updates of the means are
  precision-weighted prediction errors" (Discussion).
- **Sensory uncertainty (Figure 3).** "In the case of low input precision,
  the volatility estimate keeps declining because most of the variation in
  input is attributed to noise instead of fluctuations in the underlying
  tendency toward one outcome category x1 or the other."
- **Inversion example.** One subject's 320 inputs and responses from
  Iglesias et al. (2013); a response model with temperature tied to μ3
  beats one with fixed ζ by a Bayes factor of 1556, "giving the second
  model a decisive advantage despite the fact that it contains an
  additional free parameter".
- **Recovery (simulation study, Figure 7).** On a grid of κ and ζ, with
  Nelder–Mead, Gaussian-process global optimization, variational Bayes
  and MCMC (100 runs per grid point for MCMC): "All optimization methods
  could reliably distinguish different values of κ at low or moderate
  decision noise (Figure 7)." At high noise, "With GP, VB, and MCMC, they
  then exhibited a tendency to underestimate κ, while NMSA tended to
  mid-range values." Abstract: "variational Bayes offering the best
  combination of efficiency and informativeness of inference".
- **Identifiability (Appendix F).** "there is a fundamental ambiguity
  between individual differences in coupling (i.e., κ) and individual
  differences in priors for x3 (i.e., μ(0)3)."
- **Tonic and phasic (Discussion).** Payzan-LeNestour and Bossaerts's
  split of stochastic volatility from unexpected uncertainty: "This
  distinction maps exactly onto the difference between tonic and phasic
  volatility in the HGF."

## Concepts

- **HGF**: "a hierarchical Bayesian model ... in which states evolve as
  coupled Gaussian random walks, such that each state determines the step
  size of the evolution of the next lower state".
- **Volatility**: "the variance of a time series per unit of time".
  Tonic volatility is ωi, fixed over time; phasic volatility is κi x(i+1),
  varying.
- **Informational uncertainty**: the posterior variance σi, also called
  estimation uncertainty. **Environmental uncertainty**: the variance the
  level above contributes, from tonic and phasic volatility, linked to
  "unexpected" uncertainty.
- **Perceptual and sensory uncertainty**: perceptual uncertainty is used
  more broadly than in LIT-tmpld7ct; sensory uncertainty is the noise of
  input given x1 (π̂u).
- **VAPE and VOPE**: the prediction error about a state's value against
  the error about its amount of change.
- **Perceptual and response models**: the HGF is generative of inputs;
  the response model maps beliefs to actions and is not.

## Connections

It extends LIT-tmpld7ct and sits inside the "observing the observer"
framework of Daunizeau et al. (2010). It places itself among
adaptive-learning-rate accounts (Yu & Dayan; Nassar et al. 2010;
Payzan-LeNestour & Bossaerts 2011; Wilson et al. 2013), distinguishing
itself by closed-form updates derived from an objective, not by fit. Its
evidence that people learn this way is cited, not shown: Iglesias et al.
(2013) and Vossel et al. (2013). None of these is held.

## Bearing on the record

- **The synthesis's characterization (its §3 and table).** Right that the
  HGF tracks beliefs about outcomes and about volatility and replaces a
  fixed learning rate with one set by inferred uncertainty; the paper says
  learning rates are adjusted "continually at each level separately".
  Wrong in placement, as for LIT-tmpld7ct: the synthesis files the HGF
  under across-participant hierarchical parameter estimation, the HDDM
  sense (LIT-563, NOTE-466). This is the wrong sense of hierarchical. The
  hierarchy is over states inside one agent's model; parameters are
  estimated per subject by MAP with fixed priors and no group-level
  pooling. The paper never builds a population model. Its table row
  "Hierarchical Bayesian filtering" is the right placement. The sentences
  the synthesis puts in quotation marks are not in this paper either: they
  are A's paraphrase. Missing: the perceptual and response model split,
  the VAPE and VOPE structure, the informational and environmental and the
  tonic and phasic distinctions, the identifiability limits, and that the
  empirical content is one subject plus simulations.
- **NOTE-1063, THEORY-882 (Laukkonen, Friston & Chandaria).** Qualifies
  THEORY-882, which is a THEORY and gets no dated note here: the HGF sets
  the precision of predictions level by level (Eq. 13), but it has no
  global hyper-model, so the difference THEORY-882 draws is real. Whether
  it is unmet is for that note.
- **QUESTION-325 and CLAIM-446 (anxiety and avoidance).** Qualifies
  QUESTION-325 indirectly. The paper ties high sensory uncertainty to a
  falling volatility estimate and inconsistent choice, but has no anxiety
  model. It supplies the machinery the uncertainty accounts use:
  uncertainty-specific learning rates, and response models that include
  μ3. Nothing bears on CLAIM-446.
- **NOTE-1120, THEORY-910, LIT-1479 (Brown, Price & Dombrovski).** The
  Figure 3 result is the formal counterpart of NOTE-1120's claim C4, that
  anxiety misreads noise as change: under the HGF, misreading noise as change is an underestimate
  of sensory noise (too high π̂u) that inflates μ3. It supports the
  construct as formalizable, and gives no evidence about anxiety.
- **QUESTION-329, THEORY-1182, THEORY-897 (learning-rate adjustment in
  anxiety).** Related: the HGF is the instrument usually fitted, and
  Appendix F's ambiguity between κ and μ(0)3 bears on how group
  differences in learning about volatility can be read.
- **LIT-1483, NOTE-1127 (Chou, Wilson & Smith).** The same
  informational and environmental vocabulary.
- **THEORY-1179, THEORY-285.** Adjacent precision-weighting accounts of
  psychopathology in the same line; the HGF is their discrete-time
  filtering counterpart.
- **QUESTION-276, CASE-165, LIT-1542, THEORY-484, THEORY-070.** Unrelated;
  the HGF learns no structure.
- **Parameter recovery, a separable claim, not filed.** In simulation, κ
  and response noise ζ of the three-level binary HGF are recovered from
  320 binary choices by all four methods at low or moderate noise. It
  would need its own THEORY, with an independent recovery study, over
  more parameters and input sequences, as its `promote_when`.
- Filed: THEORY-tmph6x8h, the n-level update form.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **The quadratic approximation remains.** Large ϑ can drive the top-level
  precision below zero, the agent knowing "less than nothing"; the
  authors bound the priors rather than fix the scheme.
- **Identifiability.** When μi is not in the response model, μ(0)i, κi
  and ωi are confounded up to a choice of coordinates, and two of them must
  be fixed (Appendix F).
- **Recovery at high noise.** κ is underestimated (GP, VB, MCMC) or pulled
  to mid-range (Nelder–Mead); VB and MCMC become slightly overconfident
  about ζ.
- **A narrow recovery study.** Two parameters, one input sequence, one
  model (three levels, binary), the others fixed.
- **Thin empirical illustration.** One subject; the bandit data are from
  a study "in preparation". Upper bounds on priors are set by judgement.
- **No comparison on data** against rival adaptive-learning-rate models;
  the claim to stand apart is derivation from free energy, not better fit.

## Open questions

- Does recovery hold for ω, ϑ and the priors, on other input sequences
  and with more levels?
- Do HGF parameters pooled across subjects, in the HDDM manner, recover
  better than per-subject MAP? The paper does not try.
