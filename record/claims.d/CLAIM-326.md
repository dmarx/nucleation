---
number: 326
status: Proposed
formerly:
- CLAIM-tmpz6mng
title: 'With losses in [0, 1] and a stated prior, the positive part of the Bayes-risk increase on the same decision problem, D⁺_Q(U → V; π), is directed, is zero from a garbling back to its source, vanishes for every finite problem and prior exactly when the rendering is at least as informative as the source in Blackwell''s order over finitely many states, and has A86''s D_Q, with the identity on tasks, as its symmetrization'
version: 4
history:
- version: 2
  date: '2026-10-19'
  note: >-
    A ground added at the owner's direction, as the follow-up to the
    owner's promotion audit of 2026-10-19. Step (b) uses the converse with
    Z finite. When U and V also take finitely many values, as with coded
    renderings, THEORY-717 (Active) covers it. For renderings with
    unbounded outcome spaces, the ground is still THEORY-156. The claim is
    unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Split at the owner's direction, carrying out the promotion audit's
    decision (record/promotion-audit/decisions/CLAIM-326.yaml, batch 014,
    ADR-047). Steps (a) to (d) for finitely many outcomes are now
    CLAIM-380, demonstrated and Active, on THEORY-717. This claim
    rests on it and keeps the unrestricted statement, whose step (b)
    needs the general converse (THEORY-156, Proposed). The claim is
    unchanged, and the status stays Proposed.
- version: 4
  date: '2026-10-29'
  note: >-
    Step (b) says the scope of the theorem it applies. The twelfth status
    review (ADR-057) narrowed THEORY-156 to standard Borel outcome spaces
    and promoted it; every rendering a design produces lies in such a
    space, so the step is unchanged. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in steps (a) to (d): a finite problem with losses in [0, 1] and a
  prior under which a garbling has lower Bayes risk than its source; two
  experiments on finitely many states with D⁺(U → V; π) = 0 for every such
  problem and prior where V is not at least as informative as U; or a pair
  for which D_Q, with the identity on tasks and the same prior, differs from
  max(D⁺(U → V), D⁺(V → U)).
tags:
- mathematical-statistics
- information-theory
date: '2026-10-15'
line: pragmatic-transport
rests_on:
- CLAIM-380
grounds:
- THEORY-156
- THEORY-717
summary: >-
  Split from [CLAIM-259](CLAIM-259.md) under [ADR-043](../decisions.d/ADR-043.md): the properties of the restated decision
  term, which [CLAIM-259](CLAIM-259.md) called "elementary and checkable", stated on their own
  so that their warrant can be. Define D⁺_Q(U → V; π) = sup over q in Q of
  [r_q,π(V) − r_q,π(U)]⁺. A garbling never gains; with Q all finite problems
  and π all priors, the term vanishes exactly when V is at least as
  informative as U, by the Bayes form of Blackwell's theorem for finitely
  many states ([THEORY-156](../theory.d/THEORY-156.md)); it is directed; and A86's D_Q is its
  symmetrization. It does not say this is the right decision term, which is
  [CLAIM-259](CLAIM-259.md)'s proposal, and it does not state the prior-free relation to Le
  Cam's deficiency.
supports:
- CLAIM-259
---
<!-- inactive-ok-file: CLAIM-259 CLAIM-258 — Proposed; the proposal this was split from, the objection whose worked case it measures, and the directed-fidelity thesis, cited as open -->
<!-- inactive-ok-file: LIT-778 — Unavailable; Torgersen, unread here, named for the constants and not leaned on -->

# CLAIM-326: With losses in [0, 1] and a stated prior, the positive part of the Bayes-risk increase on the same decision problem, D⁺_Q(U → V; π), is directed, is zero from a garbling back to its source, vanishes for every finite problem and prior exactly when the rendering is at least as informative as the source in Blackwell's order over finitely many states, and has A86's D_Q, with the identity on tasks, as its symmetrization

## The claim

These are steps (a) to (d) of [CLAIM-259](CLAIM-259.md), stated on their own. [CLAIM-259](CLAIM-259.md):
"Steps (a) to (d) below are elementary and checkable. That receivers'
judged fidelity behaves like this term is a proposal". This claim is the
first sentence; [CLAIM-259](CLAIM-259.md) keeps the second.

