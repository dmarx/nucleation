---
status: Read
paper: LIT-tmpqt7ea
title: 'Sánchez-Cañizares — Decision-making through irruption theory'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read in full on 2026-11-03 from the publisher's open-access PDF
    (link.springer.com/content/pdf/10.1007/s11097-026-10164-0.pdf, CC BY
    4.0, online-first, 23 pp., accepted 6 May 2026). Text extracted with
    pypdf. I read every page: abstract, §§1–6, footnotes 1–17, the six
    figure captions and the references. Pages below are the PDF's; the
    online-first PDF has no journal pagination. Figures 4–6 reproduce
    other papers' figures and were read from their captions. The model of
    §4 was re-simulated (see Key results).
date: '2026-11-03'
summary: >-
  Uses the Haken–Kelso–Bunz potential with parameters switched in time
  (no landscape, then two wells, then one) as a model of binary decisions,
  and compares the resulting rise and fall of the across-trial standard
  deviation of cos φ with trial-to-trial variability of event-related
  potentials in Sergent et al. 2021, Wolff et al. 2019 and 2021 and Hua et
  al. 2025, qualitatively only. It reinterprets Froese's irruption as the
  onset of a two-attractor landscape and absorption as the passage to one
  (IAT*), reversing the sign of Froese 2024's variance hypothesis. The
  mind's role is to set the control parameters, "selecting the relevant
  physical coarse-graining", which is not derived and is said to be
  underivable. Re-simulation confirms the trend, but under the stated noise
  the deviation settles near 0.40, not 0.
---
<!-- inactive-ok-file: LIT-1132 LIT-tmp31f3t LIT-tmp8fjub CLAIM-tmpex9rg CLAIM-478 QUESTION-071 THEORY-tmp1jrus — Proposed, Open, Deferred or Unavailable; the entries this reading bears on, cited as open -->

# NOTE-tmpbmoj1: Sánchez-Cañizares — Decision-making through irruption theory

## Contribution

It gives Irruption Theory, which the author says "lacks a formal,
'axiomatic' grounding" (p. 2), a mathematical stand-in: the HKB potential
with time-dependent parameters a(t), b(t). It sets three regimes in
sequence and computes means and standard deviations over initial
conditions. It claims, for the first time, that HKB fits decision-making
results, specifically "neural variability quenching through time-changing
control parameters" (p. 18). It also revises Froese's pairing of irruption
and absorption, as IAT*.

## Key insight

A decision is modelled as a change in the number of attractors: a landscape
with two wells opens (one per option), then closes to one. Variability
across trials rises while two wells are open and falls once one remains.
The mind does not push the state. It sets the landscape: "Through
'irruption,' the mind formally sets up the relevant attractor landscape in
the brain. Through the 'absorption' of physiological variability
(reduction of the number of attractors), conscious experience is
associated with its distinctive brain signature" (p. 7). "Mind and brain
drive the dynamics, but none completely controls it" (p. 7).

## Assumptions

- **The model** (eqs. 1, 2, p. 8): V(φ) = −a cos φ − b cos 2φ,
  φ̇ = −∂V/∂φ = −a sin φ − 2b sin 2φ, plus a noise term √q ξ(t), with φ
  the relative phase of two oscillators, here two neuronal assemblies
  firing at nearly the same frequency (p. 13).
- **The schedule** (eq. 3, p. 8): a = b = 0 for 0 ≤ t < 1; a = b = 1 for
  1 ≤ t < 2; a = 1, b = 0 for 2 ≤ t ≤ 15; q = 1 throughout (Fig. 2, 3
  captions).
- **The statistics** (eqs. 4–7, p. 11) are over the initial condition φ(0),
  taken uniform on (−π, π]. The text says "the differences that justify a
  statistical treatment in a deterministic equation stem from the different
  initial conditions" (p. 10), although a noise term is present.
