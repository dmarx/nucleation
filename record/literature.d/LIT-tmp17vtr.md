---
status: Active
status_note: 'read in full 2026-10-02 ([NOTE-tmpayo8o](../notes.d/NOTE-tmpayo8o.md)); worth reading as the source of inclusive fitness and of the rule the moral-psychology literature calls Hamilton''s rule. It is a population-genetic model with non-overlapping generations, random mating and weak selection, and its rule appears as −k > 1/r (§5), not in the later rb > c form. It proves that mean inclusive fitness increases only for genes whose total effect on others is non-negative (giving traits); for harming traits it shows only that selection points uphill. It says nothing about morality: it is the kin domain of morality-as-cooperation in its biological form, read as biology.'
title: 'The Genetical Evolution of Social Behaviour. I'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (the Journal of Theoretical Biology typeset text, 7(1):
    1–16, 16 pp., from the copy in Peter Dodds's course archive at the
    University of Vermont, pdodds.w3.uvm.edu/files/papers/others/1964/
    hamilton1964a.pdf; text extracted with PyMuPDF). I read the abstract,
    §§1–5 and the references. Several displayed equations lost symbols in
    extraction (the δ and ° indices, fractions); where a result depends on
    one I give it in the form the prose states. Citation checked against
    Crossref (DOI resolves; July 1964, no day). Received 13 May 1963,
    revised 24 February 1964 (p. 1). Not held in the Anthology of the SOTA
    (a grep of its literature.d for the DOI, the title and "Hamilton"
    found no such work), nor already in this record. Filed for the
    lineage of morality-as-cooperation (ADR-018).
tags:
- natural-sciences
- mathematics
date: '2026-10-02'
published: '1964-07-01'
doi: '10.1016/0022-5193(64)90038-4'
first_author: 'Hamilton'
keywords:
- 'inclusive fitness'
- 'coefficient of relationship'
- 'altruism'
- 'selfish behaviour'
- 'kin selection'
- 'viscous populations'
implementations: []
summary: >-
  Hamilton (1964), J. Theor. Biol. 7:1–16. A one-locus model in which an
  individual's genotype affects relatives' fitness. Weighting each effect
  by Wright's coefficient of relationship r gives "inclusive fitness",
  which tends to be maximized as classical fitness is. An action that
  costs the actor is favoured only if the benefit to a relative exceeds
  1/r times the cost: more than two brothers, four half-brothers or eight
  first cousins (§5). The increase of mean inclusive fitness is proved
  only for giving traits; the model is not about morality.
---

<!-- inactive-ok-file: LIT-047 — Proposed: the sixty-society test of morality-as-cooperation, placed by NOTE-034; cited for the domains it coded -->
<!-- inactive-ok-file: LIT-tmpcsgn6 — Proposed: Curry 2016, the statement of morality-as-cooperation filed in the same batch; cited for which sources it credits for each domain -->

# LIT-tmp17vtr: The Genetical Evolution of Social Behaviour. I

W. D. Hamilton (1964), *Journal of Theoretical Biology 7(1): 1–16 (received 13 May 1963, revised 24 February 1964)* — `doi:10.1016/0022-5193(64)90038-4`

## Key takeaways

- If an individual's genes affect the fitness of relatives, selection acts as though each organism maximized its *inclusive* fitness: its own fitness stripped of its social environment's effects, plus the effects it causes on others weighted by its relationship to them (§2).
- An action that lowers the actor's fitness spreads only if the ratio of benefit to cost exceeds 1/r: twice the cost for a full sib, four times for a half-sib, eight times for a first cousin (§5). A selfish action is held back only by the same weighting.
- Placing a benefit on a relative of degree r instead of on oneself slows selection by the factor r (§3a), and "viscous" populations should show the most giving traits (§3b).

## Standing in the record

Filed on 2026-10-02 at the owner's request, as one of the evolutionary
sources of morality-as-cooperation. [NOTE-034](../notes.d/NOTE-034.md), the record's reading of
Curry, Mullins & Whitehouse's sixty-society test ([LIT-047](LIT-047.md)), names
Hamilton's kin selection first in the theory's lineage, and Curry's 2016
statement of the theory ([LIT-tmpcsgn6](LIT-tmpcsgn6.md)) cites "Hamilton, 1964" for its kin
domain. Its sequel, with the applications, is [LIT-tmpfgxhl](LIT-tmpfgxhl.md).

[NOTE-tmpayo8o](../notes.d/NOTE-tmpayo8o.md) is the close reading of 2026-10-02, and it placed the work:
**Active**. It is the place the quantity "inclusive fitness" and the 1/r
threshold are first derived. What it grounds for morality-as-cooperation is
narrow and real: a selective reason to favour kin over non-kin in
proportion to relatedness, which is the kin domain ([LIT-047](LIT-047.md)'s "family").
It grounds no other domain, and it does not mention morality. The rb > c
form that later work calls Hamilton's rule is a restatement: Hamilton
writes −k > 1/r with k the ratio of the effect on neighbours to the effect
on oneself.

Two things a reader citing it should know. First, the theorem that mean
inclusive fitness increases is proved only when no genotype's total effect
on others is negative; for harming traits Hamilton says only that the
change is "aimed somewhere in the direction of a local maximum" (§2).
Second, the coefficient r is exact only for loci not under selection and
for ancestors, and Hamilton says he "has so far failed to reach any
definite general conclusions" on the error this introduces (§4). The
later derivations of the rule from the Price equation are not in the
record; Luque's analysis of the Price equation ([LIT-205](LIT-205.md)) defends the
equation against critics including Nowak and Highfield, but its reading
([NOTE-101](../notes.d/NOTE-101.md)) found that it has no section on Hamilton's rule.

**Topic.** `natural-sciences` first: it is population genetics.
`mathematics` holds the model. It is not tagged `moral-psychology`: it
says nothing about morality, moral judgement or norms, and [ADR-018](../decisions.d/ADR-018.md) keeps
the cooperation sources out of that word unless they are read as accounts
of morality.

**Anthology.** No instruction for machine-learning practice; the
anthology does not hold it.
