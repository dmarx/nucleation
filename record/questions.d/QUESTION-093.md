---
number: 93
status: Open
formerly:
- QUESTION-tmpuz3py
title: 'Which of predictive autonomy, interventional autonomy, organizational closure and self-individuation must a coalition of processes have before it is a higher-level agent and not a convenient aggregate, and, beyond an effective-information advantage without closure or self-individuation, which of them can it have without the others?'
version: 2
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Split under ADR-049. Whether a macro description can have
    interventional autonomy, an effective-information advantage, without
    organizational closure or self-individuation is QUESTION-250,
    Answered by THEORY-222. This question is reworded to what is left:
    which criteria are necessary, and which other pairs come apart.
    Version 1's title was 'Which of predictive autonomy, interventional
    autonomy, organizational closure and self-individuation must a
    coalition of processes have before it is a higher-level agent and not
    a convenient aggregate, and can it have the first without the
    others?'
tags:
- individuation
- agency
date: '2026-10-13'
line: distributed-agency
refines:
- QUESTION-009
summary: >-
  A11's Q3 with A10 §4.1's three criteria, sharpening [QUESTION-009](QUESTION-009.md)
  (Deferred) into separable conditions. The record's reification rule
  ([CLAIM-154](../claims.d/CLAIM-154.md)) prices the first. [CLAIM-170](../claims.d/CLAIM-170.md) makes agents a factorization
  relative to a level. An effective-information advantage without closure
  or self-individuation is QUESTION-250, Answered. Which criteria are
  necessary, and whether the others come apart, is open, and r/place
  ([CASE-079](../cases.d/CASE-079.md)) offers coalitions on which to test it.
refined_by:
- QUESTION-204
- QUESTION-250
---

<!-- inactive-ok-file: CLAIM-170 CLAIM-194 QUESTION-009 THEORY-071 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# QUESTION-093: Which of predictive autonomy, interventional autonomy, organizational closure and self-individuation must a coalition of processes have before it is a higher-level agent and not a convenient aggregate, and, beyond an effective-information advantage without closure or self-individuation, which of them can it have without the others?

## Why it is a question

A11 §6: "**Q3. Under what conditions does a recursively organized
population become a higher-level agent?** Which combinations of predictive
autonomy, intervention autonomy, organizational closure, and
self-individuation distinguish an effective macro-agent from a merely
convenient aggregate?" A10 §4.1 defined three: "**Predictive autonomy:** Does
the higher-level model predict future behavior efficiently and robustly?
**Intervention autonomy:** Do higher-level variables support stable
predictions about the effects of interventions? **Constitutive autonomy:**
Does the higher-level organization maintain the constraints that enable its
own functioning? A system might satisfy the first while failing the other
two."

It refines [QUESTION-009](QUESTION-009.md), "When does a pattern of coordination constitute an
additional agent?", which is Deferred, by breaking the answer into criteria
that can be checked separately. What the record holds on each:

- **Predictive autonomy.** The reification rule, [CLAIM-154](../claims.d/CLAIM-154.md), prices it as
  effect-to-noise against Occam cost. Hoel et al. 2013 ([LIT-1038](../literature.d/LIT-1038.md)) is
  the causal-emergence version. It is read, and [THEORY-222](../theory.d/THEORY-222.md) places it
  under interventional autonomy (note of 2026-10-16).
- **Being an agent relative to a level and a target.** [CLAIM-170](../claims.d/CLAIM-170.md) and
  [QUESTION-032](QUESTION-032.md).
- **Closure and self-individuation.** [THEORY-071](../theory.d/THEORY-071.md)'s individuality condition,
  and [CLAIM-194](../claims.d/CLAIM-194.md)'s objection that coupling criteria cannot tell a made
  boundary from an imposed one.

A8 §5 proposed the test on r/place: whether a model with latent coalitions
predicts held-out behaviour, "especially after leadership changes, territorial
attacks, or alliance shifts", better than a flat model with complexity
controlled. An answer says which criteria are necessary and whether any is
sufficient, with a case where they come apart.

## Note of 2026-10-16: Hoel et al. 2013 is read

The list above calls [LIT-1038](../literature.d/LIT-1038.md) unread. It was read on 2026-10-13
([NOTE-726](../notes.d/NOTE-726.md)) and has a reading, [THEORY-222](../theory.d/THEORY-222.md). Its status note places it
here as an interventional criterion met with no closure and no
self-individuation. [QUESTION-115](QUESTION-115.md) asks the parallel question for
individuation rather than agency.

**Split, 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).** [THEORY-222](../theory.d/THEORY-222.md) answers half the question,
as its Connections says, and that half is [QUESTION-250](QUESTION-250.md), Answered. A
coarse-grained macro of a known mechanism can have more effective
information than its micro, under uniform interventions at each level, in
systems that maintain nothing and with a grouping an analyst chose. This
question keeps what that leaves: which criteria a higher-level agent
needs, whether any is sufficient, and whether predictive autonomy from
data, closure or self-individuation can be had without the others.
