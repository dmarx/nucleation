---
number: 304
status: Read
formerly:
- NOTE-tmpsnlqn
paper: LIT-339
title: 'The intrinsic parity of elementary particles'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full paper, *Physical Review* 88(1), 1 October 1952,
    pp. 101–105, from the Internet Archive's scan of the issue. *Physical
    Review* issues are renewed only from July 1956, and no contribution
    renewals are on record, so this 1952 issue is in the US public domain. I
    read every page from column-cropped page images: the abstract, all four
    sections ("The possibility of indeterminate parities", "Spinors",
    "Charged fields", "Applications") and footnotes 1–10. Nothing was
    skipped. Two lines at the break between columns on p. 101 were read from
    the OCR layer.). The first NOTE on this paper, which was seeded from its
    abstract alone.
date: '2026-09-29'
summary: >-
  The paper defines a *superselection rule*: a decomposition of Hilbert
  space into orthogonal subspaces A, B, C, … between which there are no
  spontaneous transitions *and* no measurable quantities with non-zero
  matrix elements. Relative phases across subspaces, and hence relative
  parities, are then unobservable. It proves such a rule between integer
  and half-integer angular momentum, from time reversal with U_AKU_AK = +1
  and U_BKU_BK = −1. It *postulates*, without conclusive evidence, a
  charge superselection rule. The consequence is that "all Hermitean
  operators represent measurable quantities" must be abandoned.
---

# NOTE-304: The intrinsic parity of elementary particles

## Contribution

The paper targets the "more or less standard position" that every elementary particle has a definite intrinsic parity that experiment can determine (p. 101). It argues that this depends on a hidden premise, the measurability of every Hermitian operator. Dropping the premise is consistent with quantum mechanics, and in relativistic field theory it is sometimes *required*. The paper introduces and names the notion that makes this precise, the superselection rule. It proves one instance of it, proposes a second, and works out what can and cannot be said about parities under each.

## Key insight

A symmetry operator is fixed only up to a phase. If the Hilbert space splits into subspaces whose relative phases no measurement can detect, each subspace carries its *own* arbitrary phase factor ω_a, ω_b, …. Relative parities across subspaces are then undefined. Such a splitting is forced whenever some symmetry's square acts as +1 on one subspace and −1 on another. Time reversal does this for integer versus half-integer angular momentum.

## Assumptions

- **The transformation law.** A field's parity law, φ′ = IφI⁻¹, determines the unitary I up to a factor ω of modulus 1, and conversely (eqs. 1–5).
- **The phase rule.** Symmetry operators are unitary, or antiunitary (time reversal, U K with K complex conjugation). They are fixed up to a phase that is independent of the state (footnote 8, citing Wigner 1931, Appendix to ch. XX).
- **Relativistic invariance.** This is taken to include time-reversal invariance with the Kramers-type relations U_AKU_AK = 1 and U_BKU_BK = −1 (eq. 8, citing Wigner 1932).
- **The charge postulate.** Multiplying the state by e^{iαQ} "produces no physically observable modification" (p. 104). It is motivated by the global U(1) invariance of Lagrangians bilinear in φ*φ.

## Key results

