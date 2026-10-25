---
status: Read
paper: LIT-tmpfjv79
title: 'Lattimore and Szepesvári — Cleaning up the neighborhood: a full classification for adversarial partial monitoring'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Read from the arXiv preprint v1 of 23 May 2018
    (arxiv.org/pdf/1805.09247v1, 24 pp.), text extracted with pdftotext.
    Read in full: §1 (introduction, contributions, problem setup, cell
    decomposition, observability, Lemma 1), §2 (Theorem 1), §3
    (NeighborhoodWatch2, Remarks 1–2, Theorem 2 with the in-text proof for
    non-degenerate games, Lemmas 2–3), §4 (RelExp3, Theorem 3), §5 (open
    problems), and Appendices A–I: the redistribution lemma, the proofs of
    Theorems 2 and 3, the corrected lower bound with its footnote, the
    lower bound in F, the generic Exp3.P bound, the bound on the
    estimators, the concentration lemma and the gallery of examples. The
    high-probability arguments of Appendices B, C and F were followed at
    the level of their steps and not checked line by line. The in-text
    expected-regret proof, the lower bounds, Lemma 1 and the redistribution
    properties are re-derived or checked in THEORY-tmpyulw1,
    THEORY-tmpwqg2f and THEORY-tmpb4ozq. The ALT 2019 text (PMLR 98,
    28 pp.) was fetched, and its abstract, contribution list, theorem
    statements and lower-bound footnote were compared with the preprint's;
    the rest was not compared. Bartók et al.'s text (NOTE-tmpupizd's copy)
    was re-opened at its Theorem 4 proof, its Theorem 6 and Corollary 5,
    and its §7, to locate what this paper corrects.
date: '2026-10-25'
summary: >-
  Completes the classification of finite partial-monitoring games against
  oblivious adversaries to every game, degenerate and duplicate actions
  included: 0 with no neighbouring pair, Θ̃(√n) locally observable,
  Θ(n^2/3) globally but not locally observable, Ω(n) otherwise. The
  missing piece is NeighborhoodWatch2, which redistributes probability
  onto degenerate actions in proportion to the neighbours they lie between
  and has a high-probability √n bound. It corrects Bartók et al.'s
  T^2/3 lower-bound proof, whose separating direction ignored the
  degenerate actions' signals. The preprint, not the published text, also
  says the earlier localisation argument exchanged an expectation and a
  maximum. RelExp3 gives point-locally observable games an asymptotic
  constant depending only on K_loc, F and log K, and a factor linear in F
  is shown to be necessary.
---
<!-- inactive-ok-file: THEORY-tmpz3a05 — Superseded by THEORY-tmpyulw1; the earlier classification this reading completes, and whose promote_when it bears on -->
<!-- inactive-ok-file: THEORY-tmpb4ozq — Proposed; the point-local bound, filed from this reading -->
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim whose check variant this reading places, nothing here rests on it -->
<!-- inactive-ok-file: QUESTION-tmp1wykc — Answered; the question whose partial-monitoring answer this reading refines, cited for that -->
# NOTE-tmpkgxba: Lattimore and Szepesvári — Cleaning up the neighborhood: a full classification for adversarial partial monitoring

## Contribution

It closes the open problem left by Bartók et al. ([LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md)): the
adversarial classification for degenerate games. Bartók et al.'s
Theorem 2 covered only games with no degenerate and no duplicate actions.
The paper proves a √n upper bound for every locally observable game with a
modified NeighborhoodWatch, which completes the four classes for all
finite games (Theorem 1). Along the way it corrects a slip in the proof of
the T^{2/3} lower bound. The arXiv text also says the earlier localisation
argument exchanged an expectation and a maximum. For point-locally
observable games it gives a new algorithm, RelExp3, whose asymptotic
regret constant is free of arbitrarily large game constants, and a lower
bound showing linear dependence on the number of feedback symbols.

## Key insight

