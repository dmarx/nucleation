---
number: 988
status: Read
formerly:
- NOTE-tmpyi9oi
paper: 'LIT-1238'
title: 'Equitz and Cover — Successive refinement of information'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the scan of the published version (IEEE TIT
    37(2):269–275) posted on Thomas Cover's Stanford page
    (isl.stanford.edu/~cover/papers/paper94.pdf). The PDF is an image scan
    with a poor OCR layer, so all seven pages were read from page images
    rendered at 130 dpi, and every displayed equation (1)–(61) was read
    from the image. Read: the abstract, §I with Fig. 1, §II with
    Definitions 1–3, Figs. 2–3 and Theorem 1 (El Gamal–Cover, cited),
    §III with Theorem 2 and its proof and the code construction, §IV (the
    counterexample, Fig. 4 and Theorem 3), §V (Gaussian, Hamming and
    Laplacian examples), §VI, and the references. Not read: Theorem 3's
    proof, the counterexample's "detailed analysis" and the Hamming
    derivation, which the paper puts in Equitz's 1989 thesis [18]; and
    the cited theorems it rests on (El Gamal and Cover 1982, Ahlswede
    1985, Gray and Wyner 1974). Checked numerically with scripts in the
    session scratchpad: the Lloyd–Max thresholds of Fig. 1, the optimal
    output distributions (33)–(36) by Blahut–Arimoto, Theorem 3's condition
    (42) on a grid, and the Hamming transition (49) for random sources.
    The Gaussian and Laplacian constructions were re-derived by hand.
- version: 2
  date: '2026-10-20'
  note: >-
    The log-loss result recalled in Connections was misattributed. It is No and Weissman (ISIT 2015; No, Entropy 2019), not No, Ingber and Weissman (2016), which treats second-order refinability and was read in NOTE-980. That reading also shows the result concerns direct log-loss, where refinability is trivial. The information bottleneck is remote log-loss, so the result does not bear on QUESTION-220's stochastic half. Corrected in place.
date: '2026-10-20'
summary: >-
  Defines successive refinement: a description at distortion D₁, followed by
  an addendum reaching D₂ < D₁, with both stages at the rate–distortion
  limit. For finite alphabets it proves this possible iff some pair of
  optimal test channels forms a Markov chain X → X̂₂ → X̂₁, so that the coarse
  reconstruction is a stochastic degradation of the fine one, not
  necessarily a function of it. The condition holds for every discrete
  source under Hamming distortion, and the paper also shows it for the
  Gaussian under squared error and the Laplacian under absolute error. It
  fails for the three-letter source (1−p, 2p, 1−p)/2 under absolute error
  when p < 3 − 2√2, where the finer optimum uses fewer reproduction letters
  than the coarser. The whole result is asymptotic, for block codes. The
  paper's own Fig. 1 shows that single-shot optimal quantizers of a
  Gaussian do not nest even though the Gaussian is refinable.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-327 CLAIM-331 THEORY-257 — Proposed; entries named as not bearing, open -->
<!-- inactive-ok-file: THEORY-163 THEORY-751 — Proposed; the account this reading files, and an open reading it bears on, nothing here rests on their being settled -->
# NOTE-988: Equitz and Cover — Successive refinement of information

## Contribution

It asks whether a source can be described progressively without loss: first
at rate R(D₁), then refined by an addendum of R(D₂) − R(D₁) bits per symbol to
distortion D₂, as well as if D₂ had been the target from the start. Treating
this as the no-excess-rate case of the multiple-descriptions problem, it
reduces the question to a single-letter condition, a Markov chain between the
optimal test channels. It then shows three standard source–distortion pairs
satisfy it and gives a three-letter source that does not.

## Key insight

