---
status: Active
title: 'The transports of Propositions 1–2 and of D_obs act on judgement outcomes, not texts, and for any one source–target pair a constant kernel transports any overlap-consistent target, so they constrain a translation only once one kernel family is fixed across many utterances and derived from the text channel'
version: 1
role: granted
tags:
- mathematics
- probabilistic-modeling
- contextuality
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-121
- CLAIM-070
- CLAIM-077
objects_to:
- CLAIM-125
- CLAIM-005
uses:
- TERM-008
- TERM-021
summary: >-
  Found in the record's audit of the line on 2026-10-10 (formal lens); no
  turn of the exchange raises it. The manuscript's kernels K_C map
  readers' judgements to readers' judgements, while a translation is a
  channel on texts, T(v | u), and [TERM-008](../terms.d/TERM-008.md) records that the two levels
  are never formally related. For one source and any overlap-consistent
  target, the constant kernel makes D_obs zero and satisfies naturality.
  Granted, because it is elementary. It does not say [CLAIM-121](CLAIM-121.md) or
  [CLAIM-070](CLAIM-070.md) is false; it bears on what they are used to support.
---
<!-- inactive-ok-file: CLAIM-125 CLAIM-005 — Proposed; open, and cited as the claims this objection is to -->
<!-- inactive-ok-file: CLAIM-077 — Proposed; cited as the admissibility condition that would exclude the constant kernel, which the manuscript lacks -->
<!-- inactive-ok-file: THEORY-156 — Proposed; cited for the Blackwell condition the uniform reading becomes, not as settled -->
<!-- inactive-ok-file: CLAIM-117 — Proposed; cited only for the parallel with CLAIM-011 -->
<!-- inactive-ok-file: CLAIM-tmpyeik3 CLAIM-tmpflbi3 — Proposed; companion objections from the same audit, cited for their neighbouring points -->

# CLAIM-tmp6xxbf: The transports of Propositions 1–2 and of D_obs act on judgement outcomes, not texts, and for any one source–target pair a constant kernel transports any overlap-consistent target, so they constrain a translation only once one kernel family is fixed across many utterances and derived from the text channel

## The objection

The manuscript's transport is a context map τ with local kernels on
outcomes. [TERM-008](../terms.d/TERM-008.md) gives it from A81 §5.2: "K_C : E_o(C) ⇝ E_t(τ(C))". Its
naturality law, from C6 Appendix B, is "restrict_tau(D) K_C = K_D
restrict_D, interpreted as equality of kernels". E_o(C) and E_t(τ(C)) are
the outcomes of the judgements elicited in a context. So each K_C maps a
source reader's judgement to a target reader's judgement.

A translation does something else. It maps a text to a text, T(v | u).
[TERM-008](../terms.d/TERM-008.md) says of the two: "the two levels are never formally related, and
the manuscript uses both." No translator, generator or captioner takes
readers' judgements as input. The source and target empirical models are
two families of responses, to two texts.

**For one pair, the kernels are unconstrained.** Take an overlap-consistent
source model e, and any overlap-consistent target model e′ on the target
cover. Let every kernel ignore its input: K_C(· | s) = e′_τ(C) for every
source outcome s. Then:

