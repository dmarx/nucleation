---
status: Proposed
title: 'Distinctions drawn by restricted Yoneda profiles only grow as nested probe families grow: a natural isomorphism of profiles on a probe subcategory restricts to one on every subcategory of it, so objects equivalent under a larger family are equivalent under each smaller one and objects told apart at a lower budget stay apart at every higher one; an equivalence a richer regime breaks was relative to its regime, not false; and the monotonicity needs an every-probe comparison, which an averaged distortion is not'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: subcategories P₁ ⊆ P₂ of a category and two
  objects whose profiles Hom(−, A) and Hom(−, B), restricted to P₂, are
  naturally isomorphic while their restrictions to P₁ are not; or, for
  probes returning outcome laws, two objects agreeing on every probe of a
  family and differing on a probe of a subfamily. Not defeated by probe
  families that are not nested as the budget grows, which the claim
  excludes by hypothesis, nor by comparisons that are not natural
  isomorphism or agreement on every probe, such as an averaged distortion,
  which the claim names as the exception.
tags:
- mathematics
- individuation
- epistemology
date: '2026-11-05'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-264
grounds:
- THEORY-032
- THEORY-354
complements:
- CLAIM-302
- CLAIM-tmp7pv9x
uses:
- TERM-069
- TERM-065
bears_on:
- QUESTION-031
- QUESTION-tmptcuch
summary: >-
  A's proposal, from the owner's paste of 2026-11-05 (latest), A's
  "Yoneda, individuation, and resource-bounded objects" §2, merged with
  §§1 and 9 of the paste before it ("Additional points of contact across
  the Nucleation record"): resource-indexed restricted profiles
  Y_b(A) = Hom(−, A)|_{𝒫_b} over nested probe subcategories, with A's
  observation that "the reverse cannot occur", and A's reading that an
  equivalence a stronger regime breaks is "regime-relative", not false.
  The proof is one line and is given; checked by the filer on a brute-force
  search in finite sets and on random finite posets. Its guard is the
  filer's: the monotonicity holds for a comparison over every probe and
  fails for a normalized average, as for the probe-weighted distortion
  [QUESTION-031](../questions.d/QUESTION-031.md) sets aside. The wording is A's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmp7bxc0 CLAIM-tmp7pv9x CLAIM-tmpxcbet TERM-088 — Proposed; A's proposals of 2026-11-05 and the entries filed beside them, and the record's open term for the senses of individuation, cited as filed, nothing here resting on their being settled -->
<!-- inactive-ok-file: CLAIM-tmp42yq0 CLAIM-tmpq06t8 — Proposed or new; entries of 2026-11-05 from A's fourth paste and the assistant, cited as open -->

# CLAIM-tmpg7w69: Distinctions drawn by restricted Yoneda profiles only grow as nested probe families grow: a natural isomorphism of profiles on a probe subcategory restricts to one on every subcategory of it, so objects equivalent under a larger family are equivalent under each smaller one and objects told apart at a lower budget stay apart at every higher one; an equivalence a richer regime breaks was relative to its regime, not false; and the monotonicity needs an every-probe comparison, which an averaged distortion is not

## The claim

A ("Yoneda, individuation, and resource-bounded objects", §2): "Let 𝒫_b
denote a subcategory of the probes or interaction contexts accessible
under that bound", and "In a first, idealized version, define
Y_b(A)= Hom_𝒞(−,A) |_{𝒫_b}." "As the available budget increases, the
repertoire of probes may expand: 𝒫_{b_1} ⊆ 𝒫_{b_2} (b_1 ≤ b_2)." Two
objects may have isomorphic profiles at b₁ and not at b₂, and "Assuming
the probe categories are nested and comparison uses natural isomorphism,
the reverse cannot occur: a natural isomorphism on a larger probe category
restricts to one on a smaller category." A names the concept it yields:
"Resource-relative descriptive individuation: the distinctions between
objects supported by the interactions available under a declared resource
regime."

**The proof.** Let P₁ ⊆ P₂ be subcategories of 𝒞, full or not, and let
α : Hom(−, A)|_{P₂} ⇒ Hom(−, B)|_{P₂} be a natural isomorphism. Its
components α_P, for P in P₁, are bijections, and the naturality square for
each morphism g of P₁ is one of the squares α already satisfies, since g
is a morphism of P₂. So α|_{P₁} is a natural isomorphism. Contrapositively,
if the profiles on P₁ are not isomorphic, no isomorphism on P₂ exists. With
budgets b₁ ⪯ b₂ and 𝒫_{b₁} ⊆ 𝒫_{b₂}: an equivalence found at b₂ holds at
b₁, and a distinction found at b₁ survives at b₂. Raising the budget can
only split classes.

The same holds, more simply, for [TERM-069](../terms.d/TERM-069.md)'s observational equivalence,
agreement of outcome laws on every probe of a family: agreement on a
family is agreement on each of its subfamilies.

**Checked** by the filer with python3 -I. In the category of finite sets of
sizes 0 to 3 with all functions, a brute-force search over families of
bijections found, for 27 pairs of objects and nested probe families, no
natural isomorphism on the larger family without one on the smaller. On
3,000 random posets of seven elements, where a profile is the set of
probes below an object, 63,000 comparisons of nested families of four and
two probes gave no pair equal on the larger and split on the smaller, and
15,206 pairs equal on the smaller and split on the larger. The smallest
instance: p ≤ A, p ≤ B and q ≤ A. On the probes {p} the profiles of A and
B agree; on {p, q} they do not.

**What it says about regime-relative equivalence.** A (the paste before,
§9): "At one scale, two systems may appear to belong to the same class. At
a more powerful intervention or observation scale, the equivalence may
break. That does not necessarily make the earlier equivalence false. It
makes it regime-relative." The proof says why, when regimes are nested:
the earlier equivalence still holds of the smaller family, and the larger
family only refines it. The record's instances run one way:

- **Access.** In [THEORY-354](../theory.d/THEORY-354.md), oracle access "simulates sample access with
  one query", so the sample-access tests are a subfamily of the oracle
  tests at the same size. A predictor indistinguishable from nature under
  oracle access is so under sample access; the converse fails, under the
  hardness assumptions [THEORY-354](../theory.d/THEORY-354.md) states.
- **Feasibility.** [CLAIM-302](CLAIM-302.md)'s efficient tests are a subfamily of all
  tests; equivalence under all is equivalence under the efficient, and
  not conversely.
- **Restriction.** [CLAIM-264](CLAIM-264.md): agreement on a restricted family can fall
  short of isomorphism, and a dense family restores full faithfulness.
  This claim adds the order between: along a chain of families, the
  classes only split.

So A's (§1 of the paste before) "Equivalence at one resource scale need
not survive at a more demanding scale" and "A claim that two systems share
a universality class must declare what it preserves" have a definite form
for nested regimes: the class is a class of the declared family, and a
richer family can only split it. This is [TERM-065](../terms.d/TERM-065.md)'s regime with its
probes ordered, and [CLAIM-152](CLAIM-152.md)'s relativity to a target with the targets
nested. [CLAIM-tmp7pv9x](CLAIM-tmp7pv9x.md) is the same shape on the side of demands: an
implication valid at a budget is valid at every lower one.

## What it does not say

- **That the families are nested.** A's assumption. If a larger budget
  buys some probes by giving up others, as when a measurement disturbs
  what a later one would see, the families are not nested and
  distinctions can be lost as well as gained.
- **That every comparison is monotone.** The proof needs agreement on
  every probe. A comparison by average is not monotone: with tolerance
  ε = 0.6, a pair whose distortion is 1 on probe p₁ is told apart under
  {p₁}, and adding a probe p₂ on which the distortion is 0 makes the mean
  0.5 and the pair equivalent under {p₁, p₂}. The supremum stays 1. A
  normalized probe-weighted distortion, which [QUESTION-031](../questions.d/QUESTION-031.md) notes "is not
  a Yoneda construction", can therefore lose a distinction as probes are
  added.
- **That the profile is resource-bounded in its morphisms.** Y_b keeps the
  whole hom-sets from the affordable probes. A's own complication (§2):
  "simply deleting all morphisms that exceed a fixed cumulative budget
  generally does not yield an ordinary presheaf closed under
  precomposition", which is [CLAIM-tmp7bxc0](CLAIM-tmp7bxc0.md)'s closure condition b ⊗ b ⪯ b.
  The cost-retaining version is an enrichment, as in [CLAIM-tmpxcbet](CLAIM-tmpxcbet.md).
- **More than descriptive individuation.** A: "The categorical
  construction addresses the first of these directly. It might help
  investigate the others, but it does not automatically establish them",
  the others being [TERM-088](../terms.d/TERM-088.md)'s dynamical, constitutive and organizational
  senses. Nor does a profile, at any budget, show that relations
  constitute the object ([THEORY-032](../theory.d/THEORY-032.md)'s presupposition; [CLAIM-150](CLAIM-150.md)).
- **That the classes are known.** That a chain of families only refines
  says nothing about where it stops, or whether it reaches isomorphism;
  that is [CLAIM-264](CLAIM-264.md)'s density condition and [QUESTION-031](../questions.d/QUESTION-031.md)'s open question.

## Note of 2026-11-05: A's fourth paste, and the assistant's contributions

[CLAIM-tmp42yq0](CLAIM-tmp42yq0.md) pairs this result with its opposite for acting: under peak costs and reversible moves, the classes of what can be turned into one another only merge as the acting budget grows ([CLAIM-tmpq06t8](CLAIM-tmpq06t8.md)). The observing budget here and the acting budget there index one system's budgeted individuation together. No status changes.
