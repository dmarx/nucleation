---
status: Active
status_note: >-
  read in full 2026-10-15 from the publisher's typeset article (Artificial Intelligence
  73 (1995) 31–68), scanned and posted by the author on his UCSD pages (adrenaline.ucsd.edu/kirsh/Articles/Space/intelligent_useof_space.pdf),
  text taken by OCR, with the formulas checked against page images; his HTML pre-publication
  version on the same site was compared and differs in the footnotes and the Tetris
  timings. Worth reading as the standard classification of how people arrange their
  workspace to cut the time and memory a task needs: arrangements that simplify
  choice (hiding or highlighting affordances, eliminating decisions, heuristic cues),
  arrangements that simplify perception (clustering, regions, marking, the vernier
  effect) and spatial dynamics that save internal computation (Tetris rotation).
  It is drawn from observation and anecdote, with no measurements of its own beyond
  the Tetris timings it cites, and it declines to quantify the savings. For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md)
  it shows that the link from informational structuring to amortized computation
  was drawn in 1995, in a footnote to Tarjan and in §3.4's "set-up costs could be
  amortized over the whole task", but as an analogy to self-adjusting structures,
  not to memoization. It also shows that its third category, just-in-time offloading,
  is not amortization at all. For [CASE-tmp9qlz6](../cases.d/CASE-tmp9qlz6.md) and [TERM-tmp5f7cu](../terms.d/TERM-tmp5f7cu.md) it supports the
  gap between presence and finding in time: memory for location is "regularly overestimated",
  a meaningful pre-existing layout helps recall, and retrieval cost matters "in
  absolute time" even where it is a constant factor. It does not cover pre-built
  environments arranged by someone other than the retriever, or failures under a
  deadline.
title: The intelligent use of space
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref
    gives February 1995, so `published:` is the first of the month. Not held in
    the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit
    d1573d2) for the authors and the title found nothing. Read the same day (NOTE-tmplm202).'
tags:
- cognition
- embodied-cognition
date: '2026-10-15'
published: '1995-02-01'
doi: 10.1016/0004-3702(94)00017-U
first_author: Kirsh
keywords:
- spatial arrangement
- external representation
- situated cognition
implementations: []
summary: >-
  Kirsh (1995), Artificial Intelligence 73. A classification, from video of cooks,
  assemblers and baggers, informal observation and the Tetris studies, of how people
  arrange things around them to cut the time and memory a task needs: arrangements
  that simplify choice (hide or highlight affordances, eliminate decisions, offload
  heuristic properties), arrangements that simplify perception (clustering, regions,
  marking, the vernier effect), and spatial dynamics that save internal computation
  (Tetris rotation, self-cueing). It frames the savings in search-complexity terms
  and links informational structuring to amortized computation in a footnote, but
  says the savings cannot in general be meaningfully quantified and offers no cost
  model, no measurements beyond the cited Tetris timings, and no case of an arrangement
  failing under a deadline. Its agents are experts arranging their own workspace
  in the medium and short term; long-term, pre-built environments are set aside.
---

# LIT-tmpvpm24: The intelligent use of space

Kirsh, D. (1995). The intelligent use of space. *Artificial Intelligence* 73(1–2), 31–68. DOI 10.1016/0004-3702(94)00017-U

## Key takeaways

Read in full ([NOTE-tmplm202](../notes.d/NOTE-tmplm202.md)). A classification, from video of cooks, assemblers and baggers, informal observation and the Tetris studies, of how people arrange things around them to cut the time and memory a task needs: arrangements that simplify choice (hide or highlight affordances, eliminate decisions, offload heuristic properties), arrangements that simplify perception (clustering, regions, marking, the vernier effect), and spatial dynamics that save internal computation (Tetris rotation, self-cueing). It frames the savings in search-complexity terms and links informational structuring to amortized computation in a footnote, but says the savings cannot in general be meaningfully quantified and offers no cost model, no measurements beyond the cited Tetris timings, and no case of an arrangement failing under a deadline. Its agents are experts arranging their own workspace in the medium and short term; long-term, pre-built environments are set aside.

## Why this is here

The owner, after the cockpit reading ([LIT-tmpn2s1p](LIT-tmpn2s1p.md)): "amortized retrieval is actually a kind of amortized computation. there's probably a clearer relationship here that I imagine has likely been clarified/formalized at some point in the 30 years since the cockpit essay was published." Registered with six others for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md).

Arranging the environment so a task becomes a perceptual judgement is the cockpit's move, and the EMT case's missing one ([CASE-tmp9qlz6](../cases.d/CASE-tmp9qlz6.md)).
