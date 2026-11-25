---
number: 334
status: Proposed
formerly:
- CASE-tmpwyp15
title: 'Block test on a phi4 kink and Kuramoto cluster'
statement: >-
  Compensation, entrainment and the block test measured by computation in
  two closed modes that are not blocks, the kink of a phi4 lattice and the
  locked cluster of a uniformly coupled Kuramoto population, beside a
  two-block control: the members compensate in all three, the cluster's
  entrain, and the block test on members singles out only the control
version: 1
standing: documented
kind: executed-study
tags:
- individuation
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-218
- QUESTION-035
summary: >-
  [LEAD-083](../leads.d/LEAD-083.md)'s study. Three arms share one protocol: [CLAIM-157](../claims.d/CLAIM-157.md)'s block test
  on the members, compensation read as in a jaw-load experiment (a
  sustained load on a few members, the form's task variable read with the
  others free and with them frozen), and entrainment read as [CLAIM-172](../claims.d/CLAIM-172.md)
  reads it, by timing. In the kink of an overdamped phi4 lattice the sites
  within about one unit of its centre compensate fully, and the set that
  compensates moves with the kink. Coupling between sites is uniform, and
  the best block ratio of a segment holding the kink falls as the square
  of the lattice spacing, from 1.57 to 0.11. In a Kuramoto population with
  uniform coupling, the 156 locked oscillators of 200 compensate (0.97)
  and entrain (0.91), and on the coupling constants every subset of 156
  scores exactly as they do. A two-block control compensates and entrains
  inside each block and not across, and is the only form the test picks
  out. The study and its wording are the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 CASE-269 CASE-266 — Proposed; the criterion tested and the testbed whose kink is used -->
<!-- inactive-ok-file: LIT-902 — Unavailable; cited for the design of the compensation test, which is described here in full -->

# CASE-334: Block test on a phi4 kink and Kuramoto cluster

## The case

**What was asked.** [LEAD-083](../leads.d/LEAD-083.md): find or simulate a closed mode that is not a
gap-isolated block, perturb it, and measure whether it compensates and
entrains. [QUESTION-218](../questions.d/QUESTION-218.md): "If the mode compensates and entrains and the
block test misses it, that meets [CLAIM-157](../claims.d/CLAIM-157.md)'s `defeated_if`". Its
`defeated_if` names "forms that do compensate and entrain but never clear
it".

**Why these models.** Each is the simplest that has the property the
question needs.

- **A, a field excitation.** The φ⁴ kink is the simplest localized
  excitation of a nonlinear field, and it is the first model of
  [CASE-269](CASE-269.md)'s testbed ([CASE-266](CASE-266.md)). Overdamped dynamics,
  ∂ₜφᵢ = (φᵢ₊₁ − 2φᵢ + φᵢ₋₁)/h² + φᵢ − φᵢ³, on [−20, 20], with φ = −1
  and +1 at the walls, at lattice spacings h = 1, 0.5 and 0.25. Every
  site is coupled to its neighbours with the same strength 1/h², so no
  grouping of sites is set off by coupling. The kink is the unit as a
  function of the whole field, not as a set of sites.
- **B, a collective mode with an environment.** Kuramoto phase
  oscillators with uniform all-to-all coupling K/N, N = 200, K = 1.9,
  natural frequencies at the quantiles of a unit Gaussian. It is the
  nonlinear twin of [CLAIM-388](../claims.d/CLAIM-388.md)'s uniform coupling, with the difference
  the question needs: only part of the population locks, so the form is
  a proper part of the system, and it has timing, which [CLAIM-172](../claims.d/CLAIM-172.md)'s
  entrainment needs. 156 oscillators lock (mean frequencies within
  7 × 10⁻⁴ of each other); 44 drift.
- **C, a block control.** Two clusters of 50 oscillators, coupling 4/N
  inside and 0.1/N across, centred at frequencies ∓1.5. Both clusters
  lock.

**The measures.**

- **Block test ([CLAIM-157](../claims.d/CLAIM-157.md)).** For a group G of members, δ is the gap
  between the two slowest modes of G's own linearized dynamics, ε the
  larger spectral norm of the coupling into and out of G, and ρ = δ/ε.
  The entrywise ratio is the mean coupling inside over the mean across.
  The Occam threshold τ is not set for these models, so ρ is reported
  and compared with other groups. For B and C the interaction matrix is
  read three ways: the coupling constants, the realized Jacobian
  Kᵢⱼ cos(θⱼ − θᵢ) averaged over 200 time units, and its absolute value.
