---
number: 829
status: Skimmed
formerly:
- NOTE-tmp8nk93
paper: LIT-259
title: 'Jorgensen & Tian — Noncommutative Analysis (GNS, RKHS)'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    A close reading of the passages the record cites, from the arXiv v8
    PDF (arxiv.org/pdf/1408.1164, 442 pp.), text extracted with
    pdftotext. Read closely: §1.4 from Exercise 1.32 to Remark 1.42
    (pp. 30–34); Ch. 3, the proof of the spectral theorem, Lemmas
    3.27–3.31 (pp. 105–107); Ch. 4, the chapter opening through Lemma 4.37
    and Theorem 4.41 (pp. 123–135), and §4.7 through Example 4.87
    (pp. 156–157); Ch. 5's opening (pp. 184–185); Ch. 11's opening
    through Theorem 11.12 (pp. 333–339); Exercise 6.8. Read in outline:
    the preface and table of contents. The rest of the book was not
    read, so this is a Skimmed note. Page numbers are the arXiv v8's.
date: '2026-10-14'
summary: >-
  The book calls the kernel-to-Hilbert-space construction "the GNS
  construction" (Remark 1.34) and states that minimal realizations
  ϕ(x,y) = ⟨Φ(x), Φ(y)⟩ are unique up to a unitary (Cor. 1.35). It does not
  prove the corollary; the proof is "left as an exercise". The parallel
  uniqueness for states and cyclic representations is proved (Thm 4.35),
  and the argument transfers. The commutative GNS space L²(μ) is written
  out explicitly (Ex. 4.86, Lemma 3.28).
---
<!-- inactive-ok-file: THEORY-005 THEORY-009 — Proposed; the accounts that cite this book or bear on its Riesz passage -->

# NOTE-829: Jorgensen & Tian — Noncommutative Analysis (GNS, RKHS)

## Contribution

A graduate text in operator theory, organized around the link between
states, the representations they induce, and the algebras those generate.
Its chapters run from Hilbert-space basics and the spectral theorem
through GNS, completely positive maps, Brownian motion, unitary
representations, Kadison–Singer, self-adjoint extensions and graph
Laplacians, to reproducing-kernel Hilbert spaces. For this record it puts
the kernel construction and the GNS construction side by side, under one
name, in one book.

## Skim

*Close reading of the cited passages only; see the history entry for what
was and was not read.*

- **Remark 1.34 (p. 30).** "An extremely useful method to build Hilbert
  spaces is the GNS construction. For details, see Chapter 4."
  - Start from ϕ: X × X → C positive definite on an arbitrary set X. Put
    the form ⟨Σc_xδ_x, Σd_yδ_y⟩_ϕ := Σ c̄_x d_y ϕ(x,y) on finite sums,
    quotient by N = {f: ⟨f,f⟩_ϕ = 0} (a subspace by Schwarz, (1.18)), and
    complete.
  - This is the Moore–Aronszajn construction. Chapter 4's GNS is the same
    recipe applied to (a,b) ↦ ϕ(a*b) on a *-algebra. The book names the
    first after the second without stating a reduction between them.
- **Corollary 1.35 (p. 31).**
  - ϕ is positive definite iff there are a Hilbert space H and Φ: X → H
    with ϕ(x,y) = ⟨Φ(x), Φ(y)⟩_H (1.22). H is "minimal" if
    H = span{Φ(x)} (1.23), where "span" is the closed linear span, as the
    book defines it in Def. 1.43.
  - For two minimal solutions there is a unitary U: H₁ → H₂ with, as
    printed, "UΦ₁(x) = Φ₂(x) U" (1.24). Φ₂(x) is a vector, so the trailing
    U is a typo for UΦ₁(x) = Φ₂(x).
  - **Proof, in full:** "These conclusions follow from Remark 1.34, and
    the definitions. (The missing details are left as an exercise to the
    student.)" The uniqueness clause is stated, not proved.
- **The missing proof, supplied here (the record's, not the book's).**
  Define U on finite sums by UΣc_xΦ₁(x) := Σc_xΦ₂(x). Then
  ‖Σc_xΦ₂(x)‖² = Σc̄_x c_y ϕ(x,y) = ‖Σc_xΦ₁(x)‖². So U is well defined
  (it kills exactly the null combinations) and isometric. It extends to
  the closed span, which is H₁ by minimality, and its range is dense in
  H₂ by minimality of H₂ and closed, so U is unitary. This is word for
  word the book's proof of uniqueness in Theorem 4.35, with π_i(A)u_i
  replaced by Φ_i(x).
