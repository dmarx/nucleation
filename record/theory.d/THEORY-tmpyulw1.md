---
status: Active
title: 'The minimax regret of every finite partial-monitoring game against an oblivious adversary, degenerate and duplicate actions included, is 0 when no two actions are neighbours, Θ̃(√n) when every pair of neighbours is locally observable, Θ(n^2/3) when every pair is globally but some pair is not locally observable, and linear otherwise; its lower bounds are proved against stochastic outcomes, so the same four classes hold for them'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmpkgxba: Lattimore and Szepesvári's Theorem 1,
    which completes Bartók et al.'s classification (THEORY-tmpz3a05) to all
    games. The condition for Active is met twice over. The reading is of
    the later complete source that restates the classification with proofs
    of its two missing or flawed pieces, which is what THEORY-tmpz3a05's
    promote_when asks for. And each of the four classes is re-derived below
    step by step, under ADR-047 v2, with two cited pieces (the √n lower
    bound and the n^2/3 upper bound) re-derived in outline, not checked
    against their sources. The decision procedure was checked numerically on
    the paper's games and on CLAIM-446's variants, and the √n upper bound's
    degenerate case by simulation. That the classes carry over to
    stochastic outcomes is the record's inference.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-tmpfjv79
- LIT-tmpwpq36
presupposes:
- THEORY-tmpwtj3m
summary: >-
  Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md),
  completing Bartók et al. (2014), [LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md). The four classes, trivial,
  easy, hard and hopeless, now cover every finite game. Two things change
  from Bartók et al.'s statement: the adversarial half no longer excludes
  degenerate and duplicate actions, and the trivial class is "no pair of
  neighbouring actions", not "one non-dominated action", which misplaces
  games whose extra actions are degenerate or duplicates. It classifies the
  best policy in a fixed, known game, up to game-dependent constants. It
  does not cover a learner barred from some actions, feedback that changes
  during play, or adaptive adversaries.
---
<!-- inactive-ok-file: THEORY-tmpz3a05 — Proposed; the earlier statement this one completes, nothing here rests on it -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose variants are classified here, nothing here rests on it -->
# THEORY-tmpyulw1: The minimax regret of every finite partial-monitoring game against an oblivious adversary, degenerate and duplicate actions included, is 0 when no two actions are neighbours, Θ̃(√n) when every pair of neighbours is locally observable, Θ(n^2/3) when every pair is globally but some pair is not locally observable, and linear otherwise; its lower bounds are proved against stochastic outcomes, so the same four classes hold for them

