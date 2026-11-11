---
number: 1418
status: Active
formerly:
- THEORY-tmpq2qdv
title: 'Stern, Pinson and Murugan find, in zero-temperature simulations of idealized rigid-panel crease patterns designed with one folding motion, distractor branches at the flat state whose number grows exponentially with the sheet''s boundary length on random meshes up to 6 × 6, which they trace to frustrated loops of two-branch vertices; and, on one 4 × 4 pattern, that whether the actuated creases'' folding islands cover the sheet predicts folding success much better than the number of actuators, and that an added actuator can ruin a folding that succeeded, without a necessary and sufficient condition'
version: 3
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review of 2026-11-06, at the status
    review's ruling (the owner delegated these rulings), under ADR-047's
    one-study ruling and ADR-065 §§2–3. The title now reports what the one
    study, read in full from the arXiv v1 preprint in NOTE-1571, measured,
    with its hedges kept; nothing in the record contradicts it. The old
    title: "Stern, Pinson and Murugan show that a crease pattern designed with one folding motion still has exponentially many distractor branches meeting at the flat state, created by frustrated loops of two-branch vertices, so folding it reliably needs actuators placed so that the regions they can each fold correctly cover the sheet". The generalization the authors assert moves to
    THEORY-1528, which extends this entry and keeps the old
    promote_when (ADR-047 kind 1). The "needs" clause, a necessary
    condition the authors disclaim, gets the note of 2026-11-06 (kind 3).
    The old promote_when: "An independent simulation or experiment on loopy
    4-vertex crease patterns designed with one folding motion reproduces
    exponential growth of distractor branches with pattern size, and shows
    that whether the actuated creases' folding islands cover the sheet
    predicts folding success better than the number of actuators." The
    published version was not read; no discrepancy with the preprint is
    named (ADR-065 §4).
- version: 3
  date: '2026-11-11'
  note: >-
    Bears on QUESTION-391, at the reading review of 2026-11-11 (by
    question, ADR-091). The question names it as "a second sign": for soft
    sheets careful actuation "needs to be maintained until a larger
    folding angle", so how long the flat-state constraint structure
    governs depends on stiffness. No other change.
tags:
- natural-sciences
- complex-systems
- mathematics
date: '2026-11-05'
source:
- LIT-2074
summary: >-
  Stern, Pinson & Murugan (2017), [LIT-2074](../literature.d/LIT-2074.md), read from the arXiv v1
  preprint in [NOTE-1571](../notes.d/NOTE-1571.md); the published version and the SI were not
  read. Its limits: simulations on idealized rigid-panel vertices with
  zero-temperature descent, actuation statistics from one 4 × 4 pattern,
  and folding islands offered as a heuristic, not a necessary and
  sufficient condition. The authors limit the difficulty to the flat
  state. The analogy to SAT and protein folding carries no hardness proof.
corroborates:
- CLAIM-567
bears_on:
- QUESTION-391
---
<!-- inactive-ok-file: THEORY-1528 — Proposed and new; the authors' generalization split off at the status review of 2026-11-06, cited as open -->

# THEORY-1418: Stern, Pinson and Murugan find, in zero-temperature simulations of idealized rigid-panel crease patterns designed with one folding motion, distractor branches at the flat state whose number grows exponentially with the sheet's boundary length on random meshes up to 6 × 6, which they trace to frustrated loops of two-branch vertices; and, on one 4 × 4 pattern, that whether the actuated creases' folding islands cover the sheet predicts folding success much better than the number of actuators, and that an added actuator can ruin a folding that succeeded, without a necessary and sufficient condition

## Source

Stern, Pinson & Murugan, "The Complexity of Folding Self-Folding Origami",
Physical Review X (2017), [LIT-2074](../literature.d/LIT-2074.md); read from the arXiv v1 preprint,
"The difficulty of folding self-folding origami", in [NOTE-1571](../notes.d/NOTE-1571.md).

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

## Note of 2026-11-06: a clause dropped at narrowing

The old title's "so folding it reliably needs actuators placed so that the regions they can each fold correctly cover the sheet" stated a necessary condition. The authors disclaim one ("we are unable to formulate a strict necessary and sufficient condition for successful folding without full pattern information", [NOTE-1571](../notes.d/NOTE-1571.md)), and their own comparison, five actuators "60× more likely to fold the pattern if it has U F I = 1 rather than U F I < 1", implies that uncovered sets sometimes succeed. A mis-statement, routed here only ([ADR-047](../decisions.d/ADR-047.md) kind 3).
