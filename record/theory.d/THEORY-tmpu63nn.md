---
status: Proposed
promote_when: >-
  Evidence beyond this preprint, in other domains, datasets or
  counterfactual-explanation methods, that an organization's upstream
  pipeline choices (label definition, feature measurement, selection
  metric, validation) change the generated counterfactual explanations by
  as much as or more than changes to the explanation method do. The
  normative consequence the title draws (that such explanations alone
  cannot establish justification or fix what the subject should do)
  follows from that finding and is not asked separately.
title: 'Counterfactual explanations used to justify a decision or to offer recourse are partly artifacts of the deployer''s upstream choices of labels, measures, selection metrics and validation, which shift them as much as or more than the explanation method does, so on their own they cannot show that a decision was justified or what its subject should change, and they bracket whether the decision-maker should have acted otherwise'
version: 1
tags:
- society-and-governance
- philosophy-of-technology
date: '2026-11-18'
source:
- LIT-2713
corroborates:
- CLAIM-tmpohafo
summary: >-
  Cerrato, Sahlgren & Heilmann (2026), [LIT-2713](../literature.d/LIT-2713.md), read in [NOTE-tmpsuiyz](../notes.d/NOTE-tmpsuiyz.md):
  experiments on one resume-screening pipeline with two retrieval-based
  methods, and a normative argument for relational recourse. It
  corroborates [CLAIM-tmpohafo](../claims.d/CLAIM-tmpohafo.md), which does not rest on it: explanation can
  be given while the choices that would have to be contested stay hidden.
  The wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpohafo — Proposed; cited with their standing, entries this reading bears on or files -->

# THEORY-tmpu63nn: Counterfactual explanations used to justify a decision or to offer recourse are partly artifacts of the deployer's upstream choices of labels, measures, selection metrics and validation, which shift them as much as or more than the explanation method does, so on their own they cannot show that a decision was justified or what its subject should change, and they bracket whether the decision-maker should have acted otherwise

Cerrato, Sahlgren & Heilmann (2026), [LIT-2713](../literature.d/LIT-2713.md).

## The result

On ACS census data with earnings standing in for fit, the authors
intervene on four upstream choices in a modelled resume-screening
pipeline and compare their effect on the generated counterfactuals with
the effect of changing the method's validity threshold. For two
retrieval-based methods, the upstream choices "have as much or more impact
on the generated counterfactuals as the specifics of the generating
method" (abstract). The normative half follows: under the "fixed model
assumption" a counterfactual brackets the deployer's choices, so
"upstream choices must be relatively settled, normatively speaking, prior
to evaluating CEs for recourse".

## What it does not show

- **That counterfactual explanations are generally unreliable.** The
  authors say they "do not report this result intending to demonstrate a
  limitation of CEs per se".
- **Generality.** One domain, proxy labels, two methods; the paper's own
  conclusions describe a single method, and some numbers in the text do
  not agree with each other.
- **Anything about suspending a decision.** The interruption entitlement
  of [CLAIM-tmpohafo](../claims.d/CLAIM-tmpohafo.md) is untouched.
