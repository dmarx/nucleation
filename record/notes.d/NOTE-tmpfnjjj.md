---
status: Read
paper: LIT-tmp08fvg
title: 'Alon & Klartag — optimal compression of approximate inner products'
version: 1
history:
- version: 1
  date: '2026-10-16'
  note: >-
    Read in full from the arXiv PDF, 1610.00239v4 of 2 April 2017 (29 PDF
    pages, numbered 1–28; category math.MG), supplied by the owner and
    extracted with pdftotext -layout: abstract, §1 with §§1.1–1.3, §2, §§3–5,
    §6 with §§6.1–6.4, §7 and the acknowledgment. Pages 1, 2, 4, 5, 8, 9
    and 13 were rendered as images where formulas were garbled, and every
    statement quoted below was checked against them. The proofs of §§3–5 and
    §6.1 were followed step by step; the convex-geometry proofs of §§6.3–6.4
    (finite volume ratio, low M*-estimate) were read in outline, taking the
    cited theorems of Artstein-Avidan, Giannopoulos and Milman as given. The
    reference list was scanned. The copy does not state the FOCS venue.
date: '2026-10-16'
summary: >-
  Storing every inner product and squared distance of n points of norm at
  most 1 in R^k to additive error ε takes Θ(n log n/ε²) bits once
  k ≥ log n/ε², Θ(nk log(2 + log n/(ε²k))) for log n ≤ k ≤ log n/ε², and
  Θ(nk log(1/ε)) below, for 1/n^0.49 ≤ ε ≤ 0.1. Comparing these counts
  across dimensions shows that some n points in R^k cannot be mapped into
  fewer than Ω(min{k, log(2 + ε²n)/ε²}) dimensions with additive error ε,
  for every ε ≥ 2/√n. A bipartite version of the Johnson–Lindenstrauss
  lemma reaches O(log(2 + ε²n)/ε²) dimensions; the one-family version at
  that size is left open.
---

# NOTE-tmpfnjjj: Alon & Klartag — optimal compression of approximate inner products

## Contribution

The paper asks how many bits it takes to store n points of the unit ball
of R^k so that every inner product and squared distance can be read back to
within an additive ε. Before it, the answer was known up to a constant only
for k ≥ log n/ε², from Kushilevitz, Ostrovsky and Rabani with Larsen and
Nelson's lower bound. It gives the answer for every k when
1/n^0.49 ≤ ε ≤ 0.1, and for k up to t = log(2 + ε²n)/ε² when ε ≥ 2/√n.
Because a low-dimensional embedding is itself a sketch, the bit counts
give a second proof of Larsen and Nelson's lower bound, and extend it to
every ε ≥ 2/√n with log(2 + ε²n) in place of log n. It also proves a
bipartite Johnson–Lindenstrauss lemma in that smaller dimension.

## Key insight

The bit count of a sketch is the log of the number of point
configurations that the tolerance can tell apart. That number can be
bounded from above by a volume argument: put a random point near each
stored point, and the chance that all inner products land within ε is at
least c^{nk}, so at most c^{−nk} configurations can be ε-separated. It can
be bounded from below by a packing: n/2 fixed random probe points
distinguish every choice of the other n/2 points from a δ-separated net.
A map into ℓ dimensions with error ε is a sketch with ℓ dimensions' worth
of bits per point, so a dimension too small for the bit count is ruled out.
For small ε the union bound over n² pairs is the wasteful step. The paper
replaces it with the Gaussian correlation inequality (Khatri–Šidák, Hargé),
which multiplies the n slab probabilities instead of adding failures. That
needs only n·e^{−ε²t/2} ≲ t, not ≲ 1/n², and this is where log(2 + ε²n)
replaces log n.

## Assumptions

