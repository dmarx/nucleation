---
status: Proposed
title: "Inquiry can fail at three sites, forming queries, producing answers and their joint realizability, and the third is not reducible to the first two, because which question–answer pairs an organization can attain together is not determined by the questions it can ask and the answers it can attain taken separately"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A composition of the costs of formulating and answering under which the
  jointly attainable question–answer pairs are fixed by the askable questions
  and the answers attainable for a supplied question, at the same budget and
  horizon.
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
- CLAIM-tmp4u0mj
summary: >-
  A58 §§1, 2 and 5 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23), on the owner's U30
  (CLAIM-tmp2enpa). A58 defines a joint inquiry-feasibility relation of
  question–answer pairs, from which the query frontier, the answer frontier
  and the resolved questions are projections, and argues that the projections
  do not determine it. Its reason in §1, a shared deadline, carries the claim;
  its formal reason in §2, two relations with the same projections, shows
  less, as the assistant's CLAIM-tmpj15c6 and ARG-tmp7xi5t set out. Warrant
  demonstrated, by the §1 construction as checked there. The wording is A's (ChatGPT's, at A58 of the exchange "Explain First Contact RL"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp2enpa CLAIM-754 CLAIM-tmpj15c6 ARG-tmp7xi5t TERM-tmpace0k CLAIM-tmp4u0mj — Proposed; the owner's thesis, the neighbour, the assistant's derivation and its argument, and A58's term -->

# CLAIM-tmpx0wv9: Inquiry can fail at three sites, forming queries, producing answers and their joint realizability, and the third is not reducible to the first two, because which question–answer pairs an organization can attain together is not determined by the questions it can ask and the answers it can attain taken separately

## The claim

A58 §1. "An organization might be able to formulate a question within ten
hours and, if given the question for free, produce an answer within ten
hours." It cannot thereby formulate and answer it within the same ten hours.
So the object is a relation: for state S, horizon H and budget B,

  𝓕_S(H, B) = {(q, a) : some admissible process formulates q, produces and
  evaluates a ∈ A_q, within H and B}.

Its projections are the query frontier 𝒬_ask (TERM-092's askable set), the
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
shared budget, worked out in CLAIM-tmpj15c6: at one budget the askable
questions and the conditional answer frontier do not fix 𝓕, though their
families over budgets do under a declared composition rule. ARG-tmp7xi5t
holds that support. CLAIM-tmp4u0mj, from A52 §7 and A54 §7, gives the
bounds the separate frontiers do fix.

## Neighbours

CLAIM-754 separates operational, developmental and inquiry frontiers, the
last in TERM-092's earlier sense, "formulate and pursue". A58 §4 warns that
widening the inquiry frontier to answers must not identify answering a
question with doing what it specifies: an inquiry may explain why a machine
fails "without possessing the ability to repair it". The answer frontier is
indexed by the kind of inquiry and its acceptance criteria, TERM-095's 𝓚.

## Standing

Proposed, in A's voice.
