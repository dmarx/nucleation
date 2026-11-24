---
status: Proposed
title: 'Coordinated unity of an organization''s activity does not entail unity of authority over it: unity of purpose, execution, specification and accountability can be had through differentiated jurisdictions and maintained interfaces, responsibility for an outcome does not entail every power over the processes that contribute to, evaluate or correct it, and more control over an organization need not mean more capacity in it'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that in organizations of the kind in question coherent execution
  and identifiable accountability are not achieved without one center
  holding directive, appointment and removal power over every contributing
  process, so that the differentiated arrangements A cites (maintained
  service contracts, an incident commander under independent review) depend
  on such a center after all; or evidence that increases in a center's
  control reliably increase the organization's capacities.
tags:
- society-and-governance
- operations-research
date: '2026-11-24'
line:
- rightful-power
- will-organization
grounds:
- LIT-tmptzlx9
summary: >-
  A40 §10's second candidate claim ("Coordinated unity does not entail
  unrestricted supervisory authority") in the exchange "Memes, Contracts, and
  Systemic Normativity" (2026-11-24), with A38 §2's five kinds of unity and
  A40 §3.1 to §3.3 and §3.5 as its parts. [CLAIM-404](CLAIM-404.md) and [CLAIM-736](CLAIM-736.md) hold
  related separations, of an evaluator's formal from its effective
  independence and of an actor's independence from control of its means.
  The wording is A's (ChatGPT, in the exchange "Memes, Contracts, and
  Systemic Normativity"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-706 CLAIM-736 LIT-tmp0qznk LIT-tmp4cqb2 LIT-tmptzlx9 TERM-128 — Proposed, Deferred or Rejected; filed or cited in the filing of the exchange 'Memes, Contracts, and Systemic Normativity', whatever their standing -->

# CLAIM-tmp1wlu2: Coordinated unity of an organization's activity does not entail unity of authority over it: unity of purpose, execution, specification and accountability can be had through differentiated jurisdictions and maintained interfaces, responsibility for an outcome does not entail every power over the processes that contribute to, evaluate or correct it, and more control over an organization need not mean more capacity in it

## The claim

A40 §10: "Collective activity can be realized through differentiated
jurisdictions and maintained relational constraints. Concentrating
authority may alter the independence and capacities of the processes
necessary for effective correction."

## Its parts

- **Five kinds of unity** (A38 §2): of purpose, execution, specification,
  accountability and authority. "The first four do not logically entail the
  fifth. A distributed organization can produce coherent activity through
  maintained contracts, differentiated jurisdictions and conditional grants
  of authority."
- **A bundle of powers** (A40 §3.1). Responsibility for an outcome is
  separable from objective-setting, coordination, supervision, direction,
  appointment and removal, and authority over the constraints on oneself:
  "an incident commander can be responsible for coordinating recovery
  without being entitled to redefine the reliability objective, suppress
  monitoring evidence or eliminate the independent review of their
  decisions." Executive authority as "a bundle of differentiated relational
  powers".
- **Control is not capacity** (A40 §3.2). ΔW_A > 0 does not imply ΔK > 0:
  "Increasing control may improve coordination. It may also destroy
  expertise, trust, alternative perspectives or independently maintained
  regulatory mechanisms." A40 cites Bednar ([LIT-tmptzlx9](../literature.d/LIT-tmptzlx9.md)), whose abstract,
  as Crossref carries it, says presidential power over policymaking "has two
  necessary components: control and capacity".
- **Unity through differentiation** (A40 §3.3): coordination over
  implementation with protected authority for evaluation, "unity through
  differentiated organization".
- **The converse** (A40 §3.5): "Independence does not establish normative
  governability" ([TERM-128](../terms.d/TERM-128.md)). Independence, autonomy, accountability,
  answerability and coordination are separate properties, and "The
  architecture must accommodate these requirements rather than maximize one
  without regard to the others."

## Correlated correction

A38 §2's illustrative model: three corrective mechanisms, each failing
independently with probability p, all disabled together by a common event
with probability q, fail together with probability q + (1 − q)p³. Checked
by enumerating the 16 joint outcomes with `python3 -I` (q = 0.05, p = 0.1:
0.05095 against p³ = 0.001 for independent mechanisms); with n mechanisms
the term is q + (1 − q)pⁿ, which tends to q, so "Adding more corrective
institutions does comparatively little if the predominant failure mechanism
disables all of them simultaneously." It is the common-shock form of
common-cause failure that reliability engineering uses. The pathology,
correlated corrective failure among checks and balances, is A36 §6's; the
model is new here.

## Where the record holds the neighbours

[CLAIM-404](CLAIM-404.md) (formal independence of an evaluator's procedure does not make
its evaluation independent), [CLAIM-736](CLAIM-736.md) (an opposition independent as an
actor whose capacity to change the arrangement depends on another's control
of its resources), [CLAIM-706](CLAIM-706.md) (execution impedance, independent constraint
and intervention opportunity vary independently) and [TERM-017](../terms.d/TERM-017.md)
(jurisdiction, precedence and suspension). None states the separation of
coordinated unity from unity of authority. A38 §2 also cites Hamilton's
Federalist No. 70 ([LIT-tmp4cqb2](../literature.d/LIT-tmp4cqb2.md)) and Madison's No. 51 ([LIT-tmp0qznk](../literature.d/LIT-tmp0qznk.md)) as
stating, respectively, executive unity and differentiated institutional
wills, "distinct requirements that need to be jointly accommodated".