- **Additive error, bounded points.** X is n points of norm at most 1 in
  R^k, with n ≥ k ≥ 1. An ε-distance sketch recovers, for any two points,
  their squared Euclidean distance and their inner product up to an
  additive ε (§1.1; the abstract names only the squared distance).
  f(n, k, ε) is the least number of bits of such a sketch.
- **Dimension reduction is also additive.** An (n, k, ℓ, ε)-Euclidean
  dimension reduction exists if for any x₁ … x_n ∈ R^k of norm at most 1
  there are y₁ … y_n ∈ R^ℓ with |x_i − x_j|² − ε ≤ |y_i − y_j|² ≤
  |x_i − x_j|² + ε for all i, j (condition (1), §2). The y_i may depend
  on the whole set, so the maps are arbitrary. The relative form,
  (1 − ε)|x_i − x_j|² ≤ |y_i − y_j|² ≤ (1 + ε)|x_i − x_j|² (condition
  (2)), is stated only in Corollary 2.1.
- **Ranges of ε.** Theorem 1.1 and Corollary 2.1 need 1/n^0.49 ≤ ε ≤ 0.1.
  Theorem 2.2, Corollary 2.3 and Theorem 6.1 need ε ≥ 2/√n.
- **Worst case, by existence.** Lower bounds are for some point set; upper
  bounds are for every set.
- **Constants are not tracked.** "Throughout the proofs we make no serious
  attempt to optimize the absolute constants involved." Logarithms are
  natural unless stated.

## Key results

- **Theorem 1.1 (bits, ε ≥ 1/n^0.49).** For all n and
  1/n^0.49 ≤ ε ≤ 0.1:
  - for log n/ε² ≤ k ≤ n, f(n, k, ε) = Θ(n log n/ε²);
  - for log n ≤ k ≤ log n/ε², f(n, k, ε) = Θ(nk log(2 + log n/(ε²k)));
  - for 1 ≤ k ≤ log n, f(n, k, ε) = Θ(nk log(1/ε)).
  Upper bounds are Lemmas 3.1–3.3; lower bounds are Lemma 5.1 and the
  argument after it.
- **Lemma 3.1 (the volume argument).** After a JL map into
  m = C log n/ε² dimensions, the ε-separated Gram matrices of n vectors of
  norm at most 2 number at most 2·3^{nm}: n points uniform in the radius-3
  ball each land within 1 of their target with probability (1/3)^m, and
  then all off-diagonal inner products are within ε/2 with probability
  above 1/2. Norms are stored apart in O(log(1/ε)) bits each.
- **Theorem 4.1 (an algorithm).** A randomized algorithm gives each point
  a sketch of g(n, k, ε) bits, Θ(log n/ε²) in the top range: a fast JL
  map into m = 40 log n/ε² dimensions, then each coordinate rounded at
  random to a neighbouring multiple of 1/√m with the right mean. Hoeffding
  bounds each error by 2e^{−ε²m/8} < 1/n⁵; all inner products are within ε
  with probability at least 1 − 2/n³. Recovery takes O(log n/ε²) time, or
  O(k) for smaller k. Sketch length is optimal up to a constant in every
  range (end of §5). The top range also follows from Kushilevitz, Ostrovsky
  and Rabani.
- **Lemma 5.1 (the lower bound).** If k = δ² log n/(200ε²) with
  2ε ≤ δ ≤ 1/2, then f(n, k, ε/2) ≥ Ω(kn log(1/δ)). The hard sets are a
  fixed set R of n/2 points in B^k, chosen at random, plus any ordered n/2
  points of a δ-separated net N of size (1/δ)^{(1+o(1))k}. R is chosen so
  that every two net points differ by more than ε in their inner product
  with some point of R; so every choice gives a different sketch, and the
  count is log |N|^{n/2}. For k ≤ log n the net is 2ε-separated, giving
  Ω(nk log(1/ε)).
