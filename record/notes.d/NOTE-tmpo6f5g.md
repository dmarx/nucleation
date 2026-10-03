---
status: Read
paper: LIT-tmp93b13
title: 'The Physics of Optimal Decision Making: A Formal Analysis of Models of Performance in Two-Alternative Forced-Choice Tasks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Main text (pp. 700–753) and Appendix B read in full from the published
    PDF on Moehlis's UCSB page; Appendix A (derivations, about 12 pages)
    read only by its section titles, so the proofs it contains (SPRT
    optimality, O-U error rates and decision times, optimal-threshold
    conditions, threshold learning, biased choices, lower bounds under
    variable drift) are taken as the main text reports them. Displayed
    equations lose symbols in the PDF text layer; equations given below
    were reconstructed from the text and checked against the prose
    definitions around them. Figures were read from captions.
date: '2026-10-03'
summary: >-
  Proves the pure DDM is the continuum limit of the SPRT and so the
  optimal two-choice decider. The linearised Usher–McClelland model
  decouples into a difference process, an O-U with λ = w − k, and a stable
  sum process, so it reduces to the DDM when k = w and both are large;
  feedforward inhibition does so at u = 1, pooled inhibition with fast
  inhibitory units, the race model never. The reward-rate-optimal threshold
  is unique and depends only on the total delay, giving a parameter-free
  optimal performance curve (peak decision time about 0.2 of the delay at
  ER about 18%).
---

# NOTE-tmpo6f5g: The Physics of Optimal Decision Making: A Formal Analysis of Models of Performance in Two-Alternative Forced-Choice Tasks

## Contribution

A systematic mathematical comparison of six two-choice decision models, the
DDM, O-U, race, mutual inhibition, feedforward inhibition and pooled
inhibition, which locates each relative to the SPRT. It then adds a theory of
how the threshold should be set under four criteria (Bayes risk, reward rate,
and two accuracy-weighted variants of reward rate), derives optimal
performance curves as predictions, and extends both analyses to biased priors
and biased rewards.

## Key insight

The question "which model of choice is right?" and the question "what would
an optimal decider do?" have the same answer in a precise regime. Integrating
the *difference* of the evidence for two options is the SPRT. Leaky,
competing neural units compute that difference when their leak and their
mutual inhibition cancel, and they do so in one dimension when both are strong
enough to pin activity to a line. Inhibition is what turns two accumulators
into one comparison; leak balanced against it is what makes the comparison
lossless. Optimality then moves from the mechanism to its settings: a
threshold that trades speed for accuracy, and a starting point that encodes
prior odds.

## Assumptions

- **Two alternatives**, evidence drawn i.i.d. within a trial from one of two
  distributions; drift fixed within a trial.
- **Linearised models.** All network models are linearised (threshold-linear
  floors ignored), with activity measured from baseline so that y < 0 need not
  mean negative firing.
- **No cost for sampling** in the optimality of the SPRT and Neyman–Pearson
  test (p. 703); time enters only through the reward criteria.
- **Extended equivalences** require the total input I₁ + I₂ to be constant
  across trials and the two starting points to be anticorrelated
  (y₁(0) = −y₂(0)); the authors note there is no cortical evidence yet for
  the latter.
- **Pooled inhibition reduction** requires the inhibitory population's decay
  to be fast relative to the excitatory one, an assumption they say needs
  physiological test (footnote 7).
- **Rewards** follow each correct response, and delays D (response to next
  stimulus) and D_p (extra penalty delay after errors) are fixed per block.

## Key results

- **DDM formulas (Eqs. 5–9).** dx = A dt + c dW. Under interrogation at T,
  ER = Φ(−A√T/c). In free response with thresholds ±z, ER = 1/(1 + e^{2Az/c²})
  and DT = (z/A) tanh(Az/c²). ER and DT depend only on ratios of A, z and c².
- **Model reductions (Fig. 4; Eqs. 18–38).** In rotated coordinates the
  linearised mutual inhibition model decouples into x₁ (difference), an O-U
  process with λ = w − k, and x₂ (sum), always a stable O-U process with rate
  k + w. With k = w the difference is a pure DDM, with drift (I₁ − I₂)/√2 and
  threshold z = √2 Z − (I₁ + I₂)/(√2(k + w)) (Eq. 26). The feedforward
  inhibition model equals the DDM exactly when u = 1. The pooled inhibition
  model equals a mutual inhibition model with decay k + ww′/k_inh − v and
  inhibition ww′/k_inh. The race model is not reducible.
