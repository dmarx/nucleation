---
number: 235
status: Proposed
formerly:
- CASE-tmp40vka
title: 'Keeping a character consistent in image generation, by training a character LoRA once or by conditioning on reference images at every generation: a 2026 practitioner thread on MiniMax H3, and the earlier generations of the same choice'
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    At the owner's review of dmarx/nucleation#482: the seven method papers
    are no longer listed under reported_in, since none reports the Reddit
    thread or the owner's case; the case came from the owner's U6 and U7.
    Their readings are where the case draws on them (draws_on), now
    including LoRA, DreamBooth and Textual Inversion.
standing: stipulated
kind: specimen
tags:
- learning-theory
date: '2026-11-12'
line:
- distributed-agency
bears_on:
- QUESTION-095
draws_on:
- THEORY-331
- THEORY-1639
- THEORY-1643
- THEORY-1645
- THEORY-1642
- THEORY-439
- THEORY-1640
- THEORY-1644
- THEORY-1641
summary: >-
  The owner's case, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, U6): a Reddit thread in r/StableDiffusion "illustrating how
  changing resource costs changes the incentive to compute on demand or
  learn and amortize via memory". At U7 the owner added that earlier model
  generations can be compared. A's report of the thread (A18) is
  unverified: the thread could not be read here, since it redirected to a
  login page on 2026-11-12. A's history of the generations is checked
  against the arXiv records of the works it names. The case bears on
  [QUESTION-095](../questions.d/QUESTION-095.md), whether storing a result and amortizing a computation are
  one trade, as a domain the question does not yet hold.
---
<!-- inactive-ok-file: THEORY-1639 THEORY-1643 THEORY-1645 THEORY-1642 THEORY-1641 — Proposed; the readings of 2026-11-12, cited in its note -->
<!-- inactive-ok-file: CLAIM-647 — Proposed; filed from the same exchange, cited in its note -->
<!-- inactive-ok-file: THEORY-331 — Proposed; the reading of inference-aware scaling the case is set against -->
<!-- inactive-ok-file: CLAIM-303 — Proposed; the break-even A tied the case to -->
<!-- inactive-ok-file: CASE-234 — Proposed; the study proposed with this case -->

# CASE-235: Keeping a character consistent in image generation, by training a character LoRA once or by conditioning on reference images at every generation: a 2026 practitioner thread on MiniMax H3, and the earlier generations of the same choice

## The case, as the owner gave it

U6: "oh hey, found a nice CASE study illustrating how changing resource
costs changes the incentive to compute on demand or learn and amortize
via memory", with the thread
https://old.reddit.com/r/StableDiffusion/comments/1xqx0jt/minimax_h3_single_frame_edit_excels_at_character/.
U7: "we can also compare and contrast earlier model generations".

The framing is the owner's: a character can be kept consistent either by
learning it once into weights, which is paid for up front and reused, or
by computing it on demand from references at every generation, and which
pays depends on what each costs.

## The thread, as A reported it (unverified)

A18: "The original poster argues that MiniMax H3 can preserve a character
from reference images, reducing the need to train a character-specific
LoRA. Commenters point to the countervailing costs: creating training
images and fitting a LoRA takes work upfront, while reference-based
generation may incur repeated processing costs. One commenter suggests
LoRAs could regain the advantage over many generations; another reports a
much faster reference-sheet workflow for their setup."

None of this is verified. A request to the thread on 2026-11-12 was
redirected to old.reddit.com's login page (`reason=lor2`), and the
attempt stopped there. That H3 is "primarily a video-generation model"
(A18) is also A's, with no source the record can check. Hence the
standing: the referent is real, by the owner's report, and its facts are
assumed here.

A16 drew the distinction the case turns on: "a reusable reference sheet
from a trained LoRA—both are forms of memory, but they move different
amounts of work into each generation."

## The earlier generations (U7), as A tabulated them

A18's correction is that H3 "did not introduce training-free character
references"; the thread is "a new practitioner example of how far that
approach has progressed". A's table, with each work's arXiv record
checked on 2026-11-12 (the works are registered, not read):

| A's generation | how identity is retained | works, first arXiv version |
|---|---|---|
| 2022–23 | learn an embedding or subject-specific weights | Textual Inversion, [LIT-2340](../literature.d/LIT-2340.md) (2022-08-02); DreamBooth, [LIT-2336](../literature.d/LIT-2336.md) (2022-08-25); LoRA, [LIT-2338](../literature.d/LIT-2338.md) (2021-06-17, for language models) |
| 2023–24 | pretrained adapters read reference images | IP-Adapter, [LIT-2342](../literature.d/LIT-2342.md) (2023-08-13); PhotoMaker, [LIT-2339](../literature.d/LIT-2339.md) (2023-12-07, which A puts in 2024); InstantID, [LIT-2341](../literature.d/LIT-2341.md) (2024-01-15) |
| 2025 | image context kept through editing instructions | FLUX.1 Kontext, [LIT-2337](../literature.d/LIT-2337.md) (2025-06-17) |
| 2026 | character sheets given to a reference-conditioned model | MiniMax H3, the thread only |

Two abstracts state the two sides of the trade in their own words.
InstantID's says fine-tuned methods are "hindered by high storage
demands, lengthy fine-tuning processes, and the need for multiple
reference images", while embedding methods need "only a single forward
inference". LoRA's says the adaptation adds "no additional inference
latency". A's caution stands: "These are methodological differences, not
measured performance rankings."

