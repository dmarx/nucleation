---
number: 127
status: Proposed
formerly:
- CLAIM-tmpansqo
title: 'Conditioning on a communicative situation, intervening on it and intervening on what the interpreter is told are three different operations, so a framing intervention should index the empirical model, e_C^a = P(Y_C | do(a)), not enter its cover as one more context'
version: 2
history:
- version: 2
  date: '2026-10-10'
  note: >-
    Provenance corrected and the three operations restated. The do()
    move is the owner's, at U41 (2026-10-09 07:34): "this feels to me
    like an opportunity for Judea Pearl's `do()` notation". A129 §1 and
    §5 formalized it. The review relayed later that day restates A129
    §5. Version 1 named observing, conditioning and intervening as three
    operations. In Pearl's calculus, observing a value and conditioning
    on it are one operation. A129's three are P(Y | S = friend),
    P(Y | do(S = friend)) and P(Y | do(I = "speaker is a friend")).
    Version 1 also said that no entry carries the refinement and that the
    record has no causal model. The refinement is A129's. A129 §1 gives a
    schematic structural model, which it says is not identified. The
    defeated_if stands.
role: thesis
defeated_if: >-
  Every framing intervention the manuscript's experiments use can be
  written as a measurement context in the cover, or as conditioning on
  an observed context variable, without changing any compatibility,
  contextuality or signalling verdict on the data; so that the do-index
  separates nothing the cover does not already separate.
tags:
- causality
- contextuality
date: '2026-10-09'
line: pragmatic-transport
grounds:
- LIT-894
uses:
- TERM-018
- TERM-030
- TERM-039
complements:
- CLAIM-125
- CLAIM-130
summary: >-
  The owner's do() move at U41, formalized at A129 §1 and §5 and restated
  in the review relayed the same day. A129 keeps three operations apart:
  conditioning on the situation, intervening on it, and intervening on
  what the interpreter is told. It keeps one cover, with the empirical
  laws indexed by intervention. The link to signalling is the record's
  extrapolation, and A129's own graph gives a second route to it.
supports:
- CLAIM-130
---
<!-- inactive-ok-file: NOTE-696 — Skimmed; the reading of four excerpts of Pearl, cited as a partial reading, which it is -->
<!-- inactive-ok-file: CLAIM-125 — Proposed; cited as the open problem this claim bears on, not as settled -->
<!-- inactive-ok-file: CLAIM-130 CLAIM-052 — Proposed; open, and cited as open: the claim is under test, not settled -->
<!-- inactive-ok-file: THEORY-177 — Proposed; Dzhafarov's direct influences, cited for what they imply here, not as settled -->

# CLAIM-127: Conditioning on a communicative situation, intervening on it and intervening on what the interpreter is told are three different operations, so a framing intervention should index the empirical model, e_C^a = P(Y_C | do(a)), not enter its cover as one more context

## The claim

The owner at U41, on A125's proposal of "an intervention kernel K_a acting
on a communicative or interpretive state": "this feels to me like an
opportunity for Judea Pearl's `do()` notation."

A129 §1 answered with three operations ([LIT-894](../literature.d/LIT-894.md)):

- P(Y | S = friend), which "conditions on naturally occurring situations in
  which the speaker is a friend";
- P(Y | do(S = friend)), which "describes a hypothetical intervention
  replacing the structural mechanism governing the speaker's role";
- P(Y | do(I = "speaker is a friend")): "This changes what the interpreter
  has been told. It need not change who actually spoke."

The first is conditioning. The second and third are interventions on
different variables. The experimental consequence of the difference between
them is [CLAIM-130](CLAIM-130.md).

A129 §1 writes them in a structural model. Z = (U, S, A, K, N, G, H) is the
communicative situation, R the interpreter's state, I "externally supplied
framing information or instructions", C a measurement protocol
([TERM-039](../terms.d/TERM-039.md)) and Y the judgement:

- R′ = f_R(R, Z, I, ε_R),
- Y = f_Y(R′, Z, C, ε_Y).

Its diagram's caption: "Schematic causal model, not a uniquely identified
causal graph." It is to be "a separate causal layer, not a replacement of
the sheaf layer."

A129 §5 puts the layers together as a causally indexed observational
system 𝔠 = (𝒮, 𝒜, ℳ, ℰ, {e_C^a}, 𝒬), with "e_C^a: empirical distributions in
context C under intervention a", and e_C^a = P(Y_C | do(a)). The review the
owner relayed later the same day restates this: "make causal interventions
and observational contexts separate indexed structures from the outset:
e_C^{do(a)} = P(Y_C | do(a)). That would connect our recent Pearl-inspired
refinement to the sheaf structure without treating observation,
conditioning, and intervention as the same operation." The refinement it
names is U41 and A129.

