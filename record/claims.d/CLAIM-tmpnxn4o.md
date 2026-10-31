---
status: Active
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
- ARG-tmptzqyx
complements:
- CLAIM-462
summary: >-
  From A24 of the exchange "Analyze nucleation concepts" (2026-10-31),
  answering the owner's U24 question whether corrigibility's desirability
  had been established. The arithmetic was rechecked by the turns' reader.
  This is the subject-matter half of the answer. The support half, that
  the record's constructions do not establish that corrigibility ought to
  be kept, is [ARG-tmptzqyx](../arguments.d/ARG-tmptzqyx.md), which this claim undercuts.
---

# CLAIM-tmpnxn4o: The value of keeping a corrective capacity is conditional on objectives, uncertainty and cost: a free, optional audit cannot lower a single time-consistent decision-maker's expected performance, but an audit that costs C to maintain and bears on k decisions with error rate ε is worth k(0.25 − 0.5ε) − C in the exchange's model, negative when C is large or k small, and where no hypothesis fits the world, correction gains no reward and improves only calibration

## The claim

**Free information.** For a single decision-maker with a fixed objective
and time-consistent preferences, an optional observation that costs
nothing cannot lower optimal expected performance. The agent can always
ignore it. This is the ordinary non-negative value of information.

**Costly correction.** The exchange's model is the regime-switching world
of [CASE-tmp061to](../cases.d/CASE-tmp061to.md). With the audit, the agent acts on the right regime with
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
