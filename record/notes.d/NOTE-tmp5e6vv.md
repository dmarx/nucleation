---
status: Skimmed
paper: LIT-tmpobt23
title: 'Bottou & Schölkopf — Borges and AI'
version: 1
date: '2026-09-26'
summary: >-
  A (perfect) language model is best understood not through science-fiction imagery of sentient machines but as Borges's Garden of Forking Paths — a fiction machine that follows narrative necessity with no regard for truth or intention — which reframes hallucination, sycophancy and alignment.
---

<!-- inactive-ok-file: LIT-tmpobt23 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmp5e6vv: Bottou & Schölkopf — Borges and AI

## Contribution

Public debate about LLMs, for and against, draws on science-fiction imagery: sentient machines rebelling, paperclip apocalypses. The authors ask whether that imagery describes the phenomenon well at all, and compare it to explaining weather through the moods of the gods. They propose instead to understand LLMs, and their relation to AI, through Jorge Luis Borges's fiction. This yields a different view of how language modelling relates to artificial intelligence.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (About LLMs): a "perfect language model" is an apparatus that extends a tape by sampling continuations from the infinite collection of all plausible texts. That is Ts'ui Pen's book in The Garden of Forking Paths, and a chat-bot is the same thing with a turn-taking token. Training is glossed as discovering Harris-style transformations and basic forms.
- §1: neither truth nor intention matters to the machine, only narrative necessity. Recognizing narrative demands is a kind of knowledge distinct from truth, and "hallucinations are just confabulations".
- §2 (The Librarians), via The Library of Babel: seeking vindication from a chat-bot is "easy and yet equally vain". Completions take on the role the user's framing implies (the professor–student example), and asking about sentience draws on science-fiction training data. The delusion that LLMs are encyclopaedic, flawless AIs feeds on that vindication.
- §2: the "Purifiers" (content restriction) and those who want a tame, world-anchored assistant both try to prune the forking garden, through fine-tuning and RLHF. Vicuna-13b transcripts show a refusal being bypassed by a more elaborate story. Monitoring and steering outputs would confer "power over what we think".
- §3 (Storytime): rewinding and resampling a model is not time travel for us. The better comparison for LLMs is storytelling rather than the printing press.

## Open questions

- A widely cited framing (LLM as a fiction or role-play machine) with direct bearing on how the anthology describes hallucination, sycophancy and jailbreaks. It pairs with simulator and role-play framings in the ML literature.
- It is an essay, not an argument with evidence. Check whether its "perfect language model" idealization survives instruction tuning and RLHF, which the authors treat as pruning rather than changing the model's nature.
- Check for later work by the authors developing the view.
