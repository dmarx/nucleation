---
number: 815
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'
formerly:
- THEORY-tmp880z4

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: 'A proof that greedy layered search on the graph HNSW actually builds, with a fixed number of pruned links per element and not an exact Delaunay graph, takes expected O(log N) distance computations to reach a stated recall, under a stated condition on the data, such as bounded intrinsic or doubling dimension. It is refuted for that class by a family of datasets meeting the condition on which the cost needed for a fixed recall grows faster than log N. More benchmarks at fixed dimension cannot settle it. They re-establish low-dimensional measurements that are already held, and they cannot reach the sizes at which the paper says the high-dimensional case could be checked.'

# The claim. Repeat it as the body's `# THEORY-815:` heading; the lint checks
# that the two agree.
title: "Layering a navigable small-world graph on nested random subsets of the data, with links separated by length scale and each layer's degree capped, makes greedy nearest-neighbour search cost grow logarithmically with the number of items on data of low intrinsic dimension, where the single-layer graph's cost grows polylogarithmically"

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- databases
- information-retrieval
- network-science

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-1098

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Malkov and Yashunin (2020), [LIT-1098](../literature.d/LIT-1098.md), read in [NOTE-916](../notes.d/NOTE-916.md), argue that HNSW's hierarchy is what makes greedy search logarithmic: constant cost per layer over O(log N) layers, against the polylogarithmic cost of their earlier flat graph. The record holds as measured, in [THEORY-365](THEORY-365.md), logarithmic-or-better cost on uniform data in 8 dimensions and a saturating beam width in 4. The bound is derived only for exact Delaunay layers, which HNSW does not build, and on 200 million SIFT vectors the paper's own scaling departs from a logarithm, so the thesis is stated for low intrinsic dimension.
extends:
- THEORY-365
answers:
- QUESTION-187
---


# THEORY-815: Layering a navigable small-world graph on nested random subsets of the data, with links separated by length scale and each layer's degree capped, makes greedy nearest-neighbour search cost grow logarithmically with the number of items on data of low intrinsic dimension, where the single-layer graph's cost grows polylogarithmically

## Source

Malkov and Yashunin (2020), [LIT-1098](../literature.d/LIT-1098.md), read in [NOTE-916](../notes.d/NOTE-916.md) from arXiv v4.
They present HNSW as a skip list generalized from linked lists to
proximity graphs, and argue that separating links by length scale into
layers, with the degree capped on every layer, makes search cost constant
per layer over O(log N) layers, so logarithmic overall. They contrast it
with their earlier single-layer navigable small-world graph, whose cost
they put at polylogarithmic because both the hop count and the hub
degree on the greedy path grow as log N.

## What is asserted, and by whom

The thesis is that the hierarchy is what makes greedy search
logarithmic: layering a navigable graph on nested random subsets, each
element's top layer drawn geometrically and each layer's degree capped,
turns the flat graph's polylogarithmic cost into a logarithmic one.
Malkov and Yashunin assert it, qualified throughout by low dimension
("in agreement with the simulations on low dimensional datasets").

## What the record holds toward it

- [THEORY-365](THEORY-365.md) (Active): on uniform random data in 8 dimensions the number
  of distance computations grew no worse than logarithmically and stayed
  below the flat graph's at every size tested; in 4 dimensions the beam
  width needed for a fixed recall saturated.
- The logarithmic bound is derived only for exact Delaunay graphs of
  bounded degree. HNSW does not build those, and Delaunay degree grows
  exponentially with dimension.
- Against it: on 200 million SIFT vectors (d = 128) the paper reports
  that the scaling "deviates from the pure logarithm". The thesis is
  therefore stated for low intrinsic dimension only.

## What this does not say

- Not that HNSW's search is logarithmic in high dimension.
- Not a recall guarantee or a worst-case bound; the paper gives neither.
- Not that the flat graph's polylogarithmic growth was measured here: it
  is the paper's account of the authors' earlier work. Only "below NSW
  at every size" was measured.

## What would confirm or reject it

Confirmed by the promote_when: a proof for the graphs HNSW actually
builds, under a stated condition on the data. Rejected for a class of
data meeting that condition by datasets on which the cost needed for a
fixed recall grows faster than log N. [QUESTION-187](../questions.d/QUESTION-187.md) asks the same thing
as a question; this entry is the answer Malkov and Yashunin propose.
