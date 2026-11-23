---
status: Proposed
title: 'The demand-weighted coverage model, by formal application, supports diversity of consequential capabilities as a measure of richness only under one-at-a-time selection by a selector that recognizes each question and with no shared budget'
version: 1
form: formal-application
rests_on:
- CLAIM-tmp7iie0
concludes:
- CLAIM-tmp6thmv
uses:
- TERM-tmp9lu6c
tags:
- ecology
- operations-research
- philosophy-of-science
date: '2026-11-23'
line:
- realizability
- readiness
summary: >-
  A60 §4 of the exchange "Explain First Contact RL" (ChatGPT, 2026-11-23)
  offers its coverage model as a reason that diversity tracks richness
  (CLAIM-tmp6thmv, step 4). The assistant's derivations (CLAIM-tmp7iie0)
  show the model supports that conclusion only under three conditions,
  two of which A60 states and one it does not, and that its hedge against
  unknown demand is not in the model. Proposed as a narrowed support: the
  conclusion's own standing lives in CLAIM-tmp6thmv and the open part in
  QUESTION-tmpzblpf. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp7iie0 CLAIM-tmp6thmv TERM-tmp9lu6c QUESTION-tmpzblpf — new; the derivations, the claim concluded, its term and the open question -->

# ARG-tmpbchnj: The demand-weighted coverage model, by formal application, supports diversity of consequential capabilities as a measure of richness only under one-at-a-time selection by a selector that recognizes each question and with no shared budget

## The inference

A60 applies a model, C(E; μ) = ∫ max_i r_i dμ, to conclude that diversity
of consequential capabilities, not the number of constituents, tracks
richness: coverage "increases when an added perspective supplies better
responses to questions that existing perspectives handle poorly" and
"need not increase much when another perspective simply duplicates
existing capabilities". Under the model, CLAIM-tmp7iie0's derivation 1
confirms both: the marginal value of a perspective is its demand-weighted
excess over the best already present, zero for a duplicate.

## Critical questions

- **Does the mapping premise hold?** In part: readiness r_i(q) and a
  demand measure μ are a fair rendering of a perspective's capacity and
  of future questions, but the aggregation by max is a further premise.
- **Are the model's assumptions met in the new domain?** Only under
  conditions. The
  max says one perspective answers each question, chosen at no cost by a
  selector that knows which is best. A60 states the first ("selected
  without substantial activation or coordination cost") and the
  non-interference condition. It does not state the third: the selector
  must tell the questions apart. Where all perspectives attempt in
  parallel, similar ones out-cover differentiated ones (derivation 3);
  where they share a budget, a duplicate lowers coverage (derivation 4);
  where the selector cannot tell questions apart, the advantage vanishes
  (derivation 5).
- **What the application does not carry.** The conclusion
  follows under the three conditions. The further step, diversity as a
  hedge against demand "not fully known", does not follow from the model:
  coverage is linear in μ, so uncertainty about μ over a fixed question
  set is the mean demand (derivation 6). The hedge rests on worst-case
  evaluation or on unformulated questions, outside the model.

## Verdict

Proposed: the inference holds, narrowed to its conditions. The claim
concluded can still stand on A60's other steps (§1, §3, §5, §6); this
argument says how much of it step 4 carries. Whether ecosystems generally
meet the conditions is QUESTION-tmpzblpf.
