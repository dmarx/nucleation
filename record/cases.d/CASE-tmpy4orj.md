---
status: Proposed
title: 'A kinetic construction in which nuclei form fast only on a teacher and, once formed, make teachers from material: the loop closes, keeping its teacher with no outside supply of it, only below a teacher turnover set by the teaching rate; withdrawal becomes safe on crossing a separatrix, while nuclei are 0.02 % to 30 % of their maintained number; material supply is still needed; nuclei that only repair teachers cut the supply needed but never to zero; and in finite numbers closure is a lifetime that grows with size'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-093. The code,
    tests and outputs are under scratch/studies/lead-093/.
standing: documented
kind: executed-study
tags:
- complex-systems
- individuation
- natural-sciences
- mathematics
date: '2026-11-22'
illustrates:
- CLAIM-597
- CLAIM-604
- CLAIM-516
bears_on:
- QUESTION-399
- QUESTION-361
line:
- transient-support
- distributed-agency
summary: >-
  [LEAD-093](../leads.d/LEAD-093.md) asked for a nucleus that, once formed, takes part in producing
  or repairing the constraints of its own formation, and a measure of when
  that loop closes ([QUESTION-399](../questions.d/QUESTION-399.md)), with a student that becomes a teacher
  ([QUESTION-361](../questions.d/QUESTION-361.md), [CASE-190](CASE-190.md)). In the model built here, nuclei form fast only
  where a teacher is present, cooperatively, and each nucleus makes
  teachers from material. At the base point, founding by an outside teacher
  is needed and the loop then holds with the outside teacher withdrawn; it
  stops closing above a teacher turnover of 0.19, and the material supply
  can never be withdrawn. The moment withdrawal becomes safe is a crossing
  of a separatrix in the joint state, reached while nuclei are 0.02 % to
  30 % of their maintained number and the self-made share of teacher supply
  is anywhere from 0.2 % to 65 %. Beyond a turnover of about 0.73 the loop
  costs more outside teacher supply than no loop. Nuclei that repair
  teachers without making them divide the supply needed by 1 + ρN/λ and
  never close. Populations matched in nucleus number close or not by the
  share of nuclei that can teach. In finite numbers the closed loop is lost
  after a time that grows roughly exponentially with size. The
  model and its rates are the assistant's, invented. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpocjfb CLAIM-tmpnyf9e CLAIM-tmpk6abl CLAIM-tmppgdad CLAIM-tmp1qqso CLAIM-tmps1ll3 CASE-265 CASE-tmplsvee CASE-tmpfktyl — new or Proposed; the claims filed from this run, and the neighbouring constructions it is compared with -->

# CASE-tmpy4orj: A kinetic construction in which nuclei form fast only on a teacher and, once formed, make teachers from material: the loop closes, keeping its teacher with no outside supply of it, only below a teacher turnover set by the teaching rate; withdrawal becomes safe on crossing a separatrix, while nuclei are 0.02 % to 30 % of their maintained number; material supply is still needed; nuclei that only repair teachers cut the supply needed but never to zero; and in finite numbers closure is a lifetime that grows with size

## Why this construction

The lead offered two routes: extend [CASE-190](CASE-190.md) so its student becomes a
teacher, or use the Life eaters. Neither was taken literally.

- **Not [CASE-190](CASE-190.md)'s equations.** Not all of them are on the record: A18's
  fuel demand Ψ is never stated.
- **Not the eaters.** The eater repairs only the strike it is shaped for
  ([CASE-tmpfktyl](CASE-tmpfktyl.md)), and a Life pattern has no turnover rate to vary.

The model built instead closes the three gaps [CASE-190](CASE-190.md) names:

- **The coupling runs both ways.** What the nuclei make is what forms them.
- **There is succession.** Each nucleus is a student of the teacher that
  formed it, and it then teaches.
- **The teacher is not stipulated.** After the founding, every teacher was
  made inside the model.

