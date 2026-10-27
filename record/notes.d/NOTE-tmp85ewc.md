---
status: Read
paper: LIT-1568
title: 'Morris, Lenski & Zinser — The Black Queen Hypothesis'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the PubMed Central copy of the version of record
    (PMC3315703, CC BY-NC-SA), fetched on 2026-10-27 as full-text XML
    through the Europe PMC REST service and converted to text. Read: the
    abstract, the untitled opening, "The Black Queen Hypothesis" with
    equations 1–3, "The BQH applied to other microbial functions", "Are
    beneficiaries 'cheaters'?", "Shooting the moon", the conclusion, and
    the caption of Figure 1. The supplemental tree methods and the
    references were not read. The worked numbers in the formal section
    were recomputed here (below). It is an Opinion/Hypothesis article:
    one phylogenetic figure, no new experiment.
date: '2026-10-27'
summary: >-
  Proposes that in free-living microbes, losing a costly function whose
  product leaks to neighbours is favoured by ordinary individual
  selection, and the loss runs until the remaining producers ("helpers")
  just supply the community, leaving most cells ("beneficiaries")
  dependent on a rare few. No relatedness, cooperation or collective is
  needed, only leakiness and frequency dependence. The one worked case is
  the loss of catalase-peroxidase (katG) in Prochlorococcus, which cannot
  survive the hydrogen peroxide that its community removes. The other
  cases are suggestions.
---
<!-- inactive-ok-file: THEORY-tmp20e6b — Proposed; filed from this reading -->
<!-- inactive-ok-file: QUESTION-277 LIT-1570 LIT-1225 THEORY-141 — Open, Deferred or Proposed; the question, works and account this reading is set beside, nothing here rests on them -->

# NOTE-tmp85ewc: Morris, Lenski & Zinser — The Black Queen Hypothesis

## Contribution

It names and formalizes a route to metabolic dependency in which
selection is the cause, not drift. Before it, genome reduction was
explained mainly for endosymbionts, by drift in small, bottlenecked
populations. Prochlorococcus and "Candidatus Pelagibacter" have reduced
genomes and huge populations, so drift cannot be the cause there. The
paper explains how selection on individuals produces dependence. It also
says why the dependence stops short of losing the function from the
community.

## Key insight

A function is a candidate for loss when it is costly and **leaky**, so
that performing it "inevitably benefits other cells in their vicinity".
Hydrogen peroxide (HOOH) crosses membranes about as easily as water, so
any cell that detoxifies its own interior also lowers the peroxide
outside. A cell that stops doing this saves resources and still gets the
protection, as long as enough others keep doing it. The advantage is
frequency dependent. When helpers become rare enough, the public good
falls until "the benefit of any further loss is negated by its cost".
The result looks like a division of labour, but "in fact this
bifurcation arises through classic Darwinian selection acting on
individuals". The helpers are "passive players", in the paper's words
"perhaps the unlucky ones that were the slowest to change".

## Assumptions

- **Free-living, well-mixed populations** for the basic argument. Spatial
  structure is discussed and set aside as not changing "the fundamental
  possibility".
- **The benefit of loss is a resource saving.** B is the fractional
  reduction in the cell quota of a limiting resource, and it raises the
  growth rate proportionally.
- **Linear response.** Growth rises linearly with the effective rate of
  the function between zero and the rate that allows maximal growth
  (equation 3). The authors say "the general conclusions should still
  hold with more complex interactions". This is asserted, not shown.
- **Large effective population size**, so that selection, not drift,
  governs loss.
- **That katG was ancestral and lost.** This is inferred from gene–species
  tree discordance and the clade's monophyly (Figure 1). The paper calls
  the losses "the simplest explanation".

## Key results

- **The katG case.** No sequenced Prochlorococcus genome has katG. Most
  Synechococcus genomes do, and their KatG proteins are monophyletic, so
  the gene was lost in several lineages, including all of Prochlorococcus
  (Figure 1). Axenic Prochlorococcus is killed by sunlit filtered seawater
  within hours, and in nature co-occurring cells act as a peroxide sink
  (references 17 and 28, not read here). "Ca. Pelagibacter ubique" also
  lacks catalase.
- **Benefit (equation 1).** B = (Q_A − Q_M)/Q_A, where Q is the cell quota
  of the limiting resource for the ancestor (A) and the mutant (M). For
  katG the saving is about 0.2% of cellular iron.
