---
status: Read
paper: 'LIT-tmp17vtr'
title: 'The Genetical Evolution of Social Behaviour. I'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the Journal of Theoretical Biology typeset text, 7(1):
    1–16, from the University of Vermont course-archive copy,
    pdodds.w3.uvm.edu/files/papers/others/1964/hamilton1964a.pdf; text
    extracted with PyMuPDF). Abstract, §§1–5 and references read. The
    extraction lost symbols in several displayed equations (δ, the °/•
    indices, some fractions); the results below are given as the prose
    states them, and the derivation of the ΔR° inequality in §2 was
    followed through the prose, not checked symbol by symbol.
date: '2026-10-02'
summary: >-
  A one-locus, non-overlapping-generation model in which genotypes affect
  relatives' fitness. Splitting each effect into a part on genes identical
  by descent (weight r) and a "diluting" part on other genes shows that the
  former alone fixes the direction of selection, and defines inclusive
  fitness. Mean inclusive fitness provably increases when no genotype
  harms others; with harm it only points uphill. A costly act spreads iff
  −k > 1/r: twice the cost to a sib, eight times to a cousin.
---

<!-- inactive-ok-file: LIT-047 — Proposed: the sixty-society test of morality-as-cooperation, placed by NOTE-034; cited for the domains it coded -->
<!-- inactive-ok-file: LIT-tmpcsgn6 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# NOTE-tmpayo8o: The Genetical Evolution of Social Behaviour. I

## Contribution

- A genetical model in which an individual's fitness is its basic unit plus
  its own genotypic effect plus the effects its neighbours' genotypes have
  on it (eq. 1), with neighbours classed by relationship (§2).
- The definition of **inclusive fitness** and the proof that, under the
  model's conditions, it plays the role classical fitness plays in the
  theorem of increasing mean fitness (§2).
- Three special cases (§3) and the threshold for altruistic and selfish
  traits (§5) that later literature calls Hamilton's rule.

## Key insight

Every effect an individual causes falls partly on genes identical by
descent with its own (in proportion r) and partly on unrelated genes. Only
the first part changes gene frequencies; the second only dilutes. So the
quantity selection maximizes is not the individual's own fitness but that
fitness plus r-weighted effects on others. Hamilton's "vivid" statement:
"no one is prepared to sacrifice his life for any single person but …
everyone will sacrifice it when he can thereby save more than two brothers,
or four half-brothers, or eight first cousins" (§5).

## Assumptions

- **Life history.** Organisms reproduce "once and for all at the end of a fixed period" (non-overlapping generations, §2).
- **Genetics.** One autosomal locus, any number of alleles; random mating from the frequency equation on (§2).
- **Relationship.** Wright's coefficient r (= c₂ + ½c₁, the expected fraction of genes identical by descent) in a non-inbred population. It is exact only for loci not under selection, so the account is "a good approximation … when selection is slow" (§2, §4).
- **Additivity.** An effect's size does not depend on the recipient's genotype or condition (§4); Hamilton calls this reasonable for giving traits and "surreptitious theft" but not for contests.
- **Not for new mutations** (§4): relatives carry the gene with probability r only after some generations.
- **Deterministic**: only expected effects are modelled.

## Key results

- **Decomposition (§2).** The total effect δT of a genotype splits as δT = δR + δS, where δR is the effect on genes i.b.d. in relatives (the inclusive fitness effect) and δS the "diluting effect". The change in allele frequency depends on the δR's; δS changes only its magnitude.
- **Increase of mean inclusive fitness (§2).** ΔR̄ > 0 is shown to hold if δS̄ ≥ 0, which holds in particular when every genotype's effects on others are non-negative. For harmful effects the change is only "aimed somewhere in the direction of a local maximum" and may overshoot.
- **Case (a), §3.** If a genotype's effects all fall on relatives of degree r′, selection progresses r′ times as fast as for the same advantage kept by the actor: a gene benefiting sibs spreads half as fast.
- **Case (b), §3.** Genes that direct giving to the nearest relatives, and taking from the most distant, are favoured. In "viscous" (non-dispersing) populations giving traits should be commonest.
- **Case (c), §3.** Pure transfers between relatives (δT = 0) are slowed by (1 − r); sib competition in a shared pool slows selection further, up to a halving for pairs.
- **The threshold (§5).** With δT = kδa, a trait costly to the actor (δa < 0) raises inclusive fitness iff −k > 1/r. A selfish trait (δa > 0, k < 0) does iff −k < 1/r. An altruistic transfer (k = −1) is never selected, and is merely neutral between clones; a selfish transfer is always selected except from a clone-mate.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under the model, selection maximizes inclusive fitness | strong for giving traits (δS̄ ≥ 0); weak for harming traits | §2 derivation; for harm only a direction is shown |
| C2 | An altruistic trait spreads iff the benefit-to-cost ratio exceeds 1/r | strong within the model's assumptions | §5 algebra from eq. (5), (7) |
| C3 | Using r for relatives other than ancestors introduces an error of unknown sign and size under selection | stated by the author as unresolved | §4: "has so far failed to reach any definite general conclusions" |
| C4 | Viscous populations should show the most developed giving traits | moderate (qualitative) | §3(b); random mating is unlikely to hold there, which the author flags |
| C5 | Alarm calls are probably favoured because the risk to the caller is small and the benefit to a nearby bird much larger | assertion | §5 illustration, no data |