- **Interrogation optimum.** Error rate is minimised at λ = 0, whatever the
  magnitude of k and w, even k = w = 0. As Usher and McClelland observed,
  error depends only on |λ|. With variable starting points, λ < 0 (leak
  dominant, recency) can do better, because it discounts the noisy start.
- **Free-response optimum (Fig. 10).** At fixed ER, DT is shortest when k = w,
  and it falls toward the DDM's value as k = w grows. The race model is
  slowest.
- **Unbounded accuracy (Table 1).** Under interrogation, ER → 0 as T → ∞ only
  for λ = 0; otherwise a finite floor depends only on |λ| (Eq. 39). In free
  response, ER → 0 for λ ≤ 0, but for λ < 0 decision times diverge. With
  drift variability no model reaches zero error; the floor is the fraction of
  trials with negative drift.
- **Optimal thresholds (Fig. 12).** For every criterion the optimal threshold
  is zero when drift is zero, rises, then falls as drift dominates noise; it
  rises with noise to a limit and rises with delay. For reward rate the
  condition is e^{2z̃ã} − 1 = 2ã(D_total − z̃), with z̃ = z/A and ã = (A/c)²,
  and a unique solution. It depends on D and D_p only through their sum (any
  RR-maximising mechanism shares this; Appendix A).
- **Optimal performance curves (Fig. 13).** For reward rate, DT/D_total is a
  function of ER alone: peak DT about 20% of the maximum inter-decision
  interval, at ER about 18%. For Bayes risk (Edwards 1965), peak DT about
  0.136q at ER about 13.5%.
- **Threshold learning (Fig. 15).** Reward rate falls more steeply below the
  optimal threshold than above it, so overestimating costs less than
  underestimating, and gradient learning finds the upward direction more
  easily. Adaptive learners should therefore set thresholds too high. The
  authors offer this as an explanation, in reward-rate terms alone, of
  people's apparent bias toward accuracy.
- **Biased priors (Eqs. 62–63, Fig. 16).** The optimal starting point is
  proportional to the log prior odds (Edwards); Link's rule, minimising ER at
  fixed threshold, is half that. Estimates from Laming, Link and Van Zandt et
  al. lie closer to Edwards's rule, significantly so for Laming's data
  (paired t-test, p = 0.04). With constant signal strength, only the start
  should move; with mixed difficulty, drift should be biased too. Above a
  critical bias or below a critical delay, the RR-optimal policy is to skip
  integration and always choose the likelier option.
- **Biased rewards (Fig. 18).** The optimal start depends on delay: like
  probability bias for short D_total, halfway to it for long D_total.
- **Neural fit.** Platt and Glimcher's prestimulus LIP activity grew roughly
  linearly with both prior probability and reward share from 20% to 80%, as
  the optimal start points do over that range.
- **Experiment.** 20 participants, dot motion at fixed coherence, four delay
  conditions. One representative participant's extended-DDM fit is reported
  (mA = 1, sA = 0.31, sx = 0.14, c = 0.33; thresholds rising from 0.16 to
  0.26 with delay; T₀ = 0.37 s). The full analysis is deferred to a later
  report.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The pure DDM implements the SPRT (free response) and Neyman–Pearson test (interrogation), so it is the optimal two-choice decider | strong (classical theorems, re-derived) | p. 703–704, Appendix A |
| C2 | The linearised mutual inhibition model reduces to the DDM when leak equals inhibition and both are large | strong for the linear model (derivation) plus simulation | Eqs. 18–26, Figs. 6–8 |
| C3 | Among mutual inhibition models, balanced and strong leak and inhibition maximise performance | strong in the linear model; simulation for the extended model | Figs. 9–10, Table 1 |
| C4 | The reward-rate-optimal threshold is unique and depends on delays only through their sum | strong (derivation) | Eq. 51, Appendix A |
| C5 | The optimal performance curve relating DT/D_total to ER is parameter-free | strong as mathematics; its empirical test is deferred | Eq. 58, Fig. 13 |
| C6 | Threshold-learning asymmetry predicts a bias toward over-cautious thresholds | moderate (analysis), untested here | Fig. 15, Inequality 61 |
| C7 | Optimal starting points under bias follow log prior odds, and data favour this over Link's rule | moderate: three data sets, one significant | Fig. 16b |
| C8 | Prestimulus LIP activity conforms to RR-optimal starting points | weak to moderate: qualitative, near-linear range, and slope difference not significant | Platt & Glimcher comparison |

