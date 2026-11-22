---
status: Proposed
title: 'Small Z2-symmetric recurrent lattices trained to report a quantity set by where the walls in their input are: walls, coherent structures and operative sites agree once the input is off, local transfer entropy misses the pinned walls, and a boundary-forced wall erased by intervention reappears at the boundary or not at all'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-040 as a delegated
    lead worker. Code, results and a rerun README are under
    scratch/studies/lead-040/.
standing: documented
kind: executed-study
tags:
- representation-learning
- complex-systems
- causality
date: '2026-11-22'
bears_on:
- QUESTION-491
draws_on:
- THEORY-2003
- THEORY-2028
- THEORY-702
- THEORY-1002
line:
- learned-structure
- distributed-agency
summary: >-
  [LEAD-040](../leads.d/LEAD-040.md) asked for A15's Experiment B: a family of small recurrent
  networks with a Z2 symmetry, trained on a task whose answer depends on
  boundaries in the input, with the four candidate partitions of the hidden
  field of [QUESTION-491](../questions.d/QUESTION-491.md) compared and walls moved by intervention. Six
  one-dimensional lattice networks (32 sites, 4 or 8 units per site, no
  bias, so the update is Z2-equivariant) were trained to report m², m the
  mean sign of a noisy domain input, held for 12 steps after the input was
  removed; four frozen random networks with trained readouts were the
  control. Five of the six learned static ordered phases with walls pinned
  to the lattice; one learned an oscillating phase. In the five, walls lay
  inside the causal-state coherent structures at every slice, and once the
  input was off flipping a wall site moved the answer (95 to 100% of wall
  sites) and moving a wall by interchange moved the answer as a wall model
  predicts (IIA 0.92 to 0.96, against 0.10 to 0.21 in the controls). Local
  transfer entropy was near zero at the pinned walls and marked under 3% of
  sites. While the input was on, the same interchange failed (IIA 0.03 to
  0.32): the input put the wall back. A closed pair of walls did not shrink
  unless shorter than the training minimum; a wall forced by opposite
  boundary inputs, erased by writing a uniform state, reappeared at the
  clamped end in four of six networks and not at all in two. The design
  choices and wording are the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2003 THEORY-2028 CLAIM-694 THEORY-1507 CLAIM-tmpwx1cm — Proposed or new; cited in this filing of 2026-11-22 -->

# CASE-tmp2e2a5: Small Z2-symmetric recurrent lattices trained to report a quantity set by where the walls in their input are: walls, coherent structures and operative sites agree once the input is off, local transfer entropy misses the pinned walls, and a boundary-forced wall erased by intervention reappears at the boundary or not at all

## What was done

[LEAD-040](../leads.d/LEAD-040.md) carries out A15's Experiment B for [QUESTION-491](../questions.d/QUESTION-491.md). Everything is in scratch/studies/lead-040/ (numpy, CPU, pytest tests; README says how to rerun).

- **Network.** A ring-free lattice of N = 32 sites, each with a hidden vector of d = 4 (four seeds) or d = 8 (two seeds), updated as h_i ← tanh(W_s h_i + W_n (h_{i−1} + h_{i+1}) + u x_i). There is no bias, so the map commutes with h → −h, x → −x. The readout (mean_i a·h_i)² is Z2-even.
- **Task.** The input is a ±1 configuration with 0 to 4 walls (domains at least 3 sites), shown with Gaussian noise (σ = 0.8) for 8 steps. Then the bulk input is removed for 12 steps, while the two end sites keep their clean input as boundary conditions. The target is m², the squared mean sign, so moving a wall changes the answer, which is what the lead says would count.
- **Controls** ([THEORY-1002](../theory.d/THEORY-1002.md)): four networks with frozen random weights (scale 0.5 and 1.5, two seeds each), readout trained.
- **The four partitions**, as site masks on slices t = 4 and 8 (input on; 8 is its last state) and 12 and 16 (input off):
  1. walls: bonds where neighbouring hidden states point to opposite sides, h_i·h_{i+1} < 0;
  2. coherent structures after Rupe and Crutchfield ([THEORY-2028](../theory.d/THEORY-2028.md)): sites whose local causal state is not a domain state, on a three-level field (projection on the leading direction at each time), past cone of depth 2, future cone of depth 2; a past is a domain state when each row of its future cone is uniform and ordered with probability at least 0.9;
  3. local transfer entropy ([THEORY-702](../theory.d/THEORY-702.md)) from both neighbours, history 2, above 0.5 bit;
  4. operative sites: replacing h_i by −h_i moves the prediction by more than 0.002.
- **Moving a wall** ([THEORY-2003](../theory.d/THEORY-2003.md)): an interchange from a source input identical to the base, same noise, with one wall two sites away, splicing the source's hidden states on the window between the two positions. A wall model predicts the source's answer. Control: a window of the same width away from every wall.
- **Closed against anchored.** A minority domain of length 1 to 8 between two walls with both ends the same sign, against a single wall with opposite end inputs, run 200 steps past the input (the networks were trained on 12). Interventions: shrink a pair to length 2 or 1 by interchange, and erase the single wall by writing the hidden state of a uniform input.

## Results

