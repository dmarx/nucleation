---
number: 117
status: Active
formerly:
- CASE-tmprbebk
title: 'Emergent specialization and recovery in a population of adaptive operators: identically parameterized operators whose contributions, influence and training opportunities co-evolve over a changing task distribution, compared across fixed and learned features, uniform, endorsement-based and contribution-based influence, coupled and decoupled training exposure, and imposed and endogenous diversity'
version: 2
history:
- version: 2
  date: '2026-10-23'
  note: >-
    Note of 2026-10-23 added: mixture-of-experts results that already
    show specialization and routing effects. The proposal is unchanged.
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
<!-- inactive-ok-file: CLAIM-266 CLAIM-277 CLAIM-288 CLAIM-347 CLAIM-362 CLAIM-367 THEORY-514 CLAIM-284 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# CASE-117: Emergent specialization and recovery in a population of adaptive operators: identically parameterized operators whose contributions, influence and training opportunities co-evolve over a changing task distribution, compared across fixed and learned features, uniform, endorsement-based and contribution-based influence, coupled and decoupled training exposure, and imposed and endogenous diversity

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
| recovery opportunities | none beyond a small positive start; externally supplied reintroduction; internally maintained exploration or reactivation |
| authority-update rule | fixed by the modeller; revisable by the organization |
| specialist parameters during recovery measurement | frozen (recovery of the retained capability); trainable (recovery with re-adaptation) |

**Baseline.** Ordinary mixture-of-experts learning with contextual
routing. Without it, the study risks rediscovering specialization that
existing architectures already explain ([QUESTION-083](../questions.d/QUESTION-083.md)'s note of
2026-10-18).

## What is measured

No one metric substitutes for the rest.

| quantity | reads |
|---|---|
| feature Gram spectrum | representational redundancy ([QUESTION-135](../questions.d/QUESTION-135.md)) |
| I(operator; context) | statistical specialization |
| conditional marginal contribution | whether a specialist adds unique value |
| rare-operator recovery exponent, resident and conditional | recovery when rare ([QUESTION-132](../questions.d/QUESTION-132.md)) |
| recovery time after suppression | access to consequential roles ([CLAIM-362](../claims.d/CLAIM-362.md)) |
| held-out task risk, on a distribution independent of the selection loop | what is retained beyond endogenous evaluation ([QUESTION-134](../questions.d/QUESTION-134.md), [CLAIM-266](../claims.d/CLAIM-266.md)) |
| changes in the compatibility complex of the operators' demands | relief or creation of structural frustration ([QUESTION-133](../questions.d/QUESTION-133.md), [CLAIM-347](../claims.d/CLAIM-347.md)) |
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

- **Same participation, different mechanism.** Hold participation
  roughly constant while varying what maintains it: fixed usage
  balancing against endogenous recovery feedback. Matching the overall
  usage distribution is not enough. Two systems can share it while giving
  experts different contexts, training different distributions or
  performing differently. So match, as far as they can be matched
  together, context-conditioned participation, task performance and
  resource budget. If systems matched on these differ in recovery
  dynamics, the difference between equal allocation and stabilizing
  coexistence is measurable.
- **Fixed rule against revisable rule.** Learning within a fixed
  authority-update rule can show endogenous differentiation under fixed
  learning machinery. An organization that revises the rule itself is the
  stronger result, the one relevant to [CLAIM-284](../claims.d/CLAIM-284.md)'s self-governing
  organization. The design keeps them as separate conditions.
- **Active, dormant and reconstructed specialists.** Compare keeping a
  specialist through active participation, keeping it as a dormant but
  recoverable capability, and rebuilding it by later learning, on cost and
  on resilience ([QUESTION-132](../questions.d/QUESTION-132.md)). Measure recovery with the specialist's
  parameters frozen and with them trainable. The first tests whether the
  retained capability is still valued, the second whether the specialist
  can be re-adapted. A positive result in the second does not imply one
  in the first.
- **Coupled against decoupled exposure.** This tests [QUESTION-134](../questions.d/QUESTION-134.md):
  whether influence-dependent training destroys a marginalized
  specialist's competence.
- **Representational novelty against dynamical stability.** Check whether
  they change at the same parameter thresholds ([QUESTION-125](../questions.d/QUESTION-125.md)).

**Main threat to inference.** An external mechanism that supplies rare
opportunities can look like endogenous recovery. Zero is absorbing under
multiplicative dynamics, so recovery is first measured from a small
positive start, with no further intervention. Externally supplied
reintroduction and internally maintained exploration are separate
conditions. The external one cannot show endogenous maintenance. The
internal one may be an organizational achievement in its own right, if
its origin, cost and causal role are established independently. The
first version of this design placed every such mechanism outside the
organization; the owner's review corrected that.

## What the outcomes would show, and what they would not

A positive result, meaning stable niches, endogenous recovery and
reorganization after loss, would answer [QUESTION-132](../questions.d/QUESTION-132.md) for this class
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

## Note of 2026-10-23: what mixture-of-experts work already shows

A5 of the exchange of 2026-10-23, "Framework Overview Request" cited three works, registered unread: Switch Transformers
([LIT-tmpg44zc](../literature.d/LIT-tmpg44zc.md)), auxiliary-loss-free load balancing ([LIT-tmpl8rxn](../literature.d/LIT-tmpl8rxn.md)), and a
theory of mixture-of-experts in continual learning ([LIT-tmpffj9m](../literature.d/LIT-tmpffj9m.md)), which
by its abstract shows experts diversifying to specialize in tasks while
the router learns to route and balance load. So specialization and its
dependence on routing are shown. A5: what remains is "whether a specialist
can remain *recoverably competent but practically excluded*; how
endogenous recovery differs from externally imposed balancing; and whether
the organization can revise its routing standards in response to failures
those standards helped cause." [CLAIM-369](../claims.d/CLAIM-369.md)'s coexistence result (with
[CASE-118](CASE-118.md)'s growth-rate condition) is the record's own formal piece.