- **The definition (p. 103).** A selection rule operates between subspaces if state vectors in each remain orthogonal to the others while the system is isolated. "We shall say that a superselection rule operates between subspaces if there are neither spontaneous transitions between their state vectors (i.e., if a selection rule operates between them) and if, in addition to this, there are no measurable quantities with finite matrix elements between their state vectors."
- **Equivalent descriptions (p. 102).** No measurement distinguishes F_a + F_b + F_c + … from e^{iα}F_a + e^{iβ}F_b + e^{iγ}F_c + … (eqs. 7, 7′). Any operator with matrix elements between A and B then has undefined expectation value, so it is not measurable. Equivalently, such a superposition "is not a pure state, but a statistical mixture" best described by a density matrix (citing von Neumann 1932). The system is in a pure state only if a single component is non-zero.
- **Consequence for symmetry operators (p. 103).** I has no matrix elements between sectors, and its restriction to each sector carries its own indeterminate factor ω_a. So "it will not be possible to make any statement as to the relative parity of states belonging to different subspaces."
- **What does not count (p. 103).** Linear momentum does *not* define superselection sectors: phases between different momenta are measured in every position measurement.
- **The spinor theorem (pp. 103–104).** Let A be the states of integer and B of half-integer total angular momentum. Time reversal sends f_A + f_B to ωU_AKf_A + ω′U_BKf_B, with ω′/ω independent of the state. Applying it twice gives const·(f_A − f_B), because of eq. 8 (eq. 9a). So f_A + f_B and f_A − f_B are indistinguishable, and the relative phase is unmeasurable. Hence any Hermitian ξ with matrix elements (f_A, ξf_B) ≠ 0 would lead to a contradiction, unless (f_A, ξf_B) is purely imaginary, in which case the pair f_A + if_B, f_A − if_B does the same job. So ψ + ψ* and i(ψ − ψ*) are not measurable for any spinor field ψ. The paper notes that the same result could come from rotations (2π), but "somewhat more involved" (p. 104).
- **The charge postulate (p. 104).** The state is invariant in observable content under e^{iαQ} (eq. 10). Assuming it, "the parities of states with different charges cannot be compared". For example, the data are equally compatible with a pseudoscalar or a scalar charged π-meson field, given compensating changes elsewhere.
- **Applications (pp. 104–105).**
  - The neutral π⁰'s parity is determinable, via decay to photons or selection rules in p + p → π⁰ + p + p. That the electric field is a polar vector is a convention. Footnote 9 discusses I versus CI and notes that C "is moreover still far from proved" as an exact symmetry.
  - With only the spinor rule, parities of any two spinor particles can be compared, and all spinors are uniformly "real" or uniformly "imaginary" in parity.
  - With a charge rule as well, a unit-charge particle's parity is an arbitrary modulus-1 ω. Other particles get ω or −ω, opposite charges ω⁻¹ or −ω⁻¹. One may "just as well call it 1".
  - A heavy-particle-number rule would add a further ω′. Yang–Tiomno's choice ω′ = ±1, ±i is a "slightly less general device".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The assumption that every Hermitian operator is measurable can be dropped consistently with QM and superposition | informal argument | p. 102: the transformation (7′) commutes with all linear relations, "a generalization of the ordinary multiplication of the whole vector by one phase factor" |
| C2 | Relativistic (time-reversal) invariance forces a superselection rule between integer and half-integer angular momentum | proof (given eq. 8 and state-independence of phases) | pp. 103–104, eqs. 8–9a |
| C3 | No spinor-field combination ψ+ψ*, i(ψ−ψ*) is measurable | proof, as a corollary of C2 | p. 104 |
| C4 | A superselection rule separates different total charge | conjecture / postulate | p. 104, "no conclusive evidence"; motivated by global phase invariance (eq. 10) |
| C5 | Relative intrinsic parities across sectors are conventions; within the spinor-only regime, all spinor parities share one type (real or imaginary) | argument from C2/C4 | pp. 104–105 |
| C6 | A superposition across sectors is operationally a mixture | definition-level argument | p. 102, citing von Neumann |

## Concepts

- **Selection rule.** Dynamics preserves the subspaces.
- **Superselection rule.** A selection rule plus the absence of any observable connecting the subspaces. The subspaces (not yet called "sectors" here) carry independent phases.
- **Indeterminate parity factor ω.** The residual phase freedom of the symmetry operator in each subspace.

## Connections