- **Compensation**, after the jaw-load design that [CLAIM-157](../claims.d/CLAIM-157.md) cites
  ([LIT-902](../literature.d/LIT-902.md)). A few members S are held displaced, the load sustained.
  A task variable T of the form is read with the other members free and
  with them frozen at their unloaded states.
  κ = (T_free − T_frozen)/(T_base − T_frozen) is the share of the load's
  damage that the other members undo: 1 is full compensation, 0 none,
  and a negative value means the others' response took the state further
  from the form. For the kink, one site is displaced by ±0.3 and T is
  minus the distance to the declared family of kinks
  tanh((x − X)/√2) over X ([CASE-269](CASE-269.md)'s declared family). For B and C,
  five members are displaced by 0.8 rad and T is the phase coherence of
  the form.
- **Entrainment**, in [CLAIM-172](../claims.d/CLAIM-172.md)'s sense that "each side's timing shifts
  with the other's". Five members are detuned by 0.2, and the shift of
  mean frequency of those five and of the rest of the form is read.

**Method.** NumPy and SciPy, run on 2026-11-22. Code, six passing tests
and the per-item results are in `scratch/studies/lead-083/` (`study.py`,
`test_study.py`, `results.jsonl`, `summarize.py`).

## Results

**1. The kink is a closed mode not found by grouping sites.** Its
linearization has a translation mode at 0.04, 0.00 and 0.00 (h = 1, 0.5,
0.25), then the shape mode at 1.40, 1.49 and 1.50 and the continuum from
2. The translation mode is spread over about 2.7 units of length at every
spacing. So the slow subspace is set off by a gap in the eigenbasis of
the whole field, while every pair of neighbouring sites is coupled
equally.

**2. The kink's members compensate, and which members do moves with
it.** κ by distance from the kink's centre, mean over the two signs of
load, at t = 50:

| h | κ at distance d from the centre |
|---|---|
| 1 | d = 0.5: 1.10; 1.5: 0.82; 2.5: 0.58; 3.5: 0.52; 4.5 and beyond: −0.09 |
| 0.5 | d = 0.25–0.75: 1.00; 1.25: 0.89; 1.75: 0.65; 2.25–3.25: 0.50 to 0.39; 3.75: −0.04; 4.25 and beyond: −0.31 |
| 0.25 | d = 0.12–0.88: 1.00; 1.12–1.38: 0.93 to 0.76; 1.62–1.88: 0.59 to 0.47; 2.12–3.62: 0.37 to 0.01; 3.88 and beyond: −0.66 to −0.74 |

A value above 1 means the loaded field fits the continuum family better
than the unloaded lattice kink did. At t = 5 the core is the same (κ 0.97 to 1.04 within 0.5 of the centre)
and the compensating set narrower.
The others compensate by moving the whole kink: a load on a core site
shifts its centre by 0.44 to 0.51, and the kink settles where the loaded
value fits it. A load in the vacuum is answered by the neighbours
healing it locally, which takes the field further from any kink, so κ is
negative there. With the kink started at 6 instead of 0, the sites with
κ > 0.5 at t = 5 are [5.25, 7.25] instead of [−0.75, 1.25] (h = 0.25),
the same profile shifted by 6. The set of members that compensate is
replaced when the kink moves.

**3. The block test on sites does not single the kink out.** Entrywise,
inside and cross coupling are equal for every segment (ratio 1). The
largest ρ for segments of a given length that contain the kink, against
segments of the same length more than 5 units from it:

| length | 2 sites | 1 | 2 | 4 | 8 | 12 |
|---|---|---|---|---|---|---|
| h = 1 | 2.51 / 2.00 | | 2.51 / 2.00 | 1.66 / 1.00 | 1.57 / 0.35 | 1.56 / 0.17 |
| h = 0.5 | 2.01 / 2.00 | 2.01 / 2.00 | 1.07 / 1.00 | 0.52 / 0.35 | 0.43 / 0.10 | 0.43 / 0.05 |
| h = 0.25 | 2.00 / 2.00 | 1.01 / 1.00 | 0.36 / 0.35 | 0.14 / 0.10 | 0.11 / 0.03 | 0.11 / 0.01 |

Any two neighbouring sites score about 2 wherever they are, since their
own coupling makes the gap. A long segment holding the kink scores its
shape-mode gap over 1/h², about 1.5h². On the coarsest lattice the kink's
segments beat the vacuum's at lengths of 4 and more and clear τ = 1.
At h = 0.5 and 0.25 only segments of at most four sites clear τ = 1, and
vacuum segments of the same size score within 7% of them. As the lattice approaches the field, the test's verdict on the kink
goes to zero while its compensation does not change.

**4. The Kuramoto cluster compensates and entrains, and the coupling
constants do not pick it out.**

| | B, locked cluster | C, block (control) |
|---|---|---|
| form size, coherence | 156 of 200, 0.83 | 50 of 100, 0.97 |
| κ, load on 5 members | 0.97 | 1.00 |
| detune 5 members by 0.2: their shift, the rest's | 0.0107, 0.0097 | 0.0206, 0.0201 |
| rest's shift over theirs | 0.91 | 0.97 |
| detune 5 outside the form: the form's shift | −0.004 (drifting members) | 0.0001 (other block) |
| ρ on coupling constants: form, random sets of its size | 1.88; 1.88–1.88 | 40; 0.05–0.57 |
| ρ on realized Jacobian: form, random | 0.81; 0.19–0.28 | 10,781; 0.002–0.58 |
| ρ on its absolute value: form, random | 1.46; 1.20–1.30 | 46.7; 0.03–0.58 |
| entrywise, coupling constants / realized | 1.0 / 3.3 | 40 / 14,447 |

The five detuned members are held by the rest (they move 5% of their
detuning) and pull the rest with them by nine tenths as much as they move. Drifting
oscillators detuned the same way shift by 0.29 and move the cluster by
nothing measurable. On the coupling constants, ρ for the cluster is
√(156/44), and every subset of 156 oscillators has the same value: the
test cannot tell the cluster from any other set of its size. On realized
interaction the cluster stands out, three times the random sets on the
signed reading and slightly on the absolute one, but on the signed
reading it does not clear τ = 1. In the control, every reading picks out
the block by a factor of 70 or more.

## What it can show

- A form can compensate under a sustained load as fully as a block does
  (κ near 1 in all three arms) without being a block of its members.
- In the kink, the members that compensate are fixed by where the kink
  is, not by how the sites are coupled. They change as it moves, so no
  grouping of sites is the unit over time. That is [QUESTION-218](../questions.d/QUESTION-218.md)'s "a
  function of the whole state", measured.
- The block test's verdict on a member grouping depends on what the
  members are. On a lattice it falls as h², so in the continuum limit
  the block test misses the kink.
- In B, compensation and entrainment pick out the locked cluster, which
  the coupling constants do not distinguish from any set of its size.
  Whether the block test misses it depends on reading interaction as
  realized and on τ, which the record has not set.

## What it cannot show

- **That either mode is one system.** It measures the independent marks
  [QUESTION-218](../questions.d/QUESTION-218.md) asks for. It does not say they suffice.
- **That compensation here is more than relaxation to an attractor.** In
  a gradient system the free members always lower the energy; κ counts
  only what restores the declared form, and it is negative in the
  kink's vacuum. A form declared differently would give other numbers.
- **Entrainment in the kink.** An overdamped kink has no timing, so
  [CLAIM-172](../claims.d/CLAIM-172.md)'s test has no observable there. What it has instead is
  co-movement: a load on one core site moves the whole kink by about
  0.45 to 0.5. That absence is recorded, not filled in.
- **Exact closure of the cluster.** The Ott–Antonsen reduction closes the
  mean field exactly only for infinitely many oscillators with
  Lorentzian frequencies; for 200 Gaussian ones closure is approximate
  and was not measured. The kink's closure is the gap in its
  linearization, not a measured transfer entropy.
- **The systematic failure [CLAIM-157](../claims.d/CLAIM-157.md)'s `defeated_if` asks for.** These
  are two cases, each one parameter setting, with one load size and one
  reading of each measure. No noise was added.
- **A flux arm.** [QUESTION-219](../questions.d/QUESTION-219.md)'s organized throughput was not simulated.
- **Why "documented".** Every number is a computation any reader can
  repeat from the code.
