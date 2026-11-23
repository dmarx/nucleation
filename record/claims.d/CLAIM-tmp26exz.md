---
status: Proposed
title: 'In a simulated federated learner with honest evaluators, audit by evaluators who hold validation evidence of their own and vote only on the tasks they hold it for lowered attack success to about zero for an overt attack and for one that mimics dissent, and raised the minority''s capability from 0.27 to 0.92, for 0.01 of main capability; reliability-weighting by agreement was captured by the mimic, and by validation without that limit of jurisdiction it stopped the overt attack and left the dissenters where unrestricted aggregation leaves them'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-180, from the
    executed study CASE-tmpqnoj1.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun of scratch/studies/lead-180/ (run.py e1, e3), or a correction of
  its code, in which role-limited audit with honest evaluators does not
  lower attack success below unrestricted aggregation's for both attack
  classes while raising minority capability above it, or in which
  validation-weighting without jurisdiction does as well for the
  minority. A different population or attack in which the ordering
  changes bounds the claim rather than defeating it: it is stated for
  this one.
tags:
- self-governance
- complex-systems
- society-and-governance
date: '2026-11-23'
line:
- distributed-agency
grounds:
- CASE-tmpqnoj1
corroborates:
- CLAIM-359
- CLAIM-342
bears_on:
- QUESTION-090
- QUESTION-089
summary: >-
  [CASE-tmpqnoj1](../cases.d/CASE-tmpqnoj1.md)'s honest-evaluator comparison. Role-limited audit did
  better than unrestricted aggregation on both of [CASE-108](../cases.d/CASE-108.md)'s scores at
  once: attack success −0.004 (overt) and −0.015 (mimic) against 0.35 and
  0.30, minority capability 0.92 against 0.27, the dissenters carrying the
  minority block at 4.4 times their head-count share. The mechanism is
  jurisdiction: evaluators without evidence on the minority block
  abstain, and those with it reject the majority's mistaken pull. The
  same evaluators pooled without that limit (validation-weighting) stop
  the overt attack (0.06) and leave the minority at 0.27. Reputation by
  agreement is captured by the attack that mimics dissent (0.39). The
  cost is 0.01 of main capability and 120 evaluations a round; against
  the oracle, 0.01 of main and 0.08 of minority capability. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-tmpqnoj1 CLAIM-tmpd6gon — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmp26exz: In a simulated federated learner with honest evaluators, audit by evaluators who hold validation evidence of their own and vote only on the tasks they hold it for lowered attack success to about zero for an overt attack and for one that mimics dissent, and raised the minority's capability from 0.27 to 0.92, for 0.01 of main capability; reliability-weighting by agreement was captured by the mimic, and by validation without that limit of jurisdiction it stopped the overt attack and left the dissenters where unrestricted aggregation leaves them

## The claim

[CASE-tmpqnoj1](../cases.d/CASE-tmpqnoj1.md), e1 and e3, 30 seeds each:

| Arm | Attack success, overt | Attack success, mimic | Minority capability, no attack | Main capability, no attack |
|---|---|---|---|---|
| Unrestricted | 0.346 | 0.300 | 0.272 | 0.999 |
| Reliability, agreement | 0.308 | 0.386 | 0.426 | 0.998 |
| Reliability, validation | 0.063 | −0.009 | 0.273 | 0.999 |
| Role-limited | −0.004 | −0.015 | 0.922 | 0.989 |
| Oracle | 0.001 | 0.000 | 1.000 | 1.000 |

This is the case [CLAIM-359](CLAIM-359.md)'s "What it does not say" names, a safeguard that
serves security and dissent at once, observed and measured; the record
held it as an argument. What makes the safeguard one of that kind is
not separation of roles as such but two properties of the evidence its
critics use: it is their own, not the proposals', and they use it only
where they hold it. Remove the second (validation-weighting, where the
majority of evaluators score the minority block against the prior) and
the dissent is scored as the majority sees it; the attack is still
stopped. That is [CLAIM-342](CLAIM-342.md)'s rule in a population: scoring that passes
through the majority's interpretation, here through its prior, does not
protect the minority from it.

For [QUESTION-090](../questions.d/QUESTION-090.md), a condition under which coherence is not bought by
suppressing plurality: authority over each part of the joint work held
by those with evidence on it. For [QUESTION-089](../questions.d/QUESTION-089.md), the dissenters improved
the organization in the arms where authority over their block could
move to them (role-limited, 4.4 times parity) and not where it could not.

## What it does not say

- It does not say role-limited audit is robust. With compromised
  evaluators it is not, on the block where honest evidence is thin
  ([CLAIM-tmpd6gon](CLAIM-tmpd6gon.md)).
- It does not say jurisdiction can be read off. Which evaluator holds
  evidence on which block is given here; a real organization must
  establish it.
- It does not say agreement-weighting always fails. Here the consensus
  it rewards is wrong on the minority block and the mimic joins the
  dissenters there.
