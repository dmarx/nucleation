---
number: 293
status: Active
formerly:
- CLAIM-tmp2deky
title: 'The topology of a support graph does not fix how a conclusion should be
  revised when one of its supports fails: two records with the same edges can carry
  evidence of different strength and call for different revisions'
version: 3
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by records-of-inquiry, at the split of that
    line (ADR-082). No other change.
- version: 3
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11, by question: bears_on QUESTION-258
    added. The question's text, against a connected, well-supported
    subgraph: "From CLAIM-293: 'A coherent, connected support graph
    does not itself establish that the selected argument has adequate
    evidentiary support.'" Its title: "The topology of a support graph
    does not fix how a conclusion should be revised". No other change.
role: granted
warrant: demonstrated
tags:
- epistemology
- probabilistic-modeling
date: '2026-10-15'
line:
- formal-apparatus
- records-of-inquiry
objects_to:
- CLAIM-295
grounds:
- CASE-089
summary: >-
  A6's compensating-evidence case ([CASE-089](../cases.d/CASE-089.md)), granted against reading [CLAIM-295](CLAIM-295.md)
  as saying a graph of justifications is enough. Two pieces of evidence support
  H in both worlds. Discount the first, and posterior odds are 20:1 in one world
  and 1.1:1 in the other. `rests_on` and `grounds` record that support exists, not
  how much.
complements:
- CLAIM-479
bears_on:
- QUESTION-258
---
<!-- inactive-ok-file: CLAIM-250 CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-tmpglid0 THEORY-tmpn7ukf THEORY-tmpo4vs4 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# CLAIM-293: The topology of a support graph does not fix how a conclusion should be revised when one of its supports fails: two records with the same edges can carry evidence of different strength and call for different revisions

## The claim

A6, [CASE-089](../cases.d/CASE-089.md): E₁ → H ← E₂ in two worlds, prior odds 1:1, E₁ and E₂
conditionally independent. The Bayes factor of E₁ is 10 in both. That of
E₂ is 20 in world A and 1.1 in world B. Discounting E₁ leaves odds of
20:1 in A and 1.1:1 in B, as A6 said, checked here. "The unweighted
graph has the same topology in both cases."

A8 drew the record's consequence: "Those edges preserve aspects of
dependency and provenance. They do not, by themselves, encode a complete
probabilistic model of evidential support."

## Why it is granted

It cuts against the strongest reading of [CLAIM-295](CLAIM-295.md) and of [CLAIM-250](CLAIM-250.md), that
keeping justificatory structure keeps what revision needs. The thesis has
to be stated so it survives: [CLAIM-295](CLAIM-295.md) says justifications can widen what a
retained state suffices for, not that topology suffices. A6: "This is an
important case because it blocks a careless inference from 'justificatory
structure matters' to 'a graph of justifications is sufficient.'"

## What it does not say

- Not that graph memory is insufficient as such. "An attributed graph
  could include likelihoods, dependence models, assumptions, and other
  relevant information."
- Not that the record should weight its edges. That is a design question
  for luria, and the owner's U14 objected to turning the exchange toward
  it.

## Note of 2026-11-12: Jung, Rubinstein, Uselis, Yun and Oh, de Kleer and Williams and de Kleer, read

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Jung, Rubinstein, Uselis, Yun and Oh** (THEORY-tmpo4vs4): MEME's gold answers *are* fixed by the DAG plus rules; it is a setting where the claim's condition (same edges, different evidence) does not arise. Contrast, not evidence.
- **de Kleer and Williams** (THEORY-tmpglid0): **consistent**. Sherlock's ranking of diagnoses needs mode probabilities beyond the conflict structure; two systems with the same conflicts can call for different probes.
- **de Kleer** (THEORY-tmpn7ukf): *supports by contrast*: the ATMS's correctness rests on edges being Horn implications; where they are, topology does fix revision. This is the boundary condition of CLAIM-293, not a counterexample to it.

The claim is unchanged.
