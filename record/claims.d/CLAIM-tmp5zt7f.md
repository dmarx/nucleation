---
status: Proposed
title: 'Standing, availability and fidelity are separate'
statement: >-
  An entry's standing (whether the record endorses it), its availability
  (how readily it enters ongoing work) and its fidelity (at what level of
  detail it is kept) are separate properties that call for separate
  governance: retiring is an epistemic operation, cooling an allocation of
  attention and condensing a change of representation, and an entry's
  right value on one does not follow from its value on another
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that in the record's own use the right availability and
  fidelity of an entry are fixed by its status and kind, so that no entry
  in force should be harder to reach than another of its kind and no
  retired entry should be easier to reach than one in force; for instance,
  that recurring rejected arguments are no more often needed than other
  Rejected entries, and Active entries carried by a synthesis no less
  often than others.
tags:
- design-rationale
- information-retrieval
- databases
date: '2026-11-26'
line:
- records-of-inquiry
- record-as-apparatus
bears_on:
- QUESTION-tmpz8xkx
uses:
- TERM-tmp96b3g
- TERM-tmp3t5jq
summary: >-
  A27 §§1–2 of the exchange "Alignment consequences brainstorm" (ChatGPT,
  2026-11-26), answering the owner's U15 (CLAIM-tmpu1fef): "Luria
  currently distinguishes identity from standing. What you are proposing is
  a third independent dimension: availability", and then a fourth,
  fidelity. "Retirement is an epistemic operation. Cooling is a
  resource-allocation operation. Condensation is a representational
  operation." A29 §3 adds generation, how long an entry has survived, as
  one more dimension apart from temperature. A offered the thesis as a
  design principle for luria ("Memory must have a lifecycle independent of
  truth"); no principle is filed. The wording is A's (ChatGPT, in the
  exchange of 2026-11-26); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpu1fef TERM-tmp96b3g TERM-tmp3t5jq CLAIM-tmp48l62 CLAIM-tmpg2wk1 CLAIM-1208 — Proposed; filed from the same exchange on 2026-11-26 -->

# CLAIM-tmp5zt7f: Standing, availability and fidelity are separate

## The claim

A27 §2:

| Property | Question |
|---|---|
| Standing | Is this knowledge currently endorsed? |
| Availability | How readily should it enter ongoing inquiry? |
| Fidelity | At what level of detail should it be retained? |

"These should not be collapsed into a single lifecycle." A's table of how
kinds of entry would be treated is the argument:

| Entry | Standing | Availability | Fidelity |
|---|---|---|---|
| Foundational theory | Active | Hot | Full |
| Established lemma incorporated into a synthesis | Active | Warm | Condensed |
| Promising unexplored hypothesis | Proposed | Hot | Full |
| Dormant research direction | Proposed | Warm | Full |
| Frequently recurring rejected argument | Rejected | Hot | Condensed |
| Obsolete technical decision | Superseded | Cold | Full |
| Redundant formulation | Active or Superseded | Cold | Minimal stub |

The separating rows are the recurring rejected argument and the absorbed
lemma: "A rejected argument can be more operationally important than an
accepted one." A27 §9 gives the first a form, a "negative knowledge
capsule" kept hot while the full reasoning goes cold: the argument, its
failure condition, and when to reactivate it. "Knowing what not to repeat
is a capability."

A29 §3 adds a fourth dimension, generation, and keeps it apart from
availability: "A mature result can be cold because it is rarely needed; a
brand-new result can be hot because it is driving current work."
CLAIM-tmp48l62 is A's hypothesis about generations.

## What it rests on in the record

Standing is the record's status field; the other two are not represented.
The owner's U15 (CLAIM-tmpu1fef) is the case for availability. Fidelity has
a held basis: CLAIM-300's sufficiency relative to a family of decisions,
and CLAIM-1208's proof relevance, under which a finding's construction
must be kept only where a later step uses it.

## What it does not say

- How to set either new property. TERM-tmp96b3g gives the tiers and
  CLAIM-tmpg2wk1 a cost model; neither is part of this claim.
- That the three must be stored as three fields. A27 §11: "Adding a `tier`
  field would not, by itself, accomplish much"; what matters is the
  operational meaning each value has for search, views, review and agents.
