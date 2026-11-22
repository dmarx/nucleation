---
status: Proposed
title: 'Checking a restricted theorem on differentiated, recoverable specialists numerically: the recovery bound holds in 7,981 random removals, with equality whenever no other component goes extinct; Gaussian-niche operators started almost identical differentiate to equilibria meeting the stability conditions; and in a two-resource trade-off a removed specialist fails to return exactly where the lone resident leaves its corner for a generalist that takes more than its share'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-049 at the
    coordinator's brief. Scripts, tests, results and a README are under
    scratch/studies/lead-049/.
standing: documented
kind: executed-study
tags:
- ecology
- mathematics
- complex-systems
date: '2026-11-22'
bears_on:
- QUESTION-132
- QUESTION-135
illustrates:
- CLAIM-tmp6kclm
- CLAIM-tmpdsv4t
line:
- distributed-agency
summary: >-
  The numerical check of CLAIM-tmp6kclm and CLAIM-tmpdsv4t, LEAD-049's
  theorem and counterexample. (1) Fixed traits: 2,000 random nonnegative
  7 × k niche matrices, k = 2–6, with 7,981 removals, each −i community
  found exactly. Every recovery rate was positive and at least
  n*_i/(A⁻¹)_ii. It equalled that bound to 10⁻¹⁴ in all 6,315 removals
  without secondary extinction, and exceeded it (median ratio 1.24) in the
  1,666 with one. (2) Gaussian niches on 12 resources: operators started
  10⁻³ apart differentiate, and the stability conditions are checked at
  each endpoint. PART2. (3) A two-resource trade-off, four shapes, c/B
  from 0.1 to 0.9. A lone resident left its corner exactly when
  c/B < a'(0)/a'(1) = 2/3, and it settled at the symmetric generalist.
  The removed specialist then failed to return in every run with
  a(1/2) > 1/2, its growth matching c(1/(2a(1/2)) − 1) to four decimals.
  With a(1/2) < 1/2 it returned and the pair re-formed. Where the
  resident stayed put, the specialist returned at B − c in every run.
  Simulated, at one integration step and finite horizons. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp6kclm CLAIM-tmpdsv4t — new, filed with this case by LEAD-049 -->

# CASE-tmp5sk3q: Checking a restricted theorem on differentiated, recoverable specialists numerically: the recovery bound holds in 7,981 random removals, with equality whenever no other component goes extinct; Gaussian-niche operators started almost identical differentiate to equilibria meeting the stability conditions; and in a two-resource trade-off a removed specialist fails to return exactly where the lone resident leaves its corner for a generalist that takes more than its share

## What was done

LEAD-049 asks for a restricted theorem and a check of it. The theorem
and the model class are CLAIM-tmp6kclm, and the counterexample is
CLAIM-tmpdsv4t. The code is scratch/studies/lead-049/: `model.py`,
`study.py`, `generalist_check.py`, `condC_check.py`, and 14 pytest tests
in `test_model.py`, all passing. Integration is RK4 in (log n, θ) with
dt = 0.02, and the trait is clipped to its box after each step.

**Part 1: Theorem B at fixed traits.** There were 2,000 random
nonnegative niche matrices U (7 × k, k = 2–6, entries uniform squared)
with an interior equilibrium n* drawn uniformly. Each −i community was
found exactly by support enumeration.

- All 7,981 recovery rates were positive and at least n*_i/(A⁻¹)_ii.
- In the 6,315 removals without a secondary extinction they equalled it,
  to within 2.4 × 10⁻¹⁵.
- In the 1,666 with one, the bound was strict. The ratio was at least
  1.00001, with median 1.24.
- The bound n*_i d_i² exceeded the spectral bound n*_i λ_min(A) by a
  median factor of 3.2.

In 30 removals the −i community and the reinvasion from 10⁻⁶ were also
simulated. The simulated recovery rates matched the exact ones within
5 × 10⁻⁴. The returning component regained at least 95% of its former
abundance within the horizon. The slowest systems had not fully settled:
the largest distance from n* was 0.21.

**Part 2: Theorems A and C from near-identical starts.** PART2DETAIL

**Part 3: the counterexample.** Two resources with B = 1 and the
specialist pair at θ = (1, 0). Four trade-off shapes:
a(t) = t + t(1 − t)(α + βt) + γt²(1 − t)², with
(α, β, γ) = (0, −½, 0), (0, −½, 1.5), (0, −½, 3) and (0.2, −1, 4).
Then a(1/2) = 0.44, 0.53, 0.63 and 0.68, and a'(0)/a'(1) = 2/3 for all
four. c/B ran from 0.1 to 0.9. Each run removed operator 2, let operator
1 adapt alone for T = 300, then reintroduced operator 2 at 10⁻⁶ with its
old trait for T = 400.

- Theorem A held at the pair in all 36 runs.
- The lone resident left its corner in exactly the runs with
  c/B < 2/3, as the margin a'(1)c − a'(0)B predicts. It always settled at
  θ = 1/2.
- There, the specialist's growth matched c(1/(2a(1/2)) − 1) to four
  decimals.
- In the 18 runs with a(1/2) > 1/2 and c/B < 2/3, the growth was
  negative (−0.006 to −0.156). The specialist did not return.
- With a(1/2) = 0.44 it was positive, and the specialist grew. For
  c/B ≥ 0.3 the resident re-specialized and the pair re-formed at
  (B − c, B − c) within the horizon. At 0.1 and 0.2 growth was still
  under way.
- Where c/B ≥ 2/3 the resident stayed at its corner, and the specialist
  returned at rate B − c.

`generalist_check.py` confirms that the lone generalist meets Theorem A
wherever its abundance is positive. So for the three shapes with
a(1/2) > 1/2 and c/B ≥ 2/3, the system has two stable states, the pair
and the lone generalist, and removal does not lead to the second.

## What it shows

It shows that the theorem's inequalities and the counterexample's
formulas hold where they were computed. It also gives what the proofs do
not: the trajectory after removal. In the trade-off the lone resident
ends at the generalist whenever it leaves its corner. In the Gaussian
niches, PART2SHOWS.

## What it cannot show

The study covers one niche family per part, finite horizons, and one
integration step size. The trade-off runs say where the resident went
from one starting point, not the whole basin structure. Nothing here
tests asymmetric interactions, delayed adaptation or a trainable
returning specialist.
