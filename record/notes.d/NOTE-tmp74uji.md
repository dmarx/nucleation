---
status: Read
paper: LIT-tmp2p2lh
title: 'The Time Course of Perceptual Choice: The Leaky, Competing Accumulator Model'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from McClelland's posted scan (43 pages, printed pp.
    550–592) through OCR, with Equations 4 and 8–10 checked against page
    images. Main text, all three experiments, the Hick's law and word
    recognition sections, General Discussion and Appendix A read;
    Appendices B–E skimmed. Figures were read from their captions and the
    text; the OCR does not recover plotted data. Results the paper takes
    from Ratcliff (1978, 1988), Vickers (1970), Hick (1952) and McClelland
    & O'Regan (1981) are taken as it reports them.
date: '2026-10-03'
summary: >-
  The LCA: dx_i = [ρ_i − k x_i − β Σ_{j≠i} x_j] dt/τ + ξ_i √(dt/τ), with
  x_i floored at 0. For two choices x₁ − x₂ is an OU process with K = k − β;
  d′(t) = d_asy (1 − e^{−Kt})/√(1 − e^{−2Kt}) and d_asy = (2v/σ)√(1/K).
  On new time–accuracy data the OU curve beats diffusion-with-drift-variance
  in 7 of 9 fits (combined likelihood ratio about 62). Leak versus
  inhibition predicts recency versus primacy; 2 of 6 participants favoured
  the end cluster and 2 opposed it. A fixed-accuracy criterion gives Hick's
  law in all three models simulated, so it does not discriminate them.
---

<!-- inactive-ok-file: THEORY-056 — Proposed; named as the record's nearest account of competing motive states, with no relation claimed -->

# NOTE-tmp74uji: The Time Course of Perceptual Choice: The Leaky, Competing Accumulator Model

## Contribution

The paper adds two principles to stochastic accumulation models of choice:
leakage of accumulated information, and competition between alternatives by
lateral inhibition. Recurrent self-excitation and a threshold-linear
nonlinearity are included, but mostly to balance leak and to stop negative
activations from propagating. It shows that the classical diffusion model is a
limiting case (balanced leak and inhibition), and it tests the new principles
on time–accuracy curves, latency–discriminability functions, RT distributions,
a new sequence-integration experiment, Hick's law and an interaction in word
identification.

## Key insight

A choice between alternatives can be both a race and a comparison at once. If
every alternative has its own accumulator and each accumulator suppresses the
others, the winner's activation comes to reflect its evidence *relative* to the
rest, while the decision can still be triggered by a fixed absolute level. The
dynamics of the difference between two such units depend on one number: leak
minus inhibition. When the two balance, the system integrates perfectly, as the
diffusion model does. When leak wins, old evidence fades and late evidence
dominates. When inhibition wins, an early lead is amplified and early evidence
dominates. In both unbalanced cases, accuracy given unlimited time is capped.

## Assumptions

- **Units as populations** (pp. 554–555): each accumulator is a neural
  population. Its activation is the population input current and its output
  the mean firing rate, related by a threshold-linear function f(x) = x for
  x ≥ 0 and 0 otherwise.
- **Noise**: zero-mean Gaussian noise added to each unit's input, justified by
  the central limit theorem over spiking populations (p. 555).
- **Dynamics** (Eq. 4, p. 559): dx_i = [ρ_i − k x_i − β Σ_{j≠i} x_j] dt/τ +
  ξ_i √(dt/τ), then x_i → max(x_i, 0). Here k = λ − α is net leak (passive
  decay minus self-excitation), β is lateral inhibition, and ρ_i is
  non-negative feed-forward input. Appendix A shows by simulation that
  truncating at 0 approximates the version with separate fast decay below 0
  and slow net decay above it.
- **Inputs sum to one** in two-choice continuum tasks, ρ₁ + ρ₂ = 1, so
  v = ρ₁ − ρ₂ (p. 559).
- **Fixed delays** for encoding and response output, lumped into T₀; no
  trial-to-trial variability in T₀ or in the input in the main fits.
- **Response rules**: in time-controlled tasks the most active unit at the
  signal is chosen; in RT tasks the first unit to reach criterion θ.
- **Hick's law simulations**: the criterion is adjusted per set size to hold
  accuracy fixed (95% or 99%), and input to each accumulator does not depend
  on the number of alternatives.

## Key results