- **Corollary 2.1 (dimension, ε ≥ 1/n^0.49).** There is c > 0 such that
  for any n ≥ k > ck ≥ ℓ (as printed) and 1/n^0.49 ≤ ε ≤ 0.1 there is an
  (n, k, ℓ, ε)-Euclidean dimension reduction if and only if
  ℓ = Ω(log n/ε²). "Moreover, the same holds" with the relative
  condition (2). The paper glosses it: if k ≥ c₁ log n/ε², JL reduces to
  ε⁻² log n; any reduction with ℓ = o(k) has k ≥ ℓ ≥ c₂ε⁻² log n. §7 says
  the first part follows from Theorem 1.1 by comparing f(n, n, 2ε) with
  f(n, k, ε), and the relative part by combining JL with Theorem 1.1's
  lower bound. That derivation is sketched in a few lines, not written
  out.
- **Theorem 2.2 (bits, ε ≥ 2/√n).** With t = log(2 + ε²n)/ε²:
  - for t ≤ k ≤ n, Ω(nt) ≤ f(n, k, ε) ≤ O(n log n/ε²), a gap the paper
    calls "probably not tight" on the upper side;
  - for log(2 + ε²n) ≤ k ≤ t, f(n, k, ε) = Θ(nk log(2 + t/k));
  - for 1 ≤ k ≤ log(2 + ε²n), f(n, k, ε) = Θ(nk log(1/ε)).
  The middle upper bound replaces Lemma 3.1's union bound with Lemma 6.2.
- **Lemma 6.2.** For symmetric slabs H₁ … H_n ⊆ R^k,
  Vol(B^k ∩ ⋂H_i)/Vol(B^k) ≥ c^k ∏ γ_k(√k H_i), by Hargé's inequality
  (a case of the Gaussian correlation inequality, proved by Royen) and
  the Khatri–Šidák lemma.
- **Corollary 2.3 (dimension, ε ≥ 2/√n).** There is c > 0 such that for
  any n ≥ k > ck ≥ ℓ and all ε ≥ 2/√n, if there is an
  (n, k, ℓ, ε)-Euclidean dimension reduction then
  ℓ = Ω(log(2 + ε²n)/ε²). Stated for the additive condition (1) only. The
  abstract's form: for k ≤ t there are n points in R^k that cannot be
  embedded in R^ℓ for ℓ < ck "without distorting some inner products (and
  distances) by more than ε". §1.2's form: no reduction below t for any
  n ≥ k ≥ t and ε > 2/√n, and "for any smaller value of ε, or for any
  k < t no reduction by more than a constant factor is possible". The
  intro says this "extends the main result of [17], where the above is
  proved only for ε ≥ log^0.5001 n/√k".
- **Theorem 1.2 (bipartite JL).** There is C such that for any
  a₁ … a_n, b₁ … b_n ∈ R^n of norm at most 1, any 0 < ε < 1 and
  t = ⌊C log(2 + ε²n)/ε²⌋, there are x₁ … x_n, y₁ … y_n ∈ R^t with
  |⟨x_i, y_j⟩ − ⟨a_i, b_j⟩| ≤ ε for all i, j. A randomized polynomial-time
  algorithm finds them: a random rotation U, x_i by linear programming
  so that Ux_i lies in a random t-dimensional subspace and in √t a_i + CK,
  and y_j from the first t coordinates of U⁻¹b_j. The statement puts no
  bound on the norms of x_i and y_j.
- **Conjecture 2.4.** Theorem 1.2 holds with ‖x_i‖, ‖y_i‖ ≤ O(1). It is
  trivial for ε < √(C/(2n)) and holds by JL for ε > 1/n^0.49. With the
  paper's methods it would close the first bullet of Theorem 2.2.
