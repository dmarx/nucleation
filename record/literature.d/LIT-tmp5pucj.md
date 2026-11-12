---
status: Active
status_note: >-
  Read on 2026-11-12 (NOTE-tmpb7lxt) from
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4530550/fullTextXML.
title: 'Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI or arXiv id, exact title and first author in record/literature.d. `published:`: Crossref's online date. No email address was sent to any service.
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 (NOTE-tmpb7lxt; THEORY-tmpes8q7).
tags:
- design-rationale
- philosophy-of-science
date: '2026-11-12'
published: '2014-07-04'
doi: '10.1186/2041-1480-5-28'
first_author: 'Clark'
keywords: []
implementations: []
summary: >-
  Clark, Ciccarese and Goble (2014), Micropublications: a semantic model for
  claims, evidence, arguments and annotations in biomedical communications.
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
  implemented as a plugin to the Domeo annotation tool. Read for the
  exchange "luria experiment design".
---
<!-- inactive-ok-file: THEORY-tmpes8q7 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# LIT-tmp5pucj: Micropublications: a semantic model for claims, evidence, arguments and annotations in biomedical communications

Tim Clark, Paolo Ciccarese and Carole Goble (2014), Journal of Biomedical Semantics. DOI 10.1186/2041-1480-5-28.

## Key takeaways

*Seeded from the exchange, not read.* A cites it for "probably the closest conceptual predecessor" of the record: claims, provenance, evidence, interpretation and challenges represented as scientific arguments. Unverified until read.

## Standing in the record

Registered on 2026-11-12 from the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A20 (§1). It bears on CLAIM-469 and QUESTION-tmps5iou.

## Reading of 2026-11-12

Read in NOTE-tmpb7lxt, from https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4530550/fullTextXML; its account is THEORY-tmpes8q7.
