---
status: Proposed
title: 'In liquid types, as in Freeman and Pfenning''s refinement types, checking moves no program, and a refinement that fails to check does not show that the program fails it: inference returns Failure whenever no conjunction of the given qualifiers can be verified by a conservative check, so the failure may lie in the program, in the qualifier set or in the checker, and every remedy the paper names, adding a qualifier, inserting a run-time check or changing the program, lies outside the checker'
version: 1
role: counter
warrant: interpretive
defeated_if: >-
  A rule of the paper's system, or of DSOLVE as it describes it, that
  changes a program, inserts a check or coercion, or otherwise moves a
  program to fit a type it failed; or a passage showing that the paper's
  Failure is reported only for programs that are unsafe, so that a failure
  locates the fault in the program. A later liquid-type system that
  inserts checks would not defeat this claim, which is about this paper's
  system; it would be a case of the elaboration CLAIM-tmpnookt names.
tags:
- logic
- software-engineering
- epistemology
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
objects_to:
- CLAIM-tmpnookt
complements:
- CLAIM-tmp764wb
grounds:
- THEORY-tmp01mu6
uses:
- TERM-tmp8b1yl
- TERM-134
summary: >-
  Filed from the reading of Rondon, Kawaguchi and Jhala (THEORY-tmp01mu6,
  NOTE-tmpnd1kd) for LEAD-tmp3xevc, answering its question of what happens
  to a program whose refinement fails. It widens CLAIM-tmp764wb from
  Freeman and Pfenning's declared lattice to the predicate form, and adds
  what that claim could not: under a finite vocabulary and a conservative
  check, failing to check is not failing. It objects to the half of
  CLAIM-tmpnookt's direction-of-fit correspondence that reads checking as
  requirement. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp01mu6 CLAIM-tmpnookt CLAIM-tmp764wb TERM-tmp8b1yl — Proposed; the reading this rests on, the claim it objects to, the counter it widens, and the term it is stated against -->

# CLAIM-tmpcmt21: In liquid types, as in Freeman and Pfenning's refinement types, checking moves no program, and a refinement that fails to check does not show that the program fails it: inference returns Failure whenever no conjunction of the given qualifiers can be verified by a conservative check, so the failure may lie in the program, in the qualifier set or in the checker, and every remedy the paper names, adding a qualifier, inserting a run-time check or changing the program, lies outside the checker

## The claim

CLAIM-tmpnookt reads checking, holding a term to a type given in advance,
as the world-to-word direction (TERM-tmp8b1yl), with elaboration or
coercion as the move that fits a term to its type. CLAIM-tmp764wb found
that in Freeman and Pfenning's system checking moves nothing. Liquid types
(THEORY-tmp01mu6) are the predicate form that CLAIM-tmpnookt actually
writes, and the same holds there, with one thing more.

**Nothing moves the program.** Types given in advance, such as sub's
a : intarray → i : {ν : int | 0 ≤ ν ∧ ν < len a} → int (p. 163), are
checked through the same subtyping constraints as inferred ones; Solve
changes only the assignment of qualifiers, and "If Infer(Γ, e, Q) =
Failure then there is no S s.t. Γ ⊢_Q e : S" (Theorem 2, p. 166). DSOLVE
"outputs [...] the set of applications of primitive operations that could
not statically be proven safe" (p. 167).

**Failing to check is not failing.** "there may be safe programs which
cannot be well-typed in our system due either to an inappropriate choice
of qualifiers or the conservativeness of our notion of subtyping"
(p. 160), and the authors list as future work telling "whether there is
either an error in her program, the set of qualifiers is insufficient, or,
the conservativeness of the system is to blame" (p. 169). A Failure is
consistent with a program that passes the type.

**Every remedy is outside the checker.** "we can use the readable results
of the inference to manually add more qualifiers, and [...] to insert a
minimal set of run-time checks" (p. 160), the latter by Flanagan's hybrid
type checking, proposed and not done here; and the programmer fixed the
bounds error DSOLVE found in BITV's blit, after which "DSOLVE successfully
typechecks the fixed version" (p. 168). The first moves the vocabulary,
not the program; the second and third move the program, by another tool
or by hand.

So in this system too the direction of fit does not divide checking from
inference: both ask whether the program as it stands passes. For the
record it adds a distinction TERM-tmp8b1yl's criterion needs when tests
are checked by a procedure: a test the entry passes can fail to be
verified, so a failed check is not by itself a world-to-word test. Under
a closed vocabulary and a conservative check, the entry, the vocabulary
and the check are three places a failure can lie.

## What it does not say

- Not that checking never fits a term to a type in any system. Hybrid type
  checking, which this paper cites for run-time checks, inserts them; it
  is the elaboration CLAIM-tmpnookt names, in another system, and the lead
  has not read it.
- Not that the record's own checks are conservative. Most of its tests are
  decided by reading the entry; the distinction bites where a check is a
  procedure that can miss, a lint or a reviewer.
