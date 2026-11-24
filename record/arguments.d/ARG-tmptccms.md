---
status: Proposed
title: 'The global Chubby planned outage, one documented specimen, as evidence, shows that realized reliability above a declared guarantee can induce dependence beyond it and that holding reliability to the guarantee can flush that dependence out, but not how often either happens'
version: 1
form: evidence
grounds:
- CASE-tmp3xxqg
- LIT-tmpihhfs
concludes:
- CLAIM-tmpb1wyc
tags:
- software-engineering
- society-and-governance
date: '2026-11-24'
line:
- dependence-and-domination
summary: >-
  The support [CASE-tmp3xxqg](../cases.d/CASE-tmp3xxqg.md) gives [CLAIM-tmpb1wyc](../claims.d/CLAIM-tmpb1wyc.md), filed from A34 §2 of the
  exchange "Memes, Contracts, and Systemic Normativity" (2026-11-24).
  Load-bearing: the case is the claim's only ground. A34 itself narrows
  what it shows ("not necessarily a mutually maintained implicit contract
  in our narrower sense"). The inference holds as an existence result and
  is weak for the general "can lower the resilience", which needs
  [LEAD-tmpmmfxt](../leads.d/LEAD-tmpmmfxt.md). The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---

<!-- inactive-ok-file: CASE-tmp3xxqg CLAIM-603 CLAIM-tmpb1wyc — Proposed, Deferred or new; filed or registered with the exchange 'Memes, Contracts, and Systemic Normativity', cited whatever their standing -->

# ARG-tmptccms: The global Chubby planned outage, one documented specimen, as evidence, shows that realized reliability above a declared guarantee can induce dependence beyond it and that holding reliability to the guarantee can flush that dependence out, but not how often either happens

## The inference

1. The book reports that "service owners began to add dependencies to
   Chubby assuming that it would never go down", because "true global
   Chubby outages are so infrequent", and that the failures of the global
   instance "consistently generated service outages, many of which were
   visible to end users" ([CASE-tmp3xxqg](../cases.d/CASE-tmp3xxqg.md)).
2. Chubby had a declared objective; its realized availability ran above
   it, which is why SRE now holds it to "meets, but does not
   significantly exceed" the objective.
3. After synthesized outages, the book reports, "we are able to flush out
   unreasonable dependencies on Chubby shortly after they are added".
4. So there is at least one provider whose realized reliability above its
   guarantee induced dependents to drop tolerance of its absence, with
   harm propagating, and for which holding realized reliability to the
   guarantee exposed dependencies as they formed.

## Critical questions

**Would the evidence be expected if the claim were false?** The
dependence might have formed whatever Chubby's realized availability, from
developers' ignorance of the objective. The book's own explanation is the
infrequency of outages ("assuming that it would never go down"), which is
the claim's mechanism; but it is the operator's explanation, not a
comparison. One instance cannot tell a reliability-induced dependence from
one that any ignorance of the objective would produce.

**Does it tell the claim apart from its rivals?** Against [CLAIM-603](../claims.d/CLAIM-603.md)'s
reading, no: the loss is a Black Queen loss either way. What the case
adds is the remedy on the provider's side, keeping the realized
regularity at the declared one, which [CLAIM-603](../claims.d/CLAIM-603.md) does not have.

**Does the measure measure what it is said to?** "Resilience of the
encompassing organization" is read off user-visible outages after
Chubby's failures. That is the propagation, the right quantity, reported
qualitatively and without numbers.

## Verdict

Proposed. An existence result from one well-documented specimen: it shows
the mechanism can occur and the remedy can work, and nothing about rates.
The claim's "can" is the right modality for that; any stronger reading
waits on [LEAD-tmpmmfxt](../leads.d/LEAD-tmpmmfxt.md).
