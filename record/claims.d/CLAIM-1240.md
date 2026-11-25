---
number: 1240
status: Proposed
formerly:
- CLAIM-tmp7rl3d
title: 'Taking each party''s reading of an ambiguous expression as a demand on their joint outcomes, clarifying a consequential misunderstanding relieves frustration by a new distinction only where the readings'' demands bear on different situations the expression conflated; where they demand different joint outcomes in the same situation, no distinction relieves them, only an outcome that meets both, and settling on one reading or rewording the demands is not relief'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A case in which a distinction alone makes the two demands jointly
  realizable, with the outcomes attainable in the shared situation and the
  declared demands held fixed; or a showing that the claim only restates
  CLAIM-347 for two parties. "The same situation" is fixed by the joint
  outcome the demands bear on; a feature introduced after the fact to
  separate situations (who is asking, when) absorbs every case and
  defeats nothing.
tags:
- epistemology
- society-and-governance
date: '2026-11-25'
line:
- will-organization
- pragmatic-transport
rests_on:
- CLAIM-347
- CLAIM-361
- CLAIM-532
- CLAIM-1298
grounds:
- CASE-191
complements:
- CLAIM-1329
- CLAIM-1280
summary: >-
  A join of the manuscript governance-of-becoming (Article 4, J4.1), in the
  corrected form an independent reader gave it on 2026-11-25, which passes
  [ADR-075](../decisions.d/ADR-075.md)'s test by derivation. As drafted, the join said clarifying a
  misunderstanding is productive exactly when it is relief; that fails,
  because a joint settlement on one reading is productive by the owner's
  [CLAIM-1329](CLAIM-1329.md) and not relief by [CLAIM-347](CLAIM-347.md) and [CLAIM-361](CLAIM-361.md). The warrant is
  demonstrated conditional on its first step, reading each party's
  reading as a demand on their joint outcomes. The wording is the
  reader's, filed by the assistant (Claude, in this session); adopting
  it, and its membership, is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1298 CLAIM-1329 CLAIM-1280 — Proposed; the components and the owner's thesis it qualifies -->

# CLAIM-1240: Taking each party's reading of an ambiguous expression as a demand on their joint outcomes, clarifying a consequential misunderstanding relieves frustration by a new distinction only where the readings' demands bear on different situations the expression conflated; where they demand different joint outcomes in the same situation, no distinction relieves them, only an outcome that meets both, and settling on one reading or rewording the demands is not relief

## Admission ([ADR-075](../decisions.d/ADR-075.md)): a derivation

1. Read each party's reading as a demand on their joint outcomes. This is
   the one free step, and the warrant is conditional on it.
2. A misunderstanding is consequential when the demands conflict: no joint
   outcome meets both ([CLAIM-347](CLAIM-347.md)'s frustration, for two parties).
3. Relief, in [CLAIM-347](CLAIM-347.md)'s and [CLAIM-361](CLAIM-361.md)'s sense, is reaching an outcome
   that meets the demands as declared, not dropping or rewording one.
4. A new distinction separates situations. It relieves the conflict only
   if the demands bear on situations it separates: then each demand can be
   met in its own situation ([CLAIM-1298](CLAIM-1298.md)'s refinement).
5. Where the demands bear on the same situation, a distinction leaves the
   conflict as it was; only an outcome that meets both relieves it.
   Settling on one reading drops a demand, and rewording changes it, so
   neither is relief, though either may be productive in the owner's sense
   ([CLAIM-1329](CLAIM-1329.md)).

[CASE-191](../cases.d/CASE-191.md) is the record's construction of frustration resolved by a new
distinction, where the demands are for different contexts: the first
branch.

## What it does not say

- Not that a settlement on one reading is unproductive: [CLAIM-1329](CLAIM-1329.md) and
  [CLAIM-1280](CLAIM-1280.md) count it as productive.
- Not that every misunderstanding is a pair of demands: step 1 is the
  claim's condition.

## Note of 2026-11-25: the complements field added

The manuscript's Article 4 (J4.1) noted that this claim "carries no
`complements` field" to [CLAIM-1329](CLAIM-1329.md) and [CLAIM-1280](CLAIM-1280.md), which its body
cites as counting a joint settlement on one reading as productive, and
left adding it "for the next pass" (the audit of what was left out,
2026-11-25, B24). The field is added: this claim says when clarifying is
relief, and the two say when it is productive, which are different parts
of what a clarification of a misunderstanding does. The title, the
derivation and the status are unchanged. The wording is the assistant's
(Claude, in this session); adopting it is the owner's call.

## Note of 2026-11-25: re-derived, and what holds it back

Re-derived on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-252](../leads.d/LEAD-252.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). No script was kept, so steps 1 to 5 were built into a finite model, `scratch/formal/clarification_relief_check.py` (standard library), run with python3 -I: situations conflated by the expression are a finite set, a joint policy assigns one outcome per cell of the current partition, each reading is a demand (the situations it bears on, the outcomes it accepts), relief is a policy meeting both as declared, and a distinction refines the partition. By exhaustion over up to four situations and three outcomes, 3,976 consequential conflicts: the 896 whose demands bear on disjoint situations are each relieved by some distinction, and the 3,080 whose demands share a situation are relieved by none, their accepted outcomes being disjoint; rewording a demand can make a pair realizable without relieving the declared one. A negative control admits the distinction the defeated_if excludes, splitting each situation by who is asking, and it relieves the overlapping demands, so the check can fail. Each step follows, given step 1, which the claim already states as its condition; the partial case (demands that share some situations and not others) falls under step 5 on the shared part. What holds it back: [ADR-057](../decisions.d/ADR-057.md)'s first criterion, its Proposed premise [CLAIM-1298](CLAIM-1298.md), as the lead already said. The note is the assistant's (Claude, in this session). No status change.