- **Reduction to an OU process (Eqs. 5–8, pp. 560–561).** For two units in
  the linear regime, x = x₁ − x₂ obeys dx = (v − Kx) dt/τ + ε√(dt/τ), with
  K = k − β. Starting from 0, x(t) is Gaussian with μ(t) = (v/K)[1 − e^{−Kt}]
  and SD(t) = (σ/√K)√(1 − e^{−2Kt}). K = 0 is the classical diffusion
  process, with μ = vt and SD = σ√t.
- **Time–accuracy function (Eqs. 9–10).** d′(t) = d_asy (1 − e^{−Kt}) /
  √(1 − e^{−2Kt}), and d_asy = (2v/σ)√(1/K). Accuracy is bounded for K > 0.
  Simulations of the full nonlinear model show the curves depend on |K| only:
  β = 0 and β = 0.4 with k = 0.2 give "virtually identical" curves (Fig. 4).
- **Trajectories differ where accuracy does not (Fig. 5).** Pure leak keeps
  the distribution of x₁ − x₂ bounded. Self-enhancement makes it diverge.
  Leak plus inhibition makes it bimodal, because the losing unit is suppressed
  to zero and the winner then feels only leak. The authors read this as the
  system producing "essentially a binary decision".
- **Experiment 1 (time–accuracy, response signal; 3 participants, lags 0 to
  2,000 ms).** Fitting the OU and drift-variance (DDV) curves with three
  parameters each per curve, 7 of 9 likelihood ratios favour OU, and their
  product is 62.02 (Table 1). With one rate and one offset per participant,
  OU is favoured for all three, with a combined ratio of 43.14 (Table 2).
  Using lag alone as integration time, OU is favoured 197 to 1 and 106 to 1.
  Fitted OU time constants lie between about 100 and 400 ms. The full
  nonlinear model, simulated with parameters derived from the OU fit, matches
  Participant 2's curves (Fig. 9).
- **Latency–discriminability (Vickers 1970, 5 participants).** Fitted with six
  parameters and no drift or starting-point variability, the model captures
  accuracy and RT mean and SD for 3 participants. It reproduces errors slower
  than correct responses and rising skew and kurtosis, which it was not fitted
  to. It misses the dips for Participants 1 and 5, which the authors call
  anomalous for every model they know. Lateral inhibition is what makes the
  latency–probability functions U-shaped (Fig. 15).
- **Experiment 2 (RT distributions; 2 participants, 960 trials per level).**
  Fitted to accuracy, RT mean, SD and skew, the model reproduces the shapes of
  the correct RT distributions. Skew rises with discriminability (1.3, 1.8,
  2.2 for Participant 1).
- **Experiment 3 (information arrival time; 6 participants, 16-item S/H
  sequences at 60 per second, 256 ms).** On balanced sequences ending in a
  4-item cluster, 2 participants favoured the end cluster (recency), 2 opposed
  it (primacy) and 2 were neutral (Table 4). Fitted leak and inhibition
  account for each pattern, and the same parameters predict accuracy on the
  40-item background trials. The neutral, balanced participants were the most
  accurate, as the model predicts.
- **Hick's law (Fig. 23).** With the criterion adjusted to keep accuracy
  fixed, RT is linear in log N for the classical accumulator, the LCA and a
  max-minus-next accumulator. With a fixed criterion none of them gives a
  logarithmic law. The authors say this does not support the LCA over the
  others.
