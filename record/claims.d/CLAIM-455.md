---
number: 455
status: Active
formerly:
- CLAIM-tmp23fhq
title: 'For one bounded observer, a transformation of a representation can make one task''s distinction legible and another''s illegible at once, so legibility regimes are ordered only relative to a task, and a regime that improves one perspective''s competence can disable another''s'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in CASE-154's table, or a task-independent order on
  representations for a fixed bounded observer under which the raw pair
  and its XOR compare the same way for both tasks. Not defeated by
  Blackwell's order between the representations for an unbounded
  receiver (CLAIM-199), which bounds what is possible and is not what
  this observer can use.
tags:
- information-theory
- epistemology
- self-governance
date: '2026-10-27'
line:
- distributed-agency
- formal-apparatus
grounds:
- CASE-154
complements:
- CLAIM-199
uses:
- TERM-064
summary: >-
  Stated in [CASE-154](../cases.d/CASE-154.md)'s title and its "What it can show" and held by no
  claim, found in the audit of 2026-10-27 for propositions cases state
  that no claim holds. With two fair bits and an observer that reads one
  coordinate and cannot compute XOR, the raw pair gives 50% error on the
  XOR task and 0% on the first bit, and the XOR gives the reverse.
  [CLAIM-199](CLAIM-199.md) says a garbling can raise usable information for a receiver;
  this adds that the same garbling lowers it for another task of the same
  receiver. The edge: one observer, two tasks; nothing about which task
  matters.
---

# CLAIM-455: For one bounded observer, a transformation of a representation can make one task's distinction legible and another's illegible at once, so legibility regimes are ordered only relative to a task, and a regime that improves one perspective's competence can disable another's

## The claim

[CASE-154](../cases.d/CASE-154.md)'s construction: X₁, X₂ independent fair bits, and an observer
that reads one coordinate and cannot compute XOR. The raw pair
U = (X₁, X₂) gives error 50% on Q_A = X₁ ⊕ X₂ and 0% on Q_B = X₁; the
compressed V = X₁ ⊕ X₂ gives 0% and 50%. Passing from U to V makes Q_A
legible and Q_B illegible for the same observer, so neither representation
is better for that observer apart from the task. [CASE-154](../cases.d/CASE-154.md): "a learned
legibility regime can be competence-enhancing for one perspective and
disabling for another, with no task-independent sense in which it is
better or worse."

It completes [CLAIM-199](CLAIM-199.md). That claim holds that a garbling can raise a
given receiver's usable information, but never above what the source
makes possible; V is a garbling of U, and it raises the observer's usable
information on Q_A. What [CLAIM-199](CLAIM-199.md) does not say is that the same garbling
lowers it on Q_B. Legibility ([TERM-064](../terms.d/TERM-064.md)) is relative to an observer and a
task, and the construction shows the task argument cannot be dropped even
with the observer fixed.

## What it does not say

- **Which task should win.** Choosing a regime is choosing whose
  distinction counts, a normative question the construction does not
  touch ([CLAIM-348](CLAIM-348.md)).
- **That the observer could not learn XOR.** The observer is bounded by
  stipulation; a richer observer orders U above V by Blackwell's order.
- **Anything about real institutions.** [CASE-154](../cases.d/CASE-154.md)'s examples (reporting
  that forecasts output better and registers grievances worse) are
  illustrations, not findings.
