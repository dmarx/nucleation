---
status: Read
paper: LIT-tmpzfbla
title: 'Song, Cheng, Zhou and Wang — Linking Scholarly Contents: The Design and Construction of an Argumentation Graph'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://storage.imrpress.com/imr/journal/KO/article/504650/1752844805579.pdf.
    **Read** in full (publisher's PDF). A delegated reader drafted the
    reading; quotations were rechecked by script against the downloaded copy,
    and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  The authors build a knowledge graph of the argumentation inside and across
  scientific papers. Their data model reuses their earlier Scientific Paper
  Argumentation Ontology (SAO, built on AMO/Toulmin, DEO, CoreSC, EXPO) with
  18 unit classes (background, claim, warrant, backing, rebuttal,
  conclusion, hypothesis, data, method, limitation, …), 12 intra-article
  relations (e.g. proves, supports, is part of, is replaced by) and
  CiTO-based inter-article relations (e.g. works for, provides principles
  for, provides assertion for). Two tools: an annotation platform (SAPSP)
  and a d3.js visualizer (VSAG) over Neo4j.
---

# NOTE-tmp2ws61: Song, Cheng, Zhou and Wang — Linking Scholarly Contents: The Design and Construction of an Argumentation Graph

## Contribution

A typed, cross-paper argumentation graph model and a hand-built demonstration on one research line, presented as infrastructure for knowledge-evolution views and reading support.

## Key results

- Abstract: "we propose a way to link the scholarly contents of scientific papers by constructing a knowledge graph based on the semantic organization of argumentation units and relations in scientific papers".
- §3: "This model consists of 18 classes, 12 intra-article argumentation relationships, 16 inter-article relationships" (see inconsistency above).
- §5: "A total of 1,818 argumentation relations, including 1,628 intra-article relations and 190 inter-article relations".
- §6.1: "the evolution of the argumentation units from TAM to TAM2 and then to TAM3 can be represented and visualized".
- §7: "It is difficult to use machine learning technology to realize the automatic extraction of argumentation units and their relationships."
- §7: for reading support, "its performance in these applications has not yet been evaluated".

## Assumptions

Arguments in published papers can be segmented into units of fixed classes and linked by a fixed relation vocabulary; annotators agree on these (no agreement measure is reported); citation relations carry argumentative meaning; the graph represents what papers argue, not what anyone currently holds.

## Concepts

Argumentation unit; Toulmin elements (claim, warrant, backing, rebuttal); SAO, AMO, CiTO, DEO, DoCO; intra- vs inter-article argumentation relations; knowledge evolution representation; strategic reading; argumentation graph.

## Bearing on the record

A (A20 §3) cites it for argument units and relations modelled across scientific articles, with knowledge-evolution uses, and says this "substantially narrows what could honestly be claimed as novel about Luria's graph structure". **The description is accurate; the inference is partly right.** Typed claims, warrants, rebuttals and support relations across documents, with evolution views, are indeed prior art (and the paper's own review traces them to Toulmin, IBIS, Dung, AIF-style ontologies and micropublications). What the paper does not have, and so does not narrow: credence or standing of a claim (status), revision of the graph over time (it represents the evolution *of the literature*, read off citations, not its own revisions), the record's own voice as distinct from the works read, governance of the schema, or any executable check. Luria's graph *grammar* is not novel against this; its maintained, versioned, governed use is not addressed by it.

- **[QUESTION-tmps5iou](../questions.d/QUESTION-tmps5iou.md)**. **Qualifies: supports A's narrowing of the structural novelty claim, leaves the governance question untouched.** The paper places "argument and claim representation" firmly in prior art, and shows a fixed schema with no change process (its relation counts disagree within the paper, an example of an ungoverned schema description). It offers nothing on coupling schema change to decision, migration or checks.
- **[ADR-032](../decisions.d/ADR-032.md)** (the record's own argument: claims, objections, support) already cites Toulmin, Dung, the AIF and ASPIC+ as the lineage; Song et al. is a scholarly-communication application of the same lineage and could be added to that lineage list. Mention only; no status change.

## Limitations

Twelve papers in one field, annotated by the authors' team; no inter-annotator agreement; use cases illustrated, not evaluated. Tables partly garbled in extraction.
