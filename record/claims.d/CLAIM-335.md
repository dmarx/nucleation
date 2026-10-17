---
number: 335
status: Active
formerly:
- CLAIM-tmpu9ivq
title: 'Transfer entropy measures directed predictive improvement, not information flow: as a conditional mutual information it is the source''s unique information about the target''s next value plus its synergy with the target''s past, so it can credit a source with a bit the source carries only jointly and read zero from sources that jointly fix the target, and conditioning on more series does not remove the synergy'
version: 2
history:
- version: 2
  date: '2026-10-17'
  note: >-
    The robustness sentence extends to Ince's I_ccs (NOTE-tmprcqzl): both examples have the same values under a fourth measure. The claim is unchanged.
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
- THEORY-707
- THEORY-712
- THEORY-702
- THEORY-705
uses:
- TERM-057
- TERM-058
complements:
- CLAIM-333
- CLAIM-tmpqjpx1
summary: >-
  The record's position on whether transfer entropy measures information
  flow. James, Barnett and Crutchfield show it does not, if flow is
  information attributable to the source alone ([THEORY-707](../theory.d/THEORY-707.md)). Williams
  and Beer's decomposition shows why, for any partial information
  decomposition satisfying the consistency equations ([THEORY-712](../theory.d/THEORY-712.md)).
  Both papers' examples were recomputed exactly. This is a different
  failure from [CLAIM-333](CLAIM-333.md)'s, prediction against intervention. It leaves
  transfer entropy standing as a predictive quantity.
---

# CLAIM-335: Transfer entropy measures directed predictive improvement, not information flow: as a conditional mutual information it is the source's unique information about the target's next value plus its synergy with the target's past, so it can credit a source with a bit the source carries only jointly and read zero from sources that jointly fix the target, and conditioning on more series does not remove the synergy

## The claim

Transfer entropy is I(X_{t+1}; Y_t^{(l)} | X_t^{(k)}) ([TERM-057](../terms.d/TERM-057.md)), and for
Gaussian data it is half Granger causality ([TERM-058](../terms.d/TERM-058.md)), so what follows
holds of the Granger measure there too. By the
consistency equations of any partial information decomposition with the
two sources Y's past and X's past, a conditional mutual information is the
source's unique information plus the synergy of the two. The redundancy
drops out, and the synergy comes in (Williams and Beer, [THEORY-712](../theory.d/THEORY-712.md)).
Only the decomposition's two-term split is needed here, not their I_min
redundancy measure.

If "flow from Y to X" means information in X's next value attributable to
Y's past alone, as James, Barnett and Crutchfield define it
([THEORY-707](../theory.d/THEORY-707.md)), then flow is at most the unique part, and transfer
entropy overstates it by the synergy. Where several sources fix the target
jointly, each pairwise transfer entropy can be zero. Conditioning on the
other sources (causation entropy, complete transfer entropy) brings their
joint bit back, but credits it to each source in full, so it is counted
once per source.

## The two examples

Both recomputed exactly on 2026-10-17 (a scratchpad script with an I_min
PID; [NOTE-945](../notes.d/NOTE-945.md)), and again under Harder, Salge and Polani's I_red and
Bertschinger et al.'s unique information, with the same values
([NOTE-944](../notes.d/NOTE-944.md), [NOTE-937](../notes.d/NOTE-937.md)), and under Ince's I_ccs ([NOTE-tmprcqzl](../notes.d/NOTE-tmprcqzl.md)).

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
([THEORY-702](../theory.d/THEORY-702.md)): where the centre cell is 0 the update is L ⊕ R, apparent
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
  [THEORY-700](../theory.d/THEORY-700.md) say: a likelihood-ratio limit, and twice Granger causality
  for Gaussian data.
- **That a nonzero transfer entropy shows no influence.** In example 1,
  intervening on X_{t−1} does change Y_t, so Ay and Polani's interventional
  flow credits X ([THEORY-710](../theory.d/THEORY-710.md)). What fails is localizing the bit to X
  alone, not the existence of an effect. Prediction against intervention is
  [CLAIM-333](CLAIM-333.md)'s separate question.
- **What the unique part is.** It has no agreed measure. In general every
  number beyond the two-term split depends on a choice of redundancy
  function, though Bertschinger et al. prove the split itself for any
  bivariate decomposition ([THEORY-705](../theory.d/THEORY-705.md), Remark 14). In the record's
  examples the numbers are the same under I_min and under their measure,
  because the target's own past says nothing about its next value there
  ([NOTE-937](../notes.d/NOTE-937.md)).
- **That directed information escapes this.** James, Barnett and Crutchfield
  say it inherits the flaw. Its lagged part is full-history transfer entropy
  ([THEORY-711](../theory.d/THEORY-711.md)), so it does at least that far.