- **[LIT-321](../literature.d/LIT-321.md) (Haag, *Local Quantum Physics*, seeded).** The map's gloss "superselection = centre of the observable algebra" is the algebraic reformulation. The observables commute with the sector projections, which then lie in the centre of the observable algebra (the commutant structure). That formulation is not in this paper. WWW work with subspaces and matrix elements. The nearest they come is footnote 10: within one subspace I² "must be a multiple of unity".
- **[LIT-306](../literature.d/LIT-306.md) (Birkhoff–von Neumann).** BvN take every closed subspace to be an experimental proposition. WWW's superselection means that not every closed subspace (or projector) corresponds to a measurement. With superselection, the propositions are the projections of a block-diagonal algebra, and the lattice is a product of the sector lattices.
- **[THEORY-017](../theory.d/THEORY-017.md).** The Hilbert space alone does not fix what is observable. WWW is a canonical instance of the observable algebra being extra data beyond the space: the decomposition A ⊕ B is supplied by the symmetry group, not by the space.
- **[LIT-352](../literature.d/LIT-352.md) (Murota et al.).** Block-diagonalising a set of matrices finds the finest decomposition of the *-algebra they generate. For a finite family of "observables", its coarsest level (the simple components) plays the role of superselection sectors.

## Bearing on the record

- **Map row 5, "Types = superselection sectors; non-sequitur = type error / truth-value gap".** The paper supplies the concept and its operational definition. It also undercuts one half of the proposed mapping.
  - *What WWW say about cross-sector superpositions.* They are not ill-formed or truth-valueless. They are ordinary states that happen to be mixtures (p. 102). What is missing is any *observable* connecting sectors, not truth values for states.
  - *The better semantic analogue.* A cross-type predication would correspond to an operator with off-diagonal blocks. WWW say such an operator is simply not an observable, not that it yields a gap.
  - *What the owner can cite and what not.* "Category mistake = no observable across sectors" can cite WWW. "Truth-value gap" cannot be sourced here.
  - *The hedge.* The map's own hedge (soft sectors, idealisation) fits the paper's history. Of its two rules, only the spinor rule was proved, and the charge rule was a postulate.
- **Map row 6, "superselection = center".** Cite Haag ([LIT-321](../literature.d/LIT-321.md)) for the centre formulation, not WWW.
- **ML practice.** It carries nothing, and does not belong in the Anthology.

## Limitations

- **The proof leans on two things.** It needs time-reversal invariance in the form of eq. 8, and the state-independence of ω′/ω. The latter is flagged in footnote 8 as "a crucial point which … has been discussed repeatedly", with a simplified proof deferred to a later article.
- **The charge rule is unsupported by argument** beyond gauge-invariance motivation.
- **Informal in style.** There are no theorems stated as such, and the "proof" is a paragraph.

## Open questions

- Raised by the paper: whether charge (and heavy-particle number) superselection holds. Later literature, e.g. Aharonov & Susskind 1967, disputed the charge rule's necessity; that is unverified here.

## Corrections to the seeded skim

- Seeded from metadata; the text confirms the summary, with three precisions. (1) The existence of a superselection rule is *proved* only for spinor fields, i.e. integer versus half-integer total angular momentum. The one for total charge is "conjectured" in the abstract and "postulate[d]" in the text: "We can give no conclusive evidence for this assertion" (p. 104). A heavy-particle-number rule is floated as a further option (p. 105). (2) The argument is not that intrinsic parity is "not always definable" in general. It is that parities of states in different superselection sectors cannot be *compared*, so relative intrinsic parities across sectors are conventions (the indeterminate factors ω, ω′). (3) The summary's "not every self-adjoint operator is an observable" is right and is the paper's explicit moral (pp. 102–103).
- The author line and affiliations are G. C. Wick (Carnegie Institute of Technology) and A. S. Wightman and E. P. Wigner (Princeton). The paper was received 16 June 1952. Footnote 1 says it grew from Wigner's address at the International Conference on Nuclear Physics and the Physics of Elementary Particles (Chicago, September 1951), and from a review article with V. Bargmann in preparation.
