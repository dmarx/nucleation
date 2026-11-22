---
status: Proposed
title: 'Receiver-restricted informativeness order'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-100. Its results
    are CLAIM-tmp03h8w; its checks are CASE-tmphabte.
tags:
- information-theory
- mathematical-statistics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
draws_on:
- THEORY-1096
- THEORY-846
- THEORY-176
summary: >-
  An order on experiments (rendering procedures) about a finite set of
  situations, with outcomes in one medium, that compares them by the best
  risk a stated class of decision rules attains with each, rather than the
  best over all rules as Blackwell's order does. It is the order
  CLAIM-225 asked for under "What would answer it" and
  CLAIM-199 said it did not supply. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmp03h8w CASE-tmphabte — new, filed with this term -->

# TERM-tmpjv1xh: Receiver-restricted informativeness order

## Definition

- **Situations and medium.** Θ is a finite set of situations, with a prior
  π of full support. X is a finite medium in which renderings are made. An
  **experiment** (a rendering procedure) is a Markov kernel P from Θ to X,
  P(x | θ). Renderings in different media are compared on one medium, the
  disjoint union of the media, so that a text-to-image chain is a kernel
  on that union.
- **Decision problem.** A finite action set A and a bounded loss L(θ, a).
- **Receiver.** For each finite A, a nonempty set R_A of decision rules,
  kernels δ from X to A: the rules this receiver can apply. R̄_A is its
  closed convex hull. The unrestricted receiver has every rule.
- **Usable risk.** V_R(P; L, π) = inf over δ in R_A of
  Σ_θ π(θ) Σ_x P(x | θ) Σ_a δ(a | x) L(θ, a). For the unrestricted
  receiver it is the Bayes risk, which CLAIM-199 calls what a rendering
  makes possible; for R it is what the receiver can use.
- **Achievable set.** Ach_{R,A}(P) = { Pδ : δ in R̄_A }, the kernels from
  situations to actions the receiver can realise with P.
- **The order.** P ⪰_R P' when V_R(P; L, π) ≤ V_R(P'; L, π) for every
  finite A, every bounded loss L on it and every full-support prior π. For
  a family Q of problems, as CLAIM-050's communicative tasks, ⪰_{R,Q}
  quantifies over Q only.

With R unrestricted, ⪰_R is Blackwell's informativeness order on the
finite case (THEORY-1096's "every risk vector attainable with β is
attainable with α", read through the achievable sets).

## What it is not

- **Not Blackwell's order.** That order quantifies over every rule, and a
  garbling is never better under it. Under ⪰_R a garbling can be strictly
  better, and an experiment can be strictly worse than one it is a
  garbling of (CLAIM-tmp03h8w, result 5).
- **Not V-information.** Xu et al.'s quantity (THEORY-846) is a single number
  for log loss and one target. This is an order over all bounded losses,
  and it needs no target variable beyond the situation.
- **Not a stitching penalty.** THEORY-176's penalty compares two
  representations in one problem through a fitted map. This compares
  experiments by a receiver's fixed rule class over every problem.
- **Not a cost of recovery.** It fixes a class of procedures and a success
  criterion (risk) and says nothing of cost, so it is not an answer to
  QUESTION-110.

## What would settle it

The definition makes three choices the lead left open, as the assistant's.
Comparing on one medium (rather than a family of rule classes, one per
medium) is chosen because the disjoint union makes the two the same. All
full-support priors are quantified because the order is the same for each
(CLAIM-tmp03h8w, result 2), so the choice costs nothing. Rules may be
randomised, since a receiver's usable risk is the same over its rules as
over their mixtures.

The results that make it worth adopting are CLAIM-tmp03h8w's, checked
numerically in CASE-tmphabte.