- **Theorem 2.5 (= Theorem 6.3, halving).** For m ≥ n ≥ 1 and
  a₁ … a_m, b₁ … b_m ∈ R^{2n} of norm at most 1, independent standard
  Gaussian X_i, Y_i ∈ R^n scaled by 1/√n satisfy
  |⟨X̄_i, Ȳ_j⟩ − ⟨a_i, b_j⟩| ≤ ε for all i, j and |X̄_i| + |Ȳ_i| ≤ C₃ with
  probability at least exp(−C₂nm), when n ≥ C₁ log(2 + ε²m)/ε². This is
  Conjecture 2.4 when t = Θ(n), that is ε = Θ(1/√n). §7: it is tight for
  m = 2n and ε = C/√n even for an orthonormal basis, since a 2n × 2n
  matrix within 1/(2√n) of the identity in every entry has rank above n
  (Alon 2009).
- **Theorem 6.1 (inner products with one vector).** For a₁ … a_n of norm
  at most 1 in R^k, ε ≥ 2/√n and log(2 + ε²n)/(8ε²) ≤ k ≤ n, the bits
  needed to store all ⟨a_i, y⟩ to ε, over y of norm at most 1, are
  Θ(log(2 + ε²n)/ε²). The upper bound is proved for every a_i, the lower
  bound for a random choice of a_i. The key step: with t solving
  ε = √(2 log(2 + n/t))/√t, Khatri–Šidák gives γ_n(K) ≥
  (1 − 2e^{−ε²t/2})^n ≥ e^{−3t}.
- **Theorems 6.7, 6.8 and Corollary 6.9.** The low M*-estimate, with its
  hypothesis γ_n(K) ≥ 1/2 weakened to γ_n(K) ≥ exp(−c₀t). The Remark
  recovers Garnaev and Gluskin's bound for a cube and says their
  tightness makes exp(−c₀ℓ) optimal.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | f(n, k, ε) is determined up to a constant for all n ≥ k ≥ 1 and 1/n^0.49 ≤ ε ≤ 0.1 | strong | Theorem 1.1; Lemmas 3.1–3.3, 5.1, complete proofs |
| C2 | Optimal-length per-point sketches can be computed efficiently and decoded in time linear in their length | strong | Theorem 4.1, §4 |
| C3 | No reduction of n points in R^k into ℓ ≤ ck dimensions keeps squared distances to additive ε unless ℓ = Ω(log(2 + ε²n)/ε²), for ε ≥ 2/√n | strong, with a sketched last step | Corollary 2.3 from Theorem 2.2; derivation given in a short remark in §7 |
| C4 | For 1/n^0.49 ≤ ε ≤ 0.1 the same holds with log n, and also for the relative condition (2) | strong, with a sketched last step | Corollary 2.1; §7 |
| C5 | Two families of n vectors can be mapped into O(log(2 + ε²n)/ε²) dimensions keeping cross inner products to additive ε | strong | Theorem 1.2, §6.4, resting on cited convex-geometry theorems |
| C6 | The same with O(1) norms (Conjecture 2.4) | conjecture | proved only for t = Θ(n), Theorem 2.5 |
| C7 | The relative-error sketch problem is harder; the lower bounds hold for it and a log gap remains | moderate | §7, citing Indyk and Wagner |

## Method

1. **Upper bounds by volume (§3, §6.2).** Take a maximal ε-separated set
   G of Gram matrices. Place independent uniform random points in a
   slightly larger ball. Each event "the random Gram matrix is within ε/2
   of G off the diagonal" has probability at least c^{nk}, and these events
   are disjoint, so |G| ≤ c^{−nk}. For small ε, condition point by point
   and bound each conditional probability by Lemma 6.2 instead of a union
   bound.
2. **Upper bound by rounding (§4).** JL, then unbiased randomized rounding
   of each coordinate to a grid of step 1/√m (or δ/√k), plus O(log(1/ε))
   bits for each norm. Self-inner products of rounded vectors are not
   close to norms, which is why norms are stored apart (§7).
3. **Lower bounds by packing (§5, §6.1–6.2).** Fix n/2 random probe
   points that separate every pair of net points by more than ε in some
   inner product; count ordered choices of n/2 net points.
