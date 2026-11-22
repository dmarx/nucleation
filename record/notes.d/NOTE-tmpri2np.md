---
status: Read
paper: LIT-2981
title: 'Gingrich, Horowitz, Perunov & England — Dissipation bounds all steady-state current fluctuations'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    From the arXiv LaTeX source of 1512.02212v3 (bound.tex, bound.bbl,
    three figure PDFs; v3 of 4 February 2016, the authors' manuscript of
    the published letter), with the arXiv PDF used to confirm the version
    and length (5 pp.), both fetched 2026-11-22 without obstacle. Read in
    full: abstract, main text, the three figure captions, the Derivation
    section, acknowledgments; the bibliography only for entries cited in
    the text; figures through their captions. The PRL version
    (doi:10.1103/PhysRevLett.116.120601) was not compared. Read by a
    reader subagent; filed by a second one, which rechecked every quote
    used here against bound.tex and reran the reader's numerical check.
    No email address sent.
date: '2026-11-22'
summary: >-
  For a Markov jump network with reversible transitions and local detailed
  balance in its steady state, the rate function of every current lies
  below a linear-response quadratic weighted by dissipation, so
  nonequilibrium current fluctuations are always at least as likely as
  linear response says, and the thermodynamic uncertainty relation
  ε²_d Σ^π ≥ 2 holds for every current: the general proof of Barato and
  Seifert's conjecture.
---
<!-- inactive-ok-file: LIT-tmp3eet2 — Proposed, Deferred or new; the account this reading files and the companion conjecture it names -->
<!-- inactive-ok-file: CLAIM-815 THEORY-1366 — Proposed; large-deviation entries named as background -->

# NOTE-tmpri2np: Gingrich, Horowitz, Perunov & England — Dissipation bounds all steady-state current fluctuations

## Contribution

The first general proof of the thermodynamic uncertainty relation for
steady-state currents of Markov jump processes, multicyclic networks far
from equilibrium included, which Barato and Seifert ([LIT-1885](../literature.d/LIT-1885.md),
[THEORY-1268](../theory.d/THEORY-1268.md)) had proved only in linear response and for unicyclic
networks. It proves more than the relation: a bound on the whole
large-deviation rate function of currents, so on rare fluctuations as
well as the variance.

## Key results

- **Edgewise bound** (Eq. 3): I(j) ≤ I_LR(j) = Σ_{y<z}
  (j(y,z) − j^π(y,z))²σ^π(y,z)/(4 j^π(y,z)²), saturated "not only at the
  minimum of I, j = j^π, but also at the symmetric point j = −j^π, as our
  bound also satisfies the fluctuation theorem for currents".
- **Generalized currents** (Eq. 4): I(j_d) ≤ (j_d − j^π_d)²Σ^π/(4(j^π_d)²);
  "this bound is tightest, and indeed as strong as the linear-response
  bound, when d=F", giving I(Σ) ≤ (Σ − Σ^π)²/(4Σ^π) (Eq. 5).
- **The relation** (Eq. 8): "As a consequence of these bounds, we have a
  general proof of the conjectured thermodynamic uncertainty relation",
  ε²_d Σ^π ≥ 2, with I''(j^π_d) = 1/Var(j_d). "Thus, reducing current
  fluctuations carries a fundamental energetic cost." Edgewise:
  Var(j(y,z)) ≥ 2 j^π(y,z)²/σ^π(y,z). "These uncertainty relations are
  tightest in linear response and when d ∝ F, as predicted by Barato and
  Seifert."
- **Direction** (abstract): "nonequilibrium current fluctuations are
  always more likely than what is expected from a linear-response
  analysis"; the bounds "are not quadratic truncations of I for small
  currents, but originate in a linear-response expansion about small force
  or entropy production"; in the expansion in F, "All higher order
  corrections must have a negative sum."
- **Design** (closing): "for fixed average dissipation and current, the
  fluctuations are most suppressed in a near-equilibrium process"; "with a
  fixed energy budget, it is impossible to surpass the linear-response
  bound, no matter how complex the design."