Lossless refinement means the coarse optimum must be obtainable by degrading
the fine optimum. Writing X̂₁ for the coarse reconstruction and X̂₂ for the
fine one, there must be optimal channels p(x̂₁|x) and p(x̂₂|x) and a channel
p(x̂₁|x̂₂) with p(x̂₁|x) = Σ_{x̂₂} p(x̂₂|x)p(x̂₁|x̂₂). When the optima at two
budgets are not related this way, an optimal coarse description is a
commitment that the finer optimum has to undo, and knowing the final budget
in advance is worth rate. The condition is about optimal *test channels* for
asymptotically long blocks. Optimal single-shot partitions of one sample are
a different object, and the paper's opening example shows they can fail to
nest when the block problem is refinable.

## Assumptions

- **A memoryless source.** X₁, X₂, … are i.i.d. ~ p(x). The rates and
  distortions are asymptotic (n → ∞), with per-letter additive distortion
  d(xⁿ, x̂ⁿ) = (1/n) Σ d(x_j, x̂_j) (eq. 4) and lim sup expected distortion
  (eqs. 5–6).
- **Finite alphabets for Theorem 2.** Definition 1 and Theorem 1 are stated
  for probability mass functions, and the reproduction alphabet is taken
  equal to the source alphabet ("X̂ = 𝒳", §II). The necessity half rests on
  Ahlswede's no-excess-rate converse, and the sufficiency half on El Gamal
  and Cover's achievable region. Both are cited, not proved, and both are
  discrete results. The distortion d: 𝒳 × X̂ → ℝ is otherwise arbitrary.
- **Points on the R(D) curve.** Successive refinement from D₁ to D₂
  (Definition 2) demands R₁ = R(D₁) and R₂ = R(D₂) exactly. "Successively
  refinable in general" (Definition 3) demands it for every pair D₁ ≥ D₂.
- **The continuous examples (§V-A, §V-C) go beyond Theorem 2's scope.**
  For the Gaussian the paper appeals to Gray and Wyner. For the Laplacian
  it exhibits the Markov chain only, and so relies on Theorem 2's
  sufficiency holding for densities, which is not shown.

## Key results

- **Definition 2.** Successive refinement from D₁ to D₂ (D₁ ≥ D₂) is
  achievable if there are encoders iₙ: 𝒳ⁿ → {1…2^{nR₁}},
  jₙ: 𝒳ⁿ → {1…2^{n(R₂−R₁)}} and decoders g₁ₙ(i), g₂ₙ(i, j) with
  lim sup E d(Xⁿ, X̂₁ⁿ) ≤ D(R₁) and lim sup E d(Xⁿ, X̂₂ⁿ) ≤ D(R₂), at
  R₁ = R(D₁), R₂ = R(D₂).
- **Theorem 1 (El Gamal and Cover 1982, cited).** (R₀, R₁, D₀, D₁, D₂) is
  achievable for multiple descriptions if some p(x̂₀, x̂₁, x̂₂|x) has
  E d(X, X̂ₘ) ≤ Dₘ and R₀ > I(X; X̂₀), R₁ > I(X; X̂₁),
  R₀ + R₁ > I(X; X̂₀, X̂₁, X̂₂) + I(X̂₀; X̂₁) (eqs. 7–9). Ahlswede showed
  these conditions are also necessary when R₀ + R₁ = R(D₂).
- **Theorem 2 (Markovian characterization).** Successive refinement from
  D₁ to D₂ is achievable **iff** there is a p(x̂₁, x̂₂|x) with
  E d(X, X̂₁) ≤ D₁, E d(X, X̂₂) ≤ D₂, I(X; X̂₁) = R(D₁), I(X; X̂₂) = R(D₂),
  and p(x̂₁, x̂₂|x) = p(x̂₂|x)p(x̂₁|x̂₂) (eqs. 11–15). That is, X → X̂₂ → X̂₁,
  equivalently X̂₁ → X̂₂ → X.
  - *Sufficiency* takes X̂₀ constant in Theorem 1, so that (18) collapses
    to I(X; X̂₁, X̂₂) = I(X; X̂₂) by the Markov chain (eq. 19).
  - *Necessity* runs the chain (23)–(26):
    R(D₂) ≥ I(X; X̂₀, X̂₁, X̂₂) + I(X̂₀; X̂₁) = I(X; X̂₂) + I(X; X̂₁|X̂₂)
    + I(X; X̂₀|X̂₁, X̂₂) + I(X̂₀; X̂₁) ≥ I(X; X̂₂) ≥ R(D₂). Every slack is then
    zero, including I(X; X̂₁|X̂₂) = 0 (eq. 29).
  - *Holds when:* finite alphabets, as above. The paper's abstract says "the
    individual solutions … can be written as a Markov chain". The theorem
    asks only that *some* pair of optimal test channels do so, which
    matters where the optimum is not unique.