- **The noise** is described as ξ(t) ∈ [−1, 1], with zero mean and
  delta-correlated (pp. 8–9). Bounded values and delta correlation do not
  go together for continuous-time white noise; the paper does not say
  which it simulated. Footnote 10 (p. 9) uses "noise" more broadly, for
  uncontrolled and "possibly biased" influences that "can modify parameters
  a and b"; the white-noise term cannot.
- **IAT* is a modelling assumption**, "not intended as a broader conceptual
  revision of IAT" but restricted to "binary decision-making tasks"
  (pp. 2, 20).

## Key results

- **The bifurcation (p. 8).** With b = 1, there are two minima, at 0 and π,
  for |a| < 4, and one otherwise. *Checked*: V″ = a cos φ + 4b cos 2φ is
  positive at π iff a < 4b and at 0 iff a > −4b. This is the anti-phase
  stability boundary b/a = 1/4 of [THEORY-1227](../theory.d/THEORY-1227.md).
- **The simulated trend (pp. 10–12, Figs. 2, 3).** In 0 ≤ t < 1, cos φ has
  mean 0. In 1 ≤ t < 2 the standard deviations of φ and cos φ rise ("a
  bump") as paths split between the wells. For t ≥ 2 "the average values of
  φ(t) and cos φ(t) tend to 0 and 1, respectively, and their standard
  deviations smoothly decrease to 0 after their bump" (p. 12). "The
  influence of white noise is less relevant than the influence of changes
  in parameters a and b."
- **Re-simulation (this reading).** 20,000 paths, Euler–Maruyama with
  dt = 10⁻³, φ(0) uniform, eq. (3), Gaussian white noise √q dW.
  - *q = 0:* the SD of cos φ goes 0.71 (t = 0.99), 0.93 (t = 1.5), 0.98
    (t = 1.99), 0.82 (t = 5), 0.12 (t = 10), 0.01 (t = 15), and the mean of
    cos φ reaches 1.00. The paper's description holds.
  - *q = 1, as stated:* the SD of cos φ goes 0.71, 0.87, 0.89, 0.48 (t = 5),
    then stays at 0.40 (t = 10, 15), with the mean of cos φ at 0.70. These
    are the stationary values of p(φ) ∝ exp(2a cos φ / q) with a = 1 (mean
    0.698, SD 0.405, computed). So under the stated noise the rise and fall
    is reproduced, but the deviation does not go to 0. The paper's Fig. 3
    must have used a weaker effective noise than q = 1 Gaussian white noise,
    perhaps the bounded ξ, or else its "decrease to 0" is wrong for q = 1.
- **Sergent et al. 2021 (pp. 13–15; Fig. 4).** 20 participants classified a
  vowel in noise at several SNRs. At the critical SNR near −9 dB, the
  ERP's SD at Cz peaks around 400–500 ms. The author reads the trend off
  their Fig. 1F, since "we do not possess a graph of the standard deviation
  over time for fixed SNR" (p. 14). He proposes a/b as a proxy for SNR. Two
  mismatches are stated: the ERP returns to baseline faster than the model
  (fn. 17), and at low SNR the experimental SD is smaller than at moderate
  to high SNR, "which our HKB model does not reproduce" (p. 15).
- **Wolff et al. 2019 and 2021 (pp. 15–16; Fig. 5).** 34 participants made
  moral trade-off decisions. Trial-to-trial variability peaks near 100 ms
  and declines after 200 ms; "the quantitative prediction makes little
  sense at this level, the qualitative agreement … is remarkable" (p. 16).
  The model cannot address pre-stimulus effects, because σ_cos φ is
  constant before t = 1.
- **Hua et al. 2025 (pp. 16–18; Fig. 6).** On-task deliberate thought
  raised pre-stimulus variability and post-stimulus inter-trial phase
  coherence and shortened response times. A direct comparison "is not
  possible" (p. 17). The author re-maps the model so that the prepared
  participant starts at a = b = 1.
- **The reversal of Froese 2024 (fn. 12, p. 10).** Froese hypothesized that
  irruption coincides with decreases in shared variance and absorption with
  increases. "Here, however, we claim the opposite", citing critical
  fluctuations and slowing before transitions.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With b = 1, the HKB potential has two attractors (φ = 0, π) for \|a\| < 4 and one otherwise | strong | analytic (p. 8); checked here |
| C2 | Switching a, b from zero to bistable to monostable makes the across-initial-condition SD of cos φ rise then fall | strong | simulation (Fig. 3); reproduced here |
| C3 | That SD falls to 0 after the switch to one attractor, with q = 1 | weak | Fig. 3 and p. 12; contradicted by re-simulation with Gaussian white noise, where it settles near 0.40 |
| C4 | The model qualitatively matches the rise and fall of ERP trial-to-trial variability in Sergent et al. 2021 and Wolff et al. 2019, 2021 | weak | visual comparison with reproduced figures; the author: "only qualitative" (p. 18); two stated mismatches (p. 15, fn. 17) |
| C5 | In IAT*, irruption is the onset of a bistable landscape and absorption the passage to a single attractor, both correlated in mind and brain | weak | proposed as a modelling assumption (pp. 6, 20) |
| C6 | The mind's causal role is to select the coarse-graining, setting the control parameters, without disturbing physical efficient causation | weak | asserted (pp. 3, 19); defended by the parameters' lack of a microscopic derivation (p. 19) |

## Concepts

- **IAT (Irruption-Absorption Theory)** — Froese 2024: a mind-to-matter
  difference shows in matter as an "unintelligible increase in measurable
  differences" (irruption), matter-to-mind as a decrease (absorption), in
  anticorrelated pairs (pp. 2, 5).
- **IAT*** — the author's modification: irruption in mind and brain go
  together, as do absorption in both; either can be cause or effect (p. 6,
  fn. 5).
- **Control parameters** — a, b (or k = b/a, Kelso's original control
  parameter, fn. 8), here made functions of time and attributed ultimately
  to the mind.
- **Neural variability quenching** — the drop in trial-to-trial
  variability after stimulus onset, which the paper aims to explain (p. 18).

## Connections

- **Haken, Kelso and Bunz 1985** ([LIT-588](../literature.d/LIT-588.md), [NOTE-1424](NOTE-1424.md), [THEORY-1227](../theory.d/THEORY-1227.md)) supply
  the potential; Schöner, Haken and Kelso 1986 its stochastic version
  (fn. 11).
- **Sánchez-Cañizares 2024** ([LIT-1132](../literature.d/LIT-1132.md), Unavailable) is the "proof of
  concept" this extends; the 2026 paper's novelty is the time-dependent
  parameters (p. 8). It quotes its Fig. 6 as a "cycle of relaxation,
  fixation of possibilities, and decision-making" (p. 10).
- **Froese 2023** ([LIT-tmp31f3t](../literature.d/LIT-tmp31f3t.md), [NOTE-tmpn7fkx](NOTE-tmpn7fkx.md)) and **Froese 2024**
  (*Entropy* 26:288, not held).
- **Hölken 2024** ([LIT-tmp8fjub](../literature.d/LIT-tmp8fjub.md)) is cited once, for the criticism that IT
  does not explain "how underdetermination arises in material systems and
  how the scaling-up of irruptions causally affects normative behavior"
  (fn. 6, p. 6). This 2026 paper does not answer it. It places the mind at
  the parameters instead of in microscopic noise, so it needs no scaling-up.
- **Juarrero 2023**, *Context Changes Everything* (open access, not held),
  is cited for "constraints' causality", which IAT "seems to initially
  reject" and which the author says "need not be the case" (fn. 7, p. 6).
  Kelso 1995 is cited for order parameters.
- **Kane is not cited**, and neither is chaos.

## Bearing on the record

- **[LIT-1132](../literature.d/LIT-1132.md).** Its status note expected this paper "may cover the same
  ground". It does not reproduce the 2024 paper. It extends it, with
  time-dependent parameters and a comparison with experiments, and it
  restates the 2024 result only in a sentence (p. 19): the HKB model "can
  instantiate some of IT's predictions". [LIT-1132](../literature.d/LIT-1132.md) stays unread.
- **What it concedes.** The registration says A22 "summarizes what it
  concedes"; A22's text is not in the record, so this reading lists the
  concessions in the paper's words, against which A22 can be checked:
  - IAT* is a restricted modelling assumption, not a revision of IAT
    (pp. 2, 20).
  - "IAT* cannot be tested with empirical results without further
    assumptions" (p. 7).
  - "The HKB model, as a scientific model, does not require the existence
    of IAT* to work" (p. 7).
  - The agreement with experiment is "only qualitative" (p. 18), with two
    stated mismatches.
  - Changes in a and b "are likely consequences of external parameters,
    like SNR, but they are also the effect of internal brain dynamics"
    (p. 15).
  - Making IAT* testable and not ad hoc needs "much more" (p. 20).
- **[CLAIM-tmpex9rg](../claims.d/CLAIM-tmpex9rg.md).** This is the irruption-theory reading A21 put first
  "for the chaos line", but it has no chaos in it. Its dynamics is a
  one-dimensional gradient flow, φ̇ = −∂V/∂φ, which cannot be chaotic, and
  its openness is bistability plus noise. On the claim's terms the agent
  has no input channel into φ at all. Its only channel is to the
  parameters a(t), b(t), that is, to the landscape. That is a different
  control architecture from the one the claim discusses: it controls which
  outcomes exist, not which one the state reaches. The paper does not ask
  how the choice between the two wells is made in the bistable interval.
  In its own simulation that is settled by the initial condition and noise
  (pp. 10–11), and the mind's contribution is to remove one well (b → 0).
  So the paper locates control exactly where [CLAIM-tmpex9rg](../claims.d/CLAIM-tmpex9rg.md) says it must
  be, in a channel to the slow structure, but without any account of whose
  input sets the parameters.
- **[CLAIM-478](../claims.d/CLAIM-478.md).** The model's control parameters are the slow structure that
  constrains the fast phase, the claim's scale separation, and the paper
  attributes setting them to the mind. Its fn. 12 appeals to critical
  fluctuations and slowing near transitions, which is [CLAIM-478](../claims.d/CLAIM-478.md)'s second
  half.
- **[QUESTION-071](../questions.d/QUESTION-071.md).** If what the mind does is set a(t), b(t), and those are
  also set by SNR and internal dynamics (p. 15), nothing in the measured
  dynamics tells a mind-set parameter change from one set by stimulus or by
  another party. The paper treats that as the black box's virtue (p. 20).
- **No instruction for machine-learning practice.**

## Limitations

- **Qualitative throughout.** No parameters are fitted, and the
  comparisons are by eye against figures reproduced from other papers.
- **The noise is underspecified**, and with the stated q = 1 the paper's
  description of Fig. 3 does not hold (above).
- **The statistics are over initial conditions**, which the author
  distinguishes from noise (fn. 13), but trial-to-trial variability in the
  experiments has no such clear counterpart.
- **The mental attribution is not tested and is said to be untestable** on
  its own: it rests on the absence of a microscopic derivation of a and b
  (p. 19), which is an argument from ignorance unless such a derivation is
  impossible.
- Schöner et al. 1986 and the four experimental papers were not checked
  here.

## Open questions

- Which noise produced Fig. 3, and does the variability-quenching match
  survive with noise strong enough to give realistic stationary
  variability?
- Can a(t), b(t) be estimated from data trial by trial, and does any
  variable other than stimulus and task predict them? That is the test the
  mental attribution would need ([THEORY-tmp1jrus](../theory.d/THEORY-tmp1jrus.md)).
