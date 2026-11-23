---
status: Proposed
title: 'Operators rewarded for realized policy under a weighted-mean decision delegate, within their own side, to its most extreme members and not its nearest, because a grant''s marginal value to the granter is proportional to how far the grantee''s policy lies from the decision'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the gradient below, or a rerun of the study's code
  (scratch/studies/lead-190/) in which bound operators' grants within
  their own side correlate with nearness to their own policy more than
  with distance of the grantee's policy from the decision. A decision rule
  other than the weighted mean does not count: the claim is about that
  rule.
tags:
- self-governance
- game-theory
date: '2026-11-23'
line:
- distributed-agency
rests_on:
- CLAIM-375
grounds:
- CASE-tmpw3vii
complements:
- CLAIM-tmpdpnid
bears_on:
- QUESTION-090
summary: >-
  Under CLAIM-375's one-hop rule and weighted-mean decision, the marginal
  value to operator i of raising its grant to j is
  2(p_i − p*)·ηb_i(p_j − p*)/S. It is positive for every j on i's side
  of the decision and largest for the j whose policy is farthest from
  the decision, whatever i's own position. In CASE-tmpw3vii's game, bound
  operators' grants within their side correlated 0.88 to 0.92 with the
  grantee's extremity and 0.07 to 0.22 with its nearness. So "aligned"
  in CLAIM-285 holds in CLAIM-375's sense, on one's side of the
  decision, and not in the sense of nearest in policy. Two readings are
  set out for the owner. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpw3vii CLAIM-tmpdpnid — new; filed by the lead run of 2026-11-23 -->
<!-- inactive-ok-file: CLAIM-285 — Proposed; the claim whose word is read, cited as open -->

# CLAIM-tmpoc6mo: Operators rewarded for realized policy under a weighted-mean decision delegate, within their own side, to its most extreme members and not its nearest, because a grant's marginal value to the granter is proportional to how far the grantee's policy lies from the decision

## The claim

Under CLAIM-375's one-hop rule, as the study builds it with baselines (1 − η)b_j and grants scaled by η, the authority is g_j = (1 − η)b_j + ηΣ_k b_k E_kj, the decision is p* = Σ_j g_j p_j/S with S = Σ_j g_j, and the objective is J_i = −(p* − p_i)² − Cost(E_i). Then

∂J_i/∂E_ij = 2(p_i − p*)·ηb_i(p_j − p*)/S − ∂Cost/∂E_ij.

The first factor is fixed for i. The marginal value of a grant to j is therefore proportional to p_j − p*, the distance of j's policy from the decision on i's side. It is not proportional to −|p_j − p_i|, j's nearness to i. A test checks the sign of the gradient against this for every pair. Among allies on its side, an operator gains most by granting to the one farthest from the decision, even when that ally is farther from the operator than the decision is. CLAIM-375's condition, ‖p_j − p_i‖ < ‖p* − p_i‖, is enough for a positive gradient. It is not what sets the ranking.

In CASE-tmpw3vii's game on 30 populations, bound operators' grants within their side correlated with the grantee's extremity at 0.88 under one-hop, 0.90 under leave-one-out and 0.92 at N = 40. Their correlation with nearness was 0.07, 0.22 and 0.02. With linear cost, which concentrates grants on the best, the figures were 0.45 to 0.60 for extremity and −0.07 to −0.11 for nearness.

## Two readings of "aligned others" in CLAIM-285, for the owner

- **Reading A (the assistant's lean): aligned means on one's own side of the decision.** This is CLAIM-375's sense, an ally whose policy moves the decision toward one's own. On it CLAIM-285's "operators delegate to aligned others" holds in this model without qualification: 100% of grants went to one's own side (CLAIM-tmpdpnid). This claim adds that the allies chosen are the side's extremes.
- **Reading B: aligned means nearest in policy.** The owner's U2 says "identify other agents with aligned policies", and A2's "a better-placed ally" can be read this way. On it CLAIM-285's incentive picks the wrong allies. Grants go to whoever pulls the decision hardest, not to whoever agrees most, and CLAIM-285 would need a narrower decision rule or a cost on distance to hold.

## What it does not say

- That authority concentrates on extremists in every population. In these balanced populations both sides do the same and the decision stays near the centre. In an unbalanced one the same gradient would pull it toward the larger side's extremes. That was not run.
- Anything about decision rules other than the weighted mean, such as a median or a vote.