- **Speed.** With B = 0.002 and one doubling a day (μ ≈ 0.69 per day), the
  mutant gains at about 0.0014 per day. In a global population of about
  10²⁵ cells, it would reach 99% "in fewer than 125 years". Recomputed
  here, with the population taken as 10⁴ cells per ml over 10 m of depth
  across a quarter of the Earth's surface:
  - the population is ≈1.3 × 10²⁵ cells;
  - going from one cell to 99% needs a change in log-odds of
    ln(99) + ln(1.3 × 10²⁵) ≈ 62.4;
  - at 0.00138 per day that takes about 45,200 days, or 124 years.

  The figure holds. It treats the mutant's advantage as constant all the
  way to 99%, while the paper's own frequency dependence would slow it.
- **Cost (equations 2–3).** The effective rate is
  k = k₀ + Σᵢ Nᵢ Lᵢ kᵢ, the cell's own rate plus everyone's rate weighted
  by density N and leakiness L. The cost of loss is
  C = (k_M − k)(μ_M − μ₀)/(μ_M k_M), which is (k_M − k)/k_M when the
  mutant cannot grow alone. This follows from the linear assumption, and
  was re-derived here. A loss-of-function mutant invades when B > C.
- **Outcomes.** Against its ancestor alone, the mutant spreads until the
  ancestor's density gives both equal growth: helper and beneficiary
  coexist on one limiting resource. In a mixed community where unrelated
  species supply the good, the mutant drives its ancestor extinct. Loss
  then "will proceed in every species in the community until B is less
  than or equal to C for all individuals".
- **Not kin selection.** Hamilton's rule asks whether a producer's cost is
  repaid through relatives (rB > C). The Black Queen asks whether a
  non-producer's saving outweighs its loss of protection, "without regard
  to the relationship between the producer and user".
- **Not necessarily cheating.** Beneficiaries harm helpers only if both
  are limited by the same resource. Prochlorococcus and its heterotrophic
  helpers are on different trophic levels, and the heterotrophs may depend
  on Prochlorococcus for carbon. So the outcome can be commensal or
  mutualistic.
- **"Shooting the moon."** Since B is a fraction of the remaining quota,
  each loss makes the next saving of the same size proportionally larger
  for a beneficiary. Loss should therefore accelerate in beneficiary
  lineages and not in helpers. The predicted community is many
  streamlined beneficiaries and a few helpers, which become rare but
  indispensable "keystone species". This is the paper's speculation, as
  it says.
- **Other candidates, all suggestions.** Nitrogen fixation (less than 1%
  of marine cyanobacteria are diazotrophs), siderophores, Pelagibacter's
  loss of sulfate reduction and dependence on DMSP, and biofilm matrix.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Loss of a costly, leaky function can be favoured by individual selection, and stops short of community-wide loss by frequency dependence | strong as a model result | equations 1–3; it follows from the definitions once leakiness and a resource saving are granted |
| C2 | Prochlorococcus lost katG adaptively, protected by a peroxide-removing community | moderate | gene absence and phylogeny (Figure 1), the cited sensitivity and sink experiments; the size of the benefit (0.2% iron) is computed, not measured as fitness |
| C3 | The genome reduction of Prochlorococcus and Pelagibacter is selected, not drifted | moderate | effective population sizes far beyond any experiment; argued, not tested here |
| C4 | Nitrogen fixation, siderophores, sulfur assimilation and biofilm matrix are lost by the same process | weak | fit to the four criteria; no analysis |
| C5 | Loss accelerates in beneficiaries, so communities polarize into many beneficiaries and few helpers that become keystone species | weak | a property of equation 1's ratio, with "all else equal"; offered as speculation |
| C6 | Beneficiaries are cheaters only when they share the helpers' limiting resource | moderate as an argument | the definitions of cheating and of the interaction |

## Concepts

- **Leaky function**: a function some of whose product becomes a public
  good available to other cells. L, the leakiness coefficient, is the
  share of activity that does so.
- **Helper / beneficiary**: a cell that still performs the function, and
  one that has lost it and depends on helpers.
- **Black Queen function**: a function that is costly to perform and yet
  indispensable to someone in the community, like the queen of spades
  in Hearts, which nobody wants and the game cannot be played without.
