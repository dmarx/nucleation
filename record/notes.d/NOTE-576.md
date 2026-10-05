---
number: 576
status: Read
formerly:
- NOTE-tmpiyl1n
paper: LIT-714
title: 'The Method of Characteristics Revisited: A Viability Approach'
version: 1
history:
- version: 1
  date: '2026-10-05'
  note: >-
    Read: the arXiv v1 PDF, front matter, introduction, chapter 1 (§§1.1–1.3;
    the proofs of §1.4 skimmed) and chapter 2 (§§2.1–2.6). Chapters 3–6, on
    epiderivatives, Hamilton–Jacobi inequalities and boundary-value problems,
    were not read; nothing below rests on them. Page numbers are the notes'
    printed pages.
date: '2026-10-05'
summary: >-
  Viability is a property of a constraint set under a dynamics: K is viable
  if from every state some evolution stays in K, invariant if all do.
  Nagumo's theorem reduces viability to a tangency condition. When K is
  not viable, the viability kernel is the largest viable part of it, and
  everything else in K leaves in finite time. Stability in the Lyapunov
  sense is not discussed.
---
<!-- inactive-ok-file: LIT-738 — Deferred, unread; Aubin's monograph, named as the book these notes summarise -->

# NOTE-576: The Method of Characteristics Revisited: A Viability Approach

## Contribution

Lecture notes, not a research paper. Chapters 1–2 restate the viability
theorems and the viability kernel and capture basin from the author's
earlier work, for ordinary differential equations, as tools for solving
Hamilton–Jacobi equations later in the notes. For this record their value
is a first-hand, compact statement of the definitions.

## Key insight

Fix a set K of states you require, independently of the dynamics. Then ask
of each state whether some evolution from it can keep satisfying K. The
answer carves K into the viability kernel, which can, and the rest, which
cannot and will leave K in finite time however it evolves. Nothing about
attractors, equilibria or return to a pattern enters into it.

## Assumptions

- Finite-dimensional state space; dynamics x′ = f(x) with f continuous, and
  with linear growth for the chapter 2 results (the general theory uses
  set-valued maps; the notes restrict to equations "for the sake of
  simplicity", p. 4).
- K locally compact for Nagumo's theorem, closed for the kernel results.

## Key results

- **Definitions 1.1.1–1.1.2.** x(·) viable in K on [0, T] if x(t) ∈ K for
  all t. K locally viable if from any x0 ∈ K some solution is viable on some
  [0, T], T > 0; globally if T = ∞ is always possible. K invariant if every
  solution from K stays in it. A repeller: all solutions from K leave in
  finite time.
- **Theorem 1.3.1 (Nagumo).** K locally viable ⇔ f(x) ∈ T_K(x) for all
  x ∈ K, equivalently ⟨p, f(x)⟩ ≤ 0 for every normal p ∈ N_K(x).
- **Definition 2.1.3.** Viab_f(C, T): states of C from which some solution
  stays in C on [0, T]; Viab_f(C) for T = ∞. Capt_f(C): states from which
  some solution reaches C in finite time. Capt^K_f(C): from which some
  solution stays in K until it reaches C.
- **Proposition 2.1.5.** Viab_f(C) is the largest subset of C viable under
  f; C \ Viab_f(C) is a repeller.
- **Theorem 2.3.1.** The viability kernel is the largest closed D ⊂ K with
  f(x) ∈ T_D(x) for all x ∈ D.
- **Proposition 2.3.2.** From a compact set outside the kernel, every
  solution leaves K within a bounded time.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Viability (some evolution stays) and invariance (all do) differ, and coincide when solutions are unique | strong | definitions and remark, p. 7 |
| C2 | Viability of K is decided by the dynamics on K alone | strong | remark, p. 7 |
| C3 | Every closed K has a largest viable subset, and from the rest of K every evolution exits in finite time | strong | Propositions 2.1.5, 2.3.2; Theorem 2.3.1 |
| C4 | These results are "mathematical metaphors" of evolutionary economics, population dynamics and biological evolution | weak | asserted, p. 5; no application in chapters 1–2 |

## Concepts

- **viable evolution** — one that stays in the constraint set K over the
  horizon considered.
- **viability kernel** — the states of K from which at least one evolution
  stays in K for ever.
- **capture basin** — the states from which at least one evolution reaches
  a target in finite time.
- **repeller** — a set from every state of which every evolution leaves in
  finite time.
- **stability** (§2.6) — here, whether viability is preserved under limits
  of sets, not stability of a state or attractor.

## Connections

The notes credit Nagumo (1942) for the viability theorem and Frankowska for
the use of kernels and capture basins to characterise value functions.
They point to Aubin's monograph ([LIT-738](../literature.d/LIT-738.md)) for the general,
set-valued theory.

## Bearing on the record

Source of [THEORY-134](../theory.d/THEORY-134.md). The owner's essay (§6.1) cites "Aubin's
mathematical theory of viability" for the claim that stability and
viability are different questions. The notes support the half of that
claim that defines viability: a state space, admissible dynamics, an
independently specified constraint set, and the states that can keep
satisfying it over a horizon. They do not make the comparison with
stability. That step is the essay's, and it is sound only once the
essay says what the constraint set is for the system in question.

The record's organizational-autonomy accounts (Barandiaran, Di Paolo &
Rohde, [LIT-566](../literature.d/LIT-566.md)) call an agent's organization "precarious". The
viability kernel is one way to make that word precise: a system is
precarious where its kernel is small or its state is near the kernel's
boundary. That reading is the record's, not either source's.

## Limitations

- Deterministic single-valued dynamics only in these chapters; the
  set-valued case, where viability and invariance genuinely diverge, is in
  the monograph.
- No worked application outside mathematics in the chapters read.

## Open questions

How to specify K for a system whose constraints are partly set by the
system itself, as with an organism or an organization that changes what it
needs. The notes take K as given.
