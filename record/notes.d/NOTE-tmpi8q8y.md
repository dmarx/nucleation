---
status: Read
paper: LIT-tmpusag6
title: 'Halilaj, Grangel-González, Coskun and Auer — Git4Voc: Git-based Versioning for Collaborative Vocabulary Development'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/1601.02433. **Read** in
    full. A delegated reader drafted the reading; quotations were rechecked by
    script against the downloaded copy, and any that did not match were kept
    as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  Collaborative vocabulary development is "the process of finding consensus"
  among experts from different systems; the authors argue that a version
  control system is "the heart of the problem" and adapt Git. They list
  eleven requirements (communication, provenance, roles, workflow
  independence, quality assurance, documentation, deltas between versions,
  editor independence, modularity, multilinguality, labeled releases) and
  meet them with conventions and hooks: issues on GitHub-like platforms for
  discussion; commit history for provenance; a branching model by kind of
  change (basic, semantic, structural); server- or client-side hooks that
  enforce roles and run syntax checks (Rapper) and best-practice checks
  (OOPS!) before a commit, cancelling it on failure; post-commit
  documentation generation; one triple per line in Turtle so diffs work;
  files of at most 300 triples as modules; tags for releases. Git cannot
  show semantic diffs; external tools are proposed.
---
<!-- inactive-ok-file: LIT-tmpt3cxh — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpi8q8y: Halilaj, Grangel-González, Coskun and Auer — Git4Voc: Git-based Versioning for Collaborative Vocabulary Development

## Contribution

Requirements for versioned collaborative vocabulary work and a set of Git conventions and hooks that meet them.

## Key results

- Abstract: "we advocate that the realization of a powerful version control system is the heart of the problem".
- §II R1: "supporting and recording discussions, changes and their reasons are crucial".
- §II R2: "it is necessary to know which change was made by whom at which time and for what reason".
- §III B: roles enforced in hooks: "an implementation of a pre-push hook can check for the user’s role and permissions".
- §III D: executable checks gate change: "In case that vocabularies fail to pass the validation process, the commit is canceled."
- §III: "Git does not show semantic diffs between versions of vocabulary."
- §V: of WebProtégé, Neologism and VocBench: "The main limitation of the aforementioned tools is the lack of version control."

## Assumptions

Vocabulary development is close enough to software development for its tools to transfer; consensus is reached in discussion outside the artefact (issues), and the reason for a change lives in commit messages and issues by convention, not by schema. No evaluation is reported.

## Concepts

Collaborative vocabulary development; requirements R1–R11; Git hooks (pre-commit, post-commit, pre-push); branching by activity category; one-triple-per-line Turtle; semantic diff; modules of ≤300 triples; release labeling.

## Bearing on the record

VoCol (LIT-tmpt3cxh, EKAW 2016) is closed. Git4Voc is the same first author and group, ten months earlier, and states the approach VoCol implements: vocabularies developed in a Git repository with hooks for validation and documentation. It restates VoCol's design premises (Git substrate, validation, documentation, discussion, roles); it does not restate VoCol's integrated querying/analytics/visualization components, its three-activity model (modeling, population, testing) or its user study.

- **QUESTION-tmps5iou**. **Qualifies the novelty claim strongly.** In 2016 this group already proposed, for vocabularies, much of the mechanics the record treats as luria's: a schema-bearing artefact in Git, executable checks that refuse a change (here at commit; luria at CI), role-based authority over changes, discussion and "reasons" for changes recorded alongside. What it lacks relative to QUESTION-tmps5iou's coupling: (a) a decision record as a typed, citable object that a schema change must cite (reasons are conventions in issues and commits); (b) migration of existing content under a schema change (it has diffs and releases, not migrations); (c) the recorded content is the vocabulary itself, not an inquiry's claims and evidence. So a capability comparison would score Git4Voc yes on checks and authority, partial on rationale, no on migration. It is also an earlier statement of the gate this record runs in CI (docs-check lints a change before it lands), placed at commit time instead.
- **CLAIM-419 / CASE-178**: comparison class for "grammar amended by decision": Git4Voc has amendment by commit and discussion, not by decision record.

## Limitations

No evaluation in the paper; it is a position-and-design paper. Published version (if any) not compared.
