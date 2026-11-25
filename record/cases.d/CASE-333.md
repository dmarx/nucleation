---
number: 333
status: Active
formerly:
- CASE-tmp69rk8
title: 'A simulated network of eight coupled oscillators carrying correspondence maps: a shared drive and coupling give the same phase locking and gluing, but displacing the drive for one member moves the others by 0.2 per cent of its shift without coupling and by 30 to 58 per cent with it; compatibility, attraction, persistence after the drive is withdrawn and revision that predicts interventions come apart across arms'
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-098: the first
    run of CASE-179's design, with A12's three arms and QUESTION-063's
    two interventions. Scripts, tests and results are committed under
    scratch/studies/lead-098/.
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-tmpc0rqa). Rerun by a session other than the filer's from a
    copy of scratch/studies/lead-098/ with its results file set aside:
    every item of results.jsonl agrees with the stored one in every
    field but the timings, and the 8 tests pass; every figure quoted
    in the body was compared and matches. An executed study, with no
    premise of its own; nothing targets it.
standing: documented
kind: executed-study
tags:
- complex-systems
- mathematics
date: '2026-11-22'
line:
- distributed-agency
illustrates:
- CLAIM-474
- CLAIM-471
- CLAIM-616
bears_on:
- QUESTION-063
- QUESTION-035
- QUESTION-319
- QUESTION-282
- QUESTION-283
draws_on:
- THEORY-1088
- THEORY-1090
summary: >-
  [LEAD-098](../leads.d/LEAD-098.md) asked for [CASE-179](CASE-179.md)'s study, with A12's arms, and for
  [QUESTION-063](../questions.d/QUESTION-063.md)'s interventions. Eight Stuart–Landau units on a ring with
  one chord, each edge carrying a phase-offset map, were run in the
  design's regimes. Under a shared drive, uncoupled and coupled networks
  both lock (phase-locking value 0.9985 and 0.9996) and their observed
  offsets glue (holonomy below 10⁻⁴), so timing and gluing cannot tell
  them apart. Displacing the drive of one member by π/2 moves the others
  by 0.2 per cent of that member's shift without coupling, 30 per cent at
  coupling 0.3 and 58 per cent at 1.0; a kick to one member reaches the
  others at 0.010 against 0.12 to 0.14. Withdrawing the drive leaves the
  coupled self-sustained network coherent (order 0.996) and the uncoupled
  one not (0.47). Long suppression of a reciprocally maintained capacity
  becomes atrophy, short suppression does not. Revision by consistency
  reaches coherence without improving prediction; revision checked
  against held-out kicks cuts the held-out error from 1.06–1.81 to
  0.14–0.34. A two-dimensional interior stalk forces a three-way boundary
  relation in 100 of 100 random sheaves. All of it is one model family,
  run once per setting.
---
<!-- inactive-ok-file: CASE-225 — Proposed; the claim and construction this study tests, and the argument that names it -->

# CASE-333: A simulated network of eight coupled oscillators carrying correspondence maps: a shared drive and coupling give the same phase locking and gluing, but displacing the drive for one member moves the others by 0.2 per cent of its shift without coupling and by 30 to 58 per cent with it; compatibility, attraction, persistence after the drive is withdrawn and revision that predicts interventions come apart across arms

## What was run

[CASE-179](CASE-179.md)'s design, made concrete. The choices are the assistant's and are
stated so that a different choice can be compared.

- **Units.** Eight Stuart–Landau oscillators,
  ż_j = (μ_j − u_j + iω_j − |z_j|²) z_j + coupling + F e^{i(Ωt+ψ_j)} + noise,
  with natural frequencies 1 + 0.05·N(0,1) (fixed seed), μ = 0.5
  (self-sustained) or −0.2 (damped), noise σ = 0.002 unless stated.
- **Graph.** A ring of eight with one chord, so two independent cycles.
- **Correspondence maps.** A phase offset θ_jk on each edge: z_j agrees
  with z_k when z_j = e^{iθ_jk} z_k. Compatible maps come from a global
  section (θ_jk = φ_j − φ_k); frustrated maps add holonomy h on the cycle
  through one edge. The apparatus holds its own maps; the coupling
  realizes its own, which may differ.
- **Coupling.** Dissipative: −K·(Lz)_j for the connection Laplacian L of
  the coupling's maps. Conservative: −iK·(Lz)_j, linear and
  norm-conserving. Common drive: F = 0.2 at Ω = 1, with drive phases ψ_j
  equal to the apparatus's section, so that the drive alone realizes the
  apparatus's maps.
- **Higher-dimensional stalks.** Linear cellular sheaves: one interior
  vertex with stalk of dimension 1, 2 or 3 and three scalar boundary
  vertices, random restriction maps, reduced by Kron reduction (the Schur
  complement), as in [THEORY-1090](../theory.d/THEORY-1090.md).
