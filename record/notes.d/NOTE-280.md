---
number: 280
status: Read
formerly:
- NOTE-tmp7u6wk
paper: LIT-309
title: 'On hypercomplex numbers'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Proceedings of the London Mathematical
    Society* (2) 6, pp. 77–118, from the Internet Archive's public-domain
    scan of the 1908 volume (University of Leeds copy). I read all 42 pages
    from page images: the index of terms and introduction (pp. 77–78),
    §§1–12 (Calculus of Complexes; Invariant Sub-algebras; Reducibility;
    Nilpotent Algebras; Potent Algebras; Classification of Potent Algebras;
    the Identical Equation; Classification continued; Non-associative
    Algebras; Semi-invariant Sub-algebras; the Direct Product; Conclusion),
    the correction "Added February 1st, 1908" (p. 117), the list of 15
    memoirs and the contents (p. 118). Nothing was skipped. §7's
    Sylvester-type identities (pp. 106–108) I followed at the level of the
    argument, not re-deriving each coefficient identity.). The first NOTE on
    this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For associative algebras with a finite basis over an arbitrary field F,
  the paper proves the structure theory. A semi-simple algebra (no
  nilpotent invariant sub-algebra) is uniquely the direct sum of simple
  algebras (Thms 10, 17). Every simple algebra is the direct product of a
  primitive (division) algebra and a simple matric algebra, i.e. a full
  n×n matrix algebra (Thms 21–23). The maximal nilpotent invariant
  sub-algebra N contains all others (Thm 13), and A/N is semi-simple. When
  every non-invertible element is nilpotent, A = B + N with B primitive
  (Thm 28, with a proof correction added 1 Feb 1908). Section 8 lists the
  results as (i)–(vi).
---

# NOTE-280: On hypercomplex numbers

## Contribution

The paper sets out "the theory of hypercomplex numbers on a rational basis": over any field, and without the characteristic equation that Cartan's and Frobenius's methods relied on. It uses a calculus of "complexes" (linear subspaces) modelled on Frobenius's group calculus (p. 78). It develops invariant sub-algebras (two-sided ideals), difference (quotient) algebras, a Jordan–Hölder theorem for composition series (Thms 5–6), nilpotent and potent algebras, idempotents and the Peirce decomposition, and then the classification of semi-simple and simple algebras. §9 extends parts to non-associative algebras, §10 treats one-sided ideals, and §11 tensor ("direct") products.

## Key insight

Idempotents do the work that characteristic roots did before. A potent algebra contains an idempotent (Thm 14, proved without extending the field). A semi-simple algebra splits along central idempotents into simple ones (Thm 17). A simple algebra's primitive idempotents e_p give Peirce pieces A_pq = e_pAe_q with A_pqA_qr = A_pr (Thm 20). Choosing x_pq ∈ A_pq with x_pqx_qp = e_p produces n² matrix units e_pq (Thm 21). Then A = (e_pq) × A₁₁, a full matrix algebra over the primitive corner algebra A₁₁ (Thm 22).

## Assumptions

- **Algebra.** Linear combinations Σ ξ_r x_r over a field F, finite basis, associative, bilinear (§1, (i)–(iii)). The field is "constant throughout but otherwise arbitrary".
- **Modulus.** An identity element; not assumed in general. Algebras with and without modulus are treated separately (Thms 7, 10, 16).
- **Invariant sub-algebra.** B with AB ≤ B and BA ≤ B. "Simple" means no invariant sub-complex (§2).
- **Semi-simple.** No nilpotent invariant sub-algebra (§4). Nilpotent means A^a = 0.
- **Primitive.** Only one idempotent. This is the paper's term for division algebra in the semi-simple case.

## Key results

