---
status: Read
paper: 'LIT-tmp9zvdz'
title: 'Balduzzi et al. — Re-evaluating evaluation'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:1806.02643v2 (30 October 2018),
    the authors' "NIPS 2018, final version", a 20-page PDF under arXiv's
    non-exclusive distribution licence, extracted by pdftotext. Read:
    sections 1–5 (pp. 1–8) and appendices A–F (pp. 12–20), with every
    proof followed. The reference list was skimmed. Page numbers below are
    v2's. Every quotation was checked against the extracted text by
    script. The checks reported below were run by script
    (scratchpad/marlb_scripts/nash_copy.py and checks.py).
date: '2026-10-24'
summary: >-
  A methods paper with two short applications. It reads evaluation data
  as antisymmetric matrices. Elo is then the row mean of the log-odds,
  exact when they are curl-free and movable by copies, and the Schur
  decomposition gives a multidimensional Elo. Nash averaging scores agents
  and tasks against the maximum-entropy Nash equilibrium of a zero-sum
  meta-game. Its proved invariance covers exact copies, and only when that
  equilibrium is unique. A checked counterexample shows what happens
  otherwise.
---
<!-- inactive-ok-file: THEORY-tmp0fsks THEORY-tmpzogk3 — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-451 CLAIM-446 CLAIM-445 CLAIM-436 CLAIM-440 — Proposed; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpr1f7n: Balduzzi et al. — Re-evaluating evaluation

## What the paper does

