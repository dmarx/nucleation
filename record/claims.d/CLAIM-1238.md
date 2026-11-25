---
number: 1238
status: Proposed
formerly:
- CLAIM-tmp6xzjy
title: 'Pairwise views can fail around a cycle'
statement: >-
  Views whose correspondences all pass through one source satisfy the
  cocycle condition by construction, as charts of a given space do, while
  views related to one another pair by pair can be compatible on every
  overlap and inconsistent around a cycle of three, so an atlas of such
  views must check its compatibility on cycles and not only on pairs
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: transition maps induced by maps into one
  source failing the cocycle condition on some triple overlap, or three
  pairwise-satisfiable correspondences on a cycle of views with nonzero
  holonomy admitting a joint assignment. That a real atlas of
  hyperarticles has no cycles of overlaps would narrow its application,
  not defeat it.
tags:
- mathematics
- design-rationale
date: '2026-11-25'
line:
- record-as-apparatus
- formal-apparatus
rests_on:
- CLAIM-153
- CLAIM-538
complements:
- CLAIM-1297
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A49, A57 and A59 of the exchange "Hyper article
  interpretation" (2026-11-25). A49 notes that a differential-geometric
  atlas "assumes mathematically well-defined compatible coordinate
  transitions" and research representations do not, but does not say
  what compatibility then requires; A59's "initial transition map" lists
  only pairs of views. The record already holds the answer in its
  formal apparatus: two contexts always glue and the minimal obstruction
  is a cycle of three ([CLAIM-153](CLAIM-153.md), [CLAIM-538](CLAIM-538.md)). Checked with python3 -I.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
---

<!-- inactive-ok-file: ADR-143 TERM-168 — Proposed, Open or new; the thesis it completes, the owner's, the tolerance result, the manuscript protocol, the route term and the holonomy question -->

# CLAIM-1238: Pairwise views can fail around a cycle

## The gap

A49 sets the atlas against its limit: "In ordinary differential
geometry, the space is given and the charts describe it." A57 asks that
the atlas's overlaps become "first-class objects", and A59 records
"transition obligations" as a table of pairs (01 ↔ 03, 02 ↔ 03, 02 ↔ 15,
and so on). Neither says what compatibility requires when the space is
not given.

## The derivation

**Charts of a given space.** If each view i maps into one common source by
φ_i, the transition between two views on their overlap is
T_ij = φ_j ∘ φ_i⁻¹, and on any triple overlap
T_jk ∘ T_ij = φ_k ∘ φ_j⁻¹ ∘ φ_j ∘ φ_i⁻¹ = T_ik. The cocycle condition
holds by construction, whatever the φ_i are.

**Transitions recorded pair by pair.** If instead each pair of views
carries its own correspondence, as an offset α_ij in a group, the pairs
are not tied together. Each pair alone can always be met. Around a cycle
of three the residuals x_j − x_i − α_ij sum to −Φ, with holonomy
Φ = α₁₂ + α₂₃ + α₃₁, whatever the assignment x, so a joint assignment
exists exactly when Φ = 0. That is [CLAIM-153](CLAIM-153.md)'s result (two contexts always
glue; the minimal obstruction needs three), and with tolerances [CLAIM-538](CLAIM-538.md)'s
(an assignment within every tolerance exists exactly when no cycle's
holonomy exceeds the sum of its tolerances).

**Check** (python3 -I, this session): with random invertible 3×3 φ_i the
induced cocycle error is 8.9 × 10⁻¹⁶. With α₁₂ = α₂₃ = α₃₁ = 1, each pair is
satisfiable, Φ = 3, and over a grid of assignments the least achievable
largest residual is 1.000 = Φ/3; with tolerance 0.5 on each overlap no
joint assignment exists, while α = (1, 1, −2), Φ = 0, is met exactly.

## What follows for the record

- **Its generated views are charts of a given space.** Luria derives every
  view from one set of sources ([LU-DP-003](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-3)), so the views it generates
  cannot be pairwise consistent and jointly inconsistent: any conflict
  among them is a conflict among the sources, where it is visible as an
  objection.
- **Its manuscripts are made charts of a given space by protocol.** A
  manuscript is outside the record ([ADR-143](../decisions.d/ADR-143.md)), so its correspondence is
  not generated. [ADR-143](../decisions.d/ADR-143.md)'s second and third invariants route it through
  the record: every step cites its entry, and every join is filed in the
  record before the manuscript is ready. That is what makes the cocycle
  condition hold for manuscripts too.
- **A transition stated between two views directly, not through the
  record, is the case that can fail.** A59's table is of that kind, and
  its manifests' neighbours already form cycles (02, 03 and 15). Checking
  each pair, as the table proposes, cannot find a cycle obstruction. The
  remedy is the one the record already uses: state the correspondence as
  an entry, so that it passes through the source, or check it on cycles.

## What it does not say

- That hyperarticles' correspondences are offsets in a group. The
  derivation needs only that transitions compose; the group model is the
  smallest case that shows the cycle obstruction, as [CLAIM-153](CLAIM-153.md) uses it.
- That routing through one source makes the views correct. It makes them
  mutually consistent with the source; whether the source is right is
  another question ([CASE-084](../cases.d/CASE-084.md)).
- An orbit in A61's sense, a route that "returns to an earlier question,
  but with the reader now equipped to understand it differently"
  ([TERM-168](../terms.d/TERM-168.md)), is formally a loop with nontrivial holonomy. That is
  an analogy only, and [QUESTION-130](../questions.d/QUESTION-130.md) holds the record's open question on
  holonomy around loops of evaluative contexts.
