---
status: Active
title: 'Under unitary evolution, two states of a quantum system can each leave a record in another system while themselves staying undisturbed only if they are orthogonal or the record does not distinguish them; so the outcomes that can be recorded repeatably form an orthogonal set, a result that uses only unitarity and repeatability and not the Born rule'
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
source:
- LIT-tmpb4amz
summary: >-
  Zurek (2009), LIT-tmpb4amz, eq. (5), read in NOTE-tmpvsoha. From
  |u⟩|e₀⟩ → |u⟩|e_u⟩ and |v⟩|e₀⟩ → |v⟩|e_v⟩, preservation of the scalar
  product gives ⟨u|v⟩ = ⟨u|v⟩⟨e_u|e_v⟩, so either the record is no record
  or ⟨u|v⟩ = 0. Zurek reads this as the origin of the outcome set of the
  collapse postulate. It does not give single outcomes, probabilities or
  which orthogonal set is chosen; that is the interaction's.
---
# THEORY-tmp08c0w: Under unitary evolution, two states of a quantum system can each leave a record in another system while themselves staying undisturbed only if they are orthogonal or the record does not distinguish them; so the outcomes that can be recorded repeatably form an orthogonal set, a result that uses only unitarity and repeatability and not the Born rule

## Source

Zurek (2009), LIT-tmpb4amz, section III, p. 5 of the arXiv preprint
0903.5082; read in NOTE-tmpvsoha.

## What was actually shown

**The setting.** Postulates (i) states are Hilbert-space vectors, (ii)
evolution is unitary, (iii) "Immediate repetition of a measurement yields
the same outcome" (p. 4). Suppose states |u⟩ and |v⟩ of S "produce an
imprint in a subsystem of E (which plays a role of an apparatus), but remain
unperturbed (so they can produce more imprints)":
|u⟩|e₀⟩ ⇒ |u⟩|e_u⟩, |v⟩|e₀⟩ ⇒ |v⟩|e_v⟩ (p. 5).

**The argument.** A unitary preserves scalar products, so with
⟨e₀|e₀⟩ = 1, ⟨u|v⟩ = ⟨u|v⟩⟨e_u|e_v⟩ (eq. 5). This "can be satisfied only
when; (a) either ⟨e_u|e_v⟩ = 1 (which means that copying was completely
unsuccessful), or; (b) ⟨u|v⟩ = 0", in which case ⟨e_u|e_v⟩ is arbitrary and
a perfect record, ⟨e_u|e_v⟩ = 0, is possible (p. 5). The argument holds for
imperfect records too: any ⟨e_u|e_v⟩ ≠ 1 forces orthogonality.

**The reading.** "As a consequence of unitarity, only sets of orthogonal
states … can be so copied, explaining selection of a set of outcomes –
terminal points of quantum jumps" (p. 5). It "relies on just two values of
the scalar product – 0 and 1 – and, thus, does not appeal to Born's rule"
(p. 5). It is the reason copying many records into disjoint fragments is
possible at all without violating no-cloning: what is copied is an
observable's eigenstates, not an unknown state (p. 4).

**What could have come out otherwise.** A record that distinguished two
non-orthogonal states and left both undisturbed would falsify it; eq. (5)
rules that out exactly, not approximately. The paper also relaxes the
assumptions: E need not start pure (ref. [23]), and repeatability can be
transferred to an apparatus A, whose orthogonal pointer states then
correlate with non-orthogonal states of S, giving POVMs (p. 6).

## What this does not say

- **Not which orthogonal set.** The argument shows the recorded set must be
  orthogonal; that it is the einselected pointer basis comes from the
  interaction ("Interaction Hamiltonians do not perturb observables that
  commute with them", p. 5), not from eq. (5).
- **Not that one outcome occurs.** Eq. (5) explains the first part of the
  collapse postulate, the set of outcomes. The single outcome per run is
  handled elsewhere in the paper by the "perception of 'collapse'" as
  observers acquire a branch fragment (p. 6), an interpretation, not a
  derivation.
- **Not probabilities.** Those come in section IV from envariance, a
  separate and contested argument.
- **Not that non-orthogonal states cannot be measured.** They can be, by
  moving repeatability to an apparatus (p. 6). The constraint is on what is
  repeatably recorded while left undisturbed.
- **Not new in this paper.** It cites ref. [23] (Zurek, Phys. Rev. A 76,
  2007, "Quantum origin of quantum jumps") for the result and its
  relaxations; that paper is not held.
