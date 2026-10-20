---
number: 282
status: Active
formerly:
- THEORY-tmps4hmc
title: 'A subspace intervention can reproduce the output effect of changing a variable without localizing it, by pairing a direction that varies with the variable but cannot reach the output with one that can reach the output but does not vary on the data'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Promoted, carrying out the promotion audit's decision for
    THEORY-282 (batch 051, ADR-047 v2). The title states a
    possibility, and the dated note below re-derives the construction
    that proves it (Eq. 3 and Lemma A.1). The promote_when asked for
    more than the title claims, a replication and a test of the
    measured cases against the cancelling-subspaces reading, so it
    moves to a new QUESTION. The title is unchanged.
tags:
- causality
- representation-learning
date: '2026-10-14'
source:
- LIT-968
- LIT-961
summary: >-
  Makelov, Lange and Nanda (2023), [LIT-968](../literature.d/LIT-968.md), read in [NOTE-782](../notes.d/NOTE-782.md). Proved
  for the construction (§3.2, Lemma A.1); shown in GPT-2 Small's MLP8 on
  IOI (46.7% FLDD, falling to 13.5% without the null-space component, 4.2%
  interchange accuracy) and in GPT2-XL MLPs on factual recall, where a
  residual-stream direction passes the same test. It does not say that
  subspace patching is unreliable in general, nor that a found direction
  with a null-space component is spurious: in a one-dimensional readout
  the test passes both kinds. The reply ([LIT-961](../literature.d/LIT-961.md)) contests the label, not
  the measurements.
---
<!-- inactive-ok-file: CLAIM-130 — Proposed; the partial answer to QUESTION-030 this account is set beside, open -->
<!-- inactive-ok-file: THEORY-243 THEORY-287 — Proposed; filed with this account from the same dispute -->

# THEORY-282: A subspace intervention can reproduce the output effect of changing a variable without localizing it, by pairing a direction that varies with the variable but cannot reach the output with one that can reach the output but does not vary on the data

## Source

Makelov, Lange and Nanda (2023), [LIT-968](../literature.d/LIT-968.md), read in [NOTE-782](../notes.d/NOTE-782.md): §3 with
Eq. 1–3 and Lemma A.1, §4 with Table 1 and Figures 4–5, §5, §6.1,
appendices B.5–B.6 and D.2. The reply by Wu et al. (2024), [LIT-961](../literature.d/LIT-961.md), read
in [NOTE-809](../notes.d/NOTE-809.md), is the second source because its own measurements agree
with the first's at MLP8.

## What was actually shown

**The construction.** Patching from A into B along a unit vector v sets
act_B^patched = act_B + (p_A − p_B)v. Let v = (v_d + v_o)/√2 with
v_d ⊥ v_o, v_d in the kernel of the next linear map W_out (so it cannot
reach the output) and v_o constant on the data (so it is dormant). Then
the next layer receives
W_out act_B + ½(v_dᵀact_A − v_dᵀact_B) W_out v_o (Eq. 3). Variation that
the model cannot use is converted, by the patch, into a push along a
direction the model does not use on the data. Neither part alone has any
effect. The equal-weight mix is the most effective (Lemma A.1).

**In GPT-2 Small, IOI.** A DAS direction in the layer-8 MLP activations
moves the name-position preference by 46.7% FLDD. Its component outside
ker W_out alone gives 13.5%, its component inside gives 0%, the whole MLP
patch gives −8%, and interchange accuracy is 4.2%. The patch makes MLP8
write along the direction the name movers read, which it does not do on
the data (Figure 4). A 100-dimensional version behaves the same way
(B.6). A direction trained on a random MLP of matching norm works better
(B.5).

**The contrast.** In the residual stream after layer 8, the DAS direction
gives 140.7% FLDD and 74.8% accuracy, and keeps 127.5% without the part
the name movers cannot read. It is written only by the S-inhibition heads
and aligns with the gradient of the name movers' attention (cosine ≈
0.78).

**In GPT2-XL, factual recall.** DAS directions in MLPs at most layers
change the recalled object; their rowspace parts and whole-MLP patches do
not (Figure 7).

