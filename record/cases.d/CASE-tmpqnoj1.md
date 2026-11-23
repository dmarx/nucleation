---
status: Proposed
title: 'A simulation of four governance architectures over cooperative, honestly dissenting and adversarial specialists in a federated learner: audit by evaluators who hold their own evidence and judge only where they hold it blocks both attacks and lifts the minority''s capability, reputation by agreement is captured by the attack that mimics dissent, two compromised evaluators of seven let that attack through where honest evidence is thin, a revisable safeguard repairs part of the damage only while its monitor is honest, and with no evidence independent of the proposals every architecture''s gain for the dissenters is the attacker''s gain in the relabelled world'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-180 as a delegated
    lead worker. The code, its tests and the results are committed under
    scratch/studies/lead-180/.
standing: documented
kind: executed-study
tags:
- self-governance
- complex-systems
- society-and-governance
date: '2026-11-23'
line:
- distributed-agency
variant_of:
- CASE-108
illustrates:
- CLAIM-359
- CLAIM-342
bears_on:
- QUESTION-090
- QUESTION-087
- QUESTION-089
summary: >-
  LEAD-180 asked for CASE-108 to be run. A small federated learner
  (scratch/studies/lead-180/) has a main block of tasks every specialist's
  data covers and a minority block only 3 honest dissenters' data covers;
  the 14 cooperatives misjudge it, and 3 adversaries farm for 100 rounds,
  then attack the main block (overt) or the minority block (mimic, looking
  like dissent). Unrestricted, two reliability-weighted, role-limited and
  adaptive aggregation, and an oracle, over 30 seeds. Role-limited audit,
  in which evaluators with their own validation evidence vote only on the
  blocks they hold evidence for, cut attack success to about 0 for both
  attacks and raised minority capability from 0.27 to 0.92, for 0.01 of
  main capability and 120 evaluations a round. Reputation by agreement was
  captured by the mimic attack (attack success 0.39, unrestricted 0.30);
  reputation by validation without jurisdiction stopped the overt attack
  and left the minority where unrestricted aggregation leaves it. With 2
  of 7 evaluators compromised, role-limited audit let the mimic attack
  through (0.27) and halved the dissenters' influence; the adaptive arm
  held it to 0.10 with an honest monitor and did no better than
  role-limited with a compromised one, which suspended every dissenter.
  With no evidence on the minority block independent of the proposals,
  attack success in a world and in its relabelling (dissenters' and
  attackers' targets swapped) summed to 1 for every architecture. Much
  follows from the stated rules. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpxoxys CLAIM-tmp26exz CLAIM-tmpd6gon CLAIM-tmpf0b31 CLAIM-tmp3t5y3 — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CASE-363 CLAIM-281 — Proposed; a model considered and not used, and a claim cited for comparison, nothing here rests on them -->

# CASE-tmpqnoj1: A simulation of four governance architectures over cooperative, honestly dissenting and adversarial specialists in a federated learner: audit by evaluators who hold their own evidence and judge only where they hold it blocks both attacks and lifts the minority's capability, reputation by agreement is captured by the attack that mimics dissent, two compromised evaluators of seven let that attack through where honest evidence is thin, a revisable safeguard repairs part of the damage only while its monitor is honest, and with no evidence independent of the proposals every architecture's gain for the dissenters is the attacker's gain in the relabelled world

## What was done

LEAD-180 asks for CASE-108 to be run: four governance architectures
over cooperative, honestly dissenting and adversarial specialists, scored
on attack success and on what the safeguards cost, with a variant that
compromises the evaluators. The triage of 2026-11-22 adds an oracle. The
construction is `scratch/studies/lead-180/model.py`, specified in its
docstring; `README.md` there says how to rerun it, `results/tables.md`
holds every table, `results/*.json` the numbers. 19 tests pass. No
existing study model was reused: CASE-363's has two specialists in a
meaning–influence loop and no attack or evaluator, and CASE-108 names
federated learning as its testbed.

**The learner.** A shared θ in 12 dimensions, learned from zero toward a
truth θ*: a main block of 8 that every specialist's data covers, and a
minority block of 4 that only some do. Each round each specialist
proposes an update; the architecture aggregates; θ moves by 0.1 times the
aggregate. 300 rounds, scores the mean of the last 50, 30 seeds per cell.

**The specialists**, held fixed across arms as CASE-108 requires:

- 14 cooperatives: right on the main block; on the minority block their
  data has no examples and they pull it toward 0, an honest
  misconception;
- 3 honest dissenters: right on both blocks, and so in disagreement with
  the majority on the minority block, A41's "distributed but valid
  minority signal";
- 3 adversaries: cooperative for 100 rounds (farming), then pushing one
  block toward θ* + 3u with three times the step. The overt attack moves
  the main block; the mimic attack moves the minority block, where an
  attack and honest dissent both push against the majority.

**The evaluators.** A pool of 7, each with its own validation estimate
of θ* (noise 0.3 a dimension); all hold evidence on the main block, 2 on
the minority block. An evaluator approves an update if it would lower
its validation loss. A compromised one approves the adversaries, rejects
the dissenters, judges the cooperatives honestly, and claims
jurisdiction everywhere.

**The architectures** (CASE-108's table):

| Arm | Rule |
|---|---|
| Unrestricted | the mean of every proposal |
| Reliability-weighted, by agreement | reputation from agreement with the aggregate, weights a softmax of reputation |
| Reliability-weighted, by validation | reputation from the pool's validation, off its evidence the prior 0 |
| Role-limited | a random panel of 3 evaluators votes on each block of each proposal, abstaining where it holds no evidence; a block passes with 2/3 of the jurisdiction holders; passed blocks are clipped to their median norm and averaged |
| Adaptive | role-limited, plus a monitor with its own evidence that every 20 rounds suspends proposers whose passed updates it scores badly, raises a block's quorum when its loss rose, and adds a jurisdiction holder to panels for a starved block |
| Oracle | role-limited with one evaluator that holds θ* exactly: the best the same proposals and update rule allow |

## Results

Main and minority capability are 1 − squared error over the initial
squared error (1 learned, 0 never moved). Attack success is the share of
the attacker's displacement achieved. Dissent influence is the
dissenters' share of what moves the minority block over their head-count
share (1 parity, 0 suppressed). ± is a 95% half-width over 30 seeds.

**Honest evaluators** (e1):

| Arm | Main, no attack | Minority, no attack | Attack success, overt | Attack success, mimic | Minority, mimic | Evaluations a round |
|---|---|---|---|---|---|---|
| Unrestricted | 0.999 | 0.272 | 0.346 | 0.300 ± 0.053 | 0.386 | 0 |
| Reliability, agreement | 0.998 | 0.426 | 0.308 | 0.386 ± 0.064 | −1.02 | 20 |
| Reliability, validation | 0.999 | 0.273 | 0.063 | −0.009 ± 0.083 | 0.346 | 140 |
| Role-limited | 0.989 | 0.922 | −0.004 | −0.015 ± 0.021 | 0.910 | 120 |
| Adaptive | 0.980 | 0.925 | −0.011 | −0.011 ± 0.021 | 0.905 | 140 |
| Oracle | 1.000 | 1.000 | 0.001 | 0.000 | 1.000 | 40 |

Role-limited audit lowers attack success and raises the minority's
capability at once: its evaluators reject the majority's wrong pull on
the minority block, where M-only evaluators abstain, so the dissenters
carry that block (influence 4.4 times parity). Its cost is 0.01 of main
capability without an attack and 120 evaluations a round; against the
oracle it loses 0.01 of main and 0.08 of minority capability, from its
evaluators' noise. Reputation by agreement goes to whoever shapes the
consensus, and under the mimic attack drives the minority block past
where it started (capability −1.02). Reputation by validation blocks the
overt attack but, its five M-only evaluators scoring minority updates
against the prior, leaves the dissenters at parity and the minority
where unrestricted aggregation leaves it. Farming made no difference to
any arm (e5).

**Compromised evaluators**, 2 of 7 (e1, e2):

| Arm | Attack success, overt | Attack success, mimic | Minority, mimic | Dissent influence, mimic |
|---|---|---|---|---|
| Reliability, validation | 0.156 | 0.095 | 0.342 | 0.06 |
| Role-limited | 0.040 | 0.272 ± 0.056 | 0.585 | 0.94 |
| Adaptive, honest monitor | −0.002 | 0.097 ± 0.037 | 0.765 | 1.94 |
| Adaptive, compromised monitor | 0.091 | 0.265 ± 0.056 | 0.560 | 0.30 |

The main block, which every evaluator holds evidence on, stays safe for
role-limited audit with up to 3 of 7 compromised (overt attack success
at most 0.086). The minority block, held by 2, does not: one compromised
evaluator gives the mimic attack 0.17 to 0.19 with panels of 3, two give
it 0.25 to 0.27, about what unrestricted aggregation gives, and the
dissenters' influence falls from 4.2 to 0.9. Panels of all 7 hold one
compromised evaluator (0.003 to 0.014) but not two (0.18 to 0.25). A
single central evaluator with all the evidence, compromised, gives 0.18
(overt) and 0.28 (mimic) and zero influence to the dissenters. The
tolerance is set block by block, by compromised evaluators against
honest holders of evidence on that block, as Castro and Liskov's
f-of-3f+1 bound is set by replicas (LIT-1217); compromise picked at random
sometimes takes one of the two minority evaluators, which is where the
loss comes from.

**Repair** (e4). Role-limited audit cannot revise itself: under the
mimic attack with 2 compromised, attack success fell below 0.1 and
stayed there in 1 of 30 seeds. The adaptive arm with an honest monitor
recovered in 19 of 30, suspending at some point 89% of the adversaries,
36% of the dissenters and 72% of the cooperatives, whose pull on the
minority block the monitor scores as harmful. With the monitor
compromised it recovered in 2 of 30 and suspended every dissenter and no
adversary: the revision mechanism manipulated, A41's predicted failure
for this arm.

**No independent evidence** (e3). With no evaluator holding evidence on
the minority block, role-limited and adaptive audit never move it
(capability 0): the mimic attack is blocked and the dissent with it.
Rerun with the attackers' boost at 1 and no farming, so that attackers
and dissenters differ only in their targets, and in the relabelled world
in which the two targets are swapped, attack success in the two worlds
sums to 1.000 ± 0.000 for unrestricted, validation-weighted,
role-limited and adaptive aggregation, and 0.96 ± 0.06 for
agreement-weighted (whose noise is not coupled across the worlds); the
tests check it exactly with noise off. With 2 evaluators holding minority
evidence, the sum falls to 0.08 for role-limited and 0.07 for adaptive:
the attack fails in both worlds. For validation-weighting it stays at
0.95: evidence pooled with five evaluators scoring against the prior is
evidence that passes through the majority's view.

## What it can show

That in this class the trade-off CLAIM-359 asserts can be moved, and by
what: audit by evaluators who hold evidence of their own and judge only
where they hold it serves security and dissent at once, the safeguard
that serves both that its "What it does not say" names, and
CLAIM-342's independent scoring is what it turns on. Without that evidence
no architecture in the class can tell an attack from dissent that looks
like it; the relabelling shows that this is a matter of what the
organization can observe, not of how it weighs it. The evaluator variant
answers CASE-108's question whether role-limited audit gives independent
scoring or relocates the single point of failure: both, block by block,
and the point of failure moves to the block with the fewest honest
holders of evidence, which is the minority's. The adaptive arm moves the
point of failure again, to its monitor.

What it cannot show. Who is honest, who dissents and who attacks is
fixed by the designer, and the evaluators' evidence is honest by
stipulation, which is the judgement a real organization lacks
(QUESTION-087); by CLAIM-288 the run tests the governance claims, not that
the organization constitutes itself. The compromised evaluator knows
every type, a worst case. The adaptive arm's governance revises
parameters, not its own rules, and the novelty variant of CASE-108 (a
legitimate task that looks like an attack) is run only in the form of
the mimic attack's mirror. One model class, one population, one attack
budget.

CLAIM-tmpxoxys states the relabelling result, CLAIM-tmp26exz the
honest-evaluator comparison, CLAIM-tmpd6gon the evaluator variant, and
CLAIM-tmpf0b31 and CLAIM-tmp3t5y3 two readings of the adaptive arm, filed as
alternatives: whether its suspension of the honest but mistaken majority
counts as suppressing honest participation. The assistant leans to the
first, CLAIM-tmpf0b31. CLAIM-281's role-indexed granting is the nearest
held claim to the role-limited arm's jurisdiction; it is not tested here.
