---
number: 827
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
- THEORY-tmppz903

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "A first-hand reading of a rubber hand study in which participants' expectations of the synchronous and comparison conditions are measured in the stimulated participants themselves and matched by design, or shown equal with a Bayes factor, and in which the synchrony difference in referred touch and in ownership survives, each item reported on its own with trait suggestibility as a covariate. Surviving trait suggestibility alone does not meet this: the reply of Lush and Seth shows that a synchrony effect unrelated to suggestibility is also what unequal but uniform expectations predict. It is refuted if, with expectations matched, synchronous and comparison brushing no longer differ on the ownership item; the referred-touch clause is refuted if they no longer differ on it either. A further replication with only control statements or an asynchronous condition as its control cannot settle it, and neither can drift."

# The claim. Repeat it as the body's `# THEORY-827:` heading; the lint checks
# that the two agree.
title: "The rubber hand illusion is a perceptual illusion driven by multisensory integration: the difference in reports between synchronous and asynchronous brushing is produced by the stimulation, not by participants' expectations"

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- self
- neuroscience
- embodied-cognition

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-1264
- LIT-1268

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Ehrsson et al. (2022), [LIT-1264](../literature.d/LIT-1264.md), read in
  [NOTE-997](../notes.d/NOTE-997.md), conclude that the rubber hand illusion is a perceptual illusion
  driven primarily by multisensory mechanisms ([NOTE-997](../notes.d/NOTE-997.md), C8), from the synchrony difference's
  independence of hypnotisability in Lush et al.'s 353 participants. Lush and
  Seth's reply, [LIT-1267](../literature.d/LIT-1267.md), shows that uniform but unequal expectations predict the
  same null. The record holds as shown, in [THEORY-766](THEORY-766.md), only the report
  differences and that the standard controls do not equalise expectations. This
  is the perceptual reading, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when that narrowing set it
  aside.
extends:
- THEORY-766
---
<!-- inactive-ok-file: THEORY-769 — Proposed; the inference account named in Connections, not leaned on -->
<!-- inactive-ok-file: THEORY-765 — Rejected; the earlier stimulation account this one does not revive, named -->

# THEORY-827: The rubber hand illusion is a perceptual illusion driven by multisensory integration: the difference in reports between synchronous and asynchronous brushing is produced by the stimulation, not by participants' expectations

## Source

Ehrsson et al. (2022), [LIT-1264](../literature.d/LIT-1264.md), read in full in [NOTE-997](../notes.d/NOTE-997.md), claim C8, which
[NOTE-997](../notes.d/NOTE-997.md) rates weak as an inference from the comment: it rests on the
difference's independence of hypnotisability (C1, C3) and on the
asynchronous condition being a valid control (C6), and C6 is the point in
dispute.

## What is asserted

That the synchronous-minus-asynchronous difference in referred-touch and
ownership reports is produced by the multisensory stimulation itself, so
that it would survive if participants' expectations of the two conditions
were equal.

## What the Active entry establishes toward it

[THEORY-766](THEORY-766.md) holds that the report difference replicates across studies, that
the ownership report is the weaker and less reliable one, that drift is not
a measure of the reports, and that the standard controls leave expectations
unequal (d = 1.40 and 1.05 in unstimulated observers, Lush 2020). It does
not decide between stimulation and expectation as the cause.

## What would confirm or reject it

The promote_when, inherited unchanged from [THEORY-766](THEORY-766.md): a first-hand reading
of a study that measures and matches the stimulated participants'
expectations of the two conditions and finds the synchrony difference
surviving, each item reported on its own with trait suggestibility as a
covariate. It is refuted if, with expectations matched, the conditions no
longer differ on the ownership item.

## What this does not say

- **It does not say the reports are not influenced by suggestion.** Ehrsson
  et al. found hypnotisability unrelated to the difference, not to the
  ratings, which it does predict.
- **It does not revive drift as a measure.** That clause of [THEORY-765](THEORY-765.md) failed
  its own refutation condition and stays failed.
- **It is not the inference account.** [THEORY-769](THEORY-769.md) explains ownership as a
  graded belief about a common cause; that is compatible with either
  answer here.
