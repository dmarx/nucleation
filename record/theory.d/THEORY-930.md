---
number: 930
status: Proposed
formerly:
- THEORY-tmp5k950
promote_when: >-
  The same profile, cluster size peaking at intermediate strength and
  narrowing at both ends, found in empirical games built by a sampler not
  tuned along the transitive axis, for instance learning agents or uniform
  draws from a restricted policy class, in games other than these eight,
  and robust to the choice of equilibrium (minimum- as well as
  maximum-entropy Nash). It is refuted if a sampler with comparable
  coverage gives clusters that keep growing with strength in these same
  games, as they do in Blotto. Theorems about long cycles among weak
  strategies do not bear on it.
title: 'In empirical games built from about a thousand sampled search agents in eight small board games, and in the AlphaStar league, Nash cluster size peaks at intermediate transitive strength and narrows toward the strongest and the weakest strategies, while Blotto, the disc game, Kuhn poker and noisy Elo games do not show that profile'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-24'
source:
- LIT-1504
summary: >-
  Czarnecki et al. (2020), [LIT-1504](../literature.d/LIT-1504.md), section 6 and supplements E–I,
  read from arXiv v2 in [NOTE-1146](../notes.d/NOTE-1146.md). Agents were MinMax at depths 0–9,
  loss-seeking MaxMin and MCTS, with 50 seeds each, about 1000 distinct
  per game after duplicates were removed. Games: Hex, Go and Quoridor on
  small boards, Tic-Tac-Toe, its misère form and Connect Four. AlphaStar's
  league shows its training system's geometry, the authors say. A
  qualitative profile with a fitted skew-normal curve and no test.
---
<!-- inactive-ok-file: NOTE-1146 — the reading this is filed from -->

# THEORY-930: In empirical games built from about a thousand sampled search agents in eight small board games, and in the AlphaStar league, Nash cluster size peaks at intermediate transitive strength and narrows toward the strongest and the weakest strategies, while Blotto, the disc game, Kuhn poker and noisy Elo games do not show that profile

## Source

Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg,
[LIT-1504](../literature.d/LIT-1504.md), read in [NOTE-1146](../notes.d/NOTE-1146.md) from arXiv:2004.09468v2: section 6 and
Table 1 (pp. 8–9), supplements D–I (pp. 17–22), Tables 2–3.

## What was actually shown

- **The data.** For each game, about 2000 agents:
  - MinMax(d, s) for d = 0–9;
  - variants that value the horizon at 0;
  - MaxMin(d, s), which seek to lose;
  - MCTS with 10, 100 and 1000 simulations;
  - 50 seeds each.
  Each pair played twice, swapping sides, and duplicate rows were
  removed, leaving about 1000 agents. AlphaStar's 900-agent league matrix
  was taken from its authors.
- **The profile.** Maximum-entropy Nash clustering. For each cluster, its
  size against its mean RPP against all clusters. A skew-normal curve is
  fitted and drawn.
- **The finding.** The eight board games and AlphaStar show sizes rising
  to a peak and falling toward both ends. Blotto and Kuhn poker grow with
  strength, the noisy Elo games grow too, the disc game is one cycle, and
  the Elo game is a chain. In Go 3×3 the top cluster is not trivial.
- **What could have come out otherwise.** Clusters could have grown with
  strength, as in Blotto. They did not in these eight games.

## What this does not say

- **That the shape belongs to the games.** The sampler sets the transitive
  axis through search depth and the spread through seeds, and the authors
  say it "does not guarantee uniform sampling of strategies" (p. 9). For
  AlphaStar they say the profile reflects "AlphaStar induced game
  geometry" (p. 18), shaped by how the league was trained.
- **That it is proved.** The abstract says so, and the body withdraws it
  (p. 6). Theorem 1 ([THEORY-926](THEORY-926.md)) shows long cycles among weak
  strategies, not narrowing at the top.
- **That cluster sizes are robust.** Maximum-entropy Nash makes clusters
  as large as possible. The authors note that minimum-entropy equilibria
  would give "more peaky tops" (p. 17).
- **Anything about large boards.** The board games are 3×3 and 4×4 except
  Tic-Tac-Toe and Connect Four.

## Connections

A descriptive picture the record can cite for where cycles are expected
in contests of skill: at middling strength, among varied styles. Its
evidential weight is that of a sampled, untested profile ([NOTE-1146](../notes.d/NOTE-1146.md)).