- **Remark 1.36 (p. 31).** H may be chosen as L²(Ω, F, P) for a
  probability space depending on ϕ. Stated without proof. Example 1.37:
  ϕ(s,t) = s ∧ t gives Brownian motion on Wiener space. Exercise 1.41
  applies Corollary 1.35 to (A,B) ↦ μ(A ∩ B) to build white noise and the
  Itō isometry.
- **Theorem 4.6 / 4.35, GNS (pp. 126, 133–134).** A bijection between
  states ϕ on a unital *-algebra and cyclic representations (π, H, u),
  ‖u‖ = 1, with ϕ(A) = ⟨u, π(A)u⟩, unique up to unitary equivalence.
  - Uniqueness is proved. W: π₁(A)u₁ ↦ π₂(A)u₂ is isometric because
    ‖π_i(A)u_i‖² = ϕ(A*A), and extends "by density" to a unitary with
    π₂W = Wπ₁.
  - Existence: H_ϕ = completion of A/{A: ϕ(A*A) = 0}, u = [1], π(A)[B] =
    [AB]. Lemma 4.37 shows the null set is a left ideal; the book says
    "two-sided", which is more than Schwarz gives. Remaining details are
    Exercise 4.39.
- **Remark 4.8.** S(A) is convex and weak*-compact; ϕ is pure iff π_ϕ is
  irreducible; a state decomposes over pure states. Stated.
- **Example 4.28 (p. 131).** For A = C(X), X compact Hausdorff,
  f ↦ ∫f dμ is a state, and "in the abelian case, all states are Borel
  probability measures. Because of this example, we say that the GNS
  construction is non-commutative measure theory." The converse is
  Riesz–Markov, cited, not proved here.
- **Example 4.86 (p. 156).** The explicit commutative GNS: for the state
  s_μ(a) = ∫a dμ on C(X), "The GNS construction gives H = L²(μ)", π(f)
  is multiplication by f, the cyclic vector is 1, and
  s_μ(f) = ⟨Ω, π(f)Ω⟩ = ∫f dμ, "the expectation of f in case μ is a
  probability measure".
- **Lemma 3.28 (pp. 105–106).** The same identification inside the proof
  of the spectral theorem. For a bounded self-adjoint A and a vector u,
  w_u(f) = ⟨u, f(A)u⟩ is a state on C(K), K = [−‖A‖, ‖A‖]. "By Riesz"
  there is μ_u, and W: f(A)u ↦ f is a unitary from the cyclic subspace
  onto L²(K, μ_u) intertwining A with multiplication by t (Lemma 3.29).
  This is Nelson's route: "selfadjoint operators → cyclic representation
  of function algebra → measure µ → L²(µ)" (p. 105).
- **Example 4.29 / Exercise 4.30 (pp. 131–132).** On the group algebra
  C[G], ϕ(g) = δ_(g,e) extends to a trace state with ϕ(A*A) = Σ|A_g|².
- **Def. 11.1 and Claim 11.2 (pp. 333–334).** H is an S-RKHS if
  evaluation E_s is continuous, "i.e., by Riesz, there is a K_s ∈ H such
  that h(s) = ⟨K_s, h⟩". Claim 11.2, proved: K_s = E_s*(1).
- **Theorem 11.10, Kolmogorov (p. 338).** c: G → C is positive definite
  iff it is the covariance of a stationary, mean-zero Gaussian process.
  Only the easy direction is proved; the other is cited to [PS75].
- **Ch. 5 opening (pp. 184–185).** Stinespring's theorem is presented as
  GNS for operator-valued completely positive maps.

## Claims

Not filled: this note is Skimmed, and only a Read note may fill in a
claims table.

## Concepts

- **Positive definite function on a set.** ϕ: X × X → C with
  Σc̄_ic_jϕ(x_i,x_j) ≥ 0 for every finite system. A kernel, in the record's
  usage.
- **Minimal realization.** Φ: X → H with ϕ = ⟨Φ(·), Φ(·)⟩ and the Φ(x)
  spanning a dense subspace.
- **State.** A linear functional ϕ on a unital *-algebra with ϕ(1) = 1 and
  ϕ(A*A) ≥ 0.
- **Cyclic representation.** (π, H, u) with π(A)u dense in H.
- **"GNS construction."** Used in this book both for states on algebras
  (Ch. 4) and, by name, for positive definite functions on sets
  (Remark 1.34).

