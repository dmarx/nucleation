---
status: Read
paper: 'LIT-tmp42ace'
title: 'Czarnecki et al. — Real world games look like spinning tops'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Read in full on 2026-10-24 from arXiv:2004.09468v2 (17 June 2020), a
    27-page PDF marked "Preprint", under arXiv's non-exclusive distribution
    licence, extracted by pdftotext. Read: sections 1–7 (pp. 1–9) and
    supplementary sections A–L (pp. 13–27), with every proof followed and
    the figure and table captions read. The reference list was skimmed.
    Theorem 4 and its proof were checked against supp_text.tex in the v2
    source, which matches the PDF. The NeurIPS proceedings version was not
    compared. Page numbers below are v2's. Every quotation was checked
    against the extracted text by script. The reader's counterexample to
    Proposition 3 and the arithmetic of Proposition 1 were run by script
    (scratchpad/marlb_scripts/checks.py).
date: '2026-10-24'
summary: >-
  A hypothesis paper with theorems and sampled empirical games. Where
  players can signal n bits before the outcome is settled, every win–loss
  pattern on 2ⁿ strategies occurs, so cycles are astronomically long.
  Nash clustering layers any symmetric zero-sum game, and beating a whole
  cluster guarantees climbing. Sampled games show cluster size peaking at
  middling strength. The body says the geometry is not proved, the
  abstract says it is. Two of the smaller results have defective
  statements or proofs.
---
<!-- inactive-ok-file: THEORY-tmp2ela3 THEORY-tmpq0hjk THEORY-tmp5k950 — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: CLAIM-451 CLAIM-443 CLAIM-446 CLAIM-445 — Proposed; the accounts this reading bears on, named in prose, nothing here rests on them -->

# NOTE-tmpat2ia: Czarnecki et al. — Real world games look like spinning tops

## What the paper does

**The hypothesis** (pp. 3–4). Games people play for skill have two
features: a strong transitive dimension, so practice pays, and diverse
styles at each level, so some styles counter others. The cycles should
thin out toward the strongest play. Strategies that try to lose thin them
out toward the bottom too. The shape is a spinning top. "Monotonic" here
means the beats relation is transitive (p. 4), which is ordinal and
differs from Balduzzi et al.'s σ-of-differences sense ([LIT-tmpd40td](../literature.d/LIT-tmpd40td.md)).

**n-bit communicative games and long cycles** (pp. 5, 13).
- Definition 1: a game is n-bit communicative if each player can transmit
  n bits before reaching a node after which a win or a loss is no longer
  attainable.
- Theorem 1: for every such game and every antisymmetric P in
  {−1, 0, 1}^{⌊2ⁿ⌋×⌊2ⁿ⌋}, there are ⌊2ⁿ⌋ pure strategies with sign f = P.
  The proof is a construction: each strategy announces its identity in n
  bits, looks up P against the opponent's, and then both play the fixed
  lexicographically first line to the agreed result. It is sound for the
  ±1 entries. For the 0 entries it also needs a draw to be still
  attainable, which Definition 1 does not guarantee: it speaks only of
  wins and losses. Go with komi has no draws. So the theorem holds as
  stated for patterns of wins and losses, and for draws only in games
  that keep a draw open.
- Corollaries: a cycle of length ⌊2ⁿ⌋. Tic-Tac-Toe is 5.58-bit
  communicative, so every 47 × 47 pattern occurs.
- Proposition 1: Go is at least 1000-bit communicative, by alternately
  placing 180 stones on each half of the board, log₂ 180! bits. The reader
  computed log₂ 180! = 1093.9.
- Proposition 2: StarCraft, DOTA or Quake limited to 10 minutes give at
  least 36,000 bits, one bit per frame at 60 Hz.
- The strategies in these cycles are weak by construction: they spend the
  game signalling.

**Layered games and fixed-memory play** (pp. 6, 13).
- Definition 2: a k-layered game, in which every strategy in a higher
  layer beats every strategy in a lower one, with layer sizes rising to a
  peak z and then falling.
