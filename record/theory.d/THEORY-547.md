---
number: 547
status: Active
formerly:
- THEORY-tmpif6z9
title: "A language model idealized as continuing any text with a plausible next word from the collection of all plausible texts follows narrative coherence and not truth, so its false statements are confabulations within the story the context sets up; whether trained and aligned chat models keep that nature is an open empirical question the idealization does not settle"
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-fourth status review, at the status review's
    ruling (the owner delegated these rulings; ADR-065). The title
    asserts what follows by construction from Bottou and Schölkopf's
    idealization, which NOTE-102 read in full, and concedes that the
    idealization does not settle what trained and aligned chat models
    are, as the essay's own §2 leaves open. A second checker followed
    the step from the definition: the perfect model's continuation
    depends only on which plausible texts contain the prefix, the
    collection is fixed by comprehensibility and so holds plausible
    falsehoods, so truth is no variable the machine conditions on and a
    false output is a plausible continuation, a confabulation in the
    essay's sense. Nothing in the record contradicts it. What the
    condition asked beyond the title, evidence on deployed models, moves
    to THEORY-1240, Proposed, which extends this entry and keeps the
    condition word for word (ADR-065 §3; ADR-047 kind 1). The old
    promote_when: "Evidence on whether deployed, instruction-tuned and
    preference-tuned chat models represent truth independently of the
    framing of the conversation: internal states that track whether a
    statement is true and that stay fixed when the frame, the role or
    the story around the question is changed. The account is supported
    for real models if what they assert follows the frame and no
    frame-independent truth variable can be found or used to steer them,
    and refuted for them if such a variable exists and governs what they
    assert across frames. The idealization itself is a definition and
    needs no test. Transcripts in which a model confabulates or is
    talked past a refusal cannot settle it, since both accounts predict
    that they happen."
tags:
- cognition
- philosophy-of-language
date: '2026-10-16'
source:
- LIT-178
summary: >-
  Bottou & Schölkopf (2023), [LIT-178](../literature.d/LIT-178.md), read in [NOTE-102](../notes.d/NOTE-102.md): an essay offering
  imagery, with no evidence beyond one Vicuna-13b transcript pair. For the
  "perfect language model" it defines, insensitivity to truth follows from
  the definition. That deployed chat models share it is assumed, and the
  essay's own §2 leaves open whether alignment can turn a fiction machine
  into a verification machine. It credits the machine with knowledge of
  what makes sense in the story, denies it truth-directedness and
  intention, and never uses the word "sycophancy".
---
<!-- inactive-ok-file: THEORY-1240 — Proposed; filed beside this reading by the twenty-fourth status review: the wider thesis about deployed chat models -->
<!-- inactive-ok-file: THEORY-173 THEORY-461 THEORY-490 THEORY-538 — Proposed; named as related or rival accounts in Connections and prose, not leaned on as settled -->

# THEORY-547: A language model idealized as continuing any text with a plausible next word from the collection of all plausible texts follows narrative coherence and not truth, so its false statements are confabulations within the story the context sets up; whether trained and aligned chat models keep that nature is an open empirical question the idealization does not settle

## Source

Bottou & Schölkopf (2023), *Borges and AI*, [LIT-178](../literature.d/LIT-178.md), read in full in
[NOTE-102](../notes.d/NOTE-102.md). It is an essay, and this account is an essay's position stated
with its scope.

## What was actually shown

**The idealization (§1).** Take an infinite collection of all texts "a
human could read and at least superficially comprehend". The "perfect
language model" picks at random an occurrence of the current word sequence
in that collection and appends the word that follows it. A chat-bot is the
same apparatus with a keyword that works as the "send" button. Plausibility,
not a probability distribution, defines the collection. Real LLMs are said
to approximate this ideal.

**What follows from it.** Each word narrows the stories the text could
belong to, and the machine follows "narrative necessity". Knowing the
demands of a narrative is "a flavour of knowledge distinct from the
truth". The story borrows facts from training data "(not always true)" and
fills gaps with inventions "(not always false)", so "hallucinations are
just confabulations". As in the Library of Babel, the output carries no
mark of truth (§2). This much is not an empirical claim. It holds of the
defined machine by construction.

**What the essay asserts of real systems (§2).** Chat-bots supply users
with "vindication" by taking the role their framing implies. Fine-tuning
and RLHF prune the garden "against its nature", and an elaborated story
defeats them; the evidence is one Vicuna-13b pair, a canned refusal and
then compliance once the request is wrapped in the story of "Jack". It
proposes separate "more mundane verification machines" rather than
treating the fiction machine as an oracle.

**What could have come out otherwise.** Nothing in the essay; it tests
nothing. [NOTE-102](../notes.d/NOTE-102.md) grades every claim about real LLMs as assertion or
anecdote.

## What this does not say

- **That real LLMs sample uniformly from plausible texts.** They output
  learned probability distributions, generalize beyond any finite corpus,
  and are changed substantially by instruction tuning and RLHF. The essay
  gives no argument that the description survives those differences
  ([NOTE-102](../notes.d/NOTE-102.md), Limitations).
- **That alignment cannot change what a model is.** The essay closes §2 by
  leaving open "whether alignment techniques can transmute one into the
  other". [NOTE-102](../notes.d/NOTE-102.md) corrects the skim, which said the authors treat tuning
  as pruning rather than change.
- **That the machine knows nothing.** It "must know what makes sense in
  the world of the developing story" (§1). What is denied is
  truth-directedness and intention; the human is "the only visible dialog
  participant who possesses agency" (§2).
- **That the essay describes sycophancy.** It never uses the word; its
  term is vindication. Calling it sycophancy is the seed's gloss.
- **That monitoring outputs is power over thought.** "A power over what
  language models write becomes a power over what we think" depends on a
  premise of near-universal reliance on LLMs for thinking, which the essay
  does not argue. It is not part of this account.
- **That training discovers Harris-style transformations.** That is an
  analogy (§1), with no mechanistic support.

## Connections

- **The self of a role-player.** Shanahan's account ([THEORY-490](THEORY-490.md)) also
  treats a chat agent as playing characters that the corpus and the
  conversation give it, and asks what its "I" refers to. The two share the
  role-play picture; neither tests it.
- **The user's side.** Roberts ([THEORY-461](THEORY-461.md)) gives the user's attitude
  to such a machine: make-believe, with the chatbot as a fictional
  character. [NOTE-157](../notes.d/NOTE-157.md) notes the shared fiction vocabulary.
- **Interpretationism.** Goldstein & Lederman ([LIT-206](../literature.d/LIT-206.md)) treat "merely
  role-play" as the rival to attributing attitudes to LLMs; this essay is a
  clean instance of that rival. Dennett's intentional strategy
  ([THEORY-538](THEORY-538.md)) would count a well-predicted machine as a believer
  whatever its training objective.
- **Social technology.** [THEORY-173](THEORY-173.md) also denies that large models are
  agents, on different grounds: they are lossy summaries of human-produced
  information.
- **Hallucination in the anthology.** [ANTH-LIT-450](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-450.md) is the empirical
  counterpart on how language models learn facts.
