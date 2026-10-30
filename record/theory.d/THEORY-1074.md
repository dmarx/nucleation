---
number: 1074
status: Active
formerly:
- THEORY-tmphcxoi
title: 'In Di Biagio and Rovelli''s relational account two classical subsystems'' perspectives merge, agreeing on a variable''s value and on each other''s, when they couple to that variable or to each other, and a coupling to a complementary variable can remove a relative fact from a perspective that did not interact; that this answers the combination problem and keeps perspectives consistent is shown only in worked examples computed relative to a single outside system'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065, ADR-057. The title
    reports what the paper computes and that its general claims rest on
    worked examples computed relative to one outside system; NOTE-1214 read
    it in full from v2, no clause of the condition asks for v1, and nothing
    in the record contradicts the report. The old promote_when asked that
    the general claims be true: "A general result that, for any arrangement
    of commuting classical subsystems coupled unitarily, the relative facts
    that the states held relative to two different outside systems assign
    never conflict about the same variables, with the conditions on
    "coupling properly" stated; or a scenario meeting those conditions in
    which they do conflict, which would refute it. Further worked examples
    computed inside one joint distribution cannot settle it, because there
    agreement follows from probability theory. Neither can the
    local-friendliness theorems, which bear on absolute facts, not on
    agreement between perspectives." It moves word for word to
    THEORY-1213, Proposed, which carries the general claim and extends
    this entry (ADR-065 §3; ADR-047, kind 1).
tags:
- quantum-foundations
date: '2026-10-27'
source:
- LIT-1676
summary: >-
  Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), read from arXiv v2 in
  [NOTE-1214](../notes.d/NOTE-1214.md), §VI and Apps. D–E. The merge, and the disturbance of a
  third party's relative fact, are computed in a three-system example and
  in Wigner's friend. The general claims, a solution to
  RQM's combination problem and consistency of perspectives, are asserted,
  not shown; whether they hold is THEORY-1213, Proposed.
  Every computation is relative to one outside system, where agreement is
  automatic. This is the same gap [THEORY-621](THEORY-621.md) and [THEORY-1080](THEORY-1080.md) name.
---
<!-- inactive-ok-file: THEORY-621 — Proposed; the earlier statement whose consistency gap this restates, cited as open -->

# THEORY-1074: In Di Biagio and Rovelli's relational account two classical subsystems' perspectives merge, agreeing on a variable's value and on each other's, when they couple to that variable or to each other, and a coupling to a complementary variable can remove a relative fact from a perspective that did not interact; that this answers the combination problem and keeps perspectives consistent is shown only in worked examples computed relative to a single outside system

## Source

Di Biagio and Rovelli (2025), [LIT-1676](../literature.d/LIT-1676.md), arXiv 2510.11349v2, §VI
(pp. 4–5), App. D (pp. 9–10) and App. E (pp. 10–11); read in [NOTE-1214](../notes.d/NOTE-1214.md).

## What was actually shown

**The merge.** Relative to us, |+⟩|a0⟩|b0⟩ (eq. 13) becomes
(|0⟩|a0⟩ + |1⟩|a1⟩)|b0⟩/√2 when A correlates with Z (eq. 14), and then
(|0⟩|a0⟩|b0⟩ + |1⟩|a1⟩|b1⟩)/√2 when B correlates with A or Z (eq. 15). Then
I_{Z|A} = I_{Z|B} = I_Z^max and I_{A|B} = I_A^max: "A and B agree on the value
of Z and about each other's value" (p. 5).

**The disturbance.** If B instead correlates with X of the qubit, the state is
eq. (16). X is a fact relative to B, A is not a fact relative to B, and "Z is
not a fact relative to A anymore, even though A did nothing in this last
timestep … because the interaction between B and S disturbed Z and changed its
correlations with A" (p. 5). This case could have come out otherwise, and it
is the one the paper uses against Frauchiger–Renner: the superobservers
"change the correlation structure of the variables of the friends" (p. 5).

**Wigner's friend.** Relative to an outside O, after Wigner asks his friend,
H_Z = H_F = H_W = log 2 with I_{Z|F} = I_{Z|W} = I_Z^max and
I_{F|W} = I_F^max (D8). "the value of Z relative to F is the same as the value
of Z relative to W", which O can verify "by interacting with Z, F, and W in any
order" (p. 10). Wigner's check M = |ψ1⟩⟨ψ1| does not commute with F, yet it
leaves F's relation to S untouched and gives Wigner no information about Z or
F (p. 10).

**The extended scenario.** RQM keeps (E2): what Alice learns on opening the
box is what Charlie saw, "guaranteed by quantum theory". It denies (E1): "at no
time will p_QM satisfy (E1)" for the interference choice, and Charlie's outcome
"is not a stable fact with respect to Alice" (p. 11).

**The general claims are asserted.** "The merging of perspectives offers a
solution to RQM's combination problem … If the variables couple correctly so
as to get correlated, their perspectives will agree" (p. 5). There is no
general statement of "correctly" and no proof.

## What this does not say

- **That perspectives relative to different outside systems agree.** Each
  agreement above is read off one joint distribution, relative to "us" or to
  O. Inside one classical distribution, if Z is fixed by F and Z is fixed by
  W, the two agree by probability theory. The open question, which [THEORY-621](THEORY-621.md)
  and [THEORY-1080](THEORY-1080.md) also leave open, is agreement between descriptions held
  relative to different systems. The paper sets it aside with its rejection
  of questions about what "really" happened (§IX).
- **That merging is guaranteed.** It requires coupling "properly", and a
  coupling to a complementary variable does the opposite (eq. 16).
- **That relative facts can be combined into one global distribution.**
  App. E says they cannot (E3).
- **That intersubjective agreement among many observers is derived.** For
  that the paper relies on Zurek's quantum Darwinism (§VIII), cited and not
  shown.
