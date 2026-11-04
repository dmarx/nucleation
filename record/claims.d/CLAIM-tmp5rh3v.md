---
status: Proposed
title: 'When early activation reduces intervention delay under uncertainty, provisionally mobilizing a specialized resource can minimize expected loss even when the resource is more likely to be canceled than used; a cancellation rate alone therefore cannot identify waste'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An algebraic error in the threshold, or an inconsistency between the
  stated costs and the decision rule: for instance, positive parameters
  with H + c0 − c1 > 0 for which no threshold below 1/2 exists. It is not
  defeated by real operations whose costs are state-dependent or whose
  deployment carries risks the model omits; the claim is about the
  expected-loss model.
tags:
- operations-research
- probabilistic-modeling
- society-and-governance
date: '2026-11-04'
line:
- distributed-agency
- formal-apparatus
grounds:
- CASE-tmpt6fm7
complements:
- CLAIM-520
undercuts:
- ARG-tmp5fhgc
uses:
- TERM-tmp5t7y8
bears_on:
- QUESTION-tmpvweyo
- QUESTION-tmpw46vw
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 2 of A's "Proposed additions to Nucleation PR #401". In an
  expected-loss model of CASE-tmpt6fm7, provisional dispatch pays when
  p > (c0 + g)/(H + c0 − c1), and the threshold can lie below 1/2, so a
  resource more often cancelled than used can be rightly sent. Checked.
  It undercuts ARG-tmp5fhgc. The wording is A's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmpt6fm7 ARG-tmp5fhgc TERM-tmp5t7y8 — Proposed or new; A's proposals of 2026-11-04 and the readings they cite, as open -->

# When early activation reduces intervention delay under uncertainty, provisionally mobilizing a specialized resource can minimize expected loss even when the resource is more likely to be canceled than used; a cancellation rate alone therefore cannot identify waste

## The claim

**The model.** For the dispatch of CASE-tmpt6fm7, let
- p be the probability the specialized resource is needed;
- H the expected harm avoided by provisional rather than delayed
  dispatch, given need;
- c0 the incremental cost of provisional dispatch when it proves
  unnecessary, and c1 when it proves necessary;
- g a fixed expected coverage opportunity cost.

The expected advantage of dispatching provisionally (TERM-tmp5t7y8) over
waiting is

  ΔV = pH − (1 − p)c0 − pc1 − g = p(H + c0 − c1) − (c0 + g).

**The threshold.** If H + c0 − c1 > 0, ΔV > 0 exactly when

  p > (c0 + g)/(H + c0 − c1).

This is checked: the rearrangement is linear in p, and dividing by
H + c0 − c1 keeps the inequality's direction only because that quantity is
positive. If it is not positive, no threshold of this form exists.

**Below one half.** Positive parameters exist that put the threshold below
1/2. With H = 10, c0 = 1, c1 = 0.5 and g = 0.5, the threshold is
1.5/10.5 ≈ 0.143. At p = 0.2, ΔV = 0.2 × 10.5 − 1.5 = 0.6 > 0: dispatch
is right although the resource will be cancelled four times in five.

**So** a cancellation rate alone cannot identify waste. A high rate is
what this optimal policy produces when need is uncommon and the delay it
saves is costly. That undercuts ARG-tmp5fhgc's inference from low exercise
to waste. CLAIM-520 makes the converse point for a corrective capacity:
its value is conditional on cost and consequence, so neither low use nor
possible use settles it.

## What it does not say

- **That real dispatch policies are optimal.** It is an expected-loss
  model with fixed costs.
- **That costs and severity are constant.** They can depend on the state
  of the system, which QUESTION-tmpvweyo asks about.
- **Anything about deployment risk.** Travel and operation risks to the
  crew and the public are left out.
- **That high cancellation is desirable**, or that any given cancellation
  rate is right. It says only that the rate cannot, by itself, show waste.
