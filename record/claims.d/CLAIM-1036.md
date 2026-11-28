---
number: 1036
status: Proposed
formerly:
- CLAIM-tmp6ppvo
title: 'Self-changing values fix no scalar optimum'
statement: >-
  When what a learner learns changes what it values, the valuations of the
  selves its policies would produce fix no scalar optimum: judged by the
  self each policy produces, the ranking changes under rescalings that leave
  every self's preferences as they were, and the policies their produced
  selves would choose again can be two or none; any rule that picks one
  optimum privileges one self, and the rule that privileges the present
  self, though it gives an optimum, counts nothing that only a later
  valuation would see
version: 2
history:
- version: 2
  date: '2026-11-26'
  note: >-
    Dated note from the exchange "Alignment consequences brainstorm"
    (ChatGPT, 2026-11-26), A21: the construction described correctly and
    applied to the development of values; Paul and Callard registered. No
    change of status or statement.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the constructions; or a rule fixed by the produced selves'
  valuations alone, unchanged when any self's utility is rescaled and when
  policies and selves are relabelled together, that picks exactly one best
  policy in the two-self or the three-self construction; or a showing that
  the present self's valuation can count a benefit its utility gives no
  weight to. An argument that some declared evaluator is the right one does
  not defeat it.
tags:
- learning-theory
- epistemology
- self-governance
date: '2026-11-23'
line:
- learned-structure
- realizability
complements:
- CLAIM-754
uses:
- TERM-092
bears_on:
- QUESTION-495
- QUESTION-364
summary: >-
  Filed by the lead run of 2026-11-23, on the reading of the lead in which
  what is learned changes what the learner values, or what it can value.
  [CLAIM-1197](CLAIM-1197.md)'s second condition, one valuation for every policy
  compared, then fails, and the three ways of putting it back each cost
  something: the present self's valuation gives an optimum but excludes
  the benefits [QUESTION-495](../questions.d/QUESTION-495.md) asks about, which cannot be specified in
  advance; each produced self's valuation counts them but ranks nothing
  until a comparison between selves is declared; and asking which policies
  their own produced selves endorse is free of scale but can return two
  policies or none. Two small symmetric constructions show it. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-1197 ARG-227 — new; filed by the lead run of 2026-11-23 -->

# CLAIM-1036: Self-changing values fix no scalar optimum

## The claim

Each learning policy π produces a learner s(π) whose valuation is
u_{s(π)}, and the learner as it now is, s₀, has u₀. Learning that changes
only beliefs, capacities or the tasks met leaves one valuation in place,
and [CLAIM-1197](CLAIM-1197.md)'s conditions can hold. Learning that changes the
valuation does not: there are now as many candidate valuations as selves,
and "the" value of a policy needs an evaluator. There are three natural
ones.

1. **Ex ante**: value every policy by u₀. Condition 2 holds, and an
   optimum exists. But a benefit that only the produced self's valuation
   sees counts for nothing, whatever its size; and an outcome the present
   self cannot formulate, past its inquiry frontier ([TERM-092](../terms.d/TERM-092.md)), has no u₀
   value at all, so any extension of u₀ to it is a further choice that u₀
   does not make.
2. **Ex post**: value π by u_{s(π)}(π). This counts what each produced
   self sees. But each u_s is fixed by that self's preferences only up to
   a positive affine rescaling (up to any increasing map, if it is only
   ordinal), and the ex post comparison of π with π′ compares numbers on
   two different selves' scales.
3. **Self-ratification**: admit π when its produced self ranks it at least
   as high as every alternative. This uses each self's preferences only,
   so it is free of scale.

## The constructions

`scratch/studies/lead-011/` checks both.

**Two selves.** Policy A learns L and produces s_L; policy B does not and
leaves s₀. u₀(A) = 0, u₀(B) = 1; u_L(A) = 1, u_L(B) = 0. Ex post,
V(A) = 1 = V(B). Multiply u_L by 2, which changes none of s_L's
preferences, and A ranks first; multiply it by ½ and B does. Both A and B
are self-ratifying. Ex ante, B is optimal, and stays optimal whatever
value u_L puts on A.