## Concepts

- **Inclusive fitness** — the fitness an individual would show if stripped of its social environment's harms and benefits, augmented by the harms and benefits it causes to neighbours, each weighted by the coefficient of relationship (§2).
- **Diluting effect** — the part of a genotype's total effect that falls on genes not identical by descent; it leaves gene-frequency direction unchanged.
- **Giving trait / taking trait** — δT positive or negative.
- **Viscous population** — one in which individuals stay near their birthplace, so neighbours tend to be relatives.

## Connections

- **Its sequel** ([LIT-tmpfgxhl](../literature.d/LIT-tmpfgxhl.md), read in [NOTE-tmps4v89](NOTE-tmps4v89.md)) states the principle for general use and applies it to warning behaviour, social insects, clones and fights.
- **Haldane 1955** is credited in Part II, not here, with the drowning-child version of the argument; this paper cites Haldane (1923) only for sib competition.
- **Trivers 1971** ([LIT-tmppstp9](../literature.d/LIT-tmppstp9.md)) takes this model as the explanation of kin altruism and builds reciprocal altruism for the cases where "kin selection can be ruled out". Axelrod & Hamilton 1981 ([LIT-tmp6z0ji](../literature.d/LIT-tmp6z0ji.md)) use it to get cooperation started from all-defection. Nowak 2006 ([LIT-tmpbmh7b](../literature.d/LIT-tmpbmh7b.md)) gives it as the first of five mechanisms, as r > c/b.
- **Morality-as-cooperation.** Curry 2016 ([LIT-tmpcsgn6](../literature.d/LIT-tmpcsgn6.md)) cites "Hamilton, 1964" for the kin domain, and [NOTE-034](NOTE-034.md) lists kin selection first in the lineage of the sixty-society test ([LIT-047](../literature.d/LIT-047.md)).

## Bearing on the record

- **Kin domain.** The model gives a selective reason to treat relatives preferentially, and to discriminate by degree of relationship (§3b). That is the biological content of MAC's "family" domain. It does not predict that kin-directed behaviour is *moralized*; the step from "favoured by selection" to "judged good" is MAC's own, and [LIT-047](../literature.d/LIT-047.md)'s design could not test it ([NOTE-034](NOTE-034.md)).
- **No other MAC domain** is grounded here. Contests, exchange and possession are absent; §4 mentions competition only as a case the model handles badly.
- **No THEORY is indicated.** No instruction for ML practice.

## Limitations

- **Narrow model.** Non-overlapping generations, one locus, random mating, weak selection; Hamilton defers the general case to Part II and calls Part II's generalization "unrigorous".
- **The metric of relationship** is approximate under selection, and the author could not bound the error (§4).
- **Harmful traits.** The maximization result is proved only when the total effect on others is non-negative.
- **No data.** The paper is wholly theoretical; evidence is left to Part II.

## Open questions

- How large is the error from using r for collateral relatives when the gene is under selection (§4)?
- Does the maximization principle extend to overlapping generations and to traits that harm others? Part II argues it should, without proof.

## Corrections

- none to a seeded skim (there was no seed)
- **The famous form.** The rule is not written as rb > c or r > c/b in this paper. It is −k > 1/r (§5), with k = δT°/δa. Nowak 2006 ([LIT-tmpbmh7b](../literature.d/LIT-tmpbmh7b.md)) introduces r > c/b as "Hamilton's rule" anticipated by Haldane's "two brothers or eight cousins"; the line in this paper is Hamilton's own, "more than two brothers, or four half-brothers, or eight first cousins".
- **Curry 2016's reference** ([LIT-tmpcsgn6](../literature.d/LIT-tmpcsgn6.md)) cites "Hamilton, W. D. (1964) … 7, 1–16, 17–52" with the DOI of Part II only (…90039-6); Part I is …90038-4.
