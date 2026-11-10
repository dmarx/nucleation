---
status: Proposed
title: 'Whether a learner''s demands share a descent direction is decided by a test that a change of chart, or a function-preserving symmetry that is a diffeomorphism, leaves unchanged, while gradient cosines and a residual budgeted in a fixed Euclidean norm can change; the compatibility complex of the demands and the singular geometry of learning are invariants of one object; and in conventional training the demands, and any condition they put the learner in, belong to the optimizer–model–data system rather than to the network'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (the frustration diagnoses of a
  learner's demands, their invariance, and the unit they belong to) left
  out without a reason given; or a link this account states that no
  component states. Its standing is its components': a component retired
  or demoted takes its clause with it, and nothing here holds the clause
  up.
tags:
- learning-theory
- loss-landscapes
- information-geometry
- agency
date: '2026-11-10'
line:
- learned-structure
integrates:
- CLAIM-366
- CLAIM-629
- CLAIM-555
- CLAIM-263
- CLAIM-367
- CLAIM-356
- CASE-113
- CASE-193
- CASE-197
- QUESTION-122
- QUESTION-127
- QUESTION-286
bears_on:
- QUESTION-122
- QUESTION-127
---
<!-- inactive-ok-file: ADR-083 CASE-193 CLAIM-170 CLAIM-174 CLAIM-187 CLAIM-263 CLAIM-367 CLAIM-555 CLAIM-629 — Proposed; components, citations and the decisions this account follows, with their standing -->
<!-- inactive-ok-file: QUESTION-286 — Answered; components and citations, with their standing -->

# SYNTHESIS-tmp4xa7p: Whether a learner's demands share a descent direction is decided by a test that a change of chart, or a function-preserving symmetry that is a diffeomorphism, leaves unchanged, while gradient cosines and a residual budgeted in a fixed Euclidean norm can change; the compatibility complex of the demands and the singular geometry of learning are invariants of one object; and in conventional training the demands, and any condition they put the learner in, belong to the optimizer–model–data system rather than to the network

*A part account of the learned-structure line (ADR-083); the line's account is built over it and its sibling parts. Its components came from the exchange of 2026-10-17 (U30 to U36), the exchange "Organizational Nucleation and SLT" (2026-11-04) and the second synthesis review (2026-11-07).*

## The account

- **Which diagnoses are invariant.** CLAIM-366 (A35 §2, proved; Active)
  proves the first three rows of A35's table: the common-descent test
  0 ∉ conv{g_i} is unchanged by a smooth invertible change of chart, the
  sign of a Euclidean gradient inner product is not, and a budgeted test
  is invariant "only with the metric pulled back" (its title). That
  settles QUESTION-286 (Answered, "because CLAIM-366 (Active) settles it
  in full"). QUESTION-127 (Open) keeps the two rows CLAIM-366 does not
  prove: function-preserving symmetries and training trajectories.
- **Symmetry orbits.** CLAIM-629 (the assistant's derivation, Proposed)
  answers QUESTION-127 for the symmetries that act as diffeomorphisms:
  common descent is constant on their orbits, and a residual in a fixed
  Euclidean norm is constant only where the symmetry's derivative is
  orthogonal, so it changes along rescalings across a ReLU. Its item 3
  joins it to CLAIM-263: "Dividing by CLAIM-263's symmetry group before
  testing for common descent changes nothing." CLAIM-366's note of
  2026-11-07 narrows its own disclaimer to symmetries that are not
  diffeomorphisms, citing CLAIM-629.
- **The complex and the singular geometry.** CLAIM-555 (the owner's
  thesis, A5's construction; Proposed) makes each demand's acceptance set
  a sublevel set of its loss and the compatibility complex their nerve,
  so the complex and singular learning theory's learning coefficient are
  "two invariants of one object" (its title). The reader's addition there
  is that the complex is unchanged by any bijection of the parameters:
  "This is the set-level counterpart of CLAIM-366's result for common
  descent directions", and it answers QUESTION-127 "for this diagnosis".
  CLAIM-629 calls its own item 1 the first-order counterpart of that.
  CASE-197 (Active, construction) is CLAIM-555's one checked model: in
  the toy model of superposition the posterior's 5 → 6 transition is
  relief only for common tolerances from 0.0482 to 1/3, and "the complex
  alone says whether the transition is relief".
- **Singularity and compatibility apart.** CASE-193 (A8's construction
  with a fourth arm by the reader; Proposed) builds four model classes
  under one set of demands, regular or singular crossed with frustrated
  or compatible.
- **The quotient.** CLAIM-263 (the assistant's, Proposed) is the
  protocol that quotients the architecture's full symmetry group before
  comparing two trained networks. CLAIM-366 complements it and names it
  among the function-preserving symmetries it does not cover, and
  QUESTION-127 calls quotienting "CLAIM-263's protocol".
- **Whose demands, and whose condition.** CLAIM-367 (the owner's
  correction at U31, granted by A31; Proposed) individuates the unit for
  the training dynamics first: most of the governance of updates belongs
  to the optimizer–model–data system, so "a condition of training is not
  thereby a condition of the network". It grounds on CASE-113 (the
  owner's application case, A31's design; Active, stipulated), whose
  crossed interventions are CLAIM-367's defeater. Both treat gradient
  conflict as an indicator only, citing CLAIM-366: CASE-113, "The case
  needs only the indicator; nothing below turns on its being
  frustration." CLAIM-356 (the owner's U35, granted by A35; Active)
  makes the training organization the bearer of the goal its objective
  sets, "which is where CLAIM-367 puts training-time regulatory
  conditions", and it complements CLAIM-367.
- **The question these serve.** QUESTION-122 (the owner's U30; Open)
  asks whether a network in training can have affect-like states and to
  which unit they would belong. Its body places CLAIM-367 as a partial
  answer to the unit half, "so it is not written as an answer", and
  CLAIM-366 as the reason a negative inner product is not a finding of
  frustration. CLAIM-555 bears on it: whose demands they are is
  QUESTION-122's question.

Outside this part, seven of these entries are joined to the acquisition
part (SYNTHESIS-tmptiwlg), nine pairs in all: CLAIM-555 bears on QUESTION-275 and
QUESTION-363; CASE-197 names both and CASE-193 names QUESTION-275; the
notes of CLAIM-366, CLAIM-367 and CASE-113 dated 2026-10-26 read the reply
at T24 of the exchange "Experimental Infrastructure Review", from which
QUESTION-275 was filed; and QUESTION-275 names CLAIM-263's quotient.
CLAIM-543, of the persona entries, cites CLAIM-367 (the line's account).

## The components

- CLAIM-366, A's (A35 §2) at the owner's U35, thesis, demonstrated,
  Active; second line formal-apparatus. Answers QUESTION-286.
- CLAIM-629, the assistant's (Claude, second synthesis review, checked
  by script), thesis, demonstrated, Proposed; second line
  formal-apparatus. Rests on CLAIM-366 and CLAIM-365 (distributed-agency,
  formal-apparatus); answers QUESTION-127.
- CLAIM-555, the owner's thesis (U5), A5's construction with the
  reader's qualifications, thesis, interpretive, Proposed; second line
  will-organization. Rests on CLAIM-347 (distributed-agency); its note of
  2026-11-06 says it waits on the owner's assent to CASE-197.
- CLAIM-263, the assistant's restatement of CLAIM-187's protocol for
  trained networks, thesis, interpretive, Proposed; this line only.
- CLAIM-367, the owner's correction (U31) granted by A31, thesis,
  interpretive, Proposed; second line distributed-agency. Rests on
  CLAIM-152, CLAIM-170, CLAIM-174 and CLAIM-027.
- CLAIM-356, the owner's (U35) granted by A35, thesis, interpretive,
  Active; also will-organization and distributed-agency (it objects to
  CLAIM-288; the sweep of 2026-11-10 added distributed-agency).
- CASE-113, the owner's application case with A31's systems and
  interventions, thought-experiment, stipulated, Active.
- CASE-197, A5's proposed experiment run by the reader, construction,
  stipulated, Active; illustrates CLAIM-555 and CLAIM-347.
- CASE-193, A8's Proposal B with the reader's fourth arm, construction,
  fictional, Proposed; illustrates CLAIM-347. No component of this part
  cites it, and it cites none of them; its one link in the line is
  QUESTION-275.
- QUESTION-122, the owner's (U30), Open.
- QUESTION-127, A34 §6G at the owner's U35, Open; narrowed on
  2026-10-27.
- QUESTION-286, split from QUESTION-127 on 2026-10-27, Answered by
  CLAIM-366.

## Links tested as claims

None is filed as a claim from this part.

- **The diagnoses sorted by the group they are invariant under.** Tested
  at the second synthesis review (curation of 2026-11-07) and not
  admitted: the sort is QUESTION-127's own target, and CLAIM-555 and
  CLAIM-629 hold the two invariances found.
- **Bearer of the goal and bearer of the condition as one unit.** Stated:
  CLAIM-356's "Whose goal" section, quoted above.
- **Quotienting before diagnosing.** Stated: CLAIM-629's item 3.

## Not stated on the record

- **CASE-193 against CLAIM-555.** Both were filed from the same
  exchange, and CLAIM-555's defeater excepts "two learners with the same
  nerve and different learning coefficients". No relation or mention
  joins them.
- **Trajectories.** QUESTION-127's second remainder, whether a diagnosis
  of an actual training run survives a change of optimizer, has no
  answer in this part. CASE-113's optimizer arm is the design; THEORY-253
  is the one solvable instance it cites.
- **Whether CLAIM-366's invariance and CLAIM-367's unit meet.** No
  component says whether a chart-invariant diagnosis is thereby a
  property of the network rather than of the training organization.

## What it does not say

- That any network in training is frustrated, or feels anything
  (CLAIM-367, QUESTION-122).
- That the compatibility complex and the learning coefficient carry the
  same information: CLAIM-555 says the nerve is coarser, and CASE-197's
  transition changes no Betti number.
- That SGD follows the posterior (CLAIM-555, CASE-197; QUESTION-363).
- Anything about symmetries that are not diffeomorphisms, such as
  blow-ups (CLAIM-305, CLAIM-629).
- Anything with standing of its own.
