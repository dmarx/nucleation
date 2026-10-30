---
number: 928
status: Active
formerly:
- THEORY-tmp3wkwk
title: 'Two softmax learners that update every action''s reward memory each step with its average reward against the other''s current play, the memories decaying at rate α, follow, in the limit of learning slow relative to play, coupled replicator equations plus a term α Σ x_j log(x_j / x_i) toward uniform play; in a two-player matrix game, without decay the dynamics preserve phase volume in log-ratio coordinates and are Hamiltonian when the game is zero-sum with an interior Nash equilibrium, and with decay the volume contracts at rate (N − 1)(α_X + α_Y)'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Narrowed and promoted to Active at the status review's ruling (the
    owner delegated these rulings), under ADR-065 §5 and ADR-047's "Where a
    narrowing's dropped claims go". A second checker (the twenty-fourth
    status review) re-derived the limit, the dissipation rate and the
    Hamiltonian structure, and checked them by script with controls; the
    steps are in the note of 2026-10-30. The title now states the
    hypotheses the source states and the old title left out: the
    full-information update, the slow-learning limit and, for the
    Hamiltonian clause, an interior Nash equilibrium. Without them it is
    false, as Q-learning shows (THEORY-932). That is routed as kind 3, a
    mis-statement, in the note of 2026-10-30. The version-of-record demand
    is dropped under ADR-065 §4. The discrepancy it names is in Eq. 14,
    the three-agent extension, which the title does not restate, and the
    derivation fixes Eq. 6's sign independently of any copy. NOTE-1144
    records the copy read (arXiv v2). The old title: Two softmax reinforcement learners whose reward memories decay at rate α follow coupled replicator equations plus a term α Σ x_j log(x_j / x_i) toward uniform play; without decay the dynamics are conservative, Hamiltonian in zero-sum games, and with decay they are dissipative. The old
    promote_when: The derivation reproduced independently from the stated update rules (softmax choice over reward memories with decay, every action's memory updated with its average reward, learning slow relative to play), and the version of record checked for the sign of the decay term, which v2 prints inconsistently between Eq. 6 and Eq. 14. It is refuted by an error in the limit. Results for Q-learning in which only the chosen action is updated are a different rule (THEORY-932) and neither promote nor refute this.
tags:
- game-theory
- learning-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-1520
summary: >-
  Sato & Crutchfield (arXiv 2002; PRE 2003), LIT-1520, read in full from
  arXiv v2 in NOTE-1144, Eqs. 1–13. The entropy-like term is what memory
  decay becomes under softmax choice. The limit, the dissipation rate and
  the Hamiltonian were re-derived, second-checked at the status review of
  2026-10-30. The model updates every action's memory at the same rate, so
  it is the full-information case, not Q-learning as usually run.
---
<!-- inactive-ok-file: NOTE-1144 THEORY-938 THEORY-936 CLAIM-443 CLAIM-444 — Proposed or new; the source and the accounts this bears on, named -->

# THEORY-928: Two softmax learners that update every action's reward memory each step with its average reward against the other's current play, the memories decaying at rate α, follow, in the limit of learning slow relative to play, coupled replicator equations plus a term α Σ x_j log(x_j / x_i) toward uniform play; in a two-player matrix game, without decay the dynamics preserve phase volume in log-ratio coordinates and are Hamiltonian when the game is zero-sum with an interior Nash equilibrium, and with decay the volume contracts at rate (N − 1)(α_X + α_Y)

## Source

Yuzuru Sato and James P. Crutchfield, "Coupled replicator equations for the
dynamics of learning in multiagent systems", *Physical Review E* 67:015206
(2003), [LIT-1520](../literature.d/LIT-1520.md), read in full in [NOTE-1144](../notes.d/NOTE-1144.md) from arXiv:nlin/0204057v2,
Eqs. 1–13 (pp. 1–2).

## What was actually shown

- **The rule.** Memories Q_i(n + 1) − Q_i(n) = R_i − αQ_i(n), choice
  x_i ∝ exp(βQ_i).
- **The limit.** With learning slow relative to play, so R_i is action i's
  average reward against the other's current mix,
  ẋ_i/x_i = β[R_i − Σ_j x_j R_j] + α Σ_j x_j log(x_j/x_i) (Eq. 6). The
  derivation is three lines, and the reading re-derived it: the decay term
  −αβ(Q_i − x·Q) is −α(log x_i − x·log x) under softmax.
- **Structure.** For bilinear rewards the phase volume in log-ratio
  coordinates contracts at rate (N − 1)(α_X + α_Y) (Eq. 10). At α = 0 the
  system preserves phase volume. If the game is zero-sum with an interior
  Nash equilibrium it is Hamiltonian (Eq. 11). The time average of an
  interior orbit is the Nash equilibrium (p. 2, citing Schuster et al.).

## What this does not say

- **That this is Q-learning.** No states, no bootstrapping, and every
  action's memory updated each step whether chosen or not. Kaisers and
  Tuyls show that the same equation describes Q-learning only after a
  frequency adjustment ([THEORY-932](THEORY-932.md)).
- **What the rest points are.** It does not say so, but with α > 0 the
  interior rest points of Eq. 8 satisfy β(Ay)_i − α log x_i = const, that
  is, x is a softmax best response to y at temperature α/β: logit
  equilibria, not Nash equilibria. This is my reading of the equations.
- **Anything for more than two agents** beyond the linear three-agent
  extension.

## Connections

- **[THEORY-938](THEORY-938.md).** The contrast that matters. Cross learning has no
  forgetting term and is absorbed in a vertex. Here forgetting is a force
  towards uniform play, and the boundary is repelling.
- **[CLAIM-443](../claims.d/CLAIM-443.md).** The schematic rule's forgetting term −λE has this
  reading under softmax selection: decay of a learned bias is pressure
  towards equal authority, and its rate sets how hard the system
  re-explores.
- **[CLAIM-444](../claims.d/CLAIM-444.md).** The coupled, two-population case of the replicator
  reading, derived for learners.

## Note of 2026-10-30: the re-derivation, written out

The second check at the status review (ADR-065 §5) followed each step.

1. **The limit.** Q̇_i = R_i − αQ_i, and x_i = e^(βQ_i)/Σ_j e^(βQ_j)
gives ẋ_i/x_i = β(Q̇_i − Σ_j x_j Q̇_j). So ẋ_i/x_i = β(R_i − x·R) −
αβ(Q_i − x·Q). The softmax gives βQ_i = log x_i + log Z, so β(Q_i − x·Q) =
log x_i − x·log x. Hence ẋ_i/x_i = β(R_i − x·R) + α Σ_j x_j log(x_j/x_i),
Eq. 6 with its printed sign. The term is positive for actions played less
than the log-average, so it pulls toward uniform play.

2. **Dissipation.** In a matrix game, R^X = Ay. In u_i = log(x_{i+1}/x_1)
the system is u̇_i = β_X[(Ay)_{i+1} − (Ay)_1] − α_X u_i (Eq. 9). The
payoff part depends on v only, so ∂u̇_i/∂u_i = −α_X, and likewise
∂v̇_j/∂v_j = −α_Y. The divergence is −(N − 1)(α_X + α_Y). It is zero at
α = 0 for any A and B.

3. **Hamiltonian.** Let B = −Aᵀ and let (p, q) be an interior
equilibrium, so that Aq and Bp have equal entries. Then (Ay)_{i+1} −
(Ay)_1 = Σ_k C_ik (y_{k+1} − q_{k+1}), with C_ik = a_{i+1,k+1} − a_{1,k+1}
− a_{i+1,1} + a_{11}. Since ∂/∂v_k Σ_j q_j log y_j = q_{k+1} − y_{k+1},
put H = (1/β_X) Σ p_i log x_i + (1/β_Y) Σ q_j log y_j. Then u̇ = P ∂_v H
and v̇ = −Pᵀ ∂_u H with the constant matrix P = −β_X β_Y C. A constant
skew-symmetric structure is a Poisson structure, so the flow is
Hamiltonian. Without an interior equilibrium the payoff differences do
not vanish at a common point, and the construction fails. The paper's
Eq. 11 prints H without the weights 1/β_X and 1/β_Y. As printed, it is
conserved only when β_X = β_Y.

A script (numpy, in the session's scratchpad, s928_sc.py) checked these
steps in three parts.

- **The limit.** It iterated the stated memory rule with step h for a
  random 3 × 3 game and compared x with Eq. 6. The largest gap was
  3.3 × 10⁻⁵ at h = 10⁻² and 3.3 × 10⁻⁶ at h = 10⁻³, falling in proportion
  to h. As a control, the same equation with the decay term's sign
  flipped, as Eq. 14 prints it, missed by 3.4 × 10⁻² at h = 10⁻³.
- **Dissipation.** The divergence of Eq. 9, taken by finite differences
  at 200 random points with random games and decay rates, matched
  −(N − 1)(α_X + α_Y) to 4 × 10⁻¹⁰.
- **The Hamiltonian.** The game was rock–scissors–paper with tie rewards
  ε_X = −ε_Y = 0.5, with β_X = 1 and β_Y = 0.6, integrated to t = 20. The
  weighted H stayed constant to 2.5 × 10⁻¹⁴, and the vector field equalled
  J∇H at 100 random points to 2 × 10⁻⁹. Three controls each had to show
  drift, and each did. The unweighted H of Eq. 11 moved by 0.33. With
  α = 0.05, H moved by 0.69. In the non-zero-sum game ε_Y = 0.1 it moved
  by 0.93.

## Note of 2026-10-30: the clauses the narrowing drops

The old title said that softmax learners with decaying memories follow
the equation, with no condition on how memories are updated or how fast.
Read so, it is false. Q-learning is softmax over decaying memories, yet
it updates only the chosen action, and its expected dynamics carry a
factor x_i that the equation lacks (THEORY-932). The old title also said
"Hamiltonian in zero-sum games" with no condition, where the source
states the result for an interior Nash equilibrium. Both conditions are
the source's own. These clauses were mis-statements, so they are
recorded here only (ADR-047's kind 3), and the title now states the
conditions.

The version-of-record demand concerned Eq. 14. v2 prints the three-agent
extension's decay term as −α_X I_i^X, against Eq. 6's +α_X I_i^X. Step 1
shows that, for the stated rule, Eq. 6's sign is right. Whether the
Physical Review E version corrects Eq. 14 is not checked, and nothing in
the record uses the three-agent equation.

## Note of 2026-10-30: Eq. 11 as printed

The paper's Eq. 11 gives H = −(Σ_j x*_j u_j + Σ_j y*_j v_j) + log(1 + Σ_j
e^(u_j)) + log(1 + Σ_j e^(v_j)), which is −Σ x*_i log x_i − Σ y*_j log
y_j, with no weights. By step 3 of the re-derivation above, the conserved
quantity is (1/β_X) Σ p_i log x_i + (1/β_Y) Σ q_j log y_j. The printed H
is conserved only when β_X = β_Y. The script's control showed this: with
β_X = 1 and β_Y = 0.6 the unweighted H moved by 0.33 over t = 20, while
the weighted H held to 2.5 × 10⁻¹⁴. The title asserts only that the flow
is Hamiltonian, which holds with the weighted H.
