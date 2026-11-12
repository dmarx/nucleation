---
status: Proposed
title: "Bickhard's account and the two-profile forager show that a profile set by a system's own upkeep is a norm different from a designer's, with the same silent case and different verdicts where persistence is at stake"
version: 2
history:
- version: 2
  date: '2026-11-12'
  note: >-
    Step 2 restates CLAIM-tmpkr3ti as revised at the review of #483 the owner relayed on 2026-11-12
    (evidence in general, entailment under a deterministic guarantee). The
    inference is unchanged.
form: existence
grounds:
- THEORY-220
- CASE-tmpfobkh
rests_on:
- CLAIM-tmpkr3ti
concludes:
- CLAIM-tmph9egz
tags:
- philosophy-of-biology
date: '2026-11-12'
line:
- organizational-normativity
summary: >-
  The inference to [CLAIM-tmph9egz](../claims.d/CLAIM-tmph9egz.md). Bickhard's account ([THEORY-220](../theory.d/THEORY-220.md))
  supplies the anticipation and its failure by the system's own lights.
  The owner's claim ([CLAIM-tmpkr3ti](../claims.d/CLAIM-tmpkr3ti.md)) supplies the reading of an absence
  under an expected profile. The forager construction ([CASE-tmpfobkh](../cases.d/CASE-tmpfobkh.md))
  shows that a profile set by upkeep and one set by a designer are
  different norms. Proposed. The construction establishes the difference
  between the norms, not that a simulated self-set norm is the system's
  own; that rests on [THEORY-220](../theory.d/THEORY-220.md), which is Proposed. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmph9egz CLAIM-tmpkr3ti CASE-tmpfobkh — filed in this pull request, Proposed -->
<!-- inactive-ok-file: THEORY-220 THEORY-628 — Proposed; readings cited with their standing -->

# ARG-tmpcd9j9: Bickhard's account and the two-profile forager show that a profile set by a system's own upkeep is a norm different from a designer's, with the same silent case and different verdicts where persistence is at stake

## The inference

1. [THEORY-220](../theory.d/THEORY-220.md): a self-maintaining system's selection of an interaction
   anticipates its success, and the anticipation can be false by the
   system's own lights.
2. [CLAIM-tmpkr3ti](../claims.d/CLAIM-tmpkr3ti.md): an absence under an expected response profile is
   evidence that what was tested failed, and entails it under a
   deterministic guarantee. The forager's profile is deterministic, so
   in [CASE-tmpfobkh](../cases.d/CASE-tmpfobkh.md) its registered failures are of the second kind.
3. [CASE-tmpfobkh](../cases.d/CASE-tmpfobkh.md): there is a construction in which a profile fixed by the
   system's upkeep and a stored designer's profile agree on a silent patch
   (S3) and give opposite verdicts in S2 and S4. Recomputed exactly:
   - in S2 only the designer's flags;
   - in S4 only the self-set profile flags, and the designer's forager
     dies at step 119.
4. So there exist profiles of both kinds that are different norms, and
   by 1 and 2 the self-set kind is the endogenous form of the debugger's
   reading ([CLAIM-tmph9egz](../claims.d/CLAIM-tmph9egz.md)).

## Critical questions

- **Is the construction coherent, and does it have the property
  claimed?** Yes. It is deterministic, and the table is reproduced
  exactly. The difference between the norms is a fact about it.
- **Does it separate what the conclusion says comes apart?** It
  separates the two profiles' verdicts. It does not separate a system's
  own norm from a modeller's choice, since both profiles are written by
  the modeller. Step 4's "endogenous" rests on [THEORY-220](../theory.d/THEORY-220.md), not on the
  case. That is the main limit, and why the ARG is Proposed.
- **Could the difference be an artefact of the parameters?** The
  qualitative pattern needs only a yield change that stays above upkeep
  (S2) and an upkeep change that passes an unchanged yield (S4). Any
  values meeting those inequalities give it. The step of death, 119,
  depends on the values.

## What it does not show

That any real system holds such a profile, or that a graded norm
([THEORY-628](../theory.d/THEORY-628.md)) can be had the same way.
