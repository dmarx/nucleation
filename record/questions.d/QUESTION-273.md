---
number: 273
status: Open
formerly:
- QUESTION-tmpu6zq7
title: 'With one population of perspectives, do the three ways of giving them influence that the owner proposed (neighbourhoods in a space whose radii others can change, a shared channel into which they emit at rates, and a budget of passes or locations at which each may act on a common representation) produce different collective decision regimes, and how far does each mechanism''s nominal resource predict the counterfactual influence a perspective actually has?'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed from U33 of the exchange. Amended the same day after the readings
    of MultiDiffusion and Multi-LoRA composition: the third mechanism has
    two published forms and A45's a third, and two results bear against the
    no branch in its time-averaged form. The question stays Open.
- version: 2
  date: '2026-10-26'
  note: >-
    A dated note added: the lab's v2.8 (dmarx/PerspectiveLab@c54617e) builds
    the convex-share mechanism and a sequential mode, and measures a
    perspective's exclusion effect apart from its grant; most of the
    measured rise is a concept only that perspective writes. The other two
    mechanisms are not built and the matched-budget comparison is not run.
    The question is unchanged.
tags:
- complex-systems
- self-governance
- network-science
date: '2026-10-25'
line: distributed-agency
summary: >-
  The owner, at U33 of the exchange of 2026-10-24, continued. It is the
  third appearance of the owner's own model: on 2026-10-13, U1 was "a
  population of denoisers, each of which has different reach, salience
  valuation, translation (motion across canvas) rate, influence strength"
  and U2 the influence canvas ([CLAIM-285](../claims.d/CLAIM-285.md), [TERM-053](../terms.d/TERM-053.md)). Here three mechanisms
  are named. A33, A35 and A36 each took influence to be control over
  opportunities to modify a shared state, and separated nominal access,
  its use and its counterfactual effect. The owner took up the build from
  U37.
bearing:
- THEORY-958
---
<!-- inactive-ok-file: CLAIM-279 CLAIM-285 CLAIM-297 CLAIM-336 THEORY-925 — Proposed; the owner's earlier model and the claims and reading that hold its parts, cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-949 — Proposed; the switching ablation as Zhong et al. report it, its sample unreported, cited as bearing on the question, not as settling it -->

# QUESTION-273: With one population of perspectives, do the three ways of giving them influence that the owner proposed (neighbourhoods in a space whose radii others can change, a shared channel into which they emit at rates, and a budget of passes or locations at which each may act on a common representation) produce different collective decision regimes, and how far does each mechanism's nominal resource predict the counterfactual influence a perspective actually has?

## Why it is a question

The owner, at U33: "I feel like we need the competing perspectives modeled
as independent objects. still on the fence about how to model their
respective relationships and things like influence. maybe model them in a
geometric space where influences are given by neighborhoods and the
perspectives can impact each others neighborhood radius? or maybe there's
a common communication channel that they emit messages into and their
influence is the rate at which they emit into the channel? or maybe a
population of denoisers and their influence is the number of iterations or
locations a given denoiser can apply to a common representational space
during a step?"

A33: "**Influence may be better modeled as control over opportunities to
modify a shared state, rather than as a scalar amount of authority.**" It
put all three under one schedule of opportunities to act: "Your proposals
then become alternative realizations of 𝒢". A36: "I would use the same
independent perspective objects under each mechanism and change **only how
they obtain opportunities to influence the shared workspace**", run first
"as **separate experimental treatments**".

The record holds the parts. The neighbourhood radius that others can
change is [TERM-053](../terms.d/TERM-053.md)'s endorsement in geometric form, and with [CLAIM-285](../claims.d/CLAIM-285.md)'s
condition no perspective controls its own. Operators acting on a shared
interpretive state are [CLAIM-297](../claims.d/CLAIM-297.md)'s and [CLAIM-336](../claims.d/CLAIM-336.md)'s model. Denoiser as a
regime and not a kind is [CLAIM-279](../claims.d/CLAIM-279.md). What no entry asks is whether the
mechanism of influence matters once its budget is matched.

Three distinctions the replies drew, which an answer must keep:

- **Nominal, used and effective.** A33 separated "nominal resources
  (radius, messages, passes), effective realized influence (counterfactual
  change caused), and independently evaluated benefit": "emission rate is
  not effective influence". Transmission count is not independent evidence
  either. A38 later reported that counting forwarded messages as new made a
  population more confident and less accurate, which is persuasion bias
  ([QUESTION-117](QUESTION-117.md)).