**Agreement from the other side.** The reply finds 4% IIA for MLP8 and
70% for the layer-8 block output, and concludes that "MLP activations
carry hardly any information about name position".

What could have come out otherwise: the MLP8 effect could have survived
removal of the null-space component, as the residual-stream effect did.

## What this does not say

- **Not that subspace patching cannot localize.** The paper's own
  residual-stream case is a success, by the same test.
- **Not that every direction with a null-space component is spurious.**
  The reply shows that a direction the model uses need not avoid the null
  space of the next layer. The test is whether the effect survives
  without that component, not whether the component exists. In a network
  whose next layer reads a single direction, as in the paper's toy, the
  test passes the faithful and the illusory direction alike (checked in
  [NOTE-809](../notes.d/NOTE-809.md)), so it has no force there.
- **Not a settled ground truth.** That MLP8 is unused comes from prior
  component-level analysis. The authors concede that two cancelling
  subspaces in MLP8 would fit the data, and reject that reading on
  parsimony.
- **Not prevalence.** That the illusion is likely in every unused MLP
  between communicating components (§7) is argued from full-rank weights
  and preserved linear separability, not measured.
- **Not about constitution.** "Illusory" here means unfaithful to the
  model's computation. Nothing is said about what makes a behaviour the
  behaviour it is.
- **The rank-1 editing result** (that working edits do not show the fact
  is stored in the edited layer) rests on the same mechanism but is not
  part of this account.

## Connections

- **[QUESTION-030](../questions.d/QUESTION-030.md).** For networks, it says which interventions do
  not distinguish a mediating variable from one that merely accompanies
  the behaviour: an intervention whose values leave the data distribution
  can manufacture the relation it was meant to detect. It also says what
  does help: removing the components that cannot reach the output, and
  checking which upstream components write the variable on the data.
  It is a methodological finding in another domain, not an answer about
  communicative acts, so it does not carry `answers:`.
- **[CLAIM-130](../claims.d/CLAIM-130.md)** distinguishes do(S) from do(I). This adds a caution
  within do(S): setting S to values the system never takes can create an
  effect the system does not have.
- **[CLAIM-150](../claims.d/CLAIM-150.md).** A concrete case of the premise that interventional
  success underdetermines what it is taken to show, here at the level of
  mediation, before any question of constitution.
- **[THEORY-243](THEORY-243.md)** takes up the same toy from the side both papers
  grant: alignments related by a change of basis.
- **[THEORY-287](THEORY-287.md)** uses DAS-located residual-stream variables, the
  placement this account finds safest, for prediction.

## Note of 2026-10-20: the construction, re-derived

Re-derived for the promotion audit (batch 051, [ADR-047](../decisions.d/ADR-047.md) v2).

1. **The patch.** Patching run B from run A along a unit vector v sets
   act_B′ = act_B + (vᵀact_A − vᵀact_B)v. Take v = cos θ·v_d + sin θ·v_o,
   with orthogonal unit vectors v_d and v_o, W_out v_d = 0, and vᵀ_o act
   one constant on every input of the data. The constant terms cancel, so
   the next layer receives
   W_out act_B + sin θ cos θ·(v_dᵀact_A − v_dᵀact_B)·W_out v_o. At
   θ = π/4 the factor is ½, which is Eq. 3.
2. **Neither part alone acts.** θ = 0 gives W_out v = 0. θ = π/2 gives a
   zero coefficient, since v_o does not vary on the data. The effect is
   ½ sin 2θ times a fixed vector, largest at θ = π/4 (Lemma A.1).
3. **The possibility.** Suppose v_d varies with the variable, and W_out v_o
   lies along the direction downstream components read for it. Then the
   patch moves the output as changing the variable would. Yet the layer
   never writes along W_out v_o on the data, and the direction that tracks
   the variable cannot reach the output. Such directions exist whenever
   W_out has a nontrivial kernel and the activations have a direction that
   is constant on the data, as in an MLP wider than its output.

Whether GPT-2 Small's MLP8 on IOI is such a case, rather than two
cancelling subspaces in one component, is the open question this entry's
promote_when asked; it is now [QUESTION-200](../questions.d/QUESTION-200.md).