- K_C# e_C = e′_τ(C). So every term of
  L_obs(T) = Σ_C w_C d_C[(K_C)#e_C^o, e_τ(C)^t] ([CLAIM-005](CLAIM-005.md)) is
  d_C(e′_τ(C), e′_τ(C)) = 0, and D_obs = 0.
- Naturality asks that restricting after K_C equal K_D after restricting.
  The left side is the constant kernel with value e′_τ(C) restricted to
  τ(D). The right side is the constant kernel with value e′_τ(D). So
  naturality holds exactly when the restriction of e′_τ(C) to τ(D) is
  e′_τ(D). That is target overlap consistency, which was assumed.

So Proposition 1's hypotheses hold ([CLAIM-121](CLAIM-121.md)), and its conclusion returns
the target consistency that was put in. Proposition 2 is the same
([CLAIM-070](CLAIM-070.md)). If e′ is noncontextual with global law p′, the constant global
kernel K_X ≡ p′ restricts to the constant kernels above, and K_X#p = p′ is
a global extension of the target. Every overlap-consistent target is
naturally transported from every source at zero observational distortion,
whatever the translation did.

If K_C is fitted to make L_obs small, the fit can reach this kernel. That is
the case [CLAIM-011](CLAIM-011.md)'s remedy is for: "Require state correspondences to be
estimated on one collection of tasks and evaluated on another".

**Separation narrows the freedom and does not remove it.** An anchoring
condition would exclude the constant kernel. [CLAIM-077](CLAIM-077.md) quotes C1 Appendix
A's anchor constraint, which "rules out constant transports when the
anchors distinguish multiple source states". It also records that "Neither
the anchor nor the separation condition is in the manuscript", whose "§6
naturality condition constrains the kernels but not their separation".

Even with separation, a kernel that separates the source outcomes can often
still push e_C onto a given target. Take two source outcomes a and b with
e_C = (1/2, 1/2), and let e′_τ(C) be uniform on three target outcomes. The
rows

- K(· | a) = (2/3, 1/3, 0),
- K(· | b) = (0, 1/3, 2/3)

average to (1/3, 1/3, 1/3). So K# e_C = e′_τ(C), and the D_obs term is zero.
The two rows are at total-variation distance 2/3.

No pair of rows does better here, and none is at distance 1. The rows must
average to 1/3 in each coordinate, so no row exceeds 2/3 anywhere. Their
distance is the sum, over the coordinates where K(· | a) exceeds 1/3, of
2K(i | a) − 2/3. With one such coordinate it is at most 4/3 − 2/3 = 2/3.
With two it is at most 2 − 4/3 = 2/3, because their entries sum to at most
1. With three it is 0. The separation available is bounded by e′, but it
is not zero. Whether separating families like this one also satisfy
naturality across a whole cover was not checked.

**The constraint appears only across utterances.** Suppose one kernel
family must serve every source utterance u in a class:
e^(t,u) = K# e^(o,u) for every u. Then for each context, the target's
judgement distributions, read as an experiment about u, are a garbling of
the source's ([THEORY-156](../theory.d/THEORY-156.md)). That is a real condition, and it is a Blackwell
condition (on where Blackwell's order reaches, see [CLAIM-tmpyeik3](CLAIM-tmpyeik3.md)). It
makes the transport a property of a translation procedure, not of one
rendering, which is also [CLAIM-tmpflbi3](CLAIM-tmpflbi3.md)'s point.

It is still a condition on the outcome-level kernels. Nothing in the record
derives those kernels from T(v | u), the channel a translator actually
applies, uniformly in u. Until that is done, Propositions 1 and 2 are
theorems about a map that translation is never shown to induce.

That bears on two claims. [CLAIM-125](CLAIM-125.md) says of its bridge question, "Half of
that question is answered", by the simulations of which Propositions 1 and
2 are special cases. The answer is about kernels between empirical models.
It reaches translation only once the kernels are derived from the text
channel. [CLAIM-005](CLAIM-005.md)'s L_obs, and [TERM-021](../terms.d/TERM-021.md)'s D(τ) before it, score one
rendering against its source. For one pair it can be made zero by the
choice of kernel.

## What it does not say

- It does not say [CLAIM-121](CLAIM-121.md) or [CLAIM-070](CLAIM-070.md) is false. Both were checked and are
  Active, and the constant kernel meets their hypotheses honestly. It bears
  on their use in support, as [CLAIM-011](CLAIM-011.md) bears on [CLAIM-117](CLAIM-117.md).
- It does not say that every separating kernel can push e_C onto any
  target. The three-point example shows the separation is bounded by the
  target. The main point rests on the constant kernel and on the missing
  derivation from T(v | u).
- It does not say anyone proposes the constant kernel. It says nothing in
  the propositions, or in D_obs as the manuscript states it, excludes it.
