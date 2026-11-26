---
status: Proposed
title: 'Optimization turns pathological by eroding its evaluators'
statement: >-
  An optimization process becomes organizationally pathological when its
  success under its own criterion progressively undermines the independent
  mechanisms through which its consequences can be evaluated and governed;
  three stages mark the way, which need not come in order or all occur:
  objective displacement, where a local criterion displaces the purpose it
  served; jurisdictional expansion, where the criterion gains influence over
  further domains; and constitutional capture, where the process compromises
  the mechanisms that could identify, constrain or reverse its consequences
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A comparison of optimization regimes with criteria equally harmful in
  their first effects, some of which eroded the independent evaluation of
  their consequences and some of which left it intact, in which the eroding
  regimes were corrected no later, at no greater cost and after no more
  harm than the others; or an argument that the erosion of evaluators is
  always a consequence of harm already done, so that it marks nothing the
  harm does not.
tags:
- society-and-governance
- ethics
- epistemology
date: '2026-11-26'
line:
- organizational-normativity
- dependence-and-domination
rests_on:
- CLAIM-1287
- CLAIM-tmpevykb
complements:
- CLAIM-624
- CLAIM-464
uses:
- TERM-tmp3rbue
summary: >-
  A8 of the exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26), closing its six case studies on the owner's U5: "a more
  precise hypothesis than simply saying that optimization is dangerous".
  A11 §VIII restates it at greater length as "the developmental pathology
  of optimization", adding dependence formation, endogenous ignorance and
  self-reproduction, and supplies the table of evidence each stage would
  need. It joins CLAIM-1287 (a narrow optimizer values weakening the
  constraints on it) to the jurisdiction claim filed from A6
  (CLAIM-tmpevykb), and states what the record held only for answerability
  (CLAIM-624). The six cases illustrate it; ARG-tmpfznfa says why they
  cannot ground it, and LEAD-tmpnn40s is the comparison that could. The wording is A's (ChatGPT, in the exchange "Alignment consequences brainstorm"); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1287 CLAIM-tmpevykb CLAIM-624 TERM-tmp3rbue ARG-tmpfznfa CASE-tmp0bk10 CASE-tmpts51k CASE-tmptm1pi CASE-tmp824kq CASE-405 CLAIM-tmpe432a CLAIM-652 CLAIM-656 ARG-071 SYNTHESIS-119 — Proposed or new; the claims it rests on and is set beside, the cases it is drawn from, the argument and lead filed with it -->

# CLAIM-tmpv3frk: Optimization turns pathological by eroding its evaluators

## The claim

The owner's U4 holds that "We're already paperclip maximizing" through
corporations (CLAIM-tmpe432a), and U5 asked for cases. A8
(https://chatgpt.com/share/6b07d7ae-9434-83ea-888b-9b20796f291c) chose six "that illustrate different mechanisms of organizational
misalignment rather than merely compiling examples of corporate
misconduct", and mapped each to a familiar alignment problem:

| Real-world case | Familiar alignment problem | Organizational mechanism |
|---|---|---|
| Tobacco (CASE-tmp0bk10) | Preference manipulation | Manufacturing demand and dependence |
| Cod fishery (CASE-tmpts51k) | Resource exhaustion | Destruction of viability conditions |
| Wells Fargo (CASE-151) | Reward hacking | Incentive-driven metric corruption |
| Purdue Pharma (CASE-405, its Purdue sub-case) | Instrumental influence | Encroachment on independent professional judgment |
| Volkswagen (CASE-tmptm1pi) | Evaluation-aware deception | Behaviour conditioned on oversight |
| Facebook (CASE-tmp824kq) | Recursive preference shaping | Optimization of the environment generating feedback |

From them A draws three stages and the claim:

> **Optimization becomes organizationally pathological when success under
> its own criterion progressively undermines the independent mechanisms
> through which its consequences can be evaluated and governed.**

Its examples of the third stage are "Volkswagen's evaluation evasion,
tobacco's suppression of research, economic lock-in around the cod
fishery".

What separates this from "optimization is dangerous" is where it puts the
pathology: not in the harm the criterion does but in what success does to
the capacity to see and correct that harm. A harmful criterion whose
evaluators stay independent is, on this claim, a bad policy; one that
captures them is a pathology.

## What it rests on

- **CLAIM-1287**: where the losses that discipline an institution depend
  on a state its actions change, a narrow optimizer values weakening them.
  A11 §5 adds "Independent evaluation" to that claim's constraints, with
  "Reduced detection of undesirable consequences" as what its erosion buys,
  and draws the consequence this claim needs: jurisdiction "can itself
  become an endogenous product of optimization".
- **CLAIM-tmpevykb** (A6's): the jurisdiction an objective holds, not the
  objective, sets what it can harm. The second stage is that jurisdiction
  widening.

Set beside it: CLAIM-624's second-order duty, to maintain the means for
violations to become knowable, contestable and correctable, is the
normative counterpart; CLAIM-464 the mechanism by which an intervention
makes its own correction costlier; CLAIM-652 and CLAIM-1064 two ways an
organization loses sight of harm without suppressing anything; CLAIM-656
the same for a newsroom's investigative capacity.

## A11's later version, and the evidence it asks for

A11 §VIII puts the stages into a longer chain and asks for each to be
established separately:

| Mechanism | Evidence required |
|---|---|
| Narrow optimization | Actual allocation and evaluation criteria |
| Jurisdictional expansion | Changes in the decisions governed by those criteria |
| Dependence formation | Changes in fallback options and exit costs |
| Endogenous ignorance | Changes in the capacity to recognize adverse consequences |
| Constitutional capture | Changes in the independence and effectiveness of corrective mechanisms |
| Self-reproduction | Evidence that optimization success causally maintains these changes |

It cites the record's own caution, ARG-071, which rejects the inference
from Wells Fargo to a regime reproducing its blindness through its
success, and SYNTHESIS-119: "similar macro-level patterns can arise
through very different processes." The table is the coding scheme
LEAD-tmpnn40s uses.

## Admission (ADR-075; the assistant's audit, 2026-11-26)

*A discriminating prediction.* Its premises say that an optimizer values
weakening its constraints and that jurisdiction sets harm. They do not
say that erosion of evaluators, rather than harm, is what distinguishes
the regimes that are corrected late and at great cost. The claim predicts
that it does, and its `defeated_if` names the comparison that would tell
against it. A8 names the condition itself: "a serious comparative study
should include organizations where similarly powerful optimization
processes remained effectively constrained."

## Limits

The six cases are selected on the outcome; ARG-tmpfznfa says what they
can and cannot carry. Three of them (tobacco, Volkswagen and, by its
plea, Purdue) are cases of conduct by people who knew what they were
doing, which illustrates the stages but not A's further thought that "No
unitary agent needed to want" the result; only the cod fishery and, by
the board's report, Wells Fargo come close to that.