4. **Dimension from bits (§7).** A map into ℓ dimensions with error ε
   yields a sketch of f(n, ℓ, ε) bits for the original set. Since f grows
   with k by more than a constant factor below t, ℓ must be Ω(min{k, t}).
5. **Bipartite reduction (§6.3–6.4).** The convex body K of x with
   |⟨x/√t, b_j⟩| ≤ c₀ε for all j has Gaussian measure at least e^{−c₀t}
   by Khatri–Šidák. By the weakened low M*-estimate a random
   t-dimensional subspace E meets v + CK for every |v| ≤ √t. Choose x_i in
   E with Ux_i − √t a_i ∈ CK, and let y_j be the scaled projection of
   U⁻¹b_j.

## Concepts

- **ε-distance sketch.** A data structure from which any pair's squared
  distance and inner product are recovered to additive ε.
- **ε-separated Gram matrices.** Two Gram matrices that differ by more
  than ε in some off-diagonal entry.
- **(n, k, ℓ, ε)-Euclidean dimension reduction.** Every n points of norm
  at most 1 in R^k have images in R^ℓ with squared distances within
  additive ε (condition (1)).
- **t = log(2 + ε²n)/ε².** The paper's dimension scale for small ε. It is
  Θ(log n/ε²) when ε ≥ 1/n^0.49, and about n when ε is near 2/√n.
- **γ₂-norm.** The least, over factorizations A = XY, of the largest row
  norm of X times the largest column norm of Y. §7 restates Theorem 1.2
  for ε = O(1/√n) as: γ₂(A) ≤ 1 implies an entrywise O(1/√n)
  approximation of rank at most n/10. A bound on max |A_ij| does not
  suffice: a Hadamard matrix's approximants have rank n − O(1).

## Connections

It builds on Larsen and Nelson ([LIT-tmp8s1wj](../literature.d/LIT-tmp8s1wj.md), read in [NOTE-tmp4mti8](NOTE-tmp4mti8.md)),
cited from the 2016 arXiv version, and on a private communication from
them asking whether log n could be replaced by log(2 + ε²n) in the JL
lemma. It uses the Johnson–Lindenstrauss lemma ([LIT-tmp7skui](../literature.d/LIT-tmp7skui.md)) and the
fast JL transform of Ailon and Chazelle as tools, and credits the top
range of its sketch to Kushilevitz, Ostrovsky and Rabani. The relative
error problem is left to Indyk and Wagner. The small-ε results rest on
the Khatri–Šidák lemma, Hargé's inequality and Royen's proof of the
Gaussian correlation conjecture, the finite volume ratio theorem of Szarek
and Tomczak-Jaegermann, and the low M*-estimate of Pajor and
Tomczak-Jaegermann. Its Remark recovers Garnaev and Gluskin's widths of
the Euclidean ball, the same result Baraniuk et al. ([LIT-tmpcfdvm](../literature.d/LIT-tmpcfdvm.md)) cite for
necessity of k log(N/k) in compressed sensing (my observation, from
[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md)). It names compressed sensing only as an application
of sketching.

## Bearing on the record

