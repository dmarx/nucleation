---
status: Proposed
promote_when: >-
  An independent simulation or experiment on loopy 4-vertex crease
  patterns designed with one folding motion reproduces exponential growth
  of distractor branches with pattern size, and shows that whether the
  actuated creases' folding islands cover the pattern predicts folding
  success better than the number of actuators.
title: 'Stern, Pinson and Murugan show that a crease pattern designed with one folding motion still has exponentially many distractor branches meeting at the flat state, created by frustrated loops of two-branch vertices, so folding it reliably needs actuators placed so that the regions they can each fold correctly cover the sheet'
version: 1
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-05'
source:
- LIT-tmpjjho1
summary: >-
  Stern, Pinson & Murugan (2017), LIT-tmpjjho1, read from the arXiv v1
  preprint in NOTE-tmp9dvve; the published version and the SI were not
  read. Proposed: simulations on idealized rigid-panel vertices with
  zero-temperature descent, actuation statistics from one 4 × 4 pattern,
  and folding islands offered as a heuristic, not a necessary and
  sufficient condition. The authors limit the difficulty to the flat
  state. The analogy to SAT and protein folding carries no hardness proof.
---

# THEORY-tmpq2qdv: Stern, Pinson and Murugan show that a crease pattern designed with one folding motion still has exponentially many distractor branches meeting at the flat state, created by frustrated loops of two-branch vertices, so folding it reliably needs actuators placed so that the regions they can each fold correctly cover the sheet

## Source

Stern, Pinson & Murugan, "The Complexity of Folding Self-Folding Origami",
Physical Review X (2017), LIT-tmpjjho1; read from the arXiv v1 preprint,
"The difficulty of folding self-folding origami", in NOTE-tmp9dvve.

## What was actually shown

- **Distractors.** "even crease patterns with only one designed folding
  motion inevitably contain an exponential number of ‘distractor’ folding
  branches accessible from a bifurcation at the flat state."; on random
  quad meshes up to 6 × 6, N_branches ∼ 2^(α√A), α ≈ 2.25.
- **Their origin.** "loops of vertices have a glassy folding energy
  landscape, much like a spin network with frustrated loops", and designing
  the target "does not change the glassy attractor structure".
- **Actuation.** On one 4 × 4 pattern, "actuators are needed on 18 out of
  a total of 60 creases to even have a 50% probability of folding the
  pattern."; "a set of 5 actuators is 60× more likely to fold the pattern
  if it has U F I = 1 rather than U F I < 1."

## What this does not say

- That folding islands give a sufficient condition: an added actuator with
  a small island can ruin folding at UFI = 1, and the authors "are unable
  to formulate a strict necessary and sufficient condition".
- That the difficulty persists beyond the flat state: it "mathematically
  applies only at the flat state".
- That folding self-folding origami is NP-hard. The comparison with SAT is
  an analogy.
- Anything about thermal folding, where backtracking is possible.
