---
status: Active
title: "In a one-locus model with non-overlapping generations, random mating and weak selection, gene frequencies change as if each individual maximized its inclusive fitness, so a trait that costs its bearer spreads only if its effect on relatives exceeds 1/r times the cost; the increase of mean inclusive fitness is proved only for traits whose total effect on others is not negative"
version: 1
tags:
- natural-sciences
- mathematics
date: '2026-10-16'
source:
- LIT-497
summary: >-
  Hamilton (1964), Part I, [LIT-497](../literature.d/LIT-497.md), read in full in [NOTE-401](../notes.d/NOTE-401.md). Each effect an
  individual causes falls partly on genes identical by descent with its own
  (weight r) and partly on others, which only dilute. So selection tracks
  inclusive fitness. The threshold is written −k > 1/r (§5), not rb > c:
  "more than two brothers, or four half-brothers, or eight first cousins".
  The maximization theorem needs non-negative total effects on others; for
  harming traits the change only points uphill. r is exact only for loci not
  under selection, and Hamilton could not bound the error (§4).
extended_by:
- THEORY-tmpkifk7
- THEORY-tmpwdh1f
---

<!-- inactive-ok-file: LIT-503 — Proposed: Curry 2016, the statement of morality-as-cooperation; cited for the kin domain it credits to "Hamilton, 1964" -->

# THEORY-tmp15rjw: In a one-locus model with non-overlapping generations, random mating and weak selection, gene frequencies change as if each individual maximized its inclusive fitness, so a trait that costs its bearer spreads only if its effect on relatives exceeds 1/r times the cost; the increase of mean inclusive fitness is proved only for traits whose total effect on others is not negative

## Source

Hamilton (1964), "The Genetical Evolution of Social Behaviour. I", [LIT-497](../literature.d/LIT-497.md)
(*Journal of Theoretical Biology* 7: 1–16), read in full in [NOTE-401](../notes.d/NOTE-401.md). Some
displayed equations lost symbols in extraction; results are taken in the
form the prose states.

## What was actually shown

**The model (§2).** One autosomal locus, any number of alleles; organisms
reproduce once at the end of a fixed period; random mating; relationship
measured by Wright's coefficient r in a non-inbred population. An
individual's fitness is a basic unit plus its own genotypic effect plus the
effects of its neighbours' genotypes on it.

**The decomposition.** A genotype's total effect splits as δT = δR + δS.
δR falls on genes identical by descent in relatives and sets the direction
of gene-frequency change. δS, the "diluting effect", changes only the
magnitude. The quantity that plays classical fitness's role is therefore
inclusive fitness: own fitness stripped of the social environment's
effects, plus the effects caused on others weighted by r.

**The theorem.** Mean inclusive fitness increases if δS̄ ≥ 0, which holds
when no genotype's effects on others are negative. For harmful effects the
change is only "aimed somewhere in the direction of a local maximum".

**The threshold (§5).** With δT = kδa, a trait costly to its bearer
(δa < 0) raises inclusive fitness if and only if −k > 1/r. A selfish trait
spreads iff −k < 1/r. A pure transfer to a relative (k = −1) is never
selected.

**Special cases (§3).** A benefit placed on relatives of degree r′ spreads
r′ times as fast as one kept by the actor. Genes that give to the nearest
relatives and take from the most distant are favoured, and "viscous"
populations should show the most giving traits.

**What could have come out otherwise.** The direction of selection could
have depended on the diluting part as well. Under the model it does not.

## What this does not say

- **The rb > c form.** That is a later restatement. Nowak ([LIT-501](../literature.d/LIT-501.md)) gives it
  as r > c/b.
- **That inclusive fitness is maximized for traits that harm others.**
  Only a direction is shown.
- **That r is exact.** It is exact only for loci not under selection and
  for ancestors. Hamilton "has so far failed to reach any definite general
  conclusions" on the error (§4), and the account is "a good approximation
  … when selection is slow".
- **That it holds for new mutations.** Relatives carry the gene with
  probability r only after some generations (§4).
- **That it holds beyond the model.** Overlapping generations and general
  life histories are deferred to Part II ([LIT-506](../literature.d/LIT-506.md)), where the extension is
  called "unrigorous" ([THEORY-tmpwdh1f](THEORY-tmpwdh1f.md)).
- **Anything about morality.** The model gives a selective reason to favour
  kin by degree of relationship. That kin-directed behaviour is judged good
  is a further step this paper does not take.

## Connections

- Part II ([LIT-506](../literature.d/LIT-506.md), [THEORY-tmpwdh1f](THEORY-tmpwdh1f.md)) generalizes this and applies it.
- Axelrod & Hamilton ([LIT-498](../literature.d/LIT-498.md), [THEORY-tmpxorvn](THEORY-tmpxorvn.md)) use kinship as the route by
  which reciprocity can start from universal defection. Nowak ([LIT-501](../literature.d/LIT-501.md),
  [THEORY-tmpkifk7](THEORY-tmpkifk7.md)) lists kin selection as the first of five mechanisms.
- Trivers ([LIT-510](../literature.d/LIT-510.md), [THEORY-tmpx3n05](THEORY-tmpx3n05.md)) builds reciprocal altruism for the
  cases where kin selection "can be ruled out".
- Morality-as-cooperation cites "Hamilton, 1964" for its kin domain
  ([LIT-503](../literature.d/LIT-503.md)). Its reference gives Part II's DOI only ([NOTE-401](../notes.d/NOTE-401.md), corrections).
- The later derivation of the rule from the Price equation is not in the
  record. Luque's analysis of the Price equation ([LIT-205](../literature.d/LIT-205.md), [NOTE-101](../notes.d/NOTE-101.md)) has no
  section on Hamilton's rule.
