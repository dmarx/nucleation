---
status: Proposed
title: 'Removing the core of Ito and Kaneko''s coupled-map network: in 12 of 12 seeds the periphery refills it to its former size and one-way structure within a million steps; half a core removed is made up from the periphery; a core made rare in influence is recovered by its own members'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-065 at the
    coordinator's brief. The model was reimplemented from NOTE-1414's
    transcription of the equations, checked against arXiv's v1 of the
    paper. Script, tests, results and a README are under
    scratch/studies/lead-065/.
standing: documented
kind: executed-study
tags:
- complex-systems
- network-science
- ecology
date: '2026-11-22'
reported_in:
- NOTE-1414
bears_on:
- QUESTION-132
illustrates:
- CLAIM-279
line:
- distributed-agency
summary: >-
  LEAD-065 asked whether QUESTION-132's candidate case, Ito and Kaneko's
  network of identical logistic maps with normalized, similarity-reinforced
  weights (LIT-1842, NOTE-1414), refills its core when core units are
  removed. The model was reimplemented at the paper's parameters (N = 100,
  a = 3.97, c = 0.12, δ = 0.1) and grown for 3 × 10⁶ steps in 12 seeds. It
  reproduces a core of 15.6 ± 1.2 units by the paper's snapshot criterion,
  and 18.2 ± 1.1 by time-averaged outgoing weight above the mean, with
  1.6 ± 2.6 periphery-to-core links (paper: 2). Five arms then ran for
  10⁶ steps. With the whole core deleted, former periphery units formed a
  new core of 17.2 ± 0.8 units. The control that deletes as many periphery
  units formed one of 17.0 ± 1.1. The new core had 2.9 ± 4.8
  periphery-to-core links. With a random half of the core deleted, 8.8 ±
  0.8 periphery units joined the 8.5 survivors. With every weight given to
  the core cut to 10⁻³ of its value, the core's own members made up 92% of
  the core 10⁶ steps later. The differentiation recovers. Which units hold
  the core is set by the dynamics, not fixed by who held it first. One
  parameter point, one system size, 12 seeds. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpf11gs — new, filed with this case -->

# CASE-tmpvn7wm: Removing the core of Ito and Kaneko's coupled-map network: in 12 of 12 seeds the periphery refills it to its former size and one-way structure within a million steps; half a core removed is made up from the periphery; a core made rare in influence is recovered by its own members

## What was done

LEAD-065 asks for Ito and Kaneko's network to be reimplemented, its
core units removed, and a check of whether peripheral units move into the
core. NOTE-1414 and QUESTION-132's note of 2026-10-29 both name the test.

