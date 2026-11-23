---
status: Proposed
title: "Under a pseudometric that compares perspectives by their probabilities of answering adequately, no two perspectives are further apart than the coverage of the ecology that holds them, so perspectives that are all consistently wrong are close under it however differently they answer, and diversity without coverage needs a metric on what is answered"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below, for d_μ and coverage as A62b §3
  defines them. Not defeated by another metric: the claim is about A62b's.
tags:
- probabilistic-modeling
- epistemology
- ecology
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
complements:
- CLAIM-tmph9g28
- CLAIM-tmp7iie0
bears_on:
- QUESTION-tmpzblpf
summary: >-
  A gap fill ([ADR-137](../decisions.d/ADR-137.md)) for A62b §3 of the exchange "Explain First Contact
  RL" (ChatGPT, the branch of 2026-11-23 08:51), which defines
  d_μ(P_i, P_j) = ∫ |r_i − r_j| dμ and coverage 𝒞_μ(S) = ∫ max_i r_i dμ and
  says "A collection of arbitrarily different, consistently wrong responses
  could have high diversity." Under d_μ it could not: every pairwise
  distance is at most the coverage. Checked by script (python3 -I). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: TERM-tmp9lu6c TERM-tmpwc4la — Proposed; entries filed from this exchange or neighbours cited, not leaned on as in force -->

# CLAIM-tmpjk3nm: Under a pseudometric that compares perspectives by their probabilities of answering adequately, no two perspectives are further apart than the coverage of the ecology that holds them, so perspectives that are all consistently wrong are close under it however differently they answer, and diversity without coverage needs a metric on what is answered

## The gap

A62b §3 measures diversity by d_μ(P_i, P_j) = ∫_Q |r_i(q) − r_j(q)| dμ(q), where r_i(q) is the probability that perspective i answers q adequately, and coverage by 𝒞_μ(S) = ∫_Q max_i r_i(q) dμ(q). To show that diversity is not yet intelligence, it says: "A collection of arbitrarily different, consistently wrong responses could have high diversity." The metric it has just defined does not allow that.

## The derivation

For numbers a, b in [0, 1], |a − b| = max(a, b) − min(a, b). So, for any two perspectives of S,

  d_μ(P_i, P_j) = ∫ max(r_i, r_j) dμ − ∫ min(r_i, r_j) dμ ≤ ∫ max_k r_k dμ − ∫ min(r_i, r_j) dμ ≤ 𝒞_μ(S).

The diameter of the ecology under d_μ is at most its coverage. In consequence:

- **Consistently wrong perspectives are close.** If every r_i ≤ δ, every distance is at most δ, however differently the perspectives answer. Their differences are in what they answer, which d_μ does not see; it sees only how often each is adequate.
- **The covering number collapses.** N_ε(𝒫, d_μ) = 1 whenever ε ≥ 𝒞_μ(S): at any resolution coarser than its coverage, an ecology has one response type.
- **The converse fails.** One perspective that answers everything has coverage 1 and diameter 0. So high coverage with no diversity is possible; high diversity with low coverage is not.

## The check

By script (python3 -I), in this session: the identity and the bound held in 20,000 random ecologies (1 to 8 questions, 2 to 6 perspectives, random μ, readiness drawn with varied skew), the largest value of d − 𝒞 being 0.0. Four perspectives, each adequate with probability 0.05 on different questions under uniform μ, have coverage 0.05 and diameter 0.05.

## What follows for A62b

A62b's distinction survives with a change of example: diversity in d_μ is not intelligence, because coverage can be high where d_μ-diversity is nil. Its example needs a different metric, one on the content of answers (for instance a distance between the laws of the answers given, as in [TERM-tmpwc4la](../terms.d/TERM-tmpwc4la.md)'s dispositional address), under which consistently wrong perspectives can be far apart. A60's richness ([TERM-tmp9lu6c](../terms.d/TERM-tmp9lu6c.md)) and [QUESTION-tmpzblpf](../questions.d/QUESTION-tmpzblpf.md)'s search for an index that tracks it should say which of the two metrics is meant: a success-profile metric builds part of coverage into diversity, and a content metric does not.
