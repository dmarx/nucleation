---
number: 1084
status: Active
formerly:
- THEORY-tmpq9x5h
title: 'Simon proposes that ill structured problems can be handled by an alternation between a solver working on a problem that is well structured at each moment and a recognition and retrieval system that keeps modifying the problem space from memory or the environment, that a serial solver gains nothing by assembling the problem space at the outset, and that nothing but the size of the knowledge base may separate ill from well structured problems, so that no qualitatively new mechanisms are needed'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted by the twenty-second status review, at the status review's
    ruling (the owner delegated these rulings); ADR-065, ADR-057. The title
    reports what Simon proposes, NOTE-1232 read the paper in full from the
    published article, and nothing in the record contradicts the report. The
    old promote_when asked that the proposal be right: "A system built only
    from the components Simon names, a solver working in a locally well
    structured problem space and a recognition-driven retrieval mechanism
    that keeps modifying that space from a large memory or from the
    environment, shown to perform on problems of the ill structured kind
    (design under requirements that arrive during the work, with no fixed
    initial solution test) comparably to a system or expert given the full
    specification at the outset, with the gap traced to the size or content
    of its memory and not to a missing mechanism. The converse settles it
    the other way: a class of such problems on which that architecture fails
    at any memory size and a qualitatively different mechanism succeeds. A
    system that solves a problem once someone has formalized it does not
    count, since that is the preparation the claim is about." It moves word
    for word to THEORY-tmpstm9o, Proposed, which carries the thesis and
    extends this entry (ADR-065 §3; ADR-047, kind 1).
tags:
- cognition
- epistemology
date: '2026-10-27'
source:
- LIT-1634
summary: >-
  Simon (1973), [LIT-1634](../literature.d/LIT-1634.md), read in [NOTE-1232](../notes.d/NOTE-1232.md). The alternation is
  described for an architect, matched to a 1923 account of battleship
  design by an organization and to the NSS chess program, and argued from
  the seriality of the solver; nothing is implemented or tested, and Simon
  states the last part as what his analysis "suggests" and as "reason to
  be optimistic". Active as a report of the proposal; whether it is
  right, which wants a test, is THEORY-tmpstm9o, Proposed.
---
<!-- inactive-ok-file: CLAIM-470 — Proposed; the claim whose defeater this bears on, cited as open -->

# THEORY-1084: Simon proposes that ill structured problems can be handled by an alternation between a solver working on a problem that is well structured at each moment and a recognition and retrieval system that keeps modifying the problem space from memory or the environment, that a serial solver gains nothing by assembling the problem space at the outset, and that nothing but the size of the knowledge base may separate ill from well structured problems, so that no qualitatively new mechanisms are needed

## Source

Simon (1973), [LIT-1634](../literature.d/LIT-1634.md), §§3–5 (pp. 187–200); read in [NOTE-1232](../notes.d/NOTE-1232.md).

## What was actually shown

**The architecture, by description.** For house design, following Reitman's
analysis of a composer writing a fugue: the task evokes attributes to
specify, requirements, an executive program and generators of alternatives,
component by component, and "During any given short period of time, the
architect will find himself working on a problem which, perhaps beginning
in an ill structured state, soon converts itself through evocation from
memory into a well structured problem" (p. 190). The system is "a GPS, which
at any given moment finds itself working on some well structured subproblem,
with a retrieval system, which continually modifies the problem space"
(pp. 191–192; Fig. 1). The same form is found in Murray's account of
battleship design, where the evoking is the consulting of departments and
long-term memory is "literally a distributed memory" (p. 194); in a robot,
whose problem is "well structured … at each moment … but one that changes
from moment to moment" (p. 195); and in a production-based chess program
whose effective problem space moves through the large space of its memory
(p. 196).

**The argument from seriality.** A serial solver can bring little
information to bear over any short period, so most of a large memory is
irrelevant at any moment (p. 192). Assembling everything relevant "once and
for all at the outset" gains nothing: "bringing it together where?";
retrieval would still be needed, and the result "would still look like a
series of transformations of the problem space" (pp. 192–193).

**The thesis.** "Any problem solving process will appear ill structured if
the problem solver is a machine that has access to a very large long-term
memory … and/or access to a very large external memory" (p. 197). "It
suggests that there may be nothing other than the size of the knowledge base
to distinguish ISPs from WSPs", and that mechanisms that work on large,
apparently well structured domains "should be extendable to ill structured
domains without any need for introducing qualitatively new components"
(p. 197). Programs of 1958–1973 already did some of this "unknowingly"
(NSS chess, GPS planning; pp. 199–200).

## What this does not say

- **That it has been tested.** No system of this design is built or run in
  the paper. Simon flags his inexperience with large semantic stores
  (p. 198) and sets aside the two hard sources of new information, natural
  language instructions and perception (pp. 198–199).
- **That revision of a problem space creates distinctions.** In the paper,
  what enters the space is "generated from, or dredged from" memory or a
  library (p. 188), so the revision it models is mostly selection within a
  larger fixed store; the robot's revising its "laws of nature" (p. 195) is
  the exception, and is not developed. That bears on [CLAIM-470](../claims.d/CLAIM-470.md)'s
  defeater (a), and does not settle it.
- **That the alternation is costless or safe.** Simon's own design account
  has requirements violated after being satisfied and criteria never evoked
  (p. 191), and an acquisition process that conserves "existing problem
  formulations" (p. 199).
- **Anything about a parallel solver.** The argument from seriality is the
  premise.
