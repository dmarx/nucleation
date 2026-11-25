---
number: 337
status: Proposed
formerly:
- CASE-tmpshw39
title: 'Beta–Bernoulli features vs shared-driver null'
statement: >-
  A dynamic beta–Bernoulli feature model fitted to a linear organizational
  simulator against a shared-driver null matched on within-group
  correlation: it finds more overlapping features, better aligned with the
  groups, when the members never interact; neither of its intervention
  readings is right in both worlds; the communication graph alone predicts
  cuts and pulses where the coupling is real and invents coupling where a
  driver is; adding the features does not remove the invented coupling, and
  observing the driver does
version: 1
standing: documented
kind: executed-study
tags:
- probabilistic-modeling
- social-ontology
- causality
- mathematical-statistics
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-276
summary: >-
  [LEAD-144](../leads.d/LEAD-144.md)'s study, the "Option A" [CASE-165](CASE-165.md) recommends, in one linear
  family. Twenty-four members in six overlapping working groups, with a
  communication graph built from the groups, are simulated in three
  worlds: coupled along the graph; driven by one persistent external
  driver per group with no interaction; and half of each. The driver's
  gain is tuned so that every world shows the same within-group
  correlation, 0.30. CASE-165's finite beta-Bernoulli model (K = 16,
  α = 3) and four comparators are fitted to 600 days of each world and
  scored on interventions none was fitted to: a pulse to a member, and
  the cut of a group's internal ties. Over seven organizations, the
  feature model finds more features under the null (11.1) than under
  coupling (8.7), better aligned with the groups (Jaccard 0.72 against
  0.44); read as causes of members it is exact under the driver and
  misses every cut under coupling, and read as realized by its holders it
  is wrong in both. The communication graph alone is right under coupling
  and invents coupling under the driver (a predicted cut effect of −0.18
  where the truth is 0); the features added to it leave that error
  (0.21), and observing the true driver removes it (0.006). One-step fit
  ranks the models the same way in every world. The design, code and
  wording are the assistant's (Claude, in this session); adopting it is
  the owner's call.
---

# CASE-337: Beta–Bernoulli features vs shared-driver null

## What was asked

[LEAD-144](../leads.d/LEAD-144.md): "Build the simulator, fit [CASE-165](CASE-165.md)'s model, compare with modes a
shared exogenous driver produces without interaction, and predict held-out
interventions." Its test: "Features that beat the shared-driver null and
predict interventions answer [QUESTION-276](../questions.d/QUESTION-276.md); features no better than the null
do not." The question's own criterion is (ii) separating modes from those
"a shared exogenous driver produces in a model with no interaction" and
(iii) predicting "the effect of intervening on the coupling ... better than
an equally flexible model given the communication and authorization
relations and no modes, on held-out interventions".

## The study

Code, tests and outputs are under `scratch/studies/lead-144/` (study.py,
test_study.py, results.jsonl, summary.txt; README says how to rerun).
Eight organizations were drawn; one (seed 5) was dropped by a rule fixed
before reading its results, because its coupled world is not stationary.
Seven remain.

**The worlds.** N = 24 members, each in one of six working groups and a
third of them in a second, so groups overlap. The communication graph C
joins every pair that shares a group, plus six random cross-group ties.
Each member's daily activity x is one number.

- *Coupled*: x_{t+1} = 0.5·x_t + 0.4·(C/d̄)·x_t + ξ. Members copy their
  contacts; there is no external driver.
- *Driver* (the null): x_{t+1} = 0.5·x_t + g·M·d_t + ξ, with one AR(1)
  driver per group (persistence 0.8) and M the membership. C is present and
  inert. The gain g is tuned per organization so that the mean
  within-group correlation equals the coupled world's.
- *Mixed*: half the coupling, and a driver tuned the same way.

So all three worlds look alike to a mode-finder by construction: same
groups, same overlap, same within-group correlation (0.303 in each).

**The models**, fitted to 600 days of observation, each scored on 150
further days (one-step fit) and on interventions:

- *F-raw*: [CASE-165](CASE-165.md)'s model on the activity: a finite beta-Bernoulli
  allocation (π_k ~ Beta(α/K, 1), K = 16, α = 3), Gaussian loadings, member
  noise, fitted by collapsed Gibbs sampling (400 sweeps, the best joint
  likelihood in the second half kept), with each feature's activation then
  given an AR(1). No relations. The allocation is held fixed over the
  window, which is [CASE-165](CASE-165.md)'s sticky transition with its stay-probability
  near 1.
- *F-self*: the same features plus each member's own AR term, the private
  map of [CASE-165](CASE-165.md)'s u.
- *R*: a VAR(1) restricted to C and self, with no modes. This is the
  question's "communication ... relations and no modes".
- *FR*: R with features: the allocation found on the innovations of each
  member's own AR, entered as lagged, persistent regressors beside the
  graph (a factor-augmented VAR). A first trial with an alternating fit
  (VAR, then features on its residuals, repeated) gave the same result.
- *FR-oracle*: R with the true drivers observed. It is the ceiling for any
  estimate of them.
- *R-int*: R fitted instead to a run in which half the members received
  random exogenous shocks (on a fifth of days, three standard deviations),
  scored on the pulses of the other half.

The feature model alone has no rule for an intervention on the coupling.
Two readings were run as alternatives. *Exo*: features cause members, so a
pulse to one member moves nobody else and a cut changes nothing. *Con*:
features are realized by their holders, so a pulse to a member moves its
co-holders as conditioning predicts, and cutting a group's ties removes
from its members the features it mostly holds.

