---
number: 445
status: Read
formerly:
- NOTE-tmp2cxrv
paper: LIT-576
title: 'The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the PMC author manuscript (PMC2474742): §§1–11,
    Tables 1–2, footnote 1 and all figure captions. Figures were read from
    captions and text; plotted quantiles were not read off. The version of
    record was not seen. The applications in §§8–10 (aging, aphasia,
    superior colliculus recordings, dual diffusion) are the authors'
    summaries of their own earlier papers, taken as stated.
date: '2026-10-03'
summary: >-
  The full diffusion model (drift v with across-trial SD η, boundaries 0
  and a, starting point z with range s_z, non-decision time Ter with range
  s_t) fitted by the χ² quantile method. In three dot-motion experiments
  with 14–17 participants difficulty maps to drift alone, speed–accuracy
  instructions to boundaries alone, and a 75:25 proportion mainly to
  starting point; RT distribution shape is invariant across conditions.
  Drift variability gives slow errors and starting-point variability fast
  ones. Reviews aging, aphasia and neural-firing applications.
---
<!-- inactive-ok-file: THEORY-061 — Proposed; named as the theory that rests on this model, nothing here rests on it -->

# NOTE-445: The Diffusion Decision Model: Theory and Data for Two-Choice Decision Tasks

## Contribution

A review that states the diffusion model completely, explains how each
parameter shapes accuracy and the correct and error RT distributions, and
illustrates the three canonical manipulations on new human data from the
motion-discrimination task used in monkey neurophysiology. It then surveys the
model as a measurement tool: individual differences, aging, aphasia, coupling
to encoding models, and the mapping to neural firing rates.

## Key insight

Two-choice behaviour carries more information than mean RT and accuracy: the
full shape of the correct and error RT distributions. A noisy accumulator
between two boundaries predicts that shape from geometry alone. Its
parameters therefore act as a decomposition of performance into evidence
quality, caution, bias and non-decision time. It can be falsified, because
each manipulation has to land on one parameter, and the shape of the
distributions must stay the same across conditions while their location and
spread change.

## Assumptions

- **Scope** (§2): fast two-choice decisions (mean RT under about 1,000–1,500
  ms) made in a single stage, not reasoning tasks.
- **Process** (§2): evidence starts at z and accumulates with drift v and
  within-trial SD s (a scaling parameter) until it reaches 0 or a. Drift is
  constant within a trial.
- **Across-trial variability** (§2): drift ~ Normal(v, η); starting point
  uniform with range s_z; non-decision time uniform with mean Ter and range
  s_t. Boundary variability is assumed to be absorbed by starting-point
  variability.
- **Contaminants** (§2.6): a proportion p_o of uniform contaminant responses
  is modelled, after cutting short and long outliers (usually 2–3%).
- **Fitting** (§2.6): χ² over the proportions between the .1, .3, .5, .7 and
  .9 quantiles of correct and error RTs, minimised by SIMPLEX. In this
  paper fits are to data averaged over participants.

## Key results

- **Distribution geometry (§2.1).** Lowering drift slows the .9 quantile
  about four times as much as the .1. Narrowing boundaries changes both,
  in roughly a 2:1 ratio, and trades speed for accuracy.
- **Bias, two ways (§2.2).** Moving the starting point shifts both the
  leading edge and the tail. Moving the drift criterion (the zero point of
  drift) changes mainly the tail, which is the analogue of moving the
  criterion in signal detection theory.
- **Correct versus error RTs (§2.3).** Across-trial drift variability makes
  errors slower than correct responses; starting-point variability makes them
  faster; together they cover the observed crossovers (Ratcliff & Rouder
  1998; Ratcliff et al. 1999).
- **Experiment 1** (15 participants, six coherences from 5% to 50%). Accuracy
  ran from .58 to .94 and mean RT from about 660 to 550 ms. Only drift varied
  across conditions (0.042 to 0.369; Table 2). The tails spread by up to 300
  ms and the leading edge by under 40 ms. Quantile–quantile plots were nearly
  linear: the shape of the distribution was invariant.
- **Experiment 2** (14 participants, speed versus accuracy instructions).
  Instructions changed accuracy by 0–6% but median RT by 120–200 ms, the .1
  quantile by 40–100 ms and the .9 by 250–550 ms. All of it was fitted by
  boundary separation alone (a = 0.109 vs 0.152). Separate Ter values for the
  two instructions differed by 6 ms and were dropped.
- **Experiment 3** (17 participants, 75:25 left–right proportions). The
  starting point moved to about a third of the boundary distance toward the
  likelier response and accounted for most of the effect. Letting the drift
  criterion vary improved χ² by only 1%. There were systematic misses on the
  .9 quantiles for errors.
- **Human versus monkey distributions (§4).** Human RT distributions in this
  task were right-skewed with roughly exponential tails, unlike the nearly
  symmetric distributions of Roitman and Shadlen's monkeys that motivated
  Ditterich's model with time-varying drift.
- **Drift and coherence (§4.4.1).** Drift is nearly linear in coherence, with
  a slight bend toward 50%, which supports Palmer et al.'s linear assumption
  without requiring it a priori.
