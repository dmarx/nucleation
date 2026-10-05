---
number: 134
status: Active
formerly:
- THEORY-tmp4t87t
title: 'Whether a system can persist is a question about a constraint set fixed independently of its dynamics: a set is viable when from each of its states some evolution can stay in it, and when it is not, its viability kernel is the largest part that is, from the rest of which every evolution leaves in finite time'
version: 1
tags:
- mathematics
- complex-systems
date: '2026-10-05'
source:
- LIT-714
summary: >-
  Aubin's viability theory, read in his 1999 mini-course notes
  [LIT-714](../literature.d/LIT-714.md). Given dynamics and a set K of required states, K is viable if
  some evolution from each state stays in K and invariant if every one
  does. Nagumo's theorem reduces viability to a tangency condition. The
  viability kernel is the largest viable subset of K; from outside it
  every evolution exits K. The notes do not compare viability with
  stability; that contrast is a further step.
---
<!-- inactive-ok-file: THEORY-128 — Proposed; the reef-recovery account, named for a parallel -->
<!-- inactive-ok-file: LIT-738 — Deferred, unread; Aubin's monograph, named as the general theory the notes restrict -->

# THEORY-134: Whether a system can persist is a question about a constraint set fixed independently of its dynamics: a set is viable when from each of its states some evolution can stay in it, and when it is not, its viability kernel is the largest part that is, from the rest of which every evolution leaves in finite time

## Source

Aubin (1999), [LIT-714](../literature.d/LIT-714.md), read in [NOTE-576](../notes.d/NOTE-576.md): the introduction and
chapters 1–2 of the mini-course notes. The monograph that founds the theory,
[LIT-738](../literature.d/LIT-738.md), is unread.

## What was actually shown

These are theorems, not findings, and they hold under their conditions:
finite-dimensional states, continuous dynamics with linear growth, and a
closed or locally compact K.

- **Two separate inputs.** Aubin's notes ([LIT-714](../literature.d/LIT-714.md)) define viability
  relative to a dynamics f and a set K that is given separately. An
  evolution is viable if it stays in K. K is viable if from every state in
  it at least one evolution stays in it, and invariant if all do. Viability
  "depends only on the behavior of f on K".
- **A local test.** By Nagumo's theorem, K is viable exactly when at each of
  its states the velocity f(x) lies in the contingent cone of K: nowhere
  does the dynamics force the state out.
- **The kernel.** When K is not viable, the states of K from which some
  evolution stays in K for ever form the viability kernel. It is the
  largest viable subset of K, and from every other state of K every
  evolution leaves K in finite time. The capture basin of a target is the
  set of states from which some evolution reaches it in finite time.

## What this does not say

- **Nothing here compares viability with stability.** The notes' "Stability
  Properties" (§2.6) concern whether viability survives limits of sets,
  not stability of an equilibrium or attractor. The claim that a regime can
  be stable (it returns to its pattern) without being viable (it cannot
  keep satisfying what it needs) is a correct consequence of the
  definitions, since nothing ties an attractor to K. But it is a step taken
  by whoever applies the theory, not something the source states.
- **K is not supplied by the theory.** Everything depends on specifying the
  constraint set independently of the dynamics. For a cell or an
  organization, which constraints count as "required" is the hard
  question, and viability theory takes the answer as given.
- **One evolution suffices.** Viability asks whether some evolution can
  stay in K. With a single deterministic evolution per state, viability and
  invariance coincide. The interesting cases, controls or set-valued
  dynamics, are in the unread monograph.

## Connections

- **Organizational autonomy.** Barandiaran, Di Paolo & Rohde ([LIT-566](../literature.d/LIT-566.md))
  call the network that constitutes an agent "precarious", and Montévil &
  Mossio ([LIT-582](../literature.d/LIT-582.md)) define organisation by closure of constraints. Reading
  precariousness as a small kernel, or a state near the kernel's boundary,
  is the record's suggestion; no relation is declared.
- **Reef recovery ([THEORY-128](THEORY-128.md)).** Hughes et al.'s reversible phase shift is
  a case where a degraded state was still inside the capture basin of the
  coral-dominated one, once herbivory was restored. The parallel is the
  record's.