- **Tree-structured codes (§III-B).** Draw 2^{nR₁} first-stage codewords
  i.i.d. from p(x̂₁). Under each one, draw 2^{n(R₂−R₁)} second-stage
  codewords from Π p(x̂₂|x̂₁). Encode by minimum distortion at each stage.
  Optimality of such tree codes is asymptotic only.
- **Counterexample (§IV, Gerrish's problem via Berger's textbook,
  exercise p. 61).** 𝒳 = X̂ = {1, 2, 3}, P_X = [(1−p)/2, p, (1−p)/2],
  d = |x − x̂|, z = e^{R′(D)} ∈ (0, (1−p)/(1+p)]. The optimal backward channel
  with all three letters in use is (33),
  P_{X|X̂} = (1/(1+z))·[[1, z(1−z), z²], [z, 1−z, z], [z², z(1−z), 1]], with
  output law (34). With only the outer letters in use, P_X̂ = [½, 0, ½] (36)
  and P_{X|X̂} is (35), whose middle column is p in both rows. For
  p < 3 − 2√2 there is a middle range of z in which the optimum drops the
  middle letter. Take D₂ in that range (z₂ = (1−p)/2) and D₁ > D₂ in the
  upper three-letter range. A Markov chain X̂₁ → X̂₂ → X would make every row
  of P_{X|X̂₁} = P_{X̂₂|X̂₁}P_{X|X̂₂} (eq. 39) have middle entry p. But (33)
  has middle entries z₁(1−z₁)/(1+z₁) and (1−z₁)/(1+z₁), which are equal only
  at z₁ = 1, and z₁ ≤ (1−p)/(1+p) < 1. So this source is not successively
  refinable from D₁ to D₂.
- **Theorem 3 (proof in the thesis [18]).** For the same source and any
  0 < p < 1, if both optima use all three letters, refinement from D₁ to D₂
  (D₁ > D₂) is achievable iff (1 + e^{R′(D₁)})(1 + e^{R′(D₂)}) ≤ 2 (eq. 42).
- **Gaussian, squared error (§V-A).** p(x̂₁) = N(0, σ² − D₁),
  p(x̂₂|x̂₁) = N(x̂₁, D₁ − D₂), p(x|x̂₂) = N(x̂₂, D₂) (eqs. 43–45) give the
  Markov chain with the right marginals. (R₁, R₂) = (½ log σ²/D₁,
  ½ log σ²/D₂) (eq. 46). The tree code needs 2^{nR(D₁)} + 2^{n(R(D₂)−R(D₁))}
  distance computations instead of 2^{nR(D₂)}.
- **Any discrete source, Hamming distortion (§V-B).** The optimum is
  "upside-down waterfilling" (Erokhin; Pinkston):
  p_X̂(a) = (p_X(a) − λ)⁺ / Σ_x (p_X(x) − λ)⁺ (47), with the backward channel (48).
  The degrading channel p(x̂₂|x̂₁) is given in closed form (49), with no
  derivation in the paper.
