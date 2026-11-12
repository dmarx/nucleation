---
status: Proposed
title: 'software-engineering joins the topics'
version: 1
tags:
- taxonomy
date: '2026-11-12'
summary: >-
  One topic word joins the closed vocabulary. `software-engineering` takes
  how software is specified, built, tested and changed: test oracles and
  metamorphic testing, reflective and metaobject architectures,
  self-adaptive systems and models kept at run time, model-driven
  engineering and the coupled evolution of metamodels and their
  instances, and version control and change management. It enters because
  the filing of the exchange "luria experiment design" verified two works
  and held them back with no word to file them under, and the owner
  accepted the filer's proposal to add one. First applied to those two
  works, and beside the existing tags of two held works it covers.
  Rejected: filing them under the nearest words (`logic`, `databases`,
  `design-rationale`), and a broader `computer-science`. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: LIT-tmp8v1tl LIT-tmpiyp1o — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: LIT-2305 LIT-2311 LIT-2312 LIT-2313 — Deferred; cited for what each holds, not as settled -->

# ADR-tmppzz2h: software-engineering joins the topics

## Context

The filing of the exchange "luria experiment design" (2026-11-10,
https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda; curation
entry of 2026-11-12, pull request #484) verified the identifiers of two
works A cited at A50 and did not register them:

- Chen, Kuo, Liu et al., "Metamorphic Testing: A Review of Challenges and
  Opportunities" (ACM Computing Surveys, 2018), cited for metamorphic
  relations as an oracle where no single expected output can be written,
  which A proposed for scoring changes to a record's schema;
- Kiczales, des Rivières and Bobrow, *The Art of the Metaobject Protocol*
  (MIT Press, 1991), cited for a system that exposes its own behaviour to
  modification through a meta-level interface.

The vocabulary's alert says a work that wants a word the list lacks gets
it "with a label, a blurb and a decision", and CLAUDE.md that it is "never
replaced by the nearest wrong one". The nearest words were `logic` (valid
inference), `databases` (how stored data is organized) and
`design-rationale` (recording reasons for a design). None names what the
works are about. The filer listed the two as left and offered the word as
one of its own ideas; the owner accepted those ideas ("file their ideas
too, I like ideas"). ADR-062 records the owner's word that the vocabulary
may be expanded where merited.

The record already held works of this kind without a word: the vision of
autonomic computing (LIT-2312) and models at run time (LIT-2305), filed on
2026-11-10 under `control-theory` with `complex-systems` and
`design-rationale`.

## Decision

Add one topic, **`software-engineering` (Software engineering)**: how
software is specified, built, tested and changed. It covers:

- testing and test oracles, metamorphic testing among them, and
  verification against specifications;
- reflective and metaobject architectures;
- self-adaptive systems and models kept at run time;
- model-driven engineering and the coupled evolution of metamodels and
  their instances;
- version control and change management.

How it is applied:

- **First** on the two works held back, now registered Deferred:
  LIT-tmp8v1tl (Chen et al.) and LIT-tmpiyp1o (Kiczales et al.), where it
  is the only word and the primary.
- **Beside the existing tags** of LIT-2312 and LIT-2305, whose subject it
  is. Nothing removed, primaries unchanged; each takes a version bump.
- **Not** to ontology and schema change read as the organization of
  stored data, which stays with `databases`, as KGCL (LIT-2313) and
  EvoOntology (LIT-2311) are filed; nor to benchmarks of coding agents,
  which are machine-learning evaluation and belong to the anthology
  (ADR-048). COPE, filed from the same exchange in pull request #484 under
  `databases` and `design-rationale`, can take the word beside its tags
  once both are merged.

## Alternatives

- **The nearest words.** `logic` for metamorphic relations and
  `design-rationale` for the metaobject protocol are each defensible in a
  phrase and wrong as a statement of what the work is about, which is the
  case the vocabulary's rule forbids.
- **A broader `computer-science`.** It would take algorithms, databases
  and information retrieval, which have words of their own, and say
  nothing about the engineering of changing software, which is why these
  works are here.
- **Leave the two works unregistered.** That keeps the vocabulary small,
  but drops two verified works the exchange cited for the record's own
  evaluation, and records nothing of the class it has started to collect.

## Consequences

- `luria.yaml` gains the term, with its blurb, after `control-theory`.
  docs/record.md and the topic pages are regenerated by CI, not edited.
- Future works on testing, reflective systems and self-adaptive software
  file here; the blurb says where schema change and coding agents go.
- Proposed until the owner adopts it, as with every topic decision so far.
