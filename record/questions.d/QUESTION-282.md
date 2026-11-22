---
number: 282
status: Open
formerly:
- QUESTION-tmplxq7l
title: 'Under what conditions do interactions change the physically operative correspondence structure among systems (the compatibility operator itself, not only the states it relates), rather than merely reveal it to a measurement or redescribe it in a model?'
version: 1
tags:
- complex-systems
- metaphysics
- mathematics
date: '2026-10-27'
line: distributed-agency
summary: >-
  Raised at the owner's review of the pull request that filed the exchange
  "Field Existence Question", which called it "one of the genuinely
  unfinished parts of the program". The formal results the record now holds
  take the correspondence structure as input. A sheaf's restriction maps,
  a gauge connection, a port condition and a Laplacian are given, and the
  mathematics says what follows. [CLAIM-471](../claims.d/CLAIM-471.md)'s strong thesis is that
  interactions can make or change that structure. Only one model the record
  has read changes it through interaction, and there agreement is reached
  by learning to lie. The question asks for conditions under which the
  operative structure changes, with a way to tell that change from
  discovery and from redescription.
---
<!-- inactive-ok-file: CASE-tmp69rk8 — filed from LEAD-098's run of 2026-11-22, new -->
<!-- inactive-ok-file: CLAIM-478 — Proposed, Open or new; the claims and readings the question presses on -->

# QUESTION-282: Under what conditions do interactions change the physically operative correspondence structure among systems (the compatibility operator itself, not only the states it relates), rather than merely reveal it to a measurement or redescribe it in a model?

## Why it is a question

The owner's review of the pull request, 2026-10-27: "The question I'd most want
to pursue is the generation of correspondence structures themselves. Almost all
the existing mathematics takes those structures as input. Our stronger ontology
wants to explain how they can become physically established, maintained, and
transformed through interaction."

The record's formal results all start one step after this:

- **[CLAIM-481](../claims.d/CLAIM-481.md)'s spectral argument** assumes the Laplacian. Its kernel is
  compatibility and its spectrum sets relaxation rates, once L is given. The
  owner's review: "the spectral mathematics ordinarily assumes the operator
  has already been specified."
- **The readings take the maps as given.** Hansen and Ghrist's restriction
  maps, Robinson's geometric correspondences, Singer's offsets and
  Torres-Hugas et al.'s connection are all inputs ([NOTE-1233](../notes.d/NOTE-1233.md),
  [NOTE-1221](../notes.d/NOTE-1221.md), [NOTE-1224](../notes.d/NOTE-1224.md), [NOTE-1218](../notes.d/NOTE-1218.md)).
- **Composition holds the junction law fixed.** Baez and Fong derive an
  effective boundary relation from a port condition that is the same at
  every junction ([NOTE-1223](../notes.d/NOTE-1223.md)). Composition changes the effective
  constraint, not the law of the junction ([CLAIM-480](../claims.d/CLAIM-480.md)).

The one model read where the maps change through interaction is the discourse
sheaf ([NOTE-1222](../notes.d/NOTE-1222.md)). Agents revise their expression maps from their
neighbours' expressions, and converge to agreement that the authors call
learning to lie ([THEORY-1088](../theory.d/THEORY-1088.md)). That is adaptation of an apparatus's
comparison rules, optimized for consistency alone. It is not a physical
correspondence coming into being.

## What the question separates

[CLAIM-471](../claims.d/CLAIM-471.md) now distinguishes three mechanisms:
- physical constraint formation;
- correspondence discovery;
- correspondence adaptation.

This question asks about a fourth possibility that the first may or may not
contain: an interaction that changes the operator, the structure that fixes
which local states count as compatible. That is a different thing from an
interaction that changes the states the operator relates.

Candidates the record holds or can name, none yet shown to be a case:

- **Slow operator dynamics.** A21 §6 let the maps evolve on their own slow
  time scale, ϑ̇ = εG(ϑ, x, o, e). In such a model the operator is a
  dynamical variable, and the question becomes what G must be for the result
  to be physical and not representational ([CLAIM-478](../claims.d/CLAIM-478.md)'s note of U15–U23).
- **Composition that changes the kind of structure.** Eliminating an interior
  can leave a boundary constraint no pairwise structure expresses
  ([THEORY-1090](../theory.d/THEORY-1090.md)). Whether that is a change in the operative structure, or
  only in what a description of a restricted class can say, is
  [QUESTION-283](QUESTION-283.md).
- **Calibration and coupling in engineered systems.** An implemented
  calibration that drives a controller changes what the system does with its
  comparisons. Whether it changes anything beyond the apparatus is the
  question asked of a case.

## What would count as an answer

1. A criterion that distinguishes a change in the operative correspondence
   structure from discovery and from redescription. One candidate: after
   the change, interventions confined to one side produce different
   admissible joint behaviour than before, by a test that does not pass
   through the apparatus's own comparisons ([CLAIM-342](../claims.d/CLAIM-342.md), [CLAIM-143](../claims.d/CLAIM-143.md)).
2. A system, physical or simulated, that meets the criterion, with the
   mechanism by which interaction produced the change.
3. Or an argument that none can. On that answer, correspondence structures
   are always background or representational, and [CLAIM-471](../claims.d/CLAIM-471.md)'s first
   mechanism reduces to composition under fixed junction laws.

## Note of 2026-11-03: redescription, one way only

A30 §5 of the exchange "Assess SDT Coverage" (2026-11-02) tested whether a change of correspondence maps is mere
redescription. An invertible change of local and edge coordinates is a sheaf
isomorphism and preserves every compatibility verdict, so a change that
alters a verdict is not a redescription. The converse fails: a change that is
not an isomorphism can preserve every verdict. So the test separates
redescription in one direction only. A30's triad (coordinate, organizational,
evaluative) is [TERM-093](../terms.d/TERM-093.md)'s formed and adapted, plus redescription, and lacks
*discovered*. [CASE-189](../cases.d/CASE-189.md)'s Construction 2 is the record's how-possibly model of
interaction producing a new correspondence, and [CLAIM-516](../claims.d/CLAIM-516.md) its necessary
condition.

