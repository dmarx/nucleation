---
status: Read
paper: LIT-300
title: 'A closed set of normal orthogonal functions'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *American Journal of Mathematics* 45(1),
    January 1923, pp. 5–24, from the Internet Archive's scan of the issue. A
    1923 US publication is in the public domain, and the Online Books Page
    records no renewals for this journal. I read all 20 pages from page
    images: the Introduction and §§1–7, with Theorems I–X, the two Lemmas,
    and all footnotes. Nothing was skipped. I checked formula (3) against
    the recursive definition (2) for n ≤ 3, and the table of c_n^(k) against
    the recurrence for n ≤ 4.). The first NOTE on this paper, which was
    seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  The paper defines a closed orthonormal set {φ} on (0, 1) of functions
  taking only the values ±1, recursively by (2) and explicitly by (3)–(4).
  In binary x = Σ a_i/2^i, the functions are signed products
  (−1)^{a_{i₁}+…+a_{i_r}}; the nth has exactly n sign changes. It proves
  Fourier-like properties: uniform convergence for continuous F with the
  terms grouped in dyadic blocks (Thm II); pointwise convergence to
  ½[F(a−0)+F(a+0)] for bounded variation (Thm IV); localisation (Thm V);
  uniform Cesàro summability for continuous F (Thm VII); a continuous
  function with a divergent φ-series at any chosen point (Thm VIII); and
  uniqueness of expansions (Thms IX–X). It never mentions groups,
  characters or (ℤ/2)ⁿ.
---

# NOTE-tmp8ppfk: A closed set of normal orthogonal functions

## Contribution

Haar (1910) had built a closed orthonormal set χ of step functions whose interest lies in its *dissimilarity* to classical sets. Walsh builds a new closed set φ of step functions, each taking only ±1 off finitely many points, whose interest lies in its *similarity* to them:

- the nth function has n − 1 (in his indexing, n) sign changes;
- each is odd or even about x = ½;
- none vanishes on a subinterval;
- the set is uniformly bounded.

Each Haar function is a finite linear combination of Walsh functions and conversely, within each dyadic level. So φ is closed because χ is. The rest of the paper develops φ's convergence theory in parallel with Fourier series: grouped uniform convergence, pointwise convergence under bounded variation, localisation, Cesàro summability, a du Bois-Reymond-type divergence example, a Gibbs-type phenomenon, and uniqueness.

## Key insight

The same 2ⁿ-dimensional space of dyadic step functions has two orthonormal bases. Haar's is localised, and Walsh's is global and oscillatory. They are related by an orthogonal transformation within each dyadic level (§2, p. 10). So the least-squares partial sums over a full level coincide (Theorem II inherits from Theorem I). The φ basis, being uniformly bounded, supports Fourier-style theorems that fail for Haar's (Theorem VI's remark).

## Assumptions

- **The interval.** (0, 1), with Lebesgue integration. At discontinuities the value is the average of the one-sided limits; at 0 it is 1, and at 1 it is (−1)^{k+1}.
- **The recursive definition (2).** φ₀ ≡ 1, and φ₁ is +1 on [0, ½), −1 on (½, 1]. Then φ_{n+1}^{(2k−1)}(x) = φ_n^{(k)}(2x) on [0, ½) and (−1)^{k+1}φ_n^{(k)}(2x−1) on (½, 1]. Likewise φ_{n+1}^{(2k)} with sign (−1)^k, for k = 1, …, 2^{n−1}.
- **Binary expansion.** Formula (3) holds for x dyadically irrational, or when a_i ≠ 0 for some i > n.

## Key results

