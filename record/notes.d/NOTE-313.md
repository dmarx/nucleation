---
number: 313
status: Read
formerly:
- NOTE-tmpzpe87
paper: LIT-355
title: 'An Introduction to Hyperplane Arrangements'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full lecture notes, "version of February 26, 2006",
    114 PDF pages (printed pp. 1–110): the contents, Lectures 1–6 with all
    exercises, and the 38-item bibliography. I also read the author's errata
    and addenda (version of 18 October 2020, 6 pp.). The PDF is the file the
    author's own page (math.mit.edu/~rstan/arrangements/arr.html) links as
    "pdf file". It is hosted on a University of Pennsylvania course
    directory (cis6100), and the author's errata name that location as the
    reference version. I used it because the author designates it, not as a
    third-party repost. The text was extracted with PyMuPDF. Figures were
    not rendered; they are described in the text wherever the argument needs
    them. At 110 printed pages the notes fall under the brief's book-length
    threshold, and I read all of it. I read Lectures 1–2 (regions, the
    intersection poset, Zaslavsky's theorem) and Lecture 6 (separating
    hyperplanes) closely, and Lectures 3–5 in full but at the level of
    statements and proof outlines. I did not read the printed version in
    *Geometric Combinatorics* (IAS/Park City Mathematics Series 13, AMS
    2007). `published:` is the date of the version read, the earliest dated
    text I could verify. The lectures were given on 12–19 July 2004, and the
    printed chapter is dated 31 October 2007 by Crossref. No anthology entry
    exists for this work.). The first NOTE on this paper, which was seeded
    from its abstract alone.
date: '2026-09-29'
summary: >-
  The notes define the regions of a real arrangement (connected components
  of the complement) and the intersection poset L(A) with its Möbius
  function and characteristic polynomial χ_A(t) = Σ μ(x) t^{dim x}. They
  prove Zaslavsky's theorem (Thm 2.5): r(A) = (−1)ⁿ χ_A(−1) and b(A) =
  (−1)^{rank A} χ_A(1), so the numbers of regions and bounded regions
  depend only on L(A), not on the face structure (Cor. 2.1, Fig. 2). The
  same machinery counts faces of every dimension (Thm 2.6: f_k = Σ_{x≤y,
  dim x=k} |μ(x,y)|). Later lectures add Whitney's theorem,
  deletion–restriction, matroids and geometric lattices, broken circuits,
  supersolvability, the finite-field method, and the metric d(R, R′) =
  number of separating hyperplanes, whose zero set shows that a region is
  determined by its separating set (p. 89).
---

# NOTE-313: An Introduction to Hyperplane Arrangements

## Contribution

These are graduate-level notes that develop the combinatorics of finite hyperplane arrangements from scratch, including the needed poset and matroid background, in six lectures with graded exercises. The notes are expository. The results are credited to Zaslavsky, Whitney, Rota, Crapo, Greene, Terao, Athanasiadis, Björner–Edelman–Ziegler, Varchenko and others. What the notes add is a single self-contained route to them. The route goes from regions to the intersection poset and the characteristic polynomial, and then to Zaslavsky's counts. From there it runs through matroids, broken circuits and supersolvable factorisation, the finite-field method with its enumerative applications (Shi, Catalan, semiorder, Linial and threshold arrangements), and finally separating hyperplanes and distance enumerators.

## Key insight

For a real arrangement, the number of pieces the hyperplanes cut space into is determined by the lattice of their intersections alone, not by how the pieces are shaped. That number is the characteristic polynomial of the intersection poset, evaluated at −1: r(A) = (−1)ⁿ χ_A(−1). Two arrangements with the same L(A) and different face structure have the same number of regions and bounded regions (Cor. 2.1, Fig. 2). The same Möbius-function computation counts faces of every dimension (Thm 2.6).

## Assumptions

- A finite set of affine hyperplanes in V ≅ Kⁿ (Lecture 1). Regions, faces and bounded regions need K = ℝ. The poset, matroid and characteristic-polynomial results hold over any field, and the finite-field method needs arrangements defined over ℚ (hence over ℤ) with "good reduction" mod p (Lecture 5).
- Lecture 3 onward assumes finiteness of posets, lattices and matroids ("Unless explicitly stated otherwise", p. 12).
- The second proof of Thm 2.5 assumes basic facts about Euler characteristic, and for the bounded case the omitted fact ψ(Γ) = 1 (p. 21).

## Key results

