---
number: 118
status: Proposed
formerly:
- CLAIM-tmpxrgp3
title: 'Context and interpreter are separate sources of interpretive change, told apart by what each carries and not by mechanism: what the current context supplies, whether held in activations or in weights updated on it and discarded after, is the signal; what earlier contexts have left in the interpreter and it carries into new ones is the interpreter; and improving the signal differs from improving the interpreter'
version: 4
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Grounds now also name the THEORYs filed from what the claim relies on:
    THEORY-439 (LIT-796, the same demonstrations used as context and
    as a training signal are not interchangeable), cited in the body as
    the case for at the level of the whole model, and THEORY-481
    (LIT-859, the outer training that produces the in-context learner).
    The claim is unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Relations corrected by the ninth status review (ADR-057, ADR-058).
    THEORY-481 and THEORY-439 move from grounds to corroborated_by:
    both were added in version 2 as evidence with the claim unchanged,
    and the body cites them as a solved case and a measured case that
    do not settle it. THEORY-169 leaves grounds: the body cites it as
    evidence against, and its citation there is the link. LIT-859
    leaves grounds, since THEORY-481 reads it. The Eq. 11 sentence now
    carries THEORY-481's correction. The claim is unchanged.
- version: 4
  date: '2026-10-29'
  note: >-
    Tenth status review (ADR-057). Restated by what each history
    carries, as CLAIM-074 now is (A44's 'contextual' and
    'adaptational' history): a per-sequence or per-task weight update
    that is discarded is part of what the context supplies.
    THEORY-169's identity of conditioning and per-sequence weight
    updates then falls inside the signal and is no longer evidence
    against. THEORY-439 leaves corroborated_by: its test-time update
    is discarded after the task, so it shows two uses of one context
    differ, not context against interpreter; the body still cites it.
    The blocker note of this date is replaced. The old title: Context
    and interpreter are separate sources of interpretive change:
    in-context conditioning changes the effective decoding context,
    adaptation changes the decoder, and improving the signal differs
    from improving the interpreter. The old defeated_if: Changes of
    interpretation produced by in-context conditioning and by
    adaptation of the interpreter are behaviourally indistinguishable:
    equally persistent, equally transferable, and predicted by the
    same model.
role: thesis
warrant: interpretive
defeated_if: >-
  What an interpreter's history has left in it can always be matched by
  context alone: for every adapted interpreter there is a fixed preamble
  that, supplied to the unadapted one, reproduces its interpretations of
  every later context, so that the carried change and the supplied one
  are one source, predicted by one model.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
works:
- what-survives-translation
corroborated_by:
- THEORY-481
summary: >-
  A43's first point about the U17 proposal, developed at A44–A45 into
  three sources of change (evidence, transient computation, parameters).
  The manuscript §5 keeps it in two sentences.
supports:
- CLAIM-074
---
<!-- inactive-ok-file: CLAIM-074 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-118: Context and interpreter are separate sources of interpretive change, told apart by what each carries and not by mechanism: what the current context supplies, whether held in activations or in weights updated on it and discarded after, is the signal; what earlier contexts have left in the interpreter and it carries into new ones is the interpreter; and improving the signal differs from improving the interpreter

## The claim

A43: the model "lets us **separate changes in communicative context from changes
in the underlying interpretive system**". A44 §4 gave two axes, context c and
interpreter parameters θ′_c = A(θ, c). A45 §7 named "**three sources of
apparent interpretive change**: changes in evidence, changes in transient
computation, and changes in the interpreter's parameters", with the interpreter
state s_t = (c_t, h_t, θ_t).

Manuscript §5: "In-context learning changes the effective decoding context
without necessarily changing model weights. Test-time training or learned
fast-state adaptation modifies the decoder itself. We thus distinguish
improving the signal from improving the interpreter."

## What it does not say

A44 §3B: "One should not identify this with literal weight updating in an
ordinary transformer", and "TTT terminology needs care". The consequence for
fidelity ([CLAIM-074](CLAIM-074.md)) is not in the manuscript.