- Proposition 3: fixed-memory fictitious play, replacing "some strategy"
  with one that beats every member, converges if the population is at
  least as large as the lowest occupied layer and one member is above z.
  The proof counts at most |P| − 1 steps without climbing, but it never
  says which member is replaced, and the count depends on it.
- The reader's counterexample, checked by script: layers {W} above
  {R, P, S} (rock-paper-scissors) above {X, Y, Z} (a cycle), population
  {X, Y, R} of size 3. A pessimistic oracle picks the weakest strategy
  beating every member. If the newest member is replaced, the population
  cycles P, S, R, P, … for ever and never reaches W. If the oldest is
  replaced, it reaches W in two steps. The proposition holds with a
  replace-oldest rule, the one the experiments use.

**Nash clustering** (pp. 7, 13–14).
- Definition 3: take the support of the maximum-entropy Nash of the whole
  game as cluster 1, remove it, and repeat on what remains. The authors'
  own caution: "We do not claim that this is the only nor the best way of
  thinking about this phenomena, but we found it to have valuable
  mathematical properties" (p. 4).
- Theorem 2: RPP(C_i, C_j) ≥ 0 for j > i. The proof: shrinking the
  opponent's set cannot lower the value, and the support of the Nash of X
  holds X to value 0. The reader re-derived it.
- Theorem 3: if the population contains a whole cluster C_i, a strategy
  beating every member lies in some C_k with k < i. If it lay below,
  C_i's value against its cluster would be negative, contradicting
  Theorem 2.
- Both results hold in every finite symmetric zero-sum game. Neither uses
  the spinning-top shape.

**Empirical games** (pp. 8–9; supplement E, G, H).
- About 2000 sampled agents per game, around 1000 left after duplicate
  rows are removed: MinMax at depths 0–9 with 50 seeds, variants assuming
  value 0 beyond the horizon, MaxMin agents seeking to lose, and MCTS with
  10, 100 and 1000 simulations.
- Eight OpenSpiel games: Hex 3×3, Go 3×3 and 4×4, Quoridor 3×3 and 4×4,
  Tic-Tac-Toe, misère Tic-Tac-Toe and Connect Four. Plus AlphaStar's
  900-agent league.
- Profiles plot Nash cluster size against mean RPP. The eight board games
  and AlphaStar look like spinning tops, with a fitted skew-normal curve
  drawn over them.
- Blotto, Kuhn poker and noisy Elo games grow clusters with strength, the
  disc game is one cycle, and the Elo game is a line.
- The sampling caveat: "While this procedure does not guarantee uniform
  sampling of strategies, it at least provides decent coverage of the
  transitive dimension" (p. 9).
- On AlphaStar: "This heavily skewed strategies sampling means that what
  we are observing is a study of AlphaStar induced game geometry, rather
  then necesarily geometry of the StarCraft II itself" (p. 18).
- Maximum-entropy Nash makes the tops "heavy", as the authors say (p. 17).
- Learning experiment: start from the k weakest strategies and repeatedly
  replace the oldest with the weakest strategy that beats the population
  on average. Small k cycles, larger k saturates in suboptimal cycles, and
  past a critical k the run converges to the strongest strategies. In the
  disc game no k helps, and in the Elo game k = 1 suffices.

**Random Games of Skill** (supplement L, pp. 23–24).
- f(π_i, π_j) = ½(W_ij − W_ji) + S_i − S_j with Gaussian W and S.
- Proposition 4: if all |W_ij| < α/2, the S values within a Nash cluster
  span at most α. The proof is sound: a strategy α ahead in S strictly
  dominates the other.