**The model.** This is eqs. (1)–(2) of LIT-1842, as NOTE-1414 gives
them. They were checked against arXiv's v1
(https://arxiv.org/pdf/cond-mat/0108408v1, fetched 2026-11-22).

- Each unit follows x_{n+1}^i = f[(1 − c)x_n^i + c Σ_j w_n^{ij} x_n^j],
  with f(x) = ax(1 − x).
- Each weight follows w_{n+1}^{ij} = [1 + δg]w_n^{ij} / Σ_j[1 + δg]w_n^{ij},
  with g = 1 − 2|x_n^i − x_n^j|.
- Both updates use time-n values.
- The paper's initial condition is used: self-weights 0, the rest
  1/(N − 1), states uniform on (0, 1).
- The paper's parameter point is used: N = 100, a = 3.97, c = 0.12,
  δ = 0.1.

A test checks the vectorized step against a loop transcription of the two
equations (`scratch/studies/lead-065/test_ikmodel.py`, 8 tests).

**Classes.** The primary criterion puts unit j in the core when its total
outgoing weight W_out^j = Σ_i w^{ij}, averaged over 50,000 steps, exceeds 1.
That is the mean, since every row of w sums to 1. The paper's own criterion
is also recorded: a snapshot out-degree above 20, counting a link when
w > 1/(N − 1), with the cut scaled to 20(M − 1)/99 in a network of M units.
The two criteria agree on 97.3 of 100 units. The averaged one is used for
membership because it does not flicker from step to step.

**Protocol.** There were 12 seeds. Each grew for 3 × 10⁶ steps, the time by
which the paper sees no more migration between groups. From each grown
state, five arms ran for 10⁶ steps:

- **control**: unchanged.
- **remove_periph**: as many random periphery units deleted as the core
  had, which controls for the smaller network.
- **remove_core**: every core unit deleted, rows and columns, and each
  survivor's incoming weights renormalized.
- **remove_half_core**: a random half of the core deleted.
- **suppress_core**: every weight given to a core unit multiplied by
  ε = 10⁻³ and the rows renormalized. Removing a unit is not the recovery
  test QUESTION-132 asks for, because zero is absorbing. This arm is that
  test: the units remain, with small positive influence and no further
  intervention.

## Result

**Reproduction, at t0 = 3 × 10⁶.** The paper's Table I is one realization
with a core of about 16, and its connection counts sum to 1,187 strong
links. Here, with snapshot counts across the 12 seeds:

| quantity | here | paper |
|---|---|---|
| snapshot core size | 15.6 ± 1.2 [14–17] | "typically 14"; Table I fits 16 |
| core size, averaged W_out > 1 | 18.2 ± 1.1 [16–20] | — |
| CC links | 134 ± 22 | 159 |
| CP links | 532 ± 24 | 792 |
| PC links | 1.6 ± 2.6 [0–7] | 2 |
| PP links | 134 ± 23 | 234 |

The core forms, and the one-way structure reproduces: the periphery sends
almost nothing to the core. There are fewer strong links overall than in
the paper's table, about 800 against 1,187. Of each seed's final core,
16.8 ± 1.1 were already core 10⁶ steps earlier. Membership is nearly but
not exactly absorbing. In the control, about one periphery unit is in the
core at any checkpoint.

**After the intervention**, as mean ± sd [min–max] over 12 seeds at 10⁶
steps. The full time course at 6 × 10⁴, 2 × 10⁵, 5 × 10⁵ and 10⁶ steps is in
`scratch/studies/lead-065/results/summary.md`.

| arm | units | core | of which core at t0 | of which periphery at t0 | snapshot core | PC links |
|---|---|---|---|---|---|---|
| control | 100 | 18.6 ± 0.9 | 17.3 ± 1.2 | 1.2 ± 1.1 | 15.2 ± 1.3 | 1.3 ± 2.3 |
| remove_periph | 81.8 | 17.0 ± 1.1 | 16.3 ± 1.1 | 0.7 ± 0.7 | 14.5 ± 1.2 | 2.8 ± 2.8 |
| remove_core | 81.8 | 17.2 ± 0.8 [16–19] | 0 | 17.2 ± 0.8 | 15.2 ± 1.3 | 2.9 ± 4.8 |
| remove_half_core | 90.7 | 17.2 ± 0.9 | 8.5 ± 0.7 | 8.8 ± 0.8 | 15.2 ± 1.0 | 2.2 ± 3.2 |
| suppress_core | 100 | 18.4 ± 0.9 | 16.8 ± 1.2 | 1.6 ± 1.2 | 15.5 ± 0.8 | 1.6 ± 2.3 |

- **The periphery refills a removed core.** This held in every seed. The new
  core is 0.95 ± 0.05 of the original's size, and 1.02 ± 0.10 of the core
  in the network of the same size that lost periphery instead. It has the
  original's one-way structure.
- **The refill takes time.** At 6 × 10⁴ steps the snapshot core is 9.9 ±
  0.5. It is 12.4 at 2 × 10⁵ and 14.1 at 5 × 10⁵. It reaches the control's
  15.2 by 10⁶. Averaged over the transient, outgoing weight is at first
  spread over more units: 25.2 above the mean at 6 × 10⁴.
- **Half a core removed is made up.** The core returns to its full size.
  The survivors stay in it and periphery units fill the vacancies.
- **A core made rare recovers itself.** With its influence cut a
  thousandfold, the old core is again the core within 6 × 10⁴ steps: 17.2
  of 19.2 units. At 10⁶ steps its members make up 0.92 ± 0.07 of the core.
  Former periphery units do not take over. Its members' recovery growth
  from rarity is positive.

## What it can show

The core-periphery split of LIT-1842 is a regime of the dynamics, not
a frozen arrangement of particular units. Remove its holders and others
take the role. Make its holders rare and they regain it. By LEAD-065's
own criterion this classes the system as one whose differentiation
recovers. NOTE-1414's reading, that "The split looks like the question's third
outcome, entrenched asymmetry" because "membership is absorbing", holds for who stays in
the core while nothing is disturbed. It does not hold for whether the
asymmetry depends on its first holders.

## What it cannot show

- **Scope.** There is one parameter point (the paper's), one system size
  and one δ. There are 12 seeds, and 10⁶ steps after each intervention.
  Other points in the desynchronized phase are not tested.
- **The recovering thing.** What recovers here is a role: some 15 to 18
  units holding attention. It is not a specialist with a niche.
  QUESTION-132's first outcome asks that each functionally distinct
  specialist recover when rare. This model has no function, accuracy or
  context for its units to specialize in, and its periphery units are
  interchangeable. Whether a role refilled by interchangeable units counts
  as stabilizing coexistence, or is a fourth thing, is taken up in
  CLAIM-tmpf11gs and is the owner's to settle.
- **Periphery rarity.** The recovery of a periphery unit made rare was not
  tested.
- **Parameters during recovery.** In QUESTION-132's terms, the units' rule is
  fixed and only the weights and states adapt during recovery. A unit has
  no other parameters, so the frozen-versus-trainable distinction does not
  arise.
- **Criterion.** The primary core criterion, averaged W_out above the
  mean, is the assistant's choice. The paper's snapshot criterion is
  reported beside it and gives the same picture.
