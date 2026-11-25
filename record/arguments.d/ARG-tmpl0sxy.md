---
status: Proposed
title: 'Martin-Löf''s table of readings of the judgement that a is an element of A, in which a is a method of solving the problem A or a program meeting the specification A, shows by analogy that a question is a type whose answers are its elements, a problem defined by what counts as its solution, narrowed to specifications over a kind of thing already given'
version: 1
form: analogy
grounds:
- THEORY-tmp62cvo
concludes:
- CLAIM-949
uses:
- TERM-152
tags:
- logic
- epistemology
date: '2026-11-25'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  The route by which the reading of Martin-Löf ([THEORY-tmp62cvo](../theory.d/THEORY-tmp62cvo.md)) bears on
  [CLAIM-949](../claims.d/CLAIM-949.md)'s correspondences of a question with a problem and a
  realization with an inhabitant, [LEAD-215](../leads.d/LEAD-215.md)'s questions (a) and (c). The
  book states the reading itself: "a is a method of solving the problem
  (doing the task) A" and "a is a program ... which meets the
  specification A" (pp. 5–6). Narrowed by [CLAIM-tmpjs6hp](../claims.d/CLAIM-tmpjs6hp.md) to
  specifications over a kind of thing already given. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp62cvo CLAIM-949 TERM-152 CLAIM-tmpjs6hp — Proposed; the reading, the claims and the term this joins -->

# ARG-tmpl0sxy: Martin-Löf's table of readings of the judgement that a is an element of A, in which a is a method of solving the problem A or a program meeting the specification A, shows by analogy that a question is a type whose answers are its elements, a problem defined by what counts as its solution, narrowed to specifications over a kind of thing already given

## The inference

Source, [THEORY-tmp62cvo](../theory.d/THEORY-tmp62cvo.md): each form of judgement "admits of several
different readings" (p. 5). For a ∈ A: an element of a set, a proof of a
proposition, "a method of fulfilling (realizing) the intention
(expectation) A", "a method of solving the problem (doing the task) A";
and "'a is a method ...' can be read as 'a is a program ...' ... which
meets the specification A" (p. 6). A set is defined by what counts as its
canonical elements (p. 8), a proposition "by laying down what counts as a
proof" (p. 11).

Target, [CLAIM-949](../claims.d/CLAIM-949.md) with [CLAIM-470](../claims.d/CLAIM-470.md) and [TERM-152](../terms.d/TERM-152.md): a question fixes which
differences would count as an answer; a specification fixes which
realizations are admissible; a question is a problem, its answers the
elements of a type.

Mapping: set or problem to question or specification; element or method
of solving to answer or realization; "A is solvable" to the question's
having an answer; "a ∈ A presupposes that A is a set" (p. 5) to a
realization's being judged only against a specification already stated.

## Critical questions

- **Are the two alike in the respects the conclusion needs?** Closer than
  any reading so far: the book itself puts set, problem, intention and
  specification in one column and their elements in the next. [CLAIM-949](../claims.d/CLAIM-949.md)'s
  "Martin-Löf's types are the same reading" holds, and more strongly than
  for Kolmogorov, whose reading (pull request 708) keeps problems apart
  from statements, where Martin-Löf makes them two readings of one form.
- **Are there differences that defeat it?** One narrows it. A set is
  defined by how its canonical elements are formed, not by tests;
  [TERM-152](../terms.d/TERM-152.md)'s tests on candidates are the "such that" set over a base set
  (p. 53), and over no base set a category, which is not a set
  ([CLAIM-tmpjs6hp](../claims.d/CLAIM-tmpjs6hp.md)). A question whose answer space is not fixed in advance
  is the second case. A second difference does not defeat it: [CLAIM-470](../claims.d/CLAIM-470.md)'s
  question "fixes which differences would count as an answer", a
  partition of states; Martin-Löf's set fixes what counts as an answer and
  when two answers are equal (p. 8), which is that partition, the
  equality on canonical elements playing the role of the differences that
  do not count.
- **Is there a counter-analogy?** The table's readings are of judgement
  forms, not of propositions inside the theory: "in ordinary set theory
  a ∈ b and a = b are propositions, while they are judgements here"
  (p. 5). That an answer answers a question is then something asserted,
  not something the question contains, which fits the record, where a
  finding is filed by someone.

## Verdict

Supports [CLAIM-949](../claims.d/CLAIM-949.md)'s first two correspondences, narrowed to specifications
over a kind of thing already given. Proposed.
