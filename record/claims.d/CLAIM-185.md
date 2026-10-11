---
number: 185
status: Proposed
formerly:
- CLAIM-tmpu984q
title: 'The nucleation threshold of an argument is whatever makes a structure persist: a persistent structure is available as an anchor, and more complex structure can evolve only on anchors'
version: 1
role: thesis
defeated_if: >-
  Complex structure (claims resting on claims, objection threads,
  revision chains) is found to form as readily on content that never
  persisted, content restated afresh each time and never addressable,
  as on content that did. Or a trigger of persistence is found that
  reliably leaves its structure unused as an anchor, so that
  persistence and anchoring come apart.
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
grounds:
- LIT-919
- LIT-920
summary: >-
  The owner's reframing of 2026-10-11, after two readings showed that no
  physical nucleation threshold is a count. The threshold is not
  recurrence as such but whatever triggers persistence. Recurrence is
  the trigger this record is built around ([CLAIM-176](CLAIM-176.md)), and there are
  others. The readings fit the reframing: a physical nucleus is defined by
  persistence, and seeds that do not persist lose their power. Proposed:
  the generalization is stated, not tested.
supports:
- CLAIM-176
- CLAIM-182
objected_by:
- CLAIM-184
---
<!-- inactive-ok-file: CLAIM-176 CLAIM-177 CLAIM-186 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->

# CLAIM-185: The nucleation threshold of an argument is whatever makes a structure persist: a persistent structure is available as an anchor, and more complex structure can evolve only on anchors

## The claim

The owner, on 2026-10-11: "I'd propose reframing the nucleation threshold
as anything that triggers persistence. Persistent structures that are
available to serve as anchors is what permits more complex structure to
evolve on top of it."

The claim has two parts. First, what matters at the threshold is not how
a thing got there but that it now persists. Second, persistence matters
because it makes the thing available as an anchor. Later structure can
point at it, rest on it, object to it or revise it, and structure that
points at nothing cannot accumulate. A claim with no persistent premise
has to restate its premise, and restating is where redefinition creeps in
([CLAIM-177](CLAIM-177.md)).

The physics read for this line fits the reframing better than it fits a
count:

- Vekilov ([LIT-919](../literature.d/LIT-919.md), [NOTE-708](../notes.d/NOTE-708.md)) defines a nucleus as a cluster with
  "equal probabilities of growth and decay". The threshold is the size at
  which a cluster becomes as likely to persist as to dissolve, and the
  size moves with the driving force. What is fixed is the persistence
  criterion, not a number.
- Ostwald ([LIT-920](../literature.d/LIT-920.md), [NOTE-709](../notes.d/NOTE-709.md)) shows that a seed acts only while
  it persists. Volatile seeds evaporate and lose their power, unstable ones
  decompose, and heat sterilizes. Stable seeds, such as alum dust, persist
  and go on seeding a whole laboratory.

The record has several triggers of persistence, and recurrence is only one
of them:

- **Recurrence.** A thing gets a code the second time it turns up
  ([ADR-032](../decisions.d/ADR-032.md); [CLAIM-176](CLAIM-176.md)).
- **A choice.** A decision is filed when an alternative is rejected, on its
  first occurrence ([LU-ADR-001](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-001.md)).
- **A source.** A work is registered as a LIT when the record needs to
  cite it, not when it has been cited twice.
- **A request.** The owner asks for something to be filed. The growth-rate
  claim, [CLAIM-186](CLAIM-186.md), was filed this way, before any second occurrence.
- **Being written down at all.** A workbench entry makes a session persist
  whether or not anything in it recurs.

Each of these makes a thing addressable: it gets a code or a dated path
that later entries can point at. That is the anchor. Lint keeps the anchor
from rotting silently: a reference to a code that no longer resolves fails.

## What it does not say

- It does not say every trigger is equally good. Recurrence also throttles
  capture, and a request does not. Which trigger fits which case is a
  separate question, and [CLAIM-176](CLAIM-176.md) keeps recurrence's case.
- It does not say persistence is enough. An anchor no one points at
  anchors nothing, and the second defeater above names that case.
- It does not say the physics proves the reframing. The readings show that
  persistence is how the physical threshold is defined, which makes the
  analogy hold where a count did not. That is a better analogy, not
  evidence about arguments.
