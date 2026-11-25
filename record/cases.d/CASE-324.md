---
number: 324
status: Proposed
formerly:
- CASE-tmp66fkd
title: 'Coupled meaning–influence model vs cut models'
statement: >-
  A simulation of the coupled meaning–influence model with three operators
  and four contexts, fitted beside separate models of matched complexity and
  training data: where authority is scored against the dominant reading, the
  joint model predicts the effects of held-out compositions of a governance
  intervention and a later change of context two to thirty times better than
  a model whose authority ignores interpretation or one that adds an
  interpretation model to a governance model, and where it is not, the joint
  model gains nothing and the information criterion prefers the cut one
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-029. The code,
    tests and outputs are under scratch/studies/lead-029/.
standing: documented
kind: executed-study
tags:
- complex-systems
- self-governance
- probabilistic-modeling
date: '2026-11-22'
bears_on:
- QUESTION-088
line:
- distributed-agency
- will-organization
- pragmatic-transport
summary: >-
  [LEAD-029](../leads.d/LEAD-029.md) asked for a joint prediction of the pragmatic-transport and
  will-organization lines, derived through [CLAIM-336](../claims.d/CLAIM-336.md)'s mapping with
  flexibility penalized, and for the comparison of one model against
  separate models that A55 §7 states and [ARG-065](../arguments.d/ARG-065.md) holds. Data were simulated
  from an instance of [CLAIM-297](../claims.d/CLAIM-297.md)'s equations: three operators, four contexts
  (frames), a scalar meaning state read out as a noisy response, and
  governance interventions that boost or suppress one operator's authority.
  The joint model (16 parameters) was fitted beside a model with the loop
  cut (15), the same with more freedom (19), and an interpretation model
  plus a governance model (18), on the same 240 training episodes, and all
  were scored on the effects of interventions in compositions not seen in
  training. With the loop present the joint model's error was 0.0013 to
  0.0185, against 0.0062 to 0.0504 for the best separate model; with the
  loop present but misspecified, about half; with no loop it tied the cut
  model and the BIC preferred the cut model. The world is built and the
  joint model is its family, so the study shows that the test has power
  and what the prediction is, not that any real system has the loop. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-286 CLAIM-336 ARG-065 CLAIM-888 — Proposed or new; the claims and the argument this study tests, and the claim filed with it -->

# CASE-324: Coupled meaning–influence model vs cut models

## The study

[LEAD-029](../leads.d/LEAD-029.md) asks for "the prediction with flexibility penalized" and then
"A55 §7's comparison of one model against separate models". As
[ARG-065](../arguments.d/ARG-065.md) and [CLAIM-336](../claims.d/CLAIM-336.md)'s note of 2026-11-07 hold A55 §7, the comparison is
on "held-out compositions of context changes and governance
interventions", against separate interpretation and governance models
"under matched complexity and training information", especially on
"history-dependent responses after an intervention that changes which
processes can influence later interpretation". The A55 text itself was
not reread; the study works from the record's paraphrase.