- **Thms 1–3.** Invariant sub-algebras are closed under sum. Two distinct maximal ones sum to A. Quotients ("difference algebras", A − B) exist, following Molien.
- **Thms 4–6.** The correspondence theorem, the second isomorphism theorem, and "Any two difference series of the same algebra are identical apart from the order of their terms" (Thm 6).
- **Thm 7 and corollary.** If an invariant sub-algebra B and A both have a modulus, A is reducible. A = B + C uniquely, with C = (e − e₁)A(e − e₁).
- **Thms 8–10.** "An algebra A can be uniquely expressed as the direct sum of irreducible algebras which have each a modulus, and an algebra which has no modulus" (Thm 10). This extends Scheffers.
- **Thms 11–12.** Filtration of an algebra of index a. A²-difference series of zero algebras.
- **Thm 13.** "If N is a maximal nilpotent invariant sub-algebra of an algebra A, all other nilpotent invariant sub-algebras of A are contained in N." Hence A − N has no nilpotent invariant sub-algebra, i.e. it is semi-simple.
- **Thm 14.** "Every potent algebra contains an idempotent element." Footnote: in most proofs the idempotent is irrational, and this one is rational. The converse: an algebra all of whose elements are nilpotent is nilpotent, so the definition of nilpotence agrees with Cartan's.
- **Thm 15.** It extends Peirce: "If an algebra A possesses only one idempotent element e, every element which does not possess an inverse with respect to e, is nilpotent." Corollary: e is then the modulus, and A is "primitive".
- **Thm 16 and corollaries.** An algebra without modulus has a nilpotent invariant sub-algebra. The Peirce decomposition is (5), A = B + Σe_pB₁ + ΣB₂e_p + Σe_pAe_q, with a principal idempotent e = Σe_p. A semi-simple algebra "always has a modulus" (p. 94).
- **Thm 17 (p. 94).** "A semi-simple algebra, which is not simple, is reducible." Hence it is the direct sum A₁ + A₂ + … + A_n of simple algebras with A_pA_q = 0 (p ≠ q).
- **Thm 18.** eAe is semi-simple for an idempotent e of a semi-simple A. Corollary: primitive if e is primitive.
- **Thm 19.** If A is simple, A_pq ≠ 0 for all p, q; if it is semi-simple and not simple, A_pq = 0 entails A_qp = 0.
- **Thm 20 (p. 96).** "If A is simple, then A_pqA_qr = A_pr, and the order of A_pq is the same for all values of p and q." Corollary: for any x_pq ≠ 0 there is x_qp with x_pqx_qp = e_p.
- **Thm 21 (p. 97).** "If A is simple, it is possible to find a set of n² elements e_pq … such that e_pqe_qr = e_pr and e_pqe_rs = 0 (q ≠ r); and e = Σe_rr is the modulus of A." Such an algebra is called a "simple or quadrate matric algebra of order n²".
- **Thm 22 (p. 99).** "Any simple algebra can be expressed as the direct product of a primitive algebra and a simple matric algebra." Footnote: Cartan (1), p. 67, gives this form over the reals, "apparently without observing that his result is capable of this simple description".
- **Thm 23.** The direct product A of a primitive B and a quadrate matric C is simple. Any element commuting with every element of C lies in B. Corollary: the only element of a quadrate matric algebra commuting with everything is (a multiple of) the modulus.
- **Thm 24.** If N is the maximal nilpotent invariant sub-algebra of A with modulus, and A − N is simple, then A is a simple matric algebra × an algebra with only one idempotent.
- **§7, the identical (characteristic) equation.** Thm 25: semi-simplicity is preserved under field extension. Footnote: this assumes that rational elements independent in F stay independent in F′. Thm 26 is a rationality lemma for commuting sub-algebras. Thm 27: over an algebraically extended F′, a primitive A that splits into r isomorphic simple algebras is the direct product of a commutative algebra rational in F and a simple algebra. Footnote: this proves Allan's theorem that the order of a primitive algebra is bn².
- **Thm 28 (p. 105).** "If A is an algebra in which every element, which has no inverse, is nilpotent, it can be expressed in the form A = B + N, where B is a primitive algebra and N the maximal nilpotent invariant sub-algebra." This holds in the commutative case, and for Galois fields via "there is no non-commutative primitive algebra" (citing Wedderburn [8], his finite-division-ring theorem). The correction "Added February 1st, 1908" repairs a gap: the proof had assumed B′ commutes with every element of A.
- **§8, summary (p. 109).**
  - (i) An algebra is uniquely modulus-part ⊕ modulus-free part (Thm 10).
  - (ii) An algebra with modulus is uniquely a direct sum of irreducibles (Thm 10).
  - (iii) Any algebra = nilpotent + semi-simple, the latter not unique but unique up to isomorphism (Thms 24, 28).
  - (iv) Semi-simple = unique direct sum of simples (Thms 10, 17).
  - (v) Simple = primitive × simple quadrate (Thms 22, 23).
  - (vi) A simple quadrate algebra is a matric algebra (Thm 22).
- **§9.** In non-associative algebras, Thms 4–6 hold, but an algebra may be simple with all elements nilpotent. Example: a three-unit algebra over GF[2]. "Modular sub-algebras" of three kinds are introduced.
- **§§10–11.** Semi-invariant (one-sided) sub-algebras: a primitive algebra is the only type with none. The direct product: if the field is such that every simple algebra is matric, the product of two simple algebras is simple or semi-simple. The quaternion example shows B × B can be reducible.
- **§12.** Many theorems need no division in the field. With integer coefficients, A² ≠ A can still hold with A² of the same order as A.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Semi-simple algebras are uniquely direct sums of simple algebras, over any field | proof | Thms 10, 13, 16, 17 |
| C2 | Every simple algebra is primitive ⊗ full matrix algebra; the matrix units exist rationally | proof | Thms 20–22 |
| C3 | Primitive (one-idempotent) semi-simple algebras have every non-zero element invertible | proof | Thm 15 and its corollary |
| C4 | Every potent algebra has a rational idempotent | proof | Thm 14 |
| C5 | A/N primitive ⇒ A = B + N with B primitive (principal theorem, special case) | proof, as corrected on 1 Feb 1908 | Thm 28 and the Added note |
| C6 | Every algebra is nilpotent + semi-simple, the latter unique up to isomorphism | claimed in the summary | §8 (iii) cites Thms 24 and 28, which cover only the A/N simple or primitive cases |
| C7 | The order of a primitive algebra is bn² (Allan) | proof sketch | Thm 27 footnote |
| C8 | Non-associative simple algebras can be nil | example | §9, the GF[2] algebra |