The record already draws the distinction in words. A frame is a property of
the communicative situation ([TERM-030](../terms.d/TERM-030.md)); a framing intervention is "an action
that changes the conditions under which an utterance is interpreted"
([TERM-018](../terms.d/TERM-018.md)). Telling a reader that the speaker is a friend is not the same as
the speaker's being one. What the record lacks is a place for the
distinction in the formalism. In the sheaf-theoretic setting a context is a
set of jointly measured observables, and the empirical model assigns each a
distribution. Nothing there says whether an elicitation only reads the
interpreter's state or changes it. In A129 the cover ℳ is the same for
every intervention; what varies with a is the family {e_C^a}. That an
intervention might also change the cover is the record's extension, not
A129's, and nothing in the exchange argues it. Transport is then compared
across a family of models indexed by intervention, and no intervention is a
context inside one of them.

A129 also derives the framing kernel instead of positing it:
K_a(r′ | r, z) = P(R′ = r′ | R = r, Z = z, do(I = a)). That gives [TERM-026](../terms.d/TERM-026.md)'s
operators and [CLAIM-052](CLAIM-052.md)'s noncommutativity a causal reading. Its equations
have one step, so K_bK_a needs time-indexed states, which it does not write.

## Why it matters for the open problems

This part is the record's extrapolation, not the review's. [CLAIM-125](CLAIM-125.md)'s second
open problem is that language data signal. In the corpus data Wang et al.'s
journal follow-up measured, 69 of 90 noun–verb systems signal. The
manuscript's experiments elicit judgements instead, and A35 §6 had already
warned that "forcing a participant to make an explicit judgment is itself an
intervention." If an elicitation is an intervention, then reading one
observable can change the interpreter's state. That change can show up as a
dependence of another observable's marginal on context, which is signalling.
The do-index gives this hypothesis a form that can be tested: models elicited
under different interventions are compared separately, not pooled into one
cover, and the elicited data can be checked for signalling beyond the
corpus baseline.

### Two routes to signalling

A129's graph lets C enter only f_Y. So in A129's own model an observable's
marginal can depend on its context with no change to R. That is a direct
influence of context in Dzhafarov's sense ([THEORY-177](../theory.d/THEORY-177.md)). The route the
extrapolation above assumes is elicitation changing the interpreter's
state. A35 §6, quoted in [TERM-018](../terms.d/TERM-018.md), says "forcing a participant to make an
explicit judgment is itself an intervention". That route needs an arrow
from C into f_R, and A129's graph has none. Which route holds is empirical.
Sequential designs, where one judgement is elicited before another,
separate them ([TERM-039](../terms.d/TERM-039.md)).

## What it does not say

It does not say the signalling in corpus data comes from elicitation. Corpus
estimates involve no elicitation at all. It does not say interventions
violate the no-signalling condition. Nor does it say Pearl's calculus
applies as it stands. A129's model is schematic, one-step and not
identified, and the record files no causal model of the interpreter.

## Note of 2026-10-10: the book read in part

[LIT-894](../literature.d/LIT-894.md) has now been skimmed in four excerpts the author posts
([NOTE-696](../notes.d/NOTE-696.md)): the contents, the second-edition preface, §§5.3.2–5.4.1
and the Epilogue. The rest of the book was not read.

- **Version 2's correction holds.** In those pages observing a value is
  conditioning on it. The conditional bar reads "given that we see" (p.
  421), E(Y | x) is "the standard conditional or observational
  expectation" (p. 158), and a passive observation "should not violate any
  of the equations" (p. 158). The Epilogue names two components of science,
  "Observations and interventions" (p. 421). The review's three-way list
  "observation, conditioning, and intervention" is not Pearl's.
- **The gloss of do() holds.** Under do(X = x) the equation for X "should be
  overruled and replaced with the equation X = x", and the others are
  solved as they stand (p. 158; the "surgery" of p. 417).
- **A sharpening the claim should carry.** Surgery deletes "the equation
  for" the variable (p. 417). In A129's model as quoted above, I is
  "externally supplied" and has no equation of its own. When an experiment
  assigns I and nothing else causes it, intervening on I and conditioning
  on its assigned value give the same distribution. That follows from the
  calculus's second rule (p. 423) and is the point of Pearl's account of
  randomization (p. 418); the inference is the reader's, not a sentence of
  the excerpts. So for I the do() notation separates something only where
  I is not assigned, as in corpus data. The claim's case for indexing
  e_C^a by a, and not adding a to the cover, does not rest on that
  difference. It concerns where a sits in the formalism, and it stands.
- **Elicitation.** §5.4.1 separates conditioning on a measurement taken
  under an intervention, P(y | do(x), z), from intervening on it,
  P(y | do(x), do(z)) (pp. 160–161). Whether an elicitation C is the first
  kind or the second is the question this claim's "two routes to
  signalling" leave open.
