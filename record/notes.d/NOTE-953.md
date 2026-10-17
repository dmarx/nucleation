---
number: 953
status: Read
formerly:
- NOTE-tmp8euox
paper: LIT-1184
title: 'Sung, Rigotti & Lee — factorized goal and uncertainty codes in lateral PFC'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the publisher's open-access PDF (Nature
    Communications 16:11643, CC BY-NC-ND, 14 pages, fetched from
    nature.com on 2026-10-16), extracted with pdftotext: abstract,
    introduction, Results (all four subsections), Discussion and the whole
    of Methods (participants, task, behavioural measures, simulation, fMRI
    collection and preprocessing, decoding, shattering, CCGP, statistics,
    data and code availability). Page 10 was rendered as an image to check
    the model equations. The Supplementary Information PDF (MOESM1) was
    also fetched: its figure captions were read, and Supplementary Tables 3
    and 4 were read row by row for the shattering comparisons and the
    neural–behaviour correlations; Tables 1 and 2 were not. The reporting
    summary was glanced at; the peer-review file and source data were not
    opened. The reference list was scanned. Page numbers below are the
    article's (1–14); quotations are from the extraction, with the
    ligature "fi" and line-break hyphens restored.
date: '2026-10-16'
summary: >-
  A reanalysis of 20 people's fMRI from a 2014 two-stage Markov task with
  cued goals and block-wise transition noise. Goals and transition
  uncertainty are linearly decodable, weakly, from vlPFC, dlPFC and OFC, in
  a geometry whose nonlinear dichotomies decode worse than goal and linear
  ones ("factorized"), and a goal decoder trained under one noise level
  transfers to the other. Goal separability and transfer in lateral PFC
  correlate with choice flexibility and optimality across subjects;
  uncertainty separability does not. Unfitted model-free agents show a
  flexibility–stability trade-off that model-based agents and humans do
  not.
---

# NOTE-953: Sung, Rigotti & Lee — factorized goal and uncertainty codes in lateral PFC

## Contribution

It reanalyses an existing dataset (Lee, Shimojo and O'Doherty 2014, its
ref. 17) with the representational-geometry tools of Bernardi et al. 2020
(shattering dimensionality, cross-condition generalization, parallelism)
and asks how goals and environmental uncertainty share a neural space. It
finds a mostly linear ("factorized") arrangement in vlPFC, dlPFC and OFC,
in which the goal code does not measurably move when transition noise
changes. Across 20 subjects, how separable and how transferable the goal
code is correlates with behaviour. It adds simulations showing that
model-free agents trade flexibility against stability, and model-based
agents do not.

## Key insight

A code in which one variable's readout generalizes across the levels of
another lets a system notice the second variable without disturbing its
use of the first. "In such a factorized embedding structure, it is
possible to detect uncertainty changes, while goal information remains
consistently represented regardless of uncertainty levels" (p. 5). The
paper's closing gloss: "By maintaining separate codes for goal and
uncertainty, the PFC preserves goal-directed action plans while selectively
adjusting behavior in response to environmental variability" (p. 9).

## Assumptions

- **The task is an action–outcome learning task.** "Goal-directed
  learning requires representing action-outcome contingencies and updating
  them to attain a goal" (p. 1). Participants make two left/right choices
  per trial through a tree of states to a coloured coin, and were told
  they "should learn, through experience, which choices were more likely
  to lead to each colored coin" (p. 9). Everything that changes their
  model arrives as the consequence of their own choices.
- **The goal is cued from outside, per trial.** A coloured box at trial
  start says which coin pays (specific goal); a white box says any coin
  pays (non-specific). The goal is not chosen, inferred or held by the
  participant across trials.
- **"Uncertainty" is block-wise transition stochasticity of the
  environment**: transition probabilities (0.9, 0.1) against (0.5, 0.5),
  alternating in short uncued blocks (3–5 and 5–7 trials, p. 9). It is not
  the subject's uncertainty about a hypothesis, nor a reliability score
  attached to a piece of evidence.
- **"Factorized" is operational, and linear.** Three tests (pp. 5–7,
  11):
  - *Shattering.* Six classes (3 goals × 2 uncertainty levels); every
    balanced dichotomy is decoded with a linear SVM, and dichotomies are
    grouped as goal (3), uncertainty (1), linear and nonlinear (9, those no
    random linear-mixing model y = W_g g + W_u u + b with N = 3 could
    separate). Factorized mixing is the profile goal, uncertainty and
    linear SD high, nonlinear SD "significantly lower".
  - *CCGP.* Train a goal decoder in low-uncertainty trials, test in high,
    and the reverse; average. "If the target embedding is influenced by
    context, the decision boundary for decoding would shift, leading to a
    lower CCGP" (p. 7). Factorization is read off CCGP not differing from
    within-condition goal SD.
  - *Parallelism.* Cosine between goal-difference vectors in the two
    uncertainty conditions (Supplementary Fig. 9).
  CCGP was computed only for goal across uncertainty. No decoder for
  uncertainty was trained under one goal and tested under another.
