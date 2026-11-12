---
status: Read
paper: LIT-2274
title: 'Tempich, Pinto, Sure and Staab — An Argumentation Ontology for DIstributed, Loosely-controlled and evolvInG Engineering processes of oNTologies (DILIGENT)'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://link.springer.com/content/pdf/10.1007%2F11431053_17.pdf. **Read**
    (2026-11-12), in full, pp. 241–256. A delegated reader drafted the
    reading; quotations were rechecked by script against the downloaded copy,
    and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  DILIGENT is a process for building a shared ontology among distributed,
  loosely controlled participants: a small team builds an initial ontology,
  users adapt it locally but may not change the shared one, a control board
  collects change requests with their arguments, analyses local adaptations,
  decides which changes enter the next version, and users then update their
  local ontologies. The paper presents an OWL DL ontology, adapted from
  IBIS, for recording the arguments exchanged in that process: Issues (what
  should be in the conceptual model), Ideas (how to formalize it, linked to
  concrete ontology change operations), Arguments (Justifications and
  Challenges, with Examples, Evaluation&Justification, Counter Examples,
  Alternative&Contrast), Positions (agree/disagree), and Decisions (status
  under discussion, postponed, discarded, agreed), with Actors that are
  human or machine (ontology-learning algorithms arguing by measures such as
  TFIDF). A discussion from an 11-person, 90-minute experiment is modelled
  after the fact.
---
<!-- inactive-ok-file: CLAIM-179 LIT-762 — Proposed, Unfetched; cited for what each holds, not as settled -->

# NOTE-tmpmnbt5: Tempich, Pinto, Sure and Staab — An Argumentation Ontology for DIstributed, Loosely-controlled and evolvInG Engineering processes of oNTologies (DILIGENT)

## Contribution

By the authors' statement, "the first formal argumentation model for Ontology
Engineering", separating conceptual from formal discussion and admitting
machine-generated arguments.

## Key results

- §1 (p. 242), from the SEKT/PROTON case: "it is already difficult for
  newcomers to enter it since (1) tracing the exchanged arguments is
  virtually impossible".
- §2.3 (p. 245), reporting their earlier experiment [2]: "restricting the
  argument types to Elaboration, Evaluation, Justification, Contrast,
  Alternative, Example and Counter Example enhances the productivity of OE
  discussions." (Reported, not shown in this paper.)
- §3 (p. 246): users "are not allowed to directly change the ontology shared
  by all users"; "a crucial activity of the board is deciding which changes
  are going to be introduced in the next version of the shared ontology."
- §4.1 (p. 248): "modelling decision are discussed more than once, since the
  modelling reasons of the existing version are not documented."
- §4.2, Table 1: three inconsistencies a formal model should detect: idea,
  argumentation and position inconsistency.
- §6 (p. 250): "concepts are only added to the ontology if they can be agreed
  upon"; a Decision records "the line of reasoning (a sequence of arguments)
  underlying the decision" (p. 251).
- §7 (p. 253): "We do not intent to automatically annotate a free
  discussion. We rather envision a template based approach. Currently we use
  a WIKI"; integration with reasoners "remains to be done."
- §8 (p. 254): the main contribution is "the first formal argumentation model
  for Ontology Engineering".

## Assumptions

Ontology building is social and continuing, not one-off; consensus is the
criterion for admitting a concept; a central control board holds authority
over the shared version; arguments are captured in free text, not formalized
logically (the ontology does not aim at formalizing the exchanged arguments
logically, pp. 242–243, across a footnote).

## Concepts

DILIGENT process (build, local adaptation, analysis, revision, local update);
control board; Issue / Idea / Argument (Justification, Challenge) / Position /
Decision; Elaboration; human vs. machine argumentation; ontology change
operation; idea, argumentation and position inconsistency; argument
selection; traceability.

## Bearing on the record

[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md) lists DILIGENT under "Argumentation-governed ontology
evolution". Accurate. Two cautions: (1) DILIGENT governs the
*domain ontology* through argument; the argumentation ontology itself is
fixed, and the paper says nothing about changing the representational
scheme in which the arguments are recorded; (2) it is a design paper with a
modelled example and no evaluation of the argumentation ontology itself
(the productivity result cited is from the authors' earlier ECAI 2004 paper,
ref. [2]).

- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)** (is luria's coupling of schema change to recorded
  decision, migration and checks what distinguishes it from ontology
  evolution, and does it do work that argumentation-governed evolution does
  not?): **supports** that argumentation-governed, decision-gated change to a
  shared schema is prior art: issues, arguments, positions, a board's
  decision with status and recorded line of reasoning, versions released to
  users. It also sharpens the question by showing what DILIGENT lacks, as
  stated in the paper: no migration of local ontologies is specified (users
  "may rather reuse" new concepts, p. 247), no executable checks beyond hoped-
  for inconsistency detection by "an appropriate reasoner" not yet integrated,
  and no revision of the argument scheme itself. So it **leaves open** the
  question's second half, and narrows the comparison class: the candidate
  difference is migration and executable checks, not governance by recorded
  argument.

- **[CLAIM-179](../claims.d/CLAIM-179.md)** (Proposed: when an agent files, the capture cost falls on the
  party that would re-derive, removing the disparity design-rationale systems
  were abandoned over): DILIGENT is a design-rationale system for ontologies
  whose authors already see capture cost as the obstacle (§4.1:
  "documentation is a time consuming, often neglected task") and propose
  templates and ontology-learning agents as arguers. It supports the claim's
  premise and is prior art for its "agent as arguer" move; it reports no
  result on whether capture was sustained.
- **[LIT-758](../literature.d/LIT-758.md)** (Kunz and Rittel, IBIS) and **[LIT-762](../literature.d/LIT-762.md)** (gIBIS), held: DILIGENT
  cites both ([10], [12]) and is built on IBIS; one may link them.
  **[ADR-030](../decisions.d/ADR-030.md) / [ADR-032](../decisions.d/ADR-032.md)** (IBIS-related decisions) are the record's own
  adoption of the same lineage.
- **[NOTE-1373](NOTE-1373.md)** mentions HCOME only as a string; unrelated.
- "Ontology engineering" and "Compendium" have no hits Duplicate check: DOI and title not held elsewhere.

## Limitations

No empirical evaluation of the argumentation ontology; the example is
modelled after the fact; tool support was future work; the OWL ontology was
promised "online in case of acceptance" and was not inspected here.
