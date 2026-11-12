---
number: 242
status: Proposed
formerly:
- CASE-tmpl4kyp
title: 'A fire-alarm chain probed at four points: one silent test detects a fault without locating it, four probes locate any single fault, and matched recovery rates hide different repair organizations until the outside service is withdrawn'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Result 2 now says that its numbers are CLAIM-649's defeasible
    reading, evidence and not entailment, as the claim was narrowed at
    the review of #483 the owner relayed on 2026-11-12. The review asked
    that the single-fault calculations and the matched-recovery example
    stay as illustrations; they do. No other change.
standing: fictional
kind: construction
tags:
- causality
- probabilistic-modeling
- control-theory
date: '2026-11-12'
line:
- formal-apparatus
- record-as-apparatus
variant_of:
- CASE-240
illustrates:
- CLAIM-414
- CLAIM-342
bears_on:
- QUESTION-285
summary: >-
  A's construction, A8's staged design (§"A concrete experiment") run in
  A10 of the exchange "Meaning Transmission Explained" (2026-11-07), on
  the owner's smoke detector and debugging cases ([CASE-243](CASE-243.md),
  [CASE-240](CASE-240.md)). A deterministic chain of injector, sensor, relay and
  actuator, one fault at a time, probed at four entry points; a 2%
  readout error for the Bayesian step; three repair architectures under
  stated damage and availability rates; a relay that fails only in heat.
  A10's Python file is not in the share, so the numbers here are
  recomputed from A's stated assumptions and agree with A's. The match
  between the mutual-maintenance and outside-service architectures is
  built in by the chosen rates. Every part restates a held result
  ([CASE-152](CASE-152.md), [CASE-163](CASE-163.md), [CLAIM-342](../claims.d/CLAIM-342.md), [CASE-161](CASE-161.md), [CLAIM-414](../claims.d/CLAIM-414.md), [CASE-186](CASE-186.md)); the
  case is their smallest common substrate. The construction's wording is
  A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-243 CASE-240 CLAIM-649 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CASE-163 CASE-202 THEORY-1092 — Proposed; the held cases and reading the construction restates, with their standing -->

# CASE-242: A fire-alarm chain probed at four points: one silent test detects a fault without locating it, four probes locate any single fault, and matched recovery rates hide different repair organizations until the outside service is withdrawn

## The construction

A8 proposed it, as "a small simulated alarm system with the following
staged variations", and A10 reported running it ("I've built and run a
small executable model"). A10 offered a download of
`nucleation_alarm_toy.py`, which the share does not carry. A10 is
explicit that "The code is a new minimal construction informed by the
Nucleation record, not a reproduction of PerspectiveLab's simulations."

**The chain.** An automated test-smoke injector, a sensor, a relay and a
sprinkler actuator, with one component failed at a time. The observable is
whether the sprinkler actuates. Four probes enter at different points:
the built-in injector, a relay bypass, a direct actuator command, and an
independent smoke source.

| mechanism | injector | relay bypass | actuator command | independent smoke |
|---|---|---|---|---|
| healthy | 1 | 1 | 1 | 1 |
| sensor failed | 0 | 1 | 1 | 0 |
| relay failed | 0 | 0 | 1 | 0 |
| actuator failed | 0 | 0 | 0 | 0 |
| injector failed | 0 | 1 | 1 | 1 |

## Results, recomputed

Rechecked on 2026-11-12 with a short script from A's stated assumptions
(exact fractions); each agrees with A10.

1. **Detection without location (A10 §1).** Under the injector probe the
   four faults give the same silence. A10: "**one failed smoke-injection
   test detects a problem but does not identify its source**." The five
   signatures are distinct, and no proper subset of the four probes
   separates all five states: location needs every probe. This is
   [CASE-152](CASE-152.md)'s missing response, which does not say what was missing, and
   [CASE-163](CASE-163.md)'s identification from probes within a known catalog; A8 §3
   also cites [THEORY-1092](../theory.d/THEORY-1092.md)'s localization by discrepancies.
2. **The likelihood ratio (A10 §2).** With a 2% readout error, a silent
   injector test has P(0 | fault)/P(0 | healthy) = 0.98/0.02 = 49, and
   silence in clean air 1. "**The observation is identical; its
   evidential meaning changes with the intervention.**" Under a uniform
   prior over the five states, P(some fault | silent test) = 3.92/3.94 ≈
   99.49%. That prior already gives a fault 0.8 before any test; A10
   calls it "an illustrative uniform prior". After all four probes return the sensor
   pattern, P(sensor failed) = 0.9604/1.0004 ≈ 96.00%.
   These are the defeasible reading of [CLAIM-649](../claims.d/CLAIM-649.md) at work. The silence
   shifts support by its likelihood ratio and entails nothing: with a 2%
   error rate, a healthy chain is silent under test one time in fifty.
