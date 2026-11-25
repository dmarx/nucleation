---
number: 308
status: Proposed
formerly:
- CASE-tmplsvee
title: 'Scaffold withdrawn from a small assembly model'
statement: >-
  A small assembly model whose scaffold forms and holds a nucleus, withdrawn
  for good at chosen states: the drop in the chance of completing falls to
  under 0.05 two units into eight only where the bound units hold the
  nucleus and it speeds their binding, stays at 0.10 or more to the last
  unit where they do not hold it, and under withdrawal at a clock time falls
  to zero in every case as runs finish
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-095. The code,
    tests and outputs are under scratch/studies/lead-095/.
standing: stipulated
kind: executed-study
tags:
- complex-systems
- probabilistic-modeling
- mathematics
- natural-sciences
date: '2026-11-22'
bears_on:
- QUESTION-398
- QUESTION-397
line:
- transient-support
- realizability
summary: >-
  [LEAD-095](../leads.d/LEAD-095.md) asked for a Markov chain in which support can be withdrawn
  at chosen intermediate states ([QUESTION-398](../questions.d/QUESTION-398.md)) and the nucleus's
  relations switched on as a state and as a rate modifier separately
  ([QUESTION-397](../questions.d/QUESTION-397.md)). The chain has a nucleus, present or not, and M = 8
  other units; a scaffold forms the nucleus fast and stops it dissolving;
  withdrawal at a state is permanent. A's measure D(s) = q_supported(s) −
  q_withdrawn(s) was computed exactly by linear solve at every state, in
  four mechanisms. With both feedback (bound units stabilize the nucleus)
  and a rate effect (the nucleus triples the binding rate), D falls from
  0.085 to under 0.05 at n = 2 and to 0.002 at n = 7, while the chance of
  completing after withdrawal is already 0.88 at n = 2: independence
  before completion, not completion. With the rate effect and no feedback,
  D falls only from 0.35 to 0.10 and the scaffold is needed to the end;
  with neither, D rises from 0.13 to 0.22 in this parameter set, though not
  in most of a random sweep. Withdrawal at a clock time shows a drop that
  falls to zero in every mechanism, because runs finish: A's rival, "the
  system merely completed before withdrawal", is real under timed
  withdrawal and excluded by withdrawing at states. With the scaffold
  absent, switching the nucleus's state and rate effects separately shows
  both raising the committor at matched progress, with only the binding
  rate (Δk = 2 against 0) telling them apart. The model is the assistant's
  and its rates are invented. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-865 — new; the claim this study grounds, filed with it -->

# CASE-308: Scaffold withdrawn from a small assembly model

## The model

A continuous-time Markov chain on states (N, n). N is 1 when a nucleus
has formed and 0 when not; n = 0, …, M counts the other units bound, with
M = 8. Two outcomes absorb: the target F and a failure K.

| Transition | Rate, unsupported | Rate, supported |
|---|---|---|
| nucleus forms, (0, n) → (1, n) | a₀ = 0.2 | a_S = 5 |
| nucleus dissolves, (1, n) → (0, n) | d₀θⁿ, d₀ = 1 | 0 (the scaffold holds it) |
| a unit binds, (N, n) → (N, n + 1) | 1, or g = 3 when N = 1 and the rate effect is on | same |
| a unit unbinds, (N, n) → (N, n − 1) | b = 1.5 | same |
| trap, any unfinished state → K | κ = 0.02 | same |

Since b exceeds the unaided binding rate, growth drifts back unless the
nucleus speeds it. Two switches set what the nucleus does:

- **feedback**: θ = 0.5, so each bound unit halves the nucleus's
  dissolution rate, or θ = 1, no feedback;
- **rate effect**: on, the nucleus triples the binding rate of the other
  units, a non-zero Δk for transitions it takes no part in
  ([QUESTION-397](../questions.d/QUESTION-397.md)); or off;
- **state effect**: on, the target needs the nucleus, F = {(1, M)}; off,
  F = {(0, M), (1, M)}. On unless said otherwise.

The scaffold is support of the kind [QUESTION-398](../questions.d/QUESTION-398.md) describes: it
helps establish the nucleus and keeps it. **Withdrawal at a state s** means
the chain continues from s under the unsupported rates for good.
q_supported(s) and q_withdrawn(s) are the exact committors
Pr_s(τ_F < τ_K) under the two generators, from the linear solve
Σⱼ Qᵢⱼ qⱼ = 0 off F ∪ K. D(s) is their difference.

**Checks.** The solver reproduces the gambler's-ruin formula
q(i) = (1 − rⁱ)/(1 − r^M) to 10⁻¹², [CLAIM-596](../claims.d/CLAIM-596.md)'s construction (0.8
and 17/30) exactly, and Monte Carlo runs of the chain within sampling error.
Twelve tests pass (`test_committor_model.py`).

## Results

**D(1, n), withdrawal with the nucleus present**, n = 0, …, 7:

| Mechanism | n = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | q_supported(1, 0) |
|---|---|---|---|---|---|---|---|---|---|
| feedback and rate effect | 0.085 | 0.068 | 0.049 | 0.032 | 0.019 | 0.011 | 0.005 | 0.002 | 0.912 |
| feedback only | 0.047 | 0.047 | 0.046 | 0.046 | 0.044 | 0.040 | 0.032 | 0.020 | 0.255 |
| rate effect only | 0.349 | 0.342 | 0.328 | 0.306 | 0.275 | 0.233 | 0.177 | 0.102 | 0.912 |
| neither | 0.128 | 0.130 | 0.136 | 0.148 | 0.166 | 0.192 | 0.217 | 0.202 | 0.255 |