- **fMRI specifics.** 3T, TR 2.8 s; each event's pattern is the first
  volume after the event (p. 10), not a modelled response; leave-one-
  session-out cross-validation with 100 undersampling repeats; eight
  anatomical ROIs.
- **Statistics.** ROI decoding tests are uncorrected across ROIs, on the
  grounds that ROIs were chosen a priori (p. 11); neural–behaviour
  correlations are called exploratory and FDR-corrected over the eight
  ROIs. n = 20 throughout (22 scanned, 2 excluded).
- **The simulated agents are not fitted to humans.** MB and MF agents
  each run with 1000 random (learning rate, inverse temperature) pairs on
  each of the 20 humans' trial and goal sequences (20,000 agents each), and
  the human–agent comparison is between scatter patterns (p. 10).

## Key results

- **Behaviour (p. 2, Fig. 1d).** Uncertainty hurt choice only without a
  specific goal: optimality 0.850 ± 0.035 (low) against 0.619 ± 0.021
  (high), t(19) = 5.975, p < 0.0001; consistency 0.897 against 0.847,
  t(19) = 5.294. With a specific goal neither changed (optimality t(19) =
  0.887, p = 0.384; consistency t(19) = 0.891, p = 0.386). Response times
  were longer with a specific goal, and longer still under high
  uncertainty (Supplementary Fig. 1).
- **Agents against humans (p. 3, Fig. 1f).** Flexibility (choice
  versatility after a goal change) with performance: humans r = 0.827,
  MB r = 0.799, MF r = −0.035. Stability (choice consistency within a
  goal) with performance: humans 0.779, MB 0.963, MF 0.042. Flexibility
  with stability: humans 0.541 (p = 0.014), MB 0.829, MF −0.964. "MF agents
  suffer from a flexibility-stability trade-off …, whereas humans and the
  MB agents did not."
- **Decoding (pp. 4–5, Fig. 2).** Goal (chance 33.3%): dlPFC 38.8%,
  vlPFC 37.2%, V1 36.9%, OFC 36.6%, ACC and preSMA 35.4%. Uncertainty
  (chance 50%), in the specific-goal condition only: OFC 53.4%
  (p = 0.0014), dlPFC 52.1% (p = 0.026), vlPFC 51.8% (p = 0.020),
  uncorrected; not decodable in the non-specific condition, and "Uncertainty
  was not decodable in ACC" (p. 8).
- **Shattering (p. 5, Supplementary Table 3).** vlPFC goal SD 0.530,
  uncertainty 0.518, linear 0.519, nonlinear 0.508; dlPFC 0.541, 0.521,
  0.526, 0.511; OFC 0.527, 0.534, 0.521, 0.507. All above 0.5, nonlinear
  included. Nonlinear SD is below goal and linear SD in vlPFC and dlPFC,
  and below all three in OFC. In vlPFC and dlPFC the uncertainty SD is not
  distinguishable from the nonlinear SD (t(19) = 1.446, p = 0.164;
  t(19) = 1.175, p = 0.254).
- **CCGP (p. 7, Fig. 4a, Supplementary Table 4).** In every ROI, goal
  CCGP across uncertainty did not differ from goal SD within either
  uncertainty level (vlPFC t(19) = −0.337 and −0.827; dlPFC −0.072 and
  −0.372; OFC 0.109 and −0.395; all n.s.). Parallelism was above zero in
  vlPFC, dlPFC, OFC and preSMA.
- **Neural–behaviour correlations, FDR-adjusted (Supplementary Tables 3
  and 4).**
  - Goal SD with flexibility: vlPFC r = 0.583, dlPFC 0.641 (q < 0.03);
    with stability: vlPFC 0.554, dlPFC 0.577 (q = 0.031); with performance:
    vlPFC 0.679, dlPFC 0.768, OFC 0.549.
  - Uncertainty SD with any behaviour: none (e.g. flexibility vlPFC
    r = −0.150, dlPFC −0.050). The text: "uncertainty separability was not
    significantly related to goal-directed behavior" (p. 6).
  - Goal CCGP with flexibility: vlPFC r = 0.576, dlPFC 0.551
    (q = 0.047); with performance: vlPFC 0.628, dlPFC 0.713, ACC 0.564,
    preSMA 0.641; **with stability: none after correction** (vlPFC
    r = 0.559, dlPFC 0.543, q = 0.054; OFC 0.468, q = 0.075).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With a cued specific goal, transition noise does not lower choice optimality or consistency; without one, it does | moderate | Fig. 1d, n = 20, paired t-tests |
