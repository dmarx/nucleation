---
status: Proposed
title: 'Whether the mathematics of modes applies to learned networks is held as the owner''s hypothesis with A''s test, which asks that independently justified modes and their couplings out-predict feature, circuit and parameter accounts; the assistant''s rule that such a mode must be invariant under the network''s function-preserving symmetries, with a construction in which a spectrum over unit order fails it; and one proposed study on modular addition, where the task supplies the modes; nothing in it has been run'
version: 1
defeated_if: >-
  A component misstated or misattributed here; an in-force component of
  this part of the learned-structure line (modes, their couplings and
  their invariance as a description of learned networks) left out without
  a reason given; or a link this account states that no component states.
  Its standing is its components'.
tags:
- learning-theory
- representation-learning
- mathematics
date: '2026-11-18'
line:
- learned-structure
integrates:
- CLAIM-698
- CLAIM-696
- CASE-270
- CASE-272
summary: >-
  The account of the modes part of the learned-structure line, filed at
  the synthesis review of 2026-11-18. All four components were filed on
  2026-11-15 from the continuation of the exchange "Explain String
  Theory", and all are Proposed. It maps them and adds nothing.
---
<!-- inactive-ok-file: SYNTHESIS-026 SYNTHESIS-029 SYNTHESIS-034 SYNTHESIS-tmp42cg7 CLAIM-698 CLAIM-696 CASE-270 CASE-272 CLAIM-263 CLAIM-629 THEORY-022 THEORY-1872 ADR-075 ADR-083 ADR-084 — Proposed; the components, the entries they cite and the decisions this account follows -->

# SYNTHESIS-tmpwrkqs: Whether the mathematics of modes applies to learned networks is held as the owner's hypothesis with A's test, which asks that independently justified modes and their couplings out-predict feature, circuit and parameter accounts; the assistant's rule that such a mode must be invariant under the network's function-preserving symmetries, with a construction in which a spectrum over unit order fails it; and one proposed study on modular addition, where the task supplies the modes; nothing in it has been run

## The account

- **The hypothesis and its test.** CLAIM-698 (the owner's hypothesis;
  the criterion and defeaters are A's; Proposed, interpretive) says the
  mathematics of waves and distributed modes "applies to how learning
  systems acquire, execute and compose computations". It "earns its
  place" only where a description in "independently justified modes and
  their couplings" out-predicts feature-, circuit- or parameter-level
  accounts fitted with the same information. It splits into three
  conjectures: modal formation in learning, modal interaction in
  computation, and individuation by interaction structure. The first is
  noted on QUESTION-217 (SYNTHESIS-029), the second on QUESTION-275
  (SYNTHESIS-034). Its held positive case is THEORY-022's Fourier
  characters. Its warning case is FREE-Merging (THEORY-1872), whose
  "frequencies" run over a weight matrix's row and column order.
- **What justifies a mode.** CLAIM-696 (the assistant's; Proposed,
  interpretive) says what CLAIM-698's "independently justified" must
  include: the mode must be "defined invariantly under the network's
  function-preserving symmetries". CLAIM-696 names its relation to
  CLAIM-698 itself: "[CLAIM-698] asks for 'independently justified'
  modes; this says what the justification must include." Its own
  `defeated_if` allows that it may only restate CLAIM-698. It calls
  itself "the spectral case of CLAIM-148's point" that a factorization is
  identified only up to a change of latent coordinates.
- **The construction.** CASE-270 (the assistant's; a stipulated
  construction, run on filing) illustrates CLAIM-696. Permuting a
  two-layer network's hidden units leaves its outputs unchanged. It moves
  the low-frequency share of a smooth update's spectrum along the
  hidden-unit axis from 0.985 to 0.193, and leaves the singular values
  fixed. It "cannot show" that FREE-Merging does not work, only that its
  spectrum "cannot be the reason".
- **The proposed test.** CASE-272 (A's "Experiment I"; a proposed study,
  not run) bears on QUESTION-275 and QUESTION-217. It would measure, over
  training checkpoints on modular addition, the coupling among Fourier
  modes and the moving-basis term Ω_τ. It asks whether changes in modal
  coupling forecast the circuit's formation better than training loss,
  Fourier energy and the progress measures of LIT-345. Its own limit:
  "The Fourier basis is given by the task", so a positive result would
  not show that modes can be found where no symmetry supplies them.
  CASE-274 (SYNTHESIS-tmp42cg7) is CLAIM-698's second named test.

## The components

- CLAIM-698, the owner's hypothesis, worded and operationalized by A,
  Proposed.
- CLAIM-696, the assistant's, filed at the owner's request, Proposed.
- CASE-270, the assistant's construction, Proposed.
- CASE-272, A's proposed study, Proposed.

## Links tested as claims

None at this review. CLAIM-696's relation to CLAIM-698 is stated by
CLAIM-696 itself, and the question whether it only restates CLAIM-698 is
written into its `defeated_if`. The account records that and does not
rule on it.

## Not stated on the record

- **CLAIM-696 and the symmetry entries of the frustration part
  (SYNTHESIS-026).** CLAIM-263 tests whether two networks compute the
  same way by "quotienting the architecture's full symmetry group".
  CLAIM-629 and CLAIM-366 show which frustration verdicts are constant on
  the orbits of function-preserving symmetries. CLAIM-696 asks the same
  invariance of a mode. It cites only CLAIM-148. No entry relates it to
  those three.

## What it does not say

- That learned networks obey a wave equation. CLAIM-698: "Gradient flow
  is dissipative relaxation, not oscillation."
- That any mode description has out-predicted a static account. Neither
  study has been run.
- That invariance suffices. CLAIM-696: "An invariant mode must still
  out-predict static accounts."
