---
number: 204
status: Open
formerly:
- QUESTION-tmp3zal3
title: "Does a macro description's effective-information advantage survive when the same intervention distribution over micro states is used at both levels, and does the EI-optimal level agree with an independent interventionist test of which level the effects track?"
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Note of 2026-10-29 added: the first half is answered, no, by
    THEORY-tmphfpe7: under one distribution over micro states at
    both levels, macro EI cannot exceed micro EI, by data
    processing. The second half is open, and the question stays
    Open.
tags:
- causality
- information-theory
date: '2026-10-20'
line: 'distributed-agency'
refines:
- QUESTION-093
summary: >-
  The promotion condition formerly on [THEORY-222](../theory.d/THEORY-222.md). [THEORY-222](../theory.d/THEORY-222.md) was narrowed
  and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2) to the statement about
  effective information that holds by construction. With uniform
  interventions imposed separately at each level, a macro description can
  have higher EI than the micro one. Whether that gain survives a single
  intervention distribution, and whether the EI peak marks where
  causation happens, is open.
answered_by:
- THEORY-787
---
<!-- inactive-ok-file: THEORY-787 — Proposed; the causal thesis this question was filed to test, cited in the note of 2026-10-29 as open -->

# QUESTION-204: Does a macro description's effective-information advantage survive when the same intervention distribution over micro states is used at both levels, and does the EI-optimal level agree with an independent interventionist test of which level the effects track?

## Why it is a question

[THEORY-222](../theory.d/THEORY-222.md) holds the arithmetic of Hoel, Albantakis and Tononi (2013).
Effective information is measured with a uniform distribution imposed
over the states at each level, and under that choice a coarse-graining
can gain more effectiveness than it loses in size. The choice weights the
micro states differently at the two levels. The authors note that this
is what lets the macro win, and present it as fairness. If the gain
disappears when one distribution over micro states is used at both
levels, it measures the change of distribution, not a property of the
system. Until 2026-10-20 this was [THEORY-222](../theory.d/THEORY-222.md)'s promote_when.

## What would answer it

- A result on systems not built to display emergence, showing that the
  EI-optimal coarse-graining stays the same, or stays macro, when the
  interventions follow the system's own stationary distribution or
  another distribution fixed in advance.
- An agreement between the EI-optimal level and an independent
  interventionist test of which level the effects track, such as
  realization insensitivity under changes of realizer.

What cannot settle it: more hand-built toy systems with positive causal
emergence, which show only that the arithmetic works; or applications
that estimate a transition matrix and report the best of many
coarse-grainings with no correction for the search.

## Note of 2026-10-29: the first half answered, by derivation

The first half of this question is answered, and the answer is no.
[THEORY-tmphfpe7](../theory.d/THEORY-tmphfpe7.md) (Active) shows that the test needs no system. With one
distribution over micro states at both levels, each macro intervention
realized by that distribution within its block, the macro EI is I(f(X);
f(Y)) ≤ I(X; Y), the micro EI, by data processing. A macro can at most
tie, on any system and under any distribution fixed in advance, the
stationary one included. Hoel's positive causal emergence is the micro
mechanism's gain from changing the distribution, less a non-negative loss.
On Eberhardt and Lee's matrices (11), (13) and (14) the decomposition is
0.456 = 0 + 0.456, 0.194 = −0.150 + 0.344 and 0.0001 = −0.074 + 0.074
bits. Comolatti and Hoel, [LIT-tmpzfaqi](../literature.d/LIT-tmpzfaqi.md) ([NOTE-tmpcmbzs](../notes.d/NOTE-tmpcmbzs.md)), concede the
stationary case ("This was known"). Eberhardt and Lee, [LIT-tmpr2bnp](../literature.d/LIT-tmpr2bnp.md)
([NOTE-tmp0q96y](../notes.d/NOTE-tmp0q96y.md)), name the maximum-entropy distribution as the source of
the artefact, but do not themselves compute EI under a common one.

The second half, whether the EI-optimal level agrees with an independent
interventionist test, is open. Eberhardt and Lee's (14) is one small case
where the two part. A test of realization insensitivity would keep x₁ and
x₂ apart, since their effects on the macro effect variable differ (0.8/0.2
against 0.9/0.1), and EI merges them. It is a hand-built 3×3 matrix, which
by this question's own terms cannot settle agreement in general.

The bound is for EI. Measures that data processing does not bound,
per-transition ones or ones normalized by log₂ n, can rise at a macro
under a common distribution; they are not what this question asks about.
[THEORY-787](../theory.d/THEORY-787.md) is noted the same day. The question stays Open.