3. **Detecting against using (A10 §3).** With a faulty sensor, an
   independent evaluator acts on the silent test; an evaluator that
   suppresses contradicting results does not, though the mismatch is
   "Physically observable". This is [CLAIM-342](../claims.d/CLAIM-342.md)'s condition, that a loop
   which scores its own evidence can lock in, and [CLAIM-349](../claims.d/CLAIM-349.md)'s separation
   of access from authority. Stated, not computed.
4. **Matched recovery, different organization (A10 §4).** The sensor
   fails and is replaced, the diagnostic apparatus is damaged, and then
   the relay fails. Each diagnostic channel is damaged with probability
   0.3; an outside service is available with probability 0.7. A single
   tester repairs the second fault with probability 0.7; two mutually
   maintaining testers 1 − 0.3² = 0.91; a single tester with the outside
   service 0.7 + 0.3 × 0.7 = 0.91; and with the service withdrawn, 0.7.
   A10: "**mutual internal maintenance and external restoration can
   exhibit identical recovery rates while implementing different causal
   organizations**", told apart only by intervening again. The two 0.91s
   are equal because the service's availability, 0.7, was set equal to a
   channel's survival, 1 − 0.3. A10 says redundancy's benefit "is built
   into the assumptions"; so is the match. With both channels destroyed
   the mutual pair fails: "Two mutually repairing components do not
   establish unlimited recursive correctability." That is [CASE-161](CASE-161.md)'s
   executed finding, that reciprocal production repairs the loss of one
   rule and not of both, and [CASE-076](CASE-076.md)'s twin pattern-keepers.
5. **The out-of-model fault (A10 §5).** A relay that works at room
   temperature fails in heat. Every probe passes, and the system is
   classed healthy until a high-temperature probe is added. A10
   separates learning "a new answer to an existing diagnostic question"
   from acquiring "a new question it previously could not ask", and
   grants that "The toy demonstrates the need for that expanded question.
   It does not yet implement an autonomous method for inventing it." That
   is [CASE-186](CASE-186.md)'s out-of-family arm and the distinction [QUESTION-285](../questions.d/QUESTION-285.md)'s note
   of 2026-10-31 records, rejecting a hypothesis against finding the
   family inadequate; [CLAIM-470](../claims.d/CLAIM-470.md)'s inquiry that "can revise what an answer
   could be".

## What it can show

That the record's diagnostic results meet on one transparent substrate:
detection without location, evidential weight changed by the
intervention, evidence present but given no authority, maintenance told
apart only by a further intervention, and a fault outside the probe
family. It illustrates [CLAIM-414](../claims.d/CLAIM-414.md) (step 4) and [CLAIM-342](../claims.d/CLAIM-342.md) (step 3). It is
the owner's smoke detector, carried by A into the record's existing
studies, as A8 proposed: "[CASE-163](CASE-163.md) already addresses the
interventional-identification part, while [CASE-186](CASE-186.md) addresses maintaining
the capacity for correction. The smoke-detector toy could connect them".

What it cannot show: anything about real fire-suppression systems (A10's
caption: "These interventions are abstract laboratory probes, not
instructions for testing a real fire-suppression installation"), or any
result the held cases lack. The matched rates of step 4 are a choice of
parameters, not a finding. Multiple faults, which A10 offers as an
extension, are not modelled. A8's last arm, letting "the system revise
and maintain its own testing policy", was not run. A8 §6's fresh-copy
control ([CASE-202](CASE-202.md)) is not part of the run either.

## Note of 2026-11-12: the chain as a readiness question

<!-- inactive-ok-block: CLAIM-632 CASE-210 — Proposed; the readiness claim and case, cited with their standing -->
The chain's response to a fire, sensor and relay and actuator, is a
conjunction of capacities in the readiness line's sense ([CLAIM-587](../claims.d/CLAIM-587.md)), and
per-component tests bound its readiness between the sum of their
probabilities less two and the weakest of them ([CLAIM-632](../claims.d/CLAIM-632.md); the note there
works an example). The injector is a capacity of the test, not the
response. The independent-smoke probe is the deadline-bound exercise
that tests the whole conjunction. [CASE-210](CASE-210.md)'s two departments are the
same pattern at the scale of an organization. The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