**Definition.** Let U be the source and V the rendering, both experiments
about one situation Z, which is finite in any design. A decision problem q
has a finite set of actions and a loss L_q(z, a) in [0, 1]. Let π be a
stated prior on Z. The Bayes risk r_q,π(U) is the least expected loss,
under π, over decision rules that read U. Then

D⁺_Q(U → V; π) = sup over q ∈ Q of [r_q,π(V) − r_q,π(U)]⁺,

where [x]⁺ = max(x, 0). The same problem is used on both sides, so no scale
between tasks is needed.

**(a) A garbling never gains.** If there is a Markov kernel G with
P(V | Z) = G P(U | Z), any rule δ that reads V gives a rule on U, namely
apply G to U and then δ, with the same distribution of actions under each z
and so the same risk. So r_q,π(U) ≤ r_q,π(V) for every q and π, and
D⁺_Q(V → U; π) = 0 always.

**(b) The converse.** If D⁺(U → V; π) = 0 for every finite problem with
losses in [0, 1] and every prior π, then r_q,π(V) ≤ r_q,π(U) for all of
them. Rescaling a bounded loss to [0, 1], by L ↦ (L − m)/(M − m), rescales
every Bayes risk by the same increasing affine map, so the inequality holds
for every bounded loss. By the Bayes form of Blackwell's theorem for
finitely many states ([THEORY-156](../theory.d/THEORY-156.md)), V is then at least as informative as U. The
form the record holds is for standard Borel outcome spaces, which every
rendering a design produces lies in.

**(c) It is directed.** With Z uniform on {0, 1}, U = Z, V a constant and
q = "guess Z" with 0–1 loss, r(U) = 0 and r(V) = 1/2, so D⁺(U → V) = 1/2
and D⁺(V → U) = 0.

**(d) A86's D_Q is its symmetrization.** With τ the identity on tasks and
the same prior, D_Q(U, V) = sup_q |r_q(U) − r_q(V)|. Since
|x| = max([x]⁺, [−x]⁺), and a supremum of a maximum is the maximum of the
suprema, D_Q(U, V) = max(D⁺(U → V), D⁺(V → U)). In [CLAIM-258](CLAIM-258.md)'s worked case
the directed pair is (1/3, 1/3), while a rendering that told its reader
nothing would have (1/3, 0) on the same two problems; D_Q is 1/3 for both.

Step (b) applies a theorem the record holds through [THEORY-156](../theory.d/THEORY-156.md); the rest
follows from the definitions.

## What it does not say

- It does not say this is the decision term fidelity should use, or that
  receivers' judged fidelity behaves like it. That is [CLAIM-259](CLAIM-259.md)'s proposal,
  with its own defeat condition, and it is interpretive.
- It does not say Q is fixed. D⁺ is relative to the problems named.
- It does not state the prior-free form or its exact relation to Le Cam's
  deficiency. Those constants are in Torgersen ([LIT-778](../literature.d/LIT-778.md)), which the record
  has not read.
- It does not supply a correspondence of tasks for re-performance fidelity.
  It assumes one situation and the identity on tasks.

## Note of 2026-10-19: when step (b) rests on an Active ground

Step (b) applies the converse of Blackwell's theorem with Z finite. If U and
V also take finitely many values, as they do once renderings are coded into
a finite set of categories, then that converse is Theorem 6 of Blackwell
(1953), held in [THEORY-717](../theory.d/THEORY-717.md), which is Active. If the outcome spaces are
unrestricted, as for raw texts, step (b) still rests on [THEORY-156](../theory.d/THEORY-156.md), which is
Proposed for that case. The claim states no restriction on the outcome
spaces, so it keeps both grounds.

## Note of 2026-10-19: the finite case, split off

The finite-outcome case of steps (a) to (d), with the worked case checked,
is now [CLAIM-380](CLAIM-380.md), Active. What keeps this claim Proposed is only
step (b) for outcome spaces that are not finite.
