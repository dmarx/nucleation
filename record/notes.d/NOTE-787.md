---
number: 787
status: Read
formerly:
- NOTE-tmpjcfop
paper: LIT-239
title: "Vereshchagin & Vitányi — Kolmogorov's structure functions and model selection"
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv v5 PDF (arxiv.org/pdf/cs/0204037, 25 pp.,
    5 Aug 2004, the final journal version), text extracted with pdftotext:
    §§I–VIII and Appendices A (oral history), B (extended models), C
    (proofs) and D (computability). Of the proofs, those of Lemma IV.2
    (Claim C.1), Theorem IV.4 (Claims C.2–C.3), Theorem IV.8 (inequalities
    C.2–C.4, Lemma C.4 and Claim C.5), Theorem IV.11, Theorems VIII.2 and
    VIII.4, Propositions B.1–B.2, Lemma V.2 and Theorems D.1, D.5 and D.6
    were read step by step. The construction proving Theorem D.2 was read
    through, but its invariants (1)–(5) were not checked line by line. The
    skim note filed with the paper is NOTE-202.
- version: 2
  date: '2026-10-14'
  note: >-
    The paper's §VI-D threshold for non-stochastic strings, quoted under
    Key results, is annotated with the bound Corollary IV.9 actually gives
    (n − √n − O(log n)), with a pointer to CLAIM-289.
date: '2026-10-14'
summary: >-
  For a string x of length n and every complexity bound α, the minimal
  two-part code length λ_x(α), the structure function h_x(α) + α and the
  best achievable fit β_x(α) + K(x) are one function to within O(log n),
  and any set witnessing λ_x or h_x also witnesses β_x. Every non-increasing
  shape occurs for some x. h_x and λ_x are upper semicomputable but not
  computable; β_x is not even semicomputable. Finite sets only; the
  extension to computable distributions costs O(log n).
---
<!-- inactive-ok-file: THEORY-277 THEORY-036 THEORY-087 CLAIM-188 — Proposed; the theory filed from this reading and the entries it bears on, open -->
<!-- inactive-ok-file: LIT-229 — Deferred; Vitányi's "Meaningful information", the paper's reference for total-recursive-function models, unread here -->

# NOTE-787: Vereshchagin & Vitányi — Kolmogorov's structure functions and model selection

## Contribution

Before this paper there were three functions of a single string and a
complexity bound α, each a candidate for "the best model of complexity at
most α": Kolmogorov's structure function h_x (smallest set), the two-part
code length λ_x (MDL) and the minimal randomness deficiency β_x (best
fit). Only a one-sided relation was known (Gács, Tromp & Vitányi). The
paper proves that the three are the same function to within O(log n),
gives the complete set of shapes they can take, and settles their
computability. After it, minimising a two-part code within a complexity
class has a guarantee about the individual datum, with no probabilistic
assumption.

## Key insight

For finite-set models, a smallest set S ∋ x of complexity at most α is
also, up to O(log n), the set in which x is most typical. The reason is
the identity δ(x | A) = Λ(A) − K(A | x*) − K(x) + O(1) (C.4): a set's
deficiency is its two-part length less the information x has about it.
Minimising Λ already leaves little room for K(A | x*). So the quantity one
cannot even approximate, goodness of fit, is reached by minimising one
that can be approximated from above, code length.

## Assumptions

- **Data.** A single finite binary string x of length n, with K(x) = k.
  No source and no distribution are assumed.
- **Models.** Finite sets S ∋ x. Model cost is the prefix complexity K(S)
  of a program listing S. Data-to-model cost is the worst-case index
  length log |S|, not K(x | S). The paper calls this choice essential: the
  "ultimate compression" K(A) + K(x | A) can select badly fitting models
  (§V-B(iii)).
- **Precision.** Every main result holds to within additive terms
  logarithmic in n, in argument and in value. Equality is the closeness
  of Definition IV.1. Two functions agree if each lies in a strip of
  width ε(i), δ(i) about the other.
- **Extended models (App. B).** Computable probability mass functions,
  with data-to-model cost −log P(x), and total recursive functions, with
  cost l_x(p) = min{|d| : p(d) = x}, are equivalent to finite sets to
  within O(log n). This holds only after restricting to K(P) ≤ n + O(log n)
  and −log P(x) ≤ n + O(1), which Remark B.3 shows costs nothing more than
  O(log n). The paper says plainly that this is not the classical setting.
  Bernoulli or k-state Markov classes are poorer than "computable
  distributions of complexity ≤ α", and a Bernoulli model with a
  non-computable bias lies outside the class. The results "cannot be
  directly transplanted to the traditional setting" and are "pristine
  truths that hold in a platonic world" (§IV-D).

