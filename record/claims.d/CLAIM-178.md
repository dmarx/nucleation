---
number: 178
status: Proposed
formerly:
- CLAIM-tmp5o4dd
title: 'A manuscript should be a view over the argument and not its only copy: a draft written straight from an exchange drops commitments and changes its thesis without saying so, and both become visible only against a record where claims carry status and inclusion separately'
version: 8
history:
- version: 2
  date: '2026-10-29'
  note: >-
    Tenth status review (ADR-057). CLAIM-181's limit written into
    'What it does not say': the record shows what a draft dropped only
    of what its grammar held. The title says such losses become
    visible only against a record, not that all do, so it is
    unchanged.
- version: 3
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by records-of-inquiry, at the split of that
    line (ADR-082). No other change.
- version: 4
  date: '2026-11-08'
  note: >-
    Carries nucleating-argument again beside its new line, at ADR-
    tmpyb8vm's rule (version 2): an entry the split moved keeps the old
    line when it answers, refines or objects to one of that line's
    entries, and it answers QUESTION-037, the line's root question, and
    rests on CLAIM-177 and CLAIM-324. No other change.
- version: 5
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11, by question: bears_on QUESTION-258
    added. The question's text: "The record already says it does not
    generate manuscripts (CLAIM-178)." Its own: a draft written
    straight from an exchange "drops commitments and changes its
    thesis without saying so", which bears on what a selection must
    preserve. No other change.
- version: 6
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
- version: 7
  date: '2026-11-25'
  note: >-
    Joins the work luria-beyond-software (ADR-tmp85hdc): Article 2 of A45
    in the exchange "Hyper article interpretation" states its proposition
    or uses it as a step, in §6. No other change.
- version: 8
  date: '2026-11-25'
  note: >-
    Joins the work hyperarticles (ADR-tmp85hdc): Article 3 of A45 in the
    exchange "Hyper article interpretation" states its proposition or uses
    it as a step, in §2. No other change.
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
line:
- records-of-inquiry
- nucleating-argument
- scholarly-publishing
works:
- hyperarticles
- luria-beyond-software
- from-obstruction-to-reorganization
answers:
- QUESTION-037
rests_on:
- CLAIM-177
- CLAIM-324
uses:
- TERM-052
summary: >-
  Luria's distinction between sources and generated views, carried over
  from files to argument. The evidence is the two "crystallized
  arguments" of the What Survives Translation? exchange and the
  manuscripts drafted from them (workbench 2026/10/09/025539,
  2026/10/10/040457). Proposed: the record is kept beside the manuscript,
  and nothing generates a manuscript from it.
bears_on:
- QUESTION-258
---
<!-- inactive-ok-file: CLAIM-182 CLAIM-185 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: CLAIM-017 — Superseded; cited as the history of a thesis or term, whose change is the point -->
<!-- inactive-ok-file: CLAIM-115 — Superseded by CLAIM-220; cited as it stood, not as what the record now holds -->

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
- It does not say the record makes every dropped commitment visible. A
  move that fits none of the record's schemes or relations was never
  filed, so dropping it from a draft leaves no trace against the record
  either ([CLAIM-181](CLAIM-181.md)). The record shows what was dropped only of what it
  held.

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
exchange. The empirical part, scoped to that exchange, is now [CLAIM-324](CLAIM-324.md), on
which this claim rests, as it already rests on [CLAIM-177](CLAIM-177.md). This claim
keeps the rest and stays interpretive: the general form, that a draft
written straight from an exchange behaves this way, generalizes from
one case, and the remedy is a proposal. Its title already states the
general form, so it was kept.

## Note of 2026-10-29: what holds it back

It generalizes from one exchange ([CLAIM-324](CLAIM-324.md)) to any draft written straight
from an exchange, and the comparison its defeat condition names has not been
made: no draft written against the record has been checked, beside one
written straight from an exchange, for dropped commitments and unannounced
changes of thesis.

## Note of 2026-11-18: what holds it back

Reviewed again. Its revisions since the note of 2026-10-29 (versions 3 to 5)
are line bookkeeping and a bears_on edge. The general form still rests on
one exchange ([CLAIM-324](CLAIM-324.md)), and the comparison its defeat condition names, a
draft written against the record checked beside one written straight from an
exchange, has not been made.

## Note of 2026-11-25: the exchange "Hyper article interpretation", U16 and U19