## Method

A Frobenius-style calculus of complexes (subspaces) with ≤, +, ∩ and products; ideals and quotients; idempotent lifting; Peirce decomposition; matrix-unit construction; characteristic-equation arguments only in §7.

## Concepts

- **Complex, order, supplement, A ∩ B, AB.** Subspace, dimension, complement, intersection, product space.
- **Invariant sub-algebra.** A two-sided ideal. **Difference algebra (A − B).** The quotient.
- **Modulus.** Identity. **Potent / nilpotent / index.**
- **Primitive algebra.** Only one idempotent. **Principal idempotent.**
- **Quadrate / simple matric algebra.** A full matrix algebra (e_pq). **Matric algebra.** A semi-simple sum of these.
- **Direct product.** The tensor product (§11).

## Connections

- **[LIT-352](../literature.d/LIT-352.md) (Murota et al.).** Theorem 3.1 there is this paper's Thms 17 and 22 specialised to *-algebras. Its erroneous 3.1(C) forgets exactly this paper's point that the primitive factor can be non-trivial: over ℝ, the division algebras ℂ and ℍ occur (Wedderburn's own §11 quaternion example).
- **[LIT-331](../literature.d/LIT-331.md) (Artin 1927, unreachable).** The ring-theoretic generalisation (chain conditions instead of a finite basis).
- **[LIT-329](../literature.d/LIT-329.md) (Peter–Weyl).** The matrix-unit relations e_ip e_qk = δ_pq (V/n) e_ik in §4 there are Thm 21's for the group algebra of a compact group.
- **[LIT-313](../literature.d/LIT-313.md) (Gelfand–Naimark).** Theorem 3 there, on simple weakly closed rings being factors, is the infinite-dimensional descendant of Thm 17's "simple components have trivial centre" (Thm 23 corollary).
- **[LIT-339](../literature.d/LIT-339.md) (WWW), [LIT-321](../literature.d/LIT-321.md) (Haag).** Superselection sectors correspond to the simple summands of Thm 17, and their central idempotents.

## Bearing on the record

- **Map row 6, "the algebra → centre / isotypic-block machinery behind types = Z(𝒜)".** Wedderburn owns the block half of this, and it is directly relevant.
  - *The blocks.* For a finite-dimensional algebra of operators closed under adjoint (hence semi-simple), Thm 17 splits it uniquely into simple blocks, and Thm 22 makes each block a full matrix algebra over a division algebra.
  - *The centre.* The paper never uses the word "centre". What it proves is Thm 23's corollary (only multiples of the modulus commute with a quadrate matric algebra) and the uniqueness of the simple summands. Together these give Z(A) = span of the block identities, and the owner can cite that. The explicit statement "types = Z(𝒜)" is a modern gloss on this; it is not stated in the paper.
  - *Isotypic multiplicity.* "Isotypic block" (irreducible module × multiplicity) is not the paper's formulation. It works with algebras, not modules. The multiplicity is visible as the n of the n² matrix units.
- **Caution for the owner.** Thm 22's primitive factor matters for real operator algebras (see the [LIT-352](../literature.d/LIT-352.md) note). A real *-algebra's simple block can be M_n(ℂ) or M_n(ℍ), not only M_n(ℝ).
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **Finite basis only.** The generalisation is Artin's.
- **The principal theorem is proved only in special cases,** though the summary states it generally. A proof gap in Thm 28 was patched by the author's added note.
- **Dated notation.** "<", "∩" and "direct product" are used idiosyncratically, and the Thm 25 footnote adds an unproved assumption about field extension.

## Open questions

- The paper's own: classification of primitive (division) algebras, and of nilpotent algebras ("cannot be carried much further", §8).

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary ("a finite-dimensional semisimple algebra is a direct sum of full matrix algebras over division algebras"), with three precisions. (1) The paper states it as two theorems: semi-simple = direct sum of simple (Thm 17, uniqueness from Thm 10), and simple = direct product of a *primitive* algebra and a *simple matric* algebra (Thm 22). "Primitive" here means having only one idempotent. The paper shows such an algebra has every element either invertible or nilpotent (Thm 15 and its corollary), which makes it a division algebra once it is also semi-simple. The phrase "division algebra" is not used. (2) The field F is arbitrary; that is the paper's advertised novelty over Cartan and Frobenius, who worked over ℂ or ℝ. (3) Wedderburn's summary (iii) states that any algebra is nilpotent + semi-simple, but Thm 28 proves the splitting only when A/N is primitive. The general principal theorem is claimed in (iii) with a reference to "Theorems 24 and 28", which is more than those theorems as stated deliver. The paper itself concedes that the classification is "incomplete in so far as the classification is given in terms of primitive algebras which have not themselves been classified" (§6).
- The paper was received 7 July 1907, read 14 November 1907, and communicated by W. Burnside. The author is printed "J. H. Maclagan Wedderburn". The volume is dated 1908, and the running heads show "1907" (the reading date).
