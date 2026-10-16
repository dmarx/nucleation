---
number: 931
status: Read
formerly:
- NOTE-tmppltl7
paper: LIT-1156
title: 'Baraniuk, Davenport, DeVore & Wakin — a simple proof of the restricted isometry property'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the author-posted copy on Mark Davenport's Georgia
    Tech page, mdav.ece.gatech.edu/publications/bddw-ca-2008.pdf (11
    pages, the Constructive Approximation typeset version with the DOI
    10.1007/s00365-007-9003-x header, received 17 May 2006, revised 18
    January 2007, accepted 5 February 2007, © 2008), extracted with
    pdftotext -layout: abstract, §§1–6, acknowledgements and the 19
    references. There are no appendices. The displayed equations garbled
    in extraction ((2.1), (2.3), (3.6), (3.8), (4.3)–(4.6), §5 in full)
    were read from renderings of PDF pp. 3–4 and 7–9. (3.9) was
    reconstructed from the extracted text alone. The proofs of Lemma 5.1
    and Theorem 5.2 were checked line by line. The results the paper only
    recalls (Kashin, Garnaev–Gluskin, Candès–Tao's (3.9), Achlioptas's
    constants) were read as stated, not checked against their sources.
date: '2026-10-14'
summary: >-
  If an n × N random matrix satisfies the concentration inequality used in
  JL proofs, Pr(|‖Φx‖² − ‖x‖²| ≥ ε‖x‖²) ≤ 2e^{−n c₀(ε)}, then a union bound
  over a (12/δ)^k-point net on each of the C(N, k) ≤ (eN/k)^k coordinate
  k-subspaces, with a short bootstrapping step from net to subspace, gives
  the restricted isometry property for all k ≤ c₁n/log(N/k) with
  probability at least 1 − 2e^{−c₂n} (Theorem 5.2). Gaussian, ±1 and
  Achlioptas's sparse ensembles qualify with c₀(ε) = ε²/4 − ε³/6, and the
  same argument gives the property in any fixed orthonormal basis.
---

# NOTE-931: Baraniuk, Davenport, DeVore & Wakin — a simple proof of the restricted isometry property

## Contribution

The paper proves the restricted isometry property (RIP) for random matrices
from two ingredients only: the concentration inequality for ‖Φx‖² that
simplified proofs of the Johnson–Lindenstrauss lemma use, and covering
numbers for balls in R^k. Any distribution satisfying that inequality gives
RIP matrices in the range k ≤ c₁n/log(N/k), which the paper says is the
widest range possible up to constants. The same argument shows that the ±1
and sparse ensembles keep the property after any fixed orthonormal change
of basis, which the authors say had not been shown before.

## Key insight

RIP is a statement about every vector in a union of C(N, k) k-dimensional
subspaces. Replace each subspace's unit sphere by a finite net, apply the
one-vector tail bound to every net point, and pay for the union bound with
the log of the number of points: k log(eN/k) for the supports plus
k log(12/δ) for the net. The tail is e^{−n c₀}, so n of order that log over
c₀ suffices. The JL lemma is the same move with the point pairs of a finite
set as the family. The paper's §6 puts it this way: the RIP "can be thought
of as a straightforward consequence of the JL lemma".

## Assumptions

- **Notation.** Φ is n × N, with n measurements and ambient dimension N.
  The record's other notes write m for measurements and n for the ambient
  dimension. Below, the paper's letters are kept.
- **Concentration (4.3).** For every fixed x ∈ R^N,
  Pr(|‖Φ(ω)x‖²_{ℓ₂ⁿ} − ‖x‖²_{ℓ₂ᴺ}| ≥ ε‖x‖²_{ℓ₂ᴺ}) ≤ 2e^{−n c₀(ε)}
  for 0 < ε < 1, with c₀(ε) > 0 depending only on ε. This is the only
  property of the distribution Lemma 5.1 and Theorem 5.2 use.
- **Ensembles that satisfy it (§4).** Entries i.i.d. as
  - (4.4) Gaussian, φᵢⱼ ∼ N(0, 1/n);
  - (4.5) ±1/√n with probability 1/2 each;
  - (4.6) +√(3/n) with probability 1/6, 0 with probability 2/3,
    −√(3/n) with probability 1/6.

  All three with c₀(ε) = ε²/4 − ε³/6. For (4.5) and (4.6) the paper says
  this "is proved in [1]" (Achlioptas). For (4.4) it calls the verification
  "elementary using Chernoff inequalities and a comparison of the moments
  of a Bernouli random variable to those of a Gaussian random variable".