- **Response signal and go/no-go (§5).** These are accounted for with implicit
  boundaries. The boundary-free version fails on response-signal data fitted
  jointly with standard RT data.
- **Individual differences (§8).** Across 18 data sets of 30–40 participants
  each, accuracy correlated with drift and mean RT with boundary separation,
  and drift and boundary separation were uncorrelated. Across four tasks,
  individuals' boundaries (r = .32), Ter (r = .47) and drift (r = .37)
  correlated. Older adults' slowing is mostly conservative boundaries; drift is
  mostly not worse. Aphasic patients set wider boundaries and have longer Ter,
  with small drift deficits.
- **Neural correlates (§10).** In superior colliculus buildup cells (Ratcliff,
  Cherian et al. 2003) the average simulated path matched the average firing
  rate, including the time shifts between fast, middle and slow thirds of
  responses, which the noise predicts. A dual diffusion model, with leaky
  accumulators per alternative as in Usher and McClelland, fits the two cell
  types separately. Wong and Wang's spiking model reduces to two units with
  self-excitation and mutual inhibition.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Difficulty maps to drift, speed–accuracy instructions to boundary separation, and stimulus proportion mainly to starting point | moderate to strong for these experiments; fits are to group-averaged data | Exps. 1–3, Tables 1–2 |
| C2 | RT distribution shape is invariant across conditions, and the model predicts it | moderate | Q–Q plots, Fig. 8; earlier unpublished analyses cited |
| C3 | Across-trial drift and starting-point variability jointly explain slow and fast errors | strong (cited) | §2.3, Ratcliff & Rouder 1998, Ratcliff et al. 1999 |
| C4 | Older adults' slowing is mostly caution, not poorer evidence | moderate, from the authors' own earlier studies | §8.2.1 |
| C5 | Averaged diffusion paths track superior colliculus firing rates | moderate (one study, aggregated cells) | §10 |
| C6 | Likelihood-ratio decision models are implausible for humans who calibrate from verbal instruction in one trial | argument, not test | §7.1 |
| C7 | Diffusion models are "as near to" a solution to simple decision making as behavioural science allows | assertion | §11 |

## Concepts

- **drift rate (v)**: the quality of evidence from the stimulus, positive
  toward one boundary.
- **drift criterion**: the zero point dividing positive from negative drift,
  analogous to the criterion of signal detection theory.
- **boundary separation (a)**: the evidence required for a response; caution.
- **Ter**: mean duration of all non-decision components (encoding u plus
  response output w).
- **quantile probability plot**: RT quantiles of correct and error responses
  plotted against response proportion, for every condition at once.

## Connections

- **Usher & McClelland 2001 ([LIT-565](../literature.d/LIT-565.md)).** Placed in the accumulator
  subclass. It and Bogacz et al. are cited as "more recent accumulator models"
  that "may be as successful as" the single-process model, but have been
  tested on fewer paradigms (§6). §7.1 adds that for leaky models such as the
  LCA it is unclear whether likelihood-based and distance-from-criterion
  accounts coincide.
- **Bogacz et al. 2006 ([LIT-569](../literature.d/LIT-569.md)).** Cited for criterion-setting
  proposals that, the authors say, cannot explain calibration from verbal
  instruction or without feedback (§7.1). Bogacz et al. also fit the
  extended model to RT quantiles and error rates, but by weighted least
  squares rather than χ².
- **Wiecki, Sofer & Frank 2013 ([LIT-563](../literature.d/LIT-563.md)).** Implements this model, with
  the same across-trial variability parameters, in hierarchical Bayesian form.
  It replaces the group-averaged χ² fits used here with partial pooling.
- **Schurger et al. 2012 ([LIT-605](../literature.d/LIT-605.md)).** Uses the linear mean–SD relation of
  first-passage times, a property of drift-diffusion, as a check on its own
  leaky accumulator.

## Bearing on the record

- The model says what an evidence-accumulation decision is, with parameters
  that dissociate. That makes it the measurement backbone for any THEORY the
  record might hold about deliberation, caution or bias; [THEORY-061](../theory.d/THEORY-061.md) is
  the first to rest on it.
- **No ML instruction.** Nothing here belongs in the anthology.

## Limitations

- **Group-averaged fits.** The authors report that individual and averaged
  parameter values were within 2 SEs "with only one or two exceptions", and
  that χ² values here are not interpretable in the standard way.
- **Scope.** The model applies only to fast single-stage two-choice decisions.
  It is silent on how criteria are set (§7.1), which the authors attribute to
  decision history.
- **Variability parameters are poorly estimated** (§4.4); η and s_z depend on
  the relatively few error RTs.
- **Neural evidence** relies on aggregated firing rates and on difference
  between cell types, not single cells, for the single-process model.

## Open questions

- How do people set and calibrate boundaries from instructions alone?
- How does encoding produce drift, for coherence and other stimuli? The model
  is offered as the meeting point where such encoding models can be tested.
- Can likelihood-based models be distinguished from distance-from-criterion
  models for leaky or dual-diffusion processes (§7.1)?

## Corrections

- none to a seeded skim (there was no seed)