**Setting.** Two kinds of evaluation data. Agent-vs-agent (AvA): a matrix
of win probabilities p_ij, turned into the antisymmetric log-odds matrix
A_ij = log(p_ij / p_ji). Agent-vs-task (AvT): a score matrix S, agents by
tasks, embedded in an antisymmetric (m + n)-square matrix. On the complete
graph, the paper takes the Hodge decomposition from Jiang et al. (the
record's [LIT-1439](../literature.d/LIT-1439.md)): every antisymmetric matrix is grad(div A) plus a
rotational part, orthogonally under the Frobenius inner product (p. 4).
div A is the row mean.

**Elo, read algebraically.**
- *Proposition 1.* Batch Elo is at a fixed point exactly when the predicted
  and observed win probabilities have the same row sums, so many win
  matrices share one rating, as many joints share marginals (p. 3).
- *Proposition 3.* If p_ij = σ(r_i − r_j), then div(logit P) = r. An Elo
  rating generating P exists if and only if curl(logit P) = 0, that is,
  log-odds around every triangle sum to zero. "Elo is, essentially, a
  uniform average in logit space" (p. 4). In rock-paper-scissors every
  rating is equal and Elo has no predictive power (p. 3).
- *Copies.* "an agent’s Elo rating can be inflated by instantiating many
  copies of an agent it beats (or conversely)" (p. 2). Appendix A's example
  is rock-paper-scissors at 0.9/0.1 with C copied, where the paper reports
  Elo moving from (0, 0, 0) to (−63, 63, 0, 0). The reading recomputed the
  batch fixed point of Proposition 1 at the stated α and found ±71.9.
  The sign and the point stand; the magnitude printed is not the fixed
  point.

**Multidimensional Elo.** The rotational part is approximated by a
low-rank antisymmetric C Ω Cᵀ from the Schur decomposition, giving
p̂_ij = σ(r_i − r_j + c_iᵀ Ω c_j). On eight Go programs from AlphaGo's
table, mElo₂ cuts the Frobenius error from 0.85 to 0.35 and gets every
likely winner right among αv, αp and Zen, where Elo gets two wrong
(p. 5). For AvT, Proposition 2 makes the SVD of the score residual and the
Schur decomposition the same thing: latent abilities of agents and latent
problems posed by tasks (p. 5).

**Nash averaging.** Desired properties (p. 6): P1, adding redundant copies
makes no difference; P2, robustness to small changes; P3, intuitive
results in basic cases. The meta-game: two players each choose a
distribution over agents, with payoff pᵀAq. Proposition 4: the game has a
unique symmetric Nash equilibrium of maximum entropy. The Nash average is
n = A p*, each agent's expected log-odds against the maximum-entropy Nash
team. Theorem 1:
- P1: invariant to redundancies;
- P2: a Nash for Â is an ε-Nash for A, ε = ‖A − Â‖_max (proved, p. 15);
- P3: p* is uniform exactly when div A = 0, and uniform on the top-rated
  agents when A = grad(r) (proved, p. 15).
Appendix D does the same for AvT, with one meta-player choosing agents and
the other environments.

**Atari** (pp. 7–8). 20 agents (including human, random and no-op) on 54
environments, scores rescaled to [0, 1] per environment. The support of
the equilibrium is five agents (distribDQN, rainbow, human, prior, popart)
and five environments. All supported agents tie, by the indifference
principle, "suggesting better-than-human performance has not yet been
achieved" (p. 2). But "We find a Nash equilibrium using an LP-solver; it
should be possible to find the maxent Nash using the algorithm in [71,
72]" (p. 7). The equilibrium shown is not the one Theorem 1 is about.

**What the authors concede** (p. 8). "Firstly, it is only as good as the
data: garbage in, garbage out." "Secondly, for good or ill, Nash averaging
removes control from the user." "Finally, Nash is a harsh master": it is
adversarial. Whether other invariant evaluations exist is left open.

## What it establishes and what it does not

**Proved, and re-derived here.** Propositions 1–4, Theorem 1's P2 and P3,
and Lemma 1, the key step for P1: since the game's value is zero, p is a
Nash equilibrium exactly when every agent scores at most zero against it,
so splitting a copied agent's mass in any proportion preserves the
condition, and merging copies reverses it.

**P1 as stated is not proved, and fails in general.** Lemma 1 is about
the Nash *set*. The maximum-entropy selection over the padded set
maximizes H(p) + p_c·log 2, the copied agent's mass picking up the entropy
of its split. When the original equilibrium is unique, p_c is fixed, the
even split is the maximum, and invariance holds. When the equilibria form
a segment, the extra term moves the maximizer. The proof never deals with
this. The appendix gestures at it: "If the copied row is not unique and
receives positive mass under maxent Nash, then maxent Nash will already be
spreading mass across the copies" (p. 14).

The reading's counterexample, checked by grid search over the simplex and
in closed form. Take rock, paper and scissors at ±1, a null agent D that
ties all three, and an agent E that loses to all three and beats D. The
Nash set is λ·(⅓, ⅓, ⅓) + (1 − λ)·D with λ ∈ [½, 1]. Maximum entropy gives
λ = ¾, p* = (¼, ¼, ¼, ¼, 0), and E's Nash average is −0.5. Copy D. The
maximum-entropy equilibrium becomes (⅕, ⅕, ⅕, ⅕, 0, ⅕) instead of the
"invariant" (¼, ¼, ¼, ⅛, 0, ⅛), and E's Nash average rises to −0.2. D's
column differs from every other, as Definition 3 requires. So both the
distribution and the Nash averages move under one copy. Equilibria are
unique for generic matrices, so the failure needs ties, and an empirical
matrix with draws or saturated win rates can have them.

**What the invariance covers even where it holds.** Exact copies: rows
identical against everyone. Not near-copies, since P2 controls the payoff
and not the distribution, which can jump (Example 2, p. 7). Not a new,
non-redundant agent chosen to change the result: adding an agent that
beats the current leader changes the equilibrium entirely, by design.

**Cardinal.** Everything is in log-odds. The transitive part is the row
mean, a cardinal average, and the Hodge cyclic part can be nonzero on a
record whose wins are acyclic. That is [CLAIM-434](../claims.d/CLAIM-434.md)'s point, and [THEORY-894](../theory.d/THEORY-894.md)'s
caveat applies here unchanged.

## How it bears on the record

- **[CASE-124](../cases.d/CASE-124.md) and [CASE-155](../cases.d/CASE-155.md): capture of the scoring layer.** Uniform
  averaging over the current population, Elo included, is exactly a score
  that a party can move by changing who gets evaluated, without changing
  anything about itself. Nash averaging removes one such route: scoring
  against a maximum-entropy equilibrium team instead of the population
  present makes the score blind to duplicates, when the equilibrium is
  unique. That narrows [CASE-124](../cases.d/CASE-124.md)'s μ route, a regime that "changes the
  scoring itself". The route through redundancy can be shut by
  construction. Other routes stay open, and Nash averaging does not
  address them: adding agents that are not copies; near-copies; the
  choice of tasks, since in AvT the scores depend on which tasks the data
  contain ("garbage in, garbage out"). And with ties, copying still moves
  the result. It is also distinct from [CASE-155](../cases.d/CASE-155.md)'s c. There a process's
  score rises with its own share of authority. Here the score depends on
  who is in the evaluated set, not on how much authority each holds. A
  Nash-averaged score is share-independent only if the underlying
  head-to-head matrix is. **Narrows.**
- **[TERM-077](../terms.d/TERM-077.md) and [THEORY-894](../theory.d/THEORY-894.md).** The paper's "transitive" is the Hodge
  gradient, cardinal. Its condition for Elo, zero curl, is the cardinal
  counterpart of [TERM-077](../terms.d/TERM-077.md)'s condition for a potential, wins that never
  cycle.
  The two can disagree, and the record already holds the reason
  ([CLAIM-434](../claims.d/CLAIM-434.md)). The paper gives the record nothing ordinal.
  **Irrelevant to the ordinal claim; consistent with [THEORY-894](../theory.d/THEORY-894.md).**
- **[CLAIM-451](../claims.d/CLAIM-451.md).** In a cyclic record, any scalar mean in the Elo
  family is uninformative: RPS gives every option the same rating. Nash
  averaging then reports that no option is better (P3(i)). In the claim's
  vocabulary, both report that no ordering prevails, and neither
  distinguishes nonintegrability from neutrality. The claim's
  feedback-arc measure is not among the paper's tools. **Complicates
  nothing; adds a negative instance.**
- **[CLAIM-436](../claims.d/CLAIM-436.md) and [CLAIM-440](../claims.d/CLAIM-440.md) (common currency).** mElo shows how a cyclic
  record still has a low-dimensional representation, a scalar plus
  planar "phase" coordinates (appendix F). That is a representation of
  interactions, not a currency over options, so it does not bear on the
  currency claims beyond that.
- **[CLAIM-446](../claims.d/CLAIM-446.md) and [CLAIM-445](../claims.d/CLAIM-445.md).** Not addressed.
