---
number: 197
status: Active
formerly:
- CLAIM-tmpk4fd7
title: 'Sections over contexts that do not overlap always glue, so a sense that differs between disjoint contexts is not a gluing failure: a failure needs an overlap carrying sections that disagree, and which families count as covers decides whether anything glues'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Dual-filed from MOM-CLM-088 under ADR-037. Active here after a
    re-check of the two things it rests on. The argument was re-derived:
    for a cover {U₁, U₂} of U with U₁ ∩ U₂ = ∅, the compatibility
    hypothesis has nothing to compare, and the sheaf condition gives a
    unique section of U restricting to each. The quotations were checked
    against MoM's source chapters at MoM d987e2a: the sheaf condition (v1
    §10.4), the "tall" example (§10.6) and the opposite diagnosis in
    "Epistemic Drift and Semantic Simulation" (§11.3.3) are verbatim.
role: thesis
defeated_if: >-
  A phenomenon modelled as a sheaf over a stated coverage in which
  sections over disjoint members of a cover fail to glue. That would show
  the model is not a sheaf, not that the theorem fails, so the claim
  would then be retracted for that phenomenon only. A disagreement
  between contexts with no stated coverage does not count.
tags:
- mathematics
- contextuality
- philosophy-of-language
date: '2026-10-12'
line:
- pragmatic-transport
- formal-apparatus
complements:
- CLAIM-143
- CLAIM-153
summary: >-
  Dual-filed from [MOM-CLM-088](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-088.md) ([ADR-037](../decisions.d/ADR-037.md)). The sheaf condition says a
  family of sections that agree on overlaps glues to one global section.
  Where two contexts do not overlap, agreement is vacuous and they glue.
  So "tall", which takes one threshold for people and another for trees,
  is one global section with the comparison class part of the meaning,
  not a failure of gluing. A failure needs contexts that overlap and
  carry sections that disagree there. Which families count as covering
  is the piece that decides whether anything glues, and a sheaf picture
  of meaning that does not state it has decided nothing.
illustrated_by:
- CASE-048
- CASE-052
supports:
- CLAIM-198
- CLAIM-196
---
<!-- inactive-ok-file: CLAIM-251 — Proposed; filed 2026-10-12 from the interlocutor's reading as advice, cited in a note as open -->
<!-- inactive-ok-file: CLAIM-143 — Proposed; the general point this claim gives the simplest instance of -->
<!-- inactive-ok-file: CLAIM-198 — Proposed; the consequence drawn from this claim, cited forward -->
<!-- inactive-ok-file: CLAIM-105 CLAIM-201 CLAIM-257 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

# CLAIM-197: Sections over contexts that do not overlap always glue, so a sense that differs between disjoint contexts is not a gluing failure: a failure needs an overlap carrying sections that disagree, and which families count as covers decides whether anything glues

## The claim

From [MOM-CLM-088](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-088.md), which reads the sheaf-semantics chapter of the MoM
manuscript (v1 §10). The chapter states the sheaf condition in full. "If
{U_i} is a cover of U", and the predicates p_i agree on the overlaps
U_ij = U_i ∩ U_j, "then there exists a unique global predicate p". It then
offers "tall" as the case that fails: "In Human-context, 'is tall' applies
with threshold >2 meters. In Tree-context, 'is tall' applies with
threshold >20 meters. These local definitions do not glue."

They do. People and trees do not overlap, so U_human ∩ U_tree is empty
and the compatibility hypothesis holds with nothing to check. The
condition the chapter printed then gives a unique global section: apply
2 m to people and 20 m to trees. That is how gradable adjectives work,
with the comparison class part of the semantics. One chapter later the
same example gets the opposite diagnosis, that the two senses are
"forcibly glued into an illusory global predicate". Neither diagnosis
holds. With an empty overlap there is nothing that could fail and
nothing to force.

Two things follow, and they are what this record needs.

- **A gluing failure needs an overlap.** It is a context, or a pair of
  overlapping contexts, in which the sections disagree. [MOM-CLM-088](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-088.md)
  supplies one for "tall": a single conversation about both skyscrapers
  and houses carries two thresholds in one context, and there the
  restriction maps conflict.
- **The cover decides.** A sheaf needs a rule saying which families count
  as covering. On a bare order of contexts with no such rule, the sheaf
  condition is either vacuous or whatever is stipulated, and which
  families cover is what decides whether any concept glues.

## Why this record holds it

The record has met the general point already. [CLAIM-143](CLAIM-143.md) says local
descriptions that disagree establish no obstruction until the
correspondences are fixed, and [CLAIM-144](CLAIM-144.md) and [CASE-039](../cases.d/CASE-039.md) find the
relativity example was never a gluing failure. This claim adds the
simplest instance, and the rule that catches it: before calling anything
a failure to glue, name the overlap.

It bears most on the self. The same MoM chapter (v1 §11.5) treats a
person's roles, "daughter", "teacher" and "friend", as sections over
family, professional and social contexts, and identity as their global
section. Read as written, roles in contexts that do not meet cannot
contradict each other. [CLAIM-153](CLAIM-153.md) already works with contexts that overlap
in pairs. The consequence for interests over time is drawn in
[CLAIM-198](CLAIM-198.md).

## What it does not say

- **That context-relative meaning is never a problem.** Contested
  evaluative vocabulary is where contexts overlap and the sections
  disagree, and that is the general case [MOM-CLM-088](https://github.com/dmarx/mathematics-of-meaning/blob/main/record/claims.d/CLM-088.md) names.
- **That the sheaf picture is wrong.** The machinery is right. The claim
  is about where it has been aimed.
- **What the right coverage is** for meaning or for a self. That stays
  open here, as it is in MOM.

## Note of 2026-10-12: a change of cover filed on 2026-10-10

PR [#121](https://github.com/dmarx/nucleation/issues/121) filed [CLAIM-201](CLAIM-201.md) and [CLAIM-257](CLAIM-257.md), which make a change of
cover the surviving form of [CLAIM-105](CLAIM-105.md)'s headline. There a context is "a
question whose answers readers give determinately", and a rendering
changes the cover when a question determinate for one side's readers is
indeterminate for the other's. This claim says which families count as
covers decides whether anything glues. [CLAIM-201](CLAIM-201.md) says a change of
cover is not thereby contextuality: it has "changed which questions can be
asked, not shown that the answers cannot be glued". The record does not
say whether this claim's coverage and PR [#121](https://github.com/dmarx/nucleation/issues/121)'s operational cover are one
notion, and the entries are not related; that is left to the owner.

## Note of 2026-10-12: the interlocutor's reading, as advice

The interlocutor's reading of 2026-10-12 says this claim "supplies an essential mathematical correction, but it does not necessarily defeat the transport proposal", and that the operational notion of [CLAIM-201](CLAIM-201.md) should get "a different formal name until an explicit functorial or sheaf-theoretic relationship is established". Filed as the counter [CLAIM-251](CLAIM-251.md). Recorded as advice.
