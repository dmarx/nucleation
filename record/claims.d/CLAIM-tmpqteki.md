---
status: Proposed
title: "A record of a student's collaboration with an LLM is not proof of understanding but a better basis for questioning it: who first proposed a step, how it was evaluated and whether it was adopted are different pieces of information, and the submission becomes a view over a learning process"
version: 3
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
- version: 3
  date: '2026-11-25'
  note: >-
    Joins the work hyperarticles (ADR-tmp85hdc): Article 3 of A45 in the
    exchange "Hyper article interpretation" states its proposition without
    citing it, in §9. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that instructors given the collaboration record and free to
  question the student assess understanding no better than from the
  submission alone (LEAD-tmphmakt), or that the record's separation of
  proposal, evaluation and adoption cannot be kept for a student's work.
tags:
- philosophy-of-technology
- epistemology
date: '2026-11-25'
line:
- records-of-inquiry
- scholarly-publishing
rests_on:
- CLAIM-tmp0ncly
- CLAIM-668
bears_on:
- QUESTION-072
summary: >-
  A35 of the exchange "Hyper article interpretation" (2026-11-22), on the owner's [CLAIM-tmp0ncly](CLAIM-tmp0ncly.md):
  "Right now, educational assessment often treats the submitted artifact as a
  proxy for the student's understanding. LLMs make that proxy substantially
  less reliable." A record of the collaboration is not the remedy by itself:
  "A detailed history isn't proof of understanding, and provenance can be
  incomplete or misrepresented. But it could give instructors a substantially
  better basis for asking questions." "The final submission becomes a view
  over a learning process." The wording is A's (ChatGPT's, at A35 of the
  exchange "Hyper article interpretation"); adopting it is the owner's call.
works:
- hyperarticles
---

<!-- inactive-ok-file: CLAIM-668 — Proposed; the premise that a record can represent who contributed -->
<!-- inactive-ok-file: CLAIM-tmp0ncly CLAIM-tmpmacjk — new; filed from the same exchange -->

# CLAIM-tmpqteki: A record of a student's collaboration with an LLM is not proof of understanding but a better basis for questioning it: who first proposed a step, how it was evaluated and whether it was adopted are different pieces of information, and the submission becomes a view over a learning process

## The claim

A35: "An LLM can propose a claim. A student can reject it, modify it, test
it, or adopt it. The fact that the model generated the first formulation
doesn't establish who did the intellectual work necessary to make it
defensible." The record keeps apart who first proposed a step, how it was
evaluated, and whether it was adopted, and those are what an instructor wants
to question: "Why did you reject this suggestion? What evidence supports this
step? How would the argument change if this assumption were false? Can you
solve a related problem without assistance?"

So the record does not certify learning. It moves assessment from inferring
the process from a polished product to questioning the student where the
record shows a decision. A35's conditions: "Recording the process needs to be
inexpensive, respect student privacy, and avoid turning every assignment into
an exercise in surveillance or metadata management. Instructors also need
ways to assess understanding independently of the record."

## A correction to A35's attribution

A35: "this connects directly to Nucleation's distinction between a
contribution's *origin*, its *standing*, and its *warrant*." The record's
three are not those. [ADR-043](../decisions.d/ADR-043.md) keeps apart a claim's `status` (the record's
credence), its `role` (thesis, counter, granted, disclaimed or supposed: its
place in the dialectic) and its `warrant` (demonstrated, empirical or
interpretive). Origin, who said it, is no field: it is the voice line each
entry's summary carries ("The wording is A's ..."), under [ADR-068](../decisions.d/ADR-068.md)'s sixth
invariant, and [CLAIM-668](CLAIM-668.md) is the claim that a record can represent it. A35's
point survives the correction; its citation does not.

## What it does not say

- Not that the record is reliable as provenance; [CLAIM-tmpmacjk](CLAIM-tmpmacjk.md) says what
  that takes.