| C2 | Unfitted model-free agents trade flexibility against stability; model-based agents and humans show a positive relation | moderate for the agents, weak as a model of humans | Fig. 1f; agents not fitted |
| C3 | Goal and transition uncertainty are linearly decodable from vlPFC, dlPFC and OFC | weak to moderate | Fig. 2; small effects (1.8–5.5 points over chance), uncorrected across ROIs |
| C4 | Their joint geometry there is factorized (linear) rather than nonlinearly mixed | weak | Fig. 3b; nonlinear SD lower but above chance; in vlPFC and dlPFC uncertainty SD not separable from nonlinear SD |
| C5 | The goal code is unaffected by uncertainty | weak | Fig. 4a; a null difference between CCGP and SD, with no equivalence test |
| C6 | Goal separability and robustness in lateral PFC are associated with behavioural flexibility, stability and performance | moderate for flexibility and performance; not shown for CCGP and stability | Supplementary Tables 3–4, n = 20, exploratory, FDR over 8 ROIs |
| C7 | The factorized code is the mechanism of stably flexible behaviour | weak | correlational only; no intervention or model linking geometry to choice |

## Method

1. Reuse Lee et al. (2014): 400 main-task trials over five sessions, 100
   pretraining trials at (0.5, 0.5) with a white box.
2. Score each choice for optimality (against an oracle with true
   transitions and rewards), versatility (switch after a goal change) and
   consistency (same choice when the goal repeats).
