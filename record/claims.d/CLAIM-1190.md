---
number: 1190
status: Active
formerly:
- CLAIM-tmpx0wv9
title: 'Joint realizability is a third failure site'
statement: >-
  Inquiry can fail at three sites, forming queries, producing answers and
  their joint realizability, and the third is not reducible to the first
  two, because which question–answer pairs an organization can attain
  together is not determined by the questions it can ask and the answers it
  can attain taken separately
version: 3
history:
- version: 2
  date: '2026-11-24'
  note: >-
    Defeater restated at the owner's word of 2026-11-24 ("handle the
    fixes for the twelve ... use your best judgement", under the
    dialectic regime; ADR-057), as the note of 2026-11-24 asked: the old
    defeated_if, "A composition of the costs of formulating and
    answering under which the jointly attainable question–answer pairs
    are fixed by the askable questions and the answers attainable for a
    supplied question, at the same budget and horizon", was met by any
    one composition that fixes the pairs, such as one in which
    formulating costs nothing, though the claim is that the separate
    frontiers do not determine the pairs where one budget is spent on
    both. It now asks for a showing over the compositions the claim
    covers, or an error in CLAIM-1115's construction 1, and names what
    does not count. A53's reason for the repair misread the old wording;
    the fault was the one the note names. No change of title: read with
    the defeater, it asserts no more than construction 1 shows.
- version: 3
  date: '2026-11-24'
  note: >-
    Promoted to Active at the same word (ADR-057): it has no premise,
    the terms it uses, TERM-092 and TERM-095, are Active, no objection
    targets it, and nothing meets its restated defeated_if: construction
    1 of CLAIM-1115, promoted in this pass and its constructions rerun
    from a kept script by a session other than the filer's, exhibits two
    organizations with the same frontiers at one budget and different
    joint pairs. In A's voice; a demonstrated promotion, listed for the
    owner in the pull request.
role: thesis
warrant: demonstrated
defeated_if: >-
  A showing that, wherever one budget or horizon is spent on both
  formulating and answering, any two organizations with the same askable
  questions and the same answers attainable for a supplied question, at a
  budget and horizon, have the same jointly attainable question–answer
  pairs there; or an error in CLAIM-1115's construction 1, which exhibits
  two that do not. Not defeated by a composition in which formulating costs
  nothing, which the claim does not cover, nor by reconstructing the joint
  pairs from the frontiers at every budget under a declared rule
  (CLAIM-1115's construction 2), which uses more than the one budget.
tags:
- epistemology
- philosophy-of-science
- operations-research
date: '2026-11-23'
line:
- learning-and-inquiry
- realizability
uses:
- TERM-092
- TERM-095
complements:
- CLAIM-754
- CLAIM-1025
summary: >-
  A58 §§1, 2 and 5 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23), on the owner's U30
  ([CLAIM-1009](CLAIM-1009.md)). A58 defines a joint inquiry-feasibility relation of
  question–answer pairs, from which the query frontier, the answer frontier
  and the resolved questions are projections, and argues that the projections
  do not determine it. Its reason in §1, a shared deadline, carries the claim;
  its formal reason in §2, two relations with the same projections, shows
  less, as the assistant's [CLAIM-1115](CLAIM-1115.md) and [ARG-221](../arguments.d/ARG-221.md) set out. Warrant
  demonstrated, by the §1 construction as checked there. The wording is A's (ChatGPT's, at A58 of the exchange "Explain First Contact RL"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1009 CLAIM-754 ARG-221 — Proposed; the owner's thesis, the neighbour, the assistant's derivation and its argument, and A58's term -->

# CLAIM-1190: Joint realizability is a third failure site

## The claim

A58 §1. "An organization might be able to formulate a question within ten
hours and, if given the question for free, produce an answer within ten
hours." It cannot thereby formulate and answer it within the same ten hours.
So the object is a relation: for state S, horizon H and budget B,

  𝓕_S(H, B) = {(q, a) : some admissible process formulates q, produces and
  evaluates a ∈ A_q, within H and B}.

Its projections are the query frontier 𝒬_ask ([TERM-092](../terms.d/TERM-092.md)'s askable set), the
joint answer frontier for each q, {a : (q, a) ∈ 𝓕}, and the resolved
questions 𝒬_resolved = proj_Q 𝓕 ⊆ 𝒬_ask. The joint answer frontier
differs from the conditional one, the answers attainable "if q is already
supplied".

A58 §5: an organization can become better at asking while worse at
answering, better at answering while suppressing the questions that would use
it, and keep both while losing the connections through which they work
together; hence three sites of failure, query formation, answer production
and joint realizability, and "The third cannot be reduced to the first two."
"Parallelism and managerial authorization therefore belong to the inquiry
frontier itself, rather than being external complications." And "multiple
maintained perspectives may increase the feasible inquiry region by
providing alternative routes between questions and answers, even without
increasing the total stock of resources."

## The two reasons

A58 §2 offers a formal reason: 𝓕_1 = {(q_1, a_1), (q_2, a_2)} and
𝓕_2 = {(q_1, a_2), (q_2, a_1)} have the same projections onto Q and A and
differ. That holds of any relation and its projections. It does not reach a
query frontier and an answer frontier indexed by question, which A58 itself
defines and which already tell 𝓕_1 from 𝓕_2. What carries the claim is §1's
shared budget, worked out in [CLAIM-1115](CLAIM-1115.md): at one budget the askable
questions and the conditional answer frontier do not fix 𝓕, though their
families over budgets do under a declared composition rule. [ARG-221](../arguments.d/ARG-221.md)
holds that support. [CLAIM-1025](CLAIM-1025.md), from A52 §7 and A54 §7, gives the
bounds the separate frontiers do fix.

## Neighbours

[CLAIM-754](CLAIM-754.md) separates operational, developmental and inquiry frontiers, the
last in [TERM-092](../terms.d/TERM-092.md)'s earlier sense, "formulate and pursue". A58 §4 warns that
widening the inquiry frontier to answers must not identify answering a
question with doing what it specifies: an inquiry may explain why a machine
fails "without possessing the ability to repair it". The answer frontier is
indexed by the kind of inquiry and its acceptance criteria, [TERM-095](../terms.d/TERM-095.md)'s 𝓚.

## Standing

In A's voice; Active since the status pass of 2026-11-24.

## Note of 2026-11-24: the exchange 'Memes, Contracts, and Systemic Normativity', A53

A53: the `defeated_if` "needs refinement. A demonstration that sufficiently rich budget-indexed frontiers determine the joint frontier under a declared composition rule does not refute the single-budget non-identifiability result." The defeater as written already says "at the same budget and horizon", so [CLAIM-1115](CLAIM-1115.md)'s reconstruction from budget-indexed families does not meet it; A53's reason misreads it. The defeater has another fault, which this note fills (the assistant's): it is met by any one composition under which the separate frontiers fix the joint pairs, and there are such compositions, for instance one in which formulating costs nothing, where the jointly attainable pairs at a budget are exactly the conditional answers at that budget. The claim is true as an existence claim (some compositions, [CLAIM-1115](CLAIM-1115.md)'s construction 1 among them, leave the pairs undetermined), so the defeater should ask for a showing that no admissible composition does, or name the compositions the claim covers (a shared budget spent on both). A53's own proposal, that "the organization of their composition contains consequential information absent from their separately measured capabilities", is the same repair stated as a thesis. Due before a ruling; the worklist lists the claim as ready for one. The note is the assistant's (Claude, in this session), reporting A's (ChatGPT's) text; adopting either is the owner's call. No status change.
