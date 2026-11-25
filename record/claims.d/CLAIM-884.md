---
number: 884
status: Proposed
formerly:
- CLAIM-tmptbxbq
title: 'Interventional variance tracks endogenisation'
statement: >-
  On a minimal ecological-scaffolding model, Bourrat's interventional
  variance criterion tracks the endogenisation of the scaffold and his
  environment-conditioned coarse-graining criterion does not, and neither,
  as defined, separates a transition from a collective that absorbs its
  external scaffold or from one its environment reconstructs
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation, found by a test or a rerun of
  scratch/studies/lead-167/; or a showing that the implementation departs
  from Bourrat's definitions as the record reads them (NOTE-027, NOTE-064)
  in a way that reverses one of the four verdicts: C2's variance falls with
  endogenisation; δC|E is unchanged by it; C2 is passed at λ = 0 by the
  patch with its scaffold; δC|E is passed by every partition of a
  common-input population. A different model on which the measures behave
  better does not defeat it, since the claim is that the measures as
  defined do not guarantee the separation, and one model shows that.
tags:
- individuation
- information-theory
- philosophy-of-biology
- causality
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-115
grounds:
- CASE-320
- THEORY-424
---
<!-- inactive-ok-file: LIT-005 LIT-049 THEORY-607 — Proposed; the papers whose measures are computed, and the reading whose promote_when this bears on -->
<!-- inactive-ok-file: CASE-320 — new, filed with this claim -->

# CLAIM-884: Interventional variance tracks endogenisation

## The claim

[CASE-320](../cases.d/CASE-320.md) computes both of Bourrat's individuality measures exactly on a
256-state model. In the model, a patch of cells holds together first only
where an external scaffold is present, and at the end whatever the scaffold
does. The parameter λ runs that path.

- **C2 tracks endogenisation.** C2 is the 2024 paper's criterion ([LIT-005](../literature.d/LIT-005.md)): low variance of
  Â under interventions on the environment. The patch's variance falls from
  0.028 to 0 along λ, from the least invariant candidate to the most. This is
  the behaviour Bourrat predicts, and it holds over the parameters tried. Â
  itself rises with λ, and C1 discriminates nothing.
- **δC|E does not.** δC|E is the 2023 paper's criterion for environmental
  confounds ([LIT-049](../literature.d/LIT-049.md)): the coarse-graining error conditioned on the
  environment. It is exactly zero for the patch partition at every λ, so it
  is the same before the transition and after.
- **Neither excludes the counterfeits.**
  - A candidate that takes the external scaffold into itself passes C2 at
    λ = 0, before any endogenisation, because Â credits the scaffold's own
    persistence to the collective.
  - A population whose cells only copy their patch's environment, with no
    interaction, passes δC|E for all 203 partitions.
  - Â ranks such an environment-driven patch above a single cell as soon as
    the cells keep any heredity of their own.

So on the record's question of where individuality criteria part on one
system ([QUESTION-115](../questions.d/QUESTION-115.md)), the interventional measure and the coarse-graining
measure part on exactly the transition. The interventional one moves with
endogenisation, and the coarse-graining one registers only the partition
the scaffold already imposed. Both are fooled by where the boundary is
drawn: around the scaffold for Â, and around nothing in particular for
δC|E.

The result bears on [THEORY-607](../theory.d/THEORY-607.md)'s promote_when, which asks for an
accuracy-plus-cost objective whose selected grain shifts with the
transition. Bourrat's own δC|E with a cost term picks the patches from the
start and so does not shift. An unconditional, distributional variant with
a cost term does shift, from the whole population to the patches late in
the path. That variant is not the paper's. Whether it meets promote_when is
the owner's call.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.

## What it does not say

- **Not that the measures fail in general.** The claim is about what they
  guarantee: one model shows they do not separate a transition from these
  counterfeits.
- **Not that Black et al.'s model behaves this way.** That model is unread
  and not reproduced, and λ is swept, not evolved.
- **Not that C2 succeeds.** It gives a ranking without a threshold. In an
  asymmetric common-input control its variance (0.0085) is as low as the
  model's halfway point.
- **Not that the exact zeros are robust.** They come from exchangeable cells
  within a patch. The rankings are what is claimed to carry over.
