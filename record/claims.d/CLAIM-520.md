---
number: 520
status: Active
formerly:
- CLAIM-tmpnxn4o
title: 'The value of keeping a corrective capacity is conditional on objectives, uncertainty and cost: a free, optional audit cannot lower a single time-consistent decision-maker''s expected performance, but an audit that costs C to maintain and bears on k decisions with error rate ε is worth k(0.25 − 0.5ε) − C in the exchange''s model, negative when C is large or k small, and where no hypothesis fits the world, correction gains no reward and improves only calibration'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the value-of-information argument or in the model's
  arithmetic (the audit's gain 0.75 − 0.5ε over a baseline of 0.5, and the
  calibration gain ½ ln(4/3) nats in the regime no hypothesis fits). It is
  not defeated by settings where corrigibility is worth its cost; the claim
  is that its value depends on the setting.
tags:
- self-governance
- information-theory
date: '2026-10-31'
line:
- distributed-agency
undercuts:
- ARG-042
complements:
- CLAIM-462
summary: >-
  From A24 of the exchange "Analyze nucleation concepts" (2026-10-31),
  answering the owner's U24 question whether corrigibility's desirability
  had been established. The arithmetic was rechecked by the turns' reader.
  This is the subject-matter half of the answer. The support half, that
  the record's constructions do not establish that corrigibility ought to
  be kept, is [ARG-042](../arguments.d/ARG-042.md), which this claim undercuts.
---
<!-- inactive-ok-file: CLAIM-tmp5rh3v ARG-tmp5fhgc ARG-042 — Proposed or new; A's proposals of 2026-11-04 on emergency readiness, cited as open -->
<!-- inactive-ok-file: NOTE-tmp4f0ld NOTE-tmpbp6yl NOTE-tmpsnl7o — Skimmed; the neighbours read for Smallwood and Sondik, Halfin and Whitt, and Jordan and Graves, cited from the reading of 2026-11-04 as open -->

# CLAIM-520: The value of keeping a corrective capacity is conditional on objectives, uncertainty and cost: a free, optional audit cannot lower a single time-consistent decision-maker's expected performance, but an audit that costs C to maintain and bears on k decisions with error rate ε is worth k(0.25 − 0.5ε) − C in the exchange's model, negative when C is large or k small, and where no hypothesis fits the world, correction gains no reward and improves only calibration

## The claim

**Free information.** For a single decision-maker with a fixed objective
and time-consistent preferences, an optional observation that costs
nothing cannot lower optimal expected performance. The agent can always
ignore it. This is the ordinary non-negative value of information.

**Costly correction.** The exchange's model is the regime-switching world
of [CASE-186](../cases.d/CASE-186.md). With the audit, the agent acts on the right regime with
probability 1 − ε and earns 0.75 − 0.5ε per decision. Without it the agent
earns 0.5, so the gain is 0.25 − 0.5ε per decision. Over k decisions,
against a maintenance cost C, the net value is k(0.25 − 0.5ε) − C. It is
negative when C is large, k small or ε near ½.

**Correction with nothing to gain.** In the regime no hypothesis fits,
where Y is ½ under either action, correcting the model gains no reward. It
improves calibration only, by KL(Bern(½) ‖ Bern(¾)) = ½ ln(4/3) ≈ 0.144
nats per observation. Whether that is worth paying for is a question about
objectives.

## What it does not say

- **That costless information never hurts.** The first result assumes one
  time-consistent decision-maker. A divided agent can do better with fewer
  options ([CASE-128](../cases.d/CASE-128.md)), and A29 endorsed that in the same synthesis without
  noting the tension.
- **Anything about accountability.** Epistemic correction answers to
  evidence and organizational correction to viability. Correction by
  others answers to their standing, and self-correction is not
  accountability ([CLAIM-462](CLAIM-462.md)).
- **That a corrigible process is good.** "A process that obeys every
  attempted correction is merely vulnerable to redirection. A process that
  resists every correction is insulated from accountability" (A24).

## Note of 2026-11-04: Kaelbling, Littman and Cassandra, "Planning and acting in partially observable stochastic domains", read

In a POMDP an audit is an information action, and the model computes its worth from cost and consequence: moving to a more certain belief "is only worthwhile when the value of the information (the difference in value between the two states) exceeds the cost of gaining the information" ([NOTE-tmp4f0ld](../notes.d/NOTE-tmp4f0ld.md); §4.1, p. 111). That qualifies the claim: its conditional value of a corrective capacity falls out of a standard model, of which the exchange's arithmetic is a special case. It leaves open the claim's point about correction where no hypothesis fits the world, since POMDPs assume a correct model. No status changes.

## Note of 2026-11-04: van Leeuwaarden, Mathijsen and Zwart, "Economies-of-Scale in Many-Server Queueing Systems", read

Skimmed in [NOTE-tmpbp6yl](../notes.d/NOTE-tmpbp6yl.md) as the stand-in for Halfin and Whitt (1981). It supports the claim in kind: in §4, headroom over mean load is set by trading a cost of capacity against a cost of delay, with an optimum β*, so how much spare capacity to keep depends on both. It also cautions that in the QED regime utilization tends to one, and pooled systems need proportionally less spare capacity; the capacity it sizes is busy, not held idle for rare events. No status changes.

## Note of 2026-11-04: Chou, Chua, Teo and Zheng, "Design for Process Flexibility", read

Skimmed in [NOTE-tmpsnl7o](../notes.d/NOTE-tmpsnl7o.md) as the stand-in for Jordan and Graves (1995). It supports the claim in kind. Full flexibility is costly, and a sparse long chain keeps at least 89% (uniform demand) or 96% (normal demand) of its expected sales, so the cheaper design is preferred. That comparison is of standing re-routing capacity under independent demand. It leaves open capacities kept for rare events, and under correlated demand a sparse design can lose almost everything. No status changes.

## Note of 2026-11-04: the same conditionality for a dispatched resource

A's [CLAIM-tmp5rh3v](CLAIM-tmp5rh3v.md) (Proposed) gives the dispatch analogue: provisional dispatch pays when p > (c0 + g)/(H + c0 − c1), which can be about 0.14, so neither a cancellation rate nor low use shows waste. [ARG-tmp5fhgc](../arguments.d/ARG-tmp5fhgc.md) (Rejected) is the counterpart of [ARG-042](../arguments.d/ARG-042.md). The claim is unchanged.