## The model

Dimensionless mass action, deterministic unless said otherwise.

    m' = J − δm − F − βmN                 material, supplied from outside at rate J
    T' = σ − k_T T + βmN                  teacher: outside supply σ, turnover k_T
    N' = (1 − ε)F − dN                    nuclei that teach
    B' = εF − dB                          defective nuclei: same structure and cost, teach nothing
    F  = a₀m² + a₁mT²/(K² + T²)           spontaneous plus templated formation

The teacher T is the constraint on formation. It catalyses formation and
is not consumed by it. A nucleus, once formed, makes teachers from
material at rate βm: the student becomes a teacher.

- **Base point.** J = 1, δ = 0.1, a₀ = 10⁻⁶, a₁ = 0.1, K = 2, d = 0.1,
  β = 0.02, k_T = 0.1, ε = 0.
- **Why cooperative.** Formation is cooperative in T, so a founding is
  needed. With linear templating the loop ignites from the spontaneous
  background, and there is nothing to found.

**The repair arm.** Here nuclei make no teachers (β = 0) and repair them
instead. A teacher is damaged at k_T into D, which is lost at λ unless a
nucleus restores it at ρND. A repair costs rcost material: 0, and 1 as a
check.

Two definitions:

- **The loop closes at a parameter point** when, with σ = 0, there is a
  stable state with N at least 50 times the spontaneous background
  a₀(J/δ)²/d = 0.001.
- **It has closed by time t** when switching the outside teacher off for
  good at t leaves the nucleus maintained.

The second definition is the assistant's choice. It measures closure by
the one test the question names, withdrawal of outside supply. The share
of teachers made inside, and the number of nuclei, are recorded beside it.

**Checks.** Eleven tests pass (`test_closing.py`):

- the steady states are zeros of the vector field, and the base point has
  a stable empty state, a saddle and a stable maintained state;
- with β = 0 the loop never closes;
- the critical turnover is a fold;
- the supply formula reproduces a steady state;
- the repair arm conserves teachers up to the loss λD;
- the generation-resolved model sums to the aggregate;
- the founding bisection brackets.

## Results

**The base point** has three steady states with σ = 0:

| state | m | T | N | |
|---|---|---|---|---|
| empty | 9.997 | 0.002 | 0.001 | stable |
| threshold | 9.675 | 0.214 | 0.111 | saddle |
| maintained | 4.548 | 2.597 | 2.855 | stable |

**Where it closes** (e1, e2). Over teacher turnover 0.02 to 1 against
teaching rate 0.002 to 0.1, on a 25 × 25 grid:

- 55 points self-ignite, from the spontaneous background alone;
- 252 are bistable: a founding is needed, and after it the loop holds
  without outside teacher;
- 318 never close.

The critical turnover k_T* at which closure is lost is a fold. It rises
with the teaching rate: 0.061, 0.111, 0.191, 0.312 and 0.483 at
β = 0.005, 0.01, 0.02, 0.04 and 0.08. It falls with the defective share
ε: 0.191 at ε = 0 and 0.111 at ε = 0.5. At base turnover the loop closes
only while ε < 0.560, β > 0.0088 and J > 0.692.

**What outside supply it still needs** (e3).

- **Material is always needed.** The least material supply that closes
  the loop rises with turnover: 0.29 at k_T = 0.02, 0.69 at 0.1 and 1.00
  at 0.19. With J = 0 nothing persists.
- **Teacher supply needed to hold N = 2.**
  - Below k_T ≈ 0.19 the loop needs none.
  - Above it the loop needs less than the same model with β = 0, but only
    up to k_T ≈ 0.73: 0.138 against 0.289 at k_T = 0.25, and 0.358
    against 0.462 at 0.4.
  - Beyond that it needs more: 1.239 against 1.154 at k_T = 1.