- **Integrator.** Stochastic Heun, dt = 0.01. An intervened copy and its
  control share their noise, so their difference is the intervention's
  effect.

Eight pytest tests check the pieces (holonomy, the twisted Laplacian,
the limit cycle, attraction to a section, norm conservation, recovery of
known gains, the Hansen–Ghrist example, the rank tolerance). The whole
run took about six minutes of one CPU.

## Results: [CASE-179](CASE-179.md)'s regimes

Four initial conditions each; a kick of 1 rad to unit 0 at t = 150 in a
paired copy. "Incompatibility" is the state's normalized distance from
the sections of the named maps (0 on a section).

| regime | apparatus maps glue | incompat. to apparatus maps | to coupling's maps | phase locking | kick to unit 0 after 50 |
|---|---|---|---|---|---|
| compatible, weak (K = 0.005) | yes | 0.86 | 0.86 | 0.70, frequencies spread 0.04 | stays 0.80 |
| compatible, strong, enforcing the maps (K = 1) | yes | 0.0004 | 0.0004 | 1.000 | spread over all, shift 0.08 kept |
| compatible, strong, enforcing other relations | yes | 0.52 | 0.0004 | 1.000 | spread over all, shift 0.10 kept |
| compatible, conservative | yes | 1.16 | 1.16 | 0.32 | no decay (rate 5×10⁻⁵) |
| frustrated, h = 0.8π, strong | no (λ_min 0.129) | 0.063 | 0.063 | 1.000 | spread over all, shift 0.12 kept |
| common drive, no coupling | yes | 0.030 | — | 1.000 | returns; others peak 0.011 |
| common drive, coupling 0.3 | yes | 0.002 | 0.002 | 1.000 | returns; others peak 0.12 |

- **Compatibility without attraction:** the weak and conservative
  regimes, whose maps glue and whose dynamics never reach the sections.
- **Attraction elsewhere:** strong coupling that enforces other relations
  locks fully and is far from the apparatus's sections, as [CASE-179](CASE-179.md)'s
  coupling assumptions say.
- **Organization without a global section:** the frustrated network
  locks into one compromise state, the same from every initial condition
  (spread 10⁻⁵), with residual incompatibility 0.063.
- **Attraction without integration:** the shared drive alone brings the
  uncoupled units within 0.03 of the apparatus's sections.
- **Time scales** ([CLAIM-481](../claims.d/CLAIM-481.md)): the enforcing Laplacian's gap is 0.586 K
  against a frequency spread of 0.05, so at K = 1 the incompatible modes
  decay about twelve times faster than the detuning acts. The measured
  decay of a kick's non-collective part is 0.19 a unit time. In the
  undriven coupled regimes the kick leaves a lasting shift of the
  collective phase (0.08 to 0.12 rad), the collective phase freedom
  A9 named; under drive it returns.

## Results: A12's arms

**Forcing withdrawal** (drive removed at t = 150; coupling 0.3):

| network | order under drive | amplitude after | order after |
|---|---|---|---|
| coupled, self-sustained | 0.999 | 0.70 | 0.996 |
| coupled, damped | 0.999 | 0.002 | (no oscillation) |
| uncoupled, self-sustained | 0.985 | 0.71 | 0.47 |
| uncoupled, damped | 0.995 | 0.003 | (no oscillation) |

Under the drive all four are locked; only the withdrawal tells them
apart. Without coupling the units keep oscillating and lose each other;
with it the network keeps its organization and its phase drifts from the
drive's clock (0.22 rad in 50 time units).

**Suppression** ([CASE-225](CASE-225.md) on the network). Control u = 1 > μ: the
network rests and still answers the drive (amplitude 0.33, order 0.999).
Withdrawing the drive alone, it decays (0.001). Withdrawing drive and
control, the coupled limit cycle returns with order 0.996, the same as
the never-suppressed network.

**Adaptive capacity.** Each μ_j is a slow variable maintained by its
neighbours' activity,
μ̇_j = ε(1.5·a_j/(a_j + 0.2) − μ_j − 0.2), a_j the mean of the
neighbours' |z|², ε = 0.02. It is bistable: maintained at μ ≈ 1.06, or
lost at −0.2.

- Suppression for 20 time units (less than 1/ε = 50) lowers μ to 0.75
  and the network recovers.
- Suppression for 300 lowers μ to −0.2; on release nothing returns.
  Suppression has become atrophy, as A12 said it could.
- Knocking out production in every unit loses the capacity everywhere
  within about 300.