## What it can show

- **A domain for [QUESTION-095](../questions.d/QUESTION-095.md).** The question asks whether leaving a
  result where it can be cheaply retrieved is the same trade as
  amortizing a computation, across a crew's speed bugs, filed arguments
  and reused inferences. Here the same choice is made by practitioners,
  with three options in view: a LoRA (work moved into weights, little per
  use), a reference sheet (made once, read at every use) and raw
  references (nothing kept). The question's note of 2026-10-15 on scaling
  laws says that in the scaling readings "the precomputed thing is a
  cheaper computation, not a stored answer"; a LoRA is that case, and a
  reference sheet is a stored thing interpreted on every use.
- **A practitioner's version of [THEORY-331](../theory.d/THEORY-331.md).** Sardana et al. and Snell et
  al. find that the least-compute way to a fixed quality moves toward
  up-front compute as expected use grows. The thread's commenter who,
  in A's paraphrase, "suggests LoRAs could regain the advantage over many
  generations" states the same dependence on reuse.
- **Why the break-even can move between generations.** In [CLAIM-303](../claims.d/CLAIM-303.md)'s
  arithmetic, learning pays when the uses exceed the up-front cost over
  the per-use saving. Better reference conditioning shrinks the per-use
  saving a LoRA offers, so it raises the number of uses a LoRA must see.
  Whether it has done so is the empirical question [CASE-234](CASE-234.md)
  proposes to measure; A18 declined to assume it.

## What it cannot show

- **Any cost or quality comparison.** A18: "the thread doesn't establish
  a controlled cost-and-quality comparison". The case is a report of
  practitioners' judgements, not a measurement.
- **That reference conditioning is now generally cheaper.** A18
  disclaims it, and so does the case.
- **[CLAIM-303](../claims.d/CLAIM-303.md)'s thesis.** A linked the case to [CLAIM-303](../claims.d/CLAIM-303.md) by `illustrates`
  (A16, A18). [CLAIM-303](../claims.d/CLAIM-303.md)'s thesis is about filing an argument and the
  record's second-occurrence rule; the case shares only its break-even
  arithmetic. So it bears on [QUESTION-095](../questions.d/QUESTION-095.md), which asks whether such
  trades are one, and illustrates no claim.

## Note of 2026-11-12: a staleness term

[CLAIM-647](../claims.d/CLAIM-647.md), the assistant's, proposes a cost the thread's commenters, as A reported them, do not name: a character LoRA is tied to its base model, so a new base model can impose a transfer cost on it. It is Proposed; after the readings and the owner's review it says only that a replacement can impose a compatibility or transfer cost, and rests on LoRA's structure, not on IP-Adapter's sentence.

## Note of 2026-11-12: the works in the table, read

All seven works in the table were read the same day (their NOTEs and
THEORYs are on each LIT).

- **A's 2023 row overstates it for character identity.** IP-Adapter
  ([THEORY-1639](../theory.d/THEORY-1639.md)) reads reference images, but its §5 says "it cannot
  synthesize images that are highly consistent with the subject of a given
  image like some existing methods, e.g., Textual Inversion [51] and
  DreamBooth [52]". Identity-level reference conditioning came with the
  face-ID methods of late 2023 and 2024: PhotoMaker and InstantID. Textual
  Inversion's authors also disclaim identity for 2022: "our model does not
  currently preserve identity to the extent where this is a concern"
  ([THEORY-1641](../theory.d/THEORY-1641.md)).
- **The trade, measured once, on one base, by an interested party.**
  PhotoMaker's Table 1 ([THEORY-1645](../theory.d/THEORY-1645.md)), on a V100 for SDXL: DreamBooth
  1284 s and Textual Inversion 2400 s per subject, against IP-Adapter 12 s
  and PhotoMaker 10 s; face similarity 49.8, 54.3, 67.1 and 61.8; DINO
  39.8, 39.3, 46.2 and 51.5. The text of its §4.2 claims "the largest
  CLIP-T and DINO scores"; by the table the largest CLIP-T is DreamBooth's
  (29.8 against 26.1), so the table is cited, not the sentence.
- **Parity with character LoRAs, claimed without a measure.** InstantID
  ([THEORY-1643](../theory.d/THEORY-1643.md)) compares itself with two community character LoRAs by
  figure only: "We can achieve competitive results as LoRAs without any
  training." Its abstract's "only a single forward inference" describes
  earlier ID-embedding methods, which InstantID joins; the case's sentence
  above attributes it so.
- **A's genealogy is the field's own.** FLUX.1 Kontext ([THEORY-1642](../theory.d/THEORY-1642.md))
  offers personalization "without the need for finetuning [43] or LoRA
  training", and names IP-Adapter among the "Early works on such
  training-free subject-driven image synthesis".
- **Both routes have a learned part.** The trained route learns per
  character, by the user; the reference route learns once, by the
  module's maker (8 A100s for two weeks for PhotoMaker; 48 H800s for
  InstantID), and every user then pays only per use. A16's "both are forms
  of memory" holds; they differ in who trains and how often.
- **The record held an analogue it did not cite.** [THEORY-439](../theory.d/THEORY-439.md) ([LIT-796](../literature.d/LIT-796.md))
  finds for language models that the same few demonstrations used as
  context and used to update weights temporarily "are not
  interchangeable". It is the trained-against-conditioned comparison in
  another domain, and the case now draws on it.
