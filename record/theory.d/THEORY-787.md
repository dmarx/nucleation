---
number: 787
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
- THEORY-tmpfb136

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "A test of whether the macro advantage depends on the uniform intervention distribution that LIT-1038 imposes separately at each level. The account is promoted by a result showing that, on systems not built to display emergence, the EI-optimal coarse-graining stays the same, or stays macro, when the interventions follow the system's own stationary distribution or another distribution fixed in advance, and that it agrees with an independent interventionist test of which level the effects track (realization insensitivity under changes of realizer). It is in trouble if the macro advantage disappears whenever the same intervention distribution over micro states is used at both levels, since then the gain measures the change of distribution, not a property of the system. What cannot settle it: more hand-built toy systems with positive CE, which show only that the arithmetic works; or applications that estimate a TPM and report the best of many coarse-grainings with no correction for the search."

# The claim. Repeat it as the body's `# THEORY-787:` heading; the lint checks
# that the two agree.
title: "A system's causal structure can be most effective at a macro scale, so that causation emerges at a coarse-grained level and the macro description is the one at which the system's causes are found, as Hoel, Albantakis and Tononi propose from effective information"

version: 1

# One or more topics from luria.yaml, primary first — the same table the
# reading list uses. Take the topic of what the account is about.
tags:
- causality
- complex-systems
- information-theory

date: '2026-10-20'

# There is deliberately no `published:` line. It is DERIVED from the first
# entry in `source:` below, and writing it down is a lint violation, because
# the value has one home and this is not it.

# REQUIRED, and a LIST. The papers this account rests on, primary first. An
# explanation with no paper behind it is a hunch, and the lint will say so.
source:
- LIT-1038

# What the index table shows. The title already carries the claim, so spend
# this on provenance and on the sharp edge: who said it, and what it does not
# say. Prose, so bare codes in it get linked by `luria link --fix`.
summary: >-
  Hoel, Albantakis and Tononi (2013), [LIT-1038](../literature.d/LIT-1038.md), argue that macro can beat micro: the scale at which effective information peaks is where a system's causal structure is, so causation can emerge at a macro level. The record holds as shown, in [THEORY-222](THEORY-222.md), only the arithmetic: under uniform interventions imposed separately at each level, a macro description can have more effective information. This is the causal thesis, filed under [ADR-047](../decisions.d/ADR-047.md) v4 when the narrowing dropped it.
extends:
- THEORY-222
answers:
- QUESTION-204
---


# THEORY-787: A system's causal structure can be most effective at a macro scale, so that causation emerges at a coarse-grained level and the macro description is the one at which the system's causes are found, as Hoel, Albantakis and Tononi propose from effective information

## Source

Hoel, Albantakis and Tononi (2013, PNAS), [LIT-1038](../literature.d/LIT-1038.md), read in [NOTE-726](../notes.d/NOTE-726.md).
Their title, "macro can beat micro", and their discussion call the
EI-optimal level the intrinsic causal scale and say the macro then
excludes the micro.

## What is asserted

That the level at which effective information is highest is the level at
which the system's causation is, so that a coarse-grained description can
be causally privileged over the micro description it supervenes on.

## What the record holds toward it

[THEORY-222](THEORY-222.md), Active, is the formal part: with uniform interventions at each
level, a macro description of a known discrete mechanism can carry more
effective information than its micro description, by 0.40 to 2.92 bits in
four toy systems. The step from "EI is highest there" to "causation is
there" rests on the uniform intervention distribution imposed separately
at each level, which weights micro states differently at the two levels.
[QUESTION-204](../questions.d/QUESTION-204.md) asks whether the advantage survives a common intervention
distribution and agrees with an independent interventionist test.

## What this does not say

- Not that any real system has been shown to have causal emergence; the
  search over coarse-grainings is exhaustive only for toy sizes.
- Not the authors' further claims about brains and the hierarchy of the
  sciences, which they offer as conjecture.

## What would confirm or reject it

Confirmed by the promote_when: the EI-optimal level stays macro under the
system's own or another fixed intervention distribution, on systems not
built for it, and agrees with an independent interventionist test.
Rejected if the macro advantage disappears whenever the same intervention
distribution over micro states is used at both levels.
