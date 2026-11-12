---
status: Read
paper: LIT-tmpk047v
title: 'Jackson et al. — OBO Foundry in 2021: operationalizing open data principles to evaluate ontologies'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://pmc.ncbi.nlm.nih.gov/articles/PMC8546234/.
    **Read** (full text, HTML). A delegated reader drafted the reading;
    quotations were rechecked by script against the downloaded copy, and any
    that did not match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The OBO Foundry's operations committee reports how it turned the Foundry's
  founding principles (open, common format, URI space, versioning, scope,
  textual definitions, relations, documentation, plurality of users,
  collaboration, locus of authority, naming, maintenance, responsiveness)
  into operational rules stated in MUST/SHOULD language, each with an
  automated check, run across all member ontologies and shown on a public
  dashboard. It first re-curated the registry metadata of every ontology
  (moving it into a GitHub repository changed by pull request), then refined
  each principle into a checkable procedure, then built the dashboard on
  ROBOT. Errors fell after the dashboard was announced; some principles
  cannot be automated.
---
<!-- inactive-ok-file: LIT-tmpt3cxh — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: TERM-108 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpsm319: Jackson et al. — OBO Foundry in 2021: operationalizing open data principles to evaluate ontologies

## Contribution

A worked case of a federated community governing a shared standard by (i) keeping the principles
under continuous, issue-tracked revision, (ii) encoding each as an executable check, and (iii)
publishing conformance per member. It is evidence that such operationalization is feasible at the
scale of ~150-200 ontologies and changes member behaviour.

## Key results

- Abstract: the principles "were not originally encoded in a precise fashion, and interpretation was subjective".
- Abstract: "formally encoding the OBO principles as operational rules and implementing a suite of automated validation checks and a dashboard".
- Results, registry: "Metadata files are stored in a structured format under version control in a repository within the OBO GitHub organization." Changes come "via GitHub pull requests"; "3045 commits by 113 developers" as of May 2021.
- Results, principles: "These principles were always envisioned as being evolutionary and have been reworded and added to throughout the years."
- Results, principles: "Conforming to all principles is not currently a requirement to be included in the list of OBO ontologies."
- Results, principles: each principle has a GitHub issue for its validation, and "there is a continuous review in bi-weekly conference calls of new questions and the need to update the wording of principles."
- Results, dashboard: "a significant reduction in reported errors" between 11/2019 and 07/2020 ("P = 0.0005, Wilcoxon test").
- Results, dashboard: "users reported issues with the automated validation code leading to false-positive and false-negative results, which were subsequently fixed".
- Table 2, Maintenance: "we realize that this does not necessarily mean that the ontology is up to date with scientific consensus."
- Discussion: "relying on human review of such principles is difficult to standardize and does not scale."
- Discussion: "not all principles formulated for the OBO Foundry can be checked reliably in an automated fashion." Commitment to Collaboration: "this cannot be automated at this time."
- Discussion: they expect "continuous improvements of the tests themselves and of the shared understanding of what the tests (and the principles) are meant to achieve".

## Assumptions

- That a principle's operational test is a fair proxy for the principle (the authors flag where it
  is not: Maintenance, Scope, Collaboration).
- The before/after error comparison has no comparison group (the checks were constant between the
  two runs, and only ontologies active in both were counted), so the fall is attributed to the
  dashboard's announcement without a control.

## Concepts

Operationalized principle; automated validation / dashboard; registry metadata under version
control with pull requests; locus of authority; conformance reporting rather than exclusion;
proxy check vs principle (versioning date as a proxy for maintenance).

## Bearing on the record

A's description (community principles refined over time, operationalized into validation checks,
and used to evaluate ontology maintenance) is **accurate**, with two qualifications: the checks
evaluate conformance to all principles, of which maintenance is one and the one the authors say is
least well proxied; and the paper reports principle revision as a practice (issues, calls), not a
formal decision-and-migration procedure. Calling it "OBO Foundry governance" is fair: the paper
names the operations committee that stewards the principles.

- QUESTION-tmps5iou (is the coupling of schema change to recorded decision, migration and
  executable checks what distinguishes luria?): **qualifies** the novelty side. OBO already couples
  a revisable standard to executable checks, pull-request-curated structured metadata on GitHub,
  issue-tracked discussion of each rule and a standing governance body: much of luria's apparatus
  (lint, PRs, closed vocabularies). What the paper does not show is a recorded decision per change
  to a principle, or a migration of members' content when a principle changes; principle changes go
  through issues and calls, and conformance is reported, not enforced (except "Open"). So it leaves
  open whether coupling-to-recorded-decision-and-migration is the distinguishing part, but narrows
  the claim to that part.
- CLAIM-419 (grammar fixed at any moment, amendable by decision; misfits treated as defects of the
  grammar): **corroborates by analogy**, not support: OBO's principles are revised when found
  imprecise, and the checks themselves were revised after false positives and negatives - a
  standard and its checker both under amendment. It is about a different object (member ontologies'
  conformance, not a record's own grammar).

Searched the record for OBO, Foundry, dashboard, operationaliz*, ontology change/evolution,
RFC 2119/MUST-SHOULD, FAIR principles, Goodhart. None held on OBO or the Foundry (no LIT holds this
DOI; not a duplicate).
- TERM-108 (proxy objective, an operational measure optimized in place of the outcome it stands
  for): the Maintenance check (date-format version IRI) is the authors' own example of a proxy
  check they say does not establish the principle. Illustrates it.
- CASE-178 (on the branch, cited by QUESTION-tmps5iou: grammar refinements with ADRs): OBO is a
  comparison case for how often a standard's revision is decision-documented; OBO's are tracked in
  issues, not in decision records.
- On the branch, the sibling unread LITs for VoCol (LIT-tmpt3cxh), WebProtege (LIT-tmptsso9) and
  DILIGENT (LIT-2274) sit in the same comparison class.

## Limitations

A short report (about 10 pages), descriptive; one uncontrolled before/after statistic; no account
of how principle changes are decided beyond issues and calls; figures not inspected.
