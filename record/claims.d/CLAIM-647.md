---
number: 647
status: Proposed
formerly:
- CLAIM-tmpnwq8a
title: 'Replacing the base model a specialization was learned into can impose a compatibility or transfer cost that shortens the specialization''s useful life, though nothing it encodes has become false: in the trade between learning once and computing on demand, the reader''s turnover is a staleness term of its own, beside the world''s changing; how often the cost binds, and whether it tips the trade toward computing on demand, is empirical'
version: 3
history:
- version: 2
  date: '2026-11-12'
  note: >-
    The cited works were read the same day. IP-Adapter's abstract sentence
    turned out to be about fine-tunes of one base, not a successor base, so
    its reading THEORY-1639 moves from grounds to corroborates, with
    ARG-080 (Rejected) saying why. LoRA's reading THEORY-1640
    becomes the ground of the premise, with ARG-079. defeated_if now
    names CLAIM-074 and CLAIM-118, and the body has a note on why the claim
    does not restate them. Title and status unchanged.
- version: 3
  date: '2026-11-12'
  note: >-
    Narrowed at the owner's review of dmarx/nucleation#482: that a module
    is trained relative to W0 does not show it must be retrained when W0
    changes; transfer may degrade, survive or work well enough. The claim
    now says a replacement can impose a compatibility or transfer cost that
    shortens useful life, and leaves its frequency and its effect on the
    trade to evidence. ARG-079 is weakened to match.
role: thesis
warrant: empirical
defeated_if: >-
  Fine-tuned specializations such as character LoRAs shown to carry over
  to replacement base models generally with no loss of fidelity and no
  added cost, so that a base-model change imposes no transfer cost at all.
  The claim is not defeated by transfer that sometimes works well enough:
  it says a replacement can impose the cost, not that it always does. Also defeated as a claim of its own if it
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
- THEORY-1640
summary: >-
  The assistant's idea, offered at the filing of "Identify Synthesis
  Opportunities" and accepted by the owner. [QUESTION-095](../questions.d/QUESTION-095.md)'s notes found that
  the readings price expected reuse and per-use cost but not staleness or
  the erosion of the alternative. In the owner's case [CASE-235](../cases.d/CASE-235.md), a
  trained character LoRA is tied to the base model it was trained on. When
  the base model is replaced, the LoRA's content is still right about the
  character, but nothing reads it. So the expected reuse that must repay
  the training is cut off at the next replacement. Its premise rests on
  LoRA's structure (THEORY-1640): a module is an update to one set of
  frozen weights. The readings of IP-Adapter, InstantID and PhotoMaker
  corroborate that trained add-ons are scoped to their base's family; none
  tests a successor base, so the claim is a hypothesis until a transfer
  test is in. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-235 CASE-234 — Proposed; filed from the same exchange -->
<!-- inactive-ok-file: THEORY-1639 THEORY-1640 ARG-080 ARG-079 — Proposed; the readings and ARGs filed with this claim's second version -->
<!-- inactive-ok-file: CLAIM-303 — Proposed; the break-even this adds a term to -->

# CLAIM-647: Replacing the base model a specialization was learned into can impose a compatibility or transfer cost that shortens the specialization's useful life, though nothing it encodes has become false: in the trade between learning once and computing on demand, the reader's turnover is a staleness term of its own, beside the world's changing; how often the cost binds, and whether it tips the trade toward computing on demand, is empirical

## The claim

In [CLAIM-303](CLAIM-303.md)'s arithmetic, learning pays when the uses n exceed the
up-front cost over the per-use saving, n > F/(c_r − c_a − u). For a
specialization learned into weights, a replacement of its base model can
cut n off: if the specialization does not carry over, F, or some part of it
spent on transfer, must be paid again. In the limiting case where nothing
carries over, with replacements every T and uses at rate λ, learning pays
only when λT exceeds the break-even, and shorter T favours conditioning on
references at each use. How much carries over to a given successor is the
empirical part.
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
- **The test.** [CASE-234](../cases.d/CASE-234.md)'s design can take one more arm: a LoRA
  trained on one base model, applied to its successor, scored at the same
  fidelity target. The arm measures the transfer cost for that pair: none
  at all, across pairs, would defeat the claim.
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

The seven works registered with [CASE-235](../cases.d/CASE-235.md) were read the same day.

- **IP-Adapter carries less than this claim cited it for.** The abstract's
  "not compatible with other base models" is, by its §1, about the image
  prompt ability not transferring "to the other custom models derived
  from the same text-to-image base models": siblings of one base, not a
  successor. The paper supports only that its own adapter is reusable "on
  custom models fine-tuned from the same base model", so a trained add-on
  is scoped to its base's family. [THEORY-1639](../theory.d/THEORY-1639.md) now corroborates the
  claim instead of grounding it; [ARG-080](../arguments.d/ARG-080.md), Rejected, says the sentence
  does not show reader-replacement staleness.
- **LoRA grounds the premise, as structure** ([THEORY-1640](../theory.d/THEORY-1640.md), [ARG-079](../arguments.d/ARG-079.md)).
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
- **Not a restatement of [CLAIM-118](CLAIM-118.md) or [CLAIM-074](CLAIM-074.md).** In [CLAIM-118](CLAIM-118.md)'s terms a
  kept LoRA is interpreter and a reference image is signal. This claim is
  the cost consequence those claims do not state: a store on the
  interpreter's side is lost with the interpreter, a store on the signal's
  side carries over, and the amortization trade has to price that.
  [THEORY-169](../theory.d/THEORY-169.md)'s finding that conditioning and per-sequence weight updates
  "differ in what state is kept, not in kind" is the same line drawn in
  attention layers; it is cited as framing, not as evidence.

No status change.
