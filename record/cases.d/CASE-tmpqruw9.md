---
status: Proposed
title: 'A ladder of outside maintainers for the mutual-maintenance model: a constant supply of the capacity, a supply running the same production law on a delayed reading of the structure, and the same law on its present reading; a brief knock to the structure separates the first two from internal production, the second by less as its delay shrinks, and no intervention on state separates the third until the internal pathway is cut'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- individuation
date: '2026-11-15'
line:
- transient-support
- distributed-agency
variant_of:
- CASE-tmp3ioyf
illustrates:
- CLAIM-522
summary: >-
  The assistant's construction, offered at the end of the filing of
  2026-11-15 and built when the owner asked for the assistant's ideas to
  be filed (scratch/formal/maintainer_ladder_check.py, run on filing). It
  extends [CASE-tmp3ioyf](CASE-tmp3ioyf.md)'s constant controller to a family that reproduces
  more and more of the production law. Fictional by construction, with
  illustrative parameters. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmp3ioyf — Proposed or new; the construction this varies and the claim it grounds -->

# CASE-tmpqruw9: A ladder of outside maintainers for the mutual-maintenance model: a constant supply of the capacity, a supply running the same production law on a delayed reading of the structure, and the same law on its present reading; a brief knock to the structure separates the first two from internal production, the second by less as its delay shrinks, and no intervention on state separates the third until the internal pathway is cut

## The construction

The model is [CASE-tmp3ioyf](CASE-tmp3ioyf.md)'s: ċ = −c + 4rc(1 − c), with the capacity r
produced either inside, ṙ = −r + 4c(1 − r), or by an outside controller.
It starts at the maintained state (c₊, r₊) ≈ (0.6545, 0.7236). Three
controllers:

- **constant:** r = r₊;
- **delayed:** ṙ = −r + 4c(t − τ)(1 − r), the same law run on a reading of
  c that is τ old;
- **exact:** the same law on c(t), [CLAIM-522](../claims.d/CLAIM-522.md)'s state feedback.

The state intervention is a brief knock: ċ reduced by 2 for 0.2 time
units, starting at t = 2. The measure is the largest gap in (c, r)
between the controlled and the internally maintained runs.

| controller | largest gap under the knock |
|---|---|
| constant | 0.146 |
| delayed, τ = 1.0 | 0.146 |
| delayed, τ = 0.3 | 0.083 |
| delayed, τ = 0.1 | 0.033 |
| delayed, τ = 0.03 | 0.010 |
| exact | 0 under every knock and start tried |

Cutting the internal production pathway separates the exact controller at
once: a gap above 0.3.

## What it shows

How far an intervention on state alone can expose an outside maintainer
depends on how much of the production law the maintainer reproduces. A
constant supply is exposed by a coarse knock. A delayed copy of the law is
exposed by a knock shorter than its delay, by a shrinking margin. An exact
copy is not exposed by any intervention on state, only by one on mechanism.

## What it cannot show

That the separation shrinks monotonically for every family of imperfect
controllers. Only this delay family was run. Nor does it show that the
margin in a real system would be measurable above noise.