- **Why the loop can cost.** Making teachers draws on the material that
  formation also needs. The loop pays only while what it makes exceeds the
  extra teacher needed to offset that draw. The crossover is
  βmN/(T_loop − T_none) = 0.02 · 5.714 · 2/(1.467 − 1.154) ≈ 0.73.

**When it closes** (e4). An outside teacher supplied at σ from the empty
state for a time t_w, then withdrawn for good. The shortest t_w after which
the nucleus persists:

| k_T | σ | t_w | T at t_w | N at t_w (share of maintained) | self-made share of teacher supply at t_w |
|---|---|---|---|---|---|
| 0.1 | 0.01 | 61.0 | 0.234 | 0.095 (3.3 %) | 0.65 |
| 0.1 | 0.05 | 7.77 | 0.289 | 0.050 (1.7 %) | 0.16 |
| 0.1 | 0.3 | 1.18 | 0.335 | 0.011 (0.4 %) | 0.007 |
| 0.03 | 0.05 | 1.34 | 0.066 | 0.0006 (0.02 %) | 0.002 |
| 0.18 | 0.05 | 30.8 | 0.604 | 0.449 (30 %) | 0.62 |

- **What marks closure.** The threshold is a crossing of the saddle's
  stable manifold in the joint state (m, T, N). Neither a count of nuclei
  nor the self-made share of supply marks it. Withdrawal is safe at a
  point where the nucleus has hardly formed: its formation is still
  ahead, and it completes on teachers that the nuclei themselves make.
  After withdrawal at t_w, N takes about 120 to 275 time units to reach
  half its maintained value. With the supply kept on it takes 8 to 39.
- **Productive nucleus.** At the bistable base point the empty state never
  forms nuclei without a founding. Where the loop self-ignites
  (k_T = 0.02, β = 0.06), half the maintained N takes 120 time units
  unaided, and 15.8 with σ = 0.05 for 10 time units (e4b).

**Disturbance survived without outside supply** (e5). From the maintained
state:

- **Losses of one constraint.** The loop survives losing every teacher,
  because the nuclei remake them, and losing every nucleus, because the
  teachers re-form them.
- **Losses of both.** It survives losing up to 91 % of both at once.
- **Turnover pulses.**
  - Raised to 0.15 for any duration: survived.
  - Raised to 0.2 or 0.3: survived for up to 204 and 51 time units.
  - Raised to 3: survived for up to 24. The nuclei, which turn over at
    their own rate, carry the loop through the loss of its teachers.

**Repair without production** (e6). In steady state the outside supply
equals the loss λD, so the supply needed to hold N is
σ = k_T T/(1 + ρN/λ). The runs agree with this within 2 × 10⁻⁴:

- **Some values.** At λ = 0.05 it falls from 0.115 without repair to
  0.0385, 0.0128, 0.0028 and 0.0004 at ρ = 0.05, 0.2, 1 and 5. The time
  for N to halve after withdrawal rises from 13 to 25, 48, 163 and 735.
- **Never zero.** The supply needed reaches zero only at λ = 0, where a
  damaged teacher is never lost and the teacher mass is conserved.
- **Repair cost.** Charging a unit of material per repair changes the
  numbers by up to about 20 %, and the pattern not at all.

**Students who cannot teach** (e7). Populations matched at 3.0 nuclei,
each held by the outside supply its own steady state needs:

- **The split.** Those with defective share ε of 0, 0.3 and 0.5 persist
  when the supply is withdrawn. Those with 0.6, 0.7 and 0.9 lose every
  nucleus.
- **What shows it before withdrawal.** The supply each needs (0.033 at
  ε = 0, 0.096 at 0.7), and its material and teacher levels.
- **What decides it.** Only the aggregate teaching gain (1 − ε)β. A
  population whose fewer teaching nuclei teach proportionally faster has
  identical aggregate equations.

**Succession** (e8). With σ = 0.05 for 12 time units:

- **Teachers at withdrawal.** 82 % of the teachers are outside ones.
- **Afterwards.** By t = 46, under 1 % are. The mean teacher generation
  then advances by one every 20 time units, which is 1/k_T + 1/d.
- **With the supply kept on** to t = 100, outside teachers hold about 16 %
  of the pool.

**Finite numbers** (e9). An exact stochastic simulation in volume Ω, from
the maintained state with σ = 0, 40 runs per size, run until both teachers
and nuclei are gone or t = 20 000:

| k_T | Ω | nuclei at start | mean time to loss | runs censored |
|---|---|---|---|---|
| 0.1 | 1 | 3 | 70 | 0 |
| 0.1 | 2 | 6 | 215 | 0 |
| 0.1 | 4 | 11 | 1 066 | 0 |
| 0.1 | 8 | 23 | ≈ 29 000 (exponential fit) | 21 |
| 0.1 | 12 | 34 | > 20 000 (one loss in 40 runs) | 39 |
| 0.15 | 1 | 2 | 31 | 0 |
| 0.15 | 2 | 4 | 71 | 0 |
| 0.15 | 4 | 8 | 115 | 0 |
| 0.15 | 8 | 17 | 339 | 0 |
| 0.15 | 12 | 25 | 658 | 0 |

Without the loop (β = 0), nuclei halve in 13 time units. Closure in
finite numbers is metastability. Its lifetime grows roughly exponentially with size, and
more slowly near the fold:

- at k_T = 0.1, from Ω = 2 to 8, the log of the mean time rises by about
  0.8 per unit of Ω;
- at k_T = 0.15, which is 0.79 of the critical turnover, it rises by about
  0.25.

Close to the fold, a loop that closes in the rate equations is lost within
a few hundred time units at these sizes.

## What it shows

- **[QUESTION-399](../questions.d/QUESTION-399.md).** It gives the system the question asks for, by
  construction. A nucleus speeds formation. Once formed, it makes the
  constraint of its own formation. The loop's closing is measured:
  - the turnover it survives: k_T* against β, ε and J;
  - the supply it still needs: material always, teacher never once
    closed;
  - when it closes in time: the separatrix crossing.

  [CLAIM-tmpocjfb](../claims.d/CLAIM-tmpocjfb.md), [CLAIM-tmpnyf9e](../claims.d/CLAIM-tmpnyf9e.md) and [CLAIM-tmpk6abl](../claims.d/CLAIM-tmpk6abl.md) state the findings.
- **[QUESTION-361](../questions.d/QUESTION-361.md).** It supplies the succession [CASE-190](CASE-190.md) lacked:
  students become teachers, generation after generation. Students equally
  present differ as teachers only through the supply they need, and on
  withdrawal ([CLAIM-tmppgdad](../claims.d/CLAIM-tmppgdad.md)).
- **Closure or autocatalysis.** Whether the loop is organizational closure
  in [TERM-070](../terms.d/TERM-070.md)'s sense or only autocatalysis is left to the owner, filed as
  two readings: [CLAIM-tmp1qqso](../claims.d/CLAIM-tmp1qqso.md) and [CLAIM-tmps1ll3](../claims.d/CLAIM-tmps1ll3.md).

## What it cannot show

- **The parameters are invented.** Each number holds for this model and
  these rates. What carries over is the pattern: a fold in turnover, a
  separatrix in time, material dependence, and repair that cannot close.
- **No physical system is modelled.** In particular this is not DNA
  origami. Repair from a strand pool ([CLAIM-597](../claims.d/CLAIM-597.md)) is the repair arm's
  case, not the production arm's.
- **It inherits the record's limits.** The motifs are irreversible mass
  action, as in [CASE-190](CASE-190.md), and the teacher carries no information
  beyond its amount. The neighbouring constructions are [CASE-265](CASE-265.md), whose
  mutual maintenance runs on a standing supply, and [CASE-tmplsvee](CASE-tmplsvee.md), whose
  scaffold is withdrawn at states.
