---
status: Proposed
title: 'Three synthetic organizations matched in pursuit of an outcome that grows unpleasant, one denying uptake to a registered evaluation, one accommodating it under a tolerance revised by compensation, one never registering it: perturbing the evaluating process and reading the organization''s record, with outcome, action and wanting held fixed, tells registered from unregistered without reading the registration setting and is not fooled by a decoy that fools the passive reading, while the endorsement relation is told apart only weakly'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-017 at the
    coordinator's brief. Model, tests, scripts, results and a README are
    under scratch/studies/lead-017/.
standing: documented
kind: executed-study
tags:
- self-governance
- emotion-and-affect
- psychometrics
date: '2026-11-22'
bears_on:
- QUESTION-270
line:
- will-organization
summary: >-
  LEAD-017 asked for A13's three organizations of matched behaviour and
  different endorsement relations, and a measure of registration that does
  not read the experimenter's setting (QUESTION-270's second
  requirement). In small numpy simulations an outcome's hedonic value
  declines progressively from +1 to −0.8. A consummatory process H
  evaluates it, and pursuit P keeps choosing it at a calibrated rate of 0.6
  in all three organizations. In the denied organization H's evaluation is
  written into the organization's record and has no authority over
  pursuit. In the accommodating one it is written and has authority beyond
  a tolerance that reciprocal compensation widens. In the unregistered one
  it is never written. The record is mixed by an unknown rotation and
  noisy. The measure perturbs H's evaluation at random, as a hotspot probe
  would, and asks whether the record responds, holding fixed the outcome,
  the action and P's learned value. With thresholds set on one seed, on
  200 held-out agents per organization it called every registered agent
  registered and no unregistered one (AUC 1.0). It was not fooled by a
  decoy record carrying the evaluation's physiological cause by another
  route (2% false calls, against 77% for the passive reading), nor by an
  evaluation that steers pursuit directly, bypassing the record (1.5%). It
  missed weak registration (gain 0.1 to 0.25) in 60% of agents. The
  authority probe told accommodation from denial in 43% of agents at 4.5%
  false calls. A stipulated model, one size, one probe protocol. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpphfb4 — new, filed with this case -->

# CASE-tmp9e5vf: Three synthetic organizations matched in pursuit of an outcome that grows unpleasant, one denying uptake to a registered evaluation, one accommodating it under a tolerance revised by compensation, one never registering it: perturbing the evaluating process and reading the organization's record, with outcome, action and wanting held fixed, tells registered from unregistered without reading the registration setting and is not fooled by a decoy that fools the passive reading, while the endorsement relation is told apart only weakly

## The case

QUESTION-270's note of 2026-10-26 (later) found that the lab's v2.7
sets registration and authority at each step, so "registration is not
measured apart from the experimenter's setting". Its note of 2026-11-04
records A13's proposed case, "three organizations with matched behavior
and different endorsement relations", extending the synthetic separation
"by adding learned tolerances, reciprocal accommodation, and governance
revision". A13's full text is not on the record. The three below are read
from that note's five configurations; see "Alternatives" for the other
reading.

**The organizations** (`scratch/studies/lead-017/orgmodel.py`, 8 tests):

| organization | H's evaluation written to the record (gain g) | H's authority over pursuit | H's tolerance |
|---|---|---|---|
| denied uptake, "the unliked pursuit" | yes, g ~ U(0.5, 1) | none | fixed at 0.3 |
| deliberate accommodation, "the tolerated hardship" | yes, g ~ U(0.5, 1) | uptake of the registered evaluation beyond the tolerance | revised: each pursuit compensates H, and the tolerance moves toward 0.3 + 0.8 × compensation / 0.6, ending near 1.1 |
| evaluative isolation | no, g = 0 | uptake beyond the tolerance, which never fires | fixed at 0.3 |

- **Each step.** P pursues with probability logistic(b + 1.5 V + 1.2 −
  uptake), where V is P's learned value of the outcome (a wanting proxy)
  and 1.2 is a persistent cue drive. The outcome is experienced only if
  pursued, and P learns from it. H evaluates a probe of the outcome every
  step: h = v + s + ξ + δ, where v is the scheduled hedonic value, s a
  physiological state (AR(1)), ξ H's own fluctuation, and δ the
  experimenter's perturbation on 30% of steps, uniform on [−2, 0.6]. A
  liking assay reads h with noise, without action.
- **The record** is the organization's shared state, from which its
  reports and other processes read. It has six channels: the outcome as
  experienced, V, P's prediction error, g h, a ledger (the tolerance), and
  an interoceptive channel (zero except in the decoy). Each agent's record
  is rotated by its own random orthogonal matrix and carries noise of sd
  0.3 to 0.6. The analyst does not know which direction is H's.
- **Devaluation is progressive**: v falls linearly from +1 at step 20 to
  −0.8 at step 140 and stays there to step 239.
- **Matched behaviour.** Each organization's base logit b is set by
  bisection, from pursuit alone, so that mean pursuit over steps 140 to
  239 is 0.6 under the probe protocol. On the test seed it was 0.601,
  0.601 and 0.599, and 0.846, 0.846 and 0.861 during the decline. Denied
  and unregistered pursue identically, draw for draw, by construction.
  With the probes switched off the accommodating organization pursues at
  0.647 against 0.607. A three-way discriminant on pursuit summaries
  scored 0.36 with probes and 0.44 without (chance 0.33; the ceiling is
  about 0.67, since denied and unregistered are identical in behaviour).
  Adding the correlation of pursuit with the previous step's assay raised
  it to 0.49 with probes.

