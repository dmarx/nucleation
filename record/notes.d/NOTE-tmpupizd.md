---
status: Read
paper: LIT-tmpwpq36
title: 'Bartók, Foster, Pál, Rakhlin and Szepesvári — Partial monitoring: classification, regret bounds and algorithms'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read from the authors' preprint dated March 27, 2013, posted on
    Alexander Rakhlin's MIT page (www.mit.edu/~rakhlin/papers/partial_monitoring.pdf),
    text extracted with pdftotext. It is not the typeset Mathematics of
    Operations Research article, whose INFORMS page returned 403, and it
    was not compared with it. Read in full: the introduction, §2's
    definitions and examples (full information, bandit, a hopeless game,
    dynamic pricing), §3's two classification theorems and Theorem 3, §4's
    lower bound (Theorem 4) with its proof, §5 on CBP with Theorem 3's
    proof, Corollaries 1–3, Theorem 5 and the dynamic-pricing example, §6
    on NeighborhoodWatch with Theorem 6, Lemma 6, Corollary 5 and §6.3 on
    random signals, §7's proof of the classification, and §8's
    discussion. The appendix proofs of Lemmas 1–11 were read at the level
    of their statements and main steps, not checked line by line. The
    lemma on which the observability conditions rest, and the paper's
    application to the record's approach–avoid example, are re-derived in
    THEORY-tmpwtj3m. The classification itself is THEORY-tmpz3a05. The
    abstract of Lattimore and Szepesvári (arXiv:1805.09247, not held) was
    read for what it says about this paper.
- version: 2
  date: '2026-10-25'
  note: >-
    Lattimore and Szepesvári are now held and read (LIT-tmpfjv79, NOTE-
    tmpkgxba). The Theorem 4 bullet notes the kernel slip they correct
    (THEORY-tmpwqg2f), and Claims C2, Connections and Limitations cite the
    reading in place of the arXiv number and "not read here". The reading
    itself is unchanged.
date: '2026-10-25'
summary: >-
  For finite partial-monitoring games the minimax regret takes exactly
  four rates: 0 with one non-dominated action, Θ̃(√T) when every pair of
  neighbouring actions is locally observable, Θ(T^2/3) when the game is
  globally but not locally observable, and Θ(T) otherwise. The conditions
  are linear algebra on loss and signal matrices: a loss difference must
  lie in the span of the row spaces of the signal matrices of the actions
  allowed to estimate it. The stochastic classification covers every game;
  the adversarial one covers non-degenerate games only.
---
<!-- inactive-ok-file: THEORY-tmpz3a05 — Superseded by THEORY-tmpyulw1; the classification as the paper states it, filed from this reading -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose dated note this reading checks, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-932 THEORY-925 — Proposed; accounts this reading is compared with, nothing here rests on their being settled -->
# NOTE-tmpupizd: Bartók, Foster, Pál, Rakhlin and Szepesvári — Partial monitoring: classification, regret bounds and algorithms

## Contribution

It completes the classification of finite partial-monitoring games by
minimax regret. Earlier work had settled the gaps between 0 and √T
(Antos et al.) and between T^{2/3} and T (Piccolboni and Schindelhauer).
This paper closes the gap between √T and T^{2/3}: a game that is not
locally observable has regret Ω(T^{2/3}) (Theorem 4), and every locally
observable game can be played with Õ(√T) regret, by CBP against
stochastic opponents and by NeighborhoodWatch against adversarial ones
when the game is non-degenerate. It also gives individual, logarithmic
regret bounds for stochastic opponents.

## Key insight

What makes a game hard is not how much the learner sees but whether the
comparisons that matter can be estimated from the actions that are worth
playing near the decision boundary. Each action's feedback is a signal
matrix S_k, and observing it gives S_k p, the distribution of symbols
under the outcome distribution p. The expected loss difference of actions
i and j is estimable from the actions in a set D exactly when ℓ_i − ℓ_j
lies in ⊕_{k∈D} Im S_kᵀ. Global observability allows every action into
D. Local observability allows only the actions whose cells contain the
boundary between i and j. When the information exists only in actions
that are bad near that boundary, the learner pays for it at rate T^{2/3}.

## Assumptions

