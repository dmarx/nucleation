---
number: 816
# Don't copy this file by hand — run `luria new theory`, which assigns the
# code and fills in what a machine can compute.
#
# A theory is a claim about WHY something happens, or about what is true of
# these systems. State it as a finding, not as an instruction: "Batch
# normalization helps by smoothing the optimization landscape" rather than
# "Use batch normalization". If what you are about to write tells the reader
# what to do in machine learning, it is a practice, and it belongs in the
# Anthology of the SOTA (ANTH-ADR-031).

# Active | Proposed | Deferred | Superseded | Rejected, optionally " — note".
# What each one means here is in luria.yaml, and it is NOT what the same word
# means on a practice: this status says whether the record believes the
# ACCOUNT, and an explanation can be `Rejected` while the thing it explained
# goes on working exactly as well as it ever did.
status: 'Proposed'
formerly:
- THEORY-tmpcgnmv

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: 'A word-learning experiment whose displays make an informative-speaker learner and a plain size-principle learner predict different bets, for example vague intended meanings, non-uniform literal meanings, or a speaker the learner knows to be uninformative, with both models and a frequency baseline fitted on part of the data and tested on the rest. It is promoted if the informative-speaker model wins on held-out displays. It is refuted if the plain size-principle learner does as well where they differ. Further correlations of condition means with a parameter-free model, in displays where the two coincide, cannot settle it.'

# The claim. Repeat it as the body's `# THEORY-816:` heading; the lint checks
# that the two agree.
title: 'Learners inferring what a novel word means from its use reason about a speaker who chose the word to be informative about the referent, so the size principle in word learning is a consequence of that inference and not a separate rule of generalisation'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- pragmatics
- cognition
- probabilistic-modeling

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-824

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Frank, Goodman, Lai and Tenenbaum (2009), [LIT-824](../literature.d/LIT-824.md), read in [NOTE-627](../notes.d/NOTE-627.md), derive the size principle from an informative speaker and present the word learner as inverting that speaker. The record holds as shown, in [THEORY-472](THEORY-472.md), the derivation and one experiment in which mean bets matched the inversion; in those displays an informative-speaker learner and a plain size-principle learner coincide, so whether learners reason about the speaker is open. [THEORY-785](THEORY-785.md) is the same inversion for listeners in reference games.
extends:
- THEORY-472
answers:
- QUESTION-167
---
<!-- inactive-ok-file: THEORY-785 — Proposed; the listener-side counterpart of this thesis, cited to say how the two differ -->


# THEORY-816: Learners inferring what a novel word means from its use reason about a speaker who chose the word to be informative about the referent, so the size principle in word learning is a consequence of that inference and not a separate rule of generalisation

## Source

Frank, Goodman, Lai and Tenenbaum (2009), [LIT-824](../literature.d/LIT-824.md), read in full in
[NOTE-627](../notes.d/NOTE-627.md). They write the informative speaker down (utility −D_KL from the
intended to the literal meaning), derive the size principle from it, and
present the learner as inverting that speaker: a learner who sees a
speaker point at the one red circle among blue shapes and say a novel
word should lean towards "red", because "red" singles the object out.
The size principle, justified elsewhere as a rule about generalisation,
"here becomes a consequence of the speaker's goal" ([NOTE-627](../notes.d/NOTE-627.md), claim C2).

## What is asserted, and by whom

The thesis is that learners who infer a novel word's meaning from its
use reason about a speaker who chose the word to be informative about
the referent, so the size principle in word learning is a consequence of
that pragmatic inference and not a separate rule of generalisation.
Frank, Goodman, Lai and Tenenbaum propose it.

## What the record holds toward it

- [THEORY-472](THEORY-472.md) (Active): the derivation (for a point referent and uniform
  literal meanings, word choice ∝ |extension|^(−α)), and, in one betting
  experiment, mean bets in line with the inverted speaker (r = .93 on
  condition means).
- In those displays the informative-speaker learner and a plain
  size-principle learner coincide by construction, so the fit does not
  separate this thesis from the rule it would explain.
- [THEORY-785](THEORY-785.md) states the same inversion for listeners interpreting
  utterances in reference games, from the rational speech act papers;
  this entry is its word-learning counterpart.

## What this does not say

- Not that speakers are informative. In the paper's free-description
  study speakers followed informativeness only weakly (r = .19), and
  colour terms not at all; the thesis is about the learner's assumption.
- Not that children learn this way; the participants were adults on the
  web.

## What would confirm or reject it

Confirmed by the promote_when: displays in which the two learners
predict different bets, with both models and a frequency baseline fitted
on part of the data and tested on the rest, and the informative-speaker
learner winning. Rejected if the plain size-principle learner does as
well where they differ. [QUESTION-167](../questions.d/QUESTION-167.md) asks the same thing as a question;
this entry is the answer the authors propose.