## Connections

The kernel construction is Aronszajn's, and the RKHS chain Riesz → K_s
matches Muandet et al.'s Def. 2.4 and Prop. 2.1 ([LIT-260](../literature.d/LIT-260.md)). The GNS
construction goes back to Gelfand & Naimark ([LIT-313](../literature.d/LIT-313.md)), read in [NOTE-303](NOTE-303.md),
which finds no uniqueness statement for kernel realizations there either.
The spectral-theorem proof follows Nelson [Nel69]. Stinespring's theorem
(Ch. 5) is the operator-valued generalization of Chapter 4.

## Bearing on the record

- **[THEORY-004](../theory.d/THEORY-004.md): the remaining clause of promote_when.**
  - **What the clause asks.** "A close reading of ... Jorgensen & Tian's
    Cor. 1.35, which the book leaves partly as an exercise. ... What
    remains is the close reading of Jorgensen & Tian ([LIT-259](../literature.d/LIT-259.md))."
  - **Met: the close reading.** Remark 1.34, Corollary 1.35, Remark 1.36,
    Example 4.28 and the GNS theorem have now been read closely.
  - **Not met by the book: a confirmed proof.** The corollary's proof is
    entirely "left as an exercise", not "partly". So the reading cannot
    confirm Corollary 1.35 from the book's own proof, because there is
    none.
  - **Met another way.** The uniqueness argument is supplied above. It is
    the book's proved argument for Theorem 4.35, transferred. Whether that
    satisfies the clause is for whoever promotes [THEORY-004](../theory.d/THEORY-004.md) to decide.
  - **Corrections to [THEORY-004](../theory.d/THEORY-004.md).**
    - Its summary says the book proves "its minimal realizations unique
      up to a unitary", and its body says the book "prove[s]" it. Both
      should say "states".
    - Equation (1.24) as printed carries a typo.
    - The book's corollary is over complex Hilbert spaces with a unitary.
      [THEORY-004](../theory.d/THEORY-004.md) applies it to real representation matrices with an
      orthogonal map. The real case follows by the same argument, but the
      book does not state it.
    - For an n × d representation whose rows do not span R^d, the
      realization is not minimal in the book's sense. Orthogonal
      equivalence then needs the extra step of extending the isometry
      across the complement, which [LIT-250](../literature.d/LIT-250.md) §5.3 states as known.
- **[THEORY-005](../theory.d/THEORY-005.md): a better citation for the L²(p) identification.**
  - [THEORY-005](../theory.d/THEORY-005.md) calls "L²(p) is the commutative GNS space" the record's
    inference from Remark 1.34 and Example 4.28. Example 4.86 states it
    outright for C(X): H = L²(μ), multiplication representation, cyclic
    vector 1, state = expectation. Lemma 3.28 does the same inside the
    spectral theorem.
  - Both are for a compact X (or a compact spectrum K). The positive-pair
    spaces of [THEORY-005](../theory.d/THEORY-005.md) are often R^d, where the book's passages read
    say nothing. The locally compact version is standard but not shown
    here.
- **[THEORY-009](../theory.d/THEORY-009.md).** Def. 11.1 says what [THEORY-009](../theory.d/THEORY-009.md) says Riesz is for:
  bounded evaluation gives K_s "by Riesz", and Claim 11.2 writes it as
  E_s*(1), an adjoint. Nothing in the passages read uses Riesz to obtain
  self-adjointness of an integral operator.
- **The GNS name is an analogy, not a theorem, in this book.** Remark
  1.34 applies the GNS recipe to a kernel on a set, which has no algebra
  and no representation. The two coincide literally for a positive
  definite function c(g⁻¹h) on a group, through the group algebra C[G].
  The book gives the ingredients (Example 4.29, Theorem 11.10) but does
  not state that coincidence. Any account that leans on "the kernel
  construction is GNS" leans on a naming.
- No instruction for machine-learning practice; nothing for the anthology.

## Open questions

- Is there a source that states the kernel construction as a GNS
  representation in the strict sense, for example as the GNS of a state
  on the *-algebra generated by the kernel sections or by multipliers
  (Def. 11.7)? That would turn the naming into a theorem.
- The L²(Ω,F,P) choice of Remark 1.36 (a Gaussian process with covariance
  ϕ) is a second, probabilistic realization of the same kernel. Does it
  bear on [THEORY-004](../theory.d/THEORY-004.md)'s reading of representations as realizations?
