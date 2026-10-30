---
status: Read
paper: LIT-588
title: 'Haken, Kelso & Bunz — A theoretical model of phase transitions in human hand movements'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Read in full on 2026-10-30 from the copy on J. A. S. Kelso's lab page
    at Florida Atlantic University
    (https://ccs.fau.edu/hbblab/pdfs/1985_Haken_Kelso_Bunz_Biol_Cyb.pdf),
    an author's posting that counts under ADR-064. It is the publisher's
    scan with a text layer: header "Biol. Cybern. 51, 347–356 (1985)",
    Springer-Verlag 1985, received 17 November 1984, ten pages. Text
    extracted with pdftotext; the equations of §§2–3 were checked on the
    page images of pp. 351 and 353, where the text layer garbles them.
    Read: the abstract, all five sections, the footnotes, the figure
    captions and the references. The figures were not viewed; what they
    show is taken from their captions and the text. None of the cited
    experiments (Kelso 1981a, 1984) was read.
date: '2026-10-30'
summary: >-
  A theory paper. It takes relative phase as the order parameter of
  bimanual rhythmic movement and models the switch from anti-phase to
  in-phase at a critical frequency with φ̇ = −∂V/∂φ, V = −a cos φ − b cos 2φ,
  anti-phase being lost when |b| < |a|/4. It derives that equation from
  two self-sustained oscillators whose coupling must be nonlinear, and
  shows the switch and hysteresis in one simulation. The data it models
  are Kelso's earlier experiments, summarized, and critical fluctuations
  and slowing are left to future work.
---
<!-- inactive-ok-file: THEORY-069 — Proposed; the account this reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-578 — Unavailable; Kelso's book, named, not leaned on -->

# NOTE-tmp0jngz: Haken, Kelso & Bunz — A theoretical model of phase transitions in human hand movements

## Contribution

It gave Kelso's observation of an involuntary switch between bimanual
patterns a dynamical model at two levels. At the top, one variable,
relative phase, moves in a potential whose shape changes with movement
frequency. Beneath it, two coupled limit-cycle oscillators, one per hand,
from which that equation is derived. After it, the switch was a
bifurcation with testable consequences, and the paper names them
(critical slowing, critical fluctuations) for later work.

## Key insight

Two patterns of coordination are two minima of one potential in relative
phase. As frequency rises and amplitude falls, the anti-phase minimum
flattens and vanishes, and the system falls into in-phase. Lowering the
frequency restores the minimum but not the occupancy, so the system stays
in-phase. Which pattern is seen is decided by the shape of the landscape
and where the system started, not by a controller choosing one.

## Assumptions

- **Phase is the order parameter.** Defended on two grounds: it reflects
  the cooperation of the components, and it stays invariant across
  scalar changes in rate or force in many motor activities (p. 349). It
  is also assumed to change much more slowly than the components'
  variables, the slaving condition of synergetics.
- **Near-harmonic motion.** x_j = r_j cos(ωt + φ_j), with amplitudes and
  phases varying slowly against ω (Eqs. 2.1–2.2).
- **Periodicity and symmetry.** V(φ + 2π) = V(φ) and V(φ) = V(−φ), the
  hands playing symmetric roles (Eqs. 2.5–2.6; footnote 5 allows
  asymmetry).
- **Amplitude carries the control.** b is tied to the movement amplitude
  r, which falls as frequency rises, so b/a falls (Eq. 2.18).
- **Approximations in §3.** The slowly varying amplitude and rotating wave
  approximations, equal and stable amplitudes r₁ = r₂, and (for
  convenience) γ ≪ ω.
- **Noise.** A transition from φ = π to φ = 0 "can be initiated only if
  fluctuating forces ... are present" (p. 353); the source of the noise is
  left open.

## Key results

- **The data modelled (§2, p. 348).** Kelso's experiments (1981a, 1984)
  show "(i) the presence of only two stable phase (or 'attractor') states
  between the hands ...; (ii) the abrupt transition from one attractor
  state to the other at a critical cycling frequency; (iii) beyond the
  transition, only one mode (symmetrical in-phase) is observed; and
  (iv) when cycling frequency is reduced, the system stays in the
  symmetrical mode". The transition frequency in units of each subject's
  preferred frequency was "constant for all subjects", and friction
  changed both frequencies but not their ratio (p. 347). Fig. 1 shows one
  run. These are reported, not shown.
- **The order-parameter equation (§2).** φ̇ = −∂V/∂φ (2.4) with
  V = −a cos φ − b cos 2φ (2.7). Extrema at φ = 0, ±π, and at
  cos φ = −a/4b (2.15), the inner maxima. Bistable while |b| > |a|/4,
  monostable (in-phase only) when |b| < |a|/4 (2.16–2.17, 3.22). Fig. 5
  plots V/a for a series of values of b/a.
- **Hysteresis is a consequence.** "When we decrease ω starting from high
  values, the system remains all the time in the φ = 0 state even if ω
  drops below ω_c. This 'hysteresis' phenomenon is well known" (p. 350).
- **Component oscillators (§3).** Each hand obeys
  ẍ + ε(ẋ² − ω₀²r₀²)ẋ + ax = 0 (3.6), whose amplitude falls as
  ω₀r₀/(√3 ω) (3.8). A linear coupling does not give the required
  potential; a nonlinear coupling of the same symmetry still "does not
  produce the correct phase relation"; the coupling must involve a time
  delay (3.11b) or time derivatives (3.25). With the derivative coupling
  K₁₂ = (ẋ₁ − ẋ₂)(α + β(x₁ − x₂)²) the phase equation is
  φ̇ = (α + 2βr²) sin φ − βr² sin 2φ (3.26), with critical amplitude
  r_c² = α/4β (3.27).
- **Simulation (§4).** Eq. (3.6) with coupling (3.25) and small noise,
  ω swept from 1.17 to 3.05, switches from out-of-phase to in-phase when
  ω exceeds a critical value (Fig. 6); "the exact form of the curves
  depends strongly on the noise level and the rate of changing ω". Fig. 7
  gives both modes' steady amplitudes against ω, the out-of-phase branch
  unstable above ω_c.
- **What is left for later (p. 355).** "In future studies a number of
  phenomena known to accompany phase transition in synergetic systems
  (e.g., critical slowing down; critical fluctuations) will also be
  analyzed." And: "it remains for further theoretical and experimental
  research to address how it is that only two stable modes emerge in the
  first place".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bimanual rhythmic movement has two stable phase relations and switches abruptly from anti-phase to in-phase at a critical frequency, with hysteresis | moderate, as reported | Kelso 1981a and 1984, summarized on pp. 347–348; one run shown (Fig. 1); no data in this paper |
| C2 | Relative phase is an order parameter for these patterns | moderate | argued from invariance and cooperativity (p. 349); fits the four features |
| C3 | V = −a cos φ − b cos 2φ is the simplest potential reproducing the features | strong, as mathematics | periodicity and symmetry plus the observed layout; §2 |
| C4 | The φ equation follows from two self-sustained oscillators only if their coupling is nonlinear and involves delay or derivatives | moderate | derivation under the stated approximations, §3; "in all likelihood the choice of f₁ and f₂ is not unique" (p. 351) |
| C5 | The transition occurs at a critical frequency via the amplitudes | weak; a prediction | Eqs. 3.24, 3.27; stated as "now open to further experimental test" (p. 355) |
| C6 | The neural coupling for voluntary bimanual movement may be subcortical | speculation | split-brain patients' bias toward synchrony or alternation (Tuller and Kelso 1984, a conference paper) |
| C7 | Nonlinearity gives a stable amplitude–frequency coupling and a means of switching, hence "stability and flexibility of motor function" | asserted | hypothesis, p. 355 |

## Method

Synergetics' strategy: identify an order parameter where behaviour changes
qualitatively, write the simplest potential consistent with the observed
attractor layout and its symmetries, then derive that order-parameter
equation from equations for the components and their coupling, and check
the whole by numerical simulation (fourth-order Runge–Kutta with small
random fluctuations).

## Concepts

- **Order parameter** — a macroscopic variable "created by the
  cooperation of the individual components" which "in turn governs the
  behavior of these components", and which changes much more slowly than
  they do (pp. 348–349).
- **Phase** — used in two senses, warned of in footnote 3: a temporal
  relation between the hands, and a state of aggregation, as in "phase
  transition"; here the transition is between behavioural modes defined
  by the first sense.
- **Control parameter** — movement frequency ω, entering through the
  coefficient a of the restoring force and, via amplitude, through b/a.
- **Hysteresis** — staying in the in-phase state when ω is lowered back
  below ω_c, from the coexistence of two basins of attraction.

## Connections

It applies Haken's synergetics (laser theory, the slaving principle) to
Kelso's bimanual experiments, and compares the switch with gait
transitions in the decerebrate cat (Shik et al. 1966) and Grillner's
"switch mechanism". Its noise term is the opening that Schöner, Haken and
Kelso's 1986 stochastic theory (Biological Cybernetics 53:247, not filed)
fills, and the critical fluctuations it promises are reported in Kelso,
Scholz and Schöner 1986 (LIT-tmp8grr0, NOTE-tmpegx3g). Kelso's 2021
retrospective (LIT-601, NOTE-467) restates this model as the "top tier"
above the coupled components, and *Dynamic Patterns* (LIT-578) is the
book-length treatment.

## Bearing on the record

- **THEORY-069: partly.** The paper is the model's original statement,
  and it confirms THEORY-069's equations, the b/a = 1/4 threshold, the
  direction of the switch (anti-phase to in-phase as frequency rises),
  and the derivation from coupled oscillators. It also states hysteresis
  as an observed feature of Kelso's experiments (p. 348) and derives it,
  which corrects THEORY-069's line that "the read text does not report
  the hysteresis data": this text reports it, though it does not show the
  data. It does not meet the condition that matters most in the
  `promote_when`: it reports neither critical fluctuations nor critical
  slowing, naming both as future work (p. 355). The 1985 paper is a
  theory paper; for first-hand data see NOTE-tmpegx3g and NOTE-tmpswmu1.
- **THEORY-069's `promote_when` names Schöner, Haken and Kelso (1986).**
  That is the stochastic theory in Biological Cybernetics 53:247, still
  not filed and not read. It is a different paper from Kelso, Scholz and
  Schöner's Physics Letters A report of the same year (LIT-tmp8grr0).
- **LIT-601 and NOTE-467.** Kelso's 2021 account of this paper is
  faithful on the model. One small difference: he speaks of hybrid
  oscillators; this paper uses a Van der Pol variant (Eq. 3.6) and a
  superposition with a Van der Pol term (Eq. 3.9), and notes the choice
  "is not unique".
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **No new data.** Every empirical feature is summarized from Kelso's
  earlier work, two of whose sources are a one-page abstract (1981a) and
  an invited talk (1982). How many subjects showed hysteresis, and how it
  was tested, is not given here.
- **Model choice.** The potential is the simplest that fits, and the
  oscillator and coupling forms were chosen among several; the authors
  say the choice is not unique. The simulation reaches no stationary
  oscillation, so its curves depend on noise level and sweep rate.
- **Amplitude as mediator.** Tying b to amplitude predicts that the
  transition happens at a critical amplitude; the paper offers this as a
  test, not a result.
- **Physiology.** The authors say the physiological basis of the
  nonlinearities is "an open issue"; the subcortical coupling is
  speculation.

## Open questions

- Do critical fluctuations and critical slowing precede the switch, as
  the synergetic analogy predicts? (Fluctuations: LIT-tmp8grr0.
  Relaxation time: Scholz, Kelso and Schöner 1987, not filed.)
- Is the transition reached at a critical amplitude, as Eqs. 3.24 and
  3.27 imply?
- Why only two stable modes "emerge in the first place from a wealth of
  possibilities" (p. 355)?
