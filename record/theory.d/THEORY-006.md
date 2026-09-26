---
number: 6
status: Proposed
formerly:
- THEORY-tmpl293u
promote_when: >-
  A close reading of Poole et al. confirming the §2.3 proof (Eqs. 8–10) and
  its assumption that negatives are drawn independently from the marginal. The
  bound is proved in the source; this record has so far only skimmed it.
title: 'InfoNCE is a lower bound on mutual information for every critic and can never exceed the log of the batch size'
version: 1
tags:
- information-theory
- representation-learning
date: '2026-09-26'
source:
- LIT-246
- LIT-247
- LIT-256
- LIT-226
summary: >-
  Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3, Eqs. 8–10 — an exact proof (CPC's
  own derivation, [ANTH-LIT-589](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-589.md), passes through an approximation). Tschannen et
  al. ([LIT-247](../literature.d/LIT-247.md)) show that tightening the bound does not explain what
  makes the representations good.
---
<!-- inactive-ok-file: LIT-247 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-256 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-246 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-006: InfoNCE is a lower bound on mutual information for every critic and can never exceed the log of the batch size

## Source

Poole et al. (2019), [LIT-246](../literature.d/LIT-246.md), §2.3, Eqs. 8–10. Supporting: Belghazi et al. (2018), [LIT-256](../literature.d/LIT-256.md), Eqs. 1, 3–4 and App. 8.2.1 (mutual information as E[log dP_XZ/d(P_X⊗P_Z)], and the Donsker–Varadhan bound tight exactly at the log Radon–Nikodym derivative plus a constant); Tschannen et al. (2020), [LIT-247](../literature.d/LIT-247.md); Fischer's conditional entropy bottleneck, [LIT-226](../literature.d/LIT-226.md), which relies on the bound (§6.3).

## What was actually shown

With K samples and negatives drawn independently from the marginal, I(X;Y) ≥ I_NCE for every critic, proved exactly as the multi-sample NWJ bound with the batch estimate of the partition function ([LIT-246](../literature.d/LIT-246.md) Eqs. 8–10). By construction I_NCE ≤ log K, and the optimal critic does not depend on K. Belghazi et al. state the underlying identity: mutual information is the expected log Radon–Nikodym derivative of the joint with respect to the product of marginals, and the variational bound is tight exactly at that log-derivative plus a constant.

Tschannen et al. show experimentally that representations can improve while the MI estimate does not, and that tighter bounds can give worse representations, so the bound's value is not what the objective's success tracks.

## What this does not say

- That I_NCE approaches I(X;Y) at any stated rate as K grows (not proved in what was read).
- That maximizing I_NCE maximizes the representation's information in a useful sense (Tschannen et al. argue against this reading).
- Anything for negatives drawn from other positive pairs in the same batch, which is what implementations do; Johnson et al. App. B.1 notes the difference.