- **Receiver against speaker.** A36: "the receiver's radius r_j determines
  which sources are salient *to that receiver*". Neighbourhoods that the
  receiver controls are not ones the speaker controls.
- **Order.** Two operators need not commute. A33: "Authority can reside in
  *sequence position*, not just frequency".

The measure the replies proposed, I_i = E d(Z^full, Z^{do(exclude i)})
(A35), is the wonderful-life or difference reward ([LIT-1506](../literature.d/LIT-1506.md)) and, per
action, COMA's counterfactual baseline ([THEORY-925](../theory.d/THEORY-925.md)). A35: "This
quantity will depend on context and need not be additive across
processes."

Later turns of the same exchange qualified the third mechanism. A45: "Running a
complete scheduler step separately for each perspective would confound
influence with the number of physical denoising steps." Its sampler gives
each perspective a share of one combined step, not a number of passes, a
departure from the owner's option that the reply did not flag.

**The third mechanism is published, in two forms.** "Locations" is
MultiDiffusion ([LIT-1522](../literature.d/LIT-1522.md), [NOTE-1158](../notes.d/NOTE-1158.md)): each view has jurisdiction over
a set of pixels, and its nominal weight at a pixel is exactly its convex
share of that pixel's step ([THEORY-958](../theory.d/THEORY-958.md), in part an answer).
"Iterations" is LoRA Switch ([LIT-1529](../literature.d/LIT-1529.md), [NOTE-1160](../notes.d/NOTE-1160.md)): one LoRA acts at a
time, in rotation. A45's share of one combined step is LoRA Composite. Per
step all three are convex weightings of the operators' predictions. Two
results bear against the no branch in its time-averaged form, every
mechanism reducing to one vector of weights. At equal step shares, the
switching interval and which LoRA acts first change the result
([THEORY-949](../theory.d/THEORY-949.md)). And the same masks used differently in the early steps
change layout IoU from 0.18 to 0.26 ([THEORY-948](../theory.d/THEORY-948.md)). Neither paper
measures any operator's counterfactual influence, so the question stays
open.

## What would answer it

One population and one evidence stream, run under each mechanism with
matched nominal budgets. For the collective, the regime by
[CLAIM-453](../claims.d/CLAIM-453.md)'s diagnostics: conditional drift and diffusion of the
readout, and its serial dependence. For each perspective, nominal resource
against counterfactual influence. A yes is mechanisms that differ in
regime, or in how far nominal resource predicts influence, at matched
budgets. A no is that, at matched budgets, every mechanism reduces to one
vector of influence weights, the ℓ of [CASE-160](../cases.d/CASE-160.md).

The apps the exchange reported for U33 and after (a population lab, then
v0.2 to v1.0) are not held, and the record has not run the comparison.

## Note of 2026-10-26: one mechanism built, with grant and exclusion effect measured

The apps of U33 and after are now held, as dmarx/PerspectiveLab. Its v2.8
(dmarx/PerspectiveLab@c54617e experiments/perspective_engine/) builds
one of the three mechanisms in A45's form, a share of one combined step.
A governor combines the perspectives' proposals for each concept by their
nominal grants, from one frozen snapshot. A sequential mode re-evaluates
each perspective after the previous one's update, with the same shares
per concept, and the lab's tests show that its result depends on the
order. Neither neighbourhoods with radii nor a channel with emission rates
is built, and the study runs only the synchronous mode.

It does measure influence apart from grant. A perspective's effect is the
distance between the workspace after five updates with and without its
grant, from the same starting state. Over 24 seeds the reframer's grant is
0.18 with and without its new frame, and its effect rises from 0.059 to
0.748 when the frame is active. With the frame and a grant of 0.60 it is
0.914. Most of that rise is a coordinate only the reframer writes:
excluding it removes the new concept, and the distance counts the
missing coordinate as a full difference. On the decision coordinate
alone, in a rerun of the lab's code for this review, the reframer's
effect with the frame is 0.247 where the cue is positive and 0.069 where
it is negative, against 0.059 without the frame. The report describes the
24 seeds as a "matched positive-cue initial state". They are not: 16 have
a positive cue and 8 a negative one, and each run starts with the arm
already applied rather than after four common updates.

Within this one mechanism, then, a perspective's grant does not predict
its counterfactual influence once a new frame changes what it can read.
That bears on the question's second part for the convex share only, in
one construction. The matched-budget comparison of the three mechanisms
is not run. The question is unchanged.
