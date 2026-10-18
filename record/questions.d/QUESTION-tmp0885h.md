---
status: Open
title: 'Under what conditions do initially equivalent adaptive operators differentiate into functionally complementary specialists that each have positive recovery growth when rare, rather than into roles kept in place by external load balancing or by persistent authority asymmetries?'
version: 1
tags:
- complex-systems
- ecology
- self-governance
date: '2026-10-18'
line: distributed-agency
refines:
- QUESTION-083
summary: >-
  The central mathematical question of the synthesis the owner relayed on
  2026-10-18. [QUESTION-083](QUESTION-083.md) asks whether operators sharing one update rule
  can come to hold differentiated authority. This asks the coexistence
  version: does the differentiation produce stabilizing negative frequency
  dependence, meaning every specialist recovers when rare (Chesson's
  stabilizing mechanisms, [LIT-1219](../literature.d/LIT-1219.md), unread)? Or is it held in place
  from outside, or by one process's entrenched advantage? An answer is a
  population model that derives the interaction structure from learned
  contributions, states recovery criteria, and finds the regimes of
  coexistence and exclusion. Heterogeneous embeddings, unequal routing
  weights or persistent expert identities do not answer it.
---
<!-- inactive-ok-file: CLAIM-277 CLAIM-362 LIT-1219 THEORY-306 THEORY-548 — Proposed or Deferred; open claims, readings and works cited as open, nothing here rests on their being settled -->

# QUESTION-tmp0885h: Under what conditions do initially equivalent adaptive operators differentiate into functionally complementary specialists that each have positive recovery growth when rare, rather than into roles kept in place by external load balancing or by persistent authority asymmetries?

## Why it is a question

Differentiation that is merely present does not show coexistence. Three
outcomes look alike from usage statistics and differ in kind:

1. **Stabilizing coexistence.** Each specialist, made rare, recovers
   because the resident organization leaves its niche open. This is
   Chesson's stabilizing mechanism ([LIT-1219](../literature.d/LIT-1219.md), unread).
2. **Imposed diversity.** Specialists persist because a programmed load
   balancer or a floor on influence keeps them from vanishing.
3. **Entrenched asymmetry.** One or a few processes hold authority
   through early advantage, the [CLAIM-277](../claims.d/CLAIM-277.md) loop, and the rest persist as
   residue.

**A recovery exponent.** Suppose operator i has influence w_i(t) and
contribution F_i(c_t, w_t), with ẇ_i = w_i F_i(c_t, w_t). Here w_i is an
unnormalized participation intensity. If influence is a normalized share,
the dynamics are of replicator type and F_i is measured against the
population mean (CLAIM-tmpc36bo, "Two boundaries of application"). While the others
follow a resident regime and i is very rare, its long-run recovery
exponent is

  λ_i = lim_{T→∞} (1/T) ∫₀ᵀ F_i(c_t, w_{−i}(t)) dt,

when the limit exists along the resident dynamics. With discrete
multiplicative updates it is the average log growth factor. λ_i > 0 means
the rare specialist recovers from small positive influence. λ_i < 0 means
the resident organization drives it toward exclusion. It is a statement
about recovery, not about equal weights: a specialist can hold little
influence most of the time and still have λ_i > 0.

**A wrinkle.** A specialist useful only during rare events can have
negative average growth over the full context distribution and still be
critical when the event comes. Two quantities are worth separating:
λ_i^resident, the long-run recovery exponent, and λ_i^conditional(C), the
recovery exponent during a specified context class C. The second is not a
substitute for the ecological invasion rate. It may better capture what
[CLAIM-362](../claims.d/CLAIM-362.md) cares about, a process keeping access to consequential roles
when its contexts recur. A process may not merit continuous presence in
the active coalition and still merit preservation as a dormant
capability.

**An ablation the answer needs.** Because zero is absorbing under
multiplicative dynamics, recovery should first be tested from small
positive abundance or influence, n_i(0) = ε > 0. The specialist then
recovers or declines under the resident dynamics with no continuing
intervention. That is how an invasion exponent is normally evaluated.
Externally supplied reintroduction and internally maintained exploration
are distinct interventions. The first cannot establish endogenous
maintenance. The second may be an organizational mechanism of
persistence, and so may be one of the achievements under study, but its
origin, resource cost and causal role must be established independently.
The first filing said testing recovery "needs some reintroduction" and
put the supplying mechanism outside the organization. The owner's review
corrected both: the endogenous protection of rare specialists should not
be defined away before it is studied. A model does not exhibit
coexistence merely because a programmed lower bound on influence keeps
every operator above zero. Uniformity-promoting objectives
([THEORY-306](../theory.d/THEORY-306.md), the equal-cluster prior of joint-embedding objectives) are
the representation-learning version of imposed diversity. A specialist
useful 1% of the time need not be active 20% of the time because there
are five specialists.

**Three ways to keep a specialist.** Recovering influence when the context
returns is one achievement. The organization might instead:

1. maintain the specialist through **active participation**;
2. maintain it as a **dormant but recoverable** capability, kept without
   being continuously activated;
3. **reconstruct** a lost specialist through later learning.

These can differ greatly in cost and resilience. Dormant preservation is
the analogue of memory, organizational archives and protected minority
expertise. It is also why positive long-run invasion growth need not be
the only criterion of valuable coexistence. Whether retention without
activation is possible when training follows influence is
QUESTION-tmpn0znj's question.

**Nonlinear transitions.** Coexistence and exclusion can change abruptly
with parameters, which bears on the open nonlinear-transition questions
(QUESTION-125; CLAIM-330 on the coupled loop; THEORY-136 on what evidence
shows alternative stable states). A model with positive feedback and
exclusion is not thereby bistable, and it need not have a cusp. That has
to be shown in the model, not inferred from the ingredients.

## What would answer it

A population model in which:

- the interaction structure is derived from the operators' learned
  contributions, not assumed;
- the recovery criteria λ^resident and λ^conditional are stated;
- the parameter regimes of each of the three outcomes are found.

In the potential case [CLAIM-tmpc36bo](../claims.d/CLAIM-tmpc36bo.md) gives the recovery test as a marginal
value, s_i = −∂_i L. A restricted theorem would be a natural first
target. For symmetric competitive interactions and bounded niche
adaptation, find sufficient conditions under which a differentiated
equilibrium is locally asymptotically stable and every active specialist
has positive growth when reintroduced into the resident equilibrium
without it. Then ask which conditions fail when symmetry is relaxed,
adaptation is delayed ([THEORY-548](../theory.d/THEORY-548.md)), or training opportunities depend on
current influence ([QUESTION-tmpn0znj](QUESTION-tmpn0znj.md)). With more than two operators,
coexistence should be judged by invasion graphs (Hofbauer and Schreiber
2022), not pairwise tests.

## What would not answer it

Heterogeneous embeddings, unequal routing weights or persistent expert
identities. Mixture-of-experts routing already produces specialization,
and an answer must show more than it does ([QUESTION-083](QUESTION-083.md)'s note of
2026-10-18).
