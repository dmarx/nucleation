---
status: Read
paper: 'LIT-1233'
title: 'Hofbauer and Schreiber — Permanence via invasion graphs'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from arXiv 2204.03773v2 (30 July 2022,
    https://arxiv.org/pdf/2204.03773, 19 pages), text extracted with
    pdftotext. The Journal of Mathematical Biology version was not
    compared. Read: the abstract, §§1–5, the proofs in Appendices A and B,
    the parameter values in Appendix C and the references. Figures 1–3
    were read from captions and text; no number was taken from a chart.
    The invasion conditions of the switching-predator example (§4.2)
    were recomputed by hand from the stated equilibria and disagree with
    the text's labelling (see Limitations). The Lotka–Volterra examples
    of Figure 1 were not re-simulated.
date: '2026-10-29'
summary: >-
  For ecological ODEs whose invasion growth rates have well-defined,
  nonzero signs on each subcommunity, it defines the invasion graph (edges
  S → T when every species in T but not S can invade S and every species
  lost cannot invade T) and proves that when the graph is acyclic,
  robust permanence holds if, and essentially only if, each species i has
  a positive invasion growth rate at every −i community. With cycles,
  signs are not enough.
---
<!-- inactive-ok-file: LIT-1219 — Deferred; Chesson's framework named as the theory this paper makes rigorous, nothing here rests on its reading -->

# NOTE-tmphiq73: Hofbauer and Schreiber — Permanence via invasion graphs

## Contribution

Modern coexistence theory equates coexistence with positive invasion
growth rates, without saying when signs suffice or which rates must be
positive. This paper answers both for deterministic models: signs suffice
when the invasion graph has no cycle, and then the rates that matter are
species i's at its −i communities, the subcommunities without i that no
other missing species can invade.

## Key insight

Coexistence is a statement about community assembly. Draw every
subcommunity and every possible transition by invasion; if no sequence of
invasions returns where it started, the boundary dynamics have a Morse
decomposition, and permanence reduces to checking that the end-points of
assembly without each species can be invaded by it.

## Assumptions

- Equations (1): dx_i/dt = x_i f_i(z), dy/dt = g(z), with auxiliary
  variables y in a compact set (A1: local Lipschitz; A2: dissipative, a
  compact global attractor).
- **A3a**: for each ergodic measure µ on the extinction set, r_j(µ) ≠ 0
  for every species j not supported by µ.
- **A3b**: r_j has the same sign at any two ergodic measures with the
  same support. It holds for Lotka–Volterra and replicator systems and
  whenever each face carries one invariant measure; it fails, for
  example, for two predators on one prey with a type II response
  (McGehee and Armstrong).
- Coexistence means robust permanence: permanence that survives small
  C⁰ perturbations of the vector field.

## Key results

- **Lemma 1.** Resident species have r_i(µ) = 0.
- **Definition.** Invasion scheme: the signs r_i(S) for every proper
  subcommunity S. Invasion graph: S → T iff S ≠ T, r_j(S) > 0 for all j ∈
  T \ S, and r_i(T) < 0 for all i ∈ S \ T.
- **Theorem 1.** A1–A3 and an acyclic invasion graph: robustly
  permanent if every subcommunity can be invaded by some species.
- **Corollary 1.** It suffices that r_i(S) > 0 at every −i community S.
  With C² vector fields, Remark 3 gives the converse: an uninvadable
  subcommunity has a stable set reaching the interior, so permanence
  fails.
- **Corollary 2 and Proposition 1.** Hofbauer's average Lyapunov
  condition (positive weights p with Σ p_i r_i(µ) > 0 on all boundary
  measures) follows from signs alone iff the invasion scheme is
  sequentially permanent, a nested build-up of permanent communities, a
  strictly smaller class than acyclic graphs.
- **Lotka–Volterra.** With one interior equilibrium per face, r_i(S) =
  sgn((Ax*)_i + b_i), so the graph comes from linear algebra. Figure 1:
  two five-species competitive systems, both acyclic; one is robustly
  permanent, the other has nine −i communities, three uninvadable.
- **Switching predator** (§4.2): predator-mediated coexistence of
  bistable prey is possible, unlike a non-switching predator; the scheme
  is not sequentially permanent.
- **Periodic chemostat** (§4.3): numerically computed invasion graphs
  account for the loss of species 3 at a = 0.325, of species 2 at a =
  0.275 and of species 1 and 2 at a = 0.2.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | With an acyclic invasion graph, signs of invasion growth rates decide robust permanence | strong | Theorem 1, Corollary 1, Remark 3; proofs read |
| C2 | Only species i's rate at each −i community needs checking | strong | Corollary 1 |
| C3 | Average Lyapunov functions follow from signs only for sequentially permanent schemes | strong | Proposition 1, proof read |
| C4 | For stochastic models, acyclic graphs with invadable −i communities give stochastic persistence | conjecture | §5 |

## Concepts

- **Invasion growth rate r_i(µ)**: ∫ f_i dµ, the long-run per-capita
  growth of species i introduced at vanishing density into the dynamics
  of µ.
- **−i community**: a subcommunity without i in which every other
  missing species has a negative invasion growth rate. Found in practice
  by simulating from all species but i and removing the "atto-foxes".
- **Robust permanence**: a compact interior attractor, persisting under
  small perturbations of the equations.
- **Sequential permanence**: an ordering of species such that each in
  turn has nonnegative rates at every remaining community.

## Connections

It makes rigorous the "−i community" of Chesson (1994) and the
recovery-from-rarity logic of Chesson's framework ([LIT-1219](../literature.d/LIT-1219.md)); its
assembly graph is related to Serván and Allesina's (2021) but allows
multi-species invasions. Rock–paper–scissors (May and Leonard 1975) is the
cyclic case where signs fail. None of these three is registered.

## Bearing on the record

- **[QUESTION-132](../questions.d/QUESTION-132.md)** defines a recovery exponent λ_i along the resident
  regime and takes λ_i > 0 as the mark of stabilizing coexistence. That
  λ_i is exactly r_i(µ) here. The reading adds two conditions the
  question should carry. (a) Positive recovery at one resident regime is
  not enough: it must be positive at every −i community, which may be a
  much smaller community than "all the others". (b) Signs decide only if
  the invasion graph is acyclic. With cyclic replacement among operators,
  rock–paper–scissors among roles, all recovery exponents can be
  positive and coexistence still fail.
- **[QUESTION-083](../questions.d/QUESTION-083.md)**: the −i communities are the "early entrants shape
  which roles later ones can hold" structure the synthesis read into the
  paper (LIT, "Why this is here"). It is the right reading: −i
  communities are assembly end-points, and whether a role can be filled
  depends on the end-points reached without it.
- **[CLAIM-369](../claims.d/CLAIM-369.md)**, a question for the coordinator rather than a finding:
  in the symmetric, gradient case the objective L decreases along every
  trajectory, which should rule out heteroclinic cycles and so cyclic
  invasion graphs. If so, [CLAIM-369](../claims.d/CLAIM-369.md)'s class always satisfies this paper's
  acyclicity hypothesis. The paper does not state this and the reading
  did not prove it.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **A labelling error in §4.2.** The text says invasibility of {1, 2}
  and {1, 3} requires a/d > α and of {2, 3} requires a/d > 1 + α. From the
  stated equilibria, prey 2 invading {1, 3} (x1 = d/a, y = 1) has rate
  r(1 − αd/a), and prey 1 invading {2, 3} (x2 = d/a, y = 0) has the same
  rate, so both need a/d > α. The predator invading {1, 2} (x1 = x2 =
  1/(1 + α), y = ½) has rate a/(1 + α) − d, so needs a/d > 1 + α. The two
  labels are swapped between {1, 2} and {2, 3}. The overall condition and
  the conclusion are unaffected.
- **Other slips.** "As the invasion graphs for α ≠ 0 are acyclic"
  probably means α ≠ 1; §4.3 gives β2 = −.3, the Figure 2 caption 0.3; in
  Appendix B and after Corollary 2, IG is written where IS is meant.
- Deterministic models only; A3b excludes common non-Lotka–Volterra
  cases; cyclic graphs are left open.

## Open questions

- Does the stochastic conjecture of §5 hold?
- For cyclic invasion graphs, which quantitative information beyond
  signs decides permanence, and how should the rates then be decomposed
  into mechanisms?
