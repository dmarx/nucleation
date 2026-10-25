---
number: 336
status: Proposed
formerly:
- CLAIM-tmp84z6h
title: 'The pragmatic-transport and will-organization lines describe one model, an organization of operators that act on a shared interpretive state under a context while allocating one another''s influence: a frame is the context under which operators act, a judgement is the response they yield, an action-generating regime is an operator or coalition, and a will-organization is the dynamics that allocates influence among them'
version: 4
history:
- version: 2
  date: '2026-10-21'
  note: >-
    Note of 2026-10-21 added, from the exchange of 2026-10-20 on effective
    description, agency and legibility: A15 proposed this claim's joint test
    as the next substantive one; A16's construction has no meaning state,
    and A17 dropped the comparison, so the claim stays untested. The claim
    is unchanged.
- version: 3
  date: '2026-10-25'
  note: >-
    A dated note added: the exchange's running population model and typed
    workspace read against the claim. The claim is unchanged.
- version: 4
  date: '2026-10-25'
  note: >-
    The note of 2026-10-25 extended after the readings of MultiDiffusion
    and Multi-LoRA composition: A45's distinction maps onto the two papers,
    with a caution that prompt-as-frame and LoRA-as-operator do not separate
    cleanly. The claim is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A phenomenon central to one line that the model cannot express without a
  component the other line lacks and the operator model does not have:
  for example, a fidelity result that needs the interpreter's state to be
  fixed while it judges, or a will-organization result that needs
  regimes to act without passing through any shared state. Or the mapping
  shown to be relabelling only: the two lines, so mapped, make no joint
  prediction that either makes alone (QUESTION-088's test of compression).
tags:
- agency
- pragmatics
- cognition
date: '2026-10-16'
line:
- distributed-agency
- pragmatic-transport
- will-organization
rests_on:
- CLAIM-297
- CLAIM-286
- CLAIM-279
uses:
- TERM-019
- TERM-023
- TERM-031
- TERM-039
- TERM-053
summary: >-
  The owner's, U2 of the exchange of 2026-10-16: the pragmatic-transport
  model and the will-organization model are "both manifestations of the
  same underlying model". The mapping is the assistant's, A6, filed at the
  owner's request ("address the still open stuff"). At U8 the owner
  endorsed it as filed ("Yes, as filed"). It reads both lines into [CLAIM-297](CLAIM-297.md)'s operator model. The
  sharp edge: it says the lines share one model, not that either line's
  results transfer to the other unchanged. Each mapping is a hypothesis
  until a result on one line is shown to hold, through it, on the other.
complements:
- CLAIM-341
- CLAIM-450
supports:
- CLAIM-338
---
<!-- inactive-ok-file: CLAIM-297 — Proposed; cited in the note of 2026-10-21, nothing here rests on it -->

# CLAIM-336: The pragmatic-transport and will-organization lines describe one model, an organization of operators that act on a shared interpretive state under a context while allocating one another's influence: a frame is the context under which operators act, a judgement is the response they yield, an action-generating regime is an operator or coalition, and a will-organization is the dynamics that allocates influence among them

## The claim

The owner, at U2, asked whether "our model" meant the pragmatic-transport
model (judgements as responses in measurement contexts) or the
will-organization model (regimes and how influence is allocated among
them): "those are both manifestations of the same underlying model."

The record's nearest statement of a model common to both is the operator
model of the distributed-agency line. [CLAIM-297](CLAIM-297.md) writes it as meaning,
influence and query processes:

- meaning: x_{t+1} = Σᵢ w_{i,t} P_i(q_t)ᵀ x_t;
- influence: w_{t+1} = G(w_t, x_t, o_t, E_t);
- queries: q_{t+1} = Q(x_{t+1}, w_{t+1}, g).

The owner has already said that what the operators do are "just different
regimes in the dynamics of our general process" ([CLAIM-279](CLAIM-279.md)). [CLAIM-286](CLAIM-286.md)
holds that habit, akrasia, rumination, rigidity and insight are regimes of
one such organization.

The mapping, A6's:

| pragmatic transport | operator model | will-organization |
|---|---|---|
| measurement context, frame ([TERM-031](../terms.d/TERM-031.md), [TERM-039](../terms.d/TERM-039.md)) | query q under which operators act | the situation a regime is cued by |
| interpretive state ([TERM-026](../terms.d/TERM-026.md)) | meaning state x | — |
| judgement, response J | the state P(q)ᵀx the operators yield, read out | — |
| — | operator, or coalition of operators | action-generating regime ([TERM-019](../terms.d/TERM-019.md)) |
| — | influence w, and its update G with endorsement E ([TERM-053](../terms.d/TERM-053.md)) | practical efficacy, and the will-organization that governs it ([TERM-023](../terms.d/TERM-023.md)) |
| transport between two interpreters | a map between two such organizations | — |

Read this way, the pragmatic-transport line studies the model from the
outside, one interpreter at a time. It asks which responses an
organization yields under which contexts, and what a translation must
keep. The will-organization line studies it from the inside. It asks which
operators get to act, and what keeps that allocation the agent's own. The
loop [CLAIM-341](CLAIM-341.md) puts at the centre, judgement reshaping the observer,
is where the two meet. A judgement under a context changes x, and through
endorsement changes w and so which operators act under the next context.

## What it does not say

- It does not transfer results. Contextuality results on judgements and
  efficacy results on regimes stay on their lines until a result is shown
  to hold through the mapping.
- The blank cells are the gaps. Pragmatic transport has no counterpart of
  influence allocation. Will-organization has no counterpart of a
  measurement context or a read-out response. The claim says both are
  partial views of one model, not that either is complete.
- It does not decide [QUESTION-056](../questions.d/QUESTION-056.md), whether a mechanism-level description
  implements the will-organization account or replaces it. The operator
  model is one such description.
- The mapping was proposed by the assistant and endorsed by the owner at
  U8. The endorsement is of the mapping, not of any transfer of results.

## Note of 2026-10-21: proposed as a test, then dropped

A15 of the exchange of 2026-10-20 proposed as "our next substantive test"
a system "in which a coarse description perfectly predicts ordinary
behavior but loses a governance response to an intervention", and then
compare descriptions that keep meaning, authority, or both. The
construction A16 gave ([CASE-125](../cases.d/CASE-125.md)) has no meaning state, so it cannot
show the joint prediction this claim's `defeated_if` asks for. A16 §13
proposed the comparison as a simulation; A17 dropped it: "the paper's
principal argument does not depend on proving it." The claim stays
untested. A15's equations are [CLAIM-297](CLAIM-297.md)'s, quoted here.

## Note of 2026-10-24: information geometry and singular learning

The owner: "let's connect back to the communicative act stuff and
amari/watanabe theory" (workbench entry of 2026-10-24, U27). The
connection is filed as [CLAIM-450](CLAIM-450.md): Amari's Fisher metric measures which
changes of an interpreter's organization the probes detect; Watanabe's
theory says what follows when different organizations give the same
responses ([CASE-152](../cases.d/CASE-152.md)). Belief, wanting, liking and feeling as the
exchange characterized them are states of organized interpreters, not
speech acts: assertion, request, praise and disclosure can each come apart
from the state they seem to express, and saying "I am afraid" can report,
warn or appeal. What links them is that communicating about such a state
can change the audience's interpretation, the speaker's standing, and the
authority of later contributions, so the meaning–authority–legibility
feedback can run between participants as well as within one. The bearing
on [QUESTION-031](../questions.d/QUESTION-031.md) is when observable responses suffice to separate the
organizations relevant to a task.

## Note of 2026-10-25: a running instance, and a typed workspace

The exchange of 2026-10-24, continued, built a running instance of this
claim's model, the "Perspective Population Lab" from v0.2 to v1.0, none of
it held. A42 cited this claim for its proposal of a typed workspace.

- A43's workspace (evidence, interpretations, policies, artifact,
  governance, commitments and an event log) refines the two dual canvases
  ([TERM-053](../terms.d/TERM-053.md)): interpretations and artifact on the meaning side, governance
  on the influence side. The commitments domain is reserved for the
  communicative-act line.
- In A45–A47's diffusion version, a perspective's conditioning prompt plays
  the frame, its low-rank adapter the operator, its mask and weight its
  allocated influence, and the single scheduler step the update of the
  shared state.
- A45: distinguish "a population with multiple genuinely specialized
  operators from a population with different interpretations of one shared
  operator". The two published works read on 2026-10-25 are its two
  sides. MultiDiffusion (LIT-tmp03agp, NOTE-tmpa8ixz) is different
  interpretations of one shared operator: one network, many frames or
  prompts, masks as influence. Multi-LoRA composition (LIT-tmpxsvgv,
  NOTE-tmphq8v2) is several specialized operators under one shared frame,
  with uniform influence (Composite) or influence sliced in time (Switch).
  A caution for the typed-workspace mapping above: in Multi-LoRA the
  shared prompt carries each LoRA's trigger words, so an operator acts
  partly through the frame, and prompt-as-frame and LoRA-as-operator do
  not separate cleanly.

No joint prediction of the two lines was derived, so the claim stays
untested. The claim is unchanged.
