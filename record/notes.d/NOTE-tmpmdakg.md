---
status: Read
paper: LIT-2313
title: 'Hegde et al. — A change language for ontologies and knowledge graphs'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11753292/fullTextXML.
    **Read**, in full, 2026-11-12 (the journal version). A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  Ontologies and knowledge graphs change constantly, yet there is "no single
  agreed-upon way" to represent or communicate changes. KGCL is a LinkML
  data model with a taxonomy of change types (node changes such as rename,
  obsolete, new synonym, definition change; edge changes such as edge
  creation, deletion, node move, predicate change), a controlled natural
  language with a Lark grammar (rename ENVO:01000575 from 'wax' to 'oil'),
  and serializations. The same representation serves as a prospective patch
  ("apply") and a retrospective diff.
---
<!-- inactive-ok-file: CASE-tmppm4do — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CLAIM-250 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpmdakg: Hegde et al. — A change language for ontologies and knowledge graphs

## Contribution

A shared, human-readable and machine-applicable representation of ontology change at the level curators think in, wired to a review workflow.

## Key results

- The gap (Introduction): “there is surprisingly no single agreed-upon way to “represent or communicate” ontology changes.”
- Survey (Introduction): 82% rated understanding changes very important, “while only 8% were satisfied with the current methods for viewing such changes”; only 17% were very or extremely satisfied with turnaround time for requested changes.
- Two uses of one object (Abstract): KGCL can “request desired changes”, and “describe changes that have already happened, corresponding to the concepts of “apply patch” and “diff””.
- Review is required (Ontobot, Fig. 4): “Curators are assigned to review the PR; it cannot be merged until at least one curator approves it.”
- Provisional changes (Future work): proposed changes “stored” as KGCL objects within the ontology “until they are either approved (in which case they will then be effectively applied) or rejected”.
- Scope (Aligning with related work): instance-level changes and “heuristic changes, such as concept merge and split, are yet to be considered”; some users want fuller support for complex axiom types.
- Purpose (Future work, AI applications): “KGCL is fundamentally a tool to help humans communicate about changes in ontologies”.

## Assumptions

Change is best represented at the level curators conceive it, not as axiom-level diffs; curator approval through PR review is the governance; a common language makes practice transferable across ontologies.

## Concepts

Change language; controlled natural language; change taxonomy (NodeChange, EdgeChange, NodeMove, PredicateChange, NodeObsoletion); patch vs diff (prospective vs retrospective change); Ontobot; provisional mode; obsoletion rather than deletion.

## Bearing on the record

The exchange (A22 table, decoded): KGCL gives "High-level, human-readable descriptions of ontology and knowledge-graph changes", and asks whether luria can "supply a stronger relationship between change intent, authorization, implementation and downstream evidence". Accurate as to KGCL. A48 (via [CASE-tmppm4do](../cases.d/CASE-tmppm4do.md)) uses it as a standard against which a change should be restatable as "a precise, independently intelligible change specification"; reasonable. One limit the exchange did not draw: KGCL's change types are changes to an ontology's terms and edges, i.e. to content. It has no change types for the metamodel (what kinds of node or relation exist), and the paper describes no rationale field and no migration of data that uses changed terms.

- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)**: **bears on part 1**. KGCL plus Ontobot couples a change request to an applied change and to curator authority (merge requires approval), and keeps a diff; it does not couple rationale or executable checks in what the paper describes, and it addresses ontology content rather than schema. It does not couple all four, so it does not answer part 1 "no"; it is the strongest precedent here for "change intent, authorization, implementation" in one workflow.
- **[CASE-tmppm4do](../cases.d/CASE-tmppm4do.md)** (names KGCL as comparator): **supports** using a KGCL-style restatement as a check on change legibility; note the restatement covers content edits, so a schema change in luria would need change types KGCL does not have.
- **[CLAIM-419](../claims.d/CLAIM-419.md)** and **[CASE-178](../cases.d/CASE-178.md)** (grammar changes come with decisions): **contrast**. In the OBO workflow, content change is reviewed by PR and, as the paper describes it, the change language itself is extended by "community-driven use cases"; no decision record is described.
- **Retire by status, never by deletion** (the record's practice): KGCL distinguishes NodeObsoletion ("Deprecates usage of the node, but does not delete it") from NodeDeletion, the same distinction. Illustration only.
- **[CLAIM-250](../claims.d/CLAIM-250.md)** (preserve accountability structure, not propositions): **leaves open**; KGCL records what changed, not why.

## Limitations

A tool and standard paper: no evaluation of whether KGCL improves change quality or turnaround; survey of workshop participants only; BioPortal widget still in development; coverage of change types incomplete.