## Key results

Notation: δ(x | S) = log |S| − K(x | S); Λ(S) = K(S) + log |S|;
h_x(α) = min{log |S| : S ∋ x, K(S) ≤ α};
λ_x(α) = min{Λ(S) : S ∋ x, K(S) ≤ α};
β_x(α) = min{δ(x | S) : S ∋ x, K(S) ≤ α}.

- **Lemma IV.2.** λ_x(α) ≤ h_x(α) + α ≤ λ_x(α) + K(α) + O(1). *Holds for*
  every x and α. The proof (Claim C.1) splits a set into 2^m equal parts,
  so h_x(α) + α is non-increasing up to K terms.
- **Theorem IV.8 (the main result).** β_x(α) + k ≅ λ_x(α) with
  ε = δ = O(log n). *Holds for* every x of length n. The direction
  β_x(i) + k ≤ λ_x(i) + O(1) (C.2) is immediate from (C.4). The converse
  (C.3) rests on Lemma C.4: for every A ∋ x there is S ∋ x with
  K(S) ≤ K(A) − K(A | x) + O(log Λ(A)) and ⌈log |S|⌉ = ⌈log |A|⌉. Its
  proof enumerates, from K(A), ⌈log |A|⌉ and K(A | x), at most
  2^{K(A) − K(A|x) + O(log m)} sets covering every string that lies in
  enough generated A's (Claim C.5). The counting checks out.
- **Remark IV.10.** Every S ∋ x of complexity at most α + O(log n) that
  minimises Λ(S) has δ(x | S) ≤ β_x(α) + O(log n). The converse fails. A
  set witnessing β_x need not witness λ_x or h_x. The counterexample is a
  random x and S₁ = {0,1}ⁿ ∪ {y} with K(x, y) ≥ 3n/2, which has
  Λ(S₁) = 3n/2 against λ_x(n/2) = n.
- **Theorem IV.11.** If A has near-best fit at α but Λ(A) ≫ λ_x(α) or
  log |A| ≫ h_x(α), then a much simpler S with Λ(S) ≈ λ_x(α) exists. At
  the "critical" α where λ_x drops, witnesses of β_x witness λ_x and h_x
  too.
- **Theorem IV.4 and Corollary IV.9 (all shapes).** For every x there is
  a non-increasing λ with λ(0) ≤ n, λ(k) = k and λ_x ≅ λ within
  K(n) + O(1). Conversely, for every such λ there is an x of length n and
  complexity k ± (K(k, n, λ) + O(1)) with λ_x ≅ λ within K(i, n, λ) + O(1).
  The same holds for β_x with β(0) ≤ n − k, β(k) = 0 and precision
  O(log n) + K(β). The construction takes the lexicographically first x
  outside every set of small Λ, with at most 2^{i+1} replacements (Claim
  C.3).
- **Non-stochastic strings (§V-E, §VI-D).** For α₀ + β₀ < n − c log n − C
  there are strings of length n with β_x(α₀) > β₀. This strengthens Shen's
  2α₀ + β₀ bound. In particular there are strings of complexity
  n − √n ± O(log n) with deficiency about √n relative to every set of
  complexity below n − O(log n). (The paper's phrase. Corollary IV.9
  gives it only below n − √n − O(log n), since {x} has complexity about
  n − √n and deficiency O(1); see [CLAIM-289](../claims.d/CLAIM-289.md).)
- **Snooping curves (Lemma V.1).** The least cumulative log loss
  L_x(α) of a predictor of complexity at most α equals h_x(α) within
  O(log n) in argument and value. A smallest set is a best predictor.
- **MDL search (§V-B, Lemma V.2).** Dovetail all programs and keep the
  (p, S) with least |p| + log |S|. At every step this carries the bound
  δ(x | L_t) + K(x) ≤ |p_t| + log |S_t| + O(1), and the limit is within
  O(log n) of the best fit at a non-critical α. Lemma V.2: if
  Λ(S₂) ≤ Λ(S₁) − 2c log |x|, then δ(x | S₂) ≤ δ(x | S₁) − c log |x| + O(1)
  when p₁ is a shortest program for S₁. The printed statement has
  δ(x | S₂) on both sides, a typo for S₁ on the right.