A degenerate action is optimal only on the boundary between two
neighbours, and its loss is a mixture of theirs (Lemma 1). It is never the
answer, but it may be the cheapest place to learn which of the two is.
NeighborhoodWatch builds a distribution from local games over the Pareto
actions, so it gives such an action no weight beyond forced exploration,
and that does not give √n. The fix is to move mass from a and b onto d in
the proportions that leave the expected loss unchanged, with at least
min(P̃_a, P̃_b)/(2K) on d. The paper's reason for not giving d more:
"a degenerate action d in N_ak is only useful for learning about the loss
differences between actions a and k, which suggests the algorithm should
not assign much more probability to d than the minimum probability of
playing a and k."

## Assumptions

- Finite game G = (L, Φ), L ∈ [0,1]^{K×E}, Φ ∈ [F]^{K×E}, both known.
  Feedback is deterministic.
- Oblivious adversary: "At the beginning of the game … the adversary
  secretly chooses a sequence of outcomes".
- Regret against the best fixed action in hindsight, realised:
  max_a Σ_t (y_{tA_t} − y_{ta}). Minimax over policies and sequences.
- Neighbours are non-degenerate by definition. Without loss of generality
  the optimal actions a*_u and a*_t are taken non-degenerate.
- NeighborhoodWatch2 plays only actions in some N_ab. The paper says that
  removing the other degenerate actions "can only increase the minimax
  regret". RelExp3 removes dominated and degenerate actions.
- Constants are game-dependent: ε_G (Lemma 2), V (the estimators' sup
  norm), K. The point-local bound is asymptotic in n.

## Key results

- **Definitions (§1).** Cells, dominated, degenerate (non-empty, dimension
  below E − 1), Pareto optimal, neighbours (non-degenerate, intersection of
  dimension E − 2), weak neighbours (cells meet), duplicates (ℓ_a = ℓ_b),
  N_ab = {c : C_a ∩ C_b ⊆ C_c}. Global, local and pairwise observability by
  estimation functions v with Σ_c v(c, Φ_{ci}) = ℓ_{ai} − ℓ_{bi}, supported
  on [K], N_ab or {a, b}. Point-local observability: every pair of weak
  neighbours is pairwise observable.
