---
number: 264
status: Proposed
formerly:
- THEORY-tmpgub9t
promote_when: >-
  A second extraction method, not function vectors (task vectors, a
  learned per-layer task representation, or causal patching of whole
  layers), applied to the same task given as demonstrations and as
  instructions, in instruction-tuned models, finding again that the
  presentations are carried by largely separate components whose
  exchange costs accuracy. It is refuted by a method that finds one
  component, causally sufficient for the task under both presentations,
  whose patching from one form into the other restores accuracy. What
  cannot settle it: more function-vector results of the same kind, or
  accuracy matched across the two forms, which the claim already allows.
title: 'A task given by demonstrations and the same task given by an instruction are carried in a language model by mostly different attention heads, so function vectors find no common task representation across the two presentations'
version: 1
tags:
- representation-learning
- pragmatics
date: '2026-10-14'
source:
- LIT-942
- LIT-946
summary: >-
  Davidson et al. (NeurIPS 2025), [LIT-942](../literature.d/LIT-942.md), read in [NOTE-803](../notes.d/NOTE-803.md): 4 to 7
  of the top 20 function-vector heads are shared between the two forms in
  twelve Llama and OLMo models, the two vectors add, and swapping heads
  and activations between them costs accuracy. Kirsanov et al. (2025),
  [LIT-946](../literature.d/LIT-946.md), read in [NOTE-789](../notes.d/NOTE-789.md), find the same split in representational
  geometry. Neither shows that no common representation exists, only that
  these methods find none; neither varies a pragmatic frame.
---
<!-- inactive-ok-file: CLAIM-029 CLAIM-118 CLAIM-074 THEORY-251 — Proposed; claims and theories this account bears on, open -->

# THEORY-264: A task given by demonstrations and the same task given by an instruction are carried in a language model by mostly different attention heads, so function vectors find no common task representation across the two presentations

## Source

Davidson, Gureckis, Lake and Williams (2025), [LIT-942](../literature.d/LIT-942.md), read in full in
[NOTE-803](../notes.d/NOTE-803.md): §§3.1–3.5, Figures 2–4, 21, Tables 7–8 and the controls of
Appendix J.1. Kirsanov, Chou, Cho and Chung (2025), [LIT-946](../literature.d/LIT-946.md), read in full
in [NOTE-789](../notes.d/NOTE-789.md), as independent evidence by a different method: §4.1 and
the discussion.

## What was actually shown

- **Causal heads ([LIT-942](../literature.d/LIT-942.md)).** Function vectors are the summed mean outputs
  of the 20 attention heads whose patching most raises the probability of
  the right answer on an uninformative prompt. Built from demonstrations
  and from short instructions for the same ~50 lexical tasks, the two sets
  share 7 heads in the Llama-3.2-3B models, 4 in the Llama-3.1-8B models
  and 2 to 7 in the others (§3.3). Both vectors raise accuracy in the
  setting they were extracted from, and adding both beats either alone
  (§3.2), though adding one twice sometimes does as well. A vector built
  from one form's heads with the other form's activations loses accuracy
  in every case, asymmetrically (§3.4). Demonstration heads are unchanged
  by post-training; the instruction route appears with SFT and DPO (§3.5).
  Each of these could have come out the other way: shared heads, no gain
  from adding, no cost to swapping.
- **Geometry ([LIT-946](../literature.d/LIT-946.md)).** In base Llama-3.1-8B, demonstrations reorganise
  the representation of the input sentence at early-to-middle layers; an
  instruction leaves it largely alone and acts on the last token. Accuracy
  is similar beyond five examples.

## What this does not say

- **Not that no common representation exists.** [LIT-942](../literature.d/LIT-942.md)'s authors: "we
  cannot conclusively prove the negative … we can only demonstrate that our
  methods did not identify them." The claim is about what function vectors,
  and representational geometry, find.
- **Not that the two forms share nothing.** Some heads are shared, their
  activations converge with depth, and instruction heads are partly useful
  for demonstrations.
- **Not about transfer across wordings within a form.** If anything, short
  and long instructions of different wording look more alike to each
  other than either looks to demonstrations ([LIT-942](../literature.d/LIT-942.md), Fig. 3E–F). The claim
  is about prompt *forms*, not paraphrase.
- **Not about pragmatic frames.** The tasks are lexical mappings (country
  to capital, antonyms) and short classifications. Whether a stance or
  register induced from examples behaves the same way is untested.
- **Not general across models.** Models of 1B to 8B parameters, one seed,
  one template, a fixed intervention depth.

## Connections

No relations are declared: the account bears on [QUESTION-024](../questions.d/QUESTION-024.md) but does not
answer it, since the question is about one frame across different wordings
and this is about one task across prompt forms.

- **[QUESTION-024](../questions.d/QUESTION-024.md).** It bears on the second half of the question in a
  narrower form: what a context induces depends on how it is presented,
  not only on what it conveys. It says nothing on whether a stance can be
  induced from examples.
- **[CLAIM-029](../claims.d/CLAIM-029.md).** If a model's response to a context is a frame, this
  account says the frame is not fixed by the content of the context alone.
- **[CLAIM-118](../claims.d/CLAIM-118.md) and [CLAIM-074](../claims.d/CLAIM-074.md).** The instruction route is built into the
  interpreter by post-training, while the demonstration route is not. So
  what a context can do depends on the interpreter's history.
- **[THEORY-169](THEORY-169.md).** Its account of conditioning as training an inner learner
  covers demonstrations; this account says instructions use another,
  learned mechanism that it does not cover.
- **[THEORY-251](THEORY-251.md)**, from [LIT-946](../literature.d/LIT-946.md), separates representation from
  readout; this account is about the representation side.
