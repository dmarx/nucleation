---
status: Proposed
title: 'A protected beacon''s miscalibration is unidentifiable from inside
  the sensor network by a symmetry: a world whose beacon reports z* + d and
  a world whose beacon is correct, with the target, the beacon placements
  and every sensor bias shifted (z + d, z* + d, b_i - A_i d), give every report
  identically, so no revision that uses only the network''s reports can find
  d, and correcting it needs evidence that breaks the symmetry from outside'
version: 1
role: thesis
warrant: demonstrated
defeated_if: An error in the identity, or a report available to the network
  that differs between the two worlds. In LEAD-177's simulation, the target
  is clipped to a box and the placements are uniform on a box. Those break
  the symmetry at the boundary, so a system that knew those laws could in
  principle learn d from boundary effects. The identity is exact for translation-invariant
  laws.
tags:
- mathematics
- epistemology
- control-theory
date: '2026-11-23'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-tmpw11e6
complements:
- CLAIM-tmpxoxys
- CLAIM-148
summary: 'The assistant''s, answering the owner''s comparison with Gödel ([CLAIM-tmphsmbq](CLAIM-tmphsmbq.md)).
  It gives the mechanism of [CLAIM-tmpw11e6](CLAIM-tmpw11e6.md)''s regress: a translation symmetry,
  the same kind of limit as [LEAD-180](../leads.d/LEAD-180.md)''s relabelling ([CLAIM-tmpxoxys](CLAIM-tmpxoxys.md)), not
  a diagonal argument. Checked in scratch/formal/beacon_gauge_check.py (1,000
  random trials, no mismatch). The wording is the assistant''s (Claude, in
  this session); adopting it is the owner''s call.'
---

<!-- inactive-ok-file: CLAIM-tmpw11e6 CLAIM-tmpxoxys — Proposed; cited in this filing of 2026-11-23 -->

# CLAIM-tmpklggb: A protected beacon's miscalibration is unidentifiable from inside the sensor network by a symmetry: a world whose beacon reports z* + d and a world whose beacon is correct, with the target, the beacon placements and every sensor bias shifted (z + d, z* + d, b_i - A_i d), give every report identically, so no revision that uses only the network's reports can find d, and correcting it needs evidence that breaks the symmetry from outside

## The identity

Sensors report o_i = A_i z + b_i. The protected beacon is placed at z*;
the sensors read it as A_i z* + b_i, and its channel reports z* + d.
Shift the world: target z + d, placement z* + d, biases b_i − A_i d, beacon
correct. Then A_i(z + d) + (b_i − A_i d) = A_i z + b_i, the same for the
beacon's readings, and the channel reports z* + d in both worlds. Every
report the network receives is the same. So d is not identifiable from
the network's reports, whatever revision rule it runs. That is why its
consistency radius was unchanged in [CLAIM-tmpw11e6](CLAIM-tmpw11e6.md)'s runs (0.114 in both).

Checked numerically: `python3 -I scratch/formal/beacon_gauge_check.py`,
1,000 random draws of maps, biases, d, target and placement, with no
mismatch.

## What it shows

The regress of anchors is a symmetry limit, of the kind the record holds
elsewhere:
- **[LEAD-180](../leads.d/LEAD-180.md)'s relabelling** ([CLAIM-tmpxoxys](CLAIM-tmpxoxys.md)): dissent and attack swap
  without any observable change.
- **Factorization identified only up to a change of latent coordinates**
  ([CLAIM-148](CLAIM-148.md)).

The survey in [CLAIM-tmpw11e6](CLAIM-tmpw11e6.md) works because it breaks the symmetry. It
places a point whose position arrives by a different channel from the
beacon's. Each further anchor breaks the symmetry left by the one below
it, and leaves its own.

## Limits

The simulation's box-clipped target and box-uniform placements break the
symmetry at the edges. The identity is exact only for translation-invariant
laws, and the defeater says so.