- **Regions and bounded regions (§1.1).** A region is a connected component of ℝⁿ − ∪H. Each region is open and convex, and its closure is a polyhedron (pp. 3–4). m lines in general position in ℝ² give C(m,2) + m + 1 regions (Ex. 1.2), and the braid arrangement xᵢ = xⱼ gives n! (Ex. 1.3). Projectivisation halves the number of regions and coning doubles it (pp. 5–7).
- **Intersection poset (Def. 1.1, Prop. 1.1).** L(A) is the set of nonempty intersections, ordered by reverse inclusion. It is graded with rank = codimension (Prop. 1.1). It is a meet-semilattice, and a lattice iff A is central (Prop. 2.3). Every interval is a geometric lattice (Prop. 3.8).
- **Characteristic polynomial (Def. 1.3).** χ_A(t) = Σ_{x∈L(A)} μ(x) t^{dim x}. For the coordinate arrangement it is (t − 1)ⁿ (Prop. 1.2).
- **Deletion–restriction and Whitney (Lemma 2.2, Thm 2.4).** χ_A = χ_{A′} − χ_{A″}, and χ_A(t) = Σ_{B⊆A central} (−1)^{#B} t^{n − rank B}.
- **Zaslavsky's theorem (Thm 2.5).** r(A) = (−1)ⁿ χ_A(−1) and b(A) = (−1)^{rank A} χ_A(1). Two proofs are given: a recurrence (Lemma 2.1: r(A) = r(A′) + r(A″)), and Euler characteristic with Möbius inversion. **Corollary 2.1**: r(A) and b(A) depend only on L(A).
- **Face counts (Thm 2.6).** f_k(A) = Σ_{x≤y in L(A), dim x = k} |μ(x, y)|.
- **General position (Prop. 2.4).** r(A) = Σ_{i≤n} C(m, i) and b(A) = C(m − 1, n).
- **Graphs (Thm 2.7, Prop. 2.5, Cor. 2.3).** χ_{A_G} = the chromatic polynomial χ_G. Regions of the graphical arrangement ↔ acyclic orientations, so #AO(G) = (−1)ⁿ χ_G(−1).
- **Matroids (Lecture 3).** A central arrangement gives a simple matroid with L(M) ≅ L(A) (Prop. 3.6). Finite geometric lattices = lattices of flats (Thm 3.8). The Möbius function alternates strictly in sign (Thm 3.10), so the coefficients of χ alternate (Cor. 3.5).
- **Broken circuits and factorisation (Lecture 4).** The coefficients of χ_M count the faces of the broken-circuit complex (Thm 4.12). For central real A, r(A) = the number of subsets of normals containing no broken circuit (Cor. 4.7). The modular-element factorisation (Thm 4.13) gives, for supersolvable lattices, χ = Π(t − eᵢ) (Cor. 4.9). Terao's factorisation for free arrangements is stated without proof (Thm 4.14).
- **Finite-field method (Thm 5.15).** With good reduction, χ_A(q) = #(F_qⁿ − ∪H). Applications: the Coxeter arrangement of type B has χ = Π(t − (2i − 1)) and r = 2ⁿn!. The Shi arrangement has χ = t(t − n)^{n−1} and r = (n + 1)^{n−1} (Thm 5.16, Cor. 5.11). The Catalan arrangement has r = n!Cₙ (Prop. 5.14, Thm 5.18). Semiorders and interval orders appear as regions (Props. 5.16–5.17, Thms 5.19–5.20).
- **Separating hyperplanes (Lecture 6).** d(R, R′) = #sep(R, R′) is a metric on regions (p. 89). The weak order and distance enumerator are defined relative to a base region. For the braid arrangement, d = the number of inversions and D = Π(1 + t + … + t^{i−1}) (Prop. 6.18). For the Shi arrangement, region labels are exactly the parking functions (Thm 6.23, sketched) and D = Σ_{PF} t^{Σaᵢ − n} (Cor. 6.14). For supersolvable arrangements with a canonical base region, D = Π(1 + … + t^{eᵢ}) (Thm 6.24, Björner–Edelman–Ziegler). The Varchenko determinant is stated without proof (Thm 6.25).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Regions of a real arrangement are open convex sets with polyhedral closures | strong | argument p. 4, with Exercise 1.1 left to the reader |
| C2 | r(A) = (−1)ⁿ χ_A(−1) | strong | Thm 2.5, two proofs (recurrence; Euler characteristic with Möbius inversion), pp. 19–20 |
| C3 | b(A) = (−1)^{rank A} χ_A(1) | moderate | Thm 2.5. The recurrence proof is complete modulo two "[why?]" steps; the topological proof omits ψ(Γ) = 1 (p. 21) |
| C4 | r(A) and b(A) depend only on the intersection poset | strong | Cor. 2.1 of Thm 2.5; Fig. 2 gives two arrangements with the same L(A) and different face shapes |
| C5 | Number of k-dimensional faces = Σ_{dim x = k, x ≤ y} \|μ(x,y)\| | strong | Thm 2.6, proof via Thm 2.5 applied to each restriction Aˣ, with Thm 3.10 for the sign |
| C6 | d(R, R′) = number of separating hyperplanes is a metric on regions (so a region is determined by which side of each hyperplane it lies on) | moderate | asserted "easily seen" (p. 89). The parenthetical reading is my own, not stated in the notes |
| C7 | For central A, L(A) is determined by which subsets of normals are linearly independent (the matroid) | strong | Prop. 3.6 |
| C8 | Shi arrangement: χ = t(t − n)^{n−1}, r = (n + 1)^{n−1}, regions labelled by parking functions | strong / moderate | Thm 5.16 proved; Thm 6.23 only sketched ("Proof … (sketch)") |
| C9 | Supersolvable central arrangements with canonical base region have D(t) = Π(1 + t + … + t^{eᵢ}) | strong | Thm 6.24, proof by induction on rank via Lemma 6.7 |
| C10 | det V(A) = Π_{x ≠ 0̂} (1 − a_x²)^{n(x)p(x)} (Varchenko) | weak here | stated, "Proof. Omitted." (p. 105) |

## Method

The notes are expository mathematics, with proofs by Möbius inversion in incidence algebras, deletion–restriction recurrences, the crosscut theorem via the Möbius algebra (Thms 2.2–2.3), E-labelings of posets (Thm 4.11), and point counting over finite fields (Thm 5.15). Each lecture ends with exercises graded [1] to [5], where [5] means unsolved. The errata supply a corrected proof of Lemma 2.2's second half (errata p. 2).

## Concepts

- **arrangement** — a finite set of affine hyperplanes in Kⁿ. It is *central* if the intersection of all its hyperplanes is nonempty, and *essential* if rank = dimension. Its *rank* is the dimension of the span of the normals.
- **region** — a connected component of the complement of ∪H (K = ℝ). *Relatively bounded* means bounded after essentialisation.
- **face** — a nonempty set R̄ ∩ x with R a region and x ∈ L(A) (Def. 2.4). Every face is a region of exactly one restriction Aˣ.
- **intersection poset L(A)** — nonempty intersections ordered by *reverse* inclusion (Def. 1.1). The reversal is chosen so that L(A) is a geometric lattice, not its dual (Note, p. 8).
- **characteristic polynomial χ_A(t)** — Σ μ(x) t^{dim x} (Def. 1.3).
- **sep(R, R′), d(R, R′), weak order, distance enumerator** — the hyperplanes separating two regions, their number, the order by inclusion of sep(R₀, ·), and Σ_R t^{d(R₀,R)} (§6.1).
- **supersolvable** — having a maximal chain of modular elements in L(A) (Def. 4.13).
- **good reduction mod p** — L(A) ≅ L(A_q) (Lecture 5).

## Connections

The central theorem (Thm 2.5) is Zaslavsky's, from the unreachable Memoir [LIT-332](../literature.d/LIT-332.md) and the unreachable announcement [LIT-359](../literature.d/LIT-359.md) (Zaslavsky 1975, Bull. AMS). These notes are the readable proof the record lacks. The notes' matroid view (Prop. 3.6) and the Boolean-algebra case (L(A) ≅ Bₙ for the coordinate arrangement, Ex. 1.4) touch the Boolean side of the map's row 8. The Stone-duality side (Stone 1937 in this batch; [LIT-353](../literature.d/LIT-353.md)) is not mentioned. For the oriented-matroid vocabulary (topes, covectors) the notes point only to Björner, Las Vergnas, Sturmfels, White and Ziegler, *Oriented Matroids* (ref. [7]), which the record does not hold.

## Bearing on the record

- **Map row 8 ("Xiong's regions are topes"; oriented matroids/Zaslavsky 1975; [LIT-332](../literature.d/LIT-332.md) unreachable).** This work supplies what the map needs from Zaslavsky:
  - the definition of regions;
  - the intersection poset;
  - the theorem that regions and bounded regions are counted by χ_{L(A)} at −1 and 1, and faces by Möbius values;
  - the fact that these counts depend only on L(A).
  It is the right open citation *alongside* [LIT-332](../literature.d/LIT-332.md), not instead of it for priority. It does **not** supply the word or theory of "topes". That needs an oriented-matroid source. As [NOTE-272](NOTE-272.md) and [NOTE-290](NOTE-290.md) already say, identifying ultrafilters of a Boolean algebra with the regions of a (generally non-orthogonal) arrangement is the owner's own step. The notes do give one ingredient for it: a region is fixed by its separating set (p. 89), i.e. by its side of each hyperplane. That is the "sign vector" half. They are silent on the Boolean-algebra half.
- **Corollary 2.1 bears on the owner's claims.** The number of regions is determined by the intersection lattice alone. So any claim about "concept regions" that depends only on counts can be checked from L(A) (which hyperplane subsets meet, and in what dimension) without knowing the region shapes, and any claim that depends on region shape cannot be.
- **Machine-learning practice.** None in the text. No anthology entry is warranted on these notes alone.

## Limitations

- Expository: the notes prove the core results but leave many details to exercises and "[why?]" prompts, sketch Thm 6.23, and omit the proofs of Thms 4.14 and 6.25.
- The bounded-region half of Thm 2.5 is not fully proved in the topological proof (ψ(Γ) = 1 omitted).
- No oriented matroids, covectors or topes. No complex arrangements, cohomology (Orlik–Solomon) or topology beyond Euler characteristic (these are deliberately left for later study, per the author's page).
- The version read (2006) differs from the printed 2007 chapter, and the 2020 errata list many small corrections, including a rewritten step in the proof of Lemma 2.2. Page references here are to the 2006 printed pagination.
- The notes do not cite Zaslavsky's texts, so they cannot confirm those texts' contents (see sup3).

## Open questions

- The notes list several [5] (unsolved) problems. Two have since been downgraded: unimodality of the characteristic-polynomial coefficients (Ex. 2.9, re-rated [4–], and the errata report log-concavity "now known to be true") and the general-position ball question (Ex. 1.7(e), re-rated [3]). Others are not re-rated in the errata, e.g. a bijective proof of the parking-function/forest-inversion identity (Ex. 6.4).
- For the map: to state "regions are topes" the owner needs an oriented-matroid source, and a proof that the Boolean algebra the owner has in mind has the regions (not all faces) as its atoms or ultrafilters.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The brief's "PCMI lecture notes, 2004/2007; author's page" is right in outline. The details:
  - The lectures were a series at the Park City Mathematics Institute, 12–19 July 2004 (author's page).
  - The version read is dated 26 February 2006.
  - The printed version is "An introduction to hyperplane arrangements", in *Geometric Combinatorics* (eds. E. Miller, V. Reiner, B. Sturmfels), IAS/Park City Mathematics Series vol. 13, AMS, 2007, pp. 389–496. Crossref gives DOI 10.1090/pcms/013/08, dated 2007-10-31.
  - The errata file calls it "Park City Mathematics Series, volume 14 … (2004)", which conflicts with Crossref's volume 13. I follow Crossref.
- The notes attribute Theorem 2.5 to Zaslavsky ("due to Thomas Zaslavsky in 1975", p. 19). Their bibliography has no entry for the Memoir ([LIT-332](../literature.d/LIT-332.md)) or for the Bull. AMS announcement (sup3). So the notes can stand in for the *theorem*, but they do not show what either Zaslavsky text contains.
- "Topes" (map row 8: "Xiong's regions are topes") is not a term in these notes. They use "regions", and "faces" (closures of regions intersected with flats, Def. 2.4). They show directly that regions are determined by sign data in two places: for the braid arrangement (a region is a choice of xᵢ < xⱼ or xᵢ > xⱼ for every pair, Ex. 1.3) and for graphical arrangements (regions ↔ acyclic orientations, Prop. 2.5). The general statement is only implicit, in the claim that d(R, R′) = #sep(R, R′) is a metric (p. 89). The identification of regions with topes is oriented-matroid language, and these notes do not supply it.
- The notes' second proof of the bounded-region formula (12) omits ψ(Γ) = 1 for the union Γ of bounded faces ("We will omit proving here that ψ(Γ) = 1", p. 21). They report that Zaslavsky's 1975 conjecture that Γ is star-shaped is false, while Björner and Ziegler proved Γ contractible. The first proof, by the deletion–restriction recurrence, is complete, but it leaves two "[why?]" steps to the reader.
