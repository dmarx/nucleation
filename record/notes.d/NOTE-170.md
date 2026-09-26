---
number: 170
status: Read
formerly:
- NOTE-tmptf0vu
paper: LIT-127
title: 'Takola & Schielzeth — Hutchinson''s niche for individuals'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text, publisher open-access PDF (CC BY), Biology &
    Philosophy 37:25, 21 pp. All sections read: Abstract, Introduction,
    "Consistent individual differences", "The ecological niche", "The
    ecological niche of individuals", the working definition, the four
    "question" sections, Conclusions, Definitions A–E, the Fig. 1–7 captions
    and declarations. The reference list was scanned. Not read: the online
    Supplementary Table S1 (36 niche definitions), which is not in the
    PDF.). Upgraded from `Skimmed` to `Read`: the claims table, assumptions
    and results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-26'
summary: >-
  The paper defines the individualized (ecological) niche as the
  environmental conditions under which a particular individual has an
  expected lifetime reproductive success of ≥ 1, counting each offspring
  as 0.5 per parent in outcrossers. The authors split it into five
  sub-concepts: realized (A), potential (B), time-slice (C), prospective
  (D) and trajectory-based (E), plus a "fundamental individualized niche"
  set aside as practically interchangeable with the potential niche. The
  individual niche has n + s dimensions, adding intraspecific axes such as
  density and morph frequency. Its boundary is the expected-LRS isocline
  of 1, which is estimable only by marginalizing fitness functions across
  individuals. The authors themselves call the concept "mostly of a
  metaphorical value".
---

# NOTE-170: Takola & Schielzeth — Hutchinson's niche for individuals

## Contribution

The paper imports Hutchinson's niche to the level of the individual in a structured way. After it, "individualized niche", used loosely in the NC3 and behavioural-ecology literature, has a working definition with an absolute-fitness boundary and five labelled sub-concepts, each paired with a quantification strategy. It identifies four problems that scaling down creates: uniqueness (no replication), time, dimensions and boundaries. It gives a partial solution to each.

## Key insight

At the population level, individuals are replicates, so a niche is a hypervolume. At the individual level, the realized niche collapses to a point, and the rest of the individual's niche is counterfactual: where it *could* have had expected LRS ≥ 1. Everything interesting about an individual niche is therefore inferred from other individuals, through repeatabilities or marginalized phenotype × environment fitness functions. The individualized niche is in practice a type-level (phenotype-class) construct presented at token level, and the authors are candid that its main value is structuring research.

## Assumptions

- **Perspective**: behavioural ecology of individually distinct animals (vertebrates, arthropods). Interest lies in how individual differences contribute to *population-level* processes, not in individual life histories. The perspective relies on the law of large numbers (p. 2).
- **Ecological, not evolutionary**: inheritance and relative fitness are excluded from the definition. LRS is the "currency of the phenotype-environment match", not the determinant of selection (pp. 2, 5).
- **The niche is environmental**: the phenotype mediates fit but is not part of the niche (p. 5; after Hutchinson and Roughgarden 1972).
- **Hutchinson read as**: the (fundamental) niche is the range in which a population persists indefinitely, which implies non-negative long-run growth. The realized niche is described as the niche after interspecific competition, "the niche of a species in n − 1 environmental dimensions" (p. 12). This last gloss is the authors' own reading.
- **Accidents**: purely random events that are equally likely across environments do not affect expectations, but environment-dependent risks do (p. 11).
- **Dimensions**: all external biotic and abiotic factors are included, not only fitness-relevant ones. Combinations not realized anywhere in the world are excluded, while axes may be treated as orthogonal in hypothetical space (p. 12).

## Key results

