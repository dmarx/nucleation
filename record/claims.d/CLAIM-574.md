---
number: 574
status: Active
formerly:
- CLAIM-tmpg7w69
title: 'Distinctions drawn by restricted Yoneda profiles only grow as nested probe families grow: a natural isomorphism of profiles on a probe subcategory restricts to one on every subcategory of it, so objects equivalent under a larger family are equivalent under each smaller one and objects told apart at a lower budget stay apart at every higher one; an equivalence a richer regime breaks was relative to its regime, not false; and the monotonicity needs an every-probe comparison, which an averaged distortion is not'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the status review of 2026-11-06, at the status review's
    ruling (the owner delegated these rulings), under ADR-057's four
    criteria. Its premises CLAIM-264, THEORY-032, TERM-069 and TERM-065 are
    Active, no objection is filed, and nothing in the record meets its
    defeater: the DNA origami readings of 2026-11-05 bear on whether
    physical probe families are nested, which the claim takes as its
    hypothesis. The reviewer rechecked the one-line proof and the
    averaged-distortion counterexample step by step. THEORY-354 moved from
    grounds to corroborated_by (ADR-058): the body cites its access result
    as one of the record's instances, and the proof does not use it.
- version: 3
  date: '2026-11-10'
  note: >-
    Carries pragmatic-transport as well, at the sweep of ADR-085's
    rule (2026-11-10): the entry takes part in that line's argument,
    through the first line of an entry it names:
    pragmatic-transport, since it bears on QUESTION-031. No other
    change.
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
- pragmatic-transport
rests_on:
- CLAIM-264
grounds:
- THEORY-032
complements:
- CLAIM-302
- CLAIM-564
- CLAIM-590
uses:
- TERM-069
- TERM-065
bears_on:
- QUESTION-031
- QUESTION-393
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

# CLAIM-574: Distinctions drawn by restricted Yoneda profiles only grow as nested probe families grow: a natural isomorphism of profiles on a probe subcategory restricts to one on every subcategory of it, so objects equivalent under a larger family are equivalent under each smaller one and objects told apart at a lower budget stay apart at every higher one; an equivalence a richer regime breaks was relative to its regime, not false; and the monotonicity needs an every-probe comparison, which an averaged distortion is not

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
nested. [CLAIM-564](CLAIM-564.md) is the same shape on the side of demands: an
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
  precomposition", which is [CLAIM-563](CLAIM-563.md)'s closure condition b ⊗ b ⪯ b.
  The cost-retaining version is an enrichment, as in [CLAIM-590](CLAIM-590.md).
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

[CLAIM-557](CLAIM-557.md) pairs this result with its opposite for acting: under peak costs and reversible moves, the classes of what can be turned into one another only merge as the acting budget grows ([CLAIM-581](CLAIM-581.md)). The observing budget here and the acting budget there index one system's budgeted individuation together. No status changes.

## Note of 2026-11-05: the DNA origami readings

Read on the owner's request to connect the record's realizability inquiry to DNA origami; the works were chosen by the assistant.

**Rothemund, "Folding DNA to create nanoscale shapes and patterns".** Rothemund (2006), [LIT-2120](../literature.d/LIT-2120.md), read in [NOTE-1631](../notes.d/NOTE-1631.md), qualifies the claim's applicability to
physical probes. Its hypothesis takes nested, non-invasive probes; in AFM the stronger probe, sharp
tips and hard tapping, resolves single missing staples, yet "repeated scanning created holes
difficult to distinguish from holes due to missing strands". A larger observing budget can
manufacture distinctions as well as reveal them.

**Wagenbauer, Wachauf and Dietz, "Quantifying quality in DNA self-assembly".** Wagenbauer, Wachauf and Dietz (2014), [LIT-2128](../literature.d/LIT-2128.md), read in [NOTE-1637](../notes.d/NOTE-1637.md), support refinement
within a chain and qualify nesting by cost. Gel mobility and TEM averages merge 0, 5 and 15 missing
staples; a cheap defect label splits them down to about 10 bases; cryo-EM, far costlier, "might be
able to resolve site-specific defects, but it will be blind to stochastically distributed defects".
The probes are not nested by cost, which the claim's hypothesis needs.

**Majikes et al., "Revealing thermodynamics of DNA origami folding via affine transformations".** Majikes et al. (2020), [LIT-2117](../literature.d/LIT-2117.md), give a physical instance of distinctions that only grow as the probe family grows. Melting temperature, the coarsest probe, already separates the scaffolds of different persistence length. The finer derived quantities (ΔH, ΔS, ΔCp) resolve only the short persistence-length scaffold, because uncertainty "propagates aggressively through the van’t Hoff analysis". Adding a domain-specific reporter separates what bulk probes merge. The paper leaves open any formal statement of the nesting.

No status changes.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Majikes, Hasni, Haridas, Robertson, Pintar, Zwolak and Liddle, "Complex cooperativity in DNA origami revealed via design-dependent defectivity".** Majikes et al. (2026), [LIT-2127](../literature.d/LIT-2127.md), support the claim at the level of example. They state that "yield measurements have an inverse relationship between their resolution and both their cost and throughput", from gels to AFM to DNA-PAINT. Their AFM classes are "a very approximate substitute" for staple counts. The cheaper probe is not a coarsening of the dearer one:
- The gel merges a damaged design with well-folded ones.
- It also splits well-folded designs by mobility.

This bears on CLAIM-574's nesting of probe families. No probe costs are quantified.

No status changes.

## Note of 2026-11-07: set beside [CLAIM-455](CLAIM-455.md), from the second share of "Individuation, Possibility, and Disposition"

A58 §10 sets this claim beside [CLAIM-455](CLAIM-455.md): "But greater representational detail does not automatically mean greater usable legibility for a bounded observer, as [CLAIM-455](CLAIM-455.md) demonstrates." The two vary different things. This claim enlarges the probe family. [CLAIM-455](CLAIM-455.md) fixes the observer's rules and changes the representation. Read together, distinctions grow with the probe family, and legibility grows with the observer's rule class, since a best risk over a larger class can only fall. Neither grows with the representation's refinement under a fixed bounded class. The probes bound what any observer they feed can make legible, which is [TERM-064](../terms.d/TERM-064.md)'s ceiling. No status changes.
