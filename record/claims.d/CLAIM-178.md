---
number: 178
status: Proposed
formerly:
- CLAIM-tmp5o4dd
title: 'A manuscript should be a view over the argument and not its only copy: a draft written straight from an exchange drops commitments and changes its thesis without saying so, and both become visible only against a record where claims carry status and inclusion separately'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Drafts written straight from an exchange, checked against the exchange
  itself, turn out to preserve its commitments and announce changes of
  thesis about as often as drafts written against a record. Or a record
  kept beside the draft catches nothing that a careful reread of the
  draft would not.
tags:
- design-rationale
- epistemology
date: '2026-10-11'
line: nucleating-argument
works:
- luria-nucleating-an-argument
answers:
- QUESTION-037
rests_on:
- CLAIM-177
- CLAIM-tmpwkbsy
uses:
- TERM-052
summary: >-
  Luria's distinction between sources and generated views, carried over
  from files to argument. The evidence is the two "crystallized
  arguments" of the What Survives Translation? exchange and the
  manuscripts drafted from them (workbench 2026/10/09/025539,
  2026/10/10/040457). Proposed: the record is kept beside the manuscript,
  and nothing generates a manuscript from it.
objected_by:
- CLAIM-181
supports:
- CLAIM-183
- CLAIM-189
---
<!-- inactive-ok-file: CLAIM-125 — Proposed; cited for the two open problems the second crystallized argument left out -->
<!-- inactive-ok-file: CLAIM-182 CLAIM-185 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: CLAIM-017 — Superseded; cited as the history of a thesis or term, whose change is the point -->
<!-- inactive-ok-file: CLAIM-115 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->

# CLAIM-178: A manuscript should be a view over the argument and not its only copy: a draft written straight from an exchange drops commitments and changes its thesis without saying so, and both become visible only against a record where claims carry status and inclusion separately

## The claim

Luria's working agreement is "Never edit a generated file". A view is
rebuilt from sources, and an edit made to the view is lost or drifts
([LU-DP-003](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-3)). When an argument exists only in its manuscript, the manuscript
is a view that is being edited as if it were the source.

The translation exchange is the case. At U38 the owner asked for "the whole
(crystallized) argument", and three minutes later for a manuscript. The
draft:

- changed the thesis from [CLAIM-017](CLAIM-017.md) to [CLAIM-115](CLAIM-115.md), with no turn arguing the
  move;
- added "necessary" to "not sufficient", supported by an example that shows
  only insufficiency ([CLAIM-053](CLAIM-053.md));
- dropped 24 items of the crystallized argument, none of them on request.

The second crystallized argument (A203), the terminal state at U56
([TERM-052](../terms.d/TERM-052.md)), announced its change of question. It also left out
Tannaka reconstruction, which A198 had offered as a model for rebuilding a
communicative kind's symmetries from its realizations ([QUESTION-036](../questions.d/QUESTION-036.md)),
[CLAIM-125](CLAIM-125.md)'s two open problems, and more. Maturing can legitimately drop
things, so some of these may have dissolved rather than been lost, but
nothing in the exchange says which. Each draft read as finished. None of
the omissions could be seen, let alone classified, without a list of what
came before.

The record supplies that list. A claim has a status (does the record
believe it?) and a `works` membership (is it in the paper?), and [ADR-032](../decisions.d/ADR-032.md)
keeps the two apart because they diverge. A manuscript is then one
marshalling of claims whose status can be read, and a dropped commitment is
a claim that is still Proposed and that the work no longer includes.

## What it does not say

- It does not say a manuscript can be generated from the record. The prose
  is written, not assembled. "View" means that the record is the reference
  the draft is checked against.
- It does not say that every change of thesis made in a draft is wrong. It
  says the change should be visible.

## Note of 2026-10-11: why drafts lose material silently

Under the owner's reframing ([CLAIM-185](CLAIM-185.md)), this claim gets a mechanism.
A draft persists, but its claims are not addressable one by one, so nothing
rests on them ([CLAIM-182](CLAIM-182.md)). When a draft drops one, no reference breaks
and nothing reports the loss. A claim in the record is an anchor. Dropping
it from a work leaves its inbound references standing and its `works`
membership visibly gone.

## Note of 2026-10-15: split under [ADR-043](../decisions.d/ADR-043.md)

[ADR-043](../decisions.d/ADR-043.md)'s classification found this claim compound: that a manuscript
should be a view over the argument is interpretive, while that the
drafts of the What Survives Translation? exchange dropped commitments
and changed the thesis without saying so is empirical, from one
exchange. The empirical part, scoped to that exchange, is now [CLAIM-tmpwkbsy](CLAIM-tmpwkbsy.md), on
which this claim rests, as it already rests on [CLAIM-177](CLAIM-177.md). This claim
keeps the rest and stays interpretive: the general form, that a draft
written straight from an exchange behaves this way, generalizes from
one case, and the remedy is a proposal. Its title already states the
general form, so it was kept.