- **RIP (3.8), after Candès and Tao.** Φ has the RIP of order k if there
  is δₖ ∈ (0, 1) with (1 − δₖ)‖x_T‖²_{ℓ₂ᴺ} ≤ ‖Φ_T x_T‖²_{ℓ₂ⁿ} ≤
  (1 + δₖ)‖x_T‖²_{ℓ₂ᴺ} for all T with #T ≤ k. Equivalently, every Gram
  matrix Φ_TᵗΦ_T has its eigenvalues in [1 − δₖ, 1 + δₖ].
- **Covering.** A δ/4-net Q_T of the unit sphere of X_T with
  #(Q_T) ≤ (12/δ)^k exists. The paper cites Chap. 13 of Lorentz, von
  Golitschek and Makovoz for this and does not prove it.

## Key results

- **Kashin, Garnaev–Gluskin (2.3), recalled.** For some C₀ > 0 and all
  0 < n < N, C₀⁻¹ √((log(N/n) + 1)/n) ≤ dⁿ(U(ℓ₁ᴺ))_{ℓ₂ᴺ} ≤
  C₀ √((log(N/n) + 1)/n), for the Gelfand width (2.2). Kashin proved the
  upper bound with a worse log exponent, using 0/1 Bernoulli matrices;
  Garnaev and Gluskin gave the lower bound and the exponent, using Gaussian
  matrices.
- **Widths and optimal CS (3.5), (3.6), recalled.** If K = −K and
  K + K ⊂ C₁K, then dⁿ(K)_X ≤ E_{n,N}(K)_X ≤ C₁dⁿ(K)_X for 1 ≤ n ≤ N. For
  the ℓ₁ ball, C₁ = 2, so the best CS error on U(ℓ₁ᴺ) in ℓ₂ is between
  C₀⁻¹ and 2C₀ times √((log(N/n) + 1)/n).
- **Candès–Tao (3.9), recalled.** If Φ has the RIP of order 3k with
  δ₃ₖ < 1, then ℓ₁ minimization (3.7) gives ‖x − Δ(Φx)‖_{ℓ₂ᴺ} ≤
  C₂σₖ(x)_{ℓ₁ᴺ}/√k, with C₂ depending only on δ₃ₖ and σₖ the ℓ₁ error of
  best k-term approximation. So RIP for k of order n/(log(N/n) + 1)
  attains (3.6). Combined with the lower bound in (2.3), "the widest range
  possible is k ≤ C₃n/(log(N/n) + 1)" for fixed δₖ.
- **Lemma 5.1.** If Φ satisfies (4.3), then for any T with #(T) = k < n
  and any 0 < δ < 1, (1 − δ)‖x‖_{ℓ₂ᴺ} ≤ ‖Φx‖_{ℓ₂ⁿ} ≤ (1 + δ)‖x‖_{ℓ₂ᴺ}
  for all x ∈ X_T (5.1), with probability ≥ 1 − 2(12/δ)^k e^{−c₀(δ/2)n}
  (5.2). Proof: (4.3) with ε = δ/2 on every net point gives (5.4); square
  roots give (5.5). Let A be the least number with ‖Φx‖ ≤ (1 + A)‖x‖ on
  X_T (5.6). For a unit x and its net point q, ‖Φx‖ ≤ 1 + δ/2 + (1 + A)δ/4
  (5.7), so A ≤ (3δ/4)/(1 − δ/4) ≤ δ. The lower side follows from
  ‖Φx‖ ≥ 1 − δ/2 − (1 + δ)δ/4 ≥ 1 − δ (5.8). I checked both final
  inequalities; each holds for δ ≤ 1.
