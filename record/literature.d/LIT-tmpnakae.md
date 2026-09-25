---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-25; not read in full
title: 'Comparing cooperative geometric puzzle solving in ants versus humans'
version: 1
tags:
- complex-systems
- cognition
date: '2026-09-25'
published: '2024-12-23'
doi: '10.1073/pnas.2414274121'
first_author: 'Dreyer'
keywords:
- 'human behavior'
- 'social insects'
- 'collective intelligence'
- 'consensus decisions'
- 'cooperative transport'
implementations: []
summary: >-
  Dreyer et al. (2024), DOI-10.1073/pnas.2414274121. On the same T-shaped load "piano-movers" puzzle, ant groups do better as they get larger, because collective alignment gives them an emergent short-term memory (persistent wall-sliding). Human groups do no better than individuals when they can talk, and worse when communication is restricted, because they fall back on greedy one-shot majority moves.
---

# LIT-tmpnakae: Comparing cooperative geometric puzzle solving in ants versus humans

Tabea Dreyer, Amir Haluts, Amos Korman, Nir Gov, Ehud Fonio, Ofer Feinerman (2024), *Proceedings of the National Academy of Sciences (PNAS) 122(1), e2414274121 (issue 2025-01-07)* — DOI-10.1073/pnas.2414274121

## Key takeaways

- On the same T-shaped load "piano-movers" puzzle, ant groups do better as they get larger, because collective alignment gives them an emergent short-term memory (persistent wall-sliding). Human groups do no better than individuals when they can talk, and worse when communication is restricted, because they fall back on greedy one-shot majority moves.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Whether collective cognition beats individual cognition is hard to test, because groups and individuals usually face different problems. Carrying a large load through a cluttered space is an exception that both people and ants handle alone and in groups. The authors gave the same scaled piano-movers puzzle to single ants, small and large ant groups (longhorn crazy ants), and to single people and groups of people with and without communication. Larger ant groups outperform smaller ones through emergent memory stored in their ordered collective state. Individual humans plan in a reduced state space and beat ants on average, but restricted-communication human groups choose greedy moves and perform worse.

## Standing in the record

Filed from the survey of 2026-09-25 of work the anthology set aside as out of scope (tier B): 290 seconds of active reading over 7 sessions in the papers-feed tracker. `Deferred` because nobody has read it closely here yet, not on merit.

**Priority for a deeper reading: medium — 7 sessions but modest time, and the skim captures the main results. The SI is what remains, and it matters only if the aggregation-mechanism comparison is going to be used.**

What a deeper reading should check:

- A clean empirical case that group performance depends on how heterogeneous the members are and on communication bandwidth, not only on group size. It is relevant to multi-agent and ensemble aggregation analogies (majority vote vs. follow-a-leader).
- Check SI Note 10, which claims random-leader choice is strictly better than majority vote when most individual choices are wrong, and check how the greediness parameter p is fitted.
- The comparison between species relies on the restricted-communication condition to match ant-like force-based communication, so check how fair that match is.

Access when seeded: Crossref metadata (online 2024-12-23) and the full text as Europe PMC XML (PMC11725855, open access), which I read: significance statement, abstract, all results sections, "Comparing Ants and Humans", methods headings and figure captions. The PNAS PDF returned 403. The SI appendix was not read. Keywords are from Europe PMC. Volume 122(1) per Crossref.
