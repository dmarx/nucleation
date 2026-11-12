---
status: Skimmed
paper: LIT-tmpo7zwb
title: 'Flouris et al. — Ontology change: classification and survey'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from
    https://typeset.io/pdf/ontology-change-classification-and-survey-4n37nzlmdf.pdf.
    **Skimmed** (the framing sections and the evolution section read in full;
    heterogeneity resolution, debugging, versioning and integration/merging
    skimmed). A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  A survey that defines "ontology change" broadly (deciding modifications in
  response to a need, implementing them, and managing their effects on
  dependent data, services and ontologies) and classifies ten subfields:
  mapping, morphism, matching (alignment), articulation, translation
  (heterogeneity resolution); evolution and debugging (modifying an
  ontology); versioning; integration and merging. Table 1 gives each
  subfield's purpose, input, output and properties. For evolution it reports
  Stojanovic et al. (2002)'s cyclic six-phase process (change capturing,
  representation, semantics of change, implementation, propagation,
  validation), elementary vs. composite changes, evolution strategies for
  side-effects, and belief-change (AGM) approaches to the semantics of
  change.
---
<!-- inactive-ok-file: QUESTION-289 — Answered; cited for what each holds, not as settled -->

# NOTE-tmpolhl4: Flouris et al. — Ontology change: classification and survey

## Contribution

A terminology and classification of ontology-change research, and a breadth survey of approaches
and tools as of about 2007.

## Key results

- Sec. 2.2: ontology change is "the problem of deciding the modifications to perform upon an ontology in response to a certain need for change as well as the implementation of these modifications and the management of their effects in depending data, services, applications, agents or other elements."
- Sec. 2.2: reasons include that "we may discover a design flaw in the original conceptualization of the domain".
- Sec. 2.2: "ontology designers cannot know who uses which part of their ontology and for what purpose, so they cannot predict the effects that a given change on their ontology would have upon dependent elements."
- Sec. 2.3: "In particular, we will identify and study 10 subfields of ontology change".
- Sec. 4.2.2: "six phases of ontology evolution have been identified in (Stojanovic et al. 2002), occurring in a cyclic loop."
- Sec. 4.2.2: the semantics of change phase "is probably the most crucial of ontology evolution, because during that phase the direct and indirect changes caused by a given change request (i.e., the effects and side-effects of the change) are determined."
- Sec. 4.2.2: implementation tools should "keep a log of the implemented changes"; the validation phase lets the engineer "review the changes and possibly undo them".
- Sec. 4.2.2: on composite changes, "creating a complete list of composite operations is not possible".
- Sec. 4.2.2: ontology evolution algorithms "assume human participation in the process".
- Sec. 4.2.3: belief change techniques apply to "the most important (and difficult) phase of ontology evolution, namely the semantics of change phase".
- Sec. 6: "Our aim was to propose a terminology in an area that is plagued by the presence of underspecified and confusing terms."

## Assumptions

- Ontology change is about a formal artefact (an ontology) in a decentralized Semantic Web.
- The engineer decides; the process supports the decision with representation, side-effect
  determination, logging and validation. Who may decide, and why, is outside the frame.

## Concepts

Ontology change; ten subfields (Table 1); heterogeneity resolution; six evolution phases (capture,
representation, semantics of change, implementation, propagation, validation); elementary vs.
composite change; evolution strategies; push vs. pull propagation; versioning as an alternative to
propagation; ontology debugging (diagnosis, repair); belief change / AGM for ontology evolution;
ontology revision (concepts as the evolving objects).

## Bearing on the record

A cited it for "processes for capturing changes, assessing their semantics, propagating consequences
and validating the result". **Accurate, but these are Stojanovic et al. (2002)'s phases as reported
by Flouris et al.**, not Flouris et al.'s own proposal. This also resolves the LIT's note that A's
companion citation "Stojanovic" names no work: Flouris et al. attribute the six phases to Stojanovic,
Maedche, Motik and Stojanovic (2002), "User-driven Ontology Evolution Management", EKAW-02, LNCS 2473,
pp. 285-300.
- [QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md) (is the coupling of schema change to recorded decision, migration and executable
  checks what distinguishes luria?): **qualifies and narrows.** The survey shows that capture,
  formal representation, determination of side-effects on dependants (migration in luria's terms),
  logging and validation of a change were already a standard process for ontology evolution by 2002.
  What it does not include is a recorded rationale or decision with standing, any governance of who
  may change the ontology, or executable checks run against the content as a gate; the evolution
  process "assume[s] human participation" and logs changes. So the survey supports that the
  distinguishing part, if any, is the recorded decision and the governance, not change management
  as such. Leaves open whether that coupling does work.
- [CLAIM-419](../claims.d/CLAIM-419.md) (the grammar is amendable by decision, and a misfit has repeatedly been treated as a
  defect of the grammar): **corroborates by analogy**: the survey lists discovering "a design flaw in
  the original conceptualization" as a standard reason for changing an ontology and gives a process
  for it; it says nothing on how often misfits are caught.

Searched the record for Flouris, the DOI, Stojanovic, KAON, Protege, AGM, belief
revision/change, schema evolution/migration. Not held (the "Flouris" hit is "Flourish" in
[NOTE-1429](NOTE-1429.md); no duplicate). Missed by the first search:
- [LIT-1050](../literature.d/LIT-1050.md) (Alchourron, Gardenfors and Makinson, AGM, Active), [LIT-1072](../literature.d/LIT-1072.md) (Logic of Belief Revision,
  Active) and [QUESTION-289](../questions.d/QUESTION-289.md) (whether a closed belief set fixes future revisions, Answered): the survey
  reports AGM-based ontology evolution as a research line; the record's AGM holdings are the theory
  it borrows from.
- Among the same filing's LITs DILIGENT ([LIT-2274](../literature.d/LIT-2274.md)), COPE/Edapt ([LIT-tmp5mdsg](../literature.d/LIT-tmp5mdsg.md)), KGCL
  ([LIT-2313](../literature.d/LIT-2313.md)), VoCol, WebProtege and OBO ([LIT-tmpk047v](../literature.d/LIT-tmpk047v.md)) are in the same comparison class; the survey
  predates most of them.

## Limitations

A breadth survey, explicitly not deep; literature to about 2007; manuscript version read; no
evaluation of the approaches it lists; no treatment of governance or rationale.
