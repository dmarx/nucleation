---
number: 916
status: Proposed
formerly:
- THEORY-tmphmdtd
promote_when: >-
  Two things. First, the proofs checked by a reader of this record (or a
  published independent proof or extension that restates Theorem 4.1 and
  Proposition 4.2), since this reading skimmed them. Second, because the
  record would lean on the model as a description of groups, a test in
  groups with a stable network of relative influence, measured
  independently of the members' self-weights, showing that their influence
  over outcomes across a sequence of issues orders as the network's
  eigenvector centralities and concentrates above them. It is refuted as a
  description if power in such groups orders otherwise, and the theorems
  are refuted only by an error in the proofs. Simulations of the model
  cannot settle the second part.
title: "In the DeGroot–Friedkin model, where a group reaches DeGroot consensus on each issue and each member's self-weight on the next issue equals their control over the last, with fixed relative interpersonal weights, self-weights converge from every non-autocratic start to one equilibrium ordered by the eigenvector centralities of those weights: power accumulates above a centrality threshold, is autocratic exactly when the network is a star and democratic exactly when it is doubly stochastic, and members whom no path of influence reaches end with none"
version: 1
tags:
- network-science
- social-science
- mathematics
date: '2026-10-24'
source:
- LIT-1146
summary: >-
  Jia, MirTabatabaei, Friedkin & Bullo (2015), [LIT-1146](../literature.d/LIT-1146.md), read in
  [NOTE-1135](../notes.d/NOTE-1135.md) from the version of record posted on the author's site;
  proofs skimmed. Theorems about a model, not findings about groups. The
  empirical companion, [LIT-1482](../literature.d/LIT-1482.md) ([THEORY-902](THEORY-902.md)), uses anchored
  dynamics and a changing network, whose attractor is autocracy rather
  than this interior equilibrium.
supports:
- CLAIM-448
---
<!-- inactive-ok-file: CLAIM-448 THEORY-902 THEORY-321 LIT-1482 — Proposed or Deferred; the claim, accounts and companion work this bears on, named, nothing here rests on them -->

# THEORY-916: In the DeGroot–Friedkin model, where a group reaches DeGroot consensus on each issue and each member's self-weight on the next issue equals their control over the last, with fixed relative interpersonal weights, self-weights converge from every non-autocratic start to one equilibrium ordered by the eigenvector centralities of those weights: power accumulates above a centrality threshold, is autocratic exactly when the network is a star and democratic exactly when it is doubly stochastic, and members whom no path of influence reaches end with none

## Source

Jia, MirTabatabaei, Friedkin & Bullo, [LIT-1146](../literature.d/LIT-1146.md), read in [NOTE-1135](../notes.d/NOTE-1135.md):
Lemmas 2.2–3.2, Theorem 4.1, Proposition 4.2 and Section 5 (pp. 376–385),
with proofs in Appendices B–G, skimmed.

## What was actually shown

A proof, not an experiment. The model: on each issue, opinions follow
DeGroot averaging with W(x) = diag(x) + (I − diag(x))C and reach
consensus; then x(s+1) = w(x(s)), the dominant left eigenvector of W.

- **The only parameter is c,** the eigenvector centrality of C (Lemma 2.2).
- **Interior equilibrium.** Unless C is a star, every non-autocratic start
  converges to one x*, ordered as c (Theorem 4.1).
- **Accumulation.** Above a threshold power exceeds centrality; below it,
  falls short (Proposition 4.2). "social power tends to accumulate at the
  top of the hierarchy" (p. 367).
- **The extremes.** A star converges to autocracy; a doubly stochastic C to
  equal power, and only then (Lemmas 3.1, 3.2).
- **The unreached.** With a reducible C, members not globally reachable
  end with zero power (Section 5); in Krackhardt's advice network, the four
  managers nobody consults.

## What this does not say

- **That groups behave this way.** The authors: "an assessment of the
  validity of the model has just begun" (p. 386).
- **That it is robust.** Anchored dynamics differ, and "At the present
  time, we cannot assert robustness" (p. 386).
- **That authority is chosen or maintained.** C is fixed and exogenous;
  nobody decides who is heard.
- **That the equilibrium is autocratic in general.** Only for a star.
  Short of that, the most central member gains disproportionately but does
  not take everything.

## Connections

- **[CLAIM-448](../claims.d/CLAIM-448.md).** The baseline it names, now in exact form. Every
  issue ends in consensus, so the record is always coherent; its content
  is weighted toward the central, and the unreached contribute nothing.
  That is a proved instance of coherence without integration, produced by
  uptake rather than by a regime of admission.
- **[THEORY-902](THEORY-902.md).** The experiment on the same mechanism under anchored
  dynamics.
- **[THEORY-321](THEORY-321.md).** Golub & Jackson's DeGroot result: a consensus is right
  in large societies only if no member's influence weight stays large.
  Under reflected appraisal the most central member's weight grows, which
  is the condition [THEORY-321](THEORY-321.md) says defeats the wisdom of crowds. That
  combination is the record's, not the paper's.
