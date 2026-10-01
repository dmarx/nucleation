---
status: Active
status_note: 'read in full 2026-10-01 ([NOTE-tmpz02gq](../notes.d/NOTE-tmpz02gq.md)); worth reading as the one-volume statement of the Döring–Isham topos programme. It is, by the authors'' own account (p. 14), "partly an amalgam" of papers I–IV ([LIT-343](LIT-343.md), [LIT-335](LIT-335.md), [LIT-299](LIT-299.md), [LIT-310](LIT-310.md)), with corrections and some new material. The new material is the value of a quantity in a pseudo-state and the inverse-image link between L(S) and PL(S) (§§8.5–8.8, Thm 8.6), the algebra of the candidate quantity-value objects (§9.3), the Boolean-subalgebra base category (§5.5.3), Kochen–Specker as a lifting obstruction (§6.6), and a long speculative §14–15. It adds no new no-go result. Its proofs are as sketchy as the series'' at the same places: Sub_cl(Σ) is Heyting (Thm 16.1) with ⇒ left unwritten, and ι : O → P_clΣ natural and monic is left to the reader. A reader who has read I–IV gains only §§8.5–8.8, 9.3 and 14; a reader new to the programme should start here.'
title: "'What is a Thing?': Topos Theory in the Foundations of Physics"
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (full text of arXiv:0803.0417 v1, 4 Mar 2008, the only
    arXiv version, 212 pp. from the arXiv PDF; text extracted with
    PyMuPDF). I read the abstract, §1 (introduction and overview), §2
    (conceptual background), §§3–4 (PL(S) and L(S)), §5 (spectral
    presheaf, outer and inner daseinisation, Sub_cl(Σ), the Bl(H) base
    category), §6 (truth objects, pseudo-states, P_clΣ, the lifting view of
    Kochen–Specker), §7 (daseinisation of self-adjoint operators, de Groote
    presheaves), §8 (sp(Â)^⪰, ℝ^⪰, ℝ^↔, observable and antonymous
    functions, values in a pseudo-state, inverse images), §9 (k(ℝ^⪰) and
    ℝ^↔/≡), §10 (unitaries), §§11–13 (the category Sys and its topos
    realisations, classical and quantum), §14 (characteristic properties
    of Σ_φ, R_φ and truth objects), §15 (conclusion) and Appendix 1
    (Thms 16.1–16.2, the k-construction, bounded variation, squares). Of
    Appendix 2, the textbook introduction to topos theory, §§17.1–17.2
    were read and §17.3 skimmed; the 73 references were sampled, not read
    through. I checked the proofs the paper gives for Thms 5.1, 5.4, 7.1,
    8.1, 8.4–8.6, 16.2 and Lemma 13.1 against the definitions. The
    published version (Lecture Notes in Physics 813, Springer 2010, pp.
    753–937, DOI 10.1007/978-3-642-12821-9_13) was not seen. Not held in
    the Anthology of the SOTA: a grep of its literature.d for the arXiv
    id, "Döring" and "topos" found nothing. `published:` is the arXiv v1
    date.
tags:
- quantum-foundations
- contextuality
- mathematics
- logic
- philosophy-of-science
- mereology
date: '2026-10-01'
published: '2008-03-04'
arxiv: '0803.0417'
doi: '10.1007/978-3-642-12821-9_13'
first_author: 'Döring'
keywords:
- 'topos theory'
- 'neo-realism'
- 'daseinisation'
- 'spectral presheaf'
- 'truth objects'
- 'quantity-value object'
- 'category of systems'
- 'quantum gravity'
implementations: []
summary: >-
  Döring & Isham (2008), arXiv:0803.0417. A 212-page restatement of the
  topos programme of papers I–IV. A theory of a system S is a
  representation of a typed language L(S) in a topos. In quantum theory
  the topos is presheaves on the poset V(H) of abelian von Neumann
  subalgebras, propositions are clopen sub-objects of the spectral
  presheaf Σ via daseinisation, a pure state gives sieve-valued truth
  values ν(A ε Δ; ψ)_V = {V′ ⊆ V | ⟨ψ|δ(Ê[A∈Δ])_{V′}|ψ⟩ = 1}, and each
  bounded self-adjoint Â becomes an arrow Σ → ℝ^↔ whose values are
  monotone intervals over subcontexts. Classical physics fits its axioms
  for composite systems exactly; quantum theory fits the disjoint sum but
  not the tensor-product composite.
---

# LIT-tmpcerv7: 'What is a Thing?': Topos Theory in the Foundations of Physics

Andreas Döring, Chris Isham (2008), *arXiv preprint, v1 only; published in B. Coecke (ed.), New Structures for Physics, Lecture Notes in Physics 813, Springer 2010, pp. 753–937* — arXiv:0803.0417

## Standing in the record

Filed on 2026-10-01 at the owner's request. It came from the anthology's
issue 180 revisit pass (https://github.com/dmarx/anthology-of-the-sota/issues/180):
the owner opened it in his reading feed on three separate days and said it
belongs in nucleation. No anthology topic can hold it, and it is not held
there. `published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

The record already holds the four Journal of Mathematical Physics papers
this one amalgamates, each read in full: the programme and its languages
([LIT-343](LIT-343.md)), daseinisation and truth objects ([LIT-335](LIT-335.md)), the quantity-value
presheaves ([LIT-299](LIT-299.md)), and the category of systems ([LIT-310](LIT-310.md)). It also holds
the paper the programme grew from, Isham and Butterfield's
generalized-valuation reformulation of Kochen–Specker ([LIT-325](LIT-325.md)), and
Kochen and Specker themselves ([LIT-298](LIT-298.md)). The sheaf-theoretic account of
contextuality in Abramsky and Brandenburger ([LIT-016](LIT-016.md)) is the other
"no global section" line in the record; this paper predates it and does
not engage it. Arsiwalla's pregeometry essay ([LIT-102](LIT-102.md)) points readers to
this programme as the worked formal-language approach.

[NOTE-tmpz02gq](../notes.d/NOTE-tmpz02gq.md) is the close reading of 2026-10-01, and it placed the work:
**Active**. It is the place to read the Döring–Isham programme in one sitting,
and it is the reference most later work cites for it. As mathematics it
adds little to papers I–IV. Its new results are the inverse-image
corollary tying PL(S) to L(S) (Thm 8.6, Cor 8.7), the value of a quantity
in a pseudo-state (§8.5), and the algebra of the quantity-value candidates
(§9.3). It also restates Kochen–Specker as an obstruction to lifting a
pseudo-state (§6.6). The rest is the series again. That includes the
series' gaps: the Heyting structure on Sub_cl(Σ) is sketched, not proved
(Thm 16.1), so this paper does not meet the promotion condition of
[THEORY-037](../theory.d/THEORY-037.md). §14–15 are speculation, and the authors say so (fn. 131).
