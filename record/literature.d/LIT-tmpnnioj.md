---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpqpqoq](../notes.d/NOTE-tmpqpqoq.md)); worth reading as the source of the "Blockhead": a machine that stores every sensible hour-long conversation and so has the capacity to pass any Turing test of that length, yet "has the intelligence of a toaster". The argument refutes behaviourist sufficient conditions for intelligence, including a capacity version that survives the standard objections, and establishes psychologism: whether behaviour is intelligent depends partly on the processing that produces it. It does not say which processing is required, only that it needs some "richness", and the closing case against simulators of physics, neurons or psychology is admitted to be a sketch.'
title: 'Psychologism and Behaviorism'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the JSTOR scan Block links from his own publications
    page (nedblock.us/publications, a Google Drive file), pp. 5–43 with
    text layer, notes 1–31 included. Crossref confirms The Philosophical
    Review 90(1), January 1981, first page 5, DOI 10.2307/2184371, sole
    author Ned Block; `published:` is the first of January. Reprinted in
    Shieber (ed.), The Turing Test (MIT Press, 2004), pp. 229–266, DOI
    10.7551/mitpress/6928.003.0032, not seen. Not held in the Anthology of
    the SOTA: a grep of its record for "Block", "psychologism",
    "Blockhead" and the title found nothing.
tags:
- cognition
- metaphysics
- anthology-candidate
date: '2026-10-03'
published: '1981-01-01'
doi: '10.2307/2184371'
first_author: 'Block'
keywords:
- 'psychologism'
- 'behaviorism'
- 'Turing test'
- 'neo-Turing test conception of intelligence'
- 'Blockhead'
- 'string-searching machine'
- 'behavioral disposition'
- 'behavioral capacity'
- 'combinatorial explosion'
- 'perfect actor'
implementations: []
extends:
- LIT-407
corrects:
- LIT-394
summary: >-
  Block (1981), The Philosophical Review 90(1):5–43. Psychologism, the
  doctrine that whether behaviour is intelligent depends on the information
  processing that produces it, is true. A machine that stores all sensible
  conversations of a test's length and looks up its replies has the
  capacity to respond sensibly to any sequence of inputs, so it satisfies
  the strongest behaviourist conception of intelligence, yet all its
  intelligence is its programmers'. The standard objections to behaviourism
  (Chisholm–Geach, the perfect actor, paralytics) defeat behaviourist
  necessary conditions but not sufficient ones; this machine defeats the
  sufficient condition. Psychologism is not chauvinism: it excludes one kind
  of processing without requiring ours.
---
<!-- inactive-ok-file: LIT-419 — Deferred: Lycan's paper is unread; cited for what Block himself reports of it in n. 30 -->
<!-- inactive-ok-file: THEORY-023 — Proposed; named as the account whose behavioural half this paper is the classic source for, no relation claimed -->

# LIT-tmpnnioj: Psychologism and Behaviorism

Ned Block (1981), *The Philosophical Review* 90(1), January 1981,
pp. 5–43 — DOI-10.2307/2184371.

The brief's citation (Phil Rev 90, 1981) is correct; the scan runs from
p. 5 to p. 43, which matches the reference Block gives in [LIT-tmp5vkka](LIT-tmp5vkka.md).

## Key takeaways

- **Psychologism** is "the doctrine that whether behavior is intelligent
  behavior depends on the character of the internal information processing
  that produces it" (p. 5). Two systems could be exactly alike in actual and
  potential behaviour, dispositions, capacities and behavioural
  counterfactuals, and differ in processing so that "one is not at all
  intelligent while the other is fully intelligent".
- **The target is the strongest behaviourist conception Block can build.**
  He grants that "sensible" can be defined behaviouristically (p. 11), then
  replaces Turing's judge with the *neo-Turing Test conception*:
  intelligence "is the capacity to produce a sensible sequence of verbal
  responses to a sequence of verbal stimuli, whatever they may be"
  (p. 18). The move from disposition to capacity disarms the
  Chisholm–Geach, perfect-actor and paralytic objections, which only ever
  told against behaviourist *necessary* conditions (pp. 14–19).
- **The machine (pp. 19–21).** List every typable string of an hour's
  conversation in which one party is sensible; the machine finds the
  strings that begin with the conversation so far and types the next
  sentence. A tree-searching variant stores one reply per branch. It has the
  capacity the conception requires, "But actually, the machine has the
  intelligence of a toaster. All the intelligence it exhibits is that of its
  programmers" (p. 21). It needs only logical possibility (Objection 6),
  though Block argues it may be nomologically possible too.