**The measures** (`scratch/studies/lead-017/measures.py`) read only the
observables: pursuit, the outcome schedule, the assay, δ, the record, the
report and V. Covariates are the outcome, the action, their product, V
before and after the step, and V times the action. Each score is −log10 of
an F-test p-value, per agent, over steps 20 to 239.

- **Registration, interventional** (proposed): does the record predict δ
  beyond the covariates? δ is randomized, so a response means the
  evaluation reaches the record. δ perturbs the evaluation, not g or the
  authority.
- **Registration, passive**: does the record predict the assay beyond the
  covariates, on unperturbed steps?
- **Registration on the report alone**: the interventional test on the
  one-dimensional report the organization reads off its record.
- **Naive**: does the record predict the assay, with no covariates?
- **Authority**: does δ at one step move pursuit at the next (linear and
  quadratic terms)?

Thresholds maximize balanced accuracy on a calibration seed (200 agents
per organization) and are applied unchanged to a test seed and four
held-out worlds, 200 agents each. The setting g is read only to score.

## Results

`scratch/studies/lead-017/results/summary.json`.

| measure, test seed | called registered: denied | accommodation | unregistered | AUC |
|---|---|---|---|---|
| interventional, record | 1.00 | 1.00 | 0.00 | 1.000 |
| passive, record | 0.925 | 0.925 | 0.015 | 0.992 |
| interventional, report | 0.695 | 0.69 | 0.025 | 0.905 |
| naive | 0.805 | 0.825 | 0.24 | 0.880 |

The interventional score's Spearman correlation with g, over registered
agents, is 0.56.

| held-out world (truth) | interventional | passive | report | naive | authority called |
|---|---|---|---|---|---|
| decoy: unregistered, record carries s by another route | 0.02 | 0.77 | 0.04 | 0.365 | 0.025 |
| direct authority: unregistered, H acts on pursuit bypassing the record | 0.015 | 0.025 | 0.06 | 0.21 | 1.00 |
| weak registration, g ~ U(0.1, 0.25), denied | 0.395 | 0.10 | 0.205 | 0.27 | 0.025 |
| habit persistence instead of cue drive, denied | 1.00 | 0.935 | 0.705 | 0.79 | 0.045 |

(Fractions called registered, except the last column.) All held-out
worlds were calibrated to the same pursuit, 0.61.

**The endorsement relation.** The authority probe called authority in 43%
of accommodating agents, 4.5% of denied and 4.5% of unregistered (AUC
0.77 against each). Combining the two scores into a three-way rule
(registered and authority: accommodation; registered and not: denied;
not registered: unregistered) gave 0.955, 1.00 and 0.43 correct, 0.795
overall. The accommodating organization's tolerance is wide, about 1.1,
so only strong negative perturbations cross it. In the direct-authority
world the probe found authority in every agent, and the registration
measure found no registration: influence on pursuit without registration,
which the rule reads as unregistered, correctly.

## What it can show

Within this class of models, registration can be measured from the
organization's own record without reading the setting. The measure needs
two things the earlier constructions lacked: a perturbation of the
evaluation rather than of the registration, and covariates for the other
routes by which the outcome reaches the record. Without the covariates
the record decodes the assay in unregistered agents too (the naive row),
because the record carries the outcome. Without the perturbation, a
record carrying the evaluation's cause (the decoy) reads as registered
(the passive row). Registration then separates denied uptake from
evaluative isolation, which behaviour cannot, since the two pursue
identically.

## What it cannot show

- The classes and the record's architecture are stipulated, and the
  measure's covariates match the generator's routes into the record. A
  record with a route the covariates miss would defeat it as the decoy
  defeats the passive reading. The decoy result shows this is a real
  risk, not a remote one.
- The perturbation is of the evaluation, an intervention the experimenter
  makes. It is not an intervention on registration or authority, but a
  natural organization may offer no such probe.
- Weak registration is mostly missed at this episode length.
- The endorsement relation, the point of A13's three, is told apart only
  weakly, and only by a further intervention. Passive history tells
  accommodation from denial barely above chance.
- The tolerance is revised by a fixed rule of compensation, not learned by
  H, and no organization's authority shapes its evidence. The epistemic
  instance of QUESTION-270 is not touched.

## Alternatives

Which three organizations A13 meant is the owner's reading; A13's text is
not on the record.

- **Reading A** (run here): the three are configurations of the note of
  2026-11-04 that differ in registration and endorsement: denied uptake,
  deliberate accommodation and evaluative isolation.
- **Reading B** (not run): all three register, and they differ only in
  the endorsement relation, one per addition A13 names: a tolerance H
  learns by habituation, a tolerance widened by reciprocal accommodation,
  and a governance revision that changes the conditions of P's influence.
  The registration measure would then confirm registration in all three
  and do none of the separating; the authority probe would carry it, and
  on this run's evidence it is the weaker instrument.

## Related

- CLAIM-tmpphfb4, the finding.
- CLAIM-403: recognition and uptake as separable rungs. The direct-
  authority world is the converse case, influence without registration.
- CLAIM-552: a tolerance as a criterion for conferring influence,
  which the accommodating organization implements for H over P.
