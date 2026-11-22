---
status: Proposed
title: 'If an evaluated party''s resources scale how strongly the evaluator''s conferral answers agreement, rather than tilting it toward one side, they enter the two-institution meaning–influence model only beyond first order at the symmetric state: they leave the linear symmetry-breaking condition unchanged, yet they capture the evaluator''s reading below that condition from a large enough push, toward the side the resources favour only, even when the evaluator''s evidence is independent of the party'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-015, from the
    executed study CASE-tmpd80em, as the alternative reading of resources
    to CLAIM-tmpz8q70's.
role: thesis
warrant: demonstrated
defeated_if: >-
  A rerun of CASE-tmpd80em's code (scratch/studies/lead-015/) in which,
  with E's conferral gain g_E(1 + ω m_P), the Jacobian at symmetry depends
  on ω, or in which no parameter set with spectral radius below 1 has a
  captured state reached from a start on the favoured side, or in which a
  captured state is reached from the disfavoured side below threshold.
tags:
- complex-systems
- society-and-governance
- self-governance
date: '2026-11-22'
line:
- distributed-agency
rests_on:
- CLAIM-tmp0v3wu
grounds:
- CASE-tmpd80em
bears_on:
- QUESTION-100
summary: >-
  The capacity reading of CLAIM-404's "resources", beside CLAIM-tmpz8q70's
  directional one. With the party's lean scaling the evaluator's conferral
  gain, g_E(1 + ω m_P), the channel's first-order term vanishes at
  symmetry, so CLAIM-tmp0v3wu's condition is unchanged (spectral radius 1.0048
  for ω from 0 to 2). Above threshold it enlarges the captured reading on
  its side (0.385 to 0.754) and shrinks the other (−0.151). Below threshold
  (spectral radius 0.987 to 0.996), and with θ = 0 (0.958), a start at 0.9
  on the favoured side was captured and a start at −0.9 was not. So under
  this reading the local condition understates the risk on one side. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmpd80em CLAIM-tmp0v3wu CLAIM-tmpz8q70 — new; the study and the condition this claim rests on, and the reading it is the alternative to, filed in the same batch -->

# CLAIM-tmp42aba: If an evaluated party's resources scale how strongly the evaluator's conferral answers agreement, rather than tilting it toward one side, they enter the two-institution meaning–influence model only beyond first order at the symmetric state: they leave the linear symmetry-breaking condition unchanged, yet they capture the evaluator's reading below that condition from a large enough push, toward the side the resources favour only, even when the evaluator's evidence is independent of the party

## The claim

CLAIM-404's evaluator is one "whose evidence or resources the evaluated party affects". CASE-tmpd80em reads "resources" two ways, and they are filed as alternatives.

- **Direction** (CLAIM-tmpz8q70): the party's resources favour the evaluator's specialist whose line agrees with the party's, an additive tilt ω m_P of the evaluator's conferral. It has a first-order term, enters the round trip as σ_E ω, and alone can destabilize symmetry.
- **Capacity** (this claim): the party's resources set how strongly the evaluator's conferral answers agreement, g_E(1 + ω m_P), as funding might buy an evaluator more of the scoring that drives its authority. At symmetry the term is ω m_P · m_E, second order, so it drops from the Jacobian.

Under the capacity reading, in CASE-tmpd80em:

1. *The linear condition is unchanged.* With θ = 0.6, ψ = 1, the spectral radius was 1.0048 at ω = 0, 0.5, 1 and 2.
2. *Beyond it, the resources pick a side.* The captured reading on the side the party's lean favours grew from 0.385 to 0.754 as ω went from 0 to 2; on the other side it shrank to −0.151.
3. *Below it, capture from a push, one-sided.* At θ = 0.4, ψ = 1 (spectral radius 0.996) with ω = 2, and at θ = 0.3, ψ = 0.8 (0.987) with ω = 5, a start at 0.9 on the favoured side was captured (m_E = 0.431 and 0.556) and a start at −0.9 returned to symmetry.
4. *Even with the evidence independent.* With θ = 0 (spectral radius 0.958), ω = 5 with ψ = 2 and ω = 10 with ψ = 1 or 2 were captured from the favoured side only.

So under this reading the symmetric state's stability is not the whole of the risk. An evaluator can pass CLAIM-tmp0v3wu's test and still hold a captured state on the side the party's resources favour, reached by a shock rather than by drift.

## Which reading

The two are not rival results: each is true of its model. They differ in what CLAIM-404's "resources" means, and so in which one its worked model is. The assistant leans to the directional reading for LEAD-015's condition, since the lead asks for the symmetry-breaking condition and only that reading has a linear term, and to keeping this one as the limit of that condition: the local test can miss a one-sided capture. Choosing, or keeping both, is the owner's call.

## What it does not say

- Where the captured states below threshold begin; no basin boundary was mapped.
- That capacity is how resources work in any institution.
- Anything about a capacity channel into the party.