- **Laplacian, absolute error (§V-C).** f(x) = (α/2)e^{−α|x|},
  R(D) = −log(αD) for 0 < D ≤ 1/α (51), and f_{X|X̂}(x|x̂) = (1/2D)e^{−|x−x̂|/D}
  (52–53). The refining kernel has characteristic function Φ_{g₁}/Φ_{g₂}
  (58–60). Its inverse transform is
  h(x̂₂|x̂₁) = (D₂/D₁)² δ(x̂₂ − x̂₁) + (1 − (D₂/D₁)²)(1/2D₁)e^{−|x̂₂−x̂₁|/D₁}
  (eq. 61, regrouped). This is a probability density for D₂ ≤ D₁.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For finite alphabets, successive refinement from D₁ to D₂ is achievable iff some pair of optimal test channels satisfies X → X̂₂ → X̂₁ | strong for finite alphabets; it rests on two cited theorems | Theorem 2. The converse is re-derived here without Ahlswede ([THEORY-751](../theory.d/THEORY-751.md)); achievability rests on El Gamal–Cover |
| C2 | Tree-structured descriptions are optimal iff the problem is successively refinable | strong as a restatement of C1, asymptotic only | §III-B; the abstract states it without the asymptotic qualifier |
| C3 | Every finite-alphabet source is successively refinable under Hamming distortion | strong (the formula is given, not derived) | (47)–(50); checked numerically here for random five-letter sources |
| C4 | Gaussian/squared-error and Laplacian/absolute-error sources are successively refinable | moderate: the Markov chains are right, the extension of Theorem 2 to densities is not shown | §V-A (via Gray–Wyner), §V-C; both constructions re-derived here |
| C5 | Not every source is successively refinable: the three-letter source with p < 3 − 2√2 under absolute error fails for suitable D₁ > D₂ | strong, with printing slips (see Limitations) | §IV, eqs. (31)–(41); re-derived and checked numerically here |
| C6 | Theorem 3's condition (1 + z₁)(1 + z₂) ≤ 2 for full-support optima | moderate: proof not in the paper | eq. (42); confirmed here on a grid for p ∈ {0.1, 0.2, 0.3, 0.4, 0.45}, no disagreement off the diagonal z₁ = z₂ |
| C7 | Even when every optimum uses all three letters, D₁ and D₂ can be chosen to make refinement fail, "for example, if p > 3 − 2√2" | weak: false as stated for p ≥ √2 − 1 | see Limitations |

## Method

The method is a reduction, not an algorithm. Successive refinement is
multiple descriptions with no constraint on the side receiver's distortion
and no excess rate (R₁ = R(D₁), R₀ + R₁ = R(D₂)). In that regime the El
Gamal–Cover region is tight (Ahlswede), and the information inequalities
force the Markov chain. Each example is then settled by exhibiting a
degrading channel (Gaussian, Hamming, Laplacian) or proving that none exists
(three-letter source). The examples use the Kuhn–Tucker form of the optimal
backward channel, p(x|x̂) ∝ p(x)λ(x)z^{d(x,x̂)}.

## Concepts

- **Successive refinement (Definition 2)**: two-stage block coding in which
  each stage meets the rate–distortion bound; the second stage is an
  addendum to the first.
- **Successively refinable in general (Definition 3)**: successive
  refinement achievable for every D₁ ≥ D₂.
- **Markov compatible**: the optimal p(x̂₁|x) and p(x̂₂|x) admit a joint
  p(x̂₁, x̂₂|x) with X → X̂₂ → X̂₁. The coarse reconstruction is a *noisy
  function* of the fine one. It need not be a deterministic function of it.
- **No excess rate**: R₀ + R₁ = R(D₂), the multiple-descriptions regime in
  which the El Gamal–Cover conditions are necessary as well as sufficient.

## Connections

The paper builds on multiple descriptions (Witsenhausen, Wolf, Wyner, Ziv,
Ozarow, El Gamal and Cover, Zhang and Berger, Ahlswede). It is related to
Gray's conditional rate–distortion function, to Yamamoto's cascade coding,
to Kaspi and Berger, and to Gray and Wyner's simple network, from which the
Gaussian case is drawn. The counterexample is Gerrish's (1963 thesis), set
as an exercise in Berger's *Rate Distortion Theory* (1971). Amir Dembo
suggested it. Tree-structured vector quantization (Chou, Lookabaugh and
Gray 1989) is the practical counterpart cited.