- **Word identification (McClelland & O'Regan 1981).** Lateral inhibition
  implements an "intersection principle". One weak source (context or visual
  preview) activates m candidates whose mutual inhibition cancels its benefit.
  Two independent weak sources leave the target with double input, and for
  0.5 < β < 1 its competitors are suppressed to zero. Simulated: 42.9, 42.8
  and 34.7 mean steps (Table 5).
- **Confidence.** Because suppression is partial, the activation difference at
  response time can serve as confidence. It falls with longer RT in free
  response and rises with time in time-controlled tasks, as Vickers's
  confidence data require.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the linear two-choice case the accumulator difference is an OU process with net leak K = k − β, and K = 0 is the classical diffusion model | strong (derivation) | Eqs. 5–8 |
| C2 | Asymptotic accuracy is bounded whenever K ≠ 0, and the time–accuracy curve depends only on \|K\| | strong for the linear case; checked by simulation for the nonlinear one | Eqs. 9–10, Fig. 4 |
| C3 | Leakage fits empirical time–accuracy curves better than drift variance | weak to moderate: 3 participants, likelihood ratios mostly small, and the DDV compared lacks decision boundaries, which the authors concede could close the gap | Tables 1–2, p. 568 |
| C4 | The balance of leak and inhibition sets primacy versus recency, and imbalance costs accuracy | moderate: confirmed on 6 participants, but alternative attentional accounts not excluded | Exp. 3, Fig. 21 |
| C5 | Lateral inhibition reproduces asymmetric, U-shaped latency–probability functions without drift variance | moderate: 3 of 5 Vickers participants fitted; fits not optimal by the authors' account | Figs. 11–15 |
| C6 | Hick's law follows from holding accuracy fixed across set sizes, not from a capacity limit | moderate in simulation; not discriminating between models | Fig. 23 |
| C7 | The LCA reconciles relative-evidence effects with confidence data that favour absolute criteria | moderate: simulation reported in prose only | pp. 586 |

## Concepts

- **leaky, competing accumulator**: an accumulator per alternative, subject to
  leakage and to lateral inhibition from the others.
- **net leakage k**: passive decay minus recurrent self-excitation, λ − α.
- **differential leakage K**: k − β, the net leak of the difference between
  two units.
- **diffusion with drift variance (DDV)**: Ratcliff's 1978 diffusion model with
  trial-to-trial variability in drift.
- **time-controlled vs information-controlled tasks**: response-signal tasks,
  where time is fixed by the experimenter, versus standard RT tasks, where the
  participant's criterion fixes it.
- **intersection principle**: support from two independent weak sources
  singles out the one candidate both favour.

## Connections

- **Bogacz et al. 2006 ([LIT-tmp93b13](../literature.d/LIT-tmp93b13.md)).** Linearises this model as the "mutual
  inhibition model", proves the reduction to the OU and diffusion models
  analytically, and adds what this paper lacks: that the balanced version is
  optimal, and that optimality also needs leak and inhibition to be large.
- **Ratcliff & McKoon 2008 ([LIT-tmpcmcw7](../literature.d/LIT-tmpcmcw7.md)).** The rival single-process view. It
  credits accumulator models of this kind with possibly comparable fits, but
  disputes how they could relate to likelihood-based decisions (its §7.1).
- **Schurger, Sitt & Dehaene 2012 ([LIT-tmpzrigj](../literature.d/LIT-tmpzrigj.md)).** Uses a single leaky
  stochastic accumulator from this paper, with a constant input as urgency, to
  model when spontaneous movements are initiated.
- **Frijda et al. ([LIT-540](../literature.d/LIT-540.md)) and [THEORY-056](../theory.d/THEORY-056.md).** These argue that emotion
  regulation is one action readiness checking another, not a separate
  regulator. The LCA gives a formal model of mutually suppressing response
  tendencies with no supervisory unit. That is my analogy, not the paper's
  claim; it is about perceptual choice only.

## Bearing on the record

- It anchors `behavioral-integration` at the level of a single decision: many
  candidate responses resolved into one by competition plus an absolute
  criterion. See the batch report for a candidate THEORY on balanced
  integration.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Small samples.** The new experiments have 3, 2 and 6 participants.
- **The leak-versus-drift-variance contest is unresolved by its own account.**
  The authors concede that DDV with starting-point variance and decision
  boundaries "tend[s] to bring" its curves close to the shifted exponential,
  and that "both leakage and drift variance are factors" (pp. 568, 585).
- **Fits are not optimal.** The latency–discriminability fits ran only 8,000
  Metropolis swaps, and noise in the fitting is acknowledged.
- **Neural motivation is analogy.** Chelazzi et al.'s IT recordings show
  competition consistent with lateral inhibition, but the model is a single
  layer with fixed delays, and its parameters are not measured in tissue.
- **Hick's law** holds only for criterion values below the expected
  asymptote of the correct unit; with unbalanced K and high thresholds the
  linear relation breaks down (p. 582).

## Open questions

- Which dominates in a given task, leakage or drift variance? The authors
  expect the answer to be task-dependent (memory tasks favouring drift
  variance).
- Do ambiguous primes give a reduced but non-zero benefit, as partial lateral
  inhibition predicts, or none, as a best-minus-next criterion predicts?
- How do leak and inhibition play out in multilayer architectures? This is
  left for later work.

## Corrections

- none to a seeded skim (there was no seed)
- **Citation.** The DOI as printed on the article is 10.1037//0033-295X.108.3.550
  (double slash), which is APA's older form. Crossref resolves
  10.1037/0033-295X.108.3.550.
