---
status: Active
title: 'Transfer entropy measures directed predictive improvement, not information flow: as a conditional mutual information it is the source''s unique information about the target''s next value plus its synergy with the target''s past, so it can credit a source with a bit the source carries only jointly and read zero from sources that jointly fix the target, and conditioning on more series does not remove the synergy'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in either worked example below: a demonstration that in the
  first process the source's past alone carries information about the
  target's next value, or that in the second either pairwise transfer
  entropy is positive. Or a proof that, under the partial-information
  consistency equations, a conditional mutual information has no
  synergistic component. Which word to use for the synergistic part, or
  whether "flow" should be defined differently, does not bear on the
  decomposition; it bears only on the title's last clause.
tags:
- information-theory
- causality
date: '2026-10-17'
line:
- formal-apparatus
grounds:
- THEORY-tmpijy6i
- THEORY-tmpt4nh7
- THEORY-tmp22xor
- THEORY-tmp8ox3d
uses:
- TERM-tmpj9z04
- TERM-tmpq0ms2
complements:
- CLAIM-tmp6nu4a
summary: >-
  The record's position on whether transfer entropy measures information
  flow. James, Barnett and Crutchfield show it does not, if flow is
  information attributable to the source alone ([THEORY-tmpijy6i](../theory.d/THEORY-tmpijy6i.md)). Williams
  and Beer's decomposition shows why, for any partial information
  decomposition satisfying the consistency equations ([THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md)).
  Both papers' examples were recomputed exactly. This is a different
  failure from [CLAIM-tmp6nu4a](CLAIM-tmp6nu4a.md)'s, prediction against intervention. It leaves
  transfer entropy standing as a predictive quantity.
---

# CLAIM-tmpu9ivq: Transfer entropy measures directed predictive improvement, not information flow: as a conditional mutual information it is the source's unique information about the target's next value plus its synergy with the target's past, so it can credit a source with a bit the source carries only jointly and read zero from sources that jointly fix the target, and conditioning on more series does not remove the synergy

## The claim

Transfer entropy is I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}) ([TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md)), and for
Gaussian data it is half Granger causality ([TERM-tmpq0ms2](../terms.d/TERM-tmpq0ms2.md)), so what follows
holds of the Granger measure there too. By the
consistency equations of any partial information decomposition with the
two sources Y's past and X's past, a conditional mutual information is the
source's unique information plus the synergy of the two. The redundancy
drops out, and the synergy comes in (Williams and Beer, [THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md)).
Only the decomposition's two-term split is needed here, not their I_min
redundancy measure.

If "flow from Y to X" means information in X's next value attributable to
Y's past alone, as James, Barnett and Crutchfield define it
([THEORY-tmpijy6i](../theory.d/THEORY-tmpijy6i.md)), then flow is at most the unique part, and transfer
entropy overstates it by the synergy. Where several sources fix the target
jointly, each pairwise transfer entropy can be zero. Conditioning on the
other sources (causation entropy, complete transfer entropy) brings their
joint bit back, but credits it to each source in full, so it is counted
once per source.

## The two examples

Both recomputed exactly on 2026-10-17 (a scratchpad script with an I_min
PID; [NOTE-tmpt2aw8](../notes.d/NOTE-tmpt2aw8.md)).

1. **Overstating flow.** X_t i.i.d. uniform bits, Y_t = X_{t−1} ⊕ Y_{t−1}.
   T_{X→Y} = I(Y_t; X_{t−1} | Y_{t−1}) = 1 bit. But I(Y_t; X_{t−1}) = 0 and
   I(Y_t; Y_{t−1}) = 0: neither past alone says anything about Y_t. The
   co-information is −1, and the PID gives 0 redundant, 0 unique to each,
   1 synergistic. The whole bit is joint.
2. **Understating influence.** X, Y i.i.d. uniform, Z_t = X_{t−1} ⊕ Y_{t−1}.
   Both T_{X→Z} and T_{Y→Z} are 0, and every pairwise information is 0, yet
   Z is fixed by the two. The causation entropies, each conditioning on the
   other source, are 1 bit each, so the one bit is counted twice.

Lizier et al.'s rule 18 is the same structure in a cellular automaton
([THEORY-tmp22xor](../theory.d/THEORY-tmp22xor.md)): where the centre cell is 0 the update is L ⊕ R, apparent
transfer entropy from each neighbour is 0 and complete transfer entropy is
1 bit from each. That reading of their case is the record's; they read the
contrast as complex against chaotic dynamics.

The first process is Williams and Beer's coupled pair at d = 1, where they
call the bit "state-dependent transfer". The two papers agree on the
decomposition. They disagree only on whether that part is to be called
transfer.

## What it does not say

- **That transfer entropy is wrong as a predictive measure.** As
  predictive improvement it is exactly what [THEORY-641](../theory.d/THEORY-641.md) and
  [THEORY-tmp0xaeq](../theory.d/THEORY-tmp0xaeq.md) say: a likelihood-ratio limit, and twice Granger causality
  for Gaussian data.
- **That a nonzero transfer entropy shows no influence.** In example 1,
  intervening on X_{t−1} does change Y_t, so Ay and Polani's interventional
  flow credits X ([THEORY-tmpkovi2](../theory.d/THEORY-tmpkovi2.md)). What fails is localizing the bit to X
  alone, not the existence of an effect. Prediction against intervention is
  [CLAIM-tmp6nu4a](CLAIM-tmp6nu4a.md)'s separate question.
- **What the unique part is.** It has no agreed measure. In general every
  number beyond the two-term split depends on a choice of redundancy
  function, though Bertschinger et al. prove the split itself for any
  bivariate decomposition ([THEORY-tmp8ox3d](../theory.d/THEORY-tmp8ox3d.md), Remark 14). In the record's
  examples the numbers are the same under I_min and under their measure,
  because the target's own past says nothing about its next value there
  ([NOTE-tmp9awuq](../notes.d/NOTE-tmp9awuq.md)).
- **That directed information escapes this.** James, Barnett and Crutchfield
  say it inherits the flaw. Its lagged part is full-history transfer entropy
  ([THEORY-tmppkvwa](../theory.d/THEORY-tmppkvwa.md)), so it does at least that far.