## Source

Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), Theorem 1 of the arXiv
preprint (Theorem 2 of the ALT text), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md). They prove
the √n upper bound for locally observable games (their Theorem 2, by
NeighborhoodWatch2) and the n^{2/3} lower bound (their Theorem 4, Bartók
et al.'s proof corrected). They cite the rest: the n^{2/3} upper bound to
Cesa-Bianchi, Lugosi and Stoltz (2006), the √n lower bound to Antos et al.
(2013), and the trivial case as immediate. The definitions are Bartók et
al.'s ([LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md), [NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)), with neighbours restricted to
non-degenerate actions.

## What was actually shown

**Setting.** K actions, E outcomes, a loss matrix L ∈ [0,1]^{K×E} and a
feedback matrix Φ, both known. An oblivious adversary fixes i₁, …, i_n in
advance. The learner sees Φ(A_t, i_t), never the loss, and its regret is
max_a Σ_t (y_{tA_t} − y_{ta}). R*_n(G) is the minimax expected regret.

**Definitions.** The cell C_a is where a is optimal. A non-empty cell of
dimension E − 1 makes a Pareto optimal, a smaller one makes it degenerate,
an empty one makes it dominated, and ℓ_a = ℓ_b makes a and b duplicates.
Non-degenerate a and b are neighbours if dim(C_a ∩ C_b) = E − 2, and
N_ab = {c : C_a ∩ C_b ⊆ C_c}. With S_c the signal matrix of action c, a
pair is globally observable if ℓ_a − ℓ_b ∈ Σ_{c∈[K]} Im S_cᵀ. Neighbours
are locally observable if ℓ_a − ℓ_b ∈ Σ_{c∈N_ab} Im S_cᵀ. The game is
globally or locally observable if every pair of neighbours is. These are
the span conditions of [THEORY-tmpwtj3m](THEORY-tmpwtj3m.md) with D = [K] and D = N_ab. The paper
states them as functions v(c, f) with Σ_c v(c, Φ_{ci}) = ℓ_{ai} − ℓ_{bi},
which is the same condition.

**Re-derivation, class by class.**

1. *Trivial: no neighbouring pair gives 0.* Every u in the simplex lies in
   some Pareto cell. The union of the Pareto cells is closed, and the
   lower-dimensional cells have empty interior, so the Pareto cells cover
   the simplex. Suppose two Pareto actions had different loss vectors. A
   segment in general position between interior points of their cells
   avoids every intersection of dimension below E − 2. It crosses from one
   cell to the next only through common facets of dimension E − 2, so some
   pair would be neighbours. With no neighbours, then, all Pareto actions
   share one loss vector and its cell is the whole simplex. Playing it is
   optimal in hindsight against every sequence, so the regret is 0.
2. *Hopeless: a pair that is not globally observable gives linear regret.*
   Take v in the kernel of every S_c with ⟨v, ℓ_a − ℓ_b⟩ = 1
   ([THEORY-tmpwtj3m](THEORY-tmpwtj3m.md) with D = [K]), u the centroid of C_a ∩ C_b, and
   u_a = u − Δv, u_b = u + Δv for a small fixed Δ. Every action has the same
   signal law under both, so the whole interaction has the same law. For
   c ∈ N_ab, ⟨ℓ_c − ℓ_a, u_a⟩ + ⟨ℓ_c − ℓ_b, u_b⟩ = Δ, by the paper's (21)
   and Lemma 1 ([THEORY-tmpwqg2f](THEORY-tmpwqg2f.md)). Every other c costs at least ε/2 under
   each. Hence R(u_a) + R(u_b) ≥ n·min(Δ, ε/2), and one of them is linear in
   n. By Yao's principle the minimax regret is too. The paper states this
   class as Ω(n) without proof.
3. *Hard: globally but not locally observable gives Ω(n^{2/3}).* This is
   the paper's Theorem 4, followed step by step. Let v be in the kernel of
   the stacked matrix S = (S_c)_{c∈N_ab} with ⟨v, ℓ_a − ℓ_b⟩ = 1. It exists
   by [THEORY-tmpwtj3m](THEORY-tmpwtj3m.md)'s construction, because the pair is not locally
   observable. Put u_a = u − Δv ∈ C_a and u_b = u + Δv ∈ C_b. Every action
   in N_ab shows the same signal law under both. Each other action c has
   KL ≤ C_uΔ² per play and costs at least ε − 2Δ‖v‖_∞ ≥ ε/2, where
   ε = min_{c∉N_ab} ⟨ℓ_c − ℓ_a, u⟩ > 0. With T̃ the number of plays outside
   N_ab, the chain rule and Pinsker's high-probability form give
   R(u_a) + R(u_b) ≥ (ε/2)E[T̃] + (nΔ/8)·exp(−C_uΔ²E[T̃]). If E[T̃] > n^{2/3},
   the first term is at least (ε/2)n^{2/3}. Otherwise Δ = (c/n)^{1/3} makes
   the exponent a constant and the second term of order n^{2/3}. The step
   that differs from Bartók et al. is the kernel: v must annihilate the
   signals of every action in N_ab ([THEORY-tmpwqg2f](THEORY-tmpwqg2f.md)).
4. *Easy, lower bound: a neighbouring pair gives Ω(√n).* This is cited to
   Antos et al. and re-derived here in outline only. Take any v with
   Σv_i = 0 and ⟨v, ℓ_a − ℓ_b⟩ = 1, and u_a, u_b as above. No signal is more
   informative than the outcome itself, so the KL between the two
   interactions is at most C nΔ². Setting Δ = n^{−1/2} keeps it bounded,
   and the second term of step 3 gives R(u_a) + R(u_b) ≥ c√n.
5. *Hard, upper bound: global observability gives O(n^{2/3}).* This is
   cited to Cesa-Bianchi et al. and re-derived in outline only. Run
   exponential weights over the Pareto actions with uniform exploration γ.
   Global observability gives each loss difference, relative to a fixed
   reference action, an unbiased estimate v(A_t, Φ_t)/P_{tA_t} with
   |·| ≤ VK/γ. The exponential-weights bound
   γn + log K/η + ηnV²K/γ, with γ = n^{−1/3} and η = n^{−2/3}, is O(n^{2/3}).
   The constraint η|Ẑ| ≤ 1 holds for large n.
6. *Easy, upper bound: local observability gives O(√n).* This is the
   paper's Theorem 2. The non-degenerate, expected-regret case (§3 of the
   preprint) was followed step by step. P̃_t is the stationary distribution
   of the local exponential-weights matrices Q_t. The localisation bound,
   Lemma 2, turns regret into the sum over k of local regrets, with
   |H| ≤ K^K departure maps under a union bound. Each local regret is at
   most log K/η + ηΣ_t Σ_a Q_tka Ẑ²_tka. The variance term is at most
   2V²P̃_tk/P_{tA_t}: if A_t = k, because P̃_tk ≤ 2P_tk; if A_t = a ≠ k,
   because stationarity gives P̃_tk Q_tka ≤ P̃_ta ≤ 2P_ta. Then
   E Σ_t 1/P_{tA_t} = nK, and with η ∝ √(log K/n) and γ = VKη the expected
   regret is O((KV/ε_G)√(n log K)), with a further √(nK log K) from the
   union bound. That has no log n factor. The degenerate case adds the
   redistribution and its Lemma 4. Parts (a), (b) and (d), and (c) for a
   degenerate action, were checked numerically on 200,000 random instances
   ([THEORY-tmpwqg2f](THEORY-tmpwqg2f.md)). The high-probability argument through their
   Theorem 6, a generic Exp3.P analysis, was read and not checked line by
   line.