What follows is the record's knowledge from memory; it was not checked in
this reading and none of these works is registered. Koshelev's papers on
hierarchical coding (Problems of Information Transmission, from 1980) are
usually credited with the sufficiency half independently. Rimoldi (1994)
characterized the full achievable rate region, with excess rate allowed.
Chow and Berger (1997) gave failures for symmetric Gaussian mixtures under
squared error. Lastras and Berger (2001) showed that every source is
nearly refinable: under squared error the rate loss is at most half a bit
per sample. No and Weissman (ISIT 2015) show that every discrete memoryless source is
refinable under logarithmic loss. This NOTE first credited the result to
No, Ingber and Weissman (2016), which is a different paper ([NOTE-980](NOTE-980.md)).
The result concerns *direct* log-loss, soft reconstructions of the source
itself, where R(D) = H − D and refinability is trivial. The information
bottleneck is *remote* log-loss, scored on Y. So the result does not bear
on [QUESTION-220](../questions.d/QUESTION-220.md) ([NOTE-980](NOTE-980.md)).

## Bearing on the record

- **[QUESTION-220](../questions.d/QUESTION-220.md): answers in part, for rate–distortion.** The
  classical answer is filed as [THEORY-751](../theory.d/THEORY-751.md). Three things change in
  how the question should be read.
  1. **"Nested" in the classical sense is a Markov chain, not a function.**
     The question's title asks for "the coarser optimum is a function of
     the finer". Equitz and Cover ask only that the coarse optimum be a
     stochastic degradation of the fine. The function version is the
     deterministic special case. For deterministic encoders T₁ = f₁(X),
     T₂ = f₂(X) the two coincide: I(X; T₁|T₂) = H(T₁|T₂) − H(T₁|X, T₂) =
     H(T₁|T₂), so X → T₂ → T₁ iff T₁ is a function of T₂, iff partition 2
     refines partition 1 on the support. For stochastic encoders, the
     Markov chain is the right target and the title asks for more.
  2. **The transfer to the information bottleneck is formal, and plausible
     but unproved here.** IB is rate–distortion with reproduction alphabet
     Δ(Y), the distributions over Y, and distortion
     d(x, q) = KL(p(y|x) ‖ q) ([NOTE-300](NOTE-300.md) records that this distortion
     "emerges" in [LIT-338](../literature.d/LIT-338.md)). For any encoder with Z – X – Y,
     E KL(p(y|X) ‖ q_Z) ≥ H(Y|Z) − H(Y|X) = I(X;Y) − I(Z;Y), with equality
     at q_z = p(y|z). So the relevance loss is the expected distortion, and
     an IB optimum at β is a point of this R(D) curve where it is strictly
     convex. Theorem 2 then says the IB is successively refinable between
     two such points iff some pair of optima, with clusters identified by
     their decoders p(y|z), satisfies X → Z₂ → Z₁. That is exactly the
     question's condition, now with an operational meaning: progressive
     block coding of Xⁿ for relevance about Yⁿ loses nothing. The steps the
     paper does not supply are the extension to an infinite reproduction
     alphabet (Δ(Y) is compact and KL lower semicontinuous, so
     quantization should carry it), and the β ↔ D correspondence on flat
     stretches of the IB curve, where one β has many optima.
  3. **Refinability is not generic.** C5 shows that the Markov condition
     can fail for a three-letter source with a natural distortion. The
     failure is the shape the question worries about: at the finer
     distortion the optimum *drops* a reproduction letter (the rare middle
     one) that the coarser optimum uses, so the coarse optimum is not a
     merging of the fine one's cells.
