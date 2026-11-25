---
number: 419
status: Proposed
formerly:
- CASE-tmptzhse
title: 'Smart touch-scroll interface'
statement: >-
  A smart touch-scroll interface as a testbed for First Contact's
  co-adaptation: the owner's proposal that a scroll interface learn the
  user's expected gain, momentum and braking from how they scroll, without
  knowing what they are looking for, under the owner's constraint that
  inference latency not add to perceptual latency; with A's designs, a fast
  deterministic scrolling loop beside a slow learning loop, one adaptive
  parameter first, and a staged comparison of correction statistics against
  the mutual-information score
version: 1
standing: stipulated
kind: proposed-study
tags:
- information-theory
- control-theory
- learning-theory
- embodied-cognition
date: '2026-11-22'
line:
- will-organization
- distributed-agency
draws_on:
- THEORY-2147
illustrates:
- CLAIM-788
- CLAIM-535
bears_on:
- QUESTION-504
summary: >-
  The owner's, U2 and U3 of the exchange "Explain First Contact RL"
  (ChatGPT, 2026-11-22): "consider a 'smart touch scroll' interface that
  could leverage this phenomenon", and "brainstorm how we could minimally
  implement this. my concern is inference latency relative to perceptual
  latency." The designs below are A's (A4, A5, A8 of that exchange): the
  wording of those is A's (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner's call. The case is filed as a proposed study,
  not a question, because the owner put forward a design to be tried and a
  constraint on it, and the record's questions about First Contact are
  already held ([QUESTION-504](../questions.d/QUESTION-504.md), [QUESTION-404](../questions.d/QUESTION-404.md)).
---
<!-- inactive-ok-file: CLAIM-788 CLAIM-787 CLAIM-1191 — Proposed or Open; the First Contact entries and rate claims this case uses -->

# CASE-419: Smart touch-scroll interface

## The case

**The owner's proposal** (U2). First Contact ([LIT-2956](../literature.d/LIT-2956.md); [NOTE-2236](../notes.d/NOTE-2236.md)) fits an
interface by the mutual information between a user's command and the state
change it induces, with no knowledge of the user's task, while the user
adapts too. A touch-scroll interface is a natural place to use that:
scrolling is a continuous loop of intention, gesture and visual result, and
the interface could learn how far the user expects content to move for a
finger movement, how much momentum after release, and how hard to brake,
without knowing what the user is reading or looking for.

**The owner's constraint** (U3). Inference latency must not add to
perceptual latency. A 120 Hz display allows about 8.3 ms per frame and a
60 Hz one about 16.7 ms (A5), and those are whole frame budgets, not
allowances for inference.

**A's design** (A5, A8), in four parts.

1. **Two loops on two timescales.** A fast loop applies the current
   scrolling physics every frame, deterministically, with no model call on
   the input or rendering path. A slow loop, between gestures and off the
   UI thread, observes what the user did and adjusts the parameters.
   Parameters are snapshotted at release and never change during a fling,
   since physics that change mid-motion feel like lag even when every frame
   is on time. On A's design targets (not measurements), the mapping and
   physics take under 0.1 ms; logging, parameter updates and any MI
   estimation run outside the frame-critical path. The learning can then
   take hundreds of milliseconds or seconds without perceptual lag: A's
   "decouple *response latency* from *adaptation latency*".
2. **One adaptive parameter first.** Leave direct finger tracking 1:1 and
   adapt only post-release friction, v(t) = v₀e^(−λt), within about ±15 %
   of the default, by small, bounded, infrequent updates. Signals: release
   velocity and coast distance; whether the next gesture reverses; how soon
   it comes; how far the correction travels. A quick reversal suggests
   overshoot (more friction), repeated same-direction flicks undertravel
   (less). A reversal is weak evidence, since rereading looks the same.
3. **A staged comparison** (A5). (i) Passive observation under default
   physics: do reversals, pauses and repeated gestures predict
   independently measured difficulty? (ii) One-parameter adaptation from
   correction statistics. (iii) Optimization of an estimate of First
   Contact's score over gesture windows. A's sharpest question: "does
   optimizing correction frequency actually produce the same friction
   setting as optimizing mutual information?" A divergence would say what
   the score measures in a continuous motor-control interface.
4. **Separating the two adapters** (A8). Users improve with any interface;
   to tell interface improvement from user accommodation, cross user
   experience (untrained, increasing) with mapping (standard, fixed,
   updated), freeze the learned mapping periodically, counterbalance
   exposure, and test transfer: a mapping learned on one document should
   help on unfamiliar documents. A further arm restores standard scrolling
   for a while, to see whether the user's unassisted control has changed.
   Measure at three horizons: within a gesture (tracking delay, response
   consistency), across gestures (corrections, target acquisition,
   sustained positioning), across sessions (transfer, retention, removal of
   the adaptation).

**A's further options**, not part of the first study: a hybrid objective,
Î(X_t; (S_t, S_{t+1})) − λ E[C_t] − β D(θ, θ₀), with a correction cost C
(reversals, repositioning, extra swipes) and a penalty D on drift from
familiar physics (A4, A's own extension, not the paper's); a latent mode
z ∈ {browse, target, read} inferred from recent gestures and changed
gradually (A4); a fixed hand-designed state machine during scrolling
(finger down 1:1, release with learned momentum, touch during momentum
brakes, reversal cancels momentum) whose thresholds could later be learned
(A5).

## What it can show

It is stipulated: nothing here has been run. Its standing is that of a
design that would test several held entries in a cheap, repeatable setting.

- **[CLAIM-788](../claims.d/CLAIM-788.md)**'s channel reading and its defeater (a), transfer: part 4's
  unfamiliar-document test is the test First Contact does not run
  ([NOTE-2236](../notes.d/NOTE-2236.md)).
- **[CLAIM-787](../claims.d/CLAIM-787.md)**'s horizon: A8 distinguishes the computational latency of
  evaluating a policy from the evaluative horizon at which one can tell
  whether a command helped; the first is part 1's, the second is First
  Contact's Δ, and they need not coincide. Strong inertial braking can
  shorten a flick and still make positioning easier, the scroll analogue
  of the lander inversion ("less immediate movement ⇏ less effective
  control"), though too much braking frustrates.
- **[CLAIM-535](../claims.d/CLAIM-535.md)**: a quick reverse swipe can mean overshoot, rereading or
  searching back, circumstances the controller cannot tell apart from the
  gesture and that call for different adjustments; A8 concludes the
  interface should stay task-agnostic and learn from patterns over many
  gestures rather than decode intent per gesture.
- **[QUESTION-504](../questions.d/QUESTION-504.md)**: part 4's removal arm asks whether adaptive scrolling
  improves assisted performance while training the user to depend on its
  dynamics.
- **What a raw score can see**: with the user's commands held fixed, the
  command-to-displacement information does not prefer a comfortable gain
  ([CLAIM-1191](../claims.d/CLAIM-1191.md)); part 3's comparison is where that matters.

It cannot show anything about First Contact's own domains, and the time
ranges in part 4 and the constants in part 2 are A's engineering choices,
not findings. A noted that work on adaptive kinetic scrolling already
adjusts for overshoot and velocity (a web citation the share does not
preserve), so the open point is whether unsupervised co-adaptation beats
conventional adaptation rules.
