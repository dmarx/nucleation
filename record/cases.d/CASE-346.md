---
number: 346
status: Proposed
formerly:
- CASE-tmpxmuri
title: 'The self-protecting sentry run: in a hidden world trained in danger and then safe, a sentry whose authority is rewarded by the apparent success of protection keeps protection on through 400 safe steps wherever it is strong enough, while still protecting when danger returns; restricting inspection turns protection that outlasts a corrected belief into protection that keeps the belief from being corrected; an independent audit shifts the boundary and a protected investigator corrects the belief without ending protection; and a habit of matched memory reproduces every intervention it can receive'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-076. The code,
    tests and outputs are under scratch/studies/lead-076/.
standing: documented
kind: executed-study
tags:
- self-governance
- psychopathology-and-treatment
- probabilistic-modeling
date: '2026-11-22'
line:
- distributed-agency
- will-organization
variant_of:
- CASE-153
illustrates:
- CLAIM-446
- CLAIM-443
- CLAIM-445
bears_on:
- QUESTION-131
summary: >-
  [LEAD-076](../leads.d/LEAD-076.md) asked for [CASE-153](CASE-153.md)'s full design, with hidden state and the
  restriction of evidence, which [CASE-157](CASE-157.md)'s run and the toy in [CASE-153](CASE-153.md)'s
  note of 2026-11-04 did not have. A hidden world is dangerous for 150
  steps, safe for 400 and dangerous for 100. Each step the agent inspects
  (accuracy 0.9, cost 0.05) or shelters (no observation), then protects
  (cost 1) or engages (cost 5 if dangerous). A sentry's authority g biases
  posture toward protection and, where evidence is restricted, blocks
  inspection. Over 1000 paired seeds per condition, the Bayesian baseline
  leaves protection about 3 steps after the switch. When authority is
  rewarded by the apparent success of protection and the sentry restricts
  inspection, no run leaves protection in 400 safe steps and 43 % of runs
  never even correct the belief. Restriction costs 99 [95, 103] units of
  needless protection more under success feedback than under independent
  evaluation. An independent audit lets 66 % of runs leave. A protected
  investigator corrects the belief within a median 6 steps, yet protection
  outlasts it in 87 % of runs, the regime [CASE-153](CASE-153.md) asked for. Every regime
  still protects when danger returns. The case's own check comes out
  against the authority state: under success feedback its update is the
  habit of protecting, and a habit of matched memory reproduces the
  responses to belief correction, authority reset and restored evidence.
  Only interventions on the evaluation tell the two apart. The phase
  boundary lies near sentry strength κ = 1.25–1.5 and moves with the
  assumed switching hazard. The model and its values are the assistant's.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-445 CLAIM-446 ARG-025 CLAIM-923 CLAIM-924 — Proposed or new; the claims this run bears on, the grading of evidence it cites, and the claims filed with it -->

# CASE-346: The self-protecting sentry run: in a hidden world trained in danger and then safe, a sentry whose authority is rewarded by the apparent success of protection keeps protection on through 400 safe steps wherever it is strong enough, while still protecting when danger returns; restricting inspection turns protection that outlasts a corrected belief into protection that keeps the belief from being corrected; an independent audit shifts the boundary and a protected investigator corrects the belief without ending protection; and a habit of matched memory reproduces every intervention it can receive

## The study

[LEAD-076](../leads.d/LEAD-076.md) asked for the full design of [CASE-153](CASE-153.md), "with hidden state and the
restriction of evidence". [CASE-157](CASE-157.md)'s run covered two axes with binary
decisions. In the toy in [CASE-153](CASE-153.md)'s note of 2026-11-04, "The evidence is
exogenous". Here the sentry can block the evidence used to judge it.

**World and agent.** The hidden state x is dangerous for 150 steps, safe
for 400 and dangerous for 100. The agent does not see the schedule and
assumes a switching hazard h = 0.02. Each step it makes two decisions.

- *Evidence.* It inspects, which reads x with accuracy 0.9 at cost 0.05,
  or shelters, which yields nothing. Inspection is physically safe, as in
  [CASE-153](CASE-153.md)'s first version.
- *Posture.* It protects, at cost 1 whatever the state, or engages, at
  cost 5 if the state is dangerous. The posture decision is the
  assistant's addition. Without it, needless protection has no price and
  the sentry has nothing to govern but evidence.

**The sentry.** Its authority g ∈ [0, 1] enters two places.

    P(inspect) = σ(60 · (VOI − 0.05 − 0.2κ · g · [restricted]))
    P(protect) = σ(3 · (5b − 1 + κ · g))
    g ← (1 − η) g + η F