- **Theorem I (for Haar's χ).** If F is continuous in (0, 1), series (1) converges uniformly to F if the terms are grouped so that each group contains all 2^{n−1} terms of a set χ_n^(k).
- **Orthonormality and closure (§2).** It is proved by induction via the change of variable y = 2x or 2x − 1. The paper says: "The set χ is known to be closed; it follows from the expression of the χ in terms of the φ that the set φ is also closed". Closed means there is no non-null integrable function orthogonal to all of them (footnote, p. 10).
- **Formula (3)–(4).** For example, φ₂^(1) = (−1)^{a₁+a₂} and φ₂^(2) = (−1)^{a₂}. In general φ_n^(1) = (−1)^{a_{n−1}+a_n}, and φ_n^(k) = φ_{k−1}φ_n^(1) (eq. 4). The subscript here denotes the number of zeros.
- **Theorem II.** If F is continuous in (0, 1), series (5) in the φ converges uniformly to F with the terms grouped in blocks of 2^{n−1}.
- **Theorem III.** For integrable F, the grouped series converges at x = a to lim F(x) if that limit exists, uniformly near a if F is continuous there. At dyadic rationals it converges to ½[F(a+0) + F(a−0)] when the one-sided limits exist.
- **Theorem IV.** If F has bounded variation on [0, 1], the ungrouped series (5) converges to F(x) at every point where F(a+0) = F(a−0), and at every dyadic rational, uniformly near a if F is continuous on both sides.
- **Theorem V (localisation).** For any integrable F, convergence at a point depends only on F near the point. With bounded variation near a, it converges to ½[F(a−0) + F(a+0)] when a is dyadic rational or the one-sided limits agree.
- **Theorem VI (Riemann–Lebesgue).** For any uniformly bounded orthonormal set ψ_n on (0, 1) and integrable Φ, ∫Φψ_n → 0. It fails for Haar's set: Φ(x) = (x − ½)^{−ν}, ν ≥ ½, is a counterexample.
- **Theorem VII (Cesàro).** If F is continuous on the closed interval, (5) is uniformly (C,1)-summable to F. It is pointwise summable to ½[F(a−0) + F(a+0)] where the one-sided limits exist and either they agree or a is dyadic rational. The proof is given for dyadic irrational a, and "we omit the proof for a dyadic rational".
- **Theorem VIII.** For any point a there is a continuous function whose φ-development diverges at a. The proof uses Haar's criterion: the Lebesgue constants c_n^(k) = ∫|Q_n^(k)(a, y)|dy are unbounded. The recurrence is c_{n+1}^{(2k+1)} = ½[c_n^{(k)} + c_n^{(k+1)}] + ½.
- **§6 (Gibbs analogue).** For a jump at a dyadic-irrational a, the φ-series of the indicator diverges at a. Partial sums at level k = 2^{n−1} take the value 2ⁿa − m ∈ (0, 1) near a. Overshoot peaks vanish at k = 2^{n−1} and reappear for other k: "a phenomenon quite analogous to Gibbs's phenomenon".
- **Theorems IX–X (uniqueness).** If Σ a_nφ_n converges to 0 uniformly except near a single point, or near finitely many points, then all a_n = 0. The proof uses the Lemma that convergence at one dyadic-irrational point forces a_n → 0, since |φ| = 1 there.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | {φ} is orthonormal and closed on (0, 1) | proof (closure via Haar's closure) | §2, induction plus the χ↔φ linear relations |
| C2 | Explicit binary-digit formula (3)–(4) | proof by induction, stated as "general law appears" | p. 10; checked for n ≤ 3 |
| C3 | Grouped uniform convergence for continuous F; pointwise under bounded variation; localisation | proof | Thms II–V |
| C4 | Uniform Cesàro summability for continuous F | proof (dyadic-rational case omitted) | Thm VII |
| C5 | Divergence at any prescribed point for some continuous F | proof via Haar's criterion | Thm VIII; c_n^(k) recurrence checked |
| C6 | Riemann–Lebesgue for any uniformly bounded orthonormal set; fails for Haar | proof plus counterexample | Thm VI |
| C7 | Uniqueness of φ-expansions converging to 0 off finitely many points | proof (the argument "is typical", given for one numerical case) | Thms IX–X |

## Method

Recursive dyadic construction; comparison with Haar's basis through least-squares partial sums; classical real-variable estimates (second mean-value theorem, Lebesgue constants).

## Concepts

- **The set φ_n^(k).** Now the Walsh functions, in sequency (Walsh) ordering.
- **Closed set.** Complete in the sense that there is no non-null orthogonal integrable function.
- **Summability.** First Cesàro mean.

## Connections

- **[LIT-346](../literature.d/LIT-346.md) (O'Donnell, *Analysis of Boolean Functions*).** This is the modern home of what the map calls "Boolean-Fourier". On {0,1}ⁿ, formula (3)'s (−1)^{Σ_{i∈S} a_i} are the characters χ_S. Walsh's functions of the first n binary digits are exactly these 2ⁿ characters (in a different order). Walsh does not observe this, and O'Donnell is the right citation for the character view.
- **[LIT-329](../literature.d/LIT-329.md) (Peter–Weyl) and [LIT-333](../literature.d/LIT-333.md) (Pontryagin).** On the compact abelian group (ℤ/2)^ℕ, the Walsh system is its character group, and Walsh's closure theorem is the Peter–Weyl/Pontryagin completeness of characters for that group. That is a later identification, not made here.
- **[LIT-317](../literature.d/LIT-317.md) and [LIT-351](../literature.d/LIT-351.md)** (information-theory seeds). Walsh–Hadamard codes are downstream; nothing in this paper.

## Bearing on the record

- **Map row 7, "Boolean-Fourier (characters of the Boolean cube) behind predicate harmonics".** The paper supplies the *functions*, not the *character theory*.
  - *What a reader of Walsh 1923 finds.* A complete ±1 orthonormal basis with Fourier-like convergence properties. Its explicit formula makes each function a parity of a subset of binary digits.
  - *What they do not find.* The statement that these are the group characters of (ℤ/2)ⁿ. Nor multiplicativity, a "spectrum" of a Boolean predicate, or degeneracy.
  - *What to cite.* For "predicate harmonics = characters", cite O'Donnell ([LIT-346](../literature.d/LIT-346.md)) or a harmonic-analysis source, with Walsh only as the historical origin of the basis.
- **ML practice.** It carries nothing, and does not belong in the Anthology.
- **For filing.** Keep `mathematics`. `information-theory` is justifiable only via later Walsh–Hadamard coding use, not this paper's content. It is borderline, and I would drop it.

## Limitations

- **Interval only.** No group structure is discussed, and there is no multidimensional or discrete (finite n) version.
- **Some proofs omitted.** Theorem VII's dyadic-rational case is omitted, and Theorem IX's proof is given for one configuration of x₁ and declared "typical".

## Open questions

- None raised by the paper. For the record, the question is whether the owner's "predicate harmonics" are meant on the Boolean cube (O'Donnell) or on a continuous symmetry group (Peter–Weyl). The citations differ.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary's second clause is not in the paper. The paper introduces the ±1-valued complete orthonormal system and proves its expansion properties. It says nothing about "the characters of the group (ℤ/2)^n" or Walsh–Hadamard analysis. The character structure is implicit in formula (3), where each φ is (−1) to a sum of binary digits, i.e. a product of what are now called Rademacher functions. But the paper neither states the multiplicative (group) structure φ·φ′ ∈ {φ} nor mentions Rademacher, whose paper is 1922.
- The ordering is by number of sign changes ("sequency"): φ_n^(k) has 2^{n−1} + k − 1 zeros. It is not the Paley or Hadamard ordering. The paper values the system for its *similarity* to sine/cosine/Sturm–Liouville sets, in contrast to Haar's χ. At discontinuities the functions take the average of the one-sided limits. So "±1-valued" holds only except at finitely many points, where the value is 0 (Introduction).
- The paper was presented to the AMS on 25 February 1922 and is dated Harvard University, May 1922. The seed's venue, pages and DOI are correct.
