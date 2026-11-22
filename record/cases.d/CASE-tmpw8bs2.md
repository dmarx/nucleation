---
status: Proposed
title: 'A simulated engagement laboratory in two worlds, one with genres planted in preferences and one where exposure alone makes the clusters, and five arms: engagement under randomized exposure stayed flat when the inferred classes steered exposure over fixed preferences, rose when they steered it while users and creators adapted, and fell when the same adaptation ran without them; concentration, fit to raw counts and stability rose with use alone and were highest for the exposure-made clusters'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-030 as a delegated
    lead worker. Code, results and a README are committed under
    scratch/studies/lead-030/.
standing: documented
kind: executed-study
tags:
- network-science
- social-science
- individuation
date: '2026-11-22'
line:
- formal-apparatus
- distributed-agency
bears_on:
- QUESTION-028
- QUESTION-276
- QUESTION-113
draws_on:
- THEORY-2054
summary: >-
  CASE-296's laboratory, run for LEAD-030 as a numpy simulation: 600 users,
  400 items, engagement given exposure, classes inferred once from five
  burn-in periods by degree-normalized spectral co-clustering and held
  fixed, then fifteen periods under one of five arms, four seeds each. In
  the world with planted genres, the in-class minus out-of-class engagement
  rate under uniform random exposure went from 0.35 to 0.36 when the classes
  steered exposure over fixed preferences, to 0.48 when they steered it while
  users and creators adapted, to 0.23 under the same adaptation without
  them, and to 0.14 when exposure followed popularity. Share of engagement
  inside the class rose from 0.42 to 0.90 whenever the classes were used. In
  the world where exposure alone made the clusters, inference recovered the
  exposure communities exactly, stability was 1.00 and fit to raw counts was
  higher than for planted genres, while the random-exposure gap was 0.00; it
  rose to 0.024 only when the classes were used with adaptation. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-296 CLAIM-762 THEORY-2054 — Proposed; the case this study runs, the claim it was filed for, and the reading behind degree correction -->
<!-- inactive-ok-file: CLAIM-tmph4j0u CLAIM-tmpvn59f — new; the claims filed from this study -->

# CASE-tmpw8bs2: A simulated engagement laboratory in two worlds, one with genres planted in preferences and one where exposure alone makes the clusters, and five arms: engagement under randomized exposure stayed flat when the inferred classes steered exposure over fixed preferences, rose when they steered it while users and creators adapted, and fell when the same adaptation ran without them; concentration, fit to raw counts and stability rose with use alone and were highest for the exposure-made clusters

## The case

Run on 2026-11-22 for LEAD-030, building the laboratory CASE-296
specifies, with its closure test and its intervention arm. Code, results
(scratch/studies/lead-030/results.md, from results.jsonl) and a README
saying how to rerun are on the branch claude/lead-030-genres-laboratory.
Ten unit tests pass. Forty runs: two worlds, five arms, seeds 0 to 3.

**The model.** 600 users and 400 items carry 8-dimensional preference
vectors; a user shown an item engages with probability
sigmoid(−2 + u·v + β), β an item's popularity; 30 exposures per user per
period, sampled without replacement by weight. A missing engagement is
never read as a dislike: every model below is fitted on exposed pairs.

- **World "taste".** Vectors drawn around six centres (between-centre sd
  0.6, within 0.3): genres and audiences exist in the preferences.
  Exposure is weighted by popularity and otherwise unstructured.