7. *Stochastic outcomes.* Every lower bound above is proved for i.i.d.
   outcomes, and against i.i.d. outcomes E[max_a Σ_t(…)] ≥ max_a E[Σ_t(…)].
   So the adversarial upper bounds bound the stochastic pseudo-regret, and
   the four classes hold for stochastic opponents too. This is the record's
   inference. Bartók et al.'s Theorem 1 claims it for every game, but with
   the trivial-class wording corrected below.

**What was checked numerically.** The cells,
neighbours, N_ab and observability were computed for each game. The
paper's spam game (its Example 1) is easy at c = 1/3, easy and degenerate
at c = 1/2, and hard at c = 2/3, as the paper says. Its Example 2 is
hopeless. Its Exhibit 3 is locally observable. [CLAIM-446](../claims.d/CLAIM-446.md)'s check variant
with H = 5 and c = 1 is easy at k = 0.5, easy and degenerate at the
threshold k = Hc/(H + c) = 5/6, and hard at k = 0.9.

NeighborhoodWatch2 was run on the degenerate spam game against stochastic
adversaries u = (½ + D, ½ − D), with expected pseudo-regret maximised over
D ∈ {2^{−2}, …, 2^{−11}} and averaged over 24 seeds. Max regret/√n stayed
at 2.37, 2.36, 2.38, 2.39 and 2.27 for n = 10³ to 2.56·10⁵. The log-log
slope was 0.49. The same algorithm without redistribution, so that the
degenerate action gets only γ/K, gave 2.74, 2.92, 5.32, 6.82 and 9.48,
with slope 0.72. This is a stylised check on one game and a stochastic
adversary, not a proof of the rate.

**The trivial class, worded.** Bartók et al.'s Theorems 1 and 2 put a game
in the trivial class when "K = 1", K the number of non-dominated actions.
Their §7 proof says "only one Pareto-optimal action". The paper's
condition, no pair of neighbouring actions, is the one that is right
whenever degenerate or duplicate actions are present. Two such games were
computed. The first is L = ((0, 0), (0, 1)), where action 2 is degenerate,
optimal only at one vertex. The second is two duplicate actions. In both,
K = 2 and there are no neighbours, so the "K > 1, locally observable"
clause (vacuously true) would place them in the easy class. But their
minimax regret is 0. Lattimore and Szepesvári do not remark on the
difference. The observation is the record's.

What could have failed: a class with an intermediate exponent among
degenerate games, which Bartók et al. could not rule out against
adversaries. NeighborhoodWatch2 rules it out.

## What this does not say

- **Not about a constrained learner.** As in [THEORY-tmpz3a05](THEORY-tmpz3a05.md), the class is
  the regret of the best policy that may play every action. A policy that
  never plays some action pays whatever that costs, linear when the
  action is sometimes needed.
- **Not about constants or a finite horizon.** C_G in the √n bound grows
  with 1/ε_G and V, which the paper calls "arbitrarily large
  game-dependent constants". Its open problems ask whether they are real
  for large n.
- **Not about adaptivity.** An algorithm with √n regret when the adversary
  stays in a locally observable subgame of a hard game, and n^{2/3}
  otherwise, is posed as open. That is the adversarial counterpart of
  Bartók et al.'s Theorem 5.
- **Not about which algorithm wins in a hopeless game.** Linear regret is
  unavoidable there, but its coefficient depends on the algorithm. The
  paper leaves refining the regret for that as open.
- **Not about adaptive adversaries, random signals, or feedback that
  changes during play.** The adversary fixes its sequence in advance, and
  Φ is deterministic and known. Bartók et al.'s §6.3 random-signal case is
  not treated.
- **Not Θ in the easy class as stated.** The theorem says Θ̃(√n). The
  in-text expected bound carries no log n factor, and the published text's
  spam example says Θ(n^{1/2}), but the theorem as stated keeps the tilde.

## Connections

- **[THEORY-tmpz3a05](THEORY-tmpz3a05.md)** is the same classification as Bartók et al. stated
  it. This entry covers its ground and corrects its trivial clause. The
  proposal to the consolidator is that it be Superseded by this one (see
  [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md)).
- **[THEORY-tmpwtj3m](THEORY-tmpwtj3m.md)** is the span condition beneath every class here. The
  hard and hopeless lower bounds are its kernel construction with
  D = N_ab and D = [K].
- **[THEORY-tmpwqg2f](THEORY-tmpwqg2f.md)** carries the role of degenerate and duplicate actions
  and the corrected kernel step.
- **[CLAIM-446](../claims.d/CLAIM-446.md).** Its base game is easy. Suppressed feedback makes it
  hopeless. Its check variant is the paper's spam game: hard above the
  threshold, easy below it, and easy at the threshold, which only this
  paper's classification settles against adversaries.
- **[QUESTION-271](../questions.d/QUESTION-271.md).** The classes say when feedback that depends on the
  action played costs more than full information, and by how much, now
  without the non-degeneracy proviso.
