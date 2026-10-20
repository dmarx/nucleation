---
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

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: 'Listener judgements in reference or signalling games whose alternative utterances and costs are manipulated while the uttered form is held fixed, predicted in advance by the inverted-informative-speaker model with its parameters set before the data are seen, and shown to beat a literal listener with the same prior and a likelihood-only model on unaggregated, trial-level data. A high correlation of condition means with a parameter-free model, which is what exists, cannot settle it.'

# The claim. Repeat it as the body's `# THEORY-tmp6lphc:` heading; the lint checks
# that the two agree.
title: 'Listeners interpret an utterance by inverting a model of a speaker who chooses among alternatives by informativeness, so what a fixed form conveys depends on what else the speaker could have said, as the rational speech act account of Frank, Goodman and coauthors proposes'

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- pragmatics
- linguistics
- cognition
- probabilistic-modeling

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-821
- LIT-816
- LIT-809

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Frank and Goodman (2012), [LIT-821](../literature.d/LIT-821.md), and Goodman and Frank's review (2016), [LIT-816](../literature.d/LIT-816.md), present listener inference as the inversion of an informative speaker, the rational speech act account. The record holds as shown, in [THEORY-172](THEORY-172.md), the fits of that model to mean bets in one-shot reference games and Bergen, Goodman and Levy's signalling-game result. This is the mechanism the fits were offered for, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-172
answers:
- QUESTION-209
---


# THEORY-tmp6lphc: Listeners interpret an utterance by inverting a model of a speaker who chooses among alternatives by informativeness, so what a fixed form conveys depends on what else the speaker could have said, as the rational speech act account of Frank, Goodman and coauthors proposes

## Source

Frank and Goodman (2012, Science), [LIT-821](../literature.d/LIT-821.md), read in [NOTE-634](../notes.d/NOTE-634.md); Goodman and
Frank (2016), [LIT-816](../literature.d/LIT-816.md), read in [NOTE-606](../notes.d/NOTE-606.md); Bergen, Goodman and Levy (2012),
[LIT-809](../literature.d/LIT-809.md), read in [NOTE-613](../notes.d/NOTE-613.md). The papers present the inversion of an
informative speaker as how listeners reason, not only as a model that fits
mean bets.

## What is asserted

That a listener's interpretation of an utterance is the result of
inverting a model of a speaker who chooses among the available
alternatives by informativeness, so that the same form conveys different
things when the alternatives differ.

## What the record holds toward it

[THEORY-172](THEORY-172.md), Active, is the measured part: in Frank and Goodman's one-shot
reference games, mean listener bets matched a parameter-free inversion of
a size-principle speaker with a separately measured salience prior, and
not salience alone; and in Bergen, Goodman and Levy's signalling games with
novel symbols, listeners read a signal as excluding what its available
alternative would have conveyed. [THEORY-472](THEORY-472.md) derives the size-principle
speaker from informative communication. [QUESTION-209](../questions.d/QUESTION-209.md) asks for the decisive
test: alternatives manipulated with the form fixed, parameters set in
advance, trial-level data.

## What this does not say

- Not that comprehension in natural conversation computes the recursion;
  the games fix the alternatives.
- Not that speakers are informative; the model is of the listener's
  assumption about speakers.

## What would confirm or reject it

Confirmed by the promote_when. Rejected if, with alternatives and costs
manipulated and the form held fixed, a literal listener with the same
prior, or a likelihood-only model, predicts trial-level judgements as well
as the inverted speaker.
