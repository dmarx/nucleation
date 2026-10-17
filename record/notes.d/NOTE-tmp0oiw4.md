---
status: Read
paper: LIT-tmpsdb4n
title: 'Giarrocco & Averbeck — sensory and choice information flow between A1 and PFC'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the publisher's open-access PDF (Nature
    Communications 17:8443, 13 pages, CC BY-NC-ND), fetched from
    nature.com/articles/s41467-026-75349-2.pdf on 2026-10-16 and
    extracted with pdftotext, page by page. Read: abstract, introduction,
    Results (all five sections), Discussion, Methods (task, recordings,
    PCA, regression, decoding, the information-flow analysis with its
    equations), the data and code statements and the end matter; figure
    captions read, figures not seen as images. The reference list was
    scanned. The Supplementary Information (Supplementary Figs. 1–3) and
    the peer review file were not read. Page numbers are the article's.
    Quotations are verbatim from the extraction, with the "fl" and "fi"
    ligatures written out and
    citation superscripts omitted.
date: '2026-10-16'
summary: >-
  In 37 sessions of simultaneous recordings from A1 and dorsolateral PFC
  of two macaques reporting by bar release whether two tones came from
  the same side, cue-side information flowed A1 to PFC only (onset
  120–147 ms), while choice information (release or hold) flowed first
  PFC to A1 (onset 315–365 ms after target) and then A1 to PFC (352–419
  ms), both peaking near 500 ms, close to the bar release. The flow
  measure is a lagged regression on one-dimensional projections, so the
  result is correlational, within a trial, and does not separate the
  decision from the motor response.
---

# NOTE-tmp0oiw4: Giarrocco & Averbeck — sensory and choice information flow between A1 and PFC

## Contribution

The paper measures the direction and timing of information transfer
between primary auditory cortex (A1) and dorsolateral prefrontal cortex
(PFC, area 46/8Ad) from simultaneously recorded ensembles, separately for
a sensory variable (cue side) and for the monkey's choice. Earlier work
had shown choice-related activity in auditory cortex and in PFC, and
reciprocal anatomy, but not the direction of task-variable flow between
them in a primate auditory task. After it there is a within-trial
measurement that sensory information goes one way and choice information
goes both ways, PFC first. It reanalyses a subset of the dataset of
Napoli et al. 2021 (its ref. 30).

## Key insight

Within a single trial, the variable that predicts the animal's report
appears first in PFC, is then predictable in A1 from PFC's past, and is
then predictable in PFC from A1's past, while the cue's location is
predictable in PFC from A1 but never the reverse. The paper reads this as
a recurrent sensory–prefrontal loop during decision, "first from PFC to
A1, and crucially back from A1 to PFC" (abstract, p. 1). What it measures
is the predictability of one area's residual activity along a task axis
from the other's lagged residual activity on the same trial.

## Assumptions

- **Task and report (pp. 2, 9).** Two male rhesus monkeys, head-fixed,
  fixating, holding a bar. A 50 ms 4 kHz cue from the left or right
  speaker; after 1000, 1300 or 1800 ms a 300 ms 1 kHz target from the
  same side (match) or the other (non-match), under 40 dB white noise.
  Match: release the bar within 700 ms. Non-match: keep holding; a third
  stimulus on the cue side follows after 800 or 1000 ms and must then be
  released to. "Releasing the bar after the target in non-match trials
  was considered an error" (p. 9). So the reported choice is a manual act,
  release versus hold, and the reward probability is equal across the two.
- **Cue side was blocked.** "Initial cue location was blocked, meaning
  that left-cue and right-cue trials were presented in separate blocks"
  (p. 9). Pre-cue cue-side decoding was at baseline, about 0.5 (p. 5), so
  the blocking did not show up as an anticipatory signal.
- **"Choice" is the report, not the stimulus category.** Choice decoding
  "included correct and error trials, so reflects actual choice, not just
  the cue x target interaction" (p. 5). With accuracy around 80% (p. 2),
  choice and match/non-match agree on most trials.