Test error: trained networks 2×10⁻⁶ to 6×10⁻⁴ against a target variance of 0.164; frozen controls 0.06 to 0.14.

Agreement across the six trained networks (means). "A→B" is the share of A's sites with a B site within one site:

| slice | density wall / structure / TE / operative | wall→structure | structure→wall | wall→TE | wall→operative | operative→wall |
|---|---|---:|---:|---:|---:|---:|
| 4 (input on) | 0.10 / 0.53 / 0.01 / 0.02 | 0.99 | 0.38 | 0.11 | 0.23 | 0.95 |
| 8 (last input) | 0.09 / 0.47 / 0.01 / 0.24 | 0.99 | 0.45 | 0.08 | 0.95 | 0.84 |
| 12 (input off) | 0.08 / 0.28 / 0.01 / 0.26 | 1.00 | 0.55 | 0.04 | 1.00 | 0.74 |
| 16 (input off) | 0.10 / 0.30 / 0.02 / 0.64 | 1.00 | 0.62 | 0.12 | 1.00 | 0.44 |

Full tables, per network and for the controls: `python3 -I summarize.py`.

- **Walls and coherent structures agree one way.** Every wall site is in a coherent structure. The structures are wider: they also take in the cone's reach around each wall, the boundary layers at the clamped ends and, while the input is on, noise.
- **Walls and operative sites agree once the input is off.** At t = 8 and 12, 95 to 100% of wall sites are operative and 74 to 84% of operative sites are walls. Late in the run (t = 16) a flip anywhere has too little time to heal before the readout, and the operative set spreads. While the input is on (t = 4) the walls are not operative (23%): the input restores them.
- **Local transfer entropy misses the pinned walls.** The walls do not move once formed, so nothing is transferred across them: mean local TE at walls is −0.02 to 0.03 bits, and TE marks 1 to 2% of sites, mostly not at walls (4 to 12% of wall sites have a TE site within one site).
- **Interchange.** At t = 8, moving a wall gives the answer the wall model predicts in 92 to 96% of pairs, the network's own source answer in 99 to 100%, and the source's wall positions in 100%; the control window changes nothing. At t = 4, with the input still on, IIA is 0.03 to 0.32. The frozen controls reach 0.10 to 0.21 against the task. Measured against their own outputs they reach up to 0.95, but there the source and base outputs barely differ (separable in 4 to 28% of pairs at scale 0.5), so that score says little.
- **The oscillating network** (d4-s0): after the input is removed its bulk flips sign about every six steps and returns in phase at the readout. Its walls hold through the trained horizon but have gone by 200 steps. It is the one exception to the agreements on pinned walls.
- **Closed against anchored.** In the five static networks walls are pinned: no drift in 200 steps, and a closed pair of length 3 or more survives in every run. Pairs of length 1 and 2, shorter than any trained domain, vanish. Shrinking a pair to 2 or 1 by interchange annihilates it in every run. So the closed pair shrinks only when an intervention or the input makes it small, not by itself. Erasing the boundary-forced wall does not bring it back in the interior. Counting all bonds (check_erasure.py, erasure.txt), a single wall sits at the clamped end after 200 steps in four of the six trained networks, and none is left in two (d4-s0 and d8-s1). There the one-site boundary input loses to the bulk.

## What it shows

On a learned feature, the case answers part of [QUESTION-491](../questions.d/QUESTION-491.md). In these networks the descriptive (wall), predictive (coherent structure) and interventional (operative, interchange) criteria pick out the same features while the field is free. Local transfer entropy comes apart from all three, because a feature can be a stored, static carrier of task information through which nothing flows. The interventional criterion also comes apart from the others in time: the same walls are present and predictive while the input is on, but not operative, because the input and not the wall then carries the answer. That fits [CLAIM-407](../claims.d/CLAIM-407.md): prediction is not intervention. The boundary result fits [CLAIM-694](../claims.d/CLAIM-694.md) and [THEORY-1507](../theory.d/THEORY-1507.md) where it holds: what the boundary conditions fix is that a wall exists, not where. An erased wall reappears at the boundary, and in two networks the soft boundary field does not even fix that. [CLAIM-tmpwx1cm](../claims.d/CLAIM-tmpwx1cm.md) states the finding.

## Limits

- A toy: one dimension, 32 sites, a task whose readout is a global average, and a small family (six trained networks, four controls). In one dimension the walls are points pinned to the lattice. A closed wall in two dimensions, which line tension can shrink, was not built.
- The partitions depend on choices made here: the three-level discretization, cone depths of 2, the domain criterion (uniform future rows, probability 0.9), the TE threshold (0.5 bit) and the operative threshold (0.002). The agreement between walls and coherent structures is partly built in, since a uniform ordered future is close to the absence of a nearby wall. No sweep over these choices was run.
- The single-site flip writes −h_i, a value the network realizes somewhere but not always in that context. The interchange, which uses realized values (Remark 47 of [THEORY-2003](../theory.d/THEORY-2003.md)), carries the weight.
- The boundary conditions are a clean input on one end site, not a hard constraint, so the anchoring is soft.
- Experiment E, the spectrum linearized around a wall, was not attempted.
