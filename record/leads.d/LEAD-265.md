---
number: 265
status: Open
formerly:
- LEAD-tmpmmfxt
title: 'Use simulated service ecologies as a testbed for the SRE readings: over-reliable providers and fallback erosion, retry amplification, operational overload under a protected allocation, error-budget precedence against fixed priorities, and utilization-funded recovery capabilities, each against a queueing or control baseline'
version: 1
stage: idea
method:
- formal
- operationalization
tags:
- software-engineering
- complex-systems
- operations-research
date: '2026-11-24'
line:
- readiness
- dependence-and-domination
advances:
- CLAIM-1256
- CLAIM-1328
- CLAIM-1288
- CLAIM-1262
- CLAIM-921
summary: >-
  A34 §19 and §20 of the exchange "Memes, Contracts, and Systemic
  Normativity" (ChatGPT, 2026-11-24): "I would prioritize several
  computational experiments based on established engineering problems",
  with relational reliability objectives as what the experiments would
  measure. Stage idea: A34 names experiments and record connections, no
  designs. The wording of the experiments is A's (ChatGPT, in the exchange
  "Memes, Contracts, and Systemic Normativity"); the selection and the
  baselines stated per experiment are the assistant's (Claude, in this
  session); adopting either is the owner's call.
---

<!-- inactive-ok-file: CLAIM-1256 CLAIM-1262 CLAIM-1288 CLAIM-1328 LIT-3202 LIT-3204 — Proposed, Deferred or new; filed or registered with the exchange 'Memes, Contracts, and Systemic Normativity', cited whatever their standing -->

# LEAD-265: Use simulated service ecologies as a testbed for the SRE readings: over-reliable providers and fallback erosion, retry amplification, operational overload under a protected allocation, error-budget precedence against fixed priorities, and utilization-funded recovery capabilities, each against a queueing or control baseline

## The idea

A34 §20 tabulates eight experiments. Those whose claims are filed:

| Experiment (A34) | Research question (A34) | Claim it would test |
|---|---|---|
| Over-reliable dependency | "Does increased provider reliability induce downstream fallback erosion?" | [CLAIM-1256](../claims.d/CLAIM-1256.md) |
| Retry amplification | "Can locally appropriate corrective responses produce systemic frustration?" | [CLAIM-1328](../claims.d/CLAIM-1328.md) |
| Operational overload | "Can immediate viability consume the resources required for self-formation?" | [CLAIM-1288](../claims.d/CLAIM-1288.md) |
| Recovery readiness | "Can utilization-based maintenance destroy rarely exercised capabilities?" | [CLAIM-921](../claims.d/CLAIM-921.md) |
| Error-budget governance | "Do conditional grants of precedence outperform fixed priorities under changing demands?" | [CLAIM-1262](../claims.d/CLAIM-1262.md), with A16's error-budget precedence, filed by another group |

The other three, "Hidden corrective subsidy", "Contractual drift" and
"Reflexive monitoring", bear on ideas introduced earlier in the exchange
and filed by other groups, and on [CLAIM-1064](../claims.d/CLAIM-1064.md)'s inquiry penalty.

A34's method: "The strongest methodological design would compare
organizations with matched ordinary service performance and different
developmental histories or governing arrangements. We would then perturb
their dependencies, resource budgets, monitoring systems and authority
structures." And its standard: "Established queueing theory, control
theory, reliability engineering, contract-based design and reinforcement
learning should serve as competing or complementary baselines. Nucleation
would need to demonstrate explanatory value beyond simply renaming known
engineering phenomena."

A34 §19's "relational reliability objectives" are the quantities such
runs would report ("Recovery readiness", "Dependency visibility",
"Contestation readiness", "Cost attribution" among eight), which A34 calls
"proposed extensions of our framework, not a standard SRE taxonomy", with
the caveat that "these properties are often difficult to measure
directly".

## What it would take

For each experiment, a design that fixes what A34 leaves open (the
assistant's):

- **Over-reliable dependency.** Consumers that keep a fallback at a
  maintenance cost and drop it when the provider's observed availability
  makes its expected value negative; providers held at the objective
  against providers whose realized availability exceeds it. Outcome:
  propagated failures per provider outage. The baseline is a consumer that
  plans to the declared objective, which should show no difference.
- **Retry amplification.** The gap fill of [CLAIM-1328](../claims.d/CLAIM-1328.md) shows that a
  load-independent failure probability gives bounded amplification; the
  run needs a goodput that falls under overload, against the metastable
  failure literature ([LIT-3204](../literature.d/LIT-3204.md)).
- **Operational overload.** One team budget split between reactive and
  engineering work, failure rates falling with engineering done; with and
  without a protected share, and with and without return of overflow,
  against Repenning and Sterman's model ([LIT-3202](../literature.d/LIT-3202.md)).

## Standing

Open, at stage idea. The wording of the experiments is A's; the designs
are the assistant's (Claude, in this session); adopting either is the
owner's call.

## Note of 2026-11-24: what the record already does, from U32 and A51 of the exchange 'Memes, Contracts, and Systemic Normativity'

<!-- inactive-ok-block: CLAIM-1338 — Proposed or new; the executed studies and claims this note checks the lead against, and the owner's thesis it answers -->
A51 Article 10: "This paper should not be an exercise in constructing new SRE-inspired toy models." Of the five experiments above, "Recovery readiness" is done: [CASE-343](../cases.d/CASE-343.md) runs the utilization-funded loop with and without decoupling for [CLAIM-921](../claims.d/CLAIM-921.md), and reproduces on a rerun of 2026-11-24. "Operational overload" is done in part by [CASE-412](../cases.d/CASE-412.md) (drills, reserves and carry-over under the peak rule, [CLAIM-878](../claims.d/CLAIM-878.md)). "Over-reliable dependency" has its mechanism demonstrated as [CLAIM-602](../claims.d/CLAIM-602.md) and [CLAIM-675](../claims.d/CLAIM-675.md) (Active), so a service-ecology run would test a known result in a new domain. "Error-budget governance" has [CASE-325](../cases.d/CASE-325.md)'s comparison of relational authority against control models as its nearest study, not the same question. "Retry amplification" is not held. Narrow the lead to retry amplification and to error-budget precedence, and cite the rest. The owner's U32 holds that the series' proposed experiments are "largely already satisfied by prior work" ([CLAIM-1338](../claims.d/CLAIM-1338.md)). The note is the assistant's (Claude, in this session); whether to narrow, lower or close the lead is the owner's call. No status change.