- **Units.** Single- and multi-unit activity pooled "as their response
  patterns were similar" (p. 10); about 15.5 A1 and 16.9 PFC neurons per
  session (p. 2). A1 recordings had "minor coverage of adjacent belt
  territories" (p. 10).
- **The flow model (p. 11), a multivariate Granger causality "done in the
  time domain".** Per session and area, a regression of each neuron's
  50 ms-binned rate on the task variable; the coefficient vector at the
  bin of largest magnitude is taken as a 1D task axis; single-trial
  activity is projected on it; an AR(1) model within each area removes
  autocorrelation; then the target area's residual at t is regressed on
  1–4 lagged residuals of the source area, ε_{a1,t} = Σ_{i=1..4}
  β_{a2(t−i)} ε_{a2(t−i)}. R² over time against a 500 ms pre-stimulus
  baseline gives onset (first significant bin, leave-one-session-out) and
  peak.
- **No causal manipulation; other areas unrecorded.** "the correlational
  nature of our data precludes direct causal inference" (p. 9). Parietal
  cortex, thalamus and basal ganglia were not recorded (p. 9).

## Key results

- **Behaviour (p. 2).** Accuracy around 80% or above. Response time after
  the target on match trials 564 ms (SEM 10) for monkey 1 and 601.4 ms
  (SEM 25.1) for monkey 2; after the second target on non-match trials
  314.7 and 251.1 ms. 1199 neurons over 37 sessions (M1: 12 sessions, PFC
  160, A1 215; M2: 25 sessions, PFC 465, A1 359).
- **Errors are in the comparison, not the cue (p. 3).** Cue selectivity
  in the 150 ms after cue onset did not differ between correct and error
  trials (e.g. M1 A1 0.103 vs 0.110, t(214) = 0.75, p = 0.457). Target
  selectivity at 500–1000 ms did (M1 A1 0.224 vs −0.09, t(214) = 9.03,
  p = 1.03 × 10⁻¹⁶). "behavioral errors primarily reflect a failure in
  evaluating and comparing the target stimulus rather than improper cue
  processing" (p. 3). False match reports separate from other conditions
  earlier in A1 than in PFC (p. 4–5); misses are "neurally
  indistinguishable from correct holding" (p. 4).
- **Decoding (p. 5).** Cue side, peak accuracy A1 0.826 vs PFC 0.698 (M1),
  0.748 vs 0.603 (M2); onset A1 25 ms vs PFC 70.83 ms (M1), 25 vs 87 ms
  (M2). Choice, peak A1 0.79 vs PFC 0.69 (M1), 0.75 vs 0.66 (M2); onset
  PFC 91.66 ms vs A1 193.75 ms (M1), PFC 163 vs A1 177 ms (M2;
  t(24) = 4.8, p = 6.87 × 10⁻⁵).
- **Cue flow (p. 6).** "a transient peak of cue-related information flow
  from A1 to PFC shortly after cue onset, whereas information flow from
  PFC to A1 was absent". Onset 119.80 ms (M1) and 146.5 ms (M2); peak
  133.33 and 137 ms.
- **Choice flow (pp. 6–7).** "choice-related information was
  bidirectionally transferred between the two areas". Onset PFC to A1
  365 ± 4.65 ms (M1) and 315 ± 2.89 ms (M2) after target onset; A1 to PFC
  418.75 ± 7.61 and 352 ± 3.93 ms (paired t: M1 t(11) = 5.91, M2
  t(24) = 7.44, both p < 0.001). Peaks did not differ by direction: PFC to
  A1 503.12 and 507 ms, A1 to PFC 515.63 and 523 ms (F(1,88) = 0.52,
  F(1,192) = 1.38). The number of lag bins shifted onset latency in one
  monkey for each variable (cue: M1; choice: M2) and interacted with
  direction for choice in both.
