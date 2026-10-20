---
number: 826
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
- THEORY-tmpkn062

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "For the clause on mood: a second experiment, with a manipulated source of displayed mood, run in groups that differ from Barsade's in the way that most threatens the claim. That means ongoing teams rather than ad hoc student groups, several confederates rather than one actor, and mood measured during the interaction rather than recalled afterwards. The clause holds if members' mood again moves with the source's valence on a measure independent of self-report. For the clause on group process: a design in which process outcomes (cooperation, conflict) are compared across the manipulated conditions, or contagion is manipulated and the process measured, rather than regressing process on measured contagion. It is refuted if the manipulated conditions spread mood but leave cooperation and conflict unchanged, which would mean the correlations were carried by a third factor, such as members' own reaction to the task. For the clause on awareness: a designed test of whether members attribute their judgments of the group and of themselves to mood they caught. The published version of the article (ASQ 47(4)) should also be read, since every number here is from the 2001 manuscript and may have changed. More correlational field studies of mood convergence cannot settle the causal clauses."

# The claim. Repeat it as the body's `# THEORY-826:` heading; the lint checks
# that the two agree.
title: "In work groups, a member's displayed mood spreads to the others, and pleasant emotional contagion improves the group's cooperation and reduces its conflict"

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- emotion-and-affect
- social-science

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-706

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Barsade (2002), [LIT-706](../literature.d/LIT-706.md), read in [NOTE-551](../notes.d/NOTE-551.md), presents emotional contagion as a
  general phenomenon of work groups and states its effect on group process
  causally: "this contagion improved cooperation, decreased conflict". The
  record holds as shown, in [THEORY-123](THEORY-123.md), only what her two studies measured:
  ad hoc student groups, one actor as the source, and a process link that is a
  correlation with measured contagion. This is her wider claim, filed under
  [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-123
---
<!-- inactive-ok-file: THEORY-126 — Proposed; the convergence account named in Connections, not leaned on -->

# THEORY-826: In work groups, a member's displayed mood spreads to the others, and pleasant emotional contagion improves the group's cooperation and reduces its conflict

## Source

Barsade (2002), [LIT-706](../literature.d/LIT-706.md), read in full in [NOTE-551](../notes.d/NOTE-551.md) from the August 2001
manuscript. Her abstract and General Discussion state contagion as a
property of work groups and its effect on cooperation and conflict as an
effect, not an association.

## What is asserted

That in work groups generally, not only in the ad hoc student groups
studied, one member's displayed mood spreads to the others; and that
pleasant contagion causes more cooperation and less conflict in the group's
process, rather than merely going with them.

## What the Active entry establishes toward it

[THEORY-123](THEORY-123.md) holds the measured part. In Study 1 a confederate randomly
assigned to show pleasant or unpleasant mood moved members' mood with its
valence, by self-report and by blind coders, so the spread is causal in
that setting. The process link is a correlation between measured contagion
and coder-rated cooperation (r = .44) and conflict (r = −.42); the
manipulated conditions were not compared on process. Study 2 found members'
moods converging without a confederate (ICC .00 to .24) in MBA groups.

## What would confirm or reject it

The promote_when, inherited unchanged from [THEORY-123](THEORY-123.md): a second
experiment with a manipulated source in ongoing teams, several
confederates and mood measured during the interaction, and process
compared across the manipulated conditions. It is refuted if the
manipulated conditions spread mood but leave cooperation and conflict
unchanged.

## What this does not say

- **It does not say how contagion works.** Mimicry with afferent feedback
  and conscious social comparison both fit Barsade's data.
- **It does not say a group has a mood of its own.** That is the question
  of the convergence account, [THEORY-126](THEORY-126.md), which this does not decide.
