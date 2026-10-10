---
status: Proposed
title: 'Telling an interpreter about a communicative situation, do(I = a), is a different intervention from changing the situation, do(S = s), so the effect of a cue is evidence about interpretation under instruction, not about whether the act changed'
version: 1
role: thesis
defeated_if: >-
  For the cues the manuscript's experiments use,
  P(Y | do(I = "S is s")) = P(Y | do(S = s)) for every situation feature
  cued; or manipulating actual speaker authority or commitments and
  merely informing interpreters of them change act classifications in the
  same way. Either way, telling and making would be interchangeable.
tags:
- causality
- pragmatics
date: '2026-10-10'
line: pragmatic-transport
answers:
- QUESTION-tmpwa1vj
rests_on:
- CLAIM-127
grounds:
- LIT-tmph1v0q
complements:
- CLAIM-tmpw83rc
- CLAIM-127
uses:
- TERM-018
- TERM-030
- TERM-tmp4ztih
summary: >-
  The owner proposed Pearl's do() at U41, and A129 §1 drew the
  distinction. It recurs at A151, A191, A203, A214 and A218. [CLAIM-127](CLAIM-127.md) is
  about where the index sits in the formalism; this claim is about what
  an experiment manipulates. The sharp edge: in a vignette or rating
  study every manipulation is a do(I).
---
<!-- inactive-ok-file: NOTE-tmpyye85 — Skimmed; the reading of four excerpts of Pearl, cited as a partial reading, which it is -->
<!-- inactive-ok-file: CLAIM-127 CLAIM-115 — Proposed; open, and cited as open: the claim is under test, not settled -->
<!-- inactive-ok-file: CLAIM-tmpw83rc — Proposed; the constitution thesis this claim complements, cited as open -->

# CLAIM-tmp2i7yj: Telling an interpreter about a communicative situation, do(I = a), is a different intervention from changing the situation, do(S = s), so the effect of a cue is evidence about interpretation under instruction, not about whether the act changed

## The claim

The owner at U41, on A125's intervention kernel: "this feels to me like an
opportunity for Judea Pearl's `do()` notation." A129 §1 wrote the structural
model ([CLAIM-127](CLAIM-127.md)) and separated three operations. The one this claim is
about is the third:

- P(Y | S = friend), which "conditions on naturally occurring situations";
- P(Y | do(S = friend)), which "describes a hypothetical intervention
  replacing the structural mechanism governing the speaker's role";
- P(Y | do(I = "speaker is a friend")): "This changes what the interpreter
  has been told. It need not change who actually spoke."

In Pearl's calculus ([LIT-tmph1v0q](../literature.d/LIT-tmph1v0q.md)) do(S = s) replaces S's structural equation
and leaves the others in place. do(I = a) replaces I's. The two act on
different variables, and nothing in the model makes their effects on Y
equal. A129 drew the experimental consequence: "a model prompted to
interpret a line as affectionate teasing is not necessarily responding to
the same causal manipulation as a reader told that the speaker is an
intimate friend."

A191 §6 turned the distinction on the ontology. Its table compares four
interventions, each with its question:

| Intervention | Ontological question |
|---|---|
| Change wording while retaining role and norms | Does the communicative act persist despite altered realization? |
| Change speaker authority while retaining wording | Does the act's normative character change? |
| Change the reader's information while retaining the actual situation | Are judgments changing, or has the communicative event itself changed? |
| Change conversational history | Are prior commitments constitutive of the present act? |

Of the third row: "If we merely tell participants that an utterance is a
reprimand, and they subsequently classify it as a reprimand, we have
learned something about interpretation under instruction. We have not
necessarily demonstrated that the underlying speech act changed." A203 §16:
"A stronger test would manipulate actual speaker authority, conversational
commitments, or the circumstances under which the utterance is performed."
The distinction recurs at A151 §3, A214 §9 and A218 Ch10.4 and Study 4.

So the effect of a cue is evidence about how interpretation responds to
instruction. It bears on which relations are constitutive of an act
([TERM-tmp4ztih](../terms.d/TERM-tmp4ztih.md); [QUESTION-tmpwa1vj](../questions.d/QUESTION-tmpwa1vj.md)) only through a do(S). The record had the words
already: a frame is a property of the situation ([TERM-030](../terms.d/TERM-030.md)), and "Telling
a reader that the speaker is a friend is an intervention" ([TERM-018](../terms.d/TERM-018.md)). This
claim draws the consequence for what an experiment can show. It
complements [CLAIM-tmpw83rc](CLAIM-tmpw83rc.md), which says the act is partly constituted by its
relations to participants and norms: only an intervention on those
relations tests that.

## What it does not say

It does not say the two effects differ in fact. That is the defeat
condition. It does not say the structural model is identified. A129's
caption: "Schematic causal model, not a uniquely identified causal graph."
It does not say that attributed-speaker studies are useless. They measure
interpretation, which is what [CLAIM-115](CLAIM-115.md)'s thesis is about.

The sharp edge is that do(S) is rarely available. In a vignette or rating
study every manipulation is a change in what the reader is told. That
includes the "speaker authority, interpersonal history, or the norms
governing the exchange" that A214 §9 proposes to manipulate. Under
[TERM-018](../terms.d/TERM-018.md) each is a framing intervention, a do(I). A214's "intervening on the
communicative situation", which "may change the performed act", is not
available in such a design. [CASE-021](../cases.d/CASE-021.md)'s factorial study manipulates "attributed speaker
identity", which is a do(I). A do(S) needs an interactive or field design,
where the speaker's role or the conversation's history is actually
changed, or an interpreter that is a model whose context is the situation
itself.

## Note of 2026-10-10: the book read in part

[LIT-tmph1v0q](../literature.d/LIT-tmph1v0q.md) has now been skimmed in four excerpts the author posts
([NOTE-tmpyye85](../notes.d/NOTE-tmpyye85.md)). The rest of the book was not read.

- **The gloss holds.** "do(S = s) replaces S's structural equation and
  leaves the others in place" is what pp. 158 and 417 say.
- **"do(I = a) replaces I's" needs a qualification.** The surgery deletes
  "the equation for" a variable (p. 417), and A129's model, as
  [CLAIM-127](CLAIM-127.md) quotes it, gives I no equation: I is an exogenous input. So
  do(I = a) sets I. It does not replace a mechanism unless the model says
  how I is chosen. The claim's distinction is untouched by this. do(I) and
  do(S) still act on different variables, and nothing makes their effects
  on Y equal.
- **Why a vignette study is a do(I).** On Pearl's account a randomized
  experiment is a surgery that cuts a variable's usual link and gives it a
  new mechanism, a coin (p. 418). A rating study that assigns what
  participants are told does that to I, and to I only. That supports the
  claim's "sharp edge". A do(S) needs the same cut made on the situation
  itself.