- **Theorem 5.2.** Given n, N and 0 < δ < 1, if the distribution
  satisfies (4.3), there are c₁, c₂ > 0 depending only on δ such that the
  RIP (3.8) holds for Φ(ω) with the prescribed δ and any
  k ≤ c₁n/log(N/k), with probability ≥ 1 − 2e^{−c₂n}. Proof: with
  C(N, k) ≤ (eN/k)^k subspaces, the failure probability is at most
  2(eN/k)^k(12/δ)^k e^{−c₀(δ/2)n} = 2e^{−c₀(δ/2)n + k[log(eN/k) +
  log(12/δ)]} (5.10). The exponent is ≤ −c₂n provided c₂ ≤ c₀(δ/2) −
  c₁[1 + (1 + log(12/δ))/log(N/k)], so c₁ small enough makes c₂ > 0.
- **Range restated.** Validity for k ≤ c₁n/log(N/k) implies validity for
  k ≤ c₁′n/[log(N/n) + 1], with c₁′ > 0 depending only on c₁ (stated, not
  proved).
- **The route through JL (§6).** Adding the origin to Q_T and applying the
  JL lemma instead of (4.3) gives "a similar result with only slightly
  worse constants". Hence "any distribution that yields a satisfactory
  JL-embedding will also generate matrices satisfying the RIP".
- **Universality (§6).** For a fixed orthonormal basis Ψ, taking the nets
  in the spans of k columns of Ψ gives the RIP for Φ(ω)Ψ for (4.4)–(4.6).
  The authors say this was known for the Gaussian by symmetry but not, to
  their knowledge, for (4.5) and (4.6). With high probability one Φ has the
  RIP "with respect to an exponential number of fixed bases" (no count or
  proof is given).
- **Cost (§6).** (4.6) "requires 2/3 fewer additions and multiplies" than
  (4.5) or (4.4).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Any distribution satisfying (4.3) gives Φ with RIP of order k ≤ c₁n/log(N/k), probability ≥ 1 − 2e^{−c₂n} | strong | Theorem 5.2, Lemma 5.1; proof checked, constants c₁, c₂ implicit in δ |
| C2 | Gaussian, ±1 and the three-point sparse ensemble satisfy (4.3) with c₀(ε) = ε²/4 − ε³/6 | strong (cited) | §4, attributed to Achlioptas [1]; not proved here |
| C3 | The range k ≲ n/(log(N/n) + 1) is the widest possible | strong (cited) | lower bound of (2.3) with (3.9), Garnaev–Gluskin and Candès–Tao; not proved here |
| C4 | The RIP is a straightforward consequence of the JL lemma; any JL distribution gives RIP matrices | moderate | §6, informal: the origin added to Q_T, "slightly worse constants", not written out |
| C5 | The ±1 and sparse ensembles have RIP in any fixed orthonormal basis, newly shown | moderate | §6, one-sentence argument; novelty "to our knowledge" |
| C6 | One draw has the RIP simultaneously for an exponential number of fixed bases | weak | §6, asserted, with no count |
| C7 | The approach gives simple proofs of Kashin's and Gluskin's width theorems | weak | abstract; only the upper bound follows, via (3.5), (3.9) and Theorem 5.2, and the paper does not write it out |

## Method

1. Fix a support T, #T = k, and the k-dimensional space X_T.
2. Take a δ/4-net Q_T of its unit sphere, #(Q_T) ≤ (12/δ)^k.
3. Apply (4.3) with ε = δ/2 to every net point; union bound (5.2).
4. Bootstrap from net to sphere by the least-constant argument (5.6)–(5.8).
   The authors stress this step: they "do not begin with a favorable bound
   on the norm of Φ on these finite-dimensional spaces".
5. Union bound over the (eN/k)^k supports (5.10) and solve for k.

## Concepts

- **Restricted Isometry Property (RIP) of order k.** (3.8): near-isometry,
  in squared norms, on every coordinate subspace of dimension ≤ k.
- **X_T.** The vectors of R^N that vanish outside T, with the ℓ₂ norm.
- **Gelfand width dⁿ(K)_X.** inf over subspaces Y of codimension n of
  sup over K ∩ Y of ‖x‖_X (2.2), dual to the Kolmogorov width.
- **E_{n,N}(K)_X.** The minimax error over all encoder–decoder pairs with
  n × N encoders (3.4).
- **Concentration inequality.** (4.3) specifically. The paper calls it a
  "concentration of measure inequality for random inner products".
