---
status: Proposed
title: 'Where no process holds evidence on a block of tasks that does not come from the proposals themselves, a governance rule that treats its members alike cannot tell honest dissent from an attack that pushes the same block as hard: in a world and in its relabelling, with the dissenters'' and attackers'' targets swapped, it ends in the same place, so what it gains for the dissenters in one world it gains for the attacker in the other'
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed 2026-11-23 by the assistant, carrying out LEAD-180, from the
    executed study CASE-tmpqnoj1.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the symmetry argument, or a rerun of the code in
  scratch/studies/lead-180/ in which, with nobody holding evidence on the
  minority block, attackers and dissenters alike in number and step, and
  the rule invariant under relabelling its members, attack success in the
  world and in its relabelling does not sum to 1. A rule that is not
  invariant under relabelling its members (one told in advance who the
  dissenters are), or an evaluator with evidence on the block, does not
  count: the claim is stated for their absence.
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
- CLAIM-342
bears_on:
- QUESTION-087
- QUESTION-090
summary: >-
  From CASE-tmpqnoj1's relabelling check. If what the organization can
  observe about a block of tasks is only the proposals, and the
  dissenters' and the attackers' proposals differ only in their targets,
  then swapping the targets swaps which members are which and leaves
  every observation's distribution unchanged. A rule that treats members
  alike, as every architecture of CASE-108 does, then produces the same
  trajectory in both worlds, and the share of the way it moves toward the
  dissenters' target in one is attack success in the other: the two sum
  to 1. The study checks it for unrestricted, reliability-weighted,
  role-limited and adaptive aggregation (exactly with noise off; 1.000 ±
  0.000, and 0.96 ± 0.06 for agreement-weighting, over 30 seeds). With
  two evaluators holding evidence of their own on the block the sum falls
  to 0.07 to 0.08. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpqnoj1 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmpxoxys: Where no process holds evidence on a block of tasks that does not come from the proposals themselves, a governance rule that treats its members alike cannot tell honest dissent from an attack that pushes the same block as hard: in a world and in its relabelling, with the dissenters' and attackers' targets swapped, it ends in the same place, so what it gains for the dissenters in one world it gains for the attacker in the other

## The claim

The argument. Let the dissenters push the minority block toward θ*, the
attackers toward θ_adv, with the same number and step, and let nothing
else the organization observes depend on which of the two is true. In
the relabelled world θ_adv is the truth and the roles of the two groups
are exchanged. The organization's observations, the proposals and any
evidence about the other blocks, have the same distribution in both. A
rule invariant under relabelling its members therefore yields the same
distribution of θ. Attack success in the first world is (θ − θ*)·u/τ
with θ_adv = θ* + τu; in the second it is (θ − θ_adv)·(−u)/τ, which is
1 minus the first. So whatever the rule does, its gain toward the
dissenters' target in one world is the attacker's gain in the other.

CASE-tmpqnoj1 checks it for CASE-108's architectures, the tests exactly
and the run over 30 seeds. Role-limited audit with no evidence on the
block never moves it, which blocks the attack and the dissent together;
unrestricted aggregation moves it a little in both directions. Neither
escapes the identity. What does is evidence on the block whose arrival
and scoring do not pass through the proposals: with two evaluators
holding it, attack success in the two worlds sums to 0.07 to 0.08 for
role-limited and adaptive audit, and the attack fails in both. That is
CLAIM-342's condition, here a necessary one for this class.

So the answer the lead asks for, whether an architecture can lower
attack success without suppressing honest dissent, is conditional: not
without such evidence, whatever the architecture.

## What it does not say

- It does not say an organization can never tell an attack from dissent
  without outside evidence. Attackers who push harder, or differ in
  number or in what else they do, break the symmetry; the claim is for
  the case where they do not.
- It does not say who holds the evidence must be outside the
  organization. The evaluators in the study are members; what matters is
  that their evidence does not come from the proposals.
- It does not settle QUESTION-087. That evidence was honest by stipulation,
  and whether a standard internal to the organization supplies it is the
  question.
