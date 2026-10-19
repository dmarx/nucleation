---
number: 251
status: Proposed
formerly:
- CLAIM-tmpu534h
title: 'A change in which questions a receiver population can answer determinately is not by itself a change of cover in the sheaf sense: the cover belongs to the measurement scenario and the responses are an empirical model on it, so such a change is a change of empirical model, which can create or remove a gluing obstruction on a fixed cover but does not change what the cover is, and the operational notion needs its own name until a functorial link is shown'
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-251.yaml, batch 002,
    ADR-047). The title adopted the reading's "only the third [changing the
    compatibility structure] directly engages gluing obstructions". As a
    formal statement that is false. On a fixed CHSH cover, changing only the
    response distribution takes an empirical model from noncontextual to
    contextual, and changing the measurement domain changes the cover. The
    title now sorts the changes into two kinds, of the scenario and of the
    empirical model, and keeps the claim's point: determinate answerability
    is the second kind. The quotation in the body is unchanged, and a note
    corrects it. The status stays Proposed: the remedy, a separate name for
    the operational notion, is the owner's decision.
role: counter
warrant: demonstrated
tags:
- contextuality
- mathematics
- translation
date: '2026-10-12'
line: pragmatic-transport
objects_to:
- CLAIM-201
summary: >-
  From the interlocutor's reading of PR [#121](https://github.com/dmarx/nucleation/issues/121) and its reconciliation,
  relayed by the owner on 2026-10-12, on the open tension between
  [CLAIM-197](CLAIM-197.md) with [CASE-048](../cases.d/CASE-048.md) and the operational cover of [CLAIM-201](CLAIM-201.md). It
  keeps the empirical notion and denies it the sheaf-theoretic name. Open.
---
<!-- inactive-ok-file: CLAIM-201 — Proposed; cited as open positions and readings the interlocutor's reading addresses, not as settled -->
# CLAIM-251: A change in which questions a receiver population can answer determinately is not by itself a change of cover in the sheaf sense: the cover belongs to the measurement scenario and the responses are an empirical model on it, so such a change is a change of empirical model, which can create or remove a gluing obstruction on a fixed cover but does not change what the cover is, and the operational notion needs its own name until a functorial link is shown

## The objection

The reading: "In sheaf theory, a cover is a family of domains equipped with specific compatibility and gluing conditions. In the transport proposal, a cover is operationally associated with which questions a receiver population can answer determinately. These are not automatically the same mathematical object."

It separates "Changing the measurement domain, changing the empirical response distribution, and changing the compatibility structure", and says: "Only the third directly engages gluing obstructions, and even there the restriction maps and admissible covers must be specified." A target language that makes an underspecified distinction obligatory "can change the set of distinctions available to readers. But this does not establish noncontextuality, contextuality, or failure of gluing." Low agreement "may indicate ambiguity, heterogeneity, uncertainty, or an inadequately defined response variable", not an absent context.

[CLAIM-201](CLAIM-201.md) already separates a change of global compatibility from local distortion. [CLAIM-197](CLAIM-197.md) says "which families count as covers decides whether anything glues", and [CASE-048](../cases.d/CASE-048.md) applies it without stating the cover. Notes of 2026-10-12 on all three record the tension.

## What would answer it

A stated construction of the operational cover as a family of contexts with restriction maps, shown to be a cover in the sense [CLAIM-197](CLAIM-197.md) uses. Or a separate name for the operational notion, with each entry that uses "cover" saying which it means.

## What it does not say

It does not say the operational notion is empty. The reading's advice is to "Keep the empirical notion of accessible distinctions, but give it a different formal name until an explicit functorial or sheaf-theoretic relationship is established."

## Note of 2026-10-19: distributions do engage gluing

The reading's "Only the third directly engages gluing obstructions" is
corrected here. In the sheaf framework ([LIT-016](../literature.d/LIT-016.md), [THEORY-012](../theory.d/THEORY-012.md)) a cover is part
of the measurement scenario: the observables and the family of jointly
measurable contexts. A family of response distributions on it is an
empirical model, and contextuality is a property of the model on a fixed
cover. The CHSH cover carries both kinds. A product of local response laws
is noncontextual, and the PR box is contextual. So changing only the
distributions can create or remove a gluing obstruction. Changing the
measurement domain changes the cover too, since a cover is a family of
subsets of the domain.

So the operations are of two kinds. A change of scenario, of domain or
cover, changes what gluing means. A change of empirical model on a fixed
cover changes whether it fails. The claim's point survives the correction
and is sharper for it. Which questions a population answers determinately
is a property of the responses, so changing it is a change of empirical
model and not of cover. That is the conflation [CLAIM-201](CLAIM-201.md)'s operational
"cover" risks.