- Finite game: N actions, M outcomes, a loss matrix L ∈ ℝ^{N×M} with
  entries in [0, 1], and a feedback matrix H ∈ Σ^{N×M}. Both are known to
  the learner before play. The loss is never revealed, only H_{I_t, J_t}.
- Two opponent models. An oblivious adversary fixes the outcome sequence
  in advance. A stochastic opponent draws outcomes i.i.d. from some p ∈
  Δ_M, and regret is then measured against the action with the least
  expected loss under p.
- Regret is against the best fixed action of the given game. A learner
  is free to play any action of the game.
- Theorem 2, the adversarial classification, needs the game to be
  non-degenerate: no degenerate actions (a non-dominated action whose
  cell is strictly contained in another's) and no duplicate actions
  (equal loss rows).
- Õ and Θ̃ hide polylogarithmic factors, and the constants depend on the
  game.

## Key results

- **Definitions 1–3.** The cell C_i is the set of outcome distributions
  under which action i is optimal. An action is dominated if its cell is
  empty, degenerate if its cell is strictly inside another's, and
  Pareto-optimal otherwise. Pareto-optimal i and j are neighbours if
  C_i ∩ C_j has dimension M − 2. The neighbourhood action set
  N⁺_{i,j} = {k : C_i ∩ C_j ⊆ C_k}.
- **Definition 4.** The signal matrix S_i ∈ {0,1}^{s_i×M} is the incidence
  matrix of the symbols in row i of H, so S_i p is the distribution of
  symbols when action i is played under p.
- **Definitions 5–6.** The game is globally observable if
  ℓ_i − ℓ_j ∈ ⊕_{k∈N} Im S_kᵀ for every pair of actions. A pair of
  neighbours is locally observable if ℓ_i − ℓ_j ∈ ⊕_{k∈N⁺_{i,j}} Im S_kᵀ,
  and the game is locally observable if every pair of neighbours is.
  Local observability implies global.
- **Theorem 1 (stochastic).** With K the number of non-dominated actions,
  the minimax expected regret is 0 if K = 1; Θ̃(√T) if K > 1 and the game
  is locally observable; Θ(T^{2/3}) if it is globally but not locally
  observable; and Θ(T) if it is not globally observable.
- **Theorem 2 (adversarial).** The same four classes, with Θ(√T) in the
  second, for non-degenerate games.
- **Theorem 4 (lower bound).** If some pair of neighbours is not locally
  observable, there is c(G) > 0 such that every algorithm suffers
  E[R_T] ≥ c(G)T^{2/3} against some opponent strategy. The proof takes v
  in Ker S_1 ∩ Ker S_2 (the minor error Lattimore and Szepesvári
  correct: v must be in the kernel of every S_k, k ∈ N⁺_{1,2};
  [THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)) with (ℓ_2 − ℓ_1)ᵀv = 1, sets p_{1,2} = p_0 ± εv
  about a point of the shared boundary, and chooses ε = c₃T^{−1/3}. Only
  actions outside the neighbourhood set can tell p₁ from p₂, and each
  such play costs at least β.
- **Theorem 3, Corollaries 1–3 (CBP).** CBP keeps, for each pair of
  neighbours, an unbiased estimate of the loss difference built from
  observer vectors, with confidence widths, and plays the candidate
  action that most reduces the remaining uncertainty. A decaying
  exploration rule caps how often a purely information-seeking action is
  played. For locally observable games the expected regret is
  O(Σ_k W_k² d_k² α log T / δ_k), logarithmic in T for a fixed p
  (Corollary 1), and O(√(T log T)) uniformly (Corollary 3). For globally
  observable games it is O(T^{2/3} log^{1/3} T) (Corollary 2).
- **Theorem 5.** In a globally observable game, if the opponent's
  distribution stays away from every boundary between neighbours that
  are not locally observable, CBP attains Õ(√T) without knowing that it
  does. Corollary 4 applies this to dynamic pricing under "sufficiently
  hilly" demand.
- **Theorem 6 and Corollary 5 (NeighborhoodWatch).** One local algorithm
  per action runs exponential weights over its neighbourhood, with
  importance-weighted estimates of loss differences and a uniform mixing
  γ over the neighbourhood. A fixed point p = Qp combines them. The local
  internal regret is at most 4N v̄ √(6(log N)T); by Lemma 6 the internal
  regret is at most K times that, and external regret is at most internal
  regret.
- **§6.3 (random signals).** With signal distributions H_{i,j} ∈ Δ(Σ), the
  same argument goes through with Ξ_i (whose columns are the signal laws)
  in place of S_i. The condition is ℓ_i − ℓ_j ∈ Im Ξ_{(i,j)}ᵀ.
- **Examples (§2.1).** Full-information and bandit games are locally
  observable. Dynamic pricing is globally but not locally observable:
  only consecutive prices are locally observable pairs.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The minimax regret of every finite partial-monitoring game against stochastic opponents is 0, Θ̃(√T), Θ(T^{2/3}) or Θ(T), decided by K, local and global observability | strong | Theorem 1, from Theorem 4, Corollaries 2–3 and cited lower bounds (Piccolboni–Schindelhauer, Antos et al.) |
| C2 | The same holds against adversarial opponents for non-degenerate games | strong as stated; the adversarial analysis was later corrected | Theorem 2 via NeighborhoodWatch, Corollary 5. Lattimore and Szepesvári (2019, [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](NOTE-tmpkgxba.md)) "correct errors in previous analyses" and extend the classification to all games |
| C3 | A game that is not locally observable has regret Ω(T^{2/3}) | strong | Theorem 4 with proof; its first step is re-derived in [THEORY-tmpwtj3m](../theory.d/THEORY-tmpwtj3m.md) |
| C4 | Against stochastic opponents, locally observable games have logarithmic individual regret | strong | Corollary 1 |
| C5 | A globally observable game behaves as an easy one against opponents kept away from the unobservable boundaries, and CBP adapts without being told | strong | Theorem 5, Corollary 4 |
| C6 | The algorithms are computationally efficient | moderate | CBP solves N + N² linear programs up front and up to N² per round; the authors call more efficient algorithms an open need |

## Concepts

- **Cell decomposition**: the partition of the simplex Δ_M by which
  action is optimal.
- **Neighbours**: Pareto-optimal actions whose cells share a facet of
  dimension M − 2.
- **Signal matrix S_i**: the 0/1 incidence matrix of symbols against
  outcomes for action i.
- **Global and local observability**: as in Definitions 5–6.
- **Observer set and observer vectors**: a set V_{i,j} of actions and
  vectors v_{i,j,k} with ℓ_i − ℓ_j = Σ_{k∈V_{i,j}} S_kᵀ v_{i,j,k}. The
  estimate is the weighted average of the observed signal frequencies.
- **Trivial, easy, hard and hopeless games**: regret 0, Θ̃(√T), Θ(T^{2/3})
  and Θ(T).
- **Local internal regret**: regret against departure functions that swap
  an action for one of its neighbours.

## Connections

It builds on Piccolboni and Schindelhauer (2001) for global observability
and the linear lower bound, Cesa-Bianchi, Lugosi and Stoltz (2006) for
the T^{2/3} rate and the revealing-action game, and Antos et al. (2012)
for the √T lower bound, and it merges Bartók, Pál and Szepesvári (2011),
Bartók, Zolghadr and Szepesvári (2012) and Foster and Rakhlin (2012).
The two-level construction of NeighborhoodWatch follows Foster and Vohra
(1997) and Blum and Mansour (2007) on turning external into internal
regret through a stationary distribution. §6.3 points to Rustichini
(1999), Lugosi, Mannor and Stoltz (2008) and Perchet (2011), the line
that Kwon and Perchet ([LIT-tmpm3j41](../literature.d/LIT-tmpm3j41.md)) continues for approachability.
Lattimore and Szepesvári, "Cleaning up the neighborhood" ([LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md),
read in [NOTE-tmpkgxba](NOTE-tmpkgxba.md)), completes the adversarial classification for degenerate games
and, in its abstract's words, corrects "errors in previous analyses".

## Bearing on the record

- **[CLAIM-446](../claims.d/CLAIM-446.md)'s note of 2026-10-25, checked.** The toy has outcomes
  (dangerous, safe), losses ℓ_avoid = (0, c) and ℓ_approach = (H, 0), and
  S_avoid = [1 1], S_approach = I₂, all as the note says. With p the
  probability of danger, avoid is optimal for p ≥ c/(H + c) and approach
  below, so both cells are segments and meet at one point. The two
  actions are neighbours, both are Pareto-optimal, there is no degenerate
  or duplicate action, and N⁺ = {avoid, approach}. The loss difference
  lies in Im S_avoidᵀ + Im S_approachᵀ = ℝ², so the game is locally
  observable, and under Theorems 1 and 2 its minimax regret is Θ̃(√T)
  against stochastic opponents and Θ(√T) against adversarial ones. The
  residuals were recomputed: 4.24 for avoid alone, 0 with approach. The
  classification is stated correctly. Three precisions follow.
  - *Removing approach is not "the avoid-only game".* A game with only
    avoid has K = 1 and zero minimax regret: regret is measured against
    the actions the learner has. The cost the claim is about is regret
    in the full game for a policy that never plays approach. Against a
    safe enough environment (p < c/(H + c)) that cost is
    T(c(1 − p) − Hp), linear in T. The classification bounds the best
    policy in a game, not a policy constrained not to sample. So the note's
    conclusion, access and not observability, is the paper's framing,
    stated more exactly.
  - *Approach with its feedback suppressed is hopeless.* If approach
    remains available but yields one symbol whatever happens, as when
    exposure is done under safety behaviours that keep the outcome from
    being credited, then neither signal matrix separates the outcomes,
    the game is not globally observable, and regret is Θ(T). This was
    checked when the note was filed: the residual stays 4.24.
  - *Checking is a third class.* Add a check action with loss k under
    both outcomes that reveals the outcome, and make approach
    uninformative. If k > Hc/(H + c), check is dominated, its cell is
    empty and it is outside N⁺. The game is then globally but not
    locally observable, Θ(T^{2/3}): the revealing-action structure of
    Cesa-Bianchi et al. If k < Hc/(H + c), check takes a cell between
    the other two (p ∈ [k/H, 1 − k/c]), the neighbours are avoid–check
    and check–approach, and the game is locally observable again. This
    gives the claim's hypervigilance clause ("checking ... that never
    acquire[s] the information that would discriminate") a formal
    counterpart: information sought only through an action that is never
    worth taking for itself is paid for at the hard rate. It is the
    record's construction, not the paper's.
- **The exploration floor.** CBP has no fixed floor. In the easy class it
  plays a suboptimal action O(log T/δ_k²) times (Corollary 1), and its
  decaying exploration rule exists to stop futile information seeking.
  NeighborhoodWatch does mix in γ/|N_i| over each neighbourhood. So "a
  floor of probability on approach" is one sufficient device. What the
  theorems require is that the observer actions be sampled often enough,
  and in the stochastic easy case that means logarithmically often.
  This bears on [QUESTION-271](../questions.d/QUESTION-271.md).
- **[THEORY-932](../theory.d/THEORY-932.md), [THEORY-925](../theory.d/THEORY-925.md).** Those entries' frequency factor is the
  1/Σ 1{I_s = k} in CBP's estimate and its confidence width.
- **[QUESTION-031](../questions.d/QUESTION-031.md).** Observability is a separation condition of exactly
  the kind that question asks for, for one decision family: the
  comparisons ℓ_i − ℓ_j, restricted to neighbours. It is checkable before
  any data are seen.

Its subject, online learning under partial feedback, is learning theory
read for itself. It carries no instruction for ML practice. The
anthology-candidate flag on the LIT stands for the anthology to judge.

## Limitations

- **Finite games only**, with L and H known in advance. Nothing is said
  about learning the feedback structure, or about a structure that
  changes during play.
- **Adversarial classification for non-degenerate games only**; the
  degenerate case is posed as the open problem (§8). Lattimore and
  Szepesvári later closed it and corrected the earlier analyses. The
  correction is read in [NOTE-tmpkgxba](NOTE-tmpkgxba.md) ([LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md)).
- **Constants are game-dependent** and can be large (W_k, d_k, the K of
  Lemma 6). The rate classes say nothing about any finite horizon.
- **Oblivious adversaries only** in the adversarial case. An adaptive
  opponent, or a learner whose own play changes L or H, is outside it.
- **Preprint copy.** It was not compared with the journal text.

## Open questions

- What is the regret class when the set of actions available at each
  round is chosen by another process, as a function of the learner's
  past estimates? That is [CLAIM-446](../claims.d/CLAIM-446.md)'s setting. The classification
  assumes a fixed action set.
- In the random-signal case of §6.3, how do noisy signals change the
  constants, as opposed to the rate class? This is the case closest to
  imperfect evidence.
