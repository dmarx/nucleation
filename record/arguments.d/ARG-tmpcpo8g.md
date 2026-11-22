---
status: Proposed
title: 'Dunfield and Krishnaswami''s survey, as evidence, shows synthesis reading a type off a term as a fact and checking holding a term to a type given as a requirement, which supports reading the two as the two directions of fit, and shows that neither moves the term, so that the update that moves a term to fit lies outside checking, where the survey does not go'
version: 1
form: evidence
grounds:
- THEORY-tmptsz1u
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
  Whether the reading of Dunfield and Krishnaswami (THEORY-tmptsz1u, in NOTE-tmpbrc1z)
  supports CLAIM-tmpnookt's correspondence between bidirectional typing
  and direction of fit. It supports it for what the type is taken as: a
  fact when synthesized, a requirement when checked, in the authors' own
  words. It does not support reading checking as an update: both modes
  are tests on a term that stays fixed, and the claim's placing of the
  performative half in elaboration or coercion is untouched by the
  survey and waits on LEAD-tmp7mkn0. The objection that mode is not direction of
  fit is held in CLAIM-tmpugw2q. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpnookt TERM-tmp8b1yl — Proposed; the claim argued about and the term it is stated in -->
<!-- inactive-ok-file: THEORY-tmptsz1u CLAIM-tmpugw2q — Proposed; the reading of Dunfield and Krishnaswami (2021) and the entries filed from it, or the entries it bears on -->

# ARG-tmpcpo8g: Dunfield and Krishnaswami's survey, as evidence, shows synthesis reading a type off a term as a fact and checking holding a term to a type given as a requirement, which supports reading the two as the two directions of fit, and shows that neither moves the term, so that the update that moves a term to fit lies outside checking, where the survey does not go

## The inference

CLAIM-tmpnookt says that bidirectional typing splits typing into
"inference, which reads a type off a term (the type is written to fit the
term: word to world, a descriptor), and checking, which holds a term to a
type given in advance (world to word, a requirement)", that "Checking only
accepts or rejects", and that the update that moves the term to fit "is
elaboration or coercion". THEORY-tmptsz1u reports:

- the synthesized type is a "fact" and the checked type a "requirement",
  joined by a rule that "verifies that a fact … is consistent with a
  requirement" (§4.4);
- inference "finds all behaviours, not only the intended behaviours",
  while annotations "force programmers to write down the behaviours they
  intend" (§9.1);
- the term is an input in both modes (§1), and a checker's check
  "returns a boolean" (§9.1);
- elaboration appears only as type systems that "automatically insert
  implicit operations" (§1) and in cited titles.

## Critical questions (evidence)

- **Would the evidence be expected if the claim were false?** The
  fact-and-requirement wording would be expected anyway if it were only
  the authors' phrasing for input and output. It is more than that in
  §9.1, where the choice of checking over inference is argued from
  intent: inference describes what the program does, annotation states
  what it should do. So the support is real for the requirement reading
  of checking, and for synthesis as description.
- **Does it tell the claim apart from its rivals?** The rival is that
  bidirectional typing is only information flow, which type is known,
  with no direction of fit in it. The survey leans that way itself
  ("the essence of bidirectional typing is the management of information
  flow", §8.4) and shows modes reversed and combined with the term's
  standing unchanged (§6.4, §6.5). That rival is held as CLAIM-tmpugw2q. The
  survey does not decide between them: in the standard recipe the two
  readings coincide.
- **Does the measure measure what it is said to?** The survey describes
  type systems, not updates. It shows that checking is a test, which the
  claim already says. It says nothing about what moves a term, beyond
  the programmer's adding annotations, which under type erasure changes
  no behaviour (§2, §3.2). So it cannot bear on the claim's elaboration
  half.

## Verdict

Supports, narrowed, the bidirectional bullet of CLAIM-tmpnookt: synthesis
and checking correspond to description and requirement in what the type
is taken as, in the standard recipe. It does not support reading the
split as informative against performative update, and leaves the
elaboration half where it was. It does not meet the claim's defeat
condition (b): the correspondence does not fail on its own terms; it is
narrower than stated.
