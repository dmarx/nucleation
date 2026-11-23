---
status: Proposed
title: 'On binary three-cycle models with the support of the PR prism, the signalling-corrected sheaf test reduces to a threshold on the signalling fraction and is sufficient only, Contextuality-by-Default 2.0 reduces to a threshold on direct influence, every model the first calls contextual the second does too, and the 36,861,830 models of the BERT anaphora study on which they differ are all CbD-contextual and not sheaf-contextual'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A model with the PR-prism support whose contextual fraction is not 1,
  whose signalling fraction is not max|ε_i|, or whose CbD 2.0 verdict is
  not Δ < 2. Or a model with that support that passes CF > 2|M|·SF and is
  not CbD-contextual. Or a correction to the counts the study published,
  showing the sheaf-contextual instances are not 77,118 or the
  CbD-contextual ones not 36,938,948. A different verdict on another
  support does not count.
tags:
- contextuality
- probabilistic-modeling
- linguistics
date: '2026-11-23'
line:
- formal-apparatus
- pragmatic-transport
grounds:
- CASE-tmpskejj
- THEORY-623
- THEORY-722
complements:
- CLAIM-374
summary: >-
  Filed from the run of [LEAD-191](../leads.d/LEAD-191.md) on 2026-11-23. On [LIT-844](../literature.d/LIT-844.md)'s support, CF is
  1 for every model. So the corrected sheaf test CF > 2|M|·SF is the
  threshold SF < 1/6, and CbD 2.0 is the threshold Δ < 2. Because
  Δ ≤ 6·SF, the first set lies inside the second. With the published
  counts, the two verdicts differ on exactly 36,861,830 instances. Reading
  the sheaf route as "the no-signalling part is contextual" makes it
  SF < 1, which calls at least as many contextual as CbD. The test [LIT-844](../literature.d/LIT-844.md)
  applies is therefore sufficient, not necessary, for that reading. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-037 — Proposed; the claim whose promotion condition this result was derived for, cited as under test -->
<!-- inactive-ok-file: CASE-tmpskejj CLAIM-tmprfjkk CLAIM-tmprq0nb CLAIM-tmpzvz98 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-tmptzmky: On binary three-cycle models with the support of the PR prism, the signalling-corrected sheaf test reduces to a threshold on the signalling fraction and is sufficient only, Contextuality-by-Default 2.0 reduces to a threshold on direct influence, every model the first calls contextual the second does too, and the 36,861,830 models of the BERT anaphora study on which they differ are all CbD-contextual and not sheaf-contextual

## The claim

Take the binary 3-cycle: contexts {X1, X2}, {X2, X3}, {X3, X1}. A
PR-like model has the support of the PR prism. It is perfectly correlated
on two contexts and anticorrelated on the third, with weights given by
ε = (ε1, ε2, ε3) ∈ [−1, 1]³. Every instance of [LIT-844](../literature.d/LIT-844.md)'s anaphora schema
is such a model, with ε_i = 2P_i(O1) − 1. On these models:

1. **The sheaf test is a signalling threshold.** No global assignment fits
   the support, so the contextual fraction is 1, signalling or not. This
   holds even for the deterministic, fully signalling model ε = (1, 1, 1).
   The only no-signalling model below any PR-like model is a multiple of
   the PR box, so SF = max|ε_i| ([LIT-844](../literature.d/LIT-844.md), Propositions 3.3 and 3.4).
   [LIT-844](../literature.d/LIT-844.md)'s corrected criterion CF > 2|M|·SF therefore holds iff
   max|ε_i| < 1/6. CF carries no information here.
2. **CbD 2.0 is a direct-influence threshold.** Each content lies in two
   contexts and is binary, so CbD 2.0's multimaximal coupling of a
   connection is its maximal coupling, and CbD 2.0 agrees with CbD 1.0
   ([THEORY-722](../theory.d/THEORY-722.md)). The cyclic criterion has s_odd = 3, giving CNT1 = 2 − Δ.
   So the model is CbD-contextual iff Δ < 2, with
   Δ = |ε1 − ε2| + |ε2 − ε3| + |ε3 + ε1|.
3. **The sheaf set lies inside the CbD set.** Each term of Δ is at most
   2·max|ε_i|, so Δ ≤ 6·SF. Then SF < 1/6 gives Δ < 1 < 2. The converse
   fails: ε = (p, p, p) has Δ = 2p, so it is CbD-contextual and not
   sheaf-contextual for every 1/6 ≤ p < 1.
4. **The divergence on the study's data.** [LIT-844](../literature.d/LIT-844.md) reports 77,118
   sheaf-contextual and 36,938,948 CbD-contextual instances of
   51,966,480 (§6b). By 3, the instances on which the verdicts differ are
   exactly the difference, 36,861,830 (70.9%). All are CbD-contextual and
   not sheaf-contextual.
5. **Read exactly, the sheaf route says contextual iff SF < 1.** Read
   "contextual once signalling is allowed" as "the no-signalling part of
   a minimal-signalling decomposition ([LIT-844](../literature.d/LIT-844.md)'s eq. 3.3) is contextual".
   That part is the PR box whenever it has positive weight, and the PR box
   is strongly contextual. So the reading says contextual iff SF < 1.
   Δ ≥ 2·SF, so every CbD-contextual instance has SF < 1, and this reading
   calls at least 36,938,948 instances contextual. On this reading the
   test [LIT-844](../literature.d/LIT-844.md) applies is sufficient and far from necessary.

## Proof and check

Items 1, 2, 3 and 5 are proved above. Item 4 is arithmetic on the
published counts given item 3. [CASE-tmpskejj](../cases.d/CASE-tmpskejj.md) checks each by linear
programming, on 120 random models and the uniform family, in 249 passing
tests (`scratch/studies/lead-191/`). The programs are:

- CF and SF by the decompositions (3.1) and (3.3);
- CbD 2.0 as the feasibility of a coupling of the six variables with
  maximally coupled connections;
- the no-signalling part's contextuality as the infeasibility of a
  noncontextual part of weight 1 − SF.

## What it does not say

- **That either verdict is right about BERT or about language.** Which
  verdict is right is the question [CLAIM-tmprfjkk](CLAIM-tmprfjkk.md), [CLAIM-tmprq0nb](CLAIM-tmprq0nb.md) and
  [CLAIM-tmpzvz98](CLAIM-tmpzvz98.md) answer differently.
- **That Vallée et al.'s criterion is sufficient only in general.** That
  paper was not read. Item 5 shows only that on this support the test, as
  [LIT-844](../literature.d/LIT-844.md) states it, is not necessary for one natural sheaf-side reading.
  A reading by distance to the nearest no-signalling model is computed in
  [CASE-tmpskejj](../cases.d/CASE-tmpskejj.md) and gives yet other verdicts. It is not claimed here.
- **Anything about instances beyond the 25 printed in [LIT-844](../literature.d/LIT-844.md).** The
  per-instance probabilities are not published.

## Bearing

This is the comparison [CLAIM-037](CLAIM-037.md)'s note of 2026-10-29 names. It does not
by itself settle that claim's "needs": the alternatives say what it does.
It extends [CLAIM-374](CLAIM-374.md)'s agreement result to the signalling side. On
consistently connected systems the two routes agree. On this signalling
family, the test [LIT-844](../literature.d/LIT-844.md) applies disagrees with CbD wherever SF ≥ 1/6 and
Δ < 2. The reading of item 5 disagrees with it in the other direction,
wherever SF < 1 and Δ ≥ 2.