<!-- inactive-ok-block: CLAIM-tmp48g02 ADR-143 — new or Proposed; the reference-implementation claim filed from the same exchange, and the manuscript protocol -->
The owner stated this claim's practice as a requirement on 2026-11-22, the day before [ADR-143](../decisions.d/ADR-143.md): "this article should be demonstrating the point by example as well. it ought to be peppered with luria references, since that's what  is  supposed to be grounding the essay" (U16), and "The cases in the article should be invoking CASEs that are persisted in Nucleation. The claims in the article should be backed by CLAIMs and TERMs and ARGs (and maybe SYNTHESIS or even other stuff) in Nucleation. ... This paper is intended to be later persisted with Nucleation as one of the views it is describing" (U19). That is [ADR-143](../decisions.d/ADR-143.md)'s invariants 2, 3 and 7 in the owner's words, with one addition: a manuscript arguing that a paper should be a view over a record should itself be one. The exchange also holds the material for the comparison this claim's defeat condition names: drafts written straight from the exchange (A28, A32, A34, A38) beside drafts ChatGPT wrote against the record's entries after U19 (A41, A42, A45). They were not compared for dropped commitments; the second set's citations were checked in its filing and are mostly right. [CLAIM-tmp48g02](CLAIM-tmp48g02.md) records how far the record implements the publishing proposal these drafts make. The note is the assistant's (Claude, in this session), quoting the owner; adopting it is the owner's call. No status change.

## Note of 2026-11-25: the exchange "Hyper article interpretation", U10

<!-- inactive-ok-block: CLAIM-tmpkvi10 CLAIM-tmpbvvmp — new and Proposed; the owner's many-views thesis and A's claim about the separation it reduces -->
The owner, at U10 of the exchange: "this manner of publishing also collapses the impetus to share a flood of interrelated papers. I can provide the single tangle of ideas to evaluate, and present different views on it to different parties with differing and diverse interests." That takes this claim from one manuscript to many, filed as the owner's [CLAIM-tmpkvi10](CLAIM-tmpkvi10.md), which rests here. ChatGPT's A24 reads the owner's account of their motivation (U9) as a separation between the form in which knowledge is developed and the form in which it becomes institutionally legible, which a view over the record reduces ([CLAIM-tmpbvvmp](CLAIM-tmpbvvmp.md), also resting here). The note is the assistant's (Claude, in this session), quoting the owner; adopting it is the owner's call. No status change.

## Note of 2026-11-25: views of views, from "Hyper article interpretation", U23 to U28

<!-- inactive-ok-block: CLAIM-tmpxkeu9 CLAIM-tmp6xzjy CLAIM-tmpd1a2h CLAIM-tmpc4q8o — new; the owner's atlas thesis, the cycle check, the coverage claim and the owner's route thesis -->
The exchange's last turns rest on this claim and extend it. ChatGPT, at
A53, names it "the manuscript-as-view claim" among the proposal's
ancestors, correctly. The owner's U23 reads the whole record's views as an
atlas of charts ([CLAIM-tmpxkeu9](CLAIM-tmpxkeu9.md)); the assistant's gap fill
([CLAIM-tmp6xzjy](CLAIM-tmp6xzjy.md)) shows why this claim's practice matters for that
reading: a view whose every step passes through the record cannot be
pairwise consistent and jointly inconsistent, while views related to one
another directly can. A57's coverage dimensions ([CLAIM-tmpd1a2h](CLAIM-tmpd1a2h.md)) keep
this claim's separation of inclusion from status, as a view's review
status against its claims' standing. The owner's U28 adds series of posts
as routes through the views ([CLAIM-tmpc4q8o](CLAIM-tmpc4q8o.md)), a view of views. The note
is the assistant's (Claude, in this session). No status change.

## Note of 2026-11-25: the exchange "Hyper article interpretation", U1 and U2

<!-- inactive-ok-block: CLAIM-tmpjf44i TERM-tmpjn06u TERM-tmpx49xx — new and Proposed; the owner's hyperarticle thesis, its term, and the owner's feed -->
The owner opened the exchange with "github dmarx/nucleation as a "hyper article "" (U1) and "an essay advocating the hyperarticle for modern scientific publishing via living documents and attribution" (U2). That takes this claim from the record's own manuscripts to scientific publishing: what is published is the work, and a paper is one view of it. It is filed as the owner's [CLAIM-tmpjf44i](CLAIM-tmpjf44i.md), which rests here, with its word as [TERM-tmpjn06u](../terms.d/TERM-tmpjn06u.md) (ChatGPT's definition at A5). At U5 the owner gave a view a memory ("A 'view' (with a memory) over data", [TERM-tmpx49xx](../terms.d/TERM-tmpx49xx.md)), which this claim's views do not need: a manuscript drawn from the record is a view over a memory the record keeps. The note is the assistant's (Claude, in this session), quoting the owner; adopting it is the owner's call. No status change.
