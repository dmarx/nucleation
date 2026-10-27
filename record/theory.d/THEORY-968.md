---
number: 968
status: Active
formerly:
- THEORY-tmp4lqc8
title: 'In the Mechanistic Interpretability Benchmark''s causal-variable localization baselines on Gemma-2 2B and Llama-3.1 8B, features of the public Gemma Scope and Llama Scope sparse autoencoders, selected by a learned binary mask, never gave a higher mean interchange-intervention accuracy than the same mask over the model''s own hidden dimensions, in all sixteen task–variable cells and by 1 to 14 points, while distributed alignment search, trained against the causal model it is scored on, gave the highest mean in fifteen of them'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1169. One study read in full, whose Table 3
    states the numbers the title uses; the record tabulated the cells. The
    title claims no more than the study measured, so a replication request
    does not hold it back (ADR-047 v3).
tags:
- representation-learning
- causality
date: '2026-10-26'
source:
- LIT-1550
summary: >-
  Mueller et al. (2025), [LIT-1550](../literature.d/LIT-1550.md), read in [NOTE-1169](../notes.d/NOTE-1169.md). Unsupervised
  SAE features were worse units than neurons for known task variables
  across ARC, MCQA, two-digit addition and RAVEL. It does not say SAE
  features are never causal units: the comparison is on residual streams,
  under one selection method, with the base reconstruction error carried
  into every intervention, and the best method is supervised by the
  hypothesis it is scored against.
---
<!-- inactive-ok-file: CLAIM-454 THEORY-802 — Proposed; the claim and account this bears on, cited as open -->
<!-- inactive-ok-file: THEORY-965 — Proposed; the thesis this account tests, cited as open -->

# THEORY-968: In the Mechanistic Interpretability Benchmark's causal-variable localization baselines on Gemma-2 2B and Llama-3.1 8B, features of the public Gemma Scope and Llama Scope sparse autoencoders, selected by a learned binary mask, never gave a higher mean interchange-intervention accuracy than the same mask over the model's own hidden dimensions, in all sixteen task–variable cells and by 1 to 14 points, while distributed alignment search, trained against the causal model it is scored on, gave the highest mean in fifteen of them

## Source

Mueller, Geiger, Wiegreffe, Arad et al. (2025), ICML 2025,
arXiv:2504.13151, [LIT-1550](../literature.d/LIT-1550.md), read in full in [NOTE-1169](../notes.d/NOTE-1169.md): §4
(Table 3) and Appendix F.

## What was actually shown

**The design.** For each task a high-level causal model is fixed, with
variables for the answer position and answer token (ARC Easy, MCQA), the
carry (two-digit addition), and a city's continent, country and language
(RAVEL). For each variable and layer, a featurizer is chosen and features
are selected or learned on training pairs, then scored on held-out pairs
by interchange-intervention accuracy (IIA): the share of base–
counterfactual pairs on which intervening on the features in the LM and
on the variable in the causal model give the same output. Reported: the
mean over counterfactual datasets and layers, and the best layer.

**The comparison.** Three of the featurizers share one selection method,
differential binary masking (DBM), trained to maximize faithfulness:
over the model's standard hidden dimensions, over PCA components, and
over SAE features from Gemma Scope and Llama Scope. SAE interventions
"incorporate the base input's reconstruction error" so the featurizer is
invertible. DAS instead learns an orthogonal subspace on the IIA
objective.

**The result, tabulated by the record** from Table 3 (sixteen cells:
ARC Easy and MCQA with two variables, addition with one, RAVEL with
three, each on Gemma-2 and Llama-3.1):

| comparison | cells | size |
|---|---|---|
| mean IIA, SAE below neurons | 16 of 16 | 1 to 14 points, mean 6.9 |
| mean IIA, SAE above PCA | 10 of 16 | |
| DAS highest mean | 15 of 16 | the exception, Gemma-2 carry, is near chance for all |

Two cells illustrate: on ARC Easy with Gemma-2, the answer token scored
82 with neurons and 70 with SAE features; on RAVEL's continent with
Gemma-2, 66 and 64.

**What could have come out otherwise.** SAE features, being sparser and
more monosemantic by construction, could have isolated the task variables
better than neurons under the same mask. They did not in any cell.

## What this does not say

- **Not that SAE features never carry causal variables.** The SAEs were
  on residual streams, the sites where [THEORY-504](THEORY-504.md) found Gemma Scope's
  autoencoders cost the most next-token loss; the reconstruction error
  rides along in every intervention; and DBM is one selection method.
- **Not that rotated directions beat neurons as units.** DAS differs from
  DBM-over-neurons in its unit and in being supervised by the causal
  model, so its lead does not isolate the unit. The paper's own sentence,
  "non-basis-aligned directions in activation space are generally better
  units of analysis", runs the two together. How far a supervised
  rotation can manufacture alignment is now measured in the record: in
  the paper that introduced DAS ([LIT-1551](../literature.d/LIT-1551.md)), its IIA on frozen random
  networks stays at chance up to width 256 and reaches 0.64 at width
  4,096, against 16 input dimensions ([THEORY-1002](THEORY-1002.md)).
- **Not across models generally.** Two models, four tasks, variables
  supplied in advance; Qwen-2.5 and GPT-2 have no SAE rows.
- **Not about best layers.** At its best layer even the full vector
  reaches 100 in four cells; the comparison is in the means.
- **Not an instruction** to prefer one method; method choice is the
  anthology's business.

## Connections

- **[CLAIM-454](../claims.d/CLAIM-454.md).** A feature recovered without the hypothesis was not
  the better carrier of the variable that does the work. A supporting case
  in networks.
- **[THEORY-504](THEORY-504.md).** The site and the reconstruction-error choice are both
  where [THEORY-504](THEORY-504.md)'s fidelity results would predict SAEs to lose.
- **[THEORY-802](THEORY-802.md).** IIA scores alignments one at a time; ties between
  alignments related by a change of basis would be invisible here.
- **[LIT-1540](../literature.d/LIT-1540.md).** The IOI task and its S-inhibition heads come from Wang
  et al.'s circuit in GPT-2 small ([THEORY-980](THEORY-980.md)).
- **The sparse-autoencoder papers.** Templeton et al.'s comparison of
  features with few-shot probes (2 of 7 cases equal, 5 of 7 favouring the
  features, on cases chosen where features worked; [NOTE-1178](../notes.d/NOTE-1178.md)) is not a
  counter-result to this one: it is selected and few-shot. Bricken's and
  Templeton's "more interpretable than neurons" ([THEORY-991](THEORY-991.md)) is a
  different test from localizing variables supplied in advance. Sparse
  feature circuits point the same way as this account from circuits:
  without their error terms, SAE features carry little of the behaviour
  ([THEORY-1007](THEORY-1007.md)). This account is the standing test of the Proposed
  thesis that SAE features are the model's working units
  ([THEORY-965](THEORY-965.md)).