- **Psychologism is not chauvinism** (pp. 6, 21): it "requires only that
  intelligent behavior not be the product of a (at least one) certain kind
  of internal processing", so Martians with very different but rich
  processing still count as intelligent.
- **Patching the test concedes the point.** Requiring that the system "avert
  exponential explosion of search" (Dennett's amendment, n. 29) is itself a
  condition on processing, hence psychologistic, and it faces a dilemma:
  "postponing" lets the machine in, "avoiding" may exclude us (pp. 38–40).

## Standing in the record

Filed on 2026-10-03 at the owner's request, with Block's other papers on
functionalism, meaning, AI and perception. It is a philosophical argument
about the concept of intelligence, and no anthology topic holds that
question as such.

**Flagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)).** Its central claim, that a
behavioural test of any length can be passed by stored responses and so
cannot certify intelligence without a claim about how the responses are
produced, is a claim about "what a measurement cannot tell you", which is
how the anthology's `analysis-and-evaluation` topic describes itself. It
carries no instruction for practice, and the reading here is about the
nature of intelligence, so it stays here. Whether the anthology wants it as
a source on memorisation and behavioural evaluation is the question the
flag asks.

**Relations declared.**

- `extends:` [LIT-407](LIT-407.md). Note 17 says "A version of this machine was sketched
  in my 'Troubles with Functionalism'", and [NOTE-366](../notes.d/NOTE-366.md) records that sketch:
  a list-searcher over all "smart speakable strings" that "clearly has no
  mental states at all" (pp. 294–295 of [LIT-407](LIT-407.md)). This paper develops it
  into a full argument against behaviourism about intelligence, and n. 30
  defends [LIT-407](LIT-407.md)'s homunculi-head intuition against Lycan.
- `corrects:` [LIT-394](LIT-394.md). Block quotes Turing (n. 13) settling for passing the
  imitation game as a *sufficient* condition of thinking ("we need not be
  troubled by this objection"), and the machine is a counterexample to
  exactly that condition, in its strongest capacity form. [NOTE-355](../notes.d/NOTE-355.md) reads
  Turing's paper itself.

**Where it bears.**

- *Searle* ([LIT-400](LIT-400.md), [NOTE-349](../notes.d/NOTE-349.md)). Note 30 notes that Searle's forthcoming
  Chinese room uses "an example of the same sort as mine", a person
  following a manual in a language they do not understand, and rejects
  Searle's wider conclusion: "some symbol-manipulating homunculi-heads are
  intelligent", and what disqualifies the one described is that "the causal
  relations among their states do not mirror the causal relations among our
  mental states".
- *Dennett* ([LIT-440](LIT-440.md), [LIT-398](LIT-398.md)). Dennett is named as close to a behaviourist
  analysis of intelligence (n. 12) and as the advocate of the
  exponential-explosion amendment (n. 29); this is the record's statement of
  the position his intentional-system view is pressed with.
- *Lycan* ([LIT-419](LIT-419.md), Deferred). Note 30 is the record's only first-hand
  report of what "Form, Function, and Feel" argues, in Block's words: that
  the intuition that a homunculi-head lacks qualia "could be made to go away
  by imagining yourself reduced to the size of a molecule", and is "an
  illusion produced by missing the forest for the trees". Block's reply is a
  single-homunculus variant where no such illusion can operate. This is
  Block's report of Lycan, not a reading of Lycan.
- *AI consciousness* ([THEORY-023](../theory.d/THEORY-023.md); Butlin et al., [LIT-056](LIT-056.md), [NOTE-052](../notes.d/NOTE-052.md)).
  [THEORY-023](../theory.d/THEORY-023.md)'s behavioural half says mimicry undercuts behavioural evidence,
  and [NOTE-052](../notes.d/NOTE-052.md) records Butlin et al. discounting behavioural tests because
  systems can be trained to mimic. This paper is the classic argument that
  mimicry by stored response defeats a behavioural *sufficient* condition
  for intelligence. It is about intelligence, not consciousness, and its
  machine is a lookup table, not a trained network, so it supports
  [THEORY-023](../theory.d/THEORY-023.md)'s premise by analogy only.
