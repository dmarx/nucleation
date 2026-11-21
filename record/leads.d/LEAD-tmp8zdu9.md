---
status: Open
title: 'Have a human second coder recode the decision census''s random sample of 30 decisions against its fixed codebook, and report agreement with the first coding field by field, to test whether the census''s reliability survives a coder who is not an instance of the same model'
version: 1
stage: specified
priority: medium
method:
- empirical
tags:
- design-rationale
- philosophy-of-science
date: '2026-11-21'
line:
- record-as-apparatus
- records-of-inquiry
advances:
- CLAIM-tmpmtv1b
- CLAIM-tmpj5aiv
- CLAIM-tmpzrl0a
summary: >-
  At the owner's ruling of 2026-11-21 on the promotion pull request ("file
  that as a lead"). Every coder of the decision census ([CASE-tmpnkuie](../cases.d/CASE-tmpnkuie.md))
  was an instance of one model, so its agreement figures (Cohen's kappa
  0.81 to 1.00 on the fields used) may measure shared framing rather
  than reliability. A human recodes the same seeded sample of 30
  decisions against the same codebook, blind to the first coding, and
  agreement is reported per field against both earlier coders.
---
<!-- inactive-ok-file: CLAIM-tmpmtv1b CLAIM-tmpzrl0a CLAIM-tmppkqzl CLAIM-tmp1xigl — Proposed or new; the census and the claims resting on its coding -->

# LEAD-tmp8zdu9: Have a human second coder recode the decision census's random sample of 30 decisions against its fixed codebook, and report agreement with the first coding field by field, to test whether the census's reliability survives a coder who is not an instance of the same model

## Sketch

**Why.** The census ([CASE-tmpnkuie](../cases.d/CASE-tmpnkuie.md)) coded all 114 decisions to 2026-11-20 with four coder agents, and a fifth recoded a seeded random 30 (seed 20261120). Agreement was high on the fields the findings use. But all five coders were instances of one model, briefed from one codebook. High agreement among readers who share a framing is weak evidence of fidelity to what is coded ([CLAIM-tmppkqzl](../claims.d/CLAIM-tmppkqzl.md), [CLAIM-tmp1xigl](../claims.d/CLAIM-tmp1xigl.md)). It is the largest threat to the census's validity the manuscript names.

**Design.**

1. **Materials.** The codebook as fixed before coding (`scratch/formal/decision-census/census/CODEBOOK.md`), and the 30 decisions of the recode sample, each as the decision's text at the commit the census read.
2. **Coder.** One person who has not seen the first coding, the recode or the manuscript's findings. Ideally not the owner, whose decisions are the coded material. The owner is an acceptable second choice, with that noted.
3. **Procedure.** Code every field the codebook defines, for each of the 30, in the codebook's order. Record ambiguities as notes rather than resolving them by asking.
4. **Analysis.** Run `census.py`'s `cohen_kappa` on the human coding against the first coding and against the recode, field by field. Report Cohen's kappa and raw agreement, and list each disagreement on the fields the findings rest on (who noticed, refinement or revision, residue).

**What would count.** If the human's agreement with the first coding is about as high as the model recode's on the fields the claims use, the census's reliability is not an artefact of a shared model. If it falls well below on "who noticed" or on refinement and revision, [CLAIM-tmpmtv1b](../claims.d/CLAIM-tmpmtv1b.md) and [CLAIM-tmpzrl0a](../claims.d/CLAIM-tmpzrl0a.md) rest on a coding that does not survive an independent reader. Those claims would need recoding or withdrawing.

**Cost.** About three to four hours of a person's time: 30 decisions at five to eight minutes each, plus reading the codebook. The scripts exist.

**Stage.** Specified: materials, procedure and analysis are fixed. Not costed in money, and no coder is named.
