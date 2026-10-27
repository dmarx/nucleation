---
number: 1062
status: Active
formerly:
- THEORY-tmp8ypuh
title: 'On a discourse sheaf, where each agent expresses a private opinion through a linear map into each edge''s space of topics, sheaf-Laplacian opinion diffusion converges to the orthogonal projection of the initial opinions onto the global sections, which are agreement in what each pair expresses and not in what they hold; stable polarized or incomparable private opinions are therefore possible, and when the sheaf has no nonzero global section the only limit is all opinions zero'
version: 1
tags:
- network-science
- mathematics
- society-and-governance
date: '2026-10-27'
source:
- LIT-1646
summary: >-
  Hansen and Ghrist (2020; SIAM J. Appl. Math. 2021), [LIT-1646](../literature.d/LIT-1646.md), §§2–4,
  read in [NOTE-1222](../notes.d/NOTE-1222.md) from the arXiv preprint. Active as mathematics: the
  convergence is a theorem about a linear heat equation, and the gap
  between expressed and held opinion is in the definitions and is worked in
  an example. It does not say that people reach agreement this way, or
  that an agreement in expression shows anything about what is held.
---
<!-- inactive-ok-file: CLAIM-471 — Proposed; the gluing claim this is a formal case of, cited as open -->

# THEORY-1062: On a discourse sheaf, where each agent expresses a private opinion through a linear map into each edge's space of topics, sheaf-Laplacian opinion diffusion converges to the orthogonal projection of the initial opinions onto the global sections, which are agreement in what each pair expresses and not in what they hold; stable polarized or incomparable private opinions are therefore possible, and when the sheaf has no nonzero global section the only limit is all opinions zero

## Source

Hansen and Ghrist (2020; SIAM J. Appl. Math. 81(5), 2021), [LIT-1646](../literature.d/LIT-1646.md),
§§2–4 (pp. 3–10 of arXiv 2005.12798v1); read in [NOTE-1222](../notes.d/NOTE-1222.md).

## What was actually shown

**The structure.** Each agent v has an opinion space F(v), and each edge e
has a discourse space F(e) whose basis topics "are not necessarily the same
as any of the basis topics" of either agent. The linear maps
F_{v⊴e}: F(v) → F(e) are expressions of opinion. The agents "have expressed
consensus when F_{u⊴e}(x_u) = F_{v⊴e}(x_v) … this does not imply that u and v
have the same opinions: it means that their expressions of personally held
opinions have the appearance of agreement" (§3, p. 7). Expression can be
selective, combining, scaled, or sign-reversed ("one can model agents who
lie"), and it can differ by edge (p. 8).

**The theorem.** With L_F = δᵀδ, solutions of dx/dt = −αL_F x converge, as
t → ∞, to the orthogonal projection of x(0) onto H⁰(G; F) = ker δ = ker L_F
(Theorem 4.1, p. 9). L_F is symmetric positive semidefinite, so the flow
is exp(−tαL_F), which tends to the projection onto its kernel. Convergence
is exponential. This could have come out otherwise only if L_F had
negative eigenvalues, which is what happens in §12's signed variant
(Proposition 12.1).

**The two consequences the paper draws.** "If this sheaf has no nontrivial
global sections, the only stable opinions will be everywhere zero: an
uninteresting solution" (p. 9). And on a sheaf with sign-reversed maps,
stable polarized distributions are global sections. In Example 4.2 (p. 9,
Fig. 4) two agents who dislike a politician "tell a polite lie to their
neighbors on the left but are frank with each other", and "any initial
opinion distribution will converge to one of these polarized
distributions". On the constant sheaf the same flow gives ordinary
consensus at the average.

## What this does not say

- **That an agreement in expression reveals the private opinions.** A
  global section fixes only the images F_{v⊴e}x_v. Agents "do not know the
  veracity of their neighbors' expressed opinions" (p. 9), and the model
  gives them no way to find out.
- **That people form opinions this way.** The paper has no data, and the
  authors say evolving opinions "is perhaps not how real people engage in
  discourse" (p. 8).
- **That the expression maps are given by anything in particular.** In
  §§3–7 they are fixed background. How they change is a separate dynamic,
  in [THEORY-1088](THEORY-1088.md).
- **That the limit is reached from any start to any section.** It is the
  projection of the starting opinions, so the starting point decides which
  section is reached. Steering to a chosen section is a control question,
  which §6 answers with relative cohomology.
- **Anything nonlinear.** The bounded-confidence and antagonistic variants
  (§§11–12) have more equilibria, or are unstable.
