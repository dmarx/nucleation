---
status: Proposed
title: 'Under cosine similarity with unit-norm vectors, Gromov–Wasserstein with squared loss is transport under one global linear map of fixed Frobenius norm, of which orthogonal maps are a subclass, so a Gromov–Wasserstein fit that beats an orthogonal map on held-out items does not by itself show that the right correspondence is lossy or not invertible'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in THEORY-1135's Lemma 4.3 identity (GW cost with cosine
  similarity and squared loss equals a marginal-fixed constant minus
  2‖XΓYᵀ‖_F² for unit-norm columns), or a case in which, with those
  conditions met, a GW plan beats orthogonal Procrustes and the
  advantage cannot be attributed either to the wider class of global
  linear maps or to a non-deterministic coupling.
tags:
- mathematics
- representation-learning
date: '2026-11-14'
line:
- pragmatic-transport
grounds:
- THEORY-1135
summary: >-
  Raised by the reading review of 2026-11-14 (by topic, part A,
  mathematics). CASE-185's correspondence arm fits orthogonal
  Procrustes, unrestricted linear maps, GW, fused GW and co-optimal
  transport, and reads "anchored fused GW or co-optimal transport
  beating orthogonal maps on held-out items" as "evidence that the right
  transports are lossy and not invertible, as CLAIM-098 holds".
  THEORY-1135, a reading in force no line used, shows that under its
  conditions GW is itself the problem of one global linear map on a
  Frobenius sphere, a class that contains the orthogonal maps. The
  wording is the assistant's; adopting it is the owner's call.
---

# CLAIM-tmp6u7m2: Under cosine similarity with unit-norm vectors, Gromov–Wasserstein with squared loss is transport under one global linear map of fixed Frobenius norm, of which orthogonal maps are a subclass, so a Gromov–Wasserstein fit that beats an orthogonal map on held-out items does not by itself show that the right correspondence is lossy or not invertible

## The claim

THEORY-1135 (Lemmas 4.1–4.3, proved and checked numerically): for point
sets X, Y with unit-norm columns, minimising Gromov–Wasserstein with
cosine similarity C^x = XᵀX, C^y = YᵀY and squared loss is the same as
maximising ‖XΓYᵀ‖_F over couplings Γ, and that is optimal transport
under one unknown linear map P with ‖P‖_F fixed, when the target is
whitened. Orthogonal maps (p = ∞) give the nuclear norm instead
(Procrustes). Both are global: "One P acts on every point."

So in a comparison like CASE-185's, a GW fit and an orthogonal fit differ
in two ways at once: the class of global linear maps (Frobenius sphere
against O(d)) and whether the coupling is estimated or given. A GW fit
that beats an orthogonal map on held-out items can win by either. It
shows that the correspondence is not orthogonal, or that the pairing was
better left to the coupling; it does not by itself show that the right
transport is lossy (many-to-one) or not invertible. That needs a
readout of the plan itself, for instance its entropy or how far it is
from a permutation, set beside an unrestricted linear map fitted on the
same items.

## What it does not say

- That GW is a global linear transport in general. The equivalence needs
  unit norms (Lemma 4.3) and, for the link to the original transport
  problem, a whitened target (Lemma 4.1); real response embeddings meet
  neither without preprocessing (THEORY-1135's own "What this does not
  say").
- Much about fused GW or co-optimal transport, which CASE-185's outcome
  names; the lemma is for plain GW. Fused GW tends to plain GW as its
  weight on structure goes to 1 (THEORY-1156), so the caution reaches
  fused GW fitted with most of its weight on structure, and the arm's
  plain GW fit, and no further.
- That CLAIM-098 is wrong. Only that this outcome of CASE-185 would not
  be evidence for it without a further readout.