- **Fine structure (§VI).** h_x(α) = ∞ for α < m(x) − O(1), where m(x) is
  the least monotone lower bound of K. The minimal sufficient statistic
  has complexity at least K(K(x)) − O(1). Past it, h_x hugs the sufficiency
  line in "bumps" of size O(log(K(x) − α₀)). Only 2^{c₁ + c₂ + 1}
  distinct sets lie within c₂ of the line.
- **Computability (§VII, App. D).**
  - h_x and λ_x are upper semicomputable.
  - Theorem D.1: no algorithm, given k and x of length k + d log k with
    |K(x) − k| ≤ 2 log k, always outputs a value within c log k of λ_x(α)
    for even one α in [2 log k, k].
  - Theorem D.2 and Corollary D.3: even given K(x) exactly, no algorithm
    approximates λ_x within ε = δ = |x|/(10 log |x|).
  - Theorem D.5 (Muchnik): given the complexity α₀ of the minimal
    sufficient statistic as well, λ_x can be computed over its whole
    domain to that precision.
  - Theorem D.6: β_x is not lower semicomputable to within |x|/3 and not
    upper semicomputable to within |x|/log⁴ |x|, but it is computable from
    the halting oracle.
- **Uniform witnesses (§VIII).** Theorem VIII.4 and Corollary VIII.5: the
  sets S_i^l, built from the binary expansion of the number N^l of strings
  of complexity ≤ l, witness h_x, λ_x and β_x at every α to within
  O(log n). At a critical α every λ_x-witness is algorithmically
  equivalent to N^α, so the best model there encodes a halting-problem
  prefix.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | At every complexity bound, a set minimising two-part length (or log-cardinality) is within O(log n) of the best achievable fit | strong | Theorem IV.8, proof via (C.4) and Lemma C.4, read |
| C2 | The converse fails: a best-fitting set need not minimise code length, except at critical complexities | strong | Remark IV.10 counterexample; Theorem IV.11 |
| C3 | Every non-increasing shape of λ_x, h_x + α or β_x + K(x) is realised by some string, to logarithmic precision | strong | Theorem IV.4, Corollary IV.9, constructive proofs read |
| C4 | Code length can be approximated from above; fit cannot be approximated in either direction, and the minimal sufficient statistic cannot be found from x and K(x) | strong | Theorems D.1, D.2, D.6 and Corollary D.3 |
| C5 | Minimising K(A) + K(x \| A) instead of K(A) + log \|A\| can select a model far from best fit | moderate | the two examples of §V-B(iii), not a theorem |
| C6 | The results carry over to computable probability models and total recursive functions | moderate | Propositions B.1–B.2 and Remark B.3, at O(log n) precision and for K(P) ≤ n + O(log n) only |
| C7 | Strings whose structure function stays far above the sufficiency line until α ≈ K(x) are "common" | weak | they exist in every (n, k) by Corollary IV.9; no measure of how many is given |

## Method

Two counting devices carry the paper. The first is the enumeration of
Claim C.2: run all programs, strike out every string that lands in a set
of small two-part length, and take the first survivor. The second is the
covering of Lemma C.4. Given K(A), ⌈log |A|⌉ and K(A | x), enumerate all
sets of that complexity and size. Mark every string covered by at least
2^{K(A|x) − δ} of them, and chop the marked strings into blocks of size
|A|. Few blocks are needed, and x is in one of them. Both devices produce
objects whose complexity is bounded by a count of halting programs. That
is why every result carries O(log n) and none is effective.

## Concepts

- **Randomness deficiency δ(x | S).** log |S| − K(x | S). Small deficiency
  means x has every simple property that most members of S have (Lemma
  II.3).
- **Optimal set, sufficient statistic.** S ∋ x with Λ(S) ≤ K(x) + c. A
  shortest program for it is a sufficient statistic. The least complex one
  is the minimal sufficient statistic, and its complexity is the number of
  bits of "meaningful information" in x.
- **Sufficiency line.** L(α) = K(x) − α, the lower bound on h_x.
- **Critical α.** A complexity at which λ_x(i) decreases as i → α from
  below.
