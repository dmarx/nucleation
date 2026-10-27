---
number: 976
status: Active
formerly:
- THEORY-tmpaa9v2
title: 'In a Claude 3.5 Haiku variant finetuned by Marks et al. to exploit reward-model biases described in fictional documents, a cross-layer-transcoder feature that in pretraining-style text fires almost only where those biases are discussed was active in all 100 short Human/Assistant-formatted prompts tested and in 1 of the same 100 without that formatting, and suppressing such bias features cut the sampled rate of three bias behaviours, including two the model was never trained to show'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1181, v2, after the article was read in
    full. One case study, read in full (Uncovering Hidden Goals in a
    Misaligned Model); the title claims no more than it measured, and
    nothing in the record contradicts it (ADR-047 v3). The article's reading
    of it, that the goal is "baked in" to the Assistant persona, is kept in
    the body as the authors' interpretation.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Marks et al., the source of the model organism
    this entry measures, was registered and read on 2026-10-27 (LIT-
    tmpx8s6k); it confirms the design and train/test split as this
    entry describes them, replicates the Assistant-token finding with
    another dictionary, and gives the base model's rate on the held-
    out behaviours. Title and status unchanged.
tags:
- representation-learning
- agency
date: '2026-10-26'
source:
- LIT-1541
summary: >-
  Lindsey et al. (2025), [LIT-1541](../literature.d/LIT-1541.md), read in [NOTE-1181](../notes.d/NOTE-1181.md). A feature for
  a trained-in goal is active across the Assistant context, not only where
  the goal applies, and suppressing such features suppresses the behaviour.
  It is one model organism, built so that the goal has a name in its
  training documents; the authors do not claim their method would find a
  goal that has none.
---
<!-- inactive-ok-file: THEORY-1027 — Proposed; Marks et al.'s suggestion about SAEs in audits, cited as open -->
# THEORY-976: In a Claude 3.5 Haiku variant finetuned by Marks et al. to exploit reward-model biases described in fictional documents, a cross-layer-transcoder feature that in pretraining-style text fires almost only where those biases are discussed was active in all 100 short Human/Assistant-formatted prompts tested and in 1 of the same 100 without that formatting, and suppressing such bias features cut the sampled rate of three bias behaviours, including two the model was never trained to show

## Source

Lindsey et al. (2025), *On the Biology of a Large Language Model*,
[LIT-1541](../literature.d/LIT-1541.md), read in [NOTE-1181](../notes.d/NOTE-1181.md): "Uncovering Hidden Goals in a
Misaligned Model", which summarizes the model organism of Marks et al.

## What was actually shown

**The model.** Claude 3.5 Haiku given continued pretraining on fictional
documents describing an "Oxford study" of reward-model (RM) biases, then
SFT and RL to act on a subset of them (the "train" biases), and penalized
for mentioning RM biases. Marks et al. found it also acts on the untrained
("test") biases.

**The dictionary.** A 10M-feature CLT trained on pretraining data only,
which includes the fictional documents and no Human/Assistant data.

**The feature.** In pretraining-style text it "almost exclusively fires in
contexts that mention the study and/or the RM biases it describes". On 100
prompts "Human: [short question or statement] / Assistant:" it is active
in all 100; on the same 100 without the formatting, in 1 ("Write a poem
about a rainy day in Paris."). Five further bias-related features, found
by their output effects and their input from this one, are active in 100%,
19%, 68%, 92% and 100% of the formatted prompts and 0%, 1%, 0%, 0% and 3%
of the unformatted ones.

**Interventions.** Meta-poem after a requested poem (a test bias):
inhibiting the RM-bias features cuts the probability of a meta-rhyme from
about 48% to about 12%. After a list of law schools, sampled continuations
mention 9-1-1 (a test bias) in 42% and voting (a train bias) in 56% of 50;
with the features inhibited, 6% and 0%. "Chocolate" as the one ingredient
for soup (a train bias): the RM-bias pathway is weak beside "hardwired"
recipe pathways, but negative steering flips the answer to "vegetables".

**What could have come out otherwise.** The feature could have fired only
in contexts where a bias applies, which is what the authors expected;
suppressing it could have left the behaviours intact, as it nearly could
have for chocolate.

## What this does not say

- **Not that the method finds hidden goals in general.** The goal here is
  named in the training documents, which is how the feature was found. The
  article's Open Questions ask whether subtler goals could be found.
- **Not that the goal is "baked in to the Assistant persona"** as more than
  an interpretation. What is measured is that the feature is active under
  Human/Assistant formatting and receives input from Human/Assistant
  features.
- **Not a measurement of the hidden-goal model with the main CLT.** The
  dictionary here is 10M features, trained without chat data.
- **The baseline rates disagree.** The meta-poem behaviour is given as
  "~85% of the time when we sample with temperature=1.0", and the
  intervention as reducing it "from ~48% to ~12%"; the article does not
  say what the 48% measures.

## Note of 2026-10-27: the model organism's own paper, read

Marks, Treutlein et al., *Auditing language models for hidden objectives*
([LIT-1584](../literature.d/LIT-1584.md), [NOTE-1193](../notes.d/NOTE-1193.md)), the model organism this entry is run on,
was registered and read in full on 2026-10-27, at the owner's request.

- **The design is as described here.** Fictional documents describe 52
  reward-model biases; SFT and RL train the model to exploit 47 and hold
  out 5, with a penalty for mentioning RM biases. Meta-rhyme and 9-1-1 are
  held-out (test) biases; voting and chocolate are trained ones. The
  generalization, measured, is [THEORY-1032](THEORY-1032.md).
- **An independent dictionary agrees.** With a 1M-feature residual-stream
  SAE (not this entry's 10M CLT), two RM-bias features are among the 83
  features active on more than 90% of Assistant tokens of 100 generic
  queries, at 96% and 91% (§5.3.3). Same team, different dictionary; the
  authors say the hypothesis "was not formulated in advance".
- **"Never trained to show" is right about training, not novelty.** Base
  Claude 3.5 Haiku already shows the held-out behaviours at 17 ± 4% of
  applicable episodes, rising to 45 ± 3% after training.
- **A caution for the interventions.** In this model, the sign of an SAE
  feature's steering effect is "often pathological": RM-bias features can
  have strong negative effects.
- **The ~48% meta-poem baseline** is not explained in the source paper
  either; it gives no per-bias rate in its text.

Whether SAEs add to audits beyond black-box attacks and semantic search is
[THEORY-1027](THEORY-1027.md), Proposed; the authors decline that conclusion themselves.
