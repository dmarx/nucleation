---
number: 695
status: Active
formerly:
- THEORY-tmpz1eac
title: "Two quantum states can be broadcast if and only if they commute, and cloned if and only if they are identical or orthogonal; the theorem is proved for invertible density operators and marks a line within quantum theory, not a witness of nonclassicality"
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-16'
source:
- LIT-018
summary: >-
  Fuchs (1995), [LIT-018](../literature.d/LIT-018.md), §4.3, read in full in [NOTE-021](../notes.d/NOTE-021.md), from the
  Barnum–Caves–Fuchs–Jozsa–Schumacher manuscript. Fidelity cannot decrease
  under partial trace or under the broadcasting map, so broadcasting forces
  equality conditions that make ρ0 commute with the optimal-fidelity
  operator. Proved for invertible ρ0, ρ1 only. Spekkens' epistricted
  classical theories ([LIT-007](../literature.d/LIT-007.md)) reproduce no-broadcasting, so the theorem
  states where broadcastability ends inside quantum theory and does not by
  itself certify nonclassicality.
---

# THEORY-695: Two quantum states can be broadcast if and only if they commute, and cloned if and only if they are identical or orthogonal; the theorem is proved for invertible density operators and marks a line within quantum theory, not a witness of nonclassicality

## Source

Fuchs (1995), PhD thesis, [LIT-018](../literature.d/LIT-018.md), §4.3, read in full in [NOTE-021](../notes.d/NOTE-021.md). The
section is "based largely on a manuscript submitted to Physical Review
Letters" with Barnum, Caves, Jozsa and Schumacher (p. 113, fn. 3).

## What was actually shown

**Definitions.** A broadcasting process sends ρ_s to a joint state whose
two marginals both equal ρ_s (Eq. 4.49). Cloning is the product special
case ρ_s ⊗ ρ_s (Eq. 4.50). The allowed processes are the most general
ancilla, unitary and partial-trace maps (Eq. 4.51).

**Theorem.** {ρ0, ρ1} can be broadcast iff [ρ0, ρ1] = 0 (Eq. 4.101), and
cloned iff F(ρ0, ρ1) ∈ {0, 1}, i.e. the states are identical or orthogonal
(Eqs. 4.52, 4.81). The "if" directions are by construction (Eqs. 4.53–4.55).

**Proof.** Fidelity cannot decrease under partial trace (Eq. 4.74) or under
the broadcasting map (Eq. 4.79). Broadcasting therefore forces
F_A = F(ρ̃0, ρ̃1) = F_B (Eq. 4.80). The equality conditions force the
operators in the fidelity bound to coincide with the optimal-fidelity
operator M (Eqs. 4.89–4.97), hence [ρ0, M] = 0 and so [ρ0, ρ1] = 0
(Eqs. 4.98–4.103). Of the candidate broadcast states, the perfectly
entangled one cannot be produced by any physical map when
S(ρ0) ≠ S(ρ1) (Eqs. 4.105–4.109).

**What could have come out otherwise.** Some non-commuting mixed pair could
have admitted a broadcast with correlated, non-product output, as mixed
states escape the pure-state no-cloning argument. It does not.

## What this does not say

- **That non-invertible mixed pairs are covered.** The proof assumes
  invertible ρ0 and ρ1 "to simplify the exposition" (p. 118). Pure states
  are covered separately by no-cloning, but mixed pairs that are not of
  full rank are covered by neither, as written ([NOTE-021](../notes.d/NOTE-021.md), Limitations).
- **That no-broadcasting marks nonclassicality.** The thesis says
  broadcasting "makes a communication theoretic cut between commuting and
  noncommuting density operators, and thus between classical and quantum
  state descriptions" (p. 114). It never considers restricted classical
  theories. Spekkens' epistricted classical statistical theories ([LIT-007](../literature.d/LIT-007.md))
  list no-broadcasting among the phenomena they reproduce. [NOTE-021](../notes.d/NOTE-021.md) records
  that both hold, since they answer different questions; [LIT-007](../literature.d/LIT-007.md)'s entry is
  asserted rather than derived, so the two cannot be compared at the level
  of proof.
- **That eavesdroppers acting on whole strings are covered.** The thesis
  extends the theorem to block systems informally, from its being
  dimension-free (p. 121; [NOTE-021](../notes.d/NOTE-021.md), C15, moderate).
- **Any trade-off between information gained and disturbance.** The
  general inference–disturbance relation (Eq. 4.31) is left unsolved.

## Connections

- The fidelity properties the proof rests on are [THEORY-584](THEORY-584.md).
- Interference, another phenomenon often read as nonclassical, has a local
  epistemically restricted classical model in the fragment [LIT-019](../literature.d/LIT-019.md) treats
  ([THEORY-403](THEORY-403.md)). The same school's toy bit theory is [THEORY-474](THEORY-474.md).
