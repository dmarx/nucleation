---
status: Read
paper: LIT-tmpzrigj
title: 'An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from PMC3479453: every section, the figure captions,
    Equation 1 (read from the PMC equation image) and the reference list.
    The supporting information, Figs. S1–S5, was not read. Figures were
    read from their captions and the text.
date: '2026-10-03'
summary: >-
  A three-parameter leaky stochastic accumulator, δx = (I − kx)Δt + cξ√Δt,
  fitted to Libet-task waiting times (k = 0.5, I = 0.11, threshold at the
  80th percentile of output), reproduces the readiness potential (r² = 0.96)
  and the linear mean–SD relation of waiting times (r = 0.9). In a variant
  with random clicks, fast responders showed a slow negativity before the
  click (P < 0.005), and fast and slow clicks were spread equally through
  the trial (P = 0.64). The neural decision to move is placed at the
  threshold crossing about 150 ms before movement.
---
<!-- inactive-ok-file: THEORY-tmp1gn9c THEORY-tmp2002z — Proposed; named as the THEORY documents filed for this note's candidates, nothing here rests on them -->

<!-- inactive-ok-file: THEORY-029 — Proposed; named to say this reading does not bear on it -->
<!-- inactive-ok-file: THEORY-040 — Proposed; named to say this reading does not bear on it -->

# NOTE-tmpqbs2w: An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement

## Contribution

A mechanistic account of the readiness potential (RP): a decision threshold
applied to autocorrelated noise, here the output of a leaky stochastic
accumulator. The account fits the RP's shape from behavioural parameters
alone, and its prediction, verified in a new "Libetus interruptus"
experiment, is that speeded responses to unpredictable cues are preceded by a
slow negativity when they are fast.

## Key insight

Average enough noise traces aligned to the moment each crossed a threshold,
and the average rises smoothly toward the threshold, even though no
individual trace was "building up" toward anything. Movement-locked averaging
is a backward selection: only epochs ending in a movement are analysed. So an
RP is what one should see if, as in a decision-making task, the decision to
move is a threshold crossing, and in an uncued task the accumulator's input is
mostly spontaneous fluctuation. What the experimenter calls planning may be
the trace of noise that happened to cross.

## Assumptions

