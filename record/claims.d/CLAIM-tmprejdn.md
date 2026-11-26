---
status: Proposed
title: 'A self can be contextual: pairwise-consistent roles with no global presentation'
statement: >-
  A person's roles can be consistent on every occasion where two of their
  contexts meet and still admit no single presentation that satisfies all
  of those occasions together, when the meeting contexts form a cycle; such
  a self is contextual in the sense of local consistency without global
  extension; keeping any one pair of the cycle's contexts apart restores a
  global presentation with no change to the demands of the remaining
  occasions; so segregation can cure incoherence only by opening cycles,
  and context collapse, or a role carried across contexts, can make a self
  incoherent without any two of its presentations ever clashing
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that the role demands people actually face on meeting
  occasions cannot form such a cycle: that whenever every pair of a
  person's meeting contexts is consistent, one presentation satisfies them
  all, so the obstruction is a mathematical possibility with no social
  instance; or that people's felt or social incoherence tracks pairwise
  clashes only, and never arises from a cycle of consistent pairs. Not
  defeated by the rarity of such cycles, which the claim does not deny.
tags:
- self
- contextuality
- social-science
date: '2026-11-26'
line:
- distributed-agency
rests_on:
- CLAIM-153
- CLAIM-196
grounds:
- CASE-052
complements:
- CLAIM-317
- CLAIM-037
bears_on:
- QUESTION-255
summary: >-
  The owner, 2026-11-26, on CLAIM-196 v2: "sort of a tautological
  statement though, isn't it? ... maybe the importance is drawing a
  connection to the contextuality program?" CLAIM-196 says only that
  conflict needs an overlap, which is CLAIM-197 for roles. The non-trivial
  content is CLAIM-153's: two consistent contexts always glue, and the
  obstruction lives on a cycle. Applied to roles, that gives a contextual
  self, a cure by opening cycles, and incoherence without pairwise clash.
  The reframing is the owner's; the statement, the toy check and the
  predictions are the assistant's (Claude, in this session). Adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-196 CLAIM-317 CLAIM-037 CLAIM-417 LIT-tmpdbb0m NOTE-tmptx4q4 — Proposed or new; the base case, its empirical half, the contextuality definition, and the reading cited -->

# CLAIM-tmprejdn: A self can be contextual: pairwise-consistent roles with no global presentation

## The claim

CLAIM-196 v2 says that roles only respectively available in disjoint
contexts cannot conflict. As the owner notes, that is near-tautological:
conflict needs something to conflict on. It is CLAIM-197 ("Disjoint
contexts always glue") for roles. The content the record holds beyond it
is CLAIM-153's: "any two locally consistent contexts glue, and the minimal
model of the obstruction needs three". CLAIM-037 states the general form:
contextuality is failure of global extension. Applied to a person's roles:

1. **A self can be contextual.** Three contexts, say work, family and
   friends, can meet pairwise: a colleague at a family event, a friend at
   the office, family among friends. Each meeting occasion can be met
   consistently, and still no single presentation meets all three. No pair
   of roles conflicts. The obstruction is the cycle.
2. **The cure is to open a cycle, not to change a role.** Keeping any one
   pair of audiences apart removes the obstruction, and the demands on the
   other occasions stay exactly as they were. So segregation strategies
   that work should target cycles of meeting contexts, not pairs and not
   the roles themselves.
3. **Incoherence without pairwise clash.** Context collapse (CLAIM-317)
   that brings three audiences into pairwise contact can make a self
   incoherent though no two of its presentations ever disagree. A role
   carried across contexts can do the same: by memory, anticipation or
   identification (CLAIM-196 v2; NOTE-tmptx4q4), each carried role adds an
   overlap that can close a loop.

## The check

scratch/studies/contextual-self/triangle.py, run with `python3 -I`. Three
contexts each fix a stance on one shared trait, a bit, and three meeting
occasions impose same, same and opposite. The script finds:

- every occasion is satisfiable alone;
- every pair of contexts glues;
- no global presentation exists;
- removing any one occasion leaves two global presentations.

This is the parity, or "liar cycle", form of contextuality, the logical
kind, not the probabilistic.

## What it does not say

- **That such cycles are common.** The toy shows possibility, and the
  defeater asks for social instances.
- **That a contextual presented self is a divided subject.** As in
  CLAIM-196, "self" here is the presented self (TERM-045). CLAIM-417 and
  QUESTION-255 ask whether one unified process can contain models that do
  not glue, and this claim gives that question a concrete case. It does
  not answer it.
- **That the toy's single bit models real role demands.** It shows the
  shape of the obstruction, not its content.