- **Streamlining**: genome and metabolic reduction that lowers the
  resource cost of making a cell.
- **Shooting the moon**: a lineage passively becoming a helper for many
  functions, with "job security" from the community's dependence.

## Connections

The paper sets itself against the Red Queen (antagonistic coevolution)
and Hamilton's rule (kin-selected production of public goods). It relies
on earlier work for the drift account of symbiont reduction (its
reference 9) and for experimental evolution with *Salmonella*
bottlenecks and *E. coli* deletions (references 10–12), none read here.
[LIT-1570](../literature.d/LIT-1570.md) (Athreya, Czuppon & Gokhale), read in [NOTE-tmp5hcss](NOTE-tmp5hcss.md), cites it
as the understood route to mutual dependence. It groups it with
"environment-induced redundancy" as a driver of symbiont genome reduction
other than the Red King effect. [LIT-1225](../literature.d/LIT-1225.md) (Cooper & West, unread) models
extreme specialization within a group, where helpers are selected as
helpers. Here helpers are a by-product.

## Bearing on the record

- **[QUESTION-277](../questions.d/QUESTION-277.md), the first route.** The reading confirms what the
  question said of this route, and sharpens it. Dependence arises with no
  collective at all: there is no co-transmission, no host and no shared
  fate. The dependence is directional, from beneficiaries to helpers, and
  helpers need not depend on beneficiaries. Function is distributed across
  the community's genomes (G). Reproductive cohesion (R) and regulatory
  control (C) are absent by construction. So of the question's five
  dimensions, the route moves D (one-way) and G, and none of the others.
  That is the clearest case in the record of dependence without
  individuality. The inference is mine.
- **The scope correction in the curation entry of 2026-10-27 stands.** The
  hypothesis is stated for free-living organisms, and the paper credits
  drift for endosymbiont reduction. Applying it to endosymbionts is
  [LIT-1570](../literature.d/LIT-1570.md)'s move ("environment-induced redundancy"), not this paper's.
- **[CLAIM-060](../claims.d/CLAIM-060.md).** The conclusion says the division of labour "is often to
  the advantage of all". Its own cheater section allows the opposite when
  helpers and beneficiaries share a limiting resource. So whether the
  community gains is contingent, which is consistent with [CLAIM-060](../claims.d/CLAIM-060.md)'s
  thesis that the whole's success and its members' welfare come apart.
  This is a further instance, not a ground. The comparison is mine.
- **[THEORY-141](../theory.d/THEORY-141.md).** Its condition for a stable collective, that selection
  between collectives trump selection within, does not apply here,
  because no collective is formed. The Black Queen is a case of
  interdependence that the transitions framework does not cover.
- Filed as [THEORY-tmp20e6b](../theory.d/THEORY-tmp20e6b.md). No instruction for machine-learning practice.

## Limitations

- **One worked case.** Everything general rests on katG. The fitness
  benefit is an iron-quota calculation, not a measured selection
  coefficient, and the peroxide sink is cited, not shown.
- **Linearity is assumed.** Equation 3's closed form, and the claim that
  the conclusions survive nonlinearity, are not demonstrated.
- **Constant advantage in the speed estimate.** The 125-year sweep ignores
  the frequency dependence the hypothesis itself requires. It is an upper
  bound on speed, not a prediction.
- **Ancestral state.** That katG was present and lost is the "simplest
  explanation" of the tree. Horizontal gain into Synechococcus is not
  excluded by the paper's argument.
- **The generalizations are untested.** The four other functions are
  matched to criteria, not analysed.
- **Selection versus drift is argued from population size alone**,
  without the dN/dS evidence the paper cites for symbionts.

## Open questions

- Has a Black Queen loss been reproduced experimentally, invading and
  then stopping at the frequency equations 2–3 predict? [LIT-1570](../literature.d/LIT-1570.md) cites
  D'Souza and Kost (2016) for metabolic dependency evolving quickly in
  experiment. That paper is not in the record.
- Does "shooting the moon" happen? The prediction is that
  helper-for-many-functions lineages are rare keystone taxa, and that
  beneficiary genomes keep shrinking faster.
- Where the beneficiary does become an endosymbiont, does the Black Queen
  start the reduction and drift finish it? The paper does not say, and
  [QUESTION-277](../questions.d/QUESTION-277.md)'s routes may run in sequence.
