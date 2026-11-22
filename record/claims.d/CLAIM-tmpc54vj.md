---
status: Proposed
title: 'For decisions that are functions of the input, the directed signature is the eigenspace of the self-adjoint two-step operator T T*, which is reversible, so directedness adds no obstruction beyond the symmetric case and enters only for decisions about the transport itself'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A directed transport is exhibited for which a decision that is a function of
  the input alone is served by the top-d left singular span of the
  conditional-expectation operator but not by the top-d eigenspace of the
  two-step operator M = T T*; or for which the same-kind pairing on inputs
  that the line's decisions turn on is not the reversible two-step chain M, so
  that directedness introduces for input-decisions an obstruction absent in
  the symmetric case.
tags:
- representation-learning
- mathematical-statistics
- mathematics
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
bears_on:
- QUESTION-052
grounds:
- CASE-tmp5w2ty
- THEORY-239
complements:
- CLAIM-210
- CLAIM-098
---
<!-- inactive-ok-file: CASE-tmp5w2ty — Proposed; the study that grounds this claim, filed with it on 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-209 — Proposed; the thesis this advances and the linear-case claim it sits beside, cited as open -->

# CLAIM-tmpc54vj: For decisions that are functions of the input, the directed signature is the eigenspace of the self-adjoint two-step operator T T*, which is reversible, so directedness adds no obstruction beyond the symmetric case and enters only for decisions about the transport itself

## The claim

[QUESTION-052](../questions.d/QUESTION-052.md) asks what replaces the top eigenspace as the decision-sufficient
signature when the pairing is directed, and [CLAIM-209](CLAIM-209.md) is faulted for naming
no signature. For decisions that are functions of the input x, the answer is
exact and needs no new object. The candidate — the top-d left singular span
span{μ₁…μ_d} of the conditional-expectation operator
`T: L²(P_A) → L²(P_X)`, `(Tg)(x) = E[g(A) | x]` — is, identically, the top-d
eigenspace of the self-adjoint, positive operator M = T T* on L²(P_X). M is
the two-step "same-kind on X" chain x → a → x′, and it is reversible with
respect to P_X (verified to 1e-17 in [CASE-tmp5w2ty](../cases.d/CASE-tmp5w2ty.md)). So for
input-decisions the directed problem **is** a symmetric problem, with M in
place of the symmetric positive-pair operator, and every symmetric-case
guarantee transfers with M: for linear probes this is exactly
[THEORY-239](../theory.d/THEORY-239.md)'s result (its guarantee "sits on the left functions μ_i"), and
the residue beyond linear probes is identical to the symmetric nonlinear
residue, not a new directed difficulty.

The directedness is real but is carried by the input–context relation
(μ_i ≠ ν_i for a non-reversible chain, [CASE-tmp5w2ty](../cases.d/CASE-tmp5w2ty.md)), and it bears on
decisions about the transport — which way it runs, or recovering the target a
from x — not on decisions about x. This is the operator-level form of
[CLAIM-210](CLAIM-210.md)'s split: kind-sharing is symmetric and fixes what is preserved,
while fidelity belongs to a directed transport. The symmetric M is the kind
side; the asymmetry of T is the transport side ([CLAIM-098](CLAIM-098.md)).

## What it does not say

- Not that the directed case is fully settled. It reduces input-decisions to a
  symmetric operator; whether the top eigenspace of M is the signature for
  **nonlinear** input-decisions is the symmetric residue of [QUESTION-052](../questions.d/QUESTION-052.md),
  and [CLAIM-tmpm4oom](CLAIM-tmpm4oom.md) argues no single span is, absent a fixed decision
  family. Decisions about the transport are left open and are where
  directedness bites.
- Not that M is the only defensible same-kind pairing on inputs. It is the one
  induced by composing T with its adjoint, and the claim chooses it because
  input-targets live in L²(P_X) and that composition is what makes the operator
  self-adjoint ([THEORY-009](../theory.d/THEORY-009.md)). A different pairing is the escape its defeat
  condition names.
- Not a claim about estimation, infinite spaces, or what training reaches.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