- Knocking it out in unit 0 alone takes its μ to −0.2, but it still
  oscillates at amplitude 0.58, carried by its neighbours; the others
  keep μ ≈ 0.86. Only decoupling (at t = 600) shows the loss: unit 0
  falls to 0.002. Its performance depended on the others once its own
  capacity was gone, and nothing in its output said so.

## Results: [QUESTION-063](../questions.d/QUESTION-063.md)'s interventions

| system | drive of unit 0 displaced by π/2: unit 0 moves | others move (mean) | fraction followed | kick to unit 0: others' peak |
|---|---|---|---|---|
| common drive, no coupling | 1.57 | 0.003 | 0.002 | 0.010 |
| drive and coupling 0.3 | 0.40 | 0.12 | 0.30 | 0.12 |
| drive and coupling 1.0 | 0.23 | 0.13 | 0.58 | 0.14 |
| coupling 1.0, no drive | (no drive) | | | 0.14 |

With coupling, the response falls off with distance from unit 0 (0.16 at
one step, 0.09 at two, at coupling 0.3).

## Which of [QUESTION-035](../questions.d/QUESTION-035.md)'s tests see the difference

On the same systems, with noise σ = 0.03 for the passive tests:

| test ([QUESTION-035](../questions.d/QUESTION-035.md)) | common drive, no coupling | drive and coupling 0.3 | sees it? |
|---|---|---|---|
| mutual entrainment read from timing (phase-locking value) | 0.9985 | 0.9996 | no |
| mutual entrainment by intervention ([CLAIM-172](../claims.d/CLAIM-172.md): each side's timing shifts with the other's) | others follow 0.2 % | 30 % | yes |
| gluing of the observed offsets (holonomy) | 3×10⁻⁵ | 4×10⁻⁶ | no |
| coupling strength fitted from fluctuations, drive unrecorded | 0.068 | 0.356 (true 0.3) | in degree only: a spurious gain, a quarter of the true one |
| the same, drive recorded (pinning to its clock allowed) | −0.001 | 0.272 | yes |
| conserved coherence after the drive is withdrawn | 0.47 | 0.996 | yes, by intervention |

Reciprocal compensation was not given a separate operationalization: the
recovery of the group's coherence after a kick is the same in both, and
whether the others do the restoring is the displacement and kick
readouts above.

## Results: revision ([CASE-179](CASE-179.md)'s third manipulation)

The apparatus predicts each unit's phase response 2, 5 and 10 time units
after a kick of 0.3 rad to one unit. It starts with wrong maps (all
offsets zero), unit gains on every edge and no pinning. Errors are on
held-out kicks to units 4–7, which the apparatus did not choose,
relative to the size of the observed response.

| system | incompatibility, initial maps → maps revised by consistency | error, unrevised | revised by consistency with passive data | checked against held-out kicks |
|---|---|---|---|---|
| common drive, no coupling | 0.63 → 0.00002 | 1.06 | 0.80 | 0.34 (gains fitted 0.001) |
| drive and coupling 0.3 | 0.68 → 0.000002 | 1.42 | 1.41 | 0.17 (gains 0.29) |
| drive and coupling 1.0 | 0.70 → 0.000001 | 1.81 | 1.81 | 0.14 (gains 0.90) |
| coupling 1.0, no drive | 0.70 → 0.000001 | 0.25 | 0.25 | 0.25, rejected as no better |

Revising the maps to the observed offsets makes the apparatus coherent
with what it sees in every system, and changes none of its predictions.
Fitting the coupling to passive fluctuations, drive unrecorded, predicts
that the others follow a kick in the common-drive system (error on the
others 0.029 against an observed response of 0.004). Fitting gains and a
pinning term from kicks the apparatus chose, and keeping the revision
only if it predicts the held-out kicks better, finds no coupling where
there is none and the coupling where there is. Where the initial model
was already near right (the undriven coupled network), the check
rejected the candidate. That is A22 §10's difference between becoming
more coherent and becoming more knowledgeable, in numbers.

## Results: holonomy and plastic maps ([QUESTION-319](../questions.d/QUESTION-319.md), [QUESTION-282](../questions.d/QUESTION-282.md))

One coupling (K = 1, identical frequencies), with holonomy h on one cycle:

| h | λ_min | residual incompatibility | locked |
|---|---|---|---|
| 0 | 0 | 0 | yes |
| π/4 | 0.016 | 0.007 | yes |
| π/2 | 0.060 | 0.027 | yes |
| 0.8π | 0.129 | 0.063 | yes |
| 0.8π, other gauge | 0.129 | 0.063 | yes |
| 0.8π, weak (K = 0.005) | 0.129 | 0.41 | yes |
| 0.8π, plastic maps (η = 0.05) | 0 at the end | 0 | yes |

