---
number: 1927
status: Proposed
formerly:
- THEORY-tmpcqstf
title: 'Ensign, Friedler, Neville, Scheidegger and Venkatasubramanian prove that, in an urn model of predictive policing that learns only from incidents its own patrols discover, deployment converges on whichever region started ahead when crime rates are equal and on the higher-rate region however slight the difference when they are not, so the system learns where it looked rather than where crime is, and that discarding discovered incidents in proportion to patrol probability restores convergence to the true rates'
version: 1
tags:
- society-and-governance
- philosophy-of-technology
- anthology-candidate
promote_when: >-
  a check of the paper's proofs (Lemmas 2 to 4 and the reported-incident
  analysis of §3.4) confirms that in the stated model deployment converges
  to a draw from the initial counts under equal rates and to the
  higher-rate region under unequal rates, and that the rejection-sampling
  filter of §3.5 yields convergence to the true rate ratio
source:
- LIT-2688
corroborates:
- CLAIM-277
- CLAIM-406
---

# THEORY-1927: Ensign, Friedler, Neville, Scheidegger and Venkatasubramanian prove that, in an urn model of predictive policing that learns only from incidents its own patrols discover, deployment converges on whichever region started ahead when crime rates are equal and on the higher-rate region however slight the difference when they are not, so the system learns where it looked rather than where crime is, and that discarding discovered incidents in proportion to patrol probability restores convergence to the true rates

## Source

[LIT-2688](../literature.d/LIT-2688.md), read in arXiv 1706.09847v3, the extended version of the FAT* 2018 paper (PMLR 81).

## What was actually shown

Proofs in a generalized Pólya urn with one officer and two regions: with equal rates the limiting share is a Beta draw fixed by the initial counts (Lemma 2); with unequal rates it is 1 for the higher-rate region (Lemma 4), so 10% against 11% "will settle on region B with probability 1". Reported incidents attenuate the bias only when discovered ones are down-weighted or the rates are close (§3.4.1). Dropping each discovered incident with probability equal to the patrol probability, "a rejection-sampling variant of Thompson-Horvitz estimation" (§3.5), restores convergence. Simulations of the urn and of PredPol on Lum and Isaac's Oakland data reproduce the runaway and the repair (Figs 1–2).

## What this does not say

- Nothing about behaviour: policing does not change crime in the model, which assumes patrols discover crime at its true rate (Assumption 3.3). The loop corrupts the evidence, not the people.
- That the remedy works in practice: the authors say that with skewed reporting "the solutions might not continue to work".
- Anything about blame, accountability or the distribution of responsibility.
