---
status: Proposed
title: 'Keeping a character consistent in image generation, by training a character LoRA once or by conditioning on reference images at every generation: a 2026 practitioner thread on MiniMax H3, and the earlier generations of the same choice'
version: 1
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
reported_in:
- LIT-tmp5b18b
- LIT-tmp3pjii
- LIT-tmpiyr8q
- LIT-tmptzx4q
- LIT-tmp8l2rx
- LIT-tmpp8vh8
- LIT-tmp4meti
summary: >-
  The owner's case, from the exchange "Identify Synthesis Opportunities"
  (2026-11-08, U6): a Reddit thread in r/StableDiffusion "illustrating how
  changing resource costs changes the incentive to compute on demand or
  learn and amortize via memory". At U7 the owner added that earlier model
  generations can be compared. A's report of the thread (A18) is
  unverified: the thread could not be read here, since it redirected to a
  login page on 2026-11-12. A's history of the generations is checked
  against the arXiv records of the works it names. The case bears on
  QUESTION-095, whether storing a result and amortizing a computation are
  one trade, as a domain the question does not yet hold.
---
<!-- inactive-ok-file: THEORY-331 — Proposed; the reading of inference-aware scaling the case is set against -->
<!-- inactive-ok-file: CLAIM-303 — Proposed; the break-even A tied the case to -->
<!-- inactive-ok-file: LIT-tmp5b18b LIT-tmp3pjii LIT-tmpiyr8q LIT-tmptzx4q LIT-tmp8l2rx LIT-tmpp8vh8 LIT-tmp4meti — Deferred; registered with this case, not read -->
<!-- inactive-ok-file: CASE-tmp3isyl — Proposed; the study proposed with this case -->

# CASE-tmp40vka: Keeping a character consistent in image generation, by training a character LoRA once or by conditioning on reference images at every generation: a 2026 practitioner thread on MiniMax H3, and the earlier generations of the same choice

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
| 2022–23 | learn an embedding or subject-specific weights | Textual Inversion, LIT-tmpiyr8q (2022-08-02); DreamBooth, LIT-tmp3pjii (2022-08-25); LoRA, LIT-tmp5b18b (2021-06-17, for language models) |
| 2023–24 | pretrained adapters read reference images | IP-Adapter, LIT-tmptzx4q (2023-08-13); PhotoMaker, LIT-tmp8l2rx (2023-12-07, which A puts in 2024); InstantID, LIT-tmpp8vh8 (2024-01-15) |
| 2025 | image context kept through editing instructions | FLUX.1 Kontext, LIT-tmp4meti (2025-06-17) |
| 2026 | character sheets given to a reference-conditioned model | MiniMax H3, the thread only |

Two abstracts state the two sides of the trade in their own words.
InstantID's says fine-tuned methods are "hindered by high storage
demands, lengthy fine-tuning processes, and the need for multiple
reference images", while embedding methods need "only a single forward
inference". LoRA's says the adaptation adds "no additional inference
latency". A's caution stands: "These are methodological differences, not
measured performance rankings."

## What it can show

- **A domain for QUESTION-095.** The question asks whether leaving a
  result where it can be cheaply retrieved is the same trade as
  amortizing a computation, across a crew's speed bugs, filed arguments
  and reused inferences. Here the same choice is made by practitioners,
  with three options in view: a LoRA (work moved into weights, little per
  use), a reference sheet (made once, read at every use) and raw
  references (nothing kept). The question's note of 2026-10-15 on scaling
  laws says that in the scaling readings "the precomputed thing is a
  cheaper computation, not a stored answer"; a LoRA is that case, and a
  reference sheet is a stored thing interpreted on every use.
- **A practitioner's version of THEORY-331.** Sardana et al. and Snell et
  al. find that the least-compute way to a fixed quality moves toward
  up-front compute as expected use grows. The thread's commenter who,
  in A's paraphrase, "suggests LoRAs could regain the advantage over many
  generations" states the same dependence on reuse.
- **Why the break-even can move between generations.** In CLAIM-303's
  arithmetic, learning pays when the uses exceed the up-front cost over
  the per-use saving. Better reference conditioning shrinks the per-use
  saving a LoRA offers, so it raises the number of uses a LoRA must see.
  Whether it has done so is the empirical question CASE-tmp3isyl
  proposes to measure; A18 declined to assume it.

## What it cannot show

- **Any cost or quality comparison.** A18: "the thread doesn't establish
  a controlled cost-and-quality comparison". The case is a report of
  practitioners' judgements, not a measurement.
- **That reference conditioning is now generally cheaper.** A18
  disclaims it, and so does the case.
- **CLAIM-303's thesis.** A linked the case to CLAIM-303 by `illustrates`
  (A16, A18). CLAIM-303's thesis is about filing an argument and the
  record's second-occurrence rule; the case shares only its break-even
  arithmetic. So it bears on QUESTION-095, which asks whether such
  trades are one, and illustrates no claim.