- **Choice axis latency (p. 6).** The 1D choice dimension did not emerge
  earlier in either area consistently: M1 A1 545.83 vs PFC 454.17 ms
  (p = 0.032), M2 A1 462 vs PFC 482 ms (p = 0.32).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Cue-side information is predictable in PFC from A1's past, not the reverse | moderate | lagged regression on 1D axes, 37 sessions, two monkeys, Fig. 6 |
| C2 | Choice information is predictable in A1 from PFC's past from about 315–365 ms after target onset, and in PFC from A1's past about 40–55 ms later | moderate | Fig. 7, paired tests per monkey |
| C3 | Choice and cue information are both stronger in A1 than in PFC | weak to moderate | decoding and vector magnitude; the authors note firing-rate differences "could still affect" it (pp. 8, 11) |
| C4 | Errors arise from the target comparison, not cue encoding | moderate | single-unit and PCA error analyses, Figs. 2, 4 |
| C5 | The bidirectional flow is cortico-cortical, not shared input | weak | argued from timing, monosynaptic anatomy and the cue-period asymmetry; unrecorded areas acknowledged (p. 9) |
| C6 | The PFC-to-A1 signal biases perception, feedback that is "thought to 'edit' sensory input" | conjecture | Discussion only (p. 8); no test |

## Method

Firing rates in 50 ms bins (100 ms windows in 25 ms steps for PCA and
decoding), z-scored per session. Linear regression per neuron on cue
side and choice; PCA on trial-type averages; linear SVM decoding with
tenfold cross-validation per session; targeted dimensionality reduction
to one axis per variable and area; AR(1) residuals; cross-area lagged
regression with 1–4 lags; R² onset and peak by paired t-test against
baseline, leave-one-session-out; two-way ANOVA on direction × number of
lags. Data on figshare (28861268); code on GitHub
(GiarroccoFranco/Auditory_Decision_Making).

## Concepts

- **information flow.** Here: the R² with which one area's
  autocorrelation-removed projection on a task axis at time t is
  predicted from the other area's lagged projections on its own axis,
  within the same trial. It is predictability along one dimension per
  area, not transfer entropy, not a causal effect, and not a measure on
  the whole population.
- **choice.** The monkey's report on the trial: bar release within 700 ms
  of the target, or continued holding. In match trials it is a movement,
  in non-match trials a withheld movement followed by a later one.
- **choice-related information.** Activity along the choice axis. The
  paper does not separate decision, motor preparation and prediction of
  the next event within it: "our paradigm does not allow us to dissociate
  decision-making from the motor response, and thus the observed
  A1-to-PFC signal could contain information related to both processes"
  (p. 9).

## Connections

It reanalyses Napoli et al. 2021 (ref. 30). It sits with work showing
decision and categorical signals in auditory cortex (Tsunada et al. 2016,
causal; Niwa et al. 2012; Francis et al. 2018) and with ferret work in
which sensory signals in auditory cortex precede categorical ones in
frontal cortex (Yin et al. 2020, p. 8). Its flow method follows Crowe,
Averbeck and Chafee and later Averbeck-lab studies (refs. 36, 38, 77).
The Discussion frames the result in hierarchical inference (refs. 57–58)
and top-down "editing" of sensory input (ref. 56). The record holds none
of these.

## Bearing on the record

- **What "choice-related information flowing PFC to A1" is.** Activity
  along the axis that best separates release from hold trials (errors
  included), in a task where the report is a manual act. The authors
  propose two readings, neither tested: a feedback that biases perception
  "toward an expected target location, which in our task corresponded to
  the location of the first cue" (p. 8), or "a recurrent process in which
  choice-related signals are iteratively refined" (p. 8). For the return
  signal they add "the preparation or stabilization of an impending
  behavioral response" (p. 9). So it is a decision, a motor plan, or both;
  the paper says it cannot tell. Nothing in it is a prediction of the
  next stimulus in the sense of an expectation tested against an outcome.