- **Same machinery as perceptual decisions** (section "The Stochastic-Decision
  Model"): an accumulator plus threshold, fed in this task with internal noise
  instead of evidence, because the instructions forbid basing the decision on
  evidence.
- **Model (Eq. 1)**: δx_i = (I − kx_i)Δt + cξ_i√Δt, with c = 0.1 and Δt =
  0.001. I is a constant urgency from the task's demand characteristics; k is
  leak; ξ is Gaussian noise. With leak, urgency raises the baseline toward the
  threshold rather than ramping to it.
- **Threshold** expressed as a percentile of output amplitude over 1,000
  simulated trials of 50,000 steps. Fitted values k = 0.5, I = 0.11, β = 0.298
  (80th percentile).
- **Independent trials and a reset to zero** after each crossing; no memory
  between trials.
- **The fit window** ends at −150 ms, the time of maximum slope of the
  lateralised RP, taken as the end of the pre-commitment phase. Activity after
  it is attributed to motor execution.
- **Interrupted responses** are assumed to come from the same accumulator as
  self-initiated ones (citing Hughes et al.). A click is simulated as a steep
  linear ramp added at the interruption.

## Key results

- **Classic Libet task** (16 recruited; 2 excluded for no RP at any electrode;
  14 for EEG). The mean reported urge was 152 ms before movement (±33 ms
  SEM), consistent with earlier reports. Normalised waiting-time distributions
  were broad and right-skewed, fitted "excellent[ly]" (Fig. 1B).
- **RP from behaviour** (Fig. 1C). With the waiting-time parameters, the
  sign-reversed average of simulated traces fitted the RP from −3 to −0.15 s
  (r² = 0.96, P < 10⁻⁹). Nearby parameters fitted worse (Fig. S1, not read).
  The fit was about as good with the window ending at −200 or −100 ms.
- **Mean–SD relation** (Fig. 2). Mean and SD of waiting times were linearly
  related across participants (r = 0.9, P < 0.00001), as for first-passage
  times of drift-diffusion processes (Wagenmakers & Brown 2007) and for the
  model.
- **Libetus interruptus** (13 participants; 150 trials). Adding random clicks
  left the RP on uninterrupted trials unchanged in the data and the model
  (Fig. 3). Responses to clicks, split into fastest and slowest thirds: fast
  responses were preceded by a more negative potential, over −0.8 to −0.3 s
  before movement and over 0.5 s before the click (both P < 0.005, two-sided
  signed-rank; Fig. 4). The simulation predicted the same (Fig. 4 E–F). Pre-
  click times of fast and slow responses were distributed equally across the
  trial (P = 0.64, n = 13), which excludes a slowly building general
  readiness (CNV). "Coincidence" trials (4%) were excluded.
- **Residual misfits.** Waiting times on successive trials were positively
  correlated, and participants preferred the "bottom" of the clock (Figs.
  S3–S4). Some participants moved earlier when clicks were possible.
- **Reinterpretation** (Discussion). The RP has two nonlinear components, a
  pre-commitment phase dominated by fluctuations and a post-commitment motor
  phase in the last ~150 ms. The neural decision to move is the threshold
  crossing, together with the lateralised RP and an abrupt rise in
  corticospinal excitability. Its time coincides with the reported urge, so
  the brain's estimate of its own decision time is "reasonably accurate", and
  there is no special gap for motor decisions as compared with sensory ones.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A leaky accumulator fed with noise and weak urgency, fitted to waiting times alone, reproduces the RP's shape | moderate to strong: three parameters, behaviour-only fit, r² = 0.96 | Fig. 1 |
| C2 | Fast responses to unpredictable cues are preceded by a slow negativity, as the model predicts and the planning account does not | moderate: n = 13, one experiment, P < 0.005 | Fig. 4 |
| C3 | The neural decision to move occurs about 150 ms before movement, not at RP onset | interpretive: follows within the model; the authors say the data show the RP "could" be spontaneous activity, not that it is | Discussion |
| C4 | Libet's conclusion that the neural decision precedes awareness by half a second or more is unfounded | moderate as a rebuttal of an inference; it does not establish the reverse | Discussion |
| C5 | The same bounded-integration mechanism serves perceptual and spontaneous decisions | weak to moderate: the mean–SD relation is consistent with it but shared by many processes | Fig. 2 |
| C6 | Conserved 1/f autocorrelation explains why crayfish and humans show similar premovement buildup | speculation | Discussion |

## Concepts

- **readiness potential (RP, Bereitschaftspotential)**: the slow negative EEG
  deflection preceding self-initiated movement in the movement-locked average
  (Kornhuber & Deecke 1965).
- **neural decision to move now**: the threshold crossing that commits to a
  movement, distinct from the conscious decision and from RP onset. Likened to
  tipping the first domino: ballistic, not deterministic, since a veto can
  still intervene.
- **waiting time (WT)**: time from trial start to the spontaneous movement.
- **urgency**: the constant input I, from the task's implicit demand to move
  within about 20 s.
- **backward selection bias**: only epochs ending in a movement are averaged,
  so the fluctuations that produced the crossing are recovered.

## Connections

- **Usher & McClelland 2001 ([LIT-tmp2p2lh](../literature.d/LIT-tmp2p2lh.md)).** The source of the model (their
  ref. 27), here a single accumulator with no competitor. The paper calls it
  "a well-known accumulator model (DDM)… an extension of an earlier model
  developed by Ratcliff". With leak it is strictly an Ornstein–Uhlenbeck
  process, not a pure diffusion.
- **Bogacz et al. 2006 ([LIT-tmp93b13](../literature.d/LIT-tmp93b13.md)).** In their terms this is a stable O-U
  process, with an attractor at I/k below the threshold. My mapping; neither
  paper draws it.
- **Ratcliff & McKoon 2008 ([LIT-tmpcmcw7](../literature.d/LIT-tmpcmcw7.md)).** The perceptual-decision
  framework the paper borrows: commitment as a threshold crossing.
- **Dennett & Kinsbourne 1992 ([LIT-431](../literature.d/LIT-431.md), [NOTE-367](NOTE-367.md)).** Both papers deny that
  Libet showed an unconscious decision preceding a conscious one. Dennett and
  Kinsbourne argue from the timing of represented content and treat the clock
  report as an artefact; Schurger et al. argue from the mechanism of the RP and
  accept the clock report as an approximate estimate of the time of
  commitment. They are compatible, but they are not the same argument, and
  they disagree on how far the urge report can be trusted.

## Bearing on the record

- **Agency and free will.** It removes an empirical premise, not a
  philosophical position. [THEORY-029](../theory.d/THEORY-029.md) and [THEORY-040](../theory.d/THEORY-040.md) do not rely on Libet, so it
  does not bear on them. It is the record's evidence that the RP does not
  establish a neural decision before awareness, and [THEORY-tmp1gn9c](../theory.d/THEORY-tmp1gn9c.md) states
  that claim.
- **Behavioral integration.** It extends the evidence-accumulation account of
  decision from choosing *which* to choosing *when*, with goals acting by
  moving a baseline rather than by issuing a command. That THEORY is filed as
  [THEORY-tmp2002z](../theory.d/THEORY-tmp2002z.md).
- **No ML instruction.** The brain–computer-interface remark (the RP's limits
  as a self-paced BCI trigger) is a prediction about neural data, not an ML
  practice. Nothing here belongs in the anthology.

## Limitations

- **Possibility, not proof.** "Although our study demonstrates that the
  readiness potential could reflect non–goal-directed (spontaneous) neural
  activity, it does not prove that this possibility is in fact the case."
- **Narrow task.** One movement per trial, spontaneous timing, no reason to
  move at a particular time; deliberate choices with stakes are not tested.
- **Small samples.** 14 and 13 participants for EEG; electrode chosen per
  participant from the classic task.
- **Model limits.** No inter-trial memory although waiting times were
  serially correlated; history cannot extend before trial start, so the early
  simulated RP is noisy.
- **Silent on the urge.** The model does not say what the conscious urge is or
  whether it plays a causal role.

## Open questions

- Does the account carry over to deliberate decisions with consequences, or to
  the Kornhuber–Deecke self-paced task with time estimation?
- What sets the urgency and the baseline, and could slow fluctuations of the
  threshold explain the trial-to-trial correlation?
- Is the reported urge time a readout of the threshold crossing, as the
  authors propose, and how would one test that independently of the clock
  method?

## Corrections

- none to a seeded skim (there was no seed)