- **Working definition** (p. 5): the individualized niche is the range of environmental conditions that provides an expected lifetime reproductive success of ≥ 1 surviving offspring to a particular individual, with each offspring counted 0.5 per parent in outcrossers.
- **Uniqueness** (pp. 6–8, Figs. 1–2). The realized individualized niche is a point or small volume. The potential niche is a space of unobservable outcomes. There are two partial fixes: repeated measures with variance decomposition (repeatabilities; Nakagawa & Schielzeth 2010), and marginalization across phenotypes, with individuals as tokens of trait types. The latter is limited when trait interactions are strong and poorly replicated. Experimental translocation (Wilson et al. 2019) covers only a few dimensions and is bounded by lifespan.
- **Time** (pp. 8–12, Figs. 3–5). Lifetime niches miss developmental switches: density-triggered long wings (Poniatowski & Fartmann 2009) and colour change for crypsis in grasshoppers. The prospective niche "always shrinks" with age, "with the possible exception of accidents". The time-slice potential niche can shrink or expand.
- **Dimensions** (pp. 12–14, Fig. 6). The individual niche has n + s dimensions, where s covers intraspecific axes: conspecific presence, mates, density, and morph frequency (apostatic selection, Bond 2007). This links the concept to hard versus soft selection (Wallace 1975).
- **Boundaries** (pp. 14–16, Fig. 7). The boundary is set by *expected*, not realized, LRS. Fitness components or proxies force soft boundaries, and may even use relative fitness. The isocline of 1 is chosen over 0 as a practical benchmark.
- **Conclusions** (pp. 16–17). The concept is not a rebranding of individual-differences research, because it concerns the environment and phenotype–environment match. Three practical challenges remain: identifying the few relevant axes, predicting fitness expectations under nonlinearities, and finding good LRS proxies.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Hutchinson's niche can be given an individual-level analogue with boundary E[LRS] ≥ 1 | moderate | definitional proposal with argument by analogy to population persistence (p. 5); no derivation that the analogy preserves Hutchinson's properties |
| C2 | Individual realized niches are points, and potential niches are unobservable | strong | follows from the definitions (p. 6) |
| C3 | Potential niches can be partly inferred by marginalizing fitness functions across phenotypes or genotypes | weak | informal argument and schematic Fig. 2; no worked estimate or data |
| C4 | Prospective niches can only shrink with age (bar accidents) | moderate | argument from irreversible developmental commitment (p. 10); assumes potentials are fixed at the zygote |
| C5 | Individual niches have n + s dimensions, with intraspecific axes absent from the population niche | moderate | conceptual argument with examples (frequency-dependent predation) |
| C6 | Expected rather than realized LRS must set the boundary | moderate | argument from stochasticity of realized LRS (pp. 14–15) |
| C7 | The individualized niche is distinct from individual-differences research | weak | asserted in Conclusions, grounded only in the environment/phenotype distinction |
| C8 | The sub-concepts are empirically quantifiable (A, C, D, E) | weak | asserted per definition; no empirical demonstration in the paper |

## Concepts

- **Individualized (ecological) niche** — environmental conditions giving a particular individual expected LRS ≥ 1.
- **Realized individualized niche (Def. A)** — the place in environmental space where the individual is found and has expected LRS ≥ 1.
- **Potential individualized niche (Def. B)** — the volume where it *could* be found with expected LRS ≥ 1. Its reference space is the population's realized niche.
- **Fundamental individualized niche** — as the potential niche, but with particular external factors absent. Its reference space is all possible environments. It is set aside as rarely distinguishable in practice.
- **Time-slice individualized niche (Def. C)** — the niche within a life stage or season.
- **Prospective individualized niche (Def. D)** — the current plus future potential niches, given the current phenotype and developmental opportunities.
- **Trajectory-based individualized niche (Def. E)** — a time-structured volume following one developmental trajectory, as distinct from alternative trajectories.
- **n + s dimensionality** — non-intraspecific axes n plus intraspecific axes s.
- **Niche fit** — phenotype–environment match, measured by expected absolute LRS.

## Connections

The paper builds on Hutchinson (1957, 1978), Roughgarden (1972: traits as proxies for resource use), Van Valen's (1965) niche-variation hypothesis, Bolnick et al. (2003) on individual specialization, and the animal-personality literature (Réale et al. 2007; Sih et al. 2004). Within the record it is the individual-level counterpart of Trappes ([LIT-169](../literature.d/LIT-169.md)). She restricts the NCT comparison to population niches and leaves open whether an individualized *evolutionary* niche exists. This paper supplies only an individualized *ecological* niche and deliberately excludes relative fitness, so it leaves her question open. Its persistence-style boundary (E[LRS] ≥ 1) is the individual-level twin of the persistence criterion Trappes uses (mean absolute fitness ≥ 1). The two papers do not cite each other (see corrections). Baedke et al. ([LIT-110](../literature.d/LIT-110.md)) name "individualized niches" (p. 16) as a place where experiential NC should connect to selection, so this paper supplies the object that their Ex node would modify.