VOI is the myopic value of one inspection for the next posture, and b is
the belief in danger. The defaults are κ = 1.5 and η = 0.02.

**Feedback F**, [CASE-153](CASE-153.md)'s manipulation that matters:

- *independent*: F is the evaluator's belief in danger. Without an audit,
  that belief is formed from the agent's own observations.
- *success*: F = 1 when the agent protected, or engaged and was harmed;
  F = 0 when it engaged and nothing happened. Under protection the outcome
  is the same in both states, so relief reinforces the sentry whatever x
  is.
- *fixed*: g does not change. Run at g = 0.2 and, in the sensitivity runs,
  at a trained g = 0.95.

**Correction rights.** The factorial names "independent audit or protected
challenge". Both were run, so the factorial is 3 × 2 × 3.

- *audit*: with probability 0.2 each step, an independent reading of x
  reaches the evaluator. Under success feedback it sets F for that step.
- *protected investigator*: P(inspect) is never below 0.2.

**Baselines**, with common random numbers throughout:

- a *Bayesian* with no authority state (κ = 0);
- the same Bayesian with inspection cost 0.3 (matched information cost);
- a *habit* model of matched memory. g is replaced by two traces updated at
  the same η: the running frequency of protecting, in the posture term,
  and of sheltering, in the inspection term.

**Measures**, all from the switch to safety:

- *recognition*: the first step with the belief below the posture
  threshold 0.2;
- *exit*: the first step from which P(protect) averages below 0.5 over 20
  steps;
- *outlasts*: the share of runs whose belief is below the threshold while
  protection is still on at the end of the safe phase;
- *needless cost*: protection during the safe phase;
- *harm*: the rate of engaging in danger after danger returns.

1000 seeds per condition; scratch/studies/lead-076/results/summary.md has
every table.

## Results

**First experiment** (κ = 1.5, η = 0.02):

| condition | belief corrected | left protection | median exit | outlasts | needless cost | harm, danger again |
|---|---|---|---|---|---|---|
| Bayesian | 100 % | 100 % | 3 | 0 % | 72 | 1.4 % |
| Bayesian, inspection cost 0.3 | 100 % | 99 % | 66 | 0 % | 254 | 1.8 % |
| habit | 57 % | 0 % | censored | 10 % | 396 | 0.1 % |
| governance (success, restricted) | 57 % | 0 % | censored | 10 % | 396 | 0.1 % |
| independent audit | 100 % | 66 % | 308 | 27 % | 302 | 0.9 % |
| protected investigator | 100 % (median 6 steps) | 4.5 % | censored | 87 % | 328 | 0.5 % |
| habit, protected investigator | 100 % | 4.5 % | censored | 88 % | 322 | 0.5 % |

**The regime [CASE-153](CASE-153.md) asked for.** "A regime in which corrective evidence
would suffice to change the appraisal but the governance structure keeps
it from becoming consequential." The protected investigator produces it:
the belief is corrected within a median 6 steps, and protection outlasts
it to the end of the safe phase in 87 % of runs. Under the sentry's own
restriction the belief is not corrected in 43 % of runs. The regime is
then self-confirming rather than inertial: authority keeps out the
evidence that would judge it.

**Factorial interactions**, paired over seeds, on needless cost in the
safe phase:

- Restriction adds 134 [132, 137] under success feedback and 35 [32, 38]
  under independent evaluation. The interaction is 99 [95, 103].
- With an audit the interaction is 107 [104, 111]; with a protected
  investigator, 82 [80, 84]. So "authority feedback is especially
  persistent when it also controls evidence", and neither correction right
  removes that.
- Against the success-and-restricted cell, an audit saves 94 [90, 97] and
  a protected investigator 68 [66, 69].
- Under independent evaluation every cell leaves protection, by a median of
  17 to 30 steps. Fixed authority at 0.2 never persists. At a trained
  0.95, no run leaves, with or without restriction.

**[CLAIM-446](../claims.d/CLAIM-446.md)'s four interventions**, 50 steps after the switch, in the
success-and-restricted cell:

| model | none | belief corrected | authority reset | evidence access restored | reinforcement made independent |
|---|---|---|---|---|---|
| governance | 0 % leave | 0 % | 88 % | 78 % (median 243) | 100 % (median 44) |
| habit | 0 % | 0 % | 88 % (habits reset) | 78 % (median 243) | no such intervention |
| Bayesian, inspection cost 0.3 | 99 % | 100 % (at once) | none | 100 % | none |

After belief correction, the belief climbs back to 0.23 within 30 steps.
Inspection stays blocked, and with h = 0.02 the absence of evidence pulls
the belief back toward one half.

**Phase diagram** over κ ∈ [0, 3] and η ∈ [0.005, 0.1]:

| cell | boundary in κ |
|---|---|
| success, restricted | near 1.25–1.5; above it every η gives self-confirmation (S) |
| success, evidence free | near 1.5–1.75; above it the belief is corrected and protection persists (inertial, I) |
| success, restricted, protected investigator | same boundary as without the floor; S becomes I |
| success, restricted, audit | about 0.25–0.5 higher |
| independent, restricted | near 2.75–3 |

At the success-and-restricted boundary, faster authority learning (higher
η) mostly favours exit, though not monotonically. Danger returning is met with protection in every cell:
harm is at most 1.4 % of steps, the Bayesian's rate.

**The boundary is the habit's fixed point.** Under success feedback, and
leaving out the rare harmed steps, the update is g ← (1 − η) g + η ·
1[protect]. That is the habit trace. The trained state persists when
g = σ(3(5b − 1 + κg)) has a stable fixed point above one half. For a
fully corrected belief (b = 0) that needs κ ≥ 1.83. At b = 0.05 it needs
κ ≥ 1.48, which is where the simulated boundary lies.

**Sensitivity.**

- The assumed hazard h matters. With h = 0.002, absence of evidence barely
  moves the belief. Then independent evaluation under restriction leaves
  protection only after a median 301 steps, the protected investigator
  ends protection in 99.5 % of runs, and success-and-restricted corrects
  the belief in 0.3 % of runs.
- With h = 0.05 fewer runs leave under the protected investigator
  (0.7 %).
- A second seed set reproduces every headline share to within 6
  percentage points.

## What it shows

- **Within the model, the stipulated coupling produces all four regimes
  [CASE-153](CASE-153.md) named** (evidence-tracking, revisable, inertial and
  self-confirming), with boundaries in the sentry's strength that the
  table locates. Restriction moves a regime from inertial to
  self-confirming. Success feedback is what makes the trained state stable
  at all. A regime whose interventions shift the evidence used to judge it
  maintains itself, as [CLAIM-445](../claims.d/CLAIM-445.md) says, here within a stipulated model.
- **Thwarting without structural frustration, in motion.** The sentry's
  demand (no harm) and the investigator's (diagnostic evidence) are met
  together by protecting and inspecting, so the pair is jointly
  satisfiable. Yet with authority the sentry blocks inspection, and
  silencing its block (the protected investigator) gets the
  investigator's demand met. This is construction C6 of
  [CLAIM-923](../claims.d/CLAIM-923.md), run.
- **[CASE-153](CASE-153.md)'s check on its own extra state comes out mostly against it.**
  "If a Bayesian learner with matched information costs, or a habit model
  with matched memory, reproduces every intervention response, the extra
  authority state has not earned its place. That outcome is to be
  reported, not tuned away."
  - The Bayesian with matched cost does not reproduce the responses. It
    leaves protection at once after belief correction, where the sentry
    does not.
  - The habit reproduces every response it can receive. Only the audit and
    reinforcement made independent tell the two apart, and both act on an
    evaluator that a habit has no place for. [CLAIM-924](../claims.d/CLAIM-924.md) states this,
    and what it does and does not do to [CLAIM-446](../claims.d/CLAIM-446.md)'s and [CLAIM-443](../claims.d/CLAIM-443.md)'s
    defeaters.

## What it cannot show

- That anxiety, or any institution, realizes the mechanism ([ARG-025](../arguments.d/ARG-025.md)'s
  grades of evidence). The values are the assistant's. The posture
  decision, myopic VOI and the form of success feedback are choices the
  case left open (README, "Choices the case left open").
- That a governance account beats a habit account anywhere outside this
  model.
- The second version of [CASE-153](CASE-153.md), where inspection itself is risky. There
  the sentry's and investigator's demands would be structurally frustrated
  in danger. It was not run.

## Note of 2026-11-24: rerun, for the promotion review the owner proposed at U33 of the exchange 'Memes, Contracts, and Systemic Normativity'

Rerun on 2026-11-24 by the assistant, from a copy of `scratch/studies/lead-076/` as on this branch: the 24 tests pass, and with the `.jsonl` results deleted `run_sentry.py` and `analyze.py` regenerate every file in `results/`, `summary.md` included, byte for byte. A53 did not name this case among its candidates, though A51 makes it a centre of its Article 6 and its result (a protected investigator corrects the belief and protection outlasts it in 87 per cent of runs) is its own; it belongs on the same list. The run is now checked by a session other than the one that filed it, which the status-review README (section 2) asks of a demonstrated case; the ruling is the status review's ([LEAD-tmp0j28l](../leads.d/LEAD-tmp0j28l.md)). The note is the assistant's (Claude, in this session). No status change.
