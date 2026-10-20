---
number: 230
# Don't copy this file by hand — run `luria new question`. A QUESTION is an
# open question the record's own argument is organised around. Claims and
# THEORY readings name it in `answers`, and its page shows both (ADR-032).

# Open | Answered | Dissolved | Deferred | Superseded
status: Open
formerly:
- QUESTION-tmp9l9pn

# The question, as a question. Repeat it as the `# QUESTION-…:` heading.
title: "Do the released HNSW, NSG and fast-preprocessing DiskANN builds, run independently on Indyk and Xu's published hard instances at the stated parameters, need a search queue of about a tenth of the points before recall@5 rises above zero, and does the same trap appear on natural data with adversarially chosen queries?"

version: 1
tags:
- databases
- information-retrieval
date: '2026-10-20'

# REQUIRED: the line of inquiry, from `lines` in luria.yaml.
line: 'distributed-agency'

# refines: [QUESTION-000]   # the broader question this sharpens

refines:
- QUESTION-114
summary: >-
  The promotion condition formerly on [THEORY-368](../theory.d/THEORY-368.md). [THEORY-368](../theory.d/THEORY-368.md) was promoted on
  2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v3) for what Indyk and Xu's one study measured. An
  independent replication on their instances, and the same test on natural
  data with adversarial queries, are open.
---

<!-- unresolved-ok-file: QUESTION-000 — the placeholder a new document replaces -->

# QUESTION-230: Do the released HNSW, NSG and fast-preprocessing DiskANN builds, run independently on Indyk and Xu's published hard instances at the stated parameters, need a search queue of about a tenth of the points before recall@5 rises above zero, and does the same trap appear on natural data with adversarially chosen queries?

## Why it is a question

[THEORY-368](../theory.d/THEORY-368.md) holds Indyk and Xu's measurement on two-dimensional point sets
built to trap best-first search. On those sets, the authors' code for
fast-preprocessing DiskANN, HNSW and NSG in most cases found none of a
query's five nearest neighbours until the queue held about 10% of the
points. At that queue length ten graph indexes averaged recall@5 between
0.0 and 0.42. That is one study, with one query per instance. Until
2026-10-20 an independent run was [THEORY-368](../theory.d/THEORY-368.md)'s promote_when.

An answer is an independent run of the published instances, which are
on the authors' GitHub, with the released HNSW, NSG and DiskANN code at
the stated parameters. It should report recall@5 against queue length.
A second answer, which the authors list as open, is the same failure on
natural data with adversarially chosen queries. A proof of a linear
lower bound for one of these builds would be a different and stronger
result. Benchmarks on natural queries cannot settle it.