- **Lemma 1** (Bartók et al.'s Lemma 11). For d ∈ N_ab,
  ℓ_d = αℓ_a + (1 − α)ℓ_b for a unique α ∈ [0, 1]. Re-derived in
  [THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md).
- **Theorem 1.** R*_n(G) is 0 if G has no pair of neighbouring actions,
  Θ̃(√n) if G is locally observable and has neighbouring actions, Θ(n^{2/3})
  if it is globally but not locally observable, and Ω(n) otherwise. Of
  its pieces the paper proves the √n upper bound and the n^{2/3} lower
  bound and cites the rest. [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md).
- **Algorithm 1 (NeighborhoodWatch2) and Theorem 2.** It keeps local
  exponential weights Q_tk over N_k ∩ A for each Pareto, duplicate-free k,
  takes the stationary distribution P̃_t, applies REDISTRIBUTE, and mixes
  in γ/K. Loss-difference estimates are updated for every local game each
  round, with a negative bias β for high probability. With
  η = V^{−1}√(log(K/δ)/(nK)) and γ = VKη, R_n ≤ C_G√(n log(e/δ)) with
  probability 1 − δ. The in-text proof for non-degenerate games, with
  β = 0, gives E[R_n] = O((KV/ε_G)√(n log K)), and V ≤ 1 + F there.
- **Lemma 4.** REDISTRIBUTE returns a distribution with P_ta ≥ P̃_ta/4,
  Σ_a (P_ta − P̃_ta)⟨ℓ_a, u⟩ ≤ γ, P_tb ≥ P̃_tk Q_tka/(4K) for non-duplicate
  b ∈ N_ka, P_ta ≥ γ/K, and P_td ≥ P̃_tk/(4K) for duplicates of k. Checked
  numerically ([THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)).
- **Algorithm 2 (RelExp3) and Theorem 3.** For point-locally observable
  games, lim sup E[R_n]/√n ≤ 8√(2K_loc(1 + F)(2 + F) log K).
  [THEORY-tmpb4ozq](../theory.d/THEORY-tmpb4ozq.md).
- **Theorem 4 (Appendix D).** The n^{2/3} lower bound, with v in the kernel
  of the stack of S_c over N_ab, and footnote 2 naming Bartók et al.'s
  slip.
- **Theorem 5 (Appendix E).** A two-action game with E = 2F − 2 has
  R*_n ≥ (F − 1)√n/45 for large n.
- **Lemma 9 (Appendix G).** For a pairwise observable pair, v can be chosen
  with ‖v‖_∞ ≤ 1 + F.
- **Examples.** Example 1, the spam game with a "don't know" action of
  cost c that reveals the label: Θ(n^{2/3}) for c > ½, Θ̃(n^{1/2}) for
  c ∈ (0, ½], and 0 at c = 0. Example 2 is hopeless. Exhibit 1: easy games
  can have no unbiased loss estimates, only loss-difference estimates.
  Exhibit 2: at c = ½ the third action is degenerate. Exhibit 3: locally
  but not point-locally observable. Exhibit 4: a game with three
  degenerate actions of which NeighborhoodWatch2 plays one.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every finite game falls in one of the four classes against oblivious adversaries | strong | Theorem 1: Theorem 2 and Appendix D proved, other pieces cited. Re-derived class by class in [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md) |
| C2 | NeighborhoodWatch2 has O(√n) regret with high probability on every locally observable game | strong | Theorem 2, Appendix B. In-text expected case re-derived. Simulated on the degenerate spam game |
| C3 | Forced exploration alone does not give √n with degenerate actions | moderate | Stated in §3 and Remark 1 without a lower bound. The record's simulation agrees on one game |
| C4 | Bartók et al.'s lower-bound proof chose v in the wrong kernel | strong | Footnote 2. Confirmed against Bartók et al.'s text, with a game where it matters ([THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)) |
| C5 | Foster–Rakhlin and Bartók et al. "inadvertently exchanged an expectation and maximum during the localisation argument" | moderate | arXiv v1 contributions only. Dropped from the published contribution list, though "correct errors in previous analyses" stays in the abstract. Located in Bartók et al.'s text below |
| C6 | RelExp3's asymptotic constant depends only on K_loc, F and log K | strong as stated | Theorem 3, Appendix C, read, not checked line by line |
| C7 | Regret linear in F is unavoidable in general | strong | Theorem 5, re-derived ([THEORY-tmpb4ozq](../theory.d/THEORY-tmpb4ozq.md)) |

## What this paper corrects in Bartók et al.'s analysis

1. **The adversarial classification's scope.** Bartók et al.'s Theorem 2
   excludes degenerate games and calls their inclusion "the immediate open
   problem" (§8). The paper proves the √n bound for them, so the
   classification covers every game. This is a completion, not a
   correction: Bartók et al. claimed nothing for those games.
2. **The localisation step of the √n bound** (arXiv v1 only). Bartók
   et al.'s Theorem 6 bounds sup_{φ∈Φ_L} E{Σ_t (e_{I_t} − e_{φ(I_t)})ᵀLe_{J_t}}.
   Their Corollary 5 then bounds E{R_T}, through Lemma 6, "internal regret
   is at most K times the local internal regret". The localising
   departure map depends on the realised play, so that step needs
   E[sup_φ …], and sup_φ E[…] is smaller. This is the record's reading of
   where the paper's "inadvertently exchanged an expectation and maximum"
   applies. The paper does not repair NeighborhoodWatch's proof, and says
   a correction "is presumably possible". It replaces the argument with
   high-probability bounds for each local game and a union bound over the
   |H| ≤ K^K departure maps (Lemma 6, Theorem 6). This applies to Bartók
   et al.'s adversarial Theorem 2 for non-degenerate games too. The
   published ALT text drops the sentence, and its contribution list keeps
   only "correctly deals with degenerate games" and the lower-bound
   correction. The abstract still says "correct errors in previous
   analyses". So the claim that NeighborhoodWatch's √n proof is flawed
   rests on the preprint. The adversarial √n bound for non-degenerate games
   now rests on NeighborhoodWatch2, which covers them.
3. **The T^{2/3} lower bound's proof.** Bartók et al. take
   v ∈ Ker S₁ ∩ Ker S₂ and later need S_c v = 0 for the actions between the
   two neighbours. The paper takes v in the kernel of every S_c,
   c ∈ N_ab. This is not specific to the adversarial case. It underlies
   both of Bartók et al.'s classification theorems, but it changes
   nothing for non-degenerate games, where N_ab = {a, b}. [THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)
   gives a three-outcome game where Bartók et al.'s choice fails and the
   corrected one works.
4. **Not flagged by the paper, the record's observation.** Bartók et al.'s
   trivial class is "K = 1" non-dominated actions in Theorems 1 and 2, but
   "only one Pareto-optimal action" in §7. Neither is right with
   degenerate or duplicate actions. A degenerate action beside an
   always-optimal one, or two duplicates, gives K = 2, no neighbours and
   regret 0, while the theorem's wording would say Θ̃(√T). The paper's "no
   pairs of neighboring actions" is right ([THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md)).

The point (d) of the arXiv contributions, that Bartók (2013) "mistakenly
combines bounds that hold in expectation in 'local games' into a bound for
the whole game as if they were high probability bounds", concerns a
different paper (Bartók's COLT 2013 algorithm), not [LIT-tmpwpq36](../literature.d/LIT-tmpwpq36.md). It too is
absent from the ALT text.

## Concepts

- **Degenerate action**: non-dominated, cell of dimension below E − 1.
  Never uniquely optimal, possibly informative.
- **Neighbourhood set N_ab**: the actions optimal on all of C_a ∩ C_b:
  a, b, their duplicates, and degenerate actions with C_d = C_a ∩ C_b.
- **REDISTRIBUTE**: moves mass from a and b onto d ∈ N_ab, preserving the
  expected loss, so that d is played about as often as the less-played of
  its two neighbours.
- **Weak neighbours, point-local game, K_loc**: cells that meet; a largest
  set of actions with a common point; its size.
- **Anchor**: in RelExp3, the action of largest weight, against which all
  loss differences are estimated.

## Connections

It builds on Bartók et al. (2014) for the definitions, Lemma 1 and the
lower-bound construction, on Foster and Rakhlin (2012) for the
stationary-distribution construction, on Auer et al. (2002) for the
Exp3.P-style bias, on Cesa-Bianchi et al. (2006) for the globally
observable upper bound, and on Antos et al. (2013) for the √n lower bound
and the stochastic degenerate case. The ALT text adds Kwon and Perchet
(2017) ([LIT-tmpm3j41](../literature.d/LIT-tmpm3j41.md)) to the approachability line of related work. The
open problem on adapting to easy data is the adversarial version of
Bartók et al.'s Theorem 5 for CBP.

## Bearing on the record

- **[THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md)'s promotion condition.** It asks for "a reading of a
  later complete source that restates the classification with its
  proofs, such as Lattimore and Szepesvári's corrected adversarial
  analysis". This is that reading. The paper restates the classification
  and proves the two pieces that were open or flawed, and it cites the
  rest as Bartók et al. did. The classes are re-derived in
  [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md). But [THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md)'s title has two defects, both
  shown above. The trivial clause, "0 when only one action is
  non-dominated", is wrong with degenerate or duplicate actions. Its
  adversarial half is narrower than now known. Its summary of the lower
  bound also repeats the kernel slip. The proposal to the consolidator is
  that [THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md) be Superseded by [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md), rather than
  promoted as worded. Its status is not changed here.
- **[CLAIM-446](../claims.d/CLAIM-446.md)'s note of 2026-10-25.** The check variant there, a
  revealing action with loss k under both outcomes beside an
  uninformative approach, is this paper's Example 1 with general H and c:
  avoid ↔ "spam" (0, 1), approach ↔ "not spam" (1, 0), check ↔ "don't
  know" (c, c), when H = c = 1. The note's two cases match the paper's,
  hard for k > Hc/(H + c) and easy below. The paper adds the boundary,
  where the check is degenerate (cell {p = c/(H + c)}): it is easy, which
  Bartók et al.'s adversarial theorem did not cover. Computed in
  [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md) for H = 5, c = 1, k = 5/6. So the variant is not only
  the record's construction. Its special case is the paper's motivating
  example. The note's sentence "If k < Hc/(H + c) the check has its own
  cell and the game is easy again" can become "k ≤".
- **[QUESTION-tmp1wykc](../questions.d/QUESTION-tmp1wykc.md).** Its partial-monitoring answer, from
  [THEORY-tmpwtj3m](../theory.d/THEORY-tmpwtj3m.md), is unchanged. The probe set that matters for the hard
  versus easy distinction is N_ab, including degenerate actions, and not
  only the two actions compared. [THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md) says how such probes
  count.
- **[CLAIM-tmpa8ttt](../claims.d/CLAIM-tmpa8ttt.md).** No direct bearing on its mixture-identifiability
  result. The one parallel: in both, the condition is a kernel condition
  on the stacked probe matrix over the whole probe set ([THEORY-tmpwqg2f](../theory.d/THEORY-tmpwqg2f.md)'s
  correction is exactly the requirement to stack all of N_ab). An
  argument that checks only two probes at a time can miss what a third,
  cheap one reveals. That is the record's analogy, not the paper's.
- **[QUESTION-271](../questions.d/QUESTION-271.md).** The classes now hold without the non-degeneracy
  proviso. [THEORY-tmpb4ozq](../theory.d/THEORY-tmpb4ozq.md) adds that within the easy class the constant
  can grow linearly with the feedback alphabet.

Its subject is learning theory read for itself. It carries no instruction
for ML practice. The anthology-candidate flag on the LIT stands for the
anthology to judge.

## Limitations

- **Two cited pieces** of the classification (Antos et al.'s √n lower
  bound and Cesa-Bianchi et al.'s n^{2/3} upper bound) are not proved here.
  [THEORY-tmpyulw1](../theory.d/THEORY-tmpyulw1.md) re-derives them in outline only.
- **High-probability proofs** (Appendices B, C, F) were followed step by
  step in structure, not verified line by line.
- **Small slips in the preprint.** Exhibit 3 names the neighbours "(1, 2)
  and (1, 3)" right after saying (1, 2) are not neighbours; computed,
  they are (1, 3) and (2, 3). Appendix E's p should be ½ − (E − 2)Δ/2 for u
  to be a distribution. Exhibit 4's matrices are garbled in the extracted
  text and were not checked. None affects a theorem.
- **Version.** The preprint was read, and the ALT text compared only at
  the level of statements. The two differ at least in the contribution
  list (above) and the related work.

## Open questions

- Does NeighborhoodWatch's original proof survive with a corrected
  localisation, or is the √n bound for non-degenerate adversarial games
  only as good as NeighborhoodWatch2's proof? The paper says a
  correction "is presumably possible".
- Are the game-dependent constants (1/ε_G, V) real for large n in the
  locally observable class, as the paper asks? For [CLAIM-446](../claims.d/CLAIM-446.md)-like games
  near a threshold, ε_G is small and the constant large.
- What is the class when the action set itself is chosen, round by round,
  by another process from the learner's past estimates? This is
  [CLAIM-446](../claims.d/CLAIM-446.md)'s setting and still outside the theorem.
