---
status: Proposed
title: "Davies and Pfenning's checking judgment, which takes its type from the programmer's ascription and passes it down to subterms, by analogy, shows that checking holds a term to a type given in advance, world to word, as against synthesis"
version: 1
form: analogy
grounds:
- THEORY-tmpei9b5
concludes:
- CLAIM-tmpnookt
uses:
- TERM-tmp8b1yl
tags:
- logic
- philosophy-of-language
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  The route by which the reading of Davies and Pfenning (THEORY-tmpei9b5)
  bears on CLAIM-tmpnookt's correspondence of the direction of fit with
  bidirectional typing's split. It holds for the checking side, narrowed:
  the checked type is the programmer's, given in advance, and a term that
  fails it is the one to change. It does not hold as stated for the
  synthesis side, since most synthesized types are declared types read
  from the context, not types written to fit the term. Whether an
  ascription its term already meets is a requirement the paper leaves
  open, so two readings are set out as alternatives. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpei9b5 CLAIM-tmpnookt CLAIM-tmp764wb TERM-tmp8b1yl — Proposed; the reading, the claim this is about, and the counter and term it is weighed against -->

# ARG-tmp7pf1t: Davies and Pfenning's checking judgment, which takes its type from the programmer's ascription and passes it down to subterms, by analogy, shows that checking holds a term to a type given in advance, world to word, as against synthesis

## The inference

CLAIM-tmpnookt: inference "reads a type off a term (the type is written to
fit the term: word to world, a descriptor)", and checking "holds a term to
a type given in advance (world to word, a requirement)". Davies and
Pfenning's checker has the two modes: synthesis, Γ ⊢ I ↑ A, and checking,
Γ ⊢ C ↓ A (pp. 6–7).

## Critical questions

- **Is the checked type given in advance?** Yes. It comes from an
  ascription, which the paper says "allows the programmer to specify
  types" (p. 6), mostly on function definitions, and is passed down: a λ's
  body is checked against the codomain, an argument against the function's
  domain, each case branch against the type of the whole (Figure 3).
- **Is a failure laid on the term?** Yes. double fails its ascription;
  the ascription stands and the term is to be fixed (p. 10). In that case
  the checked type is world to word in TERM-tmp8b1yl's sense on any
  reading.
- **Is the synthesized type written to fit the term?** Mostly not. An
  ascription "checks C against A and then yields A as the synthesized
  type" (p. 6), and variables synthesize the types the context declares.
  Only constants and constructors (ε ↑ nat, I 1 ↑ pos) are read off the
  term's shape. So the synthesis side of the correspondence is narrowed:
  in this system synthesis mostly passes on a requirement already checked
  elsewhere, which the context then relies on as a description. The same
  ascription is a requirement on its term and a description to its uses.
- **Is a met ascription a requirement?** The paper does not say: inc
  passes its ascription, and nothing tells whether the type was written
  before the code. Two readings, filed here as alternatives for the
  owner:
  - *Alternative 1, with CLAIM-tmp764wb and TERM-tmp8b1yl's criterion*:
    the term as it stands settles the direction, so a met ascription is a
    descriptor, and only a failing one (double) is world to word. Then the
    modes do not divide the directions; checking is where the world-to-word
    case can arise.
  - *Alternative 2, with the parallel reading of Dunfield and
    Krishnaswami (pull request 707)*: a type given in advance is a
    requirement whether or not the term meets it, so checking is world to
    word throughout and the correspondence holds for the checking side as
    stated.

  The paper's practice leans to the second: types are stated for what
  "the programmer" wants "statically verified" (p. 1), and a true but
  weaker ascription for inc "would have been insufficient" (p. 10), which
  only makes sense of a type chosen before the proof goes through. It is a
  lean, not a finding.

## Verdict

Supports CLAIM-tmpnookt's correspondence for the checking side, narrowed
to where the checked type comes from, and does not support it for the
synthesis side as stated. Proposed: which alternative holds is the owner's
call.