- **World "exposure"** (CASE-296's negative control). Vectors with the
  same spread and no clusters; exposure is channelled through six
  communities, weight 0.08 outside one's own, as a language or a
  promotion slot would.

**Classes.** Inferred once, from the raw engagement counts of five
burn-in periods under the base policy, by regularized degree-normalized
spectral co-clustering with K = 6, then held fixed, as CASE-296's
intervention arm holds the classification fixed. Each audience's target
genre is the one its degree-corrected block rate is highest for. Degree
correction follows Larremore, Clauset and Jacobs (THEORY-2054): without
it, the model "tends to sort vertices by degree".

**Arms**, fifteen periods each.

1. *Inferred*: the base policy continues; preferences fixed.
2. *Inferred + adapt*: the base policy; users move 10% a period toward
   the mean of the items they engaged with, and creators replace the 3%
   least-engaged items by noisy copies of engaged ones. This arm is not in
   CASE-296. It is the control the lead's criterion needs, "reshape
   preferences only when used".
3. *Used*: exposure weighted 20:1 toward the user's target genre;
   preferences fixed.
4. *Used + adapt*: arm 3 with arm 2's adaptation.
5. *Popular + adapt*: exposure weighted toward the last period's most
   engaged items, with adaptation, where erasure was expected.

**Measures**, at the end of burn-in and at the end.

- *Concentration*: share of engagements under the arm's policy that fall
  in the user's target genre.
- *Random-exposure gap* (the intervention arm): each user is shown 20
  items uniformly at random, which changes nothing; in-class minus
  out-of-class engagement rate.
- *Closure* (CASE-296's test, the assistant's): a degree-corrected class
  logistic model against a rank-8 ridge factor model, both fitted to the
  last five periods plus a second random probe, scored on held-out random
  exposure. The score is the share of the factor model's gain over the
  degree-only model that the classes keep; the defect is the factor
  model's held-out log-likelihood minus the class model's. Controls:
  partitions with the same sizes by popularity, and co-clusters of the
  exposure matrix.
- *Raw gain*: the same comparison not conditioned on exposure, a
  degree-corrected Poisson block model against the degree-only model on
  the next period's raw counts, in millinats per user-item cell.
- *Stability*: adjusted Rand index of classes re-inferred from the last
  five periods against the fixed ones.
- *Ground truth*, which a real study lacks: the true in-class gap in
  engagement probability, and the within-class spread of true preferences.

## Results

Means over four seeds, range in brackets.

**Inference and the closure test at burn-in.**

- In the taste world the classes matched the planted genres with ARI 0.58
  [0.46, 0.81] for users; the closure score was 0.86 [0.79, 0.93], against
  0.01 for the popularity partition and 0.00 for the exposure partition.
- In the exposure world the classes matched the exposure communities
  exactly (ARI 1.00), and so did the exposure partition. The closure score
  was −0.01, the same as both controls.
- The raw gain ranked the worlds the other way: 9.6 millinats for the
  exposure-made clusters against 3.7 for the planted genres, with the
  exposure partition equal to the genre partition (9.6) and the popularity
  partition 0.0.
- Inference from the residual of engagement given exposure, run beside it
  as a variant, matched the planted genres with ARI 0.72 and the exposure
  communities with 0.04.

**Start to end, by arm.**

| world | arm | concentration | random-exposure gap | true gap | raw gain | stability (users) |
|---|---|---|---|---|---|---|
| taste | inferred | 0.42 → 0.40 | 0.352 → 0.357 | 0.344 → 0.344 | 3.7 → 3.6 | 0.49 |
| taste | inferred + adapt | 0.42 → 0.33 | 0.352 → 0.231 | 0.344 → 0.217 | 3.7 → 1.9 | 0.24 |
| taste | used | 0.42 → 0.90 | 0.352 → 0.357 | 0.344 → 0.344 | 24.5 → 41.1 | 0.89 |
| taste | used + adapt | 0.42 → 0.90 | 0.352 → 0.482 | 0.344 → 0.466 | 24.5 → 49.0 | 0.84 |
| taste | popular + adapt | 0.42 → 0.26 | 0.352 → 0.142 | 0.344 → 0.132 | 3.2 → 0.8 | 0.32 |
| exposure | inferred | 0.67 → 0.67 | 0.005 → −0.002 | 0.000 → 0.000 | 9.6 → 9.7 | 1.00 |
| exposure | inferred + adapt | 0.67 → 0.68 | 0.005 → 0.005 | 0.000 → 0.012 | 9.6 → 10.2 | 1.00 |
| exposure | used | 0.67 → 0.97 | 0.005 → −0.002 | 0.000 → 0.000 | 19.9 → 24.4 | 1.00 |
| exposure | used + adapt | 0.67 → 0.98 | 0.005 → 0.024 | 0.000 → 0.020 | 19.9 → 26.4 | 1.00 |
| exposure | popular + adapt | 0.67 → 0.19 | 0.005 → −0.001 | 0.000 → 0.001 | 5.9 → 0.0 | 0.02 |

The raw gain's starting value differs by arm because it is scored on a
draw of each arm's own policy. The random-exposure gaps of "inferred" and
"used" agree to every digit because the runs share random numbers and the
preferences did not move. The used + adapt gap in the exposure world lay
in [0.015, 0.034] across seeds, against [0.000, 0.012] for inferred + adapt.

**The closure defect under adaptation.** At the end, the defect on random
exposure was positive in the arms with fixed preferences (0.010 and 0.011
nats per observation in the taste world) and negative in every adaptive
arm, used or not (−0.013 to −0.022), where the score left [0, 1].
Adaptation shrank the within-class spread of true preferences to between
0.07 and 0.15 of its start in every adaptive arm, and the class model then
beat the factor model fitted on stale data.

## What it can show

1. **The three kinds of class come apart, and only under randomized
   exposure.** Use with fixed preferences moved concentration (0.42 to
   0.90), raw gain and stability, and left the random-exposure gap exactly
   where it was. Use with adaptation moved all of these and the gap
   (0.35 to 0.48), and the true gap moved with it. Adaptation without use
   lowered the gap (to 0.23). So in this model the classes reshape
   preferences only when used, which is what LEAD-030 says would count
   for CLAIM-762's reading. Filed as CLAIM-tmph4j0u.
2. **A's three outcomes all occurred.** The loop *reinforced* planted
   genres (taste, used + adapt). It *created* a small distinction where
   there had been none (exposure, used + adapt: gap 0.024, true gap 0.020,
   between-class share of preference variance 0.01 to 0.16). It *erased*
   one when exposure followed popularity (taste, popular + adapt: gap 0.35
   to 0.14, item classes no longer recoverable, ARI −0.01).
3. **Fit and stability favour the wrong classes.** The exposure-made
   clusters fitted raw counts better than planted genres and were perfectly
   stable; planted genres were stable (0.89) only when used. Conditioned on
   exposure and tested on random exposure, CASE-296's closure test passed
   the planted genres and failed the exposure-made ones, and its control
   partition caught the confound in both forms. Filed as
   CLAIM-tmpvn59f.
4. **The closure defect does not separate the third kind from adaptation
   in general.** It turned negative wherever preferences homogenized within
   classes, with or without use. It registers homogenization within classes;
   the random-exposure gap registers separation between them.

## What it cannot show

The mechanisms were written into the simulator: users who drift toward
what they engage with, and a recommender that channels exposure. The
laboratory shows that the measures can tell the cases apart when the
cases are known, not that real genres are reshaped. It cannot show what
the owner's earlier analysis of real data showed (CASE-296). Creation was
small in fifteen periods and was not run longer. Classes were inferred
once with K fixed at the planted number; re-inference during the run,
choice of K, and A27 §5's self-supervised arm were not run. "The cost of
the task" was read as the closure defect and the engagement yield, and
not modelled further. Three settings (the genres' separation, the
burn-in length and the factor model's ridge) were chosen once, on seeds 1
and 2, before the runs (scratch/studies/lead-030/README.md).
