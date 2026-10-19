---
number: 264
status: Active
formerly:
- CLAIM-tmp5bgh5
title: 'Two objects can agree on every probe in a restricted family without being isomorphic, so equivalence under a probe family is coarser than identity unless the family is rich enough'
version: 2
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-142 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-142 rests on; CLAIM-142
    now rests on this claim.
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected, then promoted from Proposed to Active at the owner's
    direction, from the owner's promotion audit of 2026-10-19, which asked
    for a final check of the density and strong-generator statements
    first. The check found one wrong. The body said a strong generator
    reflects isomorphisms and that any other family identifies objects
    only up to a coarser equivalence, which implied that a strong
    generator identifies objects. It does not: it makes the restricted
    functor conservative, so a morphism the probes cannot tell from an
    isomorphism is one, but two objects with isomorphic profiles need not
    be isomorphic. (ℤ/p)³ and the Heisenberg group mod p, for p odd, are
    the counterexample now in the body. Nor does identifying objects
    require density. The leftover evidential half, which CLAIM-322 has
    held since 2026-10-15, is removed from the body and the summary. The
    defeat condition is restated for a demonstrated claim. With the
    evidential half gone, the claim is cited results and the record's
    counterexamples, all checked.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in a cited result (density as full faithfulness of the restricted
  Yoneda functor; a strong generator as conservativity in a category with
  finite limits; Cramér–Wold; Lovász's homomorphism counts) or in one of the
  record's counterexamples: (ℤ/p)³ and the Heisenberg group mod p through ℤ,
  and distributions that agree on every probe's marginal and differ.
tags:
- mathematics
- epistemology
- individuation
date: '2026-10-13'
line:
- formal-apparatus
grounds:
- THEORY-032
- LIT-221
summary: 'The general content of [CLAIM-142](CLAIM-142.md), filed alone under [ADR-040](../decisions.d/ADR-040.md) so that
  it does not rest on [CLAIM-046](CLAIM-046.md) and [CLAIM-011](CLAIM-011.md), which are about pragmatic identity.
  The restricted Yoneda functor is fully faithful exactly when the probe
  family is dense. A strong generator makes it conservative, which is weaker:
  a morphism the probes see as invertible is invertible, but objects with
  isomorphic profiles need not be isomorphic. Matching every probe''s marginal
  leaves the joint unconstrained. The evidential rule is [CLAIM-322](CLAIM-322.md)''s.'
supports:
- CLAIM-142
- CLAIM-190
- CLAIM-187
- CLAIM-322
complements:
- CLAIM-302
---
<!-- inactive-ok-file: CLAIM-046 CLAIM-142 CLAIM-187 CLAIM-190 CLAIM-193 QUESTION-031 — Proposed; cited for what each holds or applies, open, not settled -->
<!-- inactive-ok-file: CLAIM-322 — Proposed; the evidential half split from this claim, named as where it now lives, not leaned on -->

# CLAIM-264: Two objects can agree on every probe in a restricted family without being isomorphic, so equivalence under a probe family is coarser than identity unless the family is rich enough

## The claim

Restrict an object's profile to a full subcategory 𝒬 of probes,
A ↦ Hom(−, A)|_𝒬. Three things can be asked of this functor, and they come
apart.

- **It is fully faithful exactly when 𝒬 is dense**, as the one-point set is
  in Set. Then objects with isomorphic profiles are isomorphic, and every
  map of profiles comes from a unique morphism.
- **In a category with finite limits, it is conservative exactly when 𝒬 is
  a strong generator** in Kelly's sense, as ℤ is in groups. Conservative
  means a morphism f: A → B is an isomorphism when every Hom(Q, f) is a
  bijection. It says
  nothing about two objects whose profiles are isomorphic by a map that no
  morphism induces. Through ℤ, a group's profile is its underlying set with
  the power maps g ↦ gⁿ. For p an odd prime, (ℤ/p)³ and the Heisenberg group
  of 3 × 3 upper unitriangular matrices over ℤ/p both have order p³ and
  exponent p. Choosing a generator of each of their (p³ − 1)/(p − 1)
  subgroups of order p and sending gᵏ to hᵏ gives a bijection that commutes
  with every power map, so the profiles are isomorphic, and one group is
  abelian and the other is not.
- **When 𝒬 is not a strong generator** in such a category, the functor is
  not conservative: some morphism that is not an isomorphism induces a
  bijection on every probe.

Identifying objects up to isomorphism does not need density. In
finite-dimensional vector spaces over a finite field, the field alone is
not dense, yet its profile, the underlying set with scalar multiplication,
has qⁿ elements and so fixes the dimension. Whether a given family is rich
enough is a question about the family and the class of objects, which is why the claim says only that
agreement can fall short of isomorphism. [THEORY-032](../theory.d/THEORY-032.md) adds three
conditions from the nLab reading ([LIT-221](../literature.d/LIT-221.md)). The identifying profile is the
hom-functor with its action by composition, not a table of hom-sets. The
lemma needs identities. And it presupposes the objects it identifies.

The same holds for distributions read through probes.
(φ_i)#P = (φ_i)#Q for every i does not in general imply P = Q, since
matching each probe's marginal leaves the joint across probes
unconstrained. A rich enough family does separate: all one-dimensional
linear projections determine a distribution (Cramér–Wold). For finite
relational structures, homomorphism counts from every finite structure
determine isomorphism (Lovász).

The rule for reading agreement under a probe family as evidence of shared
structure is [CLAIM-322](CLAIM-322.md)'s, split from this claim on 2026-10-15.

## Where the record applies it

[CLAIM-142](CLAIM-142.md) applies it to communicative realizations, with a realist reading
of communicative identity ([CLAIM-046](CLAIM-046.md)) and the remedy of anchored
correspondences ([CLAIM-011](CLAIM-011.md)). [CLAIM-190](CLAIM-190.md) applies it to the anchoring measures
of a record. [CLAIM-193](CLAIM-193.md) and [CLAIM-187](CLAIM-187.md) apply its relativity to learned
representations. Each keeps its own premises for the application.

## What it does not say

- It does not say any particular domain has a category whose objects the
  probes approximate. That is a premise of each application.
- It does not say which probes to choose, or when a family is rich enough
  for a task ([QUESTION-031](../questions.d/QUESTION-031.md)).
- It says nothing about contextuality: being representable and having a
  global section are independent.

## Note of 2026-10-15: a restriction forced by feasibility

A15 of the exchange of 2026-10-14 (workbench entry of 2026-10-15)
recommended amending this claim with computationally bounded probes. The
result is filed apart, as [CLAIM-302](CLAIM-302.md), because it is conditional on an assumption
this claim does not need: if pseudorandom generators exist, there are
distributions almost disjoint in total variation that no efficient test
tells apart. "Computational indistinguishability gives it a non-arbitrary
source of restricted observational families: feasibility." This claim's
restricted families are chosen; [CLAIM-302](CLAIM-302.md)'s is imposed by the observer's
resources.

It bears on [TERM-037](../terms.d/TERM-037.md), an observable as "a reproducible elicitation or
coding procedure". A15: "For computational observers, the procedure
includes a computation." The term is not revised. Equivalence under
feasible probes is relative to the encoding and to any auxiliary
information, as this claim's evidential half would predict. The status is
unchanged.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s full classification found this claim compound: its exact half
(the restricted Yoneda functor, Cramér–Wold, marginals) is demonstrated,
and its evidential half, that only probes chosen independently of the
comparison and evaluated on held-out cases are evidence that structure was
preserved, is interpretive. The evidential half is now [CLAIM-322](CLAIM-322.md) (interpretive),
which rests on this claim. This claim keeps the exact half and stays
demonstrated. Its title, which stated the evidential half, is shortened to
the exact half, and the second disjunct of its defeat condition, about
chosen probes, moves to [CLAIM-322](CLAIM-322.md).
