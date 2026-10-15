---
number: 264
status: Proposed
formerly:
- CLAIM-tmp5bgh5
title: Two objects can agree on every probe in a restricted family without
  being isomorphic, so equivalence under a probe family is coarser than identity
  unless the family is rich enough, and only probes chosen independently of
  the comparison and evaluated on held-out cases are evidence that structure
  was preserved
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: Split from CLAIM-142 under ADR-040, at the owner's request ("go ahead
    with the group B splits"). The assistant restated the general content
    without the premises about translation that CLAIM-142 rests on; CLAIM-142
    now rests on this claim.
role: thesis
warrant: demonstrated
defeated_if: A probe family fixed in advance, not chosen for the comparison
  at hand and not dense or strongly generating, that is shown to separate
  every pair of non-isomorphic objects in a class of interest. Or an argument
  that agreement under probes chosen to make two objects agree is as good
  evidence of shared structure as agreement under independently chosen, held-out
  probes.
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
  The exact half: the restricted Yoneda functor is fully faithful exactly
  when the probe family is dense, and reflects isomorphisms when it is a strong
  generator; otherwise it identifies only up to a coarser equivalence. Matching
  every probe''s marginal leaves the joint unconstrained. The evidential half:
  a family chosen to make two objects look alike is weak evidence that they
  share structure.'
supports:
- CLAIM-142
- CLAIM-190
- CLAIM-187
complements:
- CLAIM-302
---
<!-- inactive-ok-file: CLAIM-046 CLAIM-142 CLAIM-187 CLAIM-190 CLAIM-193 QUESTION-031 — Proposed; cited for what each holds or applies, open, not settled -->

# CLAIM-264: Two objects can agree on every probe in a restricted family without being isomorphic, so equivalence under a probe family is coarser than identity unless the family is rich enough, and only probes chosen independently of the comparison and evaluated on held-out cases are evidence that structure was preserved

## The claim

**The exact half.** Restrict an object's profile to a family 𝒬 of probes,
A ↦ Hom(−, A)|_𝒬. This functor is fully faithful exactly when 𝒬 is dense,
as the one-point set is in Set. When 𝒬 is only a strong generator, in a
category with finite limits, it reflects isomorphisms without capturing
all morphisms, as ℤ does in groups. Any other family identifies objects
only up to an equivalence coarser than isomorphism. [THEORY-032](../theory.d/THEORY-032.md) adds three
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

**The evidential half.** Agreement under a probe family is evidence of
shared structure only to the degree that the family was chosen
independently of the comparison and is evaluated on cases it was not
chosen on. A family selected to make two objects look alike shows that it
can be selected.

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
