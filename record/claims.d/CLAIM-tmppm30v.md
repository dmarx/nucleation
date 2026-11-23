---
status: Proposed
title: 'When critics are scored by observed relevance, a population''s shared meaning settles exactly where the competence-weighted side of its specialists puts it, so grants indexed by role trade factions for a meaning that follows where competence happens to sit and can override a weak imbalance in the evidence'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of the study's code (scratch/studies/lead-190/) in which the
  role scheme's shared meaning at ζ = 0 departs from
  (b + σa_r)/(1 − φ′), or a derivation that its fixed point depends on
  anything but the corpus imbalance, the relevance-weighted side of the
  specialists and the framing; or a population in which side-correlated
  relevance does not move the shared meaning toward the more competent
  side.
tags:
- self-governance
- complex-systems
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-tmpw3vii
complements:
- CLAIM-tmp5wozo
bears_on:
- QUESTION-100
- QUESTION-089
summary: >-
  In CASE-tmpw3vii's role scheme with ζ = 0 and φ_s = 0, every reader's
  critic weights relax to the same softmax of relevance, so the
  population's shared meaning is m* = (b + σa_r)/(1 − φ′), where a_r is
  the net side of that softmax over the specialists. It matched every
  population to 2e-15. Specialists' lean toward their own side therefore
  passes into the shared meaning, weighted by where competence sits. With
  relevance spread over 0.4 to 0.9, the meaning matched a corpus
  imbalance of 0.05 in half of 30 populations; with equal relevance, in
  all of them. Agreement scoring above threshold got the sign right in
  all, by capture. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpw3vii CLAIM-tmp5wozo — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmppm30v: When critics are scored by observed relevance, a population's shared meaning settles exactly where the competence-weighted side of its specialists puts it, so grants indexed by role trade factions for a meaning that follows where competence happens to sit and can override a weak imbalance in the evidence

## The claim

Take CASE-tmpw3vii's role scheme with ζ = 0 and φ_s = 0. Each reader's critic weights relax to softmax(g·r), which reads no meaning, so every reader weights the sources alike. Write a_r = Σ_j softmax(g·r)_j s_j for the net side of that weighting. Each reader's meaning map is then m′ = (1 − ρ)m + ρ(b + σa_r + φ′m). Its unique fixed point is

m* = (b + σa_r)/(1 − φ′),

the same for every reader. e6 found it to 2e-15 in every population. Each specialist's items lean to its own side by σ, and relevance is drawn independently of side. a_r is therefore zero only on average, and in a given population it is whatever lean competence happens to have. When σ|a_r| > |b|, the shared meaning takes the competent side's lean against the evidence. With relevance over 0.4 to 0.9 (g = 12), the population read a corpus imbalance correctly in 50% of populations at b = 0.02 and 0.05, 73% at 0.1 and 93% at 0.2. Over 0.6 to 0.7 the figures were 63%, 90%, 100% and 100%. With equal relevance, 100% throughout. Agreement scoring above threshold read every one correctly, by capture.

So in this model the role-indexed scheme that keeps factions out ([CLAIM-tmp5wozo](CLAIM-tmp5wozo.md)) keeps out the loop that amplifies the evidence's lean too. What it puts in their place is a linear readout in which competence sets the weights and the specialists' own biases come through.

## What it does not say

- That role indexing is worse for fidelity than scalar agreement scoring. Agreement scoring got the sign right here by capture, which is the regime [CASE-092](../cases.d/CASE-092.md) asks about. Its fidelity is the fidelity of a captured state and would fail with a misleading corpus.
- That competence and side are uncorrelated in any real case. If they are correlated, the lean is systematic and not chance.
- Anything for φ_s > 0, where the fixed point also depends on the sources' own meanings. That case was simulated (e1) but the formula is not claimed for it.
