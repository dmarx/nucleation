---
status: Read
paper: LIT-tmp5pucj
title: 'Clark, Ciccarese and Goble — Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4530550/fullTextXML.
    **Read** (2026-11-12). The main text was read in full, apart from three
    things: Examples 1–3, 6, 7 and 9 were read only in part, the tables were
    not read, and the Additional files were not read. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  The paper treats scientific publications as defeasible arguments and
  proposes "micropublications" as a layered semantic model, available as an
  OWL vocabulary at purl.org/mp. **Range of the model.** - At its minimum, a
  micropublication is a statement with its attribution. - At its maximum, it
  is a Claim with a support graph of Statements, Data and Methods (including
  Materials), plus a challenge graph. **Relations and constraints.** -
  Support is transitive. - A challenge is either direct, or indirect by
  undercutting a supporter. - Within one micropublication, support forms a
  DAG rooted at the Claim. - A Representation can be asserted by the
  micropublication or quoted from another one. This is what lets claim
  networks span publications. **Contrast with statement-based models.** The
  paper sets micropublications against nanopublications, SWAN and BEL. Those
  models represent assertions without their evidence, and they cannot close
  claim lineages down to data. **Examples.** - Example 4 builds claim
  networks across papers. - Example 5 handles "similogs" (statements with
  the same meaning) through holotype claims. - Example 8 models challenge
  and disagreement. **Citation distortion.** The authors apply the model to
  Greenberg's case of citation distortion, where a claim was upgraded to
  "fact" through a chain of self-citations. **Implementation.** It is
  implemented as a plugin to the Domeo annotation tool.
---

# NOTE-tmpb7lxt: Clark, Ciccarese and Goble — Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications

## Contribution

The paper gives a formal, Toulmin–Verheij-grounded model of scientific argument. The model:
- has explicit support and challenge relations, reaching down to data and methods;
- has asserted and quoted provenance;
- supports incremental adoption, from minimal to maximal form;
- has no central curator;
- treats challenges, similarity judgements and annotations as micropublications themselves, so each is attributed.

## Key results

These are design claims, not empirical results.

- **Abstract.** "The minimal form of a micropublication is a statement with its attribution."
- **Background.** "None of these models provide a means to build claim networks of arbitrary depth."
- **Background.** "Scientific assertions do not become matters of fact until the facts have been established, through judgements made over time in a complex social process."
- **Background, on natural language.** "We treat formalization separately as an optional curatorial step."
- **Example 5.** "identification of statements as being similogs is itself an assertion."
- **Example 8.** "But the present model does not require a central curator". Further: "annotations of inconsistency between micropublications, are themselves micropublications."

## Assumptions

- Claims are best captured in their natural language, with formalization optional.
- Attribution is weak support, and empirical data and methods are the critical support.
- Adoption is distributed. Value accrues through annotation at many points in the ecosystem.
- There is no central authority over consistency. Each view is selected at retrieval.

## Concepts

- micropublication, at minimal and maximal forms
- Claim, Statement, Qualifier, Data, Method and Material
- support graph and challenge graph
- direct and indirect challenge (undercutting)
- asserts and quotes
- claim lineage and claim network
- similogs and holotype
- citation distortion
- Toulmin–Verheij argumentation

## Bearing on the record

A calls it "probably the closest conceptual predecessor". That holds for the record's entry level. Like this record, the model represents claims with provenance, evidence, interpretation and challenge as argument structure, with challenges carried as attributed objects.

Three things are absent, and they are the axis of QUESTION-tmps5iou:
- **No standing or credence on claims.** Truth is left to the community over time.
- **No schema-evolution or governance mechanism.** Nothing governs changes to the model itself.
- **No decision records, and no enforced checks beyond OWL/DL-safe rules.**

The paper explicitly declines a central curator. A governed record has one, in the form of decisions plus CI.

- **CLAIM-469** (luria realizes a system of distinctions that fixes what counts as a referable, governable object, and revises them through use). **Verdict: qualifies.**
  - Micropublications is an earlier system of distinctions over claims. It has Claim, Statement, Data and Method types, and supports and challenges relations. It also makes judgements objects: a challenge or a similarity call is itself a micropublication.
  - It therefore shows that the "referable object" half of CLAIM-469 is not new.
  - The model's distinctions are fixed in an OWL vocabulary, with no provision in the paper for revising them through use. That puts the weight of CLAIM-469's distinctiveness on its last clause.
- **QUESTION-tmps5iou** (is coupling schema change to decision, migration and checks what distinguishes luria?). **Verdict: supports it as a comparison point.**
  - Micropublications is a strong argument-model baseline with no coupled schema evolution.
  - It sharpens the contrast class: argumentation-structured records without governed grammar change.

## Limitations

- This is a model and design paper. There is no user evaluation; the paper promises one in a forthcoming article.
- The OWL details sit in Additional files, which were not read.
- The examples are biomedical.