- **(α, β)-stochastic.** β_x(α) ≤ β. "Positively random" strings have a
  simple sufficient statistic; "negatively random", non-stochastic ones
  do not (Fig. 4, after Kolmogorov's 1974 abstract).

## Connections

The paper completes the algorithmic sufficient statistic of Gács, Tromp
and Vitányi (2001), who had β_x(α) ≤ h_x(α) + α − K(x) + O(1). It extends
V'yugin's shapes for β_x, which held only for α = o(n), and Levin's
unpublished result reported in Appendix A. Its §V-B gives ideal two-part
MDL the individual-data foundation that Vitányi & Li ([LIT-225](../literature.d/LIT-225.md)) argue for
through Bayes's rule. Rissanen (2002) is cited for carrying the structure
function to statistical model classes. Grünwald & Vitányi ([LIT-224](../literature.d/LIT-224.md),
§6) restate the main results and relate the expected structure function to
Shannon's distortion-rate function. Grünwald & Roos ([LIT-238](../literature.d/LIT-238.md), §7) point
to Rissanen's later use of the structure function. Theorem VIII.4 builds
on [LIT-229](../literature.d/LIT-229.md)'s total-recursive-function models (cited as [25]).

## Bearing on the record

- **No THEORY, QUESTION or CLAIM cited this paper before today.** Its
  main result is filed as [THEORY-277](../theory.d/THEORY-277.md).
- **[CLAIM-152](../claims.d/CLAIM-152.md) (sufficiency is relative to a target).** The algorithmic
  sufficient statistic is a sufficiency with no outcome variable Y. It is
  sufficient for x itself, relative only to the reference machine, up to
  O(1). That is a qualification of the claim's "any individuation built on
  sufficiency", not a counterexample to its point. The minimal sufficient
  statistic is defined only to logarithmic precision. It cannot be
  computed (Corollary D.3). At non-critical complexities, distinct and
  independent sets witness the same code length. For a random x at α = n/2
  these are the prefix set and the suffix set (§VIII). So it does not give
  a unique boundary either.
- **[QUESTION-040](../questions.d/QUESTION-040.md) and [CLAIM-188](../claims.d/CLAIM-188.md) (what an Occam term should count).** Here
  the Occam term is K(S), the length of a program for the model, not a
  parameter count or a posterior volume. The paper's own warning (§IV-D)
  applies before carrying it over: parametric classes are not
  complexity-bounded classes. It adds a caution the Bayesian accounts lack.
  At a critical complexity the best model encodes a halting-problem prefix
  (Theorem VIII.4(iii)), so the ideal Occam term is not something any
  procedure evaluates.
- **[THEORY-036](../theory.d/THEORY-036.md) (Dennett's real patterns).** Dennett's criterion,
  "a description more efficient than the bit map", is K(x) < |x|. This
  paper separates the model part of such a description from the noise
  part, and shows a string can be compressible and still have no simple
  model (non-stochastic strings, §V-E). The paper does not cite Dennett,
  and the link is this reading's. [THEORY-036](../theory.d/THEORY-036.md)'s line that no source here
  connects real patterns to minimum description length remains true.
- **[THEORY-087](../theory.d/THEORY-087.md).** No bearing. Its (d/2) log n and λ log n penalties are
  Bayesian expansions for parametric families. This paper's precision is
  O(log n) throughout, the same order as those penalties, so its results
  cannot distinguish them.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Logarithmic slack everywhere.** For the parametric families of
  practice, (k/2) log n is the whole model cost, and it falls inside the
  error terms. The authors make no claim about what survives at practical
  sizes.
- **Uncomputable.** Every guaranteed quantity is defined by Kolmogorov
  complexity. The MDL algorithm of §V-B converges at an unknown time. The
  goodness-of-fit guarantee holds only in the limit.
- **Models are complexity-bounded classes, not statistical families.**
  The authors say so (§IV-D). The Bernoulli example in §V-B(iii) is used
  only to illustrate the worst-case data-to-model code.
- **Small slips.** The typo in Lemma V.2. The arXiv footnote gives the
  conference as the "47th" FOCS; FOCS 2002 was the 43rd ([LIT-239](../literature.d/LIT-239.md) flags
  this). The open question at the end of App. D (an upper semicomputable
  f_x with β_x = E(f_x)) is left open.

## Open questions

- Is there a non-increasing upper semicomputable f_x with β_x = E(f_x) to
  O(log |x|), or even o(|x|)? (The paper's own open question, App. D.)
- How much of Theorem IV.8 survives for a restricted, statistically
  natural class, for instance k-parameter exponential families at
  precision (k/2) log n? Rissanen (2002) and the later Vereshchagin–Shen
  treatments are where to look.
- How many strings of a given length and complexity are non-stochastic
  at a given level? The shape results give existence, not frequency.