- **[THEORY-tmpfo89o](../theory.d/THEORY-tmpfo89o.md) (Larsen–Nelson optimality).**
  - *The range of ε.* Corollary 2.3 replaces Theorem 2's
    lg^0.5001 n/√min{n, d} < ε < 1 with ε ≥ 2/√n, and lg(ε²n) with
    log(2 + ε²n). Below 2/√n, §1.2 says no reduction by more than a
    constant factor is possible; that follows from the case ε = 2/√n,
    where t is of order n (my observation). So the lower bound
    Ω(min{k, log(2 + ε²n)/ε²}) holds across the whole range, up to an
    unstated constant, for a worst-case set.
  - *Additive against relative.* Corollary 2.3 is stated for additive
    error on squared distances of points of norm at most 1. The relative
    form (2) is stated only in Corollary 2.1, for 1/n^0.49 ≤ ε ≤ 0.1. For
    lower bounds the additive form is the stronger one: on points of norm
    at most 1, condition (2) implies condition (1) with 4ε, since
    |x_i − x_j|² ≤ 4. So the relative lower bound, Conjecture 1's lower
    half, follows for ε ≥ 2/√n with the constant changed (my
    observation; the paper does not state it). The converse fails, as
    Larsen and Nelson note: additive error says nothing relative about
    small distances.
  - *What is still open.* The upper half of Conjecture 1, a one-family
    embedding into O(log(2 + ε²n)/ε²) dimensions, is not proved. Only the
    bipartite Theorem 1.2 is, for cross inner products, additive, with no
    control of norms. [THEORY-tmpfo89o](../theory.d/THEORY-tmpfo89o.md)'s "Anything for small ε" should say
    the lower bound is now known there and the upper bound is not.
  - *[THEORY-tmpfo89o](../theory.d/THEORY-tmpfo89o.md)'s report of this paper* ("proved the lower bound of
    its Conjecture 1 … for all parameters") is right in substance, with
    three qualifications: the stated range is ε ≥ 2/√n, smaller ε being
    the trivial case; the statement is additive; and the step from bits
    to dimension is a short remark in §7.
  - *A second proof of Theorem 2.* Corollary 2.1, for
    1/n^0.49 ≤ ε ≤ 0.1. Its range is the abstract form of Larsen and
    Nelson's, not their sharper lg^0.5001 n/√min{n, d}, and it stops at
    ε = 0.1 rather than 1, which matters only for constants. The hard set
    is different: n/2 random probe points plus n/2 points of a
    δ-separated net, not basis vectors with k-sparse vectors. Both are
    encoding arguments that read a point's identity off its inner products
    with fixed probes (my observation).
  - Filed as [THEORY-tmpup7x5](../theory.d/THEORY-tmpup7x5.md) (the bit counts and the lower bound) and
    [THEORY-tmpbh0v2](../theory.d/THEORY-tmpbh0v2.md) (the bipartite reduction).
- **[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), distances.**
  - *The shape.* The bit count is literally the log of a family's size:
    f(n, k, ε) is log₂ of the number of ε-separated Gram matrices. The
    dimension is that count per point, divided by the O(1) bits per
    coordinate that randomized rounding needs (Theorem 4.1). In the large-ε
    range this is the question's shape, log n over ε².
  - *But the family is not the pairs.* For small ε the threshold is
    log(2 + ε²n)/ε², not log(n²)/ε². In Theorem 6.1 and Lemma 6.2 the
    union bound over pairs is replaced by a product of slab probabilities,
    which needs only n·e^{−ε²t/2} ≲ t. So "log of the family size over a
    squared tolerance" survives in form, but the log counts 2 + ε²n, not
    the n² pairs a union bound counts (my observation). The question's
    sentence that the bound is tight should be widened from "for ε above
    about 1/√min{n, d}" to every ε ≥ 2/√n for the lower bound, with the
    upper bound at log(2 + ε²n) still open for one family.
- **[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), superposition.**
  - The paper says nothing directly about incoherent or nearly orthogonal
    sets. Its hard set is not nearly orthogonal.
  - §7's tightness remark is about them: a 2n × 2n matrix within 1/(2√n)
    of the identity in each entry has rank above n. That is a lower bound
    on the dimension of n nearly orthogonal directions at ε of order
    1/√n.
  - My observation: Theorem 1.2 with a_i = b_i = e_i gives n pairs
    (x_i, y_i) in O(log(2 + ε²n)/ε²) dimensions with ⟨x_i, y_i⟩ within ε
    of 1 and |⟨x_i, y_j⟩| ≤ ε for i ≠ j. That is a nearly orthogonal
    system with separate write and read vectors, below the log n/ε² order
    for small ε. It is not a set of unit vectors, since norms are not
    controlled, so it does not bound superposition as [NOTE-278](NOTE-278.md) defines it.
    Whether a model with untied encoder and decoder could use this is a
    question, not a finding.