**Bearing on the philosophy-of-science tag.** The question is about the **structure of a scientific concept**: the unit, level, modality, dimensionality and boundary of the niche when its reference unit changes from population to individual. The position is pragmatic and operationalist: define the niche by an absolute-fitness threshold, split it into quantifiable sub-concepts, and treat the whole as a heuristic ("metaphorical") framework. This is explication of a theoretical term, so the tag is justified as a secondary tag. It does not engage realism, explanation, causation or evidence debates. Only one philosophy paper is cited on substance: Drouet & Merlin 2015 on propensity fitness. natural-sciences should be the primary topic.

## Bearing on the record

No nucleation THEORY documents are affected. It completes a small niche-concept cluster with [LIT-169](../literature.d/LIT-169.md) and [LIT-110](../literature.d/LIT-110.md). For ML practice: nothing. Its marginalization-across-individuals move is ordinary statistical estimation, and it carries no instruction for machine-learning practice.

## Limitations

- By the authors' own account the concept is "mostly of a metaphorical value" (p. 17). The abstract does not say so.
- Its core quantity, an individual's expected LRS across counterfactual environments, has "no empirical solution" at the individual level (p. 15). It is estimated from other individuals, so the "individual" niche is in practice a phenotype-class niche. The paper does not confront this token/type tension explicitly.
- The threshold 1 versus 0 is a pragmatic choice, and working with fitness proxies abandons the absolute threshold altogether (p. 15).
- It excludes inheritance and relative fitness by design, so it says nothing about how individualized niches evolve.
- The scope is limited to individually distinct animals; clonal and modular organisms are not addressed.
- There are no data, no worked example of the marginalization, and no demonstration that any sub-concept has been measured.

## Open questions

- Can the potential individualized niche be estimated for any real system, with the marginalization of Fig. 2 carried out on data?
- Is an individualized *evolutionary* niche definable (Trappes' question, [LIT-169](../literature.d/LIT-169.md)), and how would it differ from this ecological one?
- How should the intraspecific s-dimensions be treated when they are themselves the outcome of other individuals' niches (frequency and density feedback)?
- Does the prospective niche really shrink monotonically once learning and reversible plasticity are included?

## Corrections to the seeded skim

- The LIT summary and skim say that scaling down "forces … a choice among time-slice, prospective and trajectory views". The paper presents these as complementary perspectives to be used together, not alternatives to choose between (pp. 9–12). The time-slice and prospective views are "two perspectives" on the individualized niche, and the trajectory-based view is added as a "lifelong perspective" for how individualized niches arise.
- The skim omits the formal Definitions A–E (pp. 8–12), each stated with a claim about empirical quantifiability. Realized, time-slice, prospective and trajectory-based niches "can be quantified empirically". The potential niche "cannot directly be quantified, but significant parts … can usually be statistically inferred". The skim also omits the third form, the *fundamental* individualized niche (p. 8). It differs from the potential niche in its reference space: all environments, rather than the population's realized niche. It is set aside as "very subtle and probably not too relevant in practical applications".
- The skim omits the authors' own hedge on status: "we see our concept mostly of a metaphorical value" (p. 17), echoed on p. 2 ("metaphorical value that may help in structuring research"). The abstract does not say this. A reader of the abstract alone would take the concept for a measurement framework.
- On boundaries, the paper explicitly weighs an expected LRS of 0 against 1 (Fig. 7). It chooses 1 as a "useful benchmark in a gradual view", because 0 is hard to determine empirically, not because 1 is theoretically forced (pp. 15–16). Expectations are glossed as law-of-large-numbers statistical summaries, not propensities (citing Drouet & Merlin 2015). The paper concedes there is "no empirical solution" to decompose an individual's LRS into stochastic and deterministic parts (p. 15).
- [LIT-127](../literature.d/LIT-127.md)'s "What a deeper reading should check" calls the paper "the natural companion to [LIT-169](../literature.d/LIT-169.md) (Trappes)". That holds thematically, but Takola & Schielzeth do not cite Trappes 2021 ([LIT-169](../literature.d/LIT-169.md)). The "Trappes et al. 2021" they cite on pp. 5, 8 and 16 is a different, multi-author EcoEvoRxiv preprint, "How individualized niches arise". The two papers do not engage each other directly.
- primary topic: natural-sciences. The work is written "from the perspective of empirically working behavioral ecologists" (p. 2), engages almost no philosophy literature, and is chiefly concept-building within ecology. philosophy-of-science should stay as a second tag, not lead.
- philosophy-of-science tag: justified, but as a secondary tag. It is an explication of a theoretical term (unit, level, modality and boundary of the niche concept), which is conceptual work on a scientific theory's structure. It is not a contribution to realism, explanation, causation or evidence debates.
