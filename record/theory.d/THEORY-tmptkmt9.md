---
status: Active
title: 'When the expression maps of a discourse sheaf diffuse to reduce disagreement, with opinions held fixed they converge to the nearest sheaf, in Frobenius distance, of which the opinions are a global section, so apparent consensus is reached by changing what is said ("learning to lie"); with opinions diffusing too the joint flow is gradient descent on ½‖δx‖², and conserved diagonal blocks of αδᵀδ − βxxᵀ keep the opinions from collapsing to zero; nothing in either flow checks an expression against the opinion it expresses'
version: 1
tags:
- network-science
- mathematics
- society-and-governance
date: '2026-10-27'
source:
- LIT-tmpf2wmd
summary: >-
  Hansen and Ghrist (2020; SIAM J. Appl. Math. 2021), [LIT-tmpf2wmd](../literature.d/LIT-tmpf2wmd.md), §§8–9,
  read in [NOTE-tmpe4zh5](../notes.d/NOTE-tmpe4zh5.md) from the arXiv preprint. Active as mathematics:
  Theorems 8.1, 9.3 and 9.4 and Lemma 9.1. Theorem 9.3's proof is right
  only for α = β as printed; with the α, β weights it holds generally,
  which was checked numerically in the reading. The degeneracy guards are
  internal to the loop: minimal change and a conserved quantity, not
  evidence from outside it.
---
<!-- inactive-ok-file: CLAIM-342 QUESTION-tmpubsi9 — Proposed or Open; the loop claim and the question this is a case for, cited as open -->

# THEORY-tmptkmt9: When the expression maps of a discourse sheaf diffuse to reduce disagreement, with opinions held fixed they converge to the nearest sheaf, in Frobenius distance, of which the opinions are a global section, so apparent consensus is reached by changing what is said ("learning to lie"); with opinions diffusing too the joint flow is gradient descent on ½‖δx‖², and conserved diagonal blocks of αδᵀδ − βxxᵀ keep the opinions from collapsing to zero; nothing in either flow checks an expression against the opinion it expresses

## Source

Hansen and Ghrist (2020; SIAM J. Appl. Math. 81(5), 2021), [LIT-tmpf2wmd](../literature.d/LIT-tmpf2wmd.md),
§§8–9 (pp. 13–17 of arXiv 2005.12798v1); read in [NOTE-tmpe4zh5](../notes.d/NOTE-tmpe4zh5.md). The
setting is [THEORY-tmp8ypuh](THEORY-tmp8ypuh.md)'s.

## What was actually shown

**Expression diffusion, opinions fixed (§8).** Each agent sees its
neighbours' expressions and changes only its own maps, by
dF_{v⊴e}/dt = −β(F_{v⊴e}x_v − F_{u⊴e}x_u)x_vᵀ (eq. 8.1), so as to "remove
the part of the image that contributes to disagreement with neighbors"
(p. 13). **Theorem 8.1:** F(t) converges to "the nearest sheaf such that x
is a global section", in the distance ‖δ − δ′‖²_F (eq. 8.4). Each edge's
flow is a linear positive-semidefinite flow, which projects δ_e onto
{δ_e : δ_e x_e = 0}. In Example 8.2 (Fig. 6), the constant sheaf on one
edge with opinions −4 and +1, one map changes sign. That agent "learns to
lie about their opinion", flipping its sign and downplaying its magnitude.
The reading computes the limit as −3/17 and 12/17, where the figure labels
−0.2 and 0.8.

**Joint diffusion (§9).** With dx/dt = −αδᵀδx as well (eq. 9.1), the flow
is gradient descent on Ψ = ½‖δx‖² (Lemma 9.1, p. 15). Trajectories converge
to a sheaf together with a global section of it, and smooth equilibria are
Lyapunov stable (Theorem 9.2). There is "no global asymptotic stability"
because the equilibria are not isolated.

**The trivial solution, named and excluded for x.** Most of the equilibrium
variety has ker δ = 0, "This would seem to indicate that we should expect
most trajectories to converge to points with x = 0. However, this is not
the case" (p. 16). **Theorem 9.3:** the diagonal blocks of αδᵀδ − βxxᵀ are
constant in time, so if one is indefinite at the start, x does not go to
zero. Hence some rescaling κx₀ of any start converges to a sheaf with a
nonzero section. The printed proof writes M = δᵀδ − xxᵀ and
tr(M) = ‖δ‖²_F − ‖x‖², which are correct only for α = β. The reading's
numerical check with α = 2, β = 0.5 found the weighted blocks conserved
and the unweighted ones not. **Theorem 9.4:** ‖δ‖²_F, ‖x‖², ‖δx‖² and the
Rayleigh quotient ‖δx‖²/‖x‖² are nonincreasing, so x "becomes a global
section of F(t) at least as quickly as it approaches zero" (p. 17).

**What drives the flows.** Both flows depend on the state only through the
edge disagreement δx (eqs. 8.1–8.3, 9.1). Neither has a term relating an
expression F_{v⊴e}x_v to the opinion x_v it expresses, to the agent's
initial maps, or to anything outside the network. This is a property of
the equations as written. Example 9.5: when opinions are far apart, "the
sheaf is able to adapt more easily than the opinions themselves" (p. 17),
and an agent again ends up lying.

## What this does not say

- **That the learned maps cannot collapse.** Theorem 9.3 bounds x away from
  zero, not δ. ‖δ‖_F only decreases (Theorem 9.4). In §8 the
  nearest-sheaf property keeps each change minimal, a rank-one change
  along x_v at each vertex, which is not a bar to zero maps. (The reading
  derives, beyond the paper, that a vertex's maps cannot all vanish when
  its weighted block starts with a positive eigenvalue.)
- **That the guards are evidence.** Minimal change and a conserved quantity
  keep the outcome non-degenerate. They do not make the agreement reached
  any more faithful to the opinions held. The consensus is coherence by
  construction.
- **That people learn to communicate this way,** or that "lying" here is
  more than a sign change in a linear map. The authors set the
  sociological question aside (p. 13).
- **Which equilibrium is selected.** The equilibria form a singular
  variety, and the paper characterizes stability only at its smooth
  points.
- **Anything about the knowledge-sheaf case directly.** The zero section
  is common to both ([THEORY-299](THEORY-299.md)), but there the maps are trained against
  negatives, and here there are none.