- **Is action in the loop?** Yes, on the reading that matters for the
  claim. The choice is the bar response, PFC-to-A1 flow begins at
  315–365 ms and both directions peak near 500–520 ms, against match
  response times of 564–601 ms. The loop is measured in the interval
  where the motor response is being prepared. My observation: this does
  not make action causal in the loop, but it means the data cannot
  separate a judgement–observation loop from an action–perception one.
- **Does the signal change A1's sensory coding?** Not shown, on this
  trial or later ones.
  - The target lasts 300 ms. PFC-to-A1 choice flow starts 315–365 ms
    after target onset, so it reaches A1 after the stimulus it concerns
    has ended, during white noise (my observation from pp. 6, 9). It
    cannot reshape the encoding of that target; it can only shape A1's
    post-stimulus activity, which the paper finds carries choice.
  - No analysis crosses trials. Nothing tests whether a trial's choice
    signal changes A1's cue or target coding on the next trial or later.
  - The "editing" and "biasing perception" readings are from the
    Discussion, citing ref. 56; the data do not test them.
- **[CLAIM-tmpq9do8](../claims.d/CLAIM-tmpq9do8.md).** The registration's reading, that "the decision
  enters the area that produces the observation", holds in a narrow form:
  activity predictive of the report becomes predictable in A1 from PFC,
  and A1's activity then predicts PFC's. That is a within-trial,
  synchronic exchange, and the claim sets the synchronic form aside. It
  gives no evidence for the diachronic form, a judgement reshaping the
  observer whose later observations it judges. And because the report is
  a movement measured in the window of its preparation, it is not
  evidence that action can be cut out of the loop. It neither supports
  nor undermines the claim; it is neutral on both of its edges. The
  sharpest thing it offers is a design: a task in which the PFC-to-A1
  signal is measured before the next stimulus, with report and decision
  dissociated, would bear on the diachronic form.
- **[CLAIM-tmp9cjyo](../claims.d/CLAIM-tmp9cjyo.md).** The authors' framing, hierarchical inference with
  "active sensory-cognitive loops" (p. 8), is the kind of redescription
  that counter-claim uses. The data do not decide between it and the
  claim.
- **[CLAIM-tmpt568z](../claims.d/CLAIM-tmpt568z.md) and [QUESTION-tmpr5tck](../questions.d/QUESTION-tmpr5tck.md).** Little. A1's return signal is
  not evidence independent of the interpretation, since it carries the
  choice PFC sent. The cue period, in which A1 drives PFC and PFC does not
  drive A1, is the paper's case of input the loop did not select; it is
  also the period in which no comparison is required (p. 8).
- **Checks of the current LIT.** The summary is correct in outline but
  should say that choice means the report by bar release, that the flow
  measure is a lagged regression on one-dimensional projections
  (Granger-style), that the result is within-trial and correlational,
  and that decision and motor response are not separated. "Why this is
  here" asked two questions; the answers are: only the current trial, and
  yes, the response is motor.
- **For the anthology.** No instruction for machine-learning practice.

## Limitations

- Two monkeys; about 16 neurons per area per session.
- Correlational. Common input from unrecorded areas (parietal, thalamus,
  basal ganglia) is argued against, not excluded (p. 9).
- One axis per area, fixed at the bin of peak modulation; the flow is
  along that axis only.
- The lag count changed onset latency in one monkey for each variable.
- Choice is confounded with motor preparation, and on most trials with
  stimulus category.
- Stronger coding in A1 may partly reflect firing-rate differences, as
  the authors say (pp. 8, 11).
- Supplementary figures were not read for this note.

## Open questions

- Does the PFC-to-A1 choice signal change A1's encoding of the next
  stimulus, within the trial (the third stimulus in non-match trials) or
  on the next trial? The non-match trials, with a later stimulus after
  the choice to hold, could test the within-trial form with the
  published data.
- With decision and report dissociated (for example, a delayed or
  counterbalanced response mapping), does the bidirectional flow remain?
- Does inactivating PFC during the choice window abolish A1's choice
  signal, as the authors propose (p. 9)?