**Three selves.** Policies A, B, C produce a, b, c. Self a prefers B,
b prefers C, c prefers A, each with utility 1 for its favourite and 0
otherwise. Every policy is regretted by the self it produces, so none is
self-ratifying.

## Why no rule fixed by the valuations alone picks one optimum

Exchanging A with B and s₀ with s_L maps the two-self construction onto
itself: u₀(A) = 0 becomes u_L(B) = 0, u₀(B) = 1 becomes u_L(A) = 1, and
A ↦ s_L becomes B ↦ s₀. Rotating A → B → C with a → b → c maps the
three-self construction onto itself. A rule that uses only the selves'
valuations, and so treats relabelled policies and selves alike, must give
A and B the same verdict in the first and A, B and C the same verdict in
the second. It picks both or neither, all or none. To pick one, a rule
must break the symmetry, and the only asymmetry is which self is present.
So a unique optimum comes from privileging a self, which is the ex ante
rule, or from a declared valuation over pairs of a self and an outcome
that fixes the selves' scales against each other, which no self supplies.

## So

Where what is learned changes what is valued, the conditions for a scalar
optimum hold only by declaring an evaluator, and the choice is a dilemma.
The evaluator that gives an optimum without further declaration, the
present self, excludes by construction the benefits that [QUESTION-495](../questions.d/QUESTION-495.md)
asks about. The evaluators that count them give no optimum until a
comparison between selves is declared.

## What it does not say

- That no evaluator is defensible, or that the present self's is wrong.
  Choosing one is a commitment, and here it is the owner's.
- That every change of valuation produces these failures. When the
  produced selves happen to agree on the best policy, every rule above
  picks it.
- Anything about persons. The selves are the learner at different points
  of different policies; whether a change of valuation keeps the same agent
  is [QUESTION-364](../questions.d/QUESTION-364.md)'s subject, and the constructions do not depend on it.
- The economics of changing tastes and the philosophy of transformative
  choice discuss the same structure; neither is read on the record, and
  the claim rests on neither.

[ARG-227](../arguments.d/ARG-227.md) carries the inference from these constructions to the claim
that one valuation cannot be dropped from [CLAIM-1197](CLAIM-1197.md)'s conditions.

## Note of 2026-11-26: the exchange "Alignment consequences brainstorm" (ChatGPT, U12–A21)

<!-- inactive-ok-file: LIT-3304 LIT-3287 LIT-3279 CLAIM-1423 CLAIM-1356 CLAIM-1350 — Deferred or Proposed; registered and filed from the exchange of 2026-11-26 -->

On the owner's U12 ("double click on Emergence of new purposes and values"), A21 §1 opened with this claim as "a surprisingly strong result already in the record". Its description is accurate: the two-self construction ("Suppose the present self prefers B, whereas the self produced by A prefers A"), the three evaluators, and "The claim demonstrates the latter two problems through small constructions. It remains Proposed in the record, and its no-optimum conclusion is conditional on the absence of an additional cross-self evaluative standard."

What the exchange adds is an application, a parallel and two works:

- **Application.** A21 states the claim's dilemma for a learner whose values are meant to develop: "evaluating that development solely by its original values risks making genuine evaluative development invisible. But evaluating it solely by the values it develops risks allowing any self-endorsing transformation to justify itself." [CLAIM-1423](CLAIM-1423.md) (A's) says what kind of change of valuation is at issue, a new evaluative distinction and not a reweighting, and [CLAIM-1356](CLAIM-1356.md) (A's) carries the dilemma to the governance of possibility.
- **The literature this claim says is not read.** "What it does not say" notes that "the philosophy of transformative choice" is not read on the record. A21 §2 names it: Paul's Transformative Experience ([LIT-3304](../literature.d/LIT-3304.md)), "exceptionally close to CLAIM-1036", and Callard's Aspiration ([LIT-3287](../literature.d/LIT-3287.md)), on proleptic reasons; also Dewey's ends-in-view ([LIT-3279](../literature.d/LIT-3279.md)). All three are registered, Deferred, unread. Until read they bear on the claim only as named parallels; the claim rests on none.
- **Generation.** The outcome "past its inquiry frontier" that has no u₀ value is the case [CLAIM-1350](CLAIM-1350.md) (A's) calls an unconstituted purpose.

No change of status or statement.