Gauge-equivalent maps give the same residual (0.06299 against 0.06300),
so the readout follows the holonomy, not the offsets edge by edge. One
connection under strong and weak coupling gives different organizations
with the same holonomy. With fixed maps the holonomy persists by
construction. With maps that adapt to the realized offsets,
θ̇_jk = η sin(arg z_j − arg z_k − θ_jk), the holonomy goes to zero and the
frustration is removed: under that rule the organization treats it as an
error. The response matrices to kicks on every unit are in the results
file.

## Results: higher-dimensional stalks ([QUESTION-283](../questions.d/QUESTION-283.md))

100 random sheaves for each interior stalk dimension. "Pairwise closure"
is the set of boundary states each of whose pairs lies in the projection
of the section space; the section space is pairwise expressible exactly
when the two have the same dimension.

| interior stalk | star alone: sections / pairwise closure | with one boundary–boundary edge |
|---|---|---|
| 1 | 1 / 1, pairwise | 0 / 0 |
| 2 | 2 / 3, three-way relation needed, 100 of 100 | 1 / 1, pairwise |
| 3 | 3 / 3, no constraint | 2 / 2, pairwise |

A three-way boundary relation is forced generically when the interior
stalk has dimension one less than the number of boundary units, as in
Hansen and Ghrist's v₁ = v₂ + v₃ ([THEORY-1090](../theory.d/THEORY-1090.md)). Adding a pairwise edge
among the boundary units can make the reduced constraint pairwise again.
A first pass counted 39 of the three-dimensional cases wrongly, from
numpy's default rank tolerance; the lines are kept in the results file
and superseded by the rerun.

## What it shows and what it does not

It shows, in one model family, that the achievements [CLAIM-474](../claims.d/CLAIM-474.md) keeps
apart can be made to come apart on purpose: compatibility without
attraction, attraction without coupling, organization without
compatibility, persistence that only withdrawal reveals, and coherence
without knowledge. It gives [QUESTION-063](../questions.d/QUESTION-063.md) a constructed answer: the
displacement and perturbation interventions separate common drive from
coupling where timing and gluing cannot. The claim filed from it is
[CLAIM-903](../claims.d/CLAIM-903.md).

It does not show any of this for a real system. The units are identical
in kind, the graph is small and known, the drive is known to the
experimenter, and each setting was run once with fixed seeds. The
apparatus's revision is a linear model of phase responses; the plastic
maps are one rule among many, and they change the coupling directly, so
the arm is [QUESTION-282](../questions.d/QUESTION-282.md)'s variant in which revision feeds back into the
physical coupling, with the rule given by the experimenter. Effective
boundary laws were tested only for linear sheaves, not fitted from the
oscillator dynamics. Costs of establishing each achievement were not
measured beyond the relaxation rates and the number of interventions
(four) the checked revision used. Not run: [CASE-179](CASE-179.md)'s note of 2026-11-03
arms (declared tolerances, own against outside channels,
observer-limited policies, captured correspondence, maintenance
knockouts beyond the one here, the positive arm), A32 §11's arms and
resource limits.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.

## Note of 2026-11-25: rerun by a session other than the filer's

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of LEAD-tmpc0rqa, at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). From a copy of `scratch/studies/lead-098/` in the session's scratch space, with `results.jsonl` set aside, run with python3 -I (scipy 1.18.1 and numpy 2.5.3 in a virtual environment of the session's scratch space; scipy was not installed on the system). The 8 tests pass. All 347 items the runner writes now agree with the stored ones in every field but `secs`; the stored file also keeps the 300 superseded `sheaf:` lines of the first pass, which the runner no longer writes. Every figure above was compared and matches, among them: phase-locking values 0.9985 and 0.9996; holonomy 3 × 10⁻⁵ and 4 × 10⁻⁶; the displaced drive followed by 0.002, 0.30 and 0.58, with others' mean shifts 0.003, 0.12 and 0.13; kicks reaching the others at 0.010, 0.12, 0.14 and 0.14; withdrawal orders 0.996 and 0.47, amplitudes 0.70, 0.002, 0.71 and 0.003; the suppression arm's 0.33, 0.001 and 0.996; μ ≈ 1.06, 0.75, −0.2 and 0.86; fitted gains 0.068, 0.356, −0.001 and 0.272; the revision errors (1.06, 1.42, 1.81, 0.25 unrevised; 0.80, 1.41, 1.81, 0.25 by consistency; 0.34, 0.17, 0.14 checked, the last candidate rejected); the holonomy table's residuals 0.007, 0.027, 0.063, 0.41 and 0, and the gauge pair 0.06299 against 0.06300; the sheaves' 1/1, 2/3 and 3/3 in 100 of 100. Nothing failed to reproduce. Promoted in the same pass (history, version 2). The note is the assistant's (Claude, in this session).
