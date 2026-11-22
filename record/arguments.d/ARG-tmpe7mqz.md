---
status: Rejected
title: "Lee and colleagues' influence dynamics in Saxe's deep linear network and in small language models, read as grounds, carry the gated child's partial order of acquisition and the step in its per-example influence"
version: 1
form: evidence
grounds:
- THEORY-tmpm3ux2
concludes:
- CLAIM-828
tags:
- learning-theory
- representation-learning
date: '2026-11-22'
line:
- learned-structure
summary: >-
  [CLAIM-828](../claims.d/CLAIM-828.md) listed Lee et al. ([LIT-3001](../literature.d/LIT-3001.md)) among its grounds while it was
  unread, from A43's link between the gate's derivative and their finding
  that influence changes sign and peaks at transitions. Read
  ([NOTE-tmp1sot8](../notes.d/NOTE-tmp1sot8.md)), the paper carries neither the claim's thesis nor its
  influence step. Its toy has no gate and no weight decay, and orders its
  influence peaks by the modes' strengths, the order the claim says
  [THEORY-740](../theory.d/THEORY-740.md) already gives, not by dependency. Its influence, taken
  through Saxe's mode strength under gradient flow, peaks mid-transition
  where the claim's equilibrium derivative steps; the filer's check puts
  the peak of ∂g_t/∂s at 2.13 before it settles to 1. Rejected as a
  ground; [LIT-3001](../literature.d/LIT-3001.md) leaves [CLAIM-828](../claims.d/CLAIM-828.md)'s grounds. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
  Standing of the conclusion apart from this route: [CLAIM-828](../claims.d/CLAIM-828.md)'s gating
  and partial order stand on its own derivation (demonstrated, in the
  claim); that real networks acquire distinctions in an order of
  dependency rather than strength is untested, and [LEAD-207](../leads.d/LEAD-207.md) is the
  record's plan to test it.
---
<!-- inactive-ok-file: CLAIM-828 THEORY-tmpm3ux2 — Proposed; the claim and the reading this argument joins -->

# ARG-tmpe7mqz: Lee and colleagues' influence dynamics in Saxe's deep linear network and in small language models, read as grounds, carry the gated child's partial order of acquisition and the step in its per-example influence

## The inference

[CLAIM-828](../claims.d/CLAIM-828.md): a child feature gated by a parent switches on only when
gs > λ, so acquisition follows a partial order of dependencies; its
corrections paragraph adds that, in the gated model, every example's
first-order influence on q* is (∂q*/∂s)(yᵢφ(xᵢ) − ŝ)/n, a step at
activation. It cited Lee et al. ([LIT-3001](../literature.d/LIT-3001.md)) among its grounds. Ground:
[THEORY-tmpm3ux2](../theory.d/THEORY-tmpm3ux2.md).

## Critical questions (evidence)

**Does the evidence bear on the thesis?** No. Lee et al.'s analytic toy
is Saxe's two-layer linear network, with no gate and no weight decay.
Its influence peaks come in the hierarchy's order ("the time point of the
branching node matches the peaks in influence", §3), and in that model
the hierarchy's order is the order of the singular values: an order by
strength. The claim's own body says [THEORY-283](../theory.d/THEORY-283.md) and [THEORY-740](../theory.d/THEORY-740.md) give orders
by strength and that its contribution is an order by dependency. The
paper does not separate the two.

**Does it bear on the influence step?** As a contrast. The paper's
influence enters through diag(g′t(s)) ⊙ diag(S′ε) (C.6, Eq. 56), the
derivative of Saxe's mode strength at a fixed training time. Filer's check
(python3 -I) of Eq. 30, g_t(s) = s e^(2st/τ)/(e^(2st/τ) − 1 + s/g₀), at
s = 1, τ = 1, g₀ = 10⁻³: ∂g_t/∂s is 0 at the start, peaks at 2.1345 at
t ≈ 3.77, just after half strength (t ≈ 3.45), and settles to 1.0000. A
larger s raises the endpoint and brings the transition earlier, so under
gradient flow the derivative overshoots. The equilibrium derivative the
claim uses gives a step; the gradient-flow derivative gives a peak. The
peak's height depends on the start (1.633 at g₀ = 10⁻², 2.670 at 10⁻⁴).
The paper's Bayesian account puts its peak elsewhere again, in a
between-phase term "maximized when the posterior mass is evenly split"
(§2.3).

**Is the evidence about the same process?** Partly. The paper's
predictions are derived for a Bayesian posterior and it names the link
to SGD as its "primary theoretical gap" (§5); the claim is about
gradient dynamics of a regularized loss.

## Verdict

Rejected as a ground. [LIT-3001](../literature.d/LIT-3001.md) is removed from [CLAIM-828](../claims.d/CLAIM-828.md)'s `grounds`, and
the claim's influence paragraph is revised in place to say that the
equilibrium derivative steps and the gradient-flow derivative peaks.
