---
status: Active
title: 'Emergent specialization and recovery in a population of adaptive operators: identically parameterized operators whose contributions, influence and training opportunities co-evolve over a changing task distribution, compared across fixed and learned features, uniform, endorsement-based and contribution-based influence, coupled and decoupled training exposure, and imposed and endogenous diversity'
version: 1
standing: stipulated
kind: proposed-study
tags:
- complex-systems
- ecology
- learning-theory
date: '2026-10-18'
line: distributed-agency
summary: >-
  The study proposed in the synthesis the owner relayed on 2026-10-18 for
  [QUESTION-083](../questions.d/QUESTION-083.md) and the questions filed with it. Operators differ only by
  initialization and experience. It measures whether stable niches emerge,
  whether specialists recover after long irrelevance, and whether the
  organization adapts after losing a dominant specialist. The decisive
  comparison holds the final diversity of operator usage roughly fixed
  while changing the mechanism that produced it. Ordinary mixture-of-experts
  routing is the baseline. Even positive results would not show
  self-constitution ([CLAIM-288](../claims.d/CLAIM-288.md)).
---
<!-- inactive-ok-file: CLAIM-266 CLAIM-277 CLAIM-288 CLAIM-347 CLAIM-362 CLAIM-367 THEORY-239 THEORY-514 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# CASE-tmprbebk: Emergent specialization and recovery in a population of adaptive operators: identically parameterized operators whose contributions, influence and training opportunities co-evolve over a changing task distribution, compared across fixed and learned features, uniform, endorsement-based and contribution-based influence, coupled and decoupled training exposure, and imposed and endogenous diversity

## The design

Contexts c_t ~ Π_t, a shared state x_t, and K operators with parameters
θ_i, identical in form and differing only by random initialization and
experience. Each proposes a_i = f_{θ_i}(x_t, c_t). The collective produces
a_t = 𝒜(a₁, …, a_K; w_t), where w_t is the operators' current influence.
Competence updates from experience, and influence from estimated
contribution. The exact update rules are experimental variables, not
assumptions about the organization.

| dimension | conditions |
|---|---|
| feature adaptation | fixed features; learned features |
| influence update | uniform; historical endorsement ([CLAIM-277](../claims.d/CLAIM-277.md)); context-sensitive contribution |
| competence exposure | training opportunities independent of influence; influence-dependent |
| diversity mechanism | none; fixed usage balancing; endogenous recovery feedback |
| environment | stationary; recurring regimes; abrupt distribution shifts |
| specialist loss | temporary suppression; complete removal; reintroduction |

**Baseline.** Ordinary mixture-of-experts learning with contextual
routing. Without it, the study risks rediscovering specialization that
existing architectures already explain ([QUESTION-083](../questions.d/QUESTION-083.md)'s note of
2026-10-18).

## What is measured

No one metric substitutes for the rest.

| quantity | reads |
|---|---|
| feature Gram spectrum | representational redundancy ([QUESTION-tmpw9b04](../questions.d/QUESTION-tmpw9b04.md)) |
| I(operator; context) | statistical specialization |
| conditional marginal contribution | whether a specialist adds unique value |
| rare-operator recovery exponent, resident and conditional | recovery when rare ([QUESTION-tmp0885h](../questions.d/QUESTION-tmp0885h.md)) |
| recovery time after suppression | access to consequential roles ([CLAIM-362](../claims.d/CLAIM-362.md)) |
| held-out task risk, on a distribution independent of the selection loop | what is retained beyond endogenous evaluation ([QUESTION-tmpn0znj](../questions.d/QUESTION-tmpn0znj.md), [CLAIM-266](../claims.d/CLAIM-266.md)) |
| changes in the compatibility complex of the operators' demands | relief or creation of structural frustration ([QUESTION-tmpjwshe](../questions.d/QUESTION-tmpjwshe.md), [CLAIM-347](../claims.d/CLAIM-347.md)) |
| viability under specialist removal | robustness and capacity to reorganize ([THEORY-134](../theory.d/THEORY-134.md)) |

An operator's functional niche can be defined relative to a context
distribution, as a proposed operational definition and not a standard
ecological one:

  𝒩_i(Π) = {c : ΔR_i(c) > 0},

where ΔR_i(c) is the marginal improvement from letting operator i take
part in the decision in context c. It is underspecified without the joint
task distribution and the downstream learner class. The organization can
change the distribution through its decisions, so the niche is partly
endogenous. Context-conditioned representations ([THEORY-239](../theory.d/THEORY-239.md)) give a way
to tell a functional niche from the mere frequency of its contexts.

## The decisive comparisons

- **Same usage, different mechanism.** Hold the final diversity of
  operator usage roughly constant while varying what produced it: fixed
  usage balancing against endogenous recovery feedback. If they match on
  usage and differ in recovery dynamics, the difference between equal
  allocation and stabilizing coexistence is measurable.
- **Coupled against decoupled exposure.** This tests [QUESTION-tmpn0znj](../questions.d/QUESTION-tmpn0znj.md):
  whether influence-dependent training destroys a marginalized
  specialist's competence.
- **Representational novelty against dynamical stability.** Check whether
  they change at the same parameter thresholds ([QUESTION-125](../questions.d/QUESTION-125.md)).

**Main threat to inference.** An external mechanism that supplies rare
opportunities, such as reintroduction or exploration, can look like
endogenous recovery. In multiplicative dynamics zero is absorbing, so
some reintroduction is needed to measure recovery at all. Its rate must
be an experimental factor, not part of the organization.

## What the outcomes would show, and what they would not

A positive result, meaning stable niches, endogenous recovery and
reorganization after loss, would answer [QUESTION-tmp0885h](../questions.d/QUESTION-tmp0885h.md) for this class
of models. It would not show self-constitution: the objectives are the
modeller's ([CLAIM-288](../claims.d/CLAIM-288.md)), and the unit that governs is the
optimizer–model–data system as much as the operators ([CLAIM-367](../claims.d/CLAIM-367.md)). The
synthesis proposed four levels of achievement, as a conceptual ordering
and not a theorem that each implies the earlier ones:

1. **differentiation**: distinct roles appear through adaptive dynamics;
2. **coexistence**: differentiated components persist through their
   interactions;
3. **endogenous regulation**: the organization maintains and revises the
   conditions of its own coordination;
4. **constitutive autonomy**: its continuing organization helps generate,
   maintain and govern the norms by which it regulates itself.

The study can reach the first two, and with influence rules that the
population revises, perhaps the third. The negative outcomes are as
informative:

- roles learned and not kept;
- roles kept only by imposed balancing;
- stable coexistence with no endogenous regulation;
- better global performance through systematic domination of some
  operators.

The relation between persisting and reorganizing is the contrast that
[THEORY-514](../theory.d/THEORY-514.md) examines, and resilience is not speed of return ([THEORY-132](../theory.d/THEORY-132.md)).