## What the in-context-learning readings say

Read by what each change carries:

- **Per-sequence learning is the signal.** In unnormalized causal linear
  attention, conditioning on a context is one gradient step of an inner
  learner (Sun et al., [LIT-801](../literature.d/LIT-801.md); von Oswald et al., [LIT-792](../literature.d/LIT-792.md); [THEORY-169](../theory.d/THEORY-169.md)),
  and the learned state is discarded with the sequence. The identity is
  between two descriptions of what the current context supplies. Nothing
  in it is carried into the next sequence, so it does not merge context
  and interpreter.
- **Two uses of one context differ.** Akyürek et al. ([LIT-796](../literature.d/LIT-796.md),
  [THEORY-439](../theory.d/THEORY-439.md)) update the weights on the demonstrations, discard the update
  after the task, and beat conditioning alone (BIG-Bench Hard 50.5% to
  57.8%). Both are uses of the current context, so this shows that how a
  signal is used matters, not that the interpreter changed.

## An exactly solved case of the separation

Mainali and Teixeira ([LIT-859](../literature.d/LIT-859.md), read in [NOTE-658](../notes.d/NOTE-658.md)) solve the training of one
linear-attention layer on in-context regression exactly, when tasks and
inputs share an eigenbasis. Training ends at a known fixed point: a
predictor that applies a preconditioner, the inverse of the *training* input covariance (exactly so in the
long-context limit; the paper's finite-context correction holds as stated
only for isotropic inputs, [THEORY-481](../theory.d/THEORY-481.md)), to each context's own empirical
covariance (their Eq. 11). In the long-context limit each eigenmode of the training
covariance is learned on its own slow, logistic timescale.

That bears on the "against" item above. [THEORY-169](../theory.d/THEORY-169.md) makes conditioning one
gradient step of an inner learner. This case shows what builds that inner
learner: the outer weights, which change only over training, store a
preconditioner fitted to the training distribution. The context then
supplies only its own covariance and task. So even in the one class of
system where conditioning *is* a learning step, there are two separate
sources of change, on two timescales: the context, which changes the
inner learner's data, and the weights, which change what the inner learner
is. That is the claim's separation, at the level of the layer.

It does not settle the claim. The case is one linear layer, with an
assumption (weights staying in the shared eigenbasis) that is not derived,
and the paper's evidence for non-linear transformers rests on timing
coincidences ([NOTE-658](../notes.d/NOTE-658.md)). And the interpreter it shows is the one
training left, not one adapted after training and kept.

## Note of 2026-10-29: restated by what each history carries

The title told context from interpreter by mechanism, and [THEORY-169](../theory.d/THEORY-169.md) holds
that in unnormalized causal linear attention conditioning and per-sequence
weight updates "differ in what state is kept, not in kind". The claim is now
stated by what each change carries, as [CLAIM-074](CLAIM-074.md) is (A44's "contextual" and
"adaptational" history): a weight update computed from the current context
and discarded after it is part of what the context supplies. [THEORY-169](../theory.d/THEORY-169.md)'s
identity then falls inside the signal, and its own scope says the same ("Not
about persistent change"). [THEORY-439](../theory.d/THEORY-439.md) leaves corroborated_by: its test-time
update is discarded after the task, so it shows that two uses of one context
differ, not that the interpreter changed. [THEORY-481](../theory.d/THEORY-481.md) stays: the outer
weights carry a preconditioner fitted to the training distribution across
contexts, and each context supplies only its own covariance.

## Note of 2026-10-29: what holds it back

Its promotion waits on the owner's ruling that test-time training whose
update is discarded after the task is part of the signal. Manuscript §5 says
test-time training "modifies the decoder itself", and the restatement
departs from that sentence, though A44 §3B says "TTT terminology needs
care". No premise or objection is on file, and nothing in the record meets
its defeat condition.