- **[QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), random features and expand-and-threshold.**
  Nothing. The γ₂ remark, that entrywise low-rank approximation depends on
  the γ₂-norm and not on the largest entry, is about what entrywise
  closeness of Gram matrices allows; the question's random-features thread
  asks about entrywise against spectral convergence ([LIT-679](../literature.d/LIT-679.md)), and the
  paper does not touch spectral norms.
- **Checks of the current LIT against the text.**
  - Summary, "Determines the number of bits needed to store inner products
    of n points to additive error ε": correct for points of norm at most 1
    in R^k and 1/n^0.49 ≤ ε ≤ 0.1. For 2/√n ≤ ε < 1/n^0.49 it is
    determined only for k ≤ t; for k ≥ t a gap Ω(nt) to O(n log n/ε²)
    remains (Theorem 2.2). The sketch also returns squared distances.
  - Summary and takeaway, "proves the lower bound of their Conjecture 1
    for all parameters", "Θ(min{n, d, ε⁻² lg(2 + ε²n)})": the lower bound
    only, in additive form, for ε ≥ 2/√n, as above.
  - `extends: LIT-tmp8s1wj`: correct. The paper says it "extends the main
    result of [17]".
  - Bibliography. The copy is v4 of 2 April 2017, math.MG. It does not
    name FOCS, so the venue, DOI and pages could not be checked against
    it. `published:` 2016-10-02 (v1) is not contradicted.
- **Checks of [NOTE-tmp4mti8](NOTE-tmp4mti8.md) §1.2's report.** "An alternative proof through
  the space complexity of storing approximate inner products": correct
  (Corollary 2.1, for 1/n^0.49 ≤ ε ≤ 0.1). "Prove the lower bound of
  Conjecture 1 for all parameters (removing the lg^0.5001 n condition)":
  correct with the three qualifications above. "A bipartite version of its
  upper bound with m = O(ε⁻² lg(2 + ε²n))": correct (Theorem 1.2), for
  cross inner products ⟨x_i, y_j⟩ to additive ε, with norms unbounded;
  bounded norms are Conjecture 2.4. It is not an embedding of one set and
  gives no distances.
- **For the anthology.** No instruction for machine-learning practice.

## Limitations

- Constants are unspecified throughout, and Corollaries 2.1 and 2.3 are
  derived in a few lines of §7.
- For 2/√n ≤ ε < 1/n^0.49 and k ≥ t the bit count is not settled.
- The dimension lower bound is stated for additive error; the relative
  form for small ε is left to the reader.
- The bipartite reduction does not control norms, keeps only cross inner
  products, and is not a JL lemma for one set.
- Theorem 2.5 holds with probability exp(−C₂nm), positive but tiny, so it
  is an existence proof, not an algorithm.
- Corollary 2.1's hypothesis "n ≥ k > ck ≥ ℓ" is printed so, and its
  "if and only if ℓ = Ω(log n/ε²)" is loose on the "if" side; the gloss
  after it gives the intended reading.
- The §§6.3–6.4 proofs rest on cited theorems of asymptotic convex
  geometry, read here in outline.

## Open questions

- Conjecture 2.4: bounded norms in the bipartite reduction. The paper
  notes that iterating Theorem 2.5 fails because norms grow.
- Whether the one-family JL lemma improves to O(log(2 + ε²n)/ε²), as
  Larsen and Nelson asked. The paper says its results "are the first to
  suggest that such an improvement may indeed hold".
- The relative-error sketch problem, with a log gap left (Indyk and
  Wagner).
- For the record (my question): whether the product-of-slabs step, which
  turns log n into log(2 + ε²n), has a counterpart in the sparse-recovery
  bound, where the union is over supports.