**The generator** is [CLAIM-297](../claims.d/CLAIM-297.md)'s three equations in the smallest form
that has both lines in it. Three operators i act under one of four
contexts q (the frame of [CLAIM-336](../claims.d/CLAIM-336.md)'s mapping). The meaning state x is the
weight on one of two interpretations, and the judgement read out at each
step is x plus noise (σ = 0.03). Operator i under q pulls x toward its
own reading a_i(q):

- meaning: x_{t+1} = (1 − ρ) x_t + ρ Σᵢ wᵢ aᵢ(q_t), with w = softmax(u),
  which is Σᵢ wᵢ Pᵢ(q)ᵀx for the stochastic matrices
  Pᵢ(q) = (1 − ρ)I + ρ·1[aᵢ(q), 1 − aᵢ(q)];
- influence: u ← (1 − κ)u + η(s − s̄), with sᵢ = −(aᵢ(q_t) − x_{t+1})²,
  each operator scored against the interpretation it helped make dominant
  ([CLAIM-297](../claims.d/CLAIM-297.md)'s circuit, [CLAIM-330](../claims.d/CLAIM-330.md)'s Regime A);
- governance: a conferral E_t adds ±Δ to one operator's u at one step.

ρ = 0.3, κ = 0.1, Δ = 1.5. In context 0 the three operators agree
(a = 0.5); in contexts 1 to 3 their readings are drawn from U(0.1, 0.9)
and differ by at least 0.4. Four generators: **amplifying** (η = 3),
**damped** (η = 0.5, below the threshold below for most pairs),
**null** (η = 0, no loop) and **amplifying-abs** (η = 1 with the score
−|aᵢ − x| in place of the square, so that the joint model fitted below is
misspecified).

## The derived prediction

For two operators under one context with dissent Δa = a₁ − a₂,
linearized at the symmetric allocation, the map on (δx, δv), v = u₁ − u₂,
has Jacobian [[1 − ρ, ρΔa/4], [2ηΔa(1 − ρ), (1 − κ) + ηρΔa²/2]], which is
[CLAIM-330](../claims.d/CLAIM-330.md)'s form, and det(I − J) = ρ(κ − ηΔa²/2). So a perturbation of
authority grows under a context exactly when **η·Δa²/2 > κ**, and decays
at the governance rate where the operators agree (Δa = 0). The tests
check the determinant and the eigenvalue condition on 20,000 draws, the
Jacobian against finite differences of the map, and growth in simulation
on both sides of the threshold.

What follows for an intervention composed with a later change of context
is two things, which together are the joint prediction:

1. **The effect of a past intervention on a response under a new context
   has the sign and size of the treated operator's reading there,
   relative to the others**, not the effect it had when applied. A model
   that adds a governance effect to an interpretation model cannot
   express this; a model that carries authority across contexts can.
2. **How much of the intervention survives depends on the dissent among
   the operators under the contexts the system passed through after it.**
   It is amplified while they dissent and decays where they agree. A
   model whose authority does not answer to interpretation lets every
   intervention decay at one rate, whatever the context.

## The rivals

All four are fitted by least squares on the same training responses,
with six random starts each fitted on growing prefixes of the episodes
(6, 12 and 24 steps); the joint model also gets three starts from the
cut model's fit with the loop switched on.

| model | parameters | what it is |
|---|---|---|
| joint | 16 | the generator's family: a (12), ρ, η, κ, Δ |
| cut | 15 | the same with η = 0: governance moves authority, interpretation never does |
| cutflex | 19 | cut with a decay and an intervention size for each operator |
| additive | 18 | an interpretation model (a level for each context, approached at rate ρ) plus a governance model (an effect for each operator and context, decaying at φ), summed |

"Separate interpretation and governance models" is open between the cut
and additive readings, so both were run. The cut model is also the
nearest this construction has to a central executive: authority set only
by intervention from outside and a fixed decay.

**Two training designs**, 240 episodes of 24 steps each. **D1**: half the
episodes change context and have no interventions, half hold one context
and have one to three interventions, so no training episode composes the
two. **D2**: episodes change context and have interventions, except that
three (operator, context) pairs are never intervened on.

**The test**: context c for 12 steps with one boost or suppression of one
operator at step 4, then context c′ ≠ c; all 72 combinations, each beside
its untreated twin. The score is the RMS error over steps 12 to 23 of the
predicted effect of the intervention (treated minus untreated) against
the noiseless truth. Six seeds per generator and design.

**Two fitting protocols.** *Blind*, as above. *Informed* adds one start at
the generating values for the three operator models (the additive model
has none), to separate a failure of the model class from a failure of the
optimizer.

## Results

RMS error of the predicted effect after the change of context, mean over
six seeds, blind protocol (informed in brackets where it differs by more
than 0.001). The true effects have RMS 0.065 (amplifying), 0.039
(damped), 0.030 (null) and 0.051 (amplifying-abs).

| generator, design | joint | cut | cutflex | additive |
|---|---|---|---|---|
| amplifying, D1 | 0.0086 [0.0029] | 0.0511 | 0.0504 | 0.0643 |
| amplifying, D2 | 0.0016 | 0.0480 | 0.0481 | 0.0876 |
| damped, D1 | 0.0044 [0.0016] | 0.0109 | 0.0099 | 0.0407 |
| damped, D2 | 0.0013 | 0.0062 | 0.0064 | 0.0542 |
| null, D1 | 0.0046 [0.0014] | 0.0039 [0.0014] | 0.0017 | 0.0371 |
| null, D2 | 0.0011 | 0.0010 | 0.0014 | 0.0551 |
| amplifying-abs, D1 | 0.0185 [0.0150] | 0.0338 | 0.0331 | 0.0495 |
| amplifying-abs, D2 | 0.0136 | 0.0296 | 0.0301 | 0.0573 |

- **With the loop present** the joint model beat every separate model in
  every seed under the informed protocol, and in all but one seed of D1
  under the blind one (seed 2, where its blind fit stopped in a poor
  local optimum, as did the cut model's). Its BIC on the training data
  was lower than every rival's in every seed, but one blind fit. The
  fitted η was 2.8 to 3.0 (true 3) and 0.49 to 0.54 (true 0.5).
- **Damped, below the threshold**: the loop never destabilizes, and the
  joint model still predicts two to five times better. The loop is
  detectable without capture.
- **With no loop** the joint model fitted η ≈ 0.02 and tied the cut
  model; the cut model had the lower BIC in five or six of six seeds, and
  in D1 a cut model beat the joint model in two to four of six. So the
  comparison can come out against the joint model, and the penalty for
  its extra parameter does its work.
- **Misspecified score**: the joint model's error was about half the best
  separate model's, not a tenth.
- **The additive model** is worst everywhere, the null world included:
  prediction 1 holds whether or not there is a loop, since in this
  construction authority acts through operators whose readings depend on
  the context.
- **Prediction 2, visibly.** In the amplifying world the effect left at
  the last step is smaller for an intervention made where the operators
  agree than where they dissent (0.031 against 0.046 to 0.049; mean
  absolute effect over the test pairs); the joint fit reproduces it
  (D2: 0.031 against 0.046 to 0.050), and the cut fit reverses it (D2:
  0.065 against 0.049 to 0.052). In the null world the order is the cut
  model's (0.019 against 0.013).

## What it shows, and what it does not

It shows that the joint prediction exists and is distinctive in the
model: a model of meaning and a model of governance, each as flexible as
the joint one and trained on the same data, miss responses to held-out
compositions of a governance intervention and a later change of frame
when, and only when, authority answers to interpretation. It shows that
A55 §7's test, run on such data, has the power to tell the two apart at
this size, in both directions.

It does not show that any interpreter, person or system has the loop. The
world is built, and in three of the four generators the joint model is
its family exactly; the misspecified one narrows the margin. No real data
were used. It does not touch [CLAIM-286](../claims.d/CLAIM-286.md)'s comparison with models built for
habit, rumination, rigidity, akrasia or insight, since the construction
has no phenomena, only operators, frames and interventions. The A55 §7
wording is the record's, not checked against the exchange. The finding
is filed as [CLAIM-888](../claims.d/CLAIM-888.md).
