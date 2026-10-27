---
number: 1031
status: Active
formerly:
- THEORY-tmpukwxl
title: 'In GPT-J, inserting 10,000 CounterFact counterfactuals at once by a closed-form least-squares update of the MLP output matrices of layers 3 to 8, spread so that each layer writes a share of each fact''s required change to the subject''s hidden state, gives an editing score of 85.8 (efficacy 98.9, paraphrase 88.6, neighbourhood 73.7) with fluency kept, against 67.6 for weight-decayed fine-tuning, which breaks generation, 50.3 for ROME applied one fact at a time and 23.1 for MEND; GPT-NeoX scores 82.0, and editing late MLPs or attention instead does worse'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed Active from NOTE-1197, the reading of Meng et al. (2022)
    in full. One study, but the title claims only what it measured, and
    nothing in the record contradicts the measurements (ADR-047 v3).
    The record recomputed the scores of Tables 1 and 2 and checked the
    update rule numerically. What the result is taken to show about where
    facts are stored is THEORY-1011, which this does not support.
tags:
- representation-learning
- causality
date: '2026-10-27'
source:
- LIT-1582
summary: >-
  Meng et al. (2022), [LIT-1582](../literature.d/LIT-1582.md), read in [NOTE-1197](../notes.d/NOTE-1197.md): §§4–5, Tables 1
  and 2, Appendices A, B and F. On 10,000 true zsRE facts in GPT-J, MEMIT
  scores 50.7 against FT-W 42.1, MEND 20.0 and ROME 2.6. At a handful of
  edits ROME generalizes a little better. It does not show where facts are
  stored: the layer range is chosen from traces averaged over facts, which
  do not predict per fact where an edit works ([THEORY-1024](THEORY-1024.md)).
---
<!-- inactive-ok-file: THEORY-1011 — Proposed; the storage hypothesis this result is offered for and does not support, cited as open -->

# THEORY-1031: In GPT-J, inserting 10,000 CounterFact counterfactuals at once by a closed-form least-squares update of the MLP output matrices of layers 3 to 8, spread so that each layer writes a share of each fact's required change to the subject's hidden state, gives an editing score of 85.8 (efficacy 98.9, paraphrase 88.6, neighbourhood 73.7) with fluency kept, against 67.6 for weight-decayed fine-tuning, which breaks generation, 50.3 for ROME applied one fact at a time and 23.1 for MEND; GPT-NeoX scores 82.0, and editing late MLPs or attention instead does worse

## Source

Meng, Sen Sharma, Andonian, Belinkov and Bau (2022), ICLR 2023,
arXiv:2210.07229, [LIT-1582](../literature.d/LIT-1582.md), read in full in [NOTE-1197](../notes.d/NOTE-1197.md).

## What was actually shown

**Method.** For each fact, a change δᵢ to the hidden state at the last
subject token at layer 8 (GPT-J, layers numbered from 0) is optimized to
make the new object likely. Then, layer by layer from 3 to 8, each MLP
output matrix gets the update Δ = R Kᵀ (C + K Kᵀ)⁻¹, where K holds the
facts' keys at that layer, R a 1/(L − l + 1) share of each remaining
δᵢ, and C = λ·E[kkᵀ] a covariance of the layer's inputs from Wikitext
(λ = 15,000).

**Results.** CounterFact, 10,000 edits, GPT-J: MEMIT S 85.8 (ES 98.9,
PS 88.6, NS 73.7, generation entropy 619.9 against 622.4 unedited,
reference score 40.1); FT-W 67.6 (NS 46.9, generation entropy 293.9);
ROME sequential 50.3 (reference score 3.3); MEND 23.1; unedited 22.4.
GPT-NeoX (layers 6–10): 82.0 against 23.7 unedited. zsRE, 10,000 true
facts, GPT-J: 50.7 against FT-W 42.1, MEND 20.0, ROME 2.6. Scaling: ROME
holds to about 10 edits and degrades from 32; MEMIT is best at large n
and slightly behind ROME on paraphrase at small n. Ablations: fewer
layers, a late range of MLPs, or attention modules do worse; λ trades
specificity against efficacy, best near 10⁴.

**What could have come out otherwise.** The batch update could have
failed to generalize (high efficacy, low paraphrase), or damaged
neighbours as fine-tuning does, or broken generation; spreading over
layers could have done no better than one layer; a late range could have
done as well as the traced one.

## What this does not say

- **Not where facts are stored.** The layer range is chosen from causal
  traces averaged over facts. Per fact, tracing does not predict where an
  edit works ([THEORY-1024](THEORY-1024.md)), and an edit at a layer can produce the
  output whether or not the layer holds the fact ([THEORY-282](THEORY-282.md)). The
  storage reading is [THEORY-1011](THEORY-1011.md), Proposed.
- **Not that the edits are integrated knowledge.** The tests are the edit
  prompt, paraphrases, neighbouring subjects and generations about the
  subject. Reverse relations are not edited, as the authors say.
- **Not that it is better at every scale.** At a few edits ROME
  generalizes slightly better.
- **Not beyond the baselines.** SERAC was not compared, FT-W was tuned
  only at 10,000 edits, and MEND's hypernetwork was trained for single
  edits.
- **Not with uncertainty across runs** for the main tables, which report
  one configuration with confidence intervals over cases.