## Concepts

- **interrogation vs free-response paradigm**: decision forced at a set time
  versus made when the participant chooses.
- **balanced** mutual inhibition model: decay equals inhibition (λ = 0).
- **decision line**: the attracting line in the (y₁, y₂) plane along which the
  difference evolves once the sum has settled.
- **reward rate (RR)**: the proportion of correct trials divided by the
  average time between decisions, which includes RT, the delay D and, after
  errors, the penalty delay D_p (Gold & Shadlen's definition).
- **optimal performance curve**: the relation between ER and normalised DT
  that must hold if the threshold is optimal for a criterion.
- **signal-to-noise ratio ã** = (A/c)², and normalised threshold z̃ = z/A.

## Connections

- **Usher & McClelland 2001 ([LIT-tmp2p2lh](../literature.d/LIT-tmp2p2lh.md)).** The source of the mutual
  inhibition model, and of the observations that λ's sign does not affect
  accuracy and that the balanced model is fastest at fixed accuracy (their
  1995 technical report). This paper derives them and adds the requirement
  of large leak and inhibition.
- **Ratcliff & McKoon 2008 ([LIT-tmpcmcw7](../literature.d/LIT-tmpcmcw7.md)).** The empirical counterpart. This
  paper uses Ratcliff's extended DDM, and Ratcliff and Tuerlinckx's quantile
  fitting; Ratcliff and McKoon later reject its account of threshold setting
  as unable to explain verbal calibration.
- **Schurger et al. 2012 ([LIT-tmpzrigj](../literature.d/LIT-tmpzrigj.md)).** Their model is the leak-dominated
  (λ < 0) single accumulator with a constant input. In this paper's terms it
  is a stable O-U process with an interior attractor, whose crossings at a
  threshold above the attractor are driven by noise. That is the regime this
  paper shows gives long and variable decision times. The mapping is mine;
  neither paper draws it.
- **Wiecki et al. 2013 ([LIT-tmp15yr3](../literature.d/LIT-tmp15yr3.md)).** Estimates the extended DDM whose
  parameters this paper interprets as controlled quantities: drift (attention),
  starting point (expectancy) and threshold (caution).

## Bearing on the record

- It supplies a normative reading of `behavioral-integration` at the level of
  one decision: accumulate the difference, and set threshold and start by the
  utility at stake. Its last section recasts cognitive control as that tuning.
  See the batch report for a candidate THEORY.
- **No ML instruction.** Although the SPRT and reward-rate optimisation are
  shared with machine learning, the paper is about human and animal decisions
  and gives no ML practice. Nothing here belongs in the anthology.

## Limitations

- **Two alternatives, stationary drift.** Multi-alternative optimality
  (MSPRT) and within-trial changes of signal are pointed to, not treated.
- **Linearised models.** Thresholding nonlinearities are dropped; their
  effects are discussed elsewhere (Brown et al. 2005).
- **Variability is not optimal.** The extended DDM fits better than the pure
  one, but its drift and starting-point variability are by construction
  suboptimal; the paper explains them by attention and history, as adaptive on
  a broader scale, without a model.
- **Accuracy floors.** That people do not reach perfect accuracy at long times
  is waved to Ratcliff's (1988) bounded diffusion, confirmed "but we do not
  treat this issue here".
- **The experiment** is reported for one participant; the predictions about
  delays and optimal performance curves are not tested here.

## Open questions

- Do people's decision times and errors fall on the parameter-free optimal
  performance curve, and does performance depend on delays only through their
  sum?
- When starting point varies, can unbalanced (leak-dominant) networks be
  optimal in practice?
- How do neuromodulatory systems (locus coeruleus is suggested) implement
  gain changes for interrogation?

## Corrections

- none to a seeded skim (there was no seed)
