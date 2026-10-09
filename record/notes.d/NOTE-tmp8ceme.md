---
status: Read
paper: 'LIT-tmp9axrl'
title: 'Computational challenges to Lévi-Strauss transformational methodology'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the publisher's version deposited in HAL
    (halshs-03348771), pp. 1–19: every section, Algorithm 1, the figure
    captions (the figures themselves, screenshots and model diagrams,
    were not legible in the text layer) and the reference list. The
    authors' 2020 Symmetry paper, where the transformation engine is
    described "in more detail", was not read.
date: '2026-10-09'
summary: >-
  Proposes DEVS modelling and simulation, in the authors' DEVSimPy, as a
  way to generate and visualise Lévi-Strauss's transformations of myth,
  and extends the canonical formula's "boundary condition" to a programme
  on identity politics. What it shows is software: myths as mytheme
  lists, variants produced by user-specified operations, and one Corsican
  folktale's mythemes placed on Google Earth. No claim about myth is
  tested.
---

<!-- inactive-ok-file: LIT-775 — Deferred; named as the work the paper models, not leaned on -->

# NOTE-tmp8ceme: Computational challenges to Lévi-Strauss transformational methodology

## Contribution

The paper argues that Lévi-Strauss's transformational method, long
dismissed in Anglo-American anthropology as "pseudo-mathematical
mystification", can be made operational with a discrete-event simulation
formalism, and presents the authors' software for it. Beyond the
argument, it adds a geographic visualisation: a myth's mythemes, given
coordinates by hand, are displayed in narrative order on a map. The
transformation-generating machinery is summarised from their 2020 paper.

## Key insight

The paper's own: treat a myth as a network of components (mythemes) whose
connections can change during a simulation, so that a transformation of a
myth is a change of model structure, which DEVS with dynamic variable
structure supports. In the software as described, which change to make is
supplied by the user.

## Assumptions

- That Lévi-Strauss's myth analysis is an algorithmic, generative system
  ("myths are something like informal algorithms").
- That a myth decomposes into mythemes, each a pair of a term and a
  function, and that a variant is obtained by operations on those pairs.
- That the canonical formula, with a boundary condition external to it,
  captures how myths transform across the boundaries between peoples.

## Key results

- **DEVS models defined** (summarised from the 2020 paper): MythGen,
  TransformationADEVS, Collector, Supervisor, MythemADEVS and Observor;
  a myth as a coupled model of mytheme atomic models; generation of a
  new myth (M2 Bororo) from the reference myth (M1 Bororo) by the
  operations held in TransformationADEVS; a graph of generated myths
  (Fig. 5).
- **Visualisation models** (new here): ViewerGen reads a text file of
  mythemes and a second, hand-made file of coordinates; MythVisu adds a
  PointMyth instance to the MythVariant coupled model for each mytheme;
  SIGviewer writes a KML placemark (Algorithm 1); Google Earth reloads the
  KML periodically, and a step-by-step plugin advances the narrative.
- **Validation.** The 20 mythemes of *U Lurcu*, from the Nebbiu in
  northern Corsica, are placed on the map in narrative order (Figs.
  11–14). The simulation's time base is not historical time.
- **Programme.** A neo-structural model of identity transformations,
  combining discourse analysis, Bayesian inference and probabilistic DEVS,
  proposed for EU and US politics.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | DEVS with dynamic structure can represent a myth as mythemes and apply transformation operations to generate variants | moderate (as a software claim) | the model inventory; details deferred to the 2020 paper |
| C2 | The software displays a myth's mythemes on a map in narrative order | strong (demonstration) | Figs. 11–14, Algorithm 1 |
| C3 | This validates or revitalises Lévi-Strauss's transformational theory | not supported here | no prediction of the theory is tested; the transformations are user-specified |
| C4 | The method can automatically validate anthropologists' hypotheses and analyse many myths | not supported here | asserted in the introduction; not shown |
| C5 | The approach can anticipate identity transformations and inform policy | not supported here | future work |

## Method

Discrete-event system specification: atomic models (states, transition
and time-advance functions) composed hierarchically into coupled models,
run by an abstract simulator; dynamic structure by a supervisor atomic
model that rewires a coupled model during simulation (after Baati et al.
2007). Implemented in Python 2 in DEVSimPy, with plugins for step-by-step
runs and map display through KML.

## Concepts

- **mytheme**: the basic element of a myth, characterised by a term (a
  person, animal, divinity or thing) and a function (its role).
- **transformation (of a myth)**: a variant obtained from another by
  operations such as inversion, opposition, homology or symmetrization;
  all variants form a group with no privileged member.
- **boundary condition**: in the authors' reading of the canonical
  formula, the external condition of crossing a spatial, linguistic or
  social boundary under which the "double twist" transformation occurs.
- **DEVS / DSDEVS**: discrete-event system specification; its dynamic
  structure extension.

## Connections

The paper's base is Santucci, Doja and Capocchi (2020), "A Discrete-Event
Simulation of Claude Lévi-Strauss' Structural Analysis of Myths Based on
Symmetry and Double Twist Transformations", *Symmetry* 12(10):1706, not
held. It reads Lévi-Strauss through *Mythologiques* and the canonical
formula (Lévi-Strauss's 1955 article "The Structural Study of Myth",
later collected in *Structural Anthropology*, [LIT-775](../literature.d/LIT-775.md), unread),
and through mathematical readings (Petitot, Maranda, Morava). It cites
Propp's *Morphology* (English 1968; [LIT-tmppp40q](../literature.d/LIT-tmppp40q.md)) among earlier
formalisations of narrative. Descola's lecture ([LIT-tmpmgblk](../literature.d/LIT-tmpmgblk.md)) is not
cited.

## Bearing on the record

- **On computational modelling of Lévi-Strauss as prior art.** The paper
  shows that Lévi-Straussian transformations have been implemented as
  software operations on mytheme representations. It does not show that
  the software discovers transformations, decides between analyses, or
  tests any structural hypothesis against a corpus: the operations are
  supplied, and the validation is a map display of one folktale. Whoever
  cites it as a computational model of Lévi-Strauss's analysis should say
  it is a framework for encoding analyst-specified transformations; the
  2020 *Symmetry* paper, unread, is where the transformation model
  itself is described.
- Descola's point ([LIT-tmpmgblk](../literature.d/LIT-tmpmgblk.md)) that in myth the analyst cuts the
  transformation continuum applies here unaltered: the software inherits
  the analyst's cuts.
- No THEORY is filed. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- No corpus beyond one reference myth (named) and one folktale (mapped);
  no evaluation, no comparison with any other analysis.
- The transformation engine is summarised, not specified, here.
- The geographic coordinates are entered by hand.
- Much of the text is a defence of Lévi-Strauss's legacy and a
  programme for future work.

## Open questions

- Given a corpus of variants, can such a system recover the
  transformations an analyst proposes, or propose ones the analyst did
  not, with some criterion for preferring one over another?
- Does the 2020 paper's double-twist implementation reproduce a published
  Lévi-Strauss analysis end to end?
