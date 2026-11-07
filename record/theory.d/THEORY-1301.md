---
number: 1301
status: Active
formerly:
- THEORY-tmp100uk
title: 'In the Haken–Kelso–Bunz potential V(φ) = −a cos φ − b cos 2φ, switching the parameters in time from no landscape (a = b = 0) to two wells (a = b = 1) to one well (a = 1, b = 0) makes the spread of the relative phase across trials rise while both wells are open and fall after one is removed, the pattern Sánchez-Cañizares compares qualitatively with post-stimulus quenching of trial-to-trial variability in decision tasks; under Gaussian white noise of the stated strength q = 1 the spread of cos φ settles near 0.40, not at 0'
version: 1
tags:
- complex-systems
- neuroscience
date: '2026-11-03'
source:
- LIT-1992
- LIT-588
summary: >-
  Sánchez-Cañizares (2026), [LIT-1992](../literature.d/LIT-1992.md), read in full in [NOTE-1506](../notes.d/NOTE-1506.md)
  from the publisher's open-access PDF. Active for the model's behaviour,
  which this reading checked: the bistability condition |a| < 4b
  analytically, and the rise and fall by re-simulation (20,000 paths). The
  paper's statement that the spread decreases "to 0" holds without noise
  and fails at q = 1. It does not say that the model fits the cited EEG
  data, which the author calls "only qualitative", or that the parameter
  changes are the mind's ([THEORY-1302](THEORY-1302.md)).
---
<!-- inactive-ok-file: THEORY-1302 — Proposed; the interpretation filed beside this, cited as open -->

# THEORY-1301: In the Haken–Kelso–Bunz potential V(φ) = −a cos φ − b cos 2φ, switching the parameters in time from no landscape (a = b = 0) to two wells (a = b = 1) to one well (a = 1, b = 0) makes the spread of the relative phase across trials rise while both wells are open and fall after one is removed, the pattern Sánchez-Cañizares compares qualitatively with post-stimulus quenching of trial-to-trial variability in decision tasks; under Gaussian white noise of the stated strength q = 1 the spread of cos φ settles near 0.40, not at 0

## Source

Sánchez-Cañizares (2026), [LIT-1992](../literature.d/LIT-1992.md), §4 (PDF pp. 7–12) and §5
(pp. 13–18); read in [NOTE-1506](../notes.d/NOTE-1506.md). The potential is Haken, Kelso and Bunz
1985 ([LIT-588](../literature.d/LIT-588.md); [THEORY-1227](THEORY-1227.md)).

## What was actually shown

**The landscape (p. 8).** φ̇ = −a sin φ − 2b sin 2φ. With b = 1 there are
minima at 0 and π for |a| < 4 and one minimum otherwise. Checked: V″ = a cos
φ + 4b cos 2φ is positive at π iff a < 4b, which is [THEORY-1227](THEORY-1227.md)'s anti-phase
boundary.

**The schedule (eq. 3, p. 8) and the statistics (eqs. 4–7, p. 11).** Means
and standard deviations of φ and cos φ over φ(0) uniform on (−π, π], with
noise √q ξ and q = 1. Fig. 3 shows the standard deviations bump in
1 ≤ t < 2 and decrease afterwards.

**Re-simulated here** (Euler–Maruyama, dt = 10⁻³, 20,000 paths). The SD of
cos φ:

| t | 0.99 | 1.5 | 1.99 | 5 | 10 | 15 |
|---|---|---|---|---|---|---|
| q = 0 | 0.71 | 0.93 | 0.98 | 0.82 | 0.12 | 0.01 |
| q = 1 | 0.71 | 0.87 | 0.89 | 0.48 | 0.40 | 0.41 |

At q = 1 the late values are the stationary ones of p(φ) ∝ exp(2a cos φ/q)
with a = 1: mean of cos φ 0.698, SD 0.405. So the rise and fall is robust,
and the fall "to 0" (p. 12) needs noise much weaker than q = 1 Gaussian
white noise. The paper's noise is underspecified (bounded ξ ∈ [−1, 1] and
delta-correlated, pp. 8–9), which may explain the difference.

**The comparison (§5).** Visual, against reproduced figures from Sergent et
al. 2021 (SD of the ERP peaking around 400–500 ms at the critical SNR),
Wolff et al. 2019 (trial-to-trial variability peaking near 100 ms and
declining after 200 ms) and, by re-mapping the initial regime, Hua et al.
2025. Two mismatches are stated: the ERP returns to baseline faster than
the model, and at low SNR the experimental SD is smaller (p. 15, fn. 17).

## What this does not say

- That HKB fits the data: no parameter was fitted, and the author says the
  agreement is "only qualitative" (p. 18).
- That the trial-to-trial variability in the experiments arises from
  spread of initial conditions, as the model's statistics do.
- Anything about the mind. That is [THEORY-1302](THEORY-1302.md).

## Note of 2026-11-07: the potential with a maintained parameter, from "Individuation, Possibility, and Disposition"
<!-- inactive-ok-block: CASE-tmpn5x96 — filed from the same exchange, Proposed -->

In the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07; https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e), A29 §3 takes this potential with a = 1, b = c/2 and lets c evolve under its own production and decay ([CASE-tmpn5x96](../cases.d/CASE-tmpn5x96.md)). The barrier against escape from anti-phase is (2c − 1)²/(4c), rechecked by the reader against A's nine chart values. Where this reading switches the parameters by hand, the case has them decline by the system's own maintenance. No change.
