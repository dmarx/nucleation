---
number: 926
status: Active
formerly:
- THEORY-tmp2ela3
title: 'In a game where each player can transmit n bits before a win or a loss becomes unattainable, every antisymmetric pattern of wins and losses among ⌊2ⁿ⌋ strategies, a cycle through all of them included, is realized by some set of pure strategies'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. A second checker followed the
    construction and re-checked the instances' arithmetic by script
    (status review 22). The demand for the NeurIPS 2020 version is dropped
    under ADR-065 §4: no discrepancy between versions is named (the gap
    about draws is in the theorem as stated, and the title already
    excludes it), and NOTE-1146 records the copy read (arXiv v2). The old
    promote_when: A checked re-derivation recorded in this file, which the
    reading made (NOTE-1146) and which ADR-047 counts toward promotion,
    together with the NeurIPS 2020 version read and found to state the
    same theorem. It is refuted by an n-bit communicative game, in the
    paper's sense, with some antisymmetric pattern of wins and losses
    among ⌊2ⁿ⌋ strategies that no set of pure strategies realizes. The
    title claims nothing about strong strategies or about the spinning-top
    shape. Results about those neither promote nor refute it.
tags:
- game-theory
- mathematics
date: '2026-10-24'
source:
- LIT-1504
summary: >-
  Czarnecki et al. (2020), [LIT-1504](../literature.d/LIT-1504.md), Theorem 1 and Propositions 1–2,
  read from arXiv v2 in [NOTE-1146](../notes.d/NOTE-1146.md), proof followed. Strategies announce
  an identity, then throw or take the game as the pattern says. Go is at
  least about 1000-bit communicative (log₂ 180! ≈ 1094), so it has cycles
  of length 2¹⁰⁰⁰. Ordinal: only the sign of outcomes matters. The paper
  states it for patterns with draws too, which also needs a draw to stay
  attainable. The strategies are weak by construction.
---
<!-- inactive-ok-file: CLAIM-451 — Proposed; named in prose, nothing here rests on it -->

# THEORY-926: In a game where each player can transmit n bits before a win or a loss becomes unattainable, every antisymmetric pattern of wins and losses among ⌊2ⁿ⌋ strategies, a cycle through all of them included, is realized by some set of pure strategies

## Source

Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg,
[LIT-1504](../literature.d/LIT-1504.md), read in [NOTE-1146](../notes.d/NOTE-1146.md) from arXiv:2004.09468v2: Definition 1
and Theorem 1 (p. 5, proof p. 13), Propositions 1–2 (p. 5, proofs p. 13),
supplement B (pp. 14–16).

## What was actually shown

- **The construction.** Fix the pattern P. Strategy π_i spends its first
  n bits of moves encoding i and reads the opponent's code. Both then
  follow a fixed, lexicographically first line of play reaching the
  outcome P_ij. That outcome is still attainable, because by definition
  neither a win nor a loss has yet been ruled out. Each π_i is a
  deterministic pure strategy, and sign f(π_i, π_j) = P_ij. A cycle of
  length ⌊2ⁿ⌋ is the special case in which each beats its predecessor and
  the first beats the last.
- **Instances.** Tic-Tac-Toe is 5.58-bit communicative by the paper's
  linear-time recursion (supplement B), so every 47 × 47 pattern occurs.
  Go: alternately filling 180 points on each half of the board encodes
  log₂ 180! bits. The paper says ≈ 1000; the reader computed 1093.9.
  StarCraft, DOTA or Quake over 10 minutes at 60 Hz: at least 36,000
  bits.

The reader re-derived the construction. It needs nothing beyond the
definition.

## What this does not say

- **Anything about draws, in general.** The paper states the theorem for
  P ∈ {−1, 0, 1}. A 0 entry needs a draw to remain attainable after the
  signalling, which the definition does not provide. The title is limited
  to wins and losses.
- **That strong play cycles.** The constructed strategies spend the game
  signalling and then deliberately lose or win. They are weak, and the
  theorem places long cycles among weak strategies only.
- **That real games have the spinning-top shape.** The authors say so
  themselves (p. 6). That is [THEORY-930](THEORY-930.md)'s empirical question.
- **Anything cardinal.** Margins play no part.

## Connections

For [CLAIM-451](../claims.d/CLAIM-451.md) and [TERM-077](../terms.d/TERM-077.md) it is the condition under which cyclic
records cannot be excluded on structural grounds. Wherever contestants can
recognize one another before the outcome is settled, any pattern of wins
can arise. Whether an ordinal potential exists is then a fact about the
strategies in play, not about the game ([NOTE-1146](../notes.d/NOTE-1146.md)).

## Note of 2026-10-30: the second check

The second check at the status review ([ADR-065](../decisions.d/ADR-065.md) §5) followed each step.

Fix an antisymmetric pattern P of wins and losses over m = ⌊2ⁿ⌋ indices.
Strategy π_i spends its first n bits of moves encoding i, which the
definition lets it do whatever the opponent plays, and decodes the
opponent's index j from the opponent's moves. Both players now know i, j
and P. By the definition, neither a win nor a loss has yet been ruled out,
so some continuation reaches the outcome P_ij for π_i. Both follow the
lexicographically first such continuation, which each can compute alone.
Because P_ji = −P_ij, it is the same line from either side, so the outcome
agrees whichever seat each strategy holds, and sign f(π_i, π_j) = P_ij.
Each π_i is deterministic, so it is pure. A cycle through all m strategies
is the pattern in which each beats its predecessor and the first beats the
last.

The instances' arithmetic: log₂ 180! = 1093.92, computed from the
log-gamma function; ⌊2^5.58⌋ = 47; and 10 minutes × 60 s × 60 Hz = 36,000.
As a check on the construction, a script (in the session's scratchpad)
built it in a toy game with two bits of signalling followed by a free
resignation, and all 64 antisymmetric patterns of wins and losses on 4
strategies were realised.
