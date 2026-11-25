---
number: 1927
status: Proposed
formerly:
- THEORY-tmpcqstf
title: 'Predictive policing learns where it looked'
statement: >-
  Ensign, Friedler, Neville, Scheidegger and Venkatasubramanian prove that,
  in an urn model of predictive policing that learns only from incidents its
  own patrols discover, deployment converges on whichever region started
  ahead when crime rates are equal and on the higher-rate region however
  slight the difference when they are not, so the system learns where it
  looked rather than where crime is, and that discarding discovered
  incidents in proportion to patrol probability restores convergence to the
  true rates
version: 2
history:
- version: 2
  date: '2026-11-18'
  note: >-
    Reconciled on 2026-11-18 with THEORY-tmp0xl3k, the account the
    continuation of the exchange's readings filed from its second
    reading of the same work (NOTE-2025). It stated the same account and
    was never merged, so it was folded in here and removed. Relations
    carried over: corroborates CLAIM-342. Its title was: "In a Pólya-urn
    model of predictive policing, Ensign and colleagues show that
    allocating patrols by incidents discovered on patrol does not learn
    true crime rates: with equal rates the prior persists and with
    unequal rates the higher-rate region takes all, reported incidents
    only attenuate the loop, and dropping discovered incidents with the
    probability of patrol removes it"
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
- CLAIM-342
---
<!-- unresolved-ok-file: THEORY-tmp0xl3k — removed at the reconciliation of 2026-11-18; named for provenance -->

# THEORY-1927: Predictive policing learns where it looked

## Source

[LIT-2688](../literature.d/LIT-2688.md), read in arXiv 1706.09847v3, the extended version of the FAT* 2018 paper (PMLR 81).

## What was actually shown

Proofs in a generalized Pólya urn with one officer and two regions: with equal rates the limiting share is a Beta draw fixed by the initial counts (Lemma 2); with unequal rates it is 1 for the higher-rate region (Lemma 4), so 10% against 11% "will settle on region B with probability 1". Reported incidents attenuate the bias only when discovered ones are down-weighted or the rates are close (§3.4.1). Dropping each discovered incident with probability equal to the patrol probability, "a rejection-sampling variant of Thompson-Horvitz estimation" (§3.5), restores convergence. Simulations of the urn and of PredPol on Lum and Isaac's Oakland data reproduce the runaway and the repair (Figs 1–2).

## What this does not say

- Nothing about behaviour: policing does not change crime in the model, which assumes patrols discover crime at its true rate (Assumption 3.3). The loop corrupts the evidence, not the people.
- That the remedy works in practice: the authors say that with skewed reporting "the solutions might not continue to work".
- Anything about blame, accountability or the distribution of responsibility.

## From the second reading (2026-11-17)

The second reading adds a relation: it corroborates [CLAIM-342](../claims.d/CLAIM-342.md), which does
not rest on it. A loop that selects its own evidence locks in (Lemma 4),
and independent evidence mixed with it only attenuates the loop: reported
incidents "can attenuate the degree of runaway feedback" but "cannot
entirely remove it" (abstract). The repair reweights the self-selected
stream by the probability of selection. One limit:

- **That the loop creates crime.** It amplifies a real difference or
  freezes the prior.
