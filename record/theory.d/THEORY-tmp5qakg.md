---
status: Proposed
promote_when: >-
  The same profile, cluster size peaking at intermediate strength and
  narrowing at both ends, found in empirical games built by a sampler not
  tuned along the transitive axis, for instance learning agents or uniform
  draws from a restricted policy class, in games other than these eight,
  and robust to the choice of equilibrium (minimum- as well as
  maximum-entropy Nash). It is refuted if a sampler with comparable
  coverage gives clusters that keep growing with strength in these same
  games, as they do in Blotto. Theorems about long cycles among weak
  strategies do not bear on it.
title: 'Real-world games of skill have a spinning-top geometry: their non-transitive part, measured as Nash cluster size, is largest at intermediate strength and narrows toward the strongest and the weakest strategies'
version: 1
tags:
- game-theory
- learning-theory
date: '2026-10-30'
source:
- LIT-1504
extends:
- THEORY-930
summary: >-
  Czarnecki et al.'s hypothesis (LIT-1504, read in NOTE-1146), filed
  beside THEORY-930 when the status review of 2026-10-30 narrowed and
  promoted that entry under ADR-065 (ADR-047 kind 1). The paper's body
  says it does not prove that real games have this geometry; its evidence
  is THEORY-930's sampled profiles, whose shape the sampler and the
  maximum-entropy equilibrium help set.
---

# THEORY-tmp5qakg: Real-world games of skill have a spinning-top geometry: their non-transitive part, measured as Nash cluster size, is largest at intermediate strength and narrows toward the strongest and the weakest strategies

## Source

Czarnecki, Gidel, Tracey, Tuyls, Omidshafiei, Balduzzi & Jaderberg (2020),
LIT-1504, read in full in NOTE-1146 from arXiv:2004.09468v2.

## The thesis

Games people play for skill have a transitive axis, from weak to strong,
and a non-transitive part that is thickest at middling strength and thin
at both ends: a spinning top. The abstract says "We prove the existence of
this geometry"; the body withdraws it: "Naturally, the above does not
prove that real world games follow the Games of Skill geometry" (p. 6).

## What the evidence is

THEORY-930: about a thousand sampled search agents in each of eight small
OpenSpiel board games, and the AlphaStar league, with clusters taken from
maximum-entropy Nash and a skew-normal curve fitted by eye. The authors say
their sampler "does not guarantee uniform sampling of strategies" (p. 9),
that the AlphaStar profile reflects "AlphaStar induced game geometry"
(p. 18), and that minimum-entropy equilibria would give "more peaky tops"
(p. 17).

## What this does not say

- **Anything from the theorems.** Theorem 1 (THEORY-926) shows long cycles
  among strategies that can signal, not narrowing at the top.
- **That every game has the shape.** Blotto, Kuhn poker and the noisy Elo
  games do not.
