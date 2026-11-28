---
number: 1414
status: Proposed
formerly:
- CLAIM-tmpi0rdz
title: 'Entrenchment needs one-way moves or a lower budget'
statement: >-
  Reading A23's "can become entrenched" as ◇□C, possibly necessarily
  consequential, over reachability within a budget: under peak costs with
  reversible moves and free holding the frame at one budget is S5, where
  ◇_b□_b C implies □_b C, so a distinction whose consequentiality is latent
  at a configuration (¬C there) cannot be made entrenched within the same
  budget; latent-then-entrenched consequentiality needs one-way moves, or
  an entrenchment relative to a smaller budget than the one used to reach
  it, ◇_b□_{b'} C with b' < b, which the budget tree supplies
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A reversible move graph with peak costs and free holding, a budget b, a
  valuation and a configuration at which C fails and ◇_b□_b C holds; or a
  one-way peak graph in which ¬C ∧ ◇_b□_b C is unsatisfiable at every
  configuration whatever the valuation. Readings of A23's modal table
  over some accessibility other than reachability within a budget are
  outside it.
tags:
- logic
- mathematics
- society-and-governance
date: '2026-11-26'
line:
- realizability
- formal-apparatus
- governing-possibility
rests_on:
- CLAIM-1439
- CLAIM-581
uses:
- TERM-185
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A23 §10 of the exchange "Alignment consequences
  brainstorm" (ChatGPT, 2026-11-26), whose table of modal expressions for
  potential consequentiality reads ¬C_i(d) ∧ ◇C_i(d) as "Its
  consequentiality is latent" and ◇□C_i(d) as "It can become entrenched",
  "particularly interesting in the context of our discussion of contracts,
  institutional commitments and lock-in". A23 does not say over which
  accessibility relation. Over A19's budgeted reachability the two rows
  cannot be combined at one reversible peak budget: in S5 ◇□φ → □φ, so
  entrenching a latent distinction needs irreversibility or a drop in
  budget. Checked with python3 -I. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1439 LIT-3315 TERM-185 — Deferred, Proposed; filed, registered or cited in the filing of 2026-11-26 from the exchange "Alignment consequences brainstorm" -->

# CLAIM-1414: Entrenchment needs one-way moves or a lower budget

## The gap

A23 §10 defines C_i(d), "distinction d is consequential to process or
party i", and reads ◇_{B,T}C_i(d) as "within a declared resource and
temporal envelope, an organizational transformation can establish
conditions under which d matters to i". Its table includes "Its
consequentiality is latent" for ¬C_i(d) ∧ ◇C_i(d) and "It can become
entrenched" for ◇□C_i(d), with the example that "a constitutional
protection can make distinctions concerning consent consequential across
a wide range of otherwise changing institutional circumstances". The
accessibility relation is left open. If it is A19 §5's R_b, reachability
within a budget ([CLAIM-1439](CLAIM-1439.md)), the logic is fixed by the resource
semantics, and in the case the record's merge tree describes ([CLAIM-581](CLAIM-581.md))
the two rows cannot both describe one configuration at one budget.

## The derivation

1. **S5 collapses entrenchment.** Under peak costs with reversible moves
   and free holding, R_b is an equivalence relation ([CLAIM-1439](CLAIM-1439.md),
   step 1). In an equivalence frame, if some y with x R_b y has □_b C at
   y, then C holds at every z with y R_b z, and those are exactly the z
   with x R_b z. So ◇_b□_b C at x gives □_b C at x, and by reflexivity C
   at x. Hence ¬C ∧ ◇_b□_b C is unsatisfiable: a distinction cannot be
   latent at x and entrenchable from x within the same reversible peak
   budget. Whatever can be reached within b can be undone within b.
2. **One-way moves allow it.** Under directed peak costs R_b is a
   preorder (S4), and ◇□φ does not imply □φ. A move that cannot be
   reversed within b leads to a region where C holds throughout what is
   reachable from it: a ratchet, in the vocabulary A19 §11 takes from
   [LIT-3315](../literature.d/LIT-3315.md) (unread).
3. **A lower budget allows it.** With reversible moves, ◇_b□_{b'} C with
   b' < b is satisfiable at a configuration where C fails: spend capacity
   b to cross a barrier, then hold where only b' is available, which
   cannot recross. In the budget tree this is moving between two classes
   that merge only at b. Take x joined to y by a move of peak 2 and y to z by
   a move of peak 8, with C true at z only: at x, ◇_8□_3 C holds and
   ◇_8□_8 C does not.

**Check (python3 -I).** On 300 random reversible five-configuration peak
graphs at b = 5, over all 32 valuations at every configuration (48,000
cases), ◇□C without □C occurred 0 times and ¬C ∧ ◇□C 0 times; on 300
one-way graphs at the same budget ¬C ∧ ◇□C was satisfied in 5,645 cases.
The two-move example gives ◇_8□_3 C true and ◇_8□_8 C false.

## What follows

- **Lock-in is a fact about asymmetry or about budgets.** A23's
  institutional cases, capture making "a previously consequential
  objection no longer matters" and a constitution making consent matter
  "across a wide range of otherwise changing institutional
  circumstances", are entrenchment only relative to what the parties can
  later spend, or because the moves do not reverse. Either has to be
  declared; a single reversible budget makes every entrenchment undoable
  with the means that made it.
- **This matches the record's readiness results.** That reaching can cost
  more than holding ([CLAIM-571](CLAIM-571.md)) is the budget gap that step 3 uses; that
  cutting slack to need freezes the configuration ([CLAIM-679](CLAIM-679.md)) is the
  lower-budget entrenchment of a configuration one already holds.

## What it does not say

- That entrenchment is bad. A19 §11: "irreversibility is not necessarily
  pathological. The capacity to establish a commitment that cannot be
  casually withdrawn is itself a form of collective power."
- Anything about C_i itself, which A23 defines only informally ([TERM-185](../terms.d/TERM-185.md)).