- **Derivation**: level-2.5 rate function; contraction bounded by
  evaluating at p = π; an edgewise quadratic upper bound on the level-2.5
  function; the generalized bound by a trial current proportional to j^π.
- **Priority**: "we became aware of the preprint by Pietzonka, Barato, and
  Seifert [arXiv 1512.01221], which conjectures (4) as a universal bound"
  (registered as [LIT-tmp3eet2](../literature.d/LIT-tmp3eet2.md), Deferred).

## Check

The reader's script, rerun by the filer with `python3 -I`, takes the
four-state rates of the paper's Fig. 2 caption (r(1,2) = 3, r(1,3) = 10,
..., r(4,3) = 5), finds Σ^π = 6.2709, computes scaled cumulants from the
tilted generator, and over the dissipation current and 299 random
generalized currents finds min ε²_d Σ^π = 2.3401, attained at d = F, as
the paper says; I_WLR − I ≥ −2 × 10⁻⁶ at six sampled points per current
(Legendre transform on a grid, which can only underestimate I), with the
d = F gap at j = −Σ^π also −2 × 10⁻⁶, saturation to numerical precision.
The proof itself was not checked step by step.

## Assumptions

Finite state space, continuous-time Markov jump process, ergodic, unique
steady state; every transition reversible; local detailed balance, so
F(y,z) = ln[π(y)r(y,z)/(π(z)r(z,y))] is a jump's dissipation; steady
state and the long-time limit; currents that are linear combinations of
edge currents; k_B = 1.

## Concepts

Thermodynamic uncertainty relation; empirical current; large-deviation
rate function; level-2.5 large deviations; contraction principle; tilted
generator; local detailed balance; generalized current; edgewise entropy
production; fluctuation theorem for currents; ASEP.

## Bearing on the record

- **[LIT-2981](../literature.d/LIT-2981.md)**: read; Active. The exchange's A26 statement of the
  relation, Var(J_T)/⟨J_T⟩² ≥ 2/⟨Σ_T⟩ "for a suitable integrated current",
  is accurate as the long-time form of Eq. 8; "suitable" means any linear
  combination of edge currents.
- **[THEORY-1268](../theory.d/THEORY-1268.md)**: supports and completes. Its "What this does not say"
  reads "Proofs for general networks came later and are not held"; this is
  that proof. Its title's "states it as a conjecture" stays true of the
  2015 letter.
- **[LIT-1885](../literature.d/LIT-1885.md)**: background; the conjecture proved.
- **[QUESTION-452](../questions.d/QUESTION-452.md)**: qualifies and leaves open. The price holds for any
  current of a Markov jump network, far from equilibrium and for rare
  fluctuations, but that maintenance is such a current is not shown, and
  occupations are not covered.
- **[THEORY-1830](../theory.d/THEORY-1830.md)** (Tu): contrast; different observables, no conflict.
- **[THEORY-431](../theory.d/THEORY-431.md)** (fluctuation theorems): parallel; the bound respects the
  current fluctuation theorem.
- **[TERM-062](../terms.d/TERM-062.md)**: no bearing. The curation entry of 2026-11-21 pairs this
  work with [TERM-062](../terms.d/TERM-062.md); that pairing belongs to Shalizi and Moore
  ([LIT-2996](../literature.d/LIT-2996.md)). Its ideas are held in [THEORY-1268](../theory.d/THEORY-1268.md).
- Large-deviation entries ([THEORY-1366](../theory.d/THEORY-1366.md), [CLAIM-815](../claims.d/CLAIM-815.md), [LIT-1892](../literature.d/LIT-1892.md)): background
  only, same apparatus, different objects; left without notes.

## Limitations

- Markov jump processes with reversible transitions only; one-way
  transitions make F infinite and the bound vacuous.
- Long-time steady-state currents only: not finite time, periodic driving,
  occupation observables or underdamped dynamics.
- Tight only near equilibrium and for d ∝ F; far from equilibrium generic
  currents sit well inside it (Fig. 2 inset).
- Two numerical illustrations; the result itself is proved.
