---
status: Read
paper: LIT-tmpsj7au
title: 'Lesser and Erman — A Retrospective View of the Hearsay-II Architecture'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from the copy named in the reading. **Read** (the body:
    abstract, overview of the Hearsay model and the Hearsay-II architecture,
    configurations C1 and C2, experiences with the blackboard data base,
    knowledge-source interaction and control, KS independence). The appendix
    of KS descriptions and the references were skimmed. The scan's OCR is
    imperfect (e.g. "Hear say -11", "Ermo.n"); quotes below were chosen from
    clean passages and checked against the extracted text. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  The Hearsay model attacks "errorful" knowledge-intensive problems with
  many separate knowledge sources (KSs) that interact only through a global,
  multi-level data structure, the blackboard. In Hearsay-II each level
  (segment, syllable, word, phrase) holds hypotheses with a uniform
  attribute-value structure: level, label, time span, AND/OR links to
  supporting hypotheses, validity ratings summarized as a rating state
  (Unrated, Neutral, Verified, Guaranteed, Rejected), and any attributes a
  KS chooses to add. KS preconditions declare which blackboard changes
  interest them and are triggered by them; a scheduler ranks pending KS
  activations.
---
<!-- inactive-ok-file: CLAIM-tmp8qsef LIT-tmpwza8d — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp83mjv: Lesser and Erman — A Retrospective View of the Hearsay-II Architecture

## Key results

- Blackboard: "Each hypothesis, no matter what its level, has a uniform attribute-value structure." and "New attributes can be created by any KS".
- Revision by addition: "In the C2 configuration, hypothesis credibility is never modified in an explicit sense; rather, new and different hypotheses are created." with the side effect that "hypotheses are never deleted from the blackboard".
- Interaction: "KSs did not in general interact by modifying previously-made assumptions" but by adding hypotheses or verifying unverified ones.
- Independence: complete KS independence was not achieved, yet "the "subroutine interaction problem" did not haunt us", which they credit to data-directed activation.
- The central weakness: "the state information associated with an hypothesis is very local and does not adequately characterize the state(s) of the hypothesis network(s) connected to it".
- Shared versus private structure: "there are advantages to specialization of structures: one for KS interaction (i.e., the blackboard), and separate ones for each KS" (a parser moved off the blackboard ran two orders of magnitude faster).

## Assumptions

Contributors are programs written by one project team; the blackboard's structure is fixed by the architecture (levels, attributes) though KSs may add attributes; credibility is a number assigned by KSs; the goal is one correct interpretation of an utterance.

## Concepts

Blackboard; knowledge source (precondition, action); levels of representation; hypothesis with rating state; AND/OR support network; data-directed activation; stimulus and response frames; scheduler and focus of attention; policy KSs; islands of reliability; goal nodes (proposed, not implemented).

## Bearing on the record

Two of LIT-tmpwza8d's four authors, describing and assessing the same architecture three years before the 1980 survey. It restates the blackboard, the knowledge sources, data-directed activation and scheduling; it does not give the 1980 paper's final performance figures or full system account.

- **QUESTION-tmpxq2sb** (does a shared, typed, governed record help agents holding different evidence?). **Supports A's caveat that a shared structured workspace is not new.** By 1977 a shared store of typed claims with standing and support links, written by independent anonymous contributors and triggering their work, was built and assessed. It does not bear on the question proper: no hidden-profile distribution, no comparison with a communication protocol, no governance of the shared structure by its users.
- **CLAIM-tmp8qsef** (the record reports dependants of a retired entry; no rule over the support graph and statuses decides them correctly). **Corroborates a neighbouring point, does not test the claim.** Lesser and Erman report that per-hypothesis state "does not adequately characterize" the network it supports, and that re-evaluating credibility automatically through the support network was built in C1 and abandoned in C2 for creating new hypotheses instead. That is a historical instance of an automatic propagation scheme given up in practice. It is not evidence that no correct rule exists.
- **Retire by status, never by deletion** (CLAUDE.md rule; ADRs on retirement): Hearsay-II C2's "hypotheses are never deleted" and revision-by-new-hypothesis is an early precedent of the same practice, adopted there for efficiency. Mention in the NOTE's Connections.
- **NOTE-339 / LIT-444** (Singh: blackboards don't scale past a few agents, C6 weak): Hearsay-II's configurations had about a dozen named KSs, with pending tasks that "often exceeds 200"; it neither confirms nor refutes Singh's claim about hundreds of agents.

## Limitations

OCR'd scan; the appendix's KS details not read closely. A 1977 interim assessment; the 1980 survey may revise it.
