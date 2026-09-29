---
number: 284
status: Read
formerly:
- NOTE-tmparutf
paper: LIT-333
title: 'The theory of topological commutative groups'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Annals of Mathematics* 35(2), April 1934,
    pp. 361–388, from the Internet Archive's scan of the issue. *Annals*
    issues are renewed only from July 1945, so this is in the US public
    domain. I read all 28 pages from page images: the Introduction; Chapter
    I (Group of Characters, Definitions 1–3 and 1′, Theorems 1–5, Lemmas
    1–8, Remarks 1–5); Chapter II (Structure of a Compact Group, Lemmas
    9–10, the First Fundamental Theorem); Chapter III (Locally Compact
    Connected Group, Lemmas 11–15, the Second Fundamental Theorem); Chapter
    IV (Locally Connected Group, Lemmas 16–17, Theorem 6, the Third
    Fundamental Theorem and Corollary); Appendix 1 (direct sums, Theorems
    1a–1b, Examples 1–2); Appendix 2 (connectivity and dimension, Theorems
    1c–2c); Appendix 3 (added in proof 14 May 1934); and footnotes 1–13. The
    scan duplicates pp. 380–381, and no page is missing. I followed the
    proofs step by step, but did not re-verify every construction (e.g.
    Example 2's divisibility estimate).). The first NOTE on this paper,
    which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For countable discrete abelian 𝔊, the character group X = Hom(𝔊, K), K =
  ℝ/ℤ with pointwise convergence, is compact and second countable (Thm 1).
  Characters separate points and subgroups, with annihilator
  correspondence and quotient/subgroup duality (Thms 2–4). An orthogonal
  pair (X, 𝔊) with trivial annihilators has each the character group of
  the other (Thm 5). By the First Fundamental Theorem, every compact
  second-countable abelian group is the character group of its discrete
  character group; the proof uses Peter–Weyl via Haar. Hence duality
  between countable discrete and compact second-countable abelian groups.
  Chapters III–IV give structure theorems for locally compact connected
  abelian groups (compact ⊕ ℝⁿ). Duality for *general* locally compact
  abelian groups is *not* proved here.
---

# NOTE-284: The theory of topological commutative groups

## Contribution

The paper sets out to investigate "the structure of continuous, locally compact, commutative groups, satisfying the second axiom of countability" (Introduction). Its principal method is the correspondence between discrete commutative groups and their compact character groups. It develops:

- **Chapter I.** The algebra of character groups and annihilators, and the duality of an "orthogonal couple".
- **Chapter II.** The theorem that every compact such group arises as a character group (First Fundamental Theorem), which reduces compact groups to discrete ones.
- **Chapter III.** Every locally compact connected group is its maximal compact subgroup ⊕ a vector group ℝʳ (Second Fundamental Theorem).
- **Chapter IV.** Connected, locally connected, locally compact groups are sums of countably many circles and a vector group (Third Fundamental Theorem).
- **Appendices.** The dictionary between direct-sum decompositions (Appendix 1) and between connectivity/dimension of X and torsion/rank of 𝔊 (Appendix 2). Counterexamples to Alexander–Cohen, Pietrkowsky and van Dantzig.

## Key insight

Pairing a discrete group with its compact dual is perfect in both directions once one has enough characters on the compact side. Peter–Weyl, applicable to all compact second-countable groups via Haar measure, supplies them. For abelian groups the irreducible unitary representations are one-dimensional (Lemmas 9–10 simultaneously diagonalise the commuting orthogonal matrices M_r(α)). So Peter–Weyl's separating family becomes a separating family of characters g_n: Ω → circle, which generate the discrete dual.

## Assumptions

- **Commutative.** All groups are commutative, written additively except in Chapter II.
- **Countability.** Continuous groups are locally compact and second countable. Discrete groups are at most countable. (Remark 2 notes that Lemma 1 extends to uncountable groups by transfinite induction.)
- **K = ℝ/ℤ,** the "continuous cyclic group".
- **External results.** Peter–Weyl (Math. Ann. 97) with Haar's measure (Annals 34, 1933) for Chapter II; Schreier's covering results; Kronecker's theorem (Lemma 6).

## Key results

- **Definition 1.** X = homomorphisms 𝔊 → K, with pointwise convergence and pointwise sum.
- **Theorem 1.** "The group of characters of a discrete group is always compact and satisfies the second axiom of countability." The proof is by diagonal extraction.
- **Lemma 1.** A non-zero character of a subgroup ℌ extends to 𝔊 with β(𝔵) ≠ 0 for a given 𝔵 ∉ ℌ. This is divisibility of K, i.e. extension of homomorphisms.
- **Theorem 2.** If Φ = (X, ℌ), the annihilator, then ℌ = (𝔊, Φ).
- **Theorem 3.** The character group of ℌ is X/Φ, and that of 𝔊/ℌ is Φ.
- **Lemmas 2–3.** Closed subgroups of K are K or finite cyclic. The dual of a finite group of order r has order r. Remark 3: it is isomorphic to it, a "well-known fact" not used.
- **Lemma 4 and Theorem 4.** If (𝔊, Φ) = 0 then Φ = X; generally (X, ℌ) = Φ when ℌ = (𝔊, Φ). The proof goes through finite groups (L5), finitely many independent generators via Kronecker (L6), finitely generated groups (L7), and a countable union.
- **Theorem 5.** If X and 𝔊 are orthogonal, each is the character group of the other, via α(𝔵) = α𝔵 = 𝔵(α).
- **Lemma 8.** For an orthogonal couple, any value of order dividing g can be realised at an element of order g.
- **Remark 5.** The dual of a free group on n generators is the n-torus.
- **First Fundamental Theorem (p. 372, verbatim).** "Let Ω be a continuous compact commutative group satisfying the second axiom of countability, and 𝔊 the discrete group of its characters, then the group Ω is isomorphic to the group of characters of 𝔊." The proof uses Peter–Weyl in the form 1)–2) (p. 371): a countable system of real functions f_{r,i} transforming by orthogonal matrices M_r(α) that separate points. Lemma 9 simultaneously diagonalises commuting orthogonal matrices over ℂ. Lemma 10 gives a countable family of continuous characters g_n separating points. The g_n generate 𝔊, and Theorem 5 applies.
- **Lemma 11.** A locally compact connected Ω has a discrete subgroup Λ, with no limit points and countable, such that Ω/Λ is compact.
- **Lemma 12.** A non-compact such Ω contains a free cyclic subgroup without limit points.
- **Lemma 13.** A connected T with a discrete Λ and toroidal T/Λ is vector ⊕ toroidal.
- **Lemma 14.** Near 0 there is a compact Λ with Ω/Λ = vector ⊕ torus.
- **Lemma 15.** A maximal compact subgroup Δ exists, and Ω/Δ is a vector group.
- **Second Fundamental Theorem (p. 377, verbatim).** "A locally compact connected group Ω satisfying the second axiom of countability decomposes into a direct sum of a compact subgroup Δ, and a vector subgroup N (see Definition 4), where the subgroup Δ is determined uniquely, and the dimensionality r of the group N is an invariant of the group Ω."
- **Lemma 16.** A torsion-free 𝔊 in which increasing sequences of subgroups of equal finite rank stop has a free basis.
- **Lemma 17.** Otherwise the dual is not locally connected.
- **Theorem 6.** A connected, locally connected compact X (second countable) is a direct sum of a finite or countable number of circles.
- **Third Fundamental Theorem (p. 380).** A connected, locally connected, locally compact Ω (second countable) is a direct sum of finitely or countably many circles and a vector group. The Corollary adds finitely many circles if Ω is finite-dimensional or has no small subgroups.
- **Appendix 1, Theorems 1a/1b.** Direct-sum decompositions of 𝔊 and X correspond via annihilators. Remark 3ab calls this "a complete duality".
  - Example 1 (Prüfer's group, dualised) contradicts Alexander–Cohen and Pietrkowsky.
  - Example 2 is a rank-2 torsion-free indecomposable 𝔊, whose dual is a 2-dimensional compact connected indecomposable group. It contradicts van Dantzig's claim.
- **Appendix 2.**
  - Theorem 1c: X is connected iff 𝔊 is torsion-free.
  - Corollary 1c: the identity component of X is the annihilator of the torsion subgroup.
  - Theorem 2c: dim X = rank 𝔊.
  - Corollary 2c: X is zero-dimensional iff 𝔊 is torsion.
- **Appendix 3.** In an orthogonal couple, the discrete 𝔊 has no non-trivially convergent sequences. So Definition 1′ rightly omits topology on the dual of a compact group.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The dual of a countable discrete abelian group is compact and second countable | proof | Theorem 1 |
| C2 | Subgroup/annihilator and quotient/subgroup duality | proof | Theorems 2–4, Lemmas 1, 4–7 |
| C3 | In an orthogonal couple each group is the other's dual | proof | Theorem 5, Appendix 3 |
| C4 | Every compact second-countable abelian group is the dual of its discrete dual | proof (relies on Peter–Weyl plus Haar) | First Fundamental Theorem, Lemmas 9–10 |
| C5 | Locally compact connected = compact ⊕ ℝʳ, with Δ unique and r invariant | proof | Second Fundamental Theorem, Lemmas 11–15 |
| C6 | Connected, locally connected, locally compact = circles ⊕ vector group | proof | Theorem 6, Third Fundamental Theorem |
| C7 | Direct-sum decompositions correspond under duality; published decomposition claims fail | proof plus counterexamples | Appendix 1, Examples 1–2 |
| C8 | Connectedness ↔ torsion-free; dimension ↔ rank | proof | Appendix 2 |

## Method

Algebraic duality via annihilators; Kronecker approximation; transfer from compact groups using Peter–Weyl and Haar; point-set topology of locally compact groups; covering-space arguments (Schreier).

## Concepts

- **Continuous cyclic group K = ℝ/ℤ.**
- **Group of characters (Definition 1 / 1′).** Not "dual group", a term the paper does not use.
- **Annihilator (X, ℌ), (𝔊, Φ).**
- **Couple and orthogonal couple (Definition 3).** A bilinear continuous pairing into K, with trivial annihilators.
- **Vector group, toroidal group.** ℝⁿ and Tⁿ.

## Connections

- **[LIT-329](../literature.d/LIT-329.md) (Peter–Weyl).** This is the input to the First Fundamental Theorem. For commutative groups, Pontryagin extracts one-dimensional characters from Peter–Weyl's orthogonal representations by simultaneous diagonalisation (Lemmas 9–10).
- **[LIT-300](../literature.d/LIT-300.md) (Walsh).** The Walsh system is the character group of the compact group (ℤ/2)^ℕ, whose dual is the countable discrete group ⊕ℤ/2. That is an instance of the First Fundamental Theorem and C8 (a zero-dimensional X ↔ a torsion 𝔊, Corollary 2c). The paper does not mention it.
- **[LIT-353](../literature.d/LIT-353.md) (Stone).** For Boolean groups the analogy is exact. The Stone space of a Boolean algebra is the space of homomorphisms to Z₂ (a compact, zero-dimensional space). Pontryagin's dual of a discrete Boolean (exponent-2) group is a compact zero-dimensional group. The paper draws no connection to Stone.
- **[LIT-313](../literature.d/LIT-313.md) (Gelfand–Naimark).** The C*-algebra of a discrete abelian group is C(dual group), which is Gelfand duality applied to Pontryagin duality. That unification is later literature.
- **[LIT-346](../literature.d/LIT-346.md) (O'Donnell).** Boolean Fourier analysis is Pontryagin duality for the finite group (ℤ/2)ⁿ. This paper's Remark 3 (the dual of a finite group is isomorphic to it) is the relevant fact, stated but not used.

## Bearing on the record

- **Map row 7 and §2 item 2, "the Pontryagin leg of the duality tripod (characters)".** The paper supplies the characters leg: a compact abelian group is recovered from its characters, and conversely. That is what makes "harmonics = characters" well defined on any compact abelian symmetry group.
- **Two scope limits for the owner.**
  - *Commutative only.* For non-abelian symmetry, the relevant object is Peter–Weyl ([LIT-329](../literature.d/LIT-329.md)), not Pontryagin duality. Non-abelian groups do not have a dual group in this sense, and characters there are traces, not homomorphisms.
  - *Compact/discrete, second countable.* That covers the (ℤ/2)ⁿ, circle and torus cases the owner is likely to use. General LCA groups (e.g. ℝ) are not covered here.
- **The "tripod".** This paper is one leg, and neither it nor the other two legs' primary sources ([LIT-313](../literature.d/LIT-313.md), [LIT-353](../literature.d/LIT-353.md)) state a common duality. Presenting Gelfand, Stone and Pontryagin as "one duality" is the owner's synthesis, and a later-literature commonplace, which should be cited to a secondary source.
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **Second countability throughout.** The duality is only for compact versus countable discrete groups. General LCA duality came later (van Kampen 1935, as the seed notes).
- **The compact case depends on Peter–Weyl plus Haar**, which is external.
- **Some proofs are "easily seen".** E.g. the neighbourhood basis in Theorem 1, and Example 2's non-decomposability.

## Open questions

- None posed explicitly. The paper points to extending beyond second countability (Remark 2) and to non-compact duality (implicitly).

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary's parenthesis "(compact or discrete, second countable)", which is exactly the paper's scope. One precision: duality is proved between *countable discrete* abelian groups and *compact second-countable* abelian groups (Theorem 5 plus the First Fundamental Theorem). The paper's own statement of "each is the character group of the other" is Theorem 5, for an orthogonal couple. Locally compact non-compact groups (Chs. III–IV) are treated for *structure* (Second and Third Fundamental Theorems), not duality.
- The characters are homomorphisms into K = ℝ/ℤ, written additively, not into the unit circle. Remark 1 identifies the two. The dual of a compact group X is taken *without* topology, as algebraic homomorphisms that are continuous (Definition 1′). Appendix 3, added in proof, justifies this: in an orthogonal couple 𝔊 has no non-trivial convergent sequences.
- The author is printed "L. Pontrjagin", Moscow. The paper was received 22 November 1933, revised 6 March 1934, and the results were reported at the International Congress, Zürich 1932 (footnote 1).
