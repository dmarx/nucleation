---
status: Proposed
title: 'A kinetic constraint-growth model on random lattices, run to test out of sample a non-monotone predictor of productive seed sets generalised from folding islands: adding a seed already in its target state can halve the chance of exact assembly, the island-based predictors, monotone or not, do not say which additions hurt, and a post hoc count of the states each component could take when it first reaches the binding threshold does on fresh architectures, with weak flags'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23. The code, tests, pre-registration
    with its two amendments, and outputs are under
    scratch/studies/lead-183/.
standing: documented
kind: executed-study
tags:
- complex-systems
- probabilistic-modeling
- mathematics
- natural-sciences
date: '2026-11-23'
line:
- realizability
- formal-apparatus
illustrates:
- CLAIM-599
- CLAIM-562
bears_on:
- QUESTION-380
draws_on:
- THEORY-1418
- THEORY-1451
summary: >-
  QUESTION-380 asks for a predictor, computed from a constraint
  architecture, of which local subsystems raise or lower the chance of a
  coherent global organization, tested in a system other than the one it
  was built for; UFI, the folding-island predictor of Stern, Pinson and
  Murugan (THEORY-1418), cannot flag a superset that lowers the chance. A
  race reading of folding islands (VIC: a component counts only if the
  first seed front to reach it forces it) and an alternative (ICN: island
  coverage per disconnected nucleus) were pre-registered and tested on a
  kinetic constraint-growth model in the threshold-2 regime of the kinetic
  tile assembly model (THEORY-1451). Adding a seed already in its target
  state can halve the chance of exact assembly (38 of 40 significant
  decreases confirmed with 3000 runs), and island coverage predicts the
  chance better than the number of seeds. Neither VIC nor ICN transfers: VIC
  ranks seed sets worse than the monotone island union (Spearman 0.22
  against 0.54) and flags 193 additions as harmful of which 2 are. The
  harmful seeds have large islands; the errors are order effects at the
  binding threshold. A post hoc predictor, threshold-front forcing (TFF),
  meets the pre-registered criterion on five fresh architectures (Spearman
  0.64 against 0.48, AUC 0.94, recall 0.66, precision 0.11). The model is
  the assistant's. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CASE-tmp2a9lm: A kinetic constraint-growth model on random lattices, run to test out of sample a non-monotone predictor of productive seed sets generalised from folding islands: adding a seed already in its target state can halve the chance of exact assembly, the island-based predictors, monotone or not, do not say which additions hurt, and a post hoc count of the states each component could take when it first reaches the binding threshold does on fresh architectures, with weak flags

## The predictors

A **constraint architecture** is a graph, a finite state set per component,
a relation per edge, and a target configuration x* satisfying every
relation. A **seed set** S is a set of components established in their
target states before assembly starts; every seed set is internally
compatible, since all of it agrees with x*.

- **Island** I(S): what S forces. As first registered, the components
  reduced to {x*_v} by arc consistency with S clamped; as amended, the
  forward forcing closure, setting any component next to set ones whose
  states compatible with its set neighbours are exactly {x*_v}. Stern et
  al.'s folding island is the largest subset that folds correctly "if that
  subset is cut out and actuated" (THEORY-1418), which the forward closure
  follows.
- **VIC**, Voronoi-island coverage (the primary predictor): the share of
  components v for which the nearest seeds, by hop distance, include v in
  their own single-seed islands. A component counts only if the front that
  reaches it first is one whose island forces it. Adding a seed can lower
  VIC: it takes over components that a farther seed's island forced. This
  is the paper's account of the added actuator "with a very small folding
  island" that stops a successful fold, written as a race.
- **ICN**, island coverage per nucleus (the registered alternative): joint
  island coverage divided by the number of disconnected island components
  containing a seed.
- **Monotone baselines**: the number of seeds; the union of single-seed
  islands (the UFI analogue); joint island coverage. None can predict a
  decrease.
- **TFF**, threshold-front forcing (post hoc, the second amendment): grow
  deterministically from S in synchronous rounds; in each round every
  component bound with strength at least τ = 2 is a candidate (if none, every
  touched one is); its options k_v are its states compatible with its set
  neighbours at that moment; set all candidates to target and repeat.
  TFF(S) = −Σ log k_v. It uses the architecture and the growth rule's
  threshold, not a simulation of the stochastic dynamics.

## The test system

Not a self-folding sheet. An 8 × 8 lattice, q = 4 states, a random
target. Each edge is rigid with probability p_r (a bijection through the
target pair, bond strength 2) or ambiguous (the target pair and one
distractor pair from each side, strength 1). An unset component bound to
set neighbours with total strength s attaches at rate κ^(s − 2), κ = 100,
taking a state uniformly among those compatible with every set neighbour;
no compatible state is a jam. An untouched component nucleates at rate
10⁻⁴ into a random state. No detachment: any wrong state is final. Success
is exact assembly of x*; V(S) is estimated from 300 Gillespie runs per set.
Per architecture: the empty set, 10 candidate seeds singly and in all 45
pairs, and 40 random triples, giving 220 additions S → S ∪ {c}.

