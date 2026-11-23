---
status: Open
title: "What are the query side's payoff and the equilibrium concept of a query–target game in its diagnostic and developmental forms, where the two sides are not opponents, and in coevolving dynamics where neither side's update is a best response?"
version: 1
tags:
- game-theory
- society-and-governance
- epistemology
date: '2026-11-23'
line:
- readiness
- learning-and-inquiry
summary: >-
  A gap fill (ADR-137) for A50 §§3–4 of the exchange "Explain First Contact
  RL" (2026-11-23). A50 gives a loss only for the adversarial form of its
  game; the diagnostic and developmental forms' objectives are named in a
  table, and its coupled dynamics S_{t+1} = F(S_t, q_t, a_t),
  ρ_{t+1} = G(ρ_t, a_t, S_{t+1}) carry no payoff for either side. Without
  them the owner's game (CLAIM-tmp61i14) has players but no solution
  concept outside the zero-sum case (CLAIM-tmp62ldm). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-tmp61i14 CLAIM-tmp62ldm CLAIM-tmp2oloi CLAIM-tmpep410 — Proposed; the thesis, the formulation and the analysis this question is left open by -->

# QUESTION-tmpn4we1: What are the query side's payoff and the equilibrium concept of a query–target game in its diagnostic and developmental forms, where the two sides are not opponents, and in coevolving dynamics where neither side's update is a best response?

## Why it is open

CLAIM-tmp2oloi's table gives the diagnostic query side the objective
"Reveal actual capabilities and limitations" and the developmental one
"Generate informative challenges that extend capabilities". Neither is a
loss to the target, so the zero-sum minimax that CLAIM-tmp62ldm analyses
does not apply. A50's §4 dynamics are adaptation rules, not best
responses, and its toy model (CLAIM-tmpep410) is a consensus dynamic with
no payoff at all.

## Candidate answers

- **Diagnostic:** the query side's payoff is information about the target's
  response law, as in optimal experimental design or adaptive testing; the
  target is a responder, not a player, unless it can shape what it shows,
  which is the adversarial form again.
- **Developmental:** a leader–follower (Stackelberg) or teaching game, where
  the query side commits to a curriculum and is paid in the capability the
  target gains, which A50's ℓ does not measure.
- **Coevolving:** an evolutionary or learning-dynamics solution concept, a
  rest point or attractor of F and G, which need not be an equilibrium of
  any game; the toy model's rest points are set by initial conditions.

An answer says, for each form, whose payoff, over what, and which solution
concept; or shows that the game frame adds nothing beyond a one-sided model
of demands and realizations, which would bear against CLAIM-tmp61i14.
