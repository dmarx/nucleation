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
status: 'Rejected'
formerly:
- THEORY-tmpfb136
status_note: >-
  Rejected on 2026-10-30, at the owner's direction, by its own refutation
  condition: the macro advantage disappears whenever the same intervention
  distribution over micro states is used at both levels. THEORY-1167 proves
  this for a coarse-graining of one transition, by data processing, and
  Comolatti and Hoel concede it (LIT-1843). The independent interventionist
  test the promote_when asks for, causal feature learning (LIT-1833), can
  confirm that a macro is proportionate but never that it beats the micro
  (THEORY-1169). What the record holds instead is CLAIM-tmpxk5cy, by
  ARG-tmp2wo7e. Hoel's temporal and spatio-temporal macros, which the bound
  does not reach, are QUESTION-tmpzfd02. The arithmetic it rested on,
  THEORY-222, stands.

# REQUIRED while the status is Proposed or Deferred; delete it when the
# explanation goes Active. What would settle it — a KIND of result, not a
# quantity of them (ANTH-ADR-014). An explanation that cannot say what would show
# it wrong is a story, and this field is where that shows up.
promote_when: "A test of whether the macro advantage depends on the uniform intervention distribution that LIT-1038 imposes separately at each level. The account is promoted by a result showing that, on systems not built to display emergence, the EI-optimal coarse-graining stays the same, or stays macro, when the interventions follow the system's own stationary distribution or another distribution fixed in advance, and that it agrees with an independent interventionist test of which level the effects track (realization insensitivity under changes of realizer). It is in trouble if the macro advantage disappears whenever the same intervention distribution over micro states is used at both levels, since then the gain measures the change of distribution, not a property of the system. What cannot settle it: more hand-built toy systems with positive CE, which show only that the arithmetic works; or applications that estimate a TPM and report the best of many coarse-grainings with no correction for the search."

# The claim. Repeat it as the body's `# THEORY-787:` heading; the lint checks
# that the two agree.
title: "A system's causal structure can be most effective at a macro scale, so that causation emerges at a coarse-grained level and the macro description is the one at which the system's causes are found, as Hoel, Albantakis and Tononi propose from effective information"

version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Status Proposed → Rejected at the owner's direction of 2026-10-30
    ("reject it and adopt the proportionality thesis"), on THEORY-1167 and
    THEORY-1169; replaced in the record's voice by CLAIM-tmpxk5cy. The body
    is unchanged: it is the account as filed, with its two dated notes of
    2026-10-29.

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
<!-- inactive-ok-file: QUESTION-204 — Open; the question whose first half the note of 2026-10-29 reports answered, cited as open -->
<!-- inactive-ok-file: CLAIM-tmpxk5cy ARG-tmp2wo7e QUESTION-tmpzfd02 — Proposed or Open; what replaces this account and the case it leaves, named in the status note -->


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

## Note of 2026-10-29: the "in trouble if" clause is met for effective information

The promote_when says this account is in trouble if the macro advantage
disappears whenever the same intervention distribution over micro states
is used at both levels. For effective information that condition is now
met, and by proof, not by example. [THEORY-1167](THEORY-1167.md) (Active): with one
distribution over micro states at both levels, each macro intervention
realized by that distribution within its block, the macro EI is I(f(X);
f(Y)), which data processing bounds by I(X; Y), the micro EI. A macro can
at most tie. By the same derivation, the positive causal emergence of
[LIT-1038](../literature.d/LIT-1038.md) is the micro mechanism's gain from changing the distribution,
from the uniform one to the one Hoel's macro interventions induce, less a
non-negative loss.

Two readings of this date bear the same way.

- **Comolatti and Hoel**, [LIT-1843](../literature.d/LIT-1843.md) ([NOTE-1416](../notes.d/NOTE-1416.md)), concede the
  decisive case: under the system's own stationary distribution, used at
  both levels, EI shows no emergence, "This was known". Their reply, that
  other measures and individual transitions still show emergence, changes
  the measure, not the distribution. Those measures are pointwise or
  normalized by log₂ n, and data processing does not bound them. So the
  reply is not evidence for EI's level, which is what this account
  asserts. Their only system is a bipartite chain built so that its macro
  is a deterministic NOT gate, a hand-built toy of the kind the
  promote_when says cannot settle it.
- **Eberhardt and Lee**, [LIT-1839](../literature.d/LIT-1839.md) ([NOTE-1413](../notes.d/NOTE-1413.md)), trace EI's
  ambiguity and non-commutativity to the maximum-entropy distribution,
  "extraneous to the system". They do not compute EI under a common
  distribution; the record's derivation supplies that step.

The bound covers a coarse-graining of one transition. It does not reach
[LIT-1038](../literature.d/LIT-1038.md)'s temporal and spatio-temporal macros, and it says nothing about
measures that data processing does not bound ([THEORY-1167](THEORY-1167.md), "What this
does not say").

A move to Rejected, or a narrowing of this account to measures that data
processing does not bound, is proposed and left to the owner. The status
and the title are unchanged.

## Note of 2026-10-29: the independent interventionist test, and what it can show

The promote_when asks, beside a common distribution, that the EI-optimal
coarse-graining agree "with an independent interventionist test of which
level the effects track (realization insensitivity under changes of
realizer)". Causal feature learning is that test: Chalupka, Perona and
Eberhardt, [LIT-1833](../literature.d/LIT-1833.md) ([NOTE-1420](../notes.d/NOTE-1420.md)), and their overview, [LIT-1834](../literature.d/LIT-1834.md)
([NOTE-1415](../notes.d/NOTE-1415.md)). Two micro causes share a macro state iff manipulating to
either has the same effect, and no distribution over interventions enters.

Its verdict bears on this account in two ways.

- **It cannot confirm the account.** On a transition matrix the causal
  partition is the coarsest description whose manipulations are
  unambiguous. The micro description is never worse, only finer: it
  "contains no more causal information", and it loses none. So the test
  can confirm that a macro is proportionate, where micro rows are exactly
  equal, as in Eberhardt and Lee's (11), Hoel's example, and never that
  causation emerges at the macro or that the macro beats the micro.
  [THEORY-1169](THEORY-1169.md) (Active) makes the link to EI exact: under one
  full-support distribution at both levels, the coarse-grainings that keep
  all of the micro EI are exactly the causal partitions and their
  refinements, whatever the distribution. The ties [THEORY-1167](THEORY-1167.md) allows
  are these, and nothing exceeds them.
- **It disagrees with the EI this account rests on.** Hoel's EI, uniform
  at each level, merges causes with different rows on Eberhardt and Lee's
  (13) and (14), and on their note 6 it keeps identical rows apart. On
  those matrices the agreement the promote_when asks for fails. They are
  hand-built, which by the promote_when's terms cannot settle it, and Hoel
  2013's own examples ([THEORY-222](THEORY-222.md)) were not recomputed.

The test also needs exact equality. With estimated rows, causal feature
learning merges by a distance threshold, a choice [THEORY-1169](THEORY-1169.md) does not
make.

Nothing here moves the account toward promotion. The status and the title
are unchanged. The move to Rejected, or the narrowing, that the earlier
note of this date proposed is still the owner's call.