**Pre-registration.** The predictors, the system, the metrics and the
criterion were committed before any run. **Transfer** means, pooled over
five architectures, an AUC of at least 0.7 for telling significant
decreases from significant increases by the predictor's change, a recall
of at least 0.5 of significant decreases, and a Spearman correlation with
V no more than 0.05 below the best monotone baseline's. A significant
decrease exceeds 2 standard errors and 0.05.

**Two amendments, each committed before the run it governs.** (1) With
random relations the target is the unique solution, and arc consistency
finds it from any single seed: every single-seed island was the whole
lattice, so all island-based predictors were constant and the first test
was void. The dynamics also failed almost always. The island became the
forward closure; the edges two-sided, with strengths and the threshold
rate, a standard kinetic tile assembly regime; κ, ε and p_r were chosen on
development architectures for a V that is not degenerate, without
computing any predictor's score there. (2) After the amended test, TFF was
designed from its failures and tested on five architectures never
generated before.

**Checks.** Thirteen pytest tests: islands on hand-built chains, VIC's
exact values including a decrease, ICN's component count, TFF on chains, a
rigid chain that always assembles, an ambiguous edge that succeeds half
the time (0.50 ± 0.04 in 4000 runs), context resolving ambiguity, the
target satisfying every relation, the metrics.

## Results

| test | predictor | Spearman with V | AUC | recall | precision | transfer |
|---|---|---|---|---|---|---|
| as first registered | every island-based one | constant | — | — | — | void |
| amended, architectures 0–4 | VIC | 0.22 | 0.70 | 0.25 (2 of 8) | 0.01 | no |
| amended, architectures 0–4 | ICN | 0.52 | 0.88 | 0 | 0 | no |
| amended, architectures 0–4 | UFI analogue | 0.54 | 0.88 | 0 | — | cannot flag |
| amended, architectures 0–4 | number of seeds | 0.14 | 0.50 | 0 | — | cannot flag |
| fresh, architectures 200–204 | VIC | 0.21 | 0.84 | 0.58 | 0.09 | no |
| fresh, architectures 200–204 | ICN | 0.48 | 0.77 | 0 | 0 | no |
| fresh, architectures 200–204 | TFF (post hoc) | 0.64 | 0.94 | 0.66 | 0.11 | yes |
| fresh, architectures 200–204 | joint island coverage | 0.48 | 0.77 | 0 | — | cannot flag |
| fresh, architectures 200–204 | number of seeds | 0.26 | 0.50 | 0 | — | cannot flag |

- **Adding a target-consistent seed can hurt.** Of the 40 significant
  decreases in the amended run (8 on the primary architectures, 32 on the
  sensitivity ones at p_r = 0.4 and 0.6), 38 are confirmed at z < −2 with
  3000 fresh runs; on the sensitivity architectures the median fall is
  0.07, typically halving V (for example 0.16 to 0.07 when seed 45 joins
  seed 3 at p_r = 0.6). Every such seed set is jointly compatible with the
  target, so this is upward non-closure (CLAIM-599) without an
  incompatibility built in.
- **Placement beats count.** Island coverage ranks seed sets well above
  the number of seeds in both runs (0.54 against 0.14; 0.48 against 0.26),
  CLAIM-562's first finding outside self-folding sheets.
- **The race reading fails.** VIC flags 193 additions on architectures
  0–4 and 251 on 200–204; 2 and 22 of them are significant decreases. Its
  ranking of seed sets is worse than the monotone union's in both runs.
- **Why.** Post hoc: the three candidate seeds whose mean effect was
  harmful have islands of 25, 62 and 62 of 64 components, not small ones.
  In 3000 runs of seed 58 against seeds 22 and 58 at p_r = 0.6, the failures
  move to components inside both seeds' islands, attached at threshold
  through two weak bonds with the same distractor, so with two states open.
  The patient closure waits until such a component is forced; the growth
  does not. A seed changes the order in which components reach threshold,
  and so which of them are decided with a choice still open.
- **Threshold-front forcing.** TFF tracks exactly that and transfers to
  fresh architectures by the registered criterion. Its flags are weak:
  flagged additions change V by −0.011 on average (55 % fall), unflagged
  ones by +0.023 (24 % fall).

## What it does not show

- **Transfer of TFF across systems.** TFF was designed on this system's
  failures; its success on fresh architectures is transfer within one
  system. Only VIC, built from the self-folding sheets, was tested across
  systems, and it failed.
- **Anything about VIC in its home kind of system.** The test system has
  no coherent alternative branch: a wrong state is a local error, not the
  start of a self-consistent distractor fold, which a self-folding sheet's
  vertices offer.
- **DNA origami.** The model and its rates are the assistant's; V is low
  throughout (at most 0.51); 8 × 8 lattices, q = 4, 300 runs per set.
- **A constraint-only predictor.** TFF needs the threshold of the growth
  rule, a condition of the dynamics, as QUESTION-380 says an answer must
  state.