The scaffold holds the nucleus, so feedback changes nothing while it is
on: the supported committor is the same with and without feedback. What
feedback changes is what happens when the scaffold goes.

- **Feedback and rate effect.** D falls below 0.05 at n = 2, a quarter of
  the way. There the chance of completing after withdrawal is 0.879
  against 0.927 kept. That is independence of the support well before
  completion, as A expected.
- **Rate effect only.** D falls, from 0.35 to 0.10, but never becomes
  small before the last unit. The nucleus stays needed, since it speeds
  every binding, and nothing but the scaffold holds it. This is the shape
  of Marras et al.'s closing strands, which [QUESTION-398](../questions.d/QUESTION-398.md) records as never
  dispensed with.
- **Feedback only.** The scaffold adds little here (0.255 kept), and D
  falls relative to it, from 18 % of the supported chance to 3 %.
- **Neither.** D rises with progress, from 0.13 to 0.22: the nucleus is a
  part the target needs, and the closer the rest is to finished, the more
  its loss costs. That reverses A's expectation, as captive rearing does in
  [QUESTION-398](../questions.d/QUESTION-398.md)'s note of 2026-11-05.

**Why.** An exact identity, which the code checks to 10⁻¹⁵:

  D(s) = E_s^supported [ ∫₀^τ c(X_t) Δ_N⁰(X_t) dt ],

where Δ_N⁰(N, n) = q_withdrawn(1, n) − q_withdrawn(0, n) is what the
nucleus is worth under the unsupported rates, c is how much the scaffold
changes the nucleus's rates (d₀θⁿ where it is present, a_S − a₀ where it
is not), and the expectation runs along the supported future from s until
absorption. So withdrawal costs, from a state, what the nucleus's
fragility times its productivity adds up to along the way the supported
system would have gone. D is small before completion only where that
product is small along the way: the bound units hold the nucleus (θⁿ
small), or the nucleus has stopped mattering (Δ_N⁰ small). The identity
holds for any support that changes rates and is withdrawn for good
([CLAIM-865](../claims.d/CLAIM-865.md)).

**How far the profiles hold.** In 2,000 random parameter sets (seed
20261122; `sweep.py`), D(1, n) fell monotonically in 98 % with feedback and
the rate effect, in 83 % with the rate effect alone and in 54 % with
feedback alone. With neither it rose monotonically in 42 % and fell in 9 %.
The rise in the table is one possible outcome, not the rule.

**A's rival, under withdrawal at a clock time.** Start at (0, 0) with the
scaffold on and withdraw it at time t. The chance of success is
Y(t) = Pr(finished by t) + Σ_s Pr(at s at t) q_withdrawn(s).

| Mechanism | t = 0 | 10 | 40 | 160 | smallest D(1, n), n < M |
|---|---|---|---|---|---|
| neither: q_supported − Y(t) | 0.128 | 0.109 | 0.047 | 0.002 | 0.128 |
| feedback and rate effect | 0.134 | 0.001 | 0.000 | 0.000 | 0.002 |

With neither mechanism, the drop under timed withdrawal falls to almost
nothing by t = 160, while from every unfinished state it is at least
0.128. All of that fall is runs that had finished, by success or failure,
before the scaffold went. That is A's rival, "the system merely completed
before withdrawal", and it can produce the whole of A's expected signature.
Withdrawing at chosen unfinished states excludes it by construction.

**The two effects switched separately** ([QUESTION-397](../questions.d/QUESTION-397.md)), unsupported,
θ = 1. Δ_N(n) = q(1, n) − q(0, n) at matched n, and the change Δk in the
binding rate of units outside the nucleus:

| State effect | Rate effect | Δ_N at n = 0 | n = 4 | n = 7 | Δk |
|---|---|---|---|---|---|
| off | off | 0.000 | 0.000 | 0.000 | 0 |
| off | on | 0.031 | 0.080 | 0.072 | 2 |
| on | off | 0.000 | 0.005 | 0.184 | 0 |
| on | on | 0.029 | 0.085 | 0.196 | 2 |

Both effects raise the committor at matched progress. A pure state effect
is a head start that matters only near completion here, since a nucleus
that dissolves at rate 1 and re-forms at 0.2 is worth little until the
rest is nearly done. The interaction contrast is near zero (−0.002 at
n = 0, −0.000 at n = 4). Near completion the two are close in committor
(0.184 against 0.196) and differ entirely in Δk, which repeats
[CLAIM-596](../claims.d/CLAIM-596.md)'s point at matched intermediate states rather than in yields.
The shape of D(s) does not reliably tell them apart either, by the sweep.

## What it can show

- **That A's measure is computable and does what A says in a model.** D
  falls near zero well before completion in one mechanism, so
  [QUESTION-398](../questions.d/QUESTION-398.md)'s "difference that persists after withdrawal" occurs,
  with the rival excluded.
- **The conditions in this model.** The partial organization becomes
  independent of the scaffold when what it has built takes over the
  scaffold's job of holding the nucleus, or no longer needs the nucleus.
  Where neither happens, the support is needed to the last step, however
  far assembly has gone.
- **That timed withdrawal cannot measure it.**
- **That the state and rate effects can be switched separately**, both
  raising committors, and are told apart by Δk.

It cannot show which mechanism any real system has. It is a stipulated
model with invented rates, one kind of support (one that holds a nucleus)
and permanent withdrawal. [CLAIM-604](../claims.d/CLAIM-604.md)'s case, where D depends on how long
an outage lasts, is outside it, and so is support that leaves something
behind outside the state.

Code: `scratch/studies/lead-095/` (`committor_model.py`, `sweep.py`,
`test_committor_model.py`, outputs in `results.txt`, `results.json`,
`sweep.txt`, `sweep.json`).
