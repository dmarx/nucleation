---
number: 143
status: Proposed
formerly:
- THEORY-tmpgo526
promote_when: >-
  Evidence from real groups, not models. Laboratory or field studies in
  which communication structure is varied while groups learn by trying
  options whose evidence depends on the choice, measured for both accuracy
  and speed. The account is supported if sparse groups are more often
  right only when alternatives are close and evidence scarce, and refuted
  if sparse groups do better or worse irrespective of difficulty. More
  simulations of the same model family, in either direction, cannot
  settle whether real communities sit in the region where the effect
  occurs.
title: 'When a group learns only about the options its members pursue and good evidence is scarce, sparser communication makes it more likely to settle on the better option, at a large cost in speed; when evidence is plentiful, sparsity only slows learning'
version: 1
tags:
- epistemology
- network-science
- philosophy-of-science
date: '2026-10-05'
source:
- LIT-724
- LIT-733
summary: >-
  Zollman (2007), [LIT-724](../literature.d/LIT-724.md), simulated Bala and Goyal's bandit model:
  cycles chose the better method more often than complete graphs, and more
  slowly; density, not centrality, predicted failure. Rosenstock et al.
  (2017), [LIT-733](../literature.d/LIT-733.md), found the effect only where inquiry is hard:
  close alternatives, small groups, small batches. Proposed: all of it is
  simulation, and real communities' place in parameter space is unknown.
extended_by:
- THEORY-148
---
<!-- inactive-ok-file: THEORY-148 — Proposed; the transient-diversity account filed in this batch -->
<!-- inactive-ok-file: THEORY-151 — Proposed; Longino's account filed in this batch -->

# THEORY-143: When a group learns only about the options its members pursue and good evidence is scarce, sparser communication makes it more likely to settle on the better option, at a large cost in speed; when evidence is plentiful, sparsity only slows learning

## Source

Zollman (2007), [LIT-724](../literature.d/LIT-724.md), read in [NOTE-583](../notes.d/NOTE-583.md), for the effect;
Rosenstock, Bruner & O'Connor (2017), [LIT-733](../literature.d/LIT-733.md), read in [NOTE-559](../notes.d/NOTE-559.md),
for its scope. Zollman's survey ([LIT-716](../literature.d/LIT-716.md)) places it among other
learning problems.

## What was actually shown

In Zollman's model ([LIT-724](../literature.d/LIT-724.md)), agents choose between a known option and
a new one that may be better or worse. They update on the outcomes of what
they and their neighbours chose. If all of them choose the known option,
learning stops for good.

- **The effect.** In simulated groups of 3–12, a cycle (each agent sees two
  neighbours) converged on the better option more often than a wheel, and
  a wheel more often than a complete network. The complete network was
  much faster. Over every network of up to six agents, density predicted
  failure and a hub's centrality did not. The mechanism is that a
  misleading early run reaches everyone in a dense network at once.
  In a sparse one, some agents keep trying the better option long enough
  to recover.
- **The scope.** Rosenstock et al. ([LIT-733](../literature.d/LIT-733.md)) widened the parameters.
  The effect fell below 2% when the better option's success rate rose from
  Zollman's 0.501 to 0.51, and vanished at 0.525 (10 agents, 1,000 trials
  a round). It shrank with larger groups and with more data per round. At
  100 agents, the complete network was right 99.12% of the time in 20
  rounds, and the cycle 100% in 1,977. Zollman's claim that the ordering
  holds "for any setting of the parameters" is false. The effect lives
  where inquiry is hard.

Either result could have come out otherwise: dense networks could have
been both faster and more reliable, as they are when agents pool estimates
rather than learn by trying ([LIT-716](../literature.d/LIT-716.md)).

## What this does not say

- **Not "less communication is better".** That holds only for this kind of
  problem (evidence depends on what is chosen), and only when evidence is
  scarce. For pooling problems denser is faster and no less accurate.
- **Not that real scientific or organizational communities are in that
  regime.** The authors of the robustness study call these
  "how-potentially" models and lower their confidence that the effect is
  common.
- **Not that restricting communication is the remedy.** Where the effect
  holds, Rosenstock et al. prefer stubborn or exploratory agents, or
  standards for how much evidence a judgment needs, which protect against
  premature consensus without discarding data.

## Connections

- **Transient diversity ([THEORY-148](THEORY-148.md))** carries this further: the
  benefit comes from diversity of pursuit, which sparse links are one way
  to keep.
- **Longino ([THEORY-151](THEORY-151.md)).** Longino's norms concern whether
  criticism has uptake. This account concerns how fast belief spreads. The
  owner's essay cites both in §8.2; they answer different questions.