3. Simulate MB agents (FORWARD transition learning with a state prediction
   error δ_SPE = 1 − T(s, a, s′), ΔT = η δ_SPE, and BACKWARD planning that
   recomputes Q_MB from the cued goal's reward at once) and MF agents
   (SARSA on the reward prediction error), both with softmax choice (p. 10).
4. Decode goal, uncertainty and all six-class dichotomies per event with
   linear SVMs; compute SD, CCGP and parallelism; correlate per-subject
   pre-outcome averages (S1–A2) with the behavioural measures.

## Concepts

- **Choice versatility** — on a trial whose goal differs from the last,
  1 if the choice at the same state differs, else 0. The paper's
  flexibility.
- **Choice consistency** — on a trial whose goal repeats, 1 if the choice
  at the same state is the same, else 0. The paper's stability. In the
  high-uncertainty blocks a consistent choice is one not revised after a
  noisy transition.
- **Shattering dimensionality (SD)** — mean linear-decoder test accuracy
  over a set of dichotomies of the condition classes.
- **CCGP** — accuracy of a decoder for one variable trained in one level
  of another variable and tested in a different level (Bernardi et al.
  2020).
- **Factorized mixing** — goal, uncertainty and linear dichotomies
  separable, nonlinear (interaction) dichotomies markedly less so.

## Connections

The analysis is Bernardi et al.'s geometry of abstraction (Cell 2020;
Rigotti is among its authors, which the paper's reference, "Bernardi, S.
et al.", does not show), with Rigotti et al.'s mixed-selectivity and
shattering apparatus (2013), applied to human BOLD patterns. The dataset
and the MB agent's FORWARD/BACKWARD scheme come from Lee, Shimojo and
O'Doherty (2014) and Gläscher et al. (2010). The factorization-for-
generalization reading follows Flesch et al. (2022) and Ito et al. (2022).
The paper cites recent task-switching work that treats stability and
flexibility as controlled by "independent mechanisms" (p. 8).

## Bearing on the record

- **[CLAIM-341](../claims.d/CLAIM-341.md) (the loop runs between judgement and observation,
  without action).** Nothing for or against. The task is an
  action–outcome loop in the sense the claim sets aside: what the subject
  learns, transitions and coins, arrives only as consequences of its own
  choices, and the paper defines its subject matter that way (p. 1). No
  condition holds action and its outcomes fixed, so defeat condition (a)
  is not touched. The goals are cued by the experimenter each trial, not
  judgements the subject forms.
- **[CLAIM-342](../claims.d/CLAIM-342.md) and [QUESTION-121](../questions.d/QUESTION-121.md) (what scores evidence
  independently of the interpretation it tests).** The LIT's "Why this is
  here" offers factorized goal and uncertainty codes as "a candidate for
  how a mind keeps its scoring of evidence apart from its current goal".
  The reading narrows that in four ways.
  - *Wrong direction measured.* CCGP was computed for the goal code across
    uncertainty levels: uncertainty does not bend the goal readout. What
    independent scoring would need is the converse, an uncertainty (or
    evidence) code that does not bend with the goal. The paper never trains
    an uncertainty decoder under one goal and tests it under another.
  - *Uncertainty is coded only under a specific goal.* vlPFC, dlPFC and
    OFC "significantly represented uncertainty information exclusively
    within the specific goal condition" (p. 5). Whether uncertainty is
    represented at all depends on the goal condition. Within that
    condition it is factorized from which goal, but the evidence-side code
    is gated by having a goal, which is the opposite of scoring that runs
    without reference to it.
  - *The uncertainty axis is the weak one.* In vlPFC and dlPFC uncertainty
    SD is not separable from the nonlinear SD (p = 0.164, 0.254), and
    uncertainty separability predicts no behaviour. The title's
    "factorized embedding of goal and uncertainty in the lateral prefrontal
    cortex" rests in LPFC on goal and linear dichotomies.
  - *Uncertainty is not evidence scoring.* It is a block-level estimate of
    how noisy transitions are, a precision-like context. It is closer to
    [QUESTION-121](../questions.d/QUESTION-121.md)'s candidate 4 (processing signals, scoring "how the
    interpretation is going, not what it says") than to Regime B's
    independent score of operators, and the paper does not show it
    regulating learning rates.
  - *My observation: the closer analogue is in the simulation.* The MB
    agent's transition model is scored by a state prediction error that
    does not involve the goal (δ_SPE = 1 − T(s, a, s′), p. 10); the goal
    enters only afterwards, in BACKWARD planning. The MF agent's only
    error signal is the goal-defined reward, so its evidence is scored
    through what it currently wants, and it shows the trade-off
    (flexibility–stability r = −0.964). That is [CLAIM-342](../claims.d/CLAIM-342.md)'s shape, an
    anchor whose scoring does not pass through the current goal, in a
    two-parameter toy. Three cautions: the agents are not fitted to the
    humans; the goal here is a cued reward, not an interpretation under
    test; and the evidence that scores the MB model, the observed
    transition, arrives through the agent's own choice. So it illustrates
    separation of scoring from goal, not evidence free of action.
- **[CLAIM-340](../claims.d/CLAIM-340.md) (commitment and κ′ against κ̄).** No bearing beyond
  analogy. In the MB agent the cued goal bends neither the committed
  transition predictions nor the reading of the observed transition, so
  in the claim's terms both weights are zero with respect to the goal,
  trivially. The paper measures nothing that could estimate κ′ or κ̄ in
  people.
- **Checks of the current LIT against the text.**
  - Summary, "In simulations model-free learning fails the
    flexibility–stability trade-off while model-based learning can be both
    flexible and stable": correct, for unfitted agents with random
    parameters.
  - Summary, "goals and uncertainty are represented as factorized
    embeddings in lateral prefrontal and orbitofrontal cortex": as the
    paper says, with the qualifications above (small effects, uncorrected
    ROI tests, nonlinear SD above chance, uncertainty side weak in LPFC,
    uncertainty coded only under specific goals).
  - Summary, "the separability of goals and their resilience to
    uncertainty correlated with participants' flexibility and stability":
    goal separability, yes. Goal resilience (CCGP) correlated with
    flexibility and performance after correction, not with stability.
    The main text says the goal CCGPs in vlPFC and dlPFC "were
    significantly correlated with behavioral flexibility, stability, and
    performance" (p. 7); Supplementary Table 4 gives the stability
    correlations q = 0.054, n.s., and Fig. 4b marks them only as "weak
    statistical significance (significant before multiple correction)".
  - Tags: `learning-and-conditioning` fits; the task is instrumental
    learning with cued goals.
- **For the anthology.** No instruction for machine-learning practice. A
  closing suggestion to build β-VAE-like factorized RL agents (p. 8) is a
  research direction, not a practice.

## Limitations

- n = 20, a reanalysis of a 2014 dataset, BOLD at TR 2.8 s with one volume
  per event.
- Decoding effects are a few points above chance and ROI tests are
  uncorrected across ROIs.
- "Unaffected by uncertainty" is a failure to find a difference, without an
  equivalence test or power analysis.
- The brain–behaviour link is across-subject correlation, called
  exploratory; nothing is manipulated.
- Agents are compared with humans by scatter pattern, not fitted; the
  human flexibility–stability correlation (0.541) is not shown to need an
  MB learner.
- The goal is cued every trial, so "goal pursuit" here does not include
  forming or holding a goal.

## Open questions

- Is the uncertainty code invariant across goals (CCGP of uncertainty
  across goals)? That is the test the record's question needs.
- Does the uncertainty code modulate learning from transitions, as an
  arbitration signal would, and is it present when no specific goal is
  cued?
- Does the human stability under noise come from goal-independent scoring
  of the transition model, as in the MB agent? Fitting the agents to the
  choices would say.
