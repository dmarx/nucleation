---
status: Read
paper: LIT-1927
title: 'Bourrat — Endogenization of scaffolded properties (2022)'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read in full, for LEAD-176, from the author's accepted manuscript
    on his own site, https://pierrickbourrat.github.io/publication/a-36/a-36.pdf
    (HTTP 200, fetched 2026-11-22; every page headed "This is the author's
    accepted manuscript without copyediting, formatting, or final
    corrections", copyright 2022 BSPS). All eight sections, the three
    figures' captions and Table 1 were read; the reference list was used
    only to resolve citations. The NetLogo supplement was not run. The
    manuscript has no page numbers, so sections stand in for pages. The
    printed version (BJPS 76(2): 269-294, 2025) was not compared. Quotes
    were checked against the text extracted with pdftotext.
date: '2026-11-22'
summary: >-
  Bourrat grades collective properties as pseudo-Darwinian (an observer's
  grouping), Darwinian-like (produced by external, ecological mechanisms)
  and Darwinian (produced by internal mechanisms that give resilience to
  perturbation), and holds that a transition in individuality is complete
  only when scaffolded properties are endogenized. An agent-based model
  with a pleiotropic trait (low growth rate, stickiness, patch defence)
  shows collectives that keep their scaffolded low growth rate after
  between-patch migration is reopened, for small propagule timescale T and
  small patch capacity S, and revert for large ones. The release lifts one
  component of the scaffold; the patches, their capacity and the periodic
  propagule generations stay.
---
<!-- inactive-ok-file: LIT-1940 — Unfetched; the model this paper extends, restated in its §4 -->
<!-- inactive-ok-file: LIT-188 THEORY-418 — Proposed; the paper that cites this one, and its reading -->

# NOTE-tmp1shj8: Bourrat — Endogenization of scaffolded properties (2022)

## Contribution

A criterion and a model. The criterion adds to Lewontin's three
conditions a condition on their source: a collective is a Darwinian
individual only when internal individuating mechanisms produce the three
conditions, and the mark of that is resilience to perturbation, graded
by its range. The model extends the ecological scaffolding model of
LIT-1940 (Black, Bourrat and Rainey 2020) with a pleiotropy that couples
a cell's growth rate to its dispersal and to its patch's resistance to
invasion, and shows, by simulation, collectives whose scaffolded
property outlasts the removal of the scaffold under some parameters.

## Key insight

Being imposed and being produced are told apart by an intervention on
the imposing structure: lift the scaffold and see whether the
collective-level properties survive. Collectives that pass are
Darwinian; collectives that collapse back to free-living cells were only
Darwinian-like. The step from one to the other is "endogenization": an
internal trait (here, pleiotropic stickiness) comes to do what the
external structure did (keep cells from migrating between patches).

## Assumptions

- Patches of perishable, limited resources on a 20 × 10 torus of 200
  patches; a patch dies if over-exploited (capacity S cells) or if its
  resources reach age 30 cell generations; an empty patch is replenished
  (§5).
- A cell's growth rate is its genotype, a float in [0, 2]; mutations
  shift it by 1 % of the maximum; mutations are small, so no high-growth
  mutant arises in one step (§5, footnote 13).
- Pleiotropy: high growth rate means high probability of leaving the
  patch and low resistance to invaders; low growth rate means stickiness
  (§5). "One realizer ... could be cells producing glue", after the
  wrinkly spreader (§5).
- Every T-th generation is different "due to some periodic environmental
  changes": no ordinary replication or movement, but one cell per patch
  with stickiness above 1.5 (growth rate below 0.5) may found a
  neighbouring patch as a propagule (§5). This rule holds in all three
  regimes.
- The scaffold is the ban on between-patch migration except at
  propagule generations. In the "reverted" regime it holds for 1500 cell
  generations and is then lifted for the rest of a 30,000-generation run
  (§5).
- T runs from 3 to 10 and S from 4 to 20 in steps of two, 72 conditions
  per regime. The number of repeats is misprinted ("Each condition is
  repeated 01 times", §5).

## Key results

- **Three grades of collective property** (§2, Table 1).
  Pseudo-Darwinian: "only due to an observer's choice"; Darwinian-like:
  "due to external (that is, ecological) individuating mechanisms";
  Darwinian: "due to internal individuating mechanisms that provide the
  entity some resilience to perturbations". "The broader the range of
  perturbations an entity can sustain, the higher its score on
  individuality" (§2).
- **Against Clarke** (§2): Clarke admits external individuating
  mechanisms; Bourrat holds that the mechanisms "have to be internalized
  or endogenized for an ETI to be genuine", for two reasons: external
  mechanisms may not solve the cross-level by-product problem, and
  without internal mechanisms a small environmental change dissolves the
  collectives. Footnote 7: external stability would need coupling to
  internal properties that control it, which "would de facto render the
  mechanism (at least partly) internal".
- **Black et al.'s collectives are Darwinian-like** (§4). Their
  bottleneck (policing) and patch boundary (demarcation) "are purely
  external to the collective"; the model "can be regarded as a way of
  initiating the ETI". It does solve the by-product problem, since cells
  interact through the patch's resources. Lift its scaffold and "the
  collectives would quickly disappear".
- **No scaffold** (§6.1): growth rate goes to the maximum (about 2) in
  every condition.
- **Scaffold** (§6.2): growth rate falls below 0.3 in most conditions;
  non-viable when T is over eight and S under ten.
- **Reverted** (§6.3, Figure 3c): for T not too long and S not too
  large, growth rate stays below 0.5 after the scaffold is lifted;
  otherwise it reverts to the no-scaffold value, more slowly the smaller
  T and the larger S (T = 9, S = 12 would take more than 30,000
  generations). The explanation offered: a low-growth cell does better
  long-term by staying for a propagule than by growing and
  over-exploiting its patch, and the cost of mutating through
  intermediate growth rates keeps it there.
- **Status of the result** (§6.3, §7): "The model and analysis provided
  here are preliminary"; the claim that Darwinian-like properties have
  become Darwinian rests on "indications (although this would require
  further investigation)".
- **Niche construction** (§7): a scaffold could be "initiated by the
  lower level entities themselves", as dead cells or waste forming a
  barrier around a patch, which could later become "an integral part of
  the collective" as an extracellular matrix or a shell has.
- **Vagueness** (§7): how much resilience suffices "accept[s] no definite
  answer"; resilience to every perturbation "sets too high a bar"; a
  single large mutation would still dissolve the evolved collectives,
  and policing mechanisms are the next step.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Lewontin's conditions do not pick out real collectives; a condition on their source is needed | moderate | argument from arbitrary groupings and by-products (§2) |
| C2 | A transition is complete only when scaffolded properties are endogenized, tested by resilience to removing the scaffold | interpretive | definition, motivated by two reasons (§2) |
| C3 | Pleiotropy between growth rate and dispersal can endogenize the scaffold for small T and S | weak to moderate | one agent-based model, repeats misprinted, called preliminary (§6) |
| C4 | Internal and external are relative, and niche construction can make a scaffold that becomes part of the collective | weak | thought experiment (§7) |

## Concepts

- **Ecological scaffold**: "a structure in the environment" imposed on
  lower-level entities that gives collectives Darwinian-like properties
  (abstract, §4).
- **Endogenization**: a process, not an explanatory strategy (footnote 1):
  collectives acquire internal mechanisms that keep the scaffolded
  properties when the scaffold is removed.
- **Darwinian-like / Darwinian / pseudo-Darwinian**: Table 1, above.
- **Internalist / externalist explanation**: after Godfrey-Smith, by
  which properties "make a difference", internal or external; "The
  distinction between internalism and externalism is relative" (§3).

## Connections

It extends LIT-1940, restating that model's setting and results in §4
(the record holds LIT-1940 Unfetched). It takes Clarke's individuating
mechanisms (demarcation and policing) and departs from her by requiring
them internal. It compares itself with Libby et al.'s ratcheting
(§7). The same group's 2024 paper (LIT-tmp6nn9d, read in NOTE-tmpculbo)
restates the endogenization puzzle as a two-peaked fitness landscape and
develops the niche-construction route of §7. Griesemer and Shavit
(LIT-188) build on it and move endogenization into the community.

## Bearing on the record

- **The release test needs a declared inside and outside, and the paper
  declares them** (the question LIT-1927's standing put). The candidate
  collective is the patch's cells; "internal" is the cells' genotype;
  "external" is the migration ban. Releasing the scaffold lifts that ban
  only: patches, their capacity S, perishing resources and the
  "periodic environmental changes" that make every T-th generation a
  propagule generation all stay outside the collective and all stay on.
  Endogenization here is relative to one component of the scaffold, and
  the propagule cycle the collectives depend on is still supplied from
  outside. Bourrat concedes the relativity (§3, §7).
- **CLAIM-529** (corroborated): the release criterion is stated on the
  cells' traits and the collective's response to an intervention on its
  environment, applies to a patch grouping not presupposed to be an
  individual, and its verdict comes out false where T or S is large.
- **CLAIM-194** (a parallel): Black et al.'s collectives have real
  interaction among members, mediated by resources, and still have their
  boundary maintained from outside. A criterion that reads interaction
  alone would pass them. Bourrat's own criterion is an intervention on
  the imposing structure, not a coupling measure.
- **CLAIM-522** (consistent): the test that separates imposed from
  internal is an intervention on the mechanism, relative to a declared
  boundary, not a perturbation of state.
- **CLAIM-531** (background): the model's endogenized collectives
  persist without the migration ban but not without the outside supply
  of the propagule cycle; nothing in it is generative entrenchment.
- **QUESTION-398**: a worked answer for one model. The organization
  becomes independent of the intervention that established it when the
  long-term return of staying for a propagule beats growing and leaving,
  which holds for small T and S.
- **THEORY-418**, LIT-188's reading: Griesemer and Shavit's report of
  this paper is accurate as far as it goes. The paper calls
  Darwinian-like individuality "imposed" by an external scaffold and
  makes resilience, graded, the mark of endogenization.

## Limitations

- One stochastic model, results from heatmaps of the last 500
  generations, the number of repeats misprinted; "preliminary" by the
  author's own word.
- Endogenization is shown against one perturbation (lifting the
  migration ban) and only for small mutations; a single large mutation
  would undo it (§7).
- The propagule rule depends on a periodic environment the release
  leaves in place, so the collectives' reproduction is still scaffolded
  after "removal". The paper does not say so.
- Gap in the argument: "internal" is the cells' genotype, so the
  resilience criterion credits the collective with a mechanism that is a
  property of each cell. The paper does not argue that a cell-level
  pleiotropy is a collective-level individuating mechanism.
- How much resilience makes a property Darwinian is left vague by
  design.

## Open questions

Does the same endogenization survive when the periodic propagule
environment is also lifted? Can the niche-constructed scaffold of §7 be
modelled so that the boundary the collectives depend on is produced by
them from the start?
