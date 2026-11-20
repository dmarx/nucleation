<!-- scratch/manuscripts/from-obstruction-to-reorganization/00-abstract-introduction.md -->

# From Obstruction to Reorganization: How an AI-Assisted Research Record Revised Its Own Grammar

*Working title. Alternative: "Nucleating an Inquiry: Anchors, Grammar and Governed Revision in an AI-Assisted Research Record."*

## Abstract

Arguments developed across many sessions with AI collaborators who keep no memory tend to lose track of what was said. Concepts are silently redefined, and the thesis shifts without anyone arguing for the shift. An earlier account from the same project proposed a remedy: a research record that gives each claim, question and term a stable address, so that later work can build on it. That account left an objection standing. The record's grammar, its document types, fields, vocabularies and relations, is fixed before the inquiry knows what it will need.

We read the grammar as part of the inquiry, using the record's own account of inquiry as specification. Changing the grammar is then the inquiry acting on its own regime: refining it by adding distinctions, or revising what counts as an answer, a criterion or a unit of inquiry.

We then study one record, Nucleation, kept with the Luria tool over its first eight weeks (25 September to 20 November 2026). It grew from 214 to over 10,000 files and from five to thirteen schemes. Every one of its 114 decisions was coded against a fixed codebook, with a second coder on a random 30. Agreement was κ 0.81–1.00 on whether a change was a refinement or a revision and on who noticed, proposed, decided and ratified it, and κ 0.65 on the form a misfit took.

Eighty-eight decisions changed the grammar: 62 refinements, 25 revisions and one act of restraint. In most changes made in answer to a misfit, the misfit had first been forced into the nearest category or kept in free text. An audit of all 34 rewordings and removals of vocabulary terms finds two things. Every one came with a decision, and entries were carried through whenever they had to move. When only a term's meaning changed, the 237 entries carrying it were not revisited. Grammar changes migrated 2,664 entries, and ten caused errors that the record later found.

The work of noticing what the grammar needed shifted over the period. Early on, filing agents noticed missing words. Later, review procedures built for the purpose did the noticing. Approval for refinements was granted by category, while judgment about revisions stayed mostly with the owner.

The record measures itself in its own grammar, and its framework was built partly from its own history, so none of this shows that the inquiry improved. We state those limits, and give designs that would test them.

---

## 1. Introduction

### 1.1 From anchors to the grammar they are written in

This project began with a question: when an argument is developed across sessions with collaborators who keep no memory, what makes it settle into stable structure, and what can a project memory contribute (QUESTION-037)?

In the record's own exchanges with AI assistants, arguments did not fail for want of structure. They failed at identity (CLAIM-177). In one documented exchange, a manuscript drafted from an argument's matured state changed the thesis "with no turn arguing the move" and dropped 24 of its items (CLAIM-324). The predecessor manuscript, "luria: nucleating an argument", proposed that a record supplies *anchors*: structures that persist because they can be addressed, on which later structure can grow (CLAIM-182, CLAIM-185).

It also filed an objection against itself, adapted from Shipman and Marshall's "Formality Considered Harmful" (CLAIM-181, LIT-756). A record's grammar formalizes early, so a move it cannot hold is forced into the nearest category, or lost, until someone notices. This paper is about what happened when the record met that objection in practice.

### 1.2 Questions

- **RQ1.** What does the record's account of inquiry imply for a record whose grammar can change (§§2–3)?
- **RQ2.** How did this record actually change its grammar: how often, at what level, by refinement or revision, at what cost, and with what errors (§§6–8)?
- **RQ3.** Who noticed, proposed, decided and ratified those changes, and how did that change over time (§8.4)?
- **RQ4.** What does the answer suggest about delegating the work to assistants, and how could it be tested (§§9, 11)?

### 1.3 Contributions

1. **The record's account of inquiry, gathered as a framework.** It covers drift, anchors and their costs, what a record of inquiry can secure, and inquiry as specification. It is stated with each claim's standing and with its provenance (§2).
2. **A mapping of the Luria tool onto that framework,** with six expectations and the evidence that would falsify each (§3).
3. **A census of all 114 decisions the record made,** coded against a fixed codebook with a second coder (§§5.3, 6.1). The codebook, the coded data and the scripts are in the repository.
4. **An audit of every change to a vocabulary term in the record's history.** It asks whether the change was announced and carried through the entries using the term (§8.2).
5. **A finding about delegation.** Noticing moved from incidental to institutional. Refinement was delegated by category and revision mostly was not (§8.4). The finding is set against the record's own warnings about support that erodes the capacity it supports (§9.1).

### 1.4 Terms

| Term | Meaning |
|---|---|
| Record | The repository of typed documents the project keeps |
| Owner | The single human researcher who directs the project |
| Grammar | What `luria.yaml` declares: schemes, fields, relations, vocabularies, statuses, lines and lint patterns. Conventions held only in prose are not grammar. |
| Line | A named inquiry within the record. Entries carry one or more. |
| Misfit | A move the grammar of the day could not hold faithfully |
| Obstruction | A misfit someone noticed |
| Refinement | A grammar change that adds a distinction while leaving what counts as an answer, criterion or unit of inquiry unchanged |
| Revision | A grammar change that changes one of those |
| Decision record (ADR) | A dated document stating a decision, its context, alternatives and consequences |
| Unit of work | The pull request a change came in |
| Filing agent | A subagent that reads and files a batch of works |
| A12, U9 | Numbered assistant (A) and user (U) turns of a filed exchange |
| Tier 1–3 evidence | Recorded rationale, observed operation, measured outcome (§5.4) |
| Active, Proposed | An entry the record accepts, or one filed and argued but not adopted |

Codes such as CLAIM-470 or ADR-042 name entries in the record. Where an entry's standing matters, it is given beside the code.

### 1.5 Relation to the predecessor

This paper succeeds "luria: nucleating an argument" (the work `luria-nucleating-an-argument`, proposed on 11 October 2026). Its argument is now held in three lines: `nucleating-argument`, `records-of-inquiry` and `record-as-apparatus`. ADR-082 split them apart on 7 November.

The predecessor's thesis stands. What changes is its scope. The anchors are written in a grammar, and the grammar needs the same traceability the anchors were meant to provide. Several results now qualify the first account:

- persistence is not productivity (CLAIM-595);
- the second-occurrence rule's two justifications part when filing is dear (CLAIM-630);
- conclusions, support graphs and sufficient states each fall short of what revision needs (CLAIM-293, CLAIM-294, CLAIM-300).

### 1.6 Roadmap

- **§2** sets out the framework and its provenance.
- **§3** maps Luria onto it and states the expectations.
- **§§4–5** give related work and method.
- **§6** presents the census and eight cases drawn from it.
- **§7** describes the record's governance in four loops.
- **§8** grades each expectation.
- **§9** discusses delegation, distinction-drawing, maintained capacity and the signatures of misfit.
- **§§10–12** give threats to validity, future evaluation and the conclusion.
