---
status: Read
paper: LIT-2302
title: 'OAEI — Ontology Alignment Evaluation Initiative 2026'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://oaei.ontologymatching.org/2026/. Read.
    The work is a web page: the campaign page was read in full, and the
    results index skimmed. A delegated reader drafted the reading; quotations
    were rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  OAEI has run yearly since 2004 to evaluate ontology matching systems. The
  2026 campaign uses the MELT platform, with SEALS for the Interactive track
  and HOBBIT for instance matching and link discovery. Tracks span
  T-Box/schema matching (anatomy, conference, multifarm, complex, food,
  Bio-ML, biodiversity, MSE, digital humanities, archaeology, circular
  economy, "Beyond Equivalence"), instance and schema matching (knowledge
  graph, DISO, SPIMBENCH, link discovery, pharmacogenomics, GeoLink cruise)
  and tabular-to-KG matching.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: THEORY-1136 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpeljih: OAEI — Ontology Alignment Evaluation Initiative 2026

## Contribution

A standing shared-task benchmark for ontology and instance matching with reference alignments. It is not a paper.

## Key results

- Scope: "Since 2004, OAEI organises evaluation campaigns aiming at evaluating ontology matching technologies."
- Interactive track: "The goal is to show if user interaction can improve the matching results", with an oracle based on the reference alignment.
- Rules: a matcher's behaviour "should not be based on features specific of the tracks … but on features of the ontologies".
- Beyond equivalence: a track for cases "where simple equivalence mappings are insufficient".
- Papers: "These papers are not peer-reviewed, but they will revised by 1-2 OAEI organisers."

## Assumptions

Reference alignments are the ground truth, and matching is aligning two fixed ontologies. Nothing on the page concerns the evolution or governance of a single ontology.

## Concepts

Ontology matching and alignment; reference alignment; complex correspondences; interactive matching with an oracle; MELT, SEALS, HOBBIT.

## Bearing on the record

The exchange rates OAEI "Adjacent" and says it covers "Ontology matching and change-related interoperability, but not directly governed schema evolution". **Mostly accurate.** "Adjacent" and "not directly governed schema evolution" are right. "Change-related interoperability" is not supported by the 2026 page: no 2026 track concerns ontology change or versioning. Every track aligns separate, fixed sources. The LIT has no characterization.

- **QUESTION-tmps5iou** (is coupling schema change to governance what distinguishes luria from ontology and metamodel evolution): **leaves open; mostly irrelevant**. OAEI evaluates alignment between ontologies, not the governed evolution of one, so it is not part of the comparison class the question names. It could serve only in the narrow role of a scorer: checking that a migrated grammar still aligns with its predecessor. Even that would require reference alignments the record does not have.
- **CASE-tmppm4do**: the Interactive track's oracle design is a precedent for the case's "deterministic rule-based simulator" reviewer. That reviewer is the exchange's design, line 1752, not the case's text. Weak bearing.
- Held entries that use OAEI data: NOTE-1323 / THEORY-1136 (hyperbolic hierarchy matching, scored on OAEI Anatomy and Biodiv). These are the record's existing contact with OAEI. LIT-1808 is the paper behind them.

## Limitations

The per-track results pages and the organizers' synthesis paper (linked "here" on the results page, not yet available) were not read. The final results come after the 2026-11-12 deadline for final system papers.
