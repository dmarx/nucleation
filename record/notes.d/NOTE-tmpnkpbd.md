---
status: Read
paper: LIT-tmptsso9
title: 'Tudorache, Nyulas, Noy and Musen — WebProtégé: A collaborative ontology editor and knowledge acquisition tool for the Web'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://pmc.ncbi.nlm.nih.gov/articles/PMC3691821/.
    **Read** in full (author manuscript in PubMed Central). A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  WebProtégé is a browser-based, lightweight ontology editor built on the
  Protégé collaborative back end, meant to let domain experts, not only
  knowledge engineers, edit ontologies. Its interface is a declarative,
  per-project and per-user configurable portal of portlets and
  knowledge-acquisition forms bound to ontology properties. Collaboration
  support includes change tracking (every authoring operation recorded in
  the Changes and Annotation Ontology, ChAO, with author, time and
  description), threaded typed notes attached to entities, watches with
  notifications, change-analysis statistics and a configurable access policy
  down to property level.
---

# NOTE-tmpnkpbd: Tudorache, Nyulas, Noy and Musen — WebProtégé: A collaborative ontology editor and knowledge acquisition tool for the Web

## Contribution

A web editor that makes collaboration (change history, discussion, notifications, permissions) part of ontology editing itself, and a customizable form layer that turns the editor into a knowledge-acquisition tool for domain experts.

## Key results

- §3.2: "All authoring operations in the WebProtégé are tracked as instances of a Changes and Annotation Ontology (ChAO)".
- §3.2: "Users can also have contextualized threaded discussions and notes attached to different entities in the ontology."
- §3.2: "WebProtégé supports a flexible access policy mechanism." — with property-level edit permissions (§3.1.2).
- §2: forms allow "the immediate validation of the values based on the definitions in the ontology is possible" (value validation against the schema).
- §5: iCAT: "Users have already made over 105,000 changes in iCAT"; "More than 19,000 notes and discussions are recorded in the platform."
- §5: the schema and forms co-evolved: "we had to make all portlets very configurable so that we can adapt the user interface quickly".
- §6: merging sandboxes: "we must be able to fold back the changes into the master version".
- §6: the UI configuration for ICD: "this configuration is getting very hard to manage, maintain, and validate".

## Assumptions

- Collaboration is supported by recording changes and discussions alongside the artefact; the paper does not tie a change to the discussion that justified it, nor require one.
- Governance is access control (who may edit what), set by administrators; there is no stated process for deciding schema changes.

## Concepts

Collaborative ontology development; ChAO (change and annotation ontology); threaded notes on entities; watches and notifications; property-level access policy; declarative UI configuration (default / project / project-and-user); knowledge-acquisition forms; iCAT for ICD-11; sandbox and merge.

## Bearing on the record

A (A22) cites it for collaborative ontology editing with change history and discussion. **Accurate.** What is absent in this paper matters for the comparison: no recorded decision or rationale required for a change, no migration of existing content when the schema changes, no executable checks over the ontology beyond value validation in forms; governance is permissions.

- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)**. **Qualifies the prior art, partly supports the distinctiveness question.** WebProtégé couples schema editing to change history, discussion attached to the entity changed, and authority (property-level permissions) at production scale (ICD-11). It does not, in this paper, couple a schema change to a decision record, a migration, or executable checks over the whole ontology; its own §6 lists merging and validation of configuration as unsolved. On [QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)'s "capability-and-workflow comparison", WebProtégé (2013) scores: rationale — discussion attached but not required; migration — no; executable checks — form-value validation only; authority over the schema — yes, by access policy. So it does not answer the first half "no". It is a strong example of A22's point that the systems "can support accountable change", as convention, not enforcement.
- **[CLAIM-419](../claims.d/CLAIM-419.md) / [CASE-178](../cases.d/CASE-178.md)** (the record's grammar amended by decision): WebProtégé records schema changes but not decisions about them; the contrast is exactly [CLAIM-419](../claims.d/CLAIM-419.md)'s "amendable by decision".

## Limitations

Published version not compared with the manuscript. Usability studies are cited, not reported, here. No measurement of whether discussion improved the ontology.