The question stays open.

## Note of 2026-11-07: a formal entry point for change of the operator, from "Individuation, Possibility, and Disposition"

In the exchange "Individuation, Possibility, and Disposition" (2026-11-06 to 07; https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e), A20 §5 separates "Change within an organization" from change of the organization. If the collective coordinate is q = L(c)x, then q̇ = L(c)ẋ + DL(c)[ċ]x, and the second term is change of the organization. With adaptive offsets on a graph, ṙ = −κDDᵀr − Da(c)[ċ]; a drift of the offsets in the cycle space is untouched by relaxation (the reader checked it on a triangle), which separates a tracking limit from a compatibility obstruction ([CLAIM-556](../claims.d/CLAIM-556.md)). It does not say how interactions change the operator, which is what this question asks. The question stays open.

## Note of 2026-11-22: plastic maps in a simulated network, from [LEAD-098](../leads.d/LEAD-098.md)

[CASE-tmp69rk8](../cases.d/CASE-tmp69rk8.md) ran one variant in which the correspondence maps change through interaction: phase offsets on the coupling that adapt to the realized offsets. Starting frustrated (holonomy 0.8π), the operative maps became compatible and the residual incompatibility went to zero. In the same study, an apparatus that only revised its own maps to the observed offsets reached coherence without changing the system or its own predictions; only revision checked against held-out interventions improved prediction. That separates a change of the operative structure from a redescription in this model. The adaptation rule was the experimenter's, so it is not structure the system generates in the question's full sense. Leaves the question open.

## Note of 2026-11-22: Manik, Timme and Witthaut, read
<!-- inactive-ok-file: THEORY-tmpnlu47 — Proposed; filed by LEAD-023 -->

Manik, Timme and Witthaut ([THEORY-tmpnlu47](../theory.d/THEORY-tmpnlu47.md), bears_on; [NOTE-tmpftn2t](../notes.d/NOTE-tmpftn2t.md)) give two results on what a change of the coupling structure does to the realizable states, which A12 cited them near. Raising one edge's capacity on a four-node ring can remove every locked state: "an increase of local transmission capacity reduces the ability of the network to support a phase locked fixed point" (§IV.D). And fusing two motifs that each have locked states can leave none, while joining two rings that have none can create one (§V.E). So the operator's change has consequences that no part's change predicts. In both, the change is the modeller's, not made by the interactions, so neither touches what this question asks. The question stays open.

## Note of 2026-11-22: Bosca and Ghrist, skimmed
<!-- inactive-ok-file: THEORY-tmp0xz8p NOTE-tmpd2cps — Proposed and Skimmed; filed by LEAD-023 -->

Bosca and Ghrist ([THEORY-tmp0xz8p](../theory.d/THEORY-tmp0xz8p.md), bears_on; [NOTE-tmpd2cps](../notes.d/NOTE-tmpd2cps.md), skimmed) extend the one model this question named, in which interaction changes the correspondence structure. Two additions bear on it. The structure flow is itself diffusion on an auxiliary sheaf of structures (Proposition 4.8), so change of the operator has the same form as change of the states it relates. And a condition is given for which of the two changes: the ratio of the expression rate to the opinion rate bounds how far the other moves (Corollary 6.5). That is a condition of the kind the question asks for, inside the model. As before, the adaptation rule is the modeller's gradient flow, and nothing in the model tells a change of the operator from its redescription. The question stays open.

## Note of 2026-11-22: Leal and colleagues, skimmed
<!-- inactive-ok-file: THEORY-tmpzt77d NOTE-tmp9h46q — Proposed and Skimmed; filed by LEAD-023 -->

Leal and colleagues ([THEORY-tmpzt77d](../theory.d/THEORY-tmpzt77d.md), bears_on; [NOTE-tmp9h46q](../notes.d/NOTE-tmp9h46q.md), skimmed; [LIT-2262](../literature.d/LIT-2262.md)) give a way to describe a correspondence structure that changes over time: a narrative valued in cellular sheaves records the sheaf at each interval and what persists and accumulates across switches of the communication topology. The switching is given as data, not produced by the agents' interactions, and the dynamics on such temporal sheaves are work in progress. A representation for the question's change of the operator, then, not a condition for it. The question stays open.