- **Universality.** RIP for Φ(ω)Ψ for every fixed orthonormal Ψ.

## Connections

The paper sets compressed sensing (Candès, Romberg and Tao; Donoho), the
Kashin and Garnaev–Gluskin widths and the JL lemma side by side. For JL it
cites Johnson and Lindenstrauss ([LIT-1153](../literature.d/LIT-1153.md)) for Lemma 4.1, and Achlioptas
([LIT-1159](../literature.d/LIT-1159.md)), Dasgupta and Gupta ([LIT-1157](../literature.d/LIT-1157.md)), Frankl and Maehara, and
Indyk and Motwani for the simplified proofs. Its constants come from
Achlioptas alone; it uses nothing specific to Dasgupta and Gupta. The
net-and-union-bound strategy it compares to modern proofs of Dvoretzky's
theorem. It does not cite Donoho and Tanner ([LIT-1160](../literature.d/LIT-1160.md)) or
Do Ba, Indyk, Price and Woodruff, and says nothing about phase
transitions or about lower bounds for sparse recovery other than (2.3).

## Bearing on the record

**[QUESTION-120](../questions.d/QUESTION-120.md), the superposition thread.**

- The paper confirms the shape the question proposes, for sufficiency. From
  (5.10), n ≥ k[log(eN/k) + log(12/δ)]/c₀(δ/2), up to the margin c₂, is
  enough, and c₀(δ/2) = δ²/16 − δ³/48. That is the log of the family's
  size over a squared tolerance (my rewriting of (5.10); the paper keeps
  c₁ implicit). The family is the net, not the supports alone. Its log has
  a k log(12/δ) term with no counterpart in the JL count.
- The paper does not show that the threshold counts the same thing in the
  other direction. It attributes optimality of k ≲ n/(log(N/n) + 1) to the
  Garnaev–Gluskin lower bound on Gelfand widths (2.3) with (3.9), which is
  geometry of the ℓ₁ ball, not concentration.
- The bound in [NOTE-278](../notes.d/NOTE-278.md) is a lower bound, m = Ω(k log(n/k)), that takes
  RIP as a hypothesis and goes through Do Ba–Indyk–Price–Woodruff. This
  paper supplies the hypothesis: random matrices meet it once n is of
  order k log(N/k). It does not touch the lower bound's proof. So the
  question's step "the [NOTE-278](NOTE-278.md) bound rewritten as the Baraniuk et al.
  union bound" cannot be done as stated. A union bound gives upper bounds
  on the measurements needed. What can be set side by side is this paper's
  sufficient n and the toy model's necessary m, which agree in order (my
  observation).
- On the open question in [NOTE-930](../notes.d/NOTE-930.md) and [NOTE-925](../notes.d/NOTE-925.md): yes, the three
  steps are the same (one-vector tail, finite family, union bound), with a
  fourth step JL lacks, the bootstrapping from net to subspace.
- On [NOTE-932](../notes.d/NOTE-932.md)'s open point: the exponent used is Achlioptas's,
  c₀(ε) = ε²/4 − ε³/6, not Dasgupta and Gupta's ε²/2 − ε³/3 per side.
  Dasgupta and Gupta are cited only in a list of simplified JL proofs.

**The other two threads.** The paper says nothing about kernels, sample
counts or the 2N = n transition, and nothing about maps that go up in
dimension or threshold. It bears on them only through the ensembles. The
sparse three-point matrix (4.6), the one closest to a fly or SDM
connectivity matrix, satisfies (4.3) and so gives both JL and RIP; that is
a statement about going down, as the question says.

**Checks of what the record says about this paper.**

- LIT summary, "Any random matrix family whose norms concentrate as in the
  Johnson–Lindenstrauss lemma". Correct: any distribution satisfying
  (4.3).
- LIT summary, "once m = O(k log(n/k))". Correct in substance, in the
  record's letters. The paper states k ≤ c₁n/log(N/k) with n measurements
  and N ambient, with probability ≥ 1 − 2e^{−c₂n} and c₁, c₂ depending on δ.
- LIT summary, "via a covering of the k-sparse vectors". Imprecise. It is a
  δ/4-net of the unit sphere of each k-dimensional coordinate subspace,
  (12/δ)^k points each, plus a bootstrapping step from net to subspace.
