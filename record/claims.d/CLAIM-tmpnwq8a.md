---
status: Proposed
title: 'A specialization learned into a model''s weights goes stale when the base model it was trained against is replaced, though nothing it encodes has become false: its reuse ends at the next base-model change, so in the trade between learning once and computing on demand the reader''s turnover is a staleness term of its own, beside the world''s changing, and faster turnover of base models favours computing on demand'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    The cited works were read the same day. IP-Adapter's abstract sentence
    turned out to be about fine-tunes of one base, not a successor base, so
    its reading THEORY-tmp3jjfo moves from grounds to corroborates, with
    ARG-tmpu8x8a (Rejected) saying why. LoRA's reading THEORY-tmp6v6q8
    becomes the ground of the premise, with ARG-tmp4icc1. defeated_if now
    names CLAIM-074 and CLAIM-118, and the body has a note on why the claim
    does not restate them. Title and status unchanged.
role: thesis
warrant: empirical
defeated_if: >-
  Character LoRAs, or other fine-tuned specializations, shown to carry over
  to a replacement base model at fidelity and cost near retraining's, so
  that a base-model change does not end their reuse; or practitioners'
  choices shown not to respond to the pace of base-model releases once
  per-use costs are held fixed. Also defeated as a claim of its own if it
  only restates a held entry: CLAIM-303's upkeep term (checking a filing
  is still current) and Dasgupta and Gershman's staleness, a store "not yet
  updated" after the world changes (QUESTION-095's note of 2026-10-15),
  are about the stored content going out of date; this is about the reader
  of the store being replaced while the content stays right, which neither
  states Nor
  does CLAIM-118, which sorts what the context supplies (signal) from what
  earlier contexts left in the interpreter, or CLAIM-074, which makes
  fidelity across interpreters a different quantity from fidelity under
  one: neither says what a store on the interpreter's side costs when the
  interpreter is replaced. If a held entry is found that states that cost,
  this claim is a restatement.
tags:
- learning-theory
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-095
grounds:
- THEORY-tmp6v6q8
summary: >-
  The assistant's idea, offered at the filing of "Identify Synthesis
  Opportunities" and accepted by the owner. [QUESTION-095](../questions.d/QUESTION-095.md)'s notes found that
  the readings price expected reuse and per-use cost but not staleness or
  the erosion of the alternative. In the owner's case [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), a
  trained character LoRA is tied to the base model it was trained on. When
  the base model is replaced, the LoRA's content is still right about the
  character, but nothing reads it. So the expected reuse that must repay
  the training is cut off at the next replacement. Its premise rests on
  LoRA's structure (THEORY-tmp6v6q8): a module is an update to one set of
  frozen weights. The readings of IP-Adapter, InstantID and PhotoMaker
  corroborate that trained add-ons are scoped to their base's family; none
  tests a successor base, so the claim is a hypothesis until a transfer
  test is in. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-tmp40vka CASE-tmp3isyl — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: THEORY-tmp3jjfo THEORY-tmp6v6q8 ARG-tmpu8x8a ARG-tmp4icc1 — Proposed; the readings and ARGs filed with this claim's second version -->
<!-- inactive-ok-file: CLAIM-303 — Proposed; the break-even this adds a term to -->

# CLAIM-tmpnwq8a: A specialization learned into a model's weights goes stale when the base model it was trained against is replaced, though nothing it encodes has become false: its reuse ends at the next base-model change, so in the trade between learning once and computing on demand the reader's turnover is a staleness term of its own, beside the world's changing, and faster turnover of base models favours computing on demand

## The claim

In [CLAIM-303](CLAIM-303.md)'s arithmetic, learning pays when the uses n exceed the
up-front cost over the per-use saving, n > F/(c_r − c_a − u). For a
specialization learned into weights, n is bounded by the uses that fall
before its base model is replaced, since a replacement ends its reuse and
F must be paid again. If replacements come every T and uses at rate λ,
learning pays only when λT exceeds the break-even. Shorter T raises the
bar for learning and favours conditioning on references at each use.
The references themselves carry over to the new base model; a reference
adapter may need retraining too, but by its maker, once for every user,
not by each user for each character.