**The interventions**, all held out: a unit pulse to each member, scored on
the others' responses over five days (root mean square error, on the
members R-int never shocked); and the cut of each group's internal ties,
scored on the change in the group's mean pairwise correlation at
stationarity (mean absolute error). Truth is exact, from the linear
dynamics.

## What it found

Means over seven organizations (± standard deviation across them).

| | coupled | driver (null) | mixed |
|---|---|---|---|
| true cut effect | −0.286 | 0 | −0.137 |
| features found, F-raw | 8.7 ± 2.0 | 11.1 ± 2.6 | 10.1 ± 1.3 |
| best Jaccard with the groups, F-raw | 0.44 ± 0.07 | 0.72 ± 0.10 | 0.63 ± 0.06 |
| features left beside the graph, FR | 3.6 ± 1.3 | 7.6 ± 1.6 | 5.4 ± 1.7 |
| cut error: F (exo) | 0.286 | 0.000 | 0.137 |
| cut error: F (con) | 0.240 | 0.250 | 0.108 |
| cut error: R | 0.035 | 0.183 | 0.107 |
| cut error: FR | 0.030 | 0.207 | 0.120 |
| cut error: FR-oracle | 0.039 | 0.006 | 0.077 |
| cut error: R-int | 0.042 | 0.149 | 0.050 |
| pulse error: F (exo) | 0.040 | 0.000 | 0.015 |
| pulse error: F (con) | 0.055 | 0.050 | 0.039 |
| pulse error: R | 0.015 | 0.037 | 0.028 |
| pulse error: FR | 0.016 | 0.037 | 0.028 |
| pulse error: FR-oracle | 0.015 | 0.013 | 0.013 |
| one-step R²: F-raw / F-self / R / FR | 0.18 / 0.33 / 0.37 / 0.37 | 0.24 / 0.42 / 0.44 / 0.44 | 0.23 / 0.40 / 0.43 / 0.43 |
| mean off-diagonal coupling, R (truth) | 0.017 (0.017) | 0.014 (0) | 0.016 (0.009) |

1. **The features do not beat the null.** Under a null matched on
   within-group correlation the feature model finds more overlapping
   features than under coupling, and they match the working groups better.
   A shared driver writes its group into every member's activity at once,
   which is the form the model's prior is built for; coupling spreads it
   along the graph, cross-group ties included.
2. **Neither reading of the features is right in both worlds.** Read as
   causes of members (exo), the model is exact under the driver and misses
   the whole cut effect under coupling. Read as realized by their holders
   (con), it predicts a cut effect of about −0.25 under the driver, where
   there is none, and about −0.05 under coupling, where it is −0.29. Which
   reading holds is what the allocation was to tell, and it cannot.
3. **The graph alone is right where the coupling is real and invents it
   where it is not.** Under coupling R recovers the coupling (0.017 against
   0.017) and predicts the cuts to 0.035. Under the driver it finds almost
   as much coupling (0.014, truth 0) and predicts a cut effect of −0.18.
   The persistent driver makes contacts' past activity predict a member's
   next, which is what a restricted VAR reads as influence.
4. **Adding the features does not fix it; observing the driver does.**
   FR's cut error under the driver is 0.21, no better than R's. With the
   true drivers observed, the invented coupling halves (0.007)
   and the cut error falls to 0.006. The
   features estimate the drivers too noisily, from four to six members
   each, to take their place.
5. **Observational fit does not discriminate.** One-step R² ranks
   R ≥ FR > F-self > F-raw in all three worlds.
6. **The interventional fit helps in part.** R-int, fitted with shocks to
   half the members, improves the cuts in the mixed world (0.050 against
   0.107) and less under the driver (0.149 against 0.183); for the
   unshocked members its pulse predictions are no better than R's.

The planted-feature test of the sampler (test_study.py) also shows
[CASE-165](CASE-165.md)'s item 4 directly: three planted features came back as
fourteen occupied columns, among them exact copies, splits and unions of the planted
ones, with the member noise estimated near its true value (about 0.22
against 0.25).

## What it can show

In this family the answer to [LEAD-144](../leads.d/LEAD-144.md)'s test is no: features under the
finite Indian buffet prior do not beat the shared-driver null, and with the
communication graph they do not predict held-out interventions better than
the graph alone. The one thing they do track, a residual left beside the
graph, is larger under the driver than under coupling: what survives the
relational model here is the common cause, not the interaction. That is
the reverse of reading a surviving feature as a perspective. And the
question's condition (iii) has a second difficulty it does not name: the
relational baseline is itself confounded by a persistent driver, so beating
it is not enough; in a driver world it is wrong too.

## What it cannot show

- Anything beyond one linear-Gaussian family with scalar activity, one
  size (24 members, six groups, 600 days), one coupling strength and one
  driver persistence. A nonlinear simulator, typed messages, team records
  or the authorization layer of [CASE-165](CASE-165.md) §7–8 were not built; the
  question's "authorization relations" were left out.
- That no feature procedure could do better. FR is a two-stage fit. A
  joint state-space fit, with the features as latent persistent drivers
  smoothed over time beside the graph's coupling, was not run, and is the
  natural next arm: the oracle shows the ceiling it would aim at.
- That the full dynamic model of [CASE-165](CASE-165.md) (a sticky allocation that moves,
  per-member activations, social and team terms in the transition) would
  behave like the static allocation fitted here.
- That any firm's members hold such features.
