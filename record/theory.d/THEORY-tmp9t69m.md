---
status: Proposed
title: 'Gingrich, Horowitz, Perunov and England prove that for an ergodic Markov jump network with reversible transitions and local detailed balance, in its nonequilibrium steady state, the large-deviation rate function of any current that is a linear combination of edge currents lies below the quadratic (j_d − j^π_d)²Σ^π/(4(j^π_d)²), so current fluctuations are always at least as likely as linear response predicts, and that every such current therefore obeys the thermodynamic uncertainty relation ε²_d Σ^π ≥ 2, tightest for the dissipation current itself and in linear response'
promote_when: >-
  The proof in the paper's Derivation section (the level-2.5 rate
  function, the contraction bounded by evaluating at the steady-state
  density, the edgewise quadratic bound on Ψ and the trial current j*) has
  been checked step by step, and the inequality ε²_d Σ^π ≥ 2 with
  saturation of I(Σ) at Σ = ±Σ^π has been reproduced numerically on at
  least one multicyclic network. The numerical half is done on the
  paper's four-state network (NOTE-tmpri2np); the step-by-step check of
  the proof remains.
version: 1
tags:
- thermodynamics
- information-theory
date: '2026-11-22'
source:
- LIT-2981
bears_on:
- QUESTION-452
summary: >-
  Gingrich and colleagues (2016), [LIT-2981](../literature.d/LIT-2981.md), read in [NOTE-tmpri2np](../notes.d/NOTE-tmpri2np.md). The
  general proof of the thermodynamic uncertainty relation that Barato and
  Seifert ([LIT-1885](../literature.d/LIT-1885.md), [THEORY-1268](THEORY-1268.md)) proved only in linear response and for
  unicyclic networks and otherwise conjectured: for every current of a
  Markov jump network, far from equilibrium included, and as a bound on
  the whole rate function, so on rare fluctuations as well as the
  variance. Long-time, steady-state, reversible transitions only.
---
<!-- inactive-ok-file: LIT-tmp3eet2 — Deferred; Pietzonka, Barato and Seifert, the companion conjecture of the generalized-current bound -->

# THEORY-tmp9t69m: Gingrich, Horowitz, Perunov and England prove that for an ergodic Markov jump network with reversible transitions and local detailed balance, in its nonequilibrium steady state, the large-deviation rate function of any current that is a linear combination of edge currents lies below the quadratic (j_d − j^π_d)²Σ^π/(4(j^π_d)²), so current fluctuations are always at least as likely as linear response predicts, and that every such current therefore obeys the thermodynamic uncertainty relation ε²_d Σ^π ≥ 2, tightest for the dissipation current itself and in linear response

## Source

Gingrich, Horowitz, Perunov and England, "Dissipation bounds all
steady-state current fluctuations", Phys. Rev. Lett. 116, 120601 (2016),
[LIT-2981](../literature.d/LIT-2981.md), read from the arXiv v3 LaTeX source of 1512.02212 in
[NOTE-tmpri2np](../notes.d/NOTE-tmpri2np.md).

## What was actually shown

- Eq. 3, the edgewise bound: I(j) ≤ I_LR(j) = Σ_{y<z} (j(y,z) −
  j^π(y,z))²σ^π(y,z)/(4 j^π(y,z)²), saturated at j = j^π and at j = −j^π,
  "as our bound also satisfies the fluctuation theorem for currents".
- Eq. 4, for any generalized current j_d = Σ d(y,z) j(y,z): I(j_d) ≤
  (j_d − j^π_d)²Σ^π/(4(j^π_d)²); "this bound is tightest, and indeed as
  strong as the linear-response bound, when d=F".
- Eq. 8: "we have a general proof of the conjectured thermodynamic
  uncertainty relation", ε²_d Σ^π ≥ 2, from I''(j^π_d) = 1/Var(j_d); and
  an edgewise version, Var(j(y,z)) ≥ 2 j^π(y,z)²/σ^π(y,z).
- Abstract: "nonequilibrium current fluctuations are always more likely
  than what is expected from a linear-response analysis"; the higher-order
  corrections in the force "must have a negative sum" (Eq. 13).
- A design principle: "with a fixed energy budget, it is impossible to
  surpass the linear-response bound, no matter how complex the design."
- Proof: level-2.5 large deviations, contraction bounded at p = π, an
  edgewise quadratic bound on the level-2.5 function.

What could have failed: a multicyclic network far from equilibrium could
have had a current with ε²_d Σ^π < 2, as Barato and Seifert's conjecture
allowed; the proof rules it out for every current. Checked numerically on
the paper's four-state network ([NOTE-tmpri2np](../notes.d/NOTE-tmpri2np.md)).

## What this does not say

- Not for finite times (the variance is the long-time scaled one), time-
  dependent driving, occupation (density) observables, or one-way
  transitions, which make the bound vacuous.
- Not tight far from equilibrium for generic currents.
- Not an extremum principle: it bounds dissipation given precision, and
  says nothing about which state a system selects.

## Connections

Completes [THEORY-1268](THEORY-1268.md) (the proof it said was not held). Bears on
[QUESTION-452](../questions.d/QUESTION-452.md): the bound holds for any current, but maintenance is not
shown to be one. Respects the current fluctuation theorem ([THEORY-431](THEORY-431.md)).
Contrast with [THEORY-1830](THEORY-1830.md) (Tu), which prices a different observable. The
generalized-current bound was conjectured at the same time by Pietzonka,
Barato and Seifert ([LIT-tmp3eet2](../literature.d/LIT-tmp3eet2.md), registered, Deferred).