- LIT summary, "*Constructive Approximation* 28(3): 253–263" and
  `published: 2008-01-15`. The copy prints only the journal, the DOI and
  "© 2008", with received, revised and accepted dates of 17 May 2006,
  18 January 2007 and 5 February 2007. It neither confirms nor contradicts
  the volume, issue, pages or day. The PDF's creation date is 11 January
  2008, which is consistent.
- LIT takeaway, "a union bound over a net of each k-dimensional coordinate
  subspace, and over all such subspaces". Correct. It leaves out the
  bootstrapping step, and that the per-subspace bound (5.1) is in
  unsquared norms.
- LIT takeaway, "The count of k-sparse supports replaces the count of point
  pairs". Imprecise. The count is supports times net points,
  (eN/k)^k(12/δ)^k, and the net's share sets the δ-dependence of c₁.
- LIT takeaway, "Gaussian, ±1 and Achlioptas's sparse ensembles all
  qualify". Correct, (4.4)–(4.6), with c₀(ε) = ε²/4 − ε³/6.
- LIT takeaway, "the RIP comes with a JL embedding for free". Not in the
  paper, and the direction is reversed. §6 says the RIP is a consequence of
  the JL lemma and that a distribution giving JL embeddings gives RIP
  matrices.
- LIT Standing, "derives that property from the same concentration as the
  Johnson–Lindenstrauss lemma ([LIT-1153](../literature.d/LIT-1153.md), [LIT-1157](../literature.d/LIT-1157.md))". Imprecise. The
  concentration (4.3) and its constant are Achlioptas's ([LIT-1159](../literature.d/LIT-1159.md)). The
  original JL paper is cited for the lemma; Dasgupta and Gupta only in a
  list.
- LIT Standing, "So if this proof is right, the superposition bound and
  the lemma share their mechanism". Wrong as stated. The proof is right (I
  checked it). But the superposition bound is a lower bound that assumes
  RIP; this paper shows random matrices satisfy that assumption. The
  bound's own mechanism, and the necessity of k log(N/k) in this paper,
  come from elsewhere: Do Ba et al. there, Gelfand widths here.
- QUESTION, "derive the restricted isometry property from the same
  concentration, by a union bound over sparse supports instead of point
  pairs". Imprecise in the same way as the takeaway: over net points on
  each sparse support, then a bootstrap.
- QUESTION, "the [NOTE-278](NOTE-278.md) bound rewritten as the Baraniuk et al. union
  bound". Not possible as stated, for the reason above.

**For the anthology.** The paper is mathematics. Its §6 remark that (4.6)
is cheaper to apply is engineering, not an instruction for machine-learning
practice.

## Limitations

- Constants are implicit. c₁ and c₂ are shown to exist; no numbers are
  given for the measurements needed at a given δ.
- Theorem 5.2 says the RIP (3.8), which is in squared norms, holds "with
  the prescribed δ". Lemma 5.1 proves (5.1) in unsquared norms. Squaring
  (1 + δ) gives 1 + 2δ + δ², so the squared constant is about 2δ, not δ (my
  observation; it changes constants only).
- Lemma 5.1 assumes #(T) = k < n. The proof does not use k < n.
- The last step of the proof of Theorem 5.2, from (5.1) on all supports to
  (3.8), is "easily derive[d]" and not written. The bridge to
  k ≤ c₁′n/[log(N/n) + 1] is likewise asserted.
- The JL route of §6 and the "exponential number of fixed bases" are not
  worked out.
- Everything about optimality, decoding and widths is recalled from other
  papers, not proved here.
- Sufficient conditions only. No lower bound on n is proved.

## Open questions

- What the explicit δ-dependence is. From (5.10) it is roughly
  n ≳ 16δ⁻²k[log(eN/k) + log(12/δ)] for small δ; whether the log(12/δ)
  term is needed is not discussed.
- For [QUESTION-120](../questions.d/QUESTION-120.md): whether the k log(N/k) necessity in the
  superposition bound and the Garnaev–Gluskin lower bound are one count.
  Reading Do Ba–Indyk–Price–Woodruff beside (2.3) would settle it.
- Whether Donoho and Tanner's phase transition sits at the constant c₁
  this argument leaves implicit, or far from it. The paper does not say.
