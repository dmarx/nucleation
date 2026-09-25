---
number: 62
status: Skimmed
formerly:
- NOTE-tmpjtzwb
paper: LIT-051
title: 'Başar, Meyn & Perkins, control system theory notes'
version: 1
date: '2026-09-25'
summary: >-
  A first-year graduate course in state-space control. It covers linear (mostly continuous-time) system modelling, structural properties (stability, controllability, observability), feedback synthesis (pole placement, observers, tracking), and optimal control via dynamic programming and HJB, including the LQR solution, and the minimum principle.
---

<!-- inactive-ok-file: LIT-051 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-062: Başar, Meyn & Perkins, control system theory notes

## Contribution

These are the three authors' lecture notes for UIUC's graduate course ECE 515 (formerly ECE 415), which follows an undergraduate frequency-domain control course. They emphasise state-space techniques in four parts: modelling, analysis of structural properties, synthesis of observers, compensators and controllers against design specifications, and optimization. Linear systems are the focus, with nonlinear systems treated only for stability and dynamic optimisation. Continuous time gets more depth than discrete time. The goals are sound design principles for feedback loops that respect the information available about the state, and familiarity with computational tools.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Outline (PDF bookmarks): Part I covers modelling and analysis (Ch. 1 state-space models with linearisation, the inverted pendulum and transfer functions; Ch. 2 vector spaces; Ch. 3 solutions of state equations). Part II covers structural properties (Ch. 4 stability; Ch. 5 controllability; Ch. 6 observability, duality and minimality). Part III covers feedback (Ch. 7 pole placement and observer feedback; Ch. 8 tracking and disturbance rejection; Ch. 9 design goals). Part IV covers optimal control (Ch. 10 DP and HJB; Ch. 11 the minimum principle).
- Preface, "Notes for the 2024 edition": examples in the early chapters also appear in Meyn's monograph *Control Systems and Reinforcement Learning* (CUP). Part 1 was revised to clarify the relation to RL "without relying on any theory from stochastic processes". A Fig. 1.1 error was corrected.
- Ch. 1 opening: the design methodology is model-based, so a simple model that is accurate enough is preferred. Linearity is the main approximation, and it works because physical laws are often linear and controllers are designed to be robust.
- Ch. 10: the general cost V(u) = ∫ℓ(x,u,τ)dτ + m(x(t1)) leads to HJB, the LQR solution via the Riccati equation and the Hamiltonian matrix, the infinite-horizon regulator, and the return-difference equation. Ch. 11 derives the minimum principle from HJB and Lagrange multipliers and includes nonlinear examples.

## Open questions

- It is background reference for control-theoretic views of optimisation and RL. Ch. 10 (HJB/LQR) is the part most often invoked in ML (linear-quadratic RL, continuous-time views of training dynamics).
- It is a textbook, not a claim. It would only be filed as a source if a practice or theory note needs a citable derivation (e.g. LQR or Lyapunov stability).