- Theorem 4 claims S̄_{t+1} > S̄_t − W, with W of zero mean and variance
  σ²/m⁴, and E[S̄_{t+1}] > E[S̄_t] under a uniform improvement oracle.
  The proof has three faults.
  - It writes S_a − S_b = Q_ab − W̃_ab, which is not an identity. The
    inequality it wants, S_a − S_b > −W̃_ab, does follow from f(a, b) > 0.
  - Its variance line equates a variance with an expectation. The
    variance of W̃_ab/m is σ_W²/(2m²), quadratic in 1/m, not quartic.
  - It treats W̃_ab as zero-mean, but a is selected for beating b, which
    biases W̃_ab upward. The expected-improvement claim does not follow.
  Whether it is true is not settled by the paper. "it reduces the
  variance of W at a quartic rate" (p. 24) should not be cited.

## What it establishes and what it does not

**Established.**
- Theorem 1 for patterns of wins and losses, and Propositions 1–2 as
  lower bounds.
- Theorems 2–3 for all finite symmetric zero-sum games.
- Proposition 3 under a replace-oldest rule.
- Proposition 4.

**Not established.**
- **The spinning top itself.** The abstract's "We prove the existence of
  this geometry for a wide class of real world games by exposing their
  temporal nature" (p. 1) is retracted by the body: "Naturally, the above
  does not prove that real world games follow the Games of Skill
  geometry" (p. 6). Theorem 1 shows long cycles among weak, signalling
  strategies, the waist of the top. Nothing proves that cycles shrink
  toward strong play. The empirical support is sampled games whose
  profile depends on the sampler: search depth sets the transitive axis
  and seeds set the spread. The equilibrium chosen sets cluster sizes.
- **Theorem 4.**
- **The causal account of training systems** in Figure 3. The authors
  call it intuition.

## How it bears on the record

- **[CLAIM-451](../claims.d/CLAIM-451.md) and [TERM-077](../terms.d/TERM-077.md): when cycles are unavoidable.** Theorem 1
  is the record's most useful result in this group, and it is ordinal. It
  is stated for the sign of outcomes, which matches [ADR-052](../decisions.d/ADR-052.md)'s preference.
  Wherever parties can condition on who they face before the outcome is
  fixed, every pattern of wins, any cycle included, is realizable. Read
  for an organization, this is interpretive: if perspectives can
  recognize one another before a contest is settled, nothing in the
  structure of the contests rules out arbitrarily long cycles in the
  record of wins. An ordinal potential then has to come from what the
  perspectives actually do, not from what they could do. The
  constructions are weak strategies, and the paper's cycles sit where
  nobody is trying hard to win. **Supports the claim's premise that
  cycles are a structural possibility, and narrows where they are
  expected: among strategies that spend effort on recognition rather
  than on winning.**
- **Nash clustering and [CLAIM-451](../claims.d/CLAIM-451.md)'s accommodation.** A cyclic record
  layered into clusters weakly ordered between them, with all the
  cycling inside them, is a cardinal version of the condensation reading
  in [NOTE-tmpxufhw](NOTE-tmpxufhw.md). Theorem 3 gives a sufficient condition for a learner
  to climb out of a cycle: beat every member of a whole cluster. That is
  close to the claim's accommodation. A policy conditioned on a richer
  context covers the whole cyclic class at once instead of answering its
  latest member. **Complements; cardinal, so it needs [ADR-052](../decisions.d/ADR-052.md)'s
  statement of what the numbers mean if the record uses it.**
- **[CLAIM-443](../claims.d/CLAIM-443.md): memory against the incumbent.** Proposition 3's gap
  is a governance point in miniature. A fixed-memory population that
  drops its oldest member climbs; one that overwrites its newest can
  cycle for ever among regimes of one level. That is consistent with
  [NOTE-tmp8gje5](NOTE-tmp8gje5.md)'s self-play contrast. Which memory is kept, not only how
  much, decides whether learning escapes a cycle. **Bears, by analogy.**
- **[CLAIM-446](../claims.d/CLAIM-446.md) and [CLAIM-445](../claims.d/CLAIM-445.md).** Not addressed.
