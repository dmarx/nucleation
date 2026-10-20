---
number: 225
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmpo255i

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Are why-provenance and, for traceable queries, where-provenance preserved by Buneman, Khanna and Tan's rewrite system, and is traceability necessary for where-provenance to be preserved?"

version: 1
tags:
- databases
- logic
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'nucleating-argument'

# refines: [QUESTION-000]   # the broader question this sharpens

refines:
- QUESTION-105
summary: >-
  Formerly part of [THEORY-367](../theory.d/THEORY-367.md)'s title. [THEORY-367](../theory.d/THEORY-367.md) was promoted on 2026-10-20
  ([ADR-047](../decisions.d/ADR-047.md) v2) for what is re-derived: minimal witnesses are invariant across
  equivalent SPJU queries, and where-provenance is not. Whether the paper's
  rewrite system preserves why- and where-provenance, and whether traceability
  is necessary, is open.
---

<!-- unresolved-ok-file: QUESTION-000 — the placeholder a new document replaces -->

# QUESTION-225: Are why-provenance and, for traceable queries, where-provenance preserved by Buneman, Khanna and Tan's rewrite system, and is traceability necessary for where-provenance to be preserved?

## Why it is a question

Buneman, Khanna and Tan (2001) state that their rewrite system preserves
the witness basis (Lemma 1), and that it preserves where-provenance for
traceable queries (Proposition 2). The paper does not give the rules or the
proofs, so the record cannot check either result. [THEORY-367](../theory.d/THEORY-367.md)'s former title
also said where-provenance is preserved "only" for traceable queries. The
paper shows that traceable queries preserve it, not that queries outside the
class fail to.

An answer is a read proof of Lemma 1 and Proposition 2 for a stated rewrite
system, from a full or journal version. A further answer would be a
non-traceable query and a rewriting that changes its where-provenance, or a
proof that preservation needs traceability. For the revision question
[QUESTION-105](QUESTION-105.md) asks, the rewrite results matter less than the invariance
[THEORY-367](../theory.d/THEORY-367.md) now holds. They decide whether a stored witness basis survives
query optimisation.