- **Brute-force check for the information bottleneck (the record's, not
  the paper's).** Script:
  `/tmp/claude-0/-home-user-nucleation/409f735e-c44b-5ba1-82f0-18d34af58efc/scratchpad/ec-scripts/ib_nesting_bruteforce.py`.
  Every set partition of X was enumerated as a deterministic encoder
  (I(X;T) = H(T), so IB and deterministic IB coincide). The script traced
  the optima of I(T;Y) − H(T)/β along the upper concave hull of
  (H(T), I(T;Y)) and tested whether each refines the last.
  - **The smallest clean example.** X uniform on four states,
    p(y = 1|x) = (0, 0, 1/8, 3/8). The optimum is the one-cell partition
    for β < 6.90 and {0,1,2 | 3} for 6.90 < β < 9.26 (H = 0.811 bits,
    I(T;Y) = 0.1175). For 9.26 < β < 16.06 it is {0,1 | 2,3} (H = 1,
    I = 0.1379), then {0,1 | 2 | 3}. The second and third optima are
    incomparable partitions: state 2 moves from 3's complement to 3's
    cell. The cheap, unbalanced cut is optimal at a low budget, and a
    larger budget buys the balanced cut instead of a split of the
    unbalanced one. (Hand check: I = h(1/8) − ¾h(1/24) − ¼h(3/8) = 0.1175
    and h(1/8) − ½h(1/4) = 0.1379, with h the binary entropy.)
  - **Non-nesting is common in random instances.** Among random joints
    p(x, y) drawn from a flat Dirichlet, consecutive Lagrangian optima
    failed to nest in 40/300 (four states, binary Y), 25/300 (four states,
    ternary Y), 83/300 and 62/300 (five states), and 43/120 and 30/120
    (six states). The cardinality-budget version, the best partition into
    k cells for k = 1, 2, …, failed in 11–44 per 300. That version is the
    analogue of the paper's Fig. 1.
  - **Stochastic encoders: a heuristic only.** For the four-state example,
    multi-restart self-consistent IB iterations at β = 8, 10, 12 and 20
    found optima with two, three, three and three clusters. A linear
    programme found no stochastic p(z₁|z₂) with
    p(z₁|x) = Σ p(z₂|x)p(z₁|z₂) for (8, 10), (8, 12) or (10, 12): the least
    L1 residuals were 1.1 × 10⁻², 2.5 × 10⁻² and 4.6 × 10⁻². The β = 20
    optimum degrades exactly to each of the others. Scripts:
    `ib_stochastic_check.py` and `ib_stochastic_polish.py` in the same
    directory. Global optimality is not certified and uniqueness of the
    optima is not checked, so this suggests, and does not show, that the
    unrestricted IB on this four-state source is not successively
    refinable between β = 8 and β = 12. Nothing is filed for it.
- **[NOTE-676](NOTE-676.md) (G-tree search).** Its nesting across the compression weight
  comes from restricting encoders to prunings of one fixed tree, and the
  example above shows what that restriction excludes. The two optima
  {0,1,2 | 3} and {0,1 | 2,3} are not laminar ({0,1,2} and {2,3} overlap),
  so no single tree has both as prunings. Any fixed-tree search on that
  source must miss one of the two unrestricted optima, and the nesting is
  bought by that loss. More generally, Equitz and Cover's notion is
  asymptotic and stochastic. The paper's own Fig. 1 makes the point for
  single-shot deterministic partitions. The optimal 2-, 4- and 8-level
  quantizers of N(0, 1) have thresholds {0}, {0, ±0.9816} and
  {0, ±0.5005, ±1.0500, ±1.7479} (recomputed here by Lloyd's algorithm;
  D = 0.3634 = (π − 2)/π at one bit). So 4 refines 2 and 8 does not
  refine 4, although the Gaussian is successively refinable. Refinability
  of a source therefore says nothing about nesting of the optimal
  partitions of one sample, which is [NOTE-676](NOTE-676.md)'s setting.
- **[THEORY-163](../theory.d/THEORY-163.md) and [NOTE-631](NOTE-631.md) (colour naming).** Whether the annealed
  categories nest is now a definite test: whether the encoders at
  successive β satisfy X → Z_{β₂} → Z_{β₁}, by the linear programme above.
  The four-state heuristic suggests that a bifurcation sequence need not
  pass it.
- **[QUESTION-217](../questions.d/QUESTION-217.md).** Its "refinement order" presupposes that the optima
  form a chain under refinement. The counterexample and the brute force
  say they need not. The refinement relation among optima across budgets
  is in general a partial order, and its maximal chains may skip budgets.
- The other key entries named for this batch ([THEORY-733](../theory.d/THEORY-733.md), [THEORY-257](../theory.d/THEORY-257.md),
  [THEORY-661](../theory.d/THEORY-661.md), [CLAIM-157](../claims.d/CLAIM-157.md), [CLAIM-331](../claims.d/CLAIM-331.md), [CLAIM-327](../claims.d/CLAIM-327.md), [CLAIM-388](../claims.d/CLAIM-388.md),
  [THEORY-755](../theory.d/THEORY-755.md)) concern dynamics and aggregation, not compression. The
  reading does not bear on them.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Printing slips in §IV.** The conditions attached to (34) and (36) are
  reversed. The middle mass in (34) is (p − z + pz + z²)/(1 − z)², which is
  negative exactly between the roots of z² − (1−p)z + p. So the
  three-letter solution (34) holds when |z − ½(1−p)|² ≥ ¼(p² − 6p + 1), and
  [½, 0, ½] (36) holds inside that interval. As printed it is the other way
  round, and the paper's own choice z₂ = ½(1−p), "in the region for which
  p(x̂) = (1/2, 0, 1/2)", contradicts the printed condition. The lower bound
  in (37) must be ½[(1−p) + √(p² − 6p + 1)]. Read with the ½ on the first
  term only, as typeset, the interval is empty at p = 0.1 (1.090 > 0.818).
  Blahut–Arimoto confirms the corrected regions: for p = 0.1 the middle
  letter is dropped for z ∈ (0.130, 0.770). The argument itself is
  unaffected.
- **C7 is overstated.** Theorem 3 needs (1 + z₁)(1 + z₂) > 2 for a failure,
  and z ≤ (1−p)/(1+p) on the whole curve. So failures with full support
  exist only if (2/(1+p))² > 2, i.e. p < √2 − 1 ≈ 0.414. For p ≥ √2 − 1
  (where p > 3 − 2√2 also makes every optimum full-support) the source is
  successively refinable everywhere. The "for example" covers only
  3 − 2√2 < p < √2 − 1. Confirmed on a grid: no failure at p = 0.45, and
  failures at p = 0.4 only near the top of the curve.
- **The theorem is proved for finite alphabets and applied to densities.**
  The Gaussian case defers to Gray and Wyner, and the Laplacian case shows
  only the Markov chain.
- **The counterexample tacitly assumes unique optimal test channels.** It
  speaks of "the" solution. At D₁ uniqueness holds, because the 3 × 3 matrix
  [z^{|x−x̂|}] is nonsingular (determinant (1 − z²)²); at D₂ the two used
  columns are independent. So the argument stands, but the paper does not
  say why.
- **"Tree structured descriptions are optimal iff …" (abstract)** is
  asymptotic. The paper says so in §III-B, and Fig. 1 shows how
  single-shot tree quantizers fail.
- **Only two stages, only D₁ ≥ D₂ on the R(D) curve, and no excess
  rate.** How much rate a non-refinable source loses is not treated (see
  Lastras and Berger, above).
- Theorem 3's proof and the Hamming derivation are not in the paper.

## Open questions

- Is there a structural condition on p(x, y) under which the information
  bottleneck is successively refinable for every β₁ < β₂, the analogue of
  "Hamming distortion makes every discrete source refinable"? The
  direct log-loss result does not answer it (see Connections). Charvin,
  Catenacci Volpi and Polani (2023) give a test by linear programming for
  exact IB refinability, and are the nearest lead.
- Does the four-state example's non-nesting survive with stochastic
  encoders under a certified global optimum? The IB curve for four source
  states can be computed to certified precision by convex relaxation or a
  fine grid over encoders with at most four clusters; that would settle it.
- How large is the rate loss from progressive IB coding when refinement
  fails, and is it bounded by a constant as under squared error?
