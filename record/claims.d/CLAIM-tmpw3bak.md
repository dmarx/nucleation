---
status: Proposed
title: 'The coupled meaning–influence model reduced to two specialists and scalar authority is a weighted-averaging opinion model with two stubborn sources whose weights relax toward an agreement kernel, so it adds nothing to that class; against fixed-weight and reflected-appraisal models, and against Gaussian bounded confidence off a balanced corpus, it produces authority chosen by the initial interpretation and switched by the evidence with hysteresis, which they cannot'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-090, from the
    executed study CASE-tmpz4n6b.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of CASE-tmpz4n6b's code (scratch/studies/lead-090/) in which the
  stated parameter map fails to reproduce the reduced map; or a fixed-weight
  DeGroot, Friedkin–Johnsen, DeGroot–Friedkin or Friedkin 2011 system, or a
  Gaussian bounded-confidence model with the same sources, of no more
  parameters, in which which specialist gains authority depends on the
  initial interpretation from a symmetric structure, or in which corpus
  imbalance switches authority with hysteresis. A model that adds a channel
  from opinions to weights to one of these does not count: that model is
  the adaptive class the claim names.
tags:
- complex-systems
- network-science
- self-governance
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-tmpz4n6b
- THEORY-1161
complements:
- CLAIM-tmp6f8w8
bears_on:
- QUESTION-117
- QUESTION-100
summary: >-
  LEAD-090's comparison. Under λ = ρ(1 − φ′), sources at
  o_j = (b + s_jσ)/(1 − φ′) and kernel gain κ = g(1 − φ′)/2, CASE-092's
  reduced map is reproduced to 1e-12 by weighted averaging with two
  stubborn sources and weights relaxing toward exp(κ·m·o_j); on a balanced
  corpus that is Gaussian bounded confidence with memory. It has four
  identifiable parameters to CASE-092's six. Fixed-weight models and the
  reflected-appraisal power maps read no opinions, so they cannot let the
  initial interpretation choose who gains authority; Gaussian bounded
  confidence's kernel moves with the evidence, so imbalance never switches
  authority there. Two readings for QUESTION-117 are set out for the owner.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmpz4n6b CLAIM-tmp6f8w8 — new; the study this claim rests on and its companion, filed in the same batch -->

# CLAIM-tmpw3bak: The coupled meaning–influence model reduced to two specialists and scalar authority is a weighted-averaging opinion model with two stubborn sources whose weights relax toward an agreement kernel, so it adds nothing to that class; against fixed-weight and reflected-appraisal models, and against Gaussian bounded confidence off a balanced corpus, it produces authority chosen by the initial interpretation and switched by the evidence with hysteresis, which they cannot

## The claim

QUESTION-117 asks whether coupling meaning to interpretive authority produces "modes, attractors or transitions" that established models with evolving influence cannot reproduce as economically, and counts as an answer "A derivation placing a reduced CASE-092 inside one of these models, or a phenomenon ... that the coupled meaning–authority model produces and they cannot at matched complexity." CASE-tmpz4n6b gives both, for different predecessors.

**The map.** Write the collective's meaning m as one open-minded agent with self-weight 1 − λ and the specialists as stubborn sources with opinions o_A, o_B, weighted λw and λ(1 − w). Let w relax with memory δ toward softmax(κ·m·o_j). With λ = ρ(1 − φ′), o_j = (b + s_jσ)/(1 − φ′), κ = g(1 − φ′)/2 and φ′ = φ(1 − ε), this is CASE-092's mean-field map under Regime A, to 1e-12, for every corpus imbalance b. Framing by the dominant interpretation becomes self-weight. Scoring by agreement becomes homophily. CASE-092's six parameters enter only through four, and two parameter sets with the same four give the same trajectories. Regime B becomes weights moving on a schedule that reads no opinions, so after a transient it is DeGroot with fixed weights.

**What is inside.** On CASE-092's balanced corpus the agreement kernel equals the Gaussian bounded-confidence kernel, so the reduced model is smooth bounded confidence with memory in the weights (memoryless when δ = 0). Its capture, its Curie–Weiss attractors and its capture without fidelity are that class's.

**What is outside.**

1. *Authority chosen by the interpretation.* From a symmetric structure, the sign of m₀ decided which specialist won authority in every mean-field run, and in 94% of 200 agent-level runs the early meaning matched the winner. Fixed-weight DeGroot, Friedkin–Johnsen and persuasion bias have no weight dynamics. DeGroot–Friedkin and Friedkin 2011 do, but their power maps read only the network and the current powers, never opinions. On the symmetric three-member system they kept the specialists equal from every start.
2. *Authority switched by the evidence, with hysteresis.* Sweeping corpus imbalance b up and down flips authority at b = ±0.12 in a loop 0.23 wide. Gaussian bounded confidence with the same sources never flips: its kernel's centre moves with b, and the field cancels. Fixed-weight models are linear and single-valued.

## Two readings for QUESTION-117, for the owner

- **Reading A: answered "inside" for the reduced form.** QUESTION-117's "adaptive networks" (Holme and Newman; Gross and Blasius) is a class: opinions and ties co-evolve. Weighted averaging with weights adapting toward a similarity kernel is a member of it. The reduced CASE-092 is then placed inside it, more economically, and what CLAIM-297 adds over predecessors has to come from what the reduction drops: role-indexed authority (LEAD-190), turnover, demands, or several operators.
- **Reading B: a phenomenon the named models cannot produce.** None of the works QUESTION-117 names and the record has read is this model. Holme and Newman's ties are unweighted and opinions are labels; Ito and Kaneko's kernel is distance-based on chaotic units; reflected appraisal and persuasion bias read no opinions; the Gaussian kernel of bounded confidence cannot let evidence switch authority. On this reading, evidence-switched authority with hysteresis is the outcome they forbid and the coupled model allows, at four parameters.

The derivation is the same on both readings. What differs is whether "adaptive networks" names the class or the read works. That is the owner's call.

## What it does not say

- That no published model uses an agreement kernel with stubborn sources. Inner-product similarity weighting may exist in work the record has not read; this was not searched.
- Anything about the full CASE-092 beyond the mean-field, two-specialist, scalar-authority reduction.
- That the coupling is idle. It is what produces both phenomena; the claim is about which known models already have it.