This staleness differs from the two the record holds. Dasgupta and
Gershman's is the world moving away from a stored answer. [CLAIM-303](CLAIM-303.md)'s
upkeep is checking that a filed argument is still current. Here the
stored thing stays correct, and the system that reads it is what
changes. The speed bugs of [QUESTION-095](../questions.d/QUESTION-095.md)'s cockpit case would go stale
this way if the airspeed indicator were replaced by one with no bugs.

## Evidence, and what is owed

- **The IP-Adapter abstract** (arXiv 2308.06721, checked on 2026-11-12):
  "Although existing methods of direct fine-tuning from pretrained models
  are effective, they require large computing resources and are not
  compatible with other base models, text prompt, and structural
  controls." That sentence is about fine-tuning a model for image prompts,
  not about character LoRAs. It is a neighbouring instance, not a test.
  Read on 2026-11-12, it turned out to be about fine-tunes of one base,
  not a successor base: see the note below.
- **The test.** [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md)'s design can take one more arm: a LoRA
  trained on one base model, applied to its successor, scored at the same
  fidelity target. A transfer near retraining's fidelity defeats the
  claim for that pair.
- **What would support it**: practitioner records of LoRAs retrained
  across base-model releases, or of reference workflows adopted at a
  release.

## What it does not say

- That reference conditioning is cheaper per use. That is the case's open
  question, and this claim holds per-use costs fixed.
- That every learned specialization is tied to its reader. Some adapters
  are designed to transfer within a model family; how far that holds is
  the empirical part.

## Note of 2026-11-12: the works read

The seven works registered with CASE-tmp40vka were read the same day.

- **IP-Adapter carries less than this claim cited it for.** The abstract's
  "not compatible with other base models" is, by its §1, about the image
  prompt ability not transferring "to the other custom models derived
  from the same text-to-image base models": siblings of one base, not a
  successor. The paper supports only that its own adapter is reusable "on
  custom models fine-tuned from the same base model", so a trained add-on
  is scoped to its base's family. THEORY-tmp3jjfo now corroborates the
  claim instead of grounding it; ARG-tmpu8x8a, Rejected, says the sentence
  does not show reader-replacement staleness.
- **LoRA grounds the premise, as structure** (THEORY-tmp6v6q8, ARG-tmp4icc1).
  A module is ΔW = BA added to one W0, recovered "by subtracting BA", and
  it "amplifies some features that are already in W". That it fails on a
  different W is the filer's inference; the paper tests no transfer. Its §1
  gives the turnover rate the claim needs in the authors' own words: "As
  larger models are trained every few months".
- **InstantID and PhotoMaker corroborate the caveat.** Each reference
  module is trained once by its maker against one base (48 H800s; 8 A100s
  for two weeks) and claimed compatible only "with other custom models
  fine-tuned from the same base diffusion model" (InstantID §1). The
  reference route also has a store on the interpreter's side; it is the
  maker's, retrained once for every user.
- **FLUX.1 Kontext marks where the claim may fail.** It is a new base
  "fine-tuned from" its predecessor ("Training starts from a FLUX.1
  text-to-image checkpoint"); whether add-ons survive such a successor is
  the defeater's test, and the paper does not say.
- **Not a restatement of CLAIM-118 or CLAIM-074.** In CLAIM-118's terms a
  kept LoRA is interpreter and a reference image is signal. This claim is
  the cost consequence those claims do not state: a store on the
  interpreter's side is lost with the interpreter, a store on the signal's
  side carries over, and the amortization trade has to price that.
  THEORY-169's finding that conditioning and per-sequence weight updates
  "differ in what state is kept, not in kind" is the same line drawn in
  attention layers; it is cited as framing, not as evidence.

No status change.
