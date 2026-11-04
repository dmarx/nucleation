---
number: 79
status: Active
formerly:
- CASE-tmpd83bj
title: 'r/place: a shared pixel canvas on which each Reddit user could place one pixel at a time under a cooldown, and communities coordinated off the canvas to build, defend and overwrite images'
version: 1
standing: documented
kind: specimen
tags:
- social-ontology
- complex-systems
date: '2026-10-13'
line: distributed-agency
illustrates:
- CLAIM-285
supports:
- CLAIM-279
- CLAIM-280
- CLAIM-272
- CLAIM-273
- CLAIM-274
summary: >-
  The owner proposed it at U8 of the 2026-10-13 exchange: "every user can
  modify a single pixel once, and different subreddits coordinated to
  present certain images or even warred amongst each other over regions
  of the canvas". Reddit ran it in 2017, 2022 and 2023, and released the
  2022 placement log. A8 read it as the exchange's two canvases made
  visible: the pixels as the meaning canvas, the plans, templates and
  alliances off the canvas as the influence canvas. First time the thing
  turns up in the record. The event and the data are documented. The
  readings of them are proposals.
reported_in:
- LIT-1025
- LIT-1032
- LIT-1037
---
<!-- inactive-ok-file: CLAIM-285 — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: THEORY-224 — Proposed; cited from the exchange "Organizational Nucleation and SLT" of 2026-11-04 as open -->

# CASE-079: r/place: a shared pixel canvas on which each Reddit user could place one pixel at a time under a cooldown, and communities coordinated off the canvas to build, defend and overwrite images

## The case

The owner, at U8: "another case worth examining is those collective
experiments reddit used to do annually on April 1st, like the one where
every user can modify a single pixel once, and different subreddits
coordinated to present certain images or even warred amongst each other over
regions of the canvas".

The facts, checked on 2026-10-13. The 2017 event ran for 72 hours on a
1000 × 1000 canvas. About 1.1 million users placed about 16.5 million tiles
(Fastly's write-up of Reddit's engineering talk,
https://www.fastly.com/blog/reddit-on-building-scaling-rplace; Reddit's own
post is quoted as "~16 million"). A user could place one pixel, then had to
wait. The cooldown was five minutes for most of the event and varied between
5 and 20 (https://en.wikipedia.org/wiki/R/place). It returned on 1 April 2022
and ran again on 20–25 July 2023. For 2022 Reddit released the placement
log, with a UTC timestamp, a hashed user id, a colour and coordinates for
each placement (r/place post "r/place datasets (April Fools 2022)", seen
through mirrors). The log does not record subreddit membership, plans or who
followed whom. Self-declared groups such as "the Void" set out to cover
others' work in black.

So the owner's "once" is once per cooldown, not once per event. The point
the owner drew from it stands: no single user can hold a region, and only
coordination can build or defend an image.

## What it can show

A8 mapped the exchange's model onto it. The pixel array is observable, and
what the pixels mean to each group is latent. Users, groups, subreddits,
bots and alliances are operators at different scales. Following a plan or
deferring to a template is endorsement ([TERM-053](../terms.d/TERM-053.md)).

- **The same act stabilizes or destabilizes, relative to a plan.** A8 §2:
  restoring a pixel is denoising for the group whose image it is, and the
  opposite edit is denoising for its rival ([CLAIM-279](../claims.d/CLAIM-279.md)).
- **Authority off the canvas.** A8 §3: "a participant who creates a
  successful design template might have almost no direct pixel-writing
  capacity beyond any ordinary user, yet exercise enormous influence over
  the pixels that thousands of other users place." The cooldown gave every
  account the same budget of placements, which is a ban on self-allocation
  at the level of pixels. Effective influence still differed by orders of
  magnitude, through recruitment and plans ([CLAIM-285](../claims.d/CLAIM-285.md) is the design
  question it illustrates). It is the record's constitutive influence
  ([CLAIM-086](../claims.d/CLAIM-086.md)): governing the conditions under which placements count.
- **Persistence by contest and repair.** An artwork defended for days has
  every pixel replaced and its defenders turn over
  ([CLAIM-280](../claims.d/CLAIM-280.md)). A8 proposed a conditional repair hazard to measure it.

The case sits beside Twitch Plays Pokémon ([CASE-074](CASE-074.md), [CASE-075](CASE-075.md)). There a
crowd's inputs are aggregated into one avatar's moves by a fixed rule. On
r/place nothing aggregates. Each placement lands where it is put, so
territory is contested and the coalitions, plans and alliances that do the
aggregating form off the canvas. It also sits beside Open Horizon
([CASE-006](CASE-006.md)), an organization that persists through turnover. Here the product
and the producer can be followed separately.

The literature registered with it, read the same day: Litherland and Mørch
2021 ([LIT-1037](../literature.d/LIT-1037.md)) on Reddit's rules ("instruction") against the planning
that arose among participants ("emergence"), Adams, Fernandez and Witkowski
2022 ([LIT-1034](../literature.d/LIT-1034.md)) on locality, Wu and Silva 2024 ([LIT-1032](../literature.d/LIT-1032.md)) on
coordination across the three editions, and Falmagne, Stephenson and Levin
2026 ([LIT-1025](../literature.d/LIT-1025.md)) on early warnings of transitions.

## What it cannot show

The log shows behaviour, not endorsement. A8 §7: "Pixel-placement data can
reveal behavioral coordination, but they cannot by themselves tell us
whether one participant endorsed another, followed an instruction, shared an
intention, or independently converged on the same action." Coordination
records, such as plans and template histories, would be needed. A8 also
warned that a model with latent coalitions can predict better just by having
more parameters, so comparisons must control for complexity. And, A8 §9: "an
artwork is not thereby a self". The case shows organization without settling
agency.

A8 said Reddit's engineering retrospective discusses automated-account
clusters. That retrospective was not read, and it is not relied on here.

## Note of 2026-10-13: what the readings add to the facts

The four registered studies are now read. One fact above is incomplete.
Reddit released placement logs for all three editions, not only 2022.
Litherland and Mørch ([LIT-1037](../literature.d/LIT-1037.md)) used the official 2017 data set, "all
16.5 million placed tiles" with hashed usernames, and Falmagne et al.
([LIT-1025](../literature.d/LIT-1025.md)) and Wu and Silva ([LIT-1032](../literature.d/LIT-1032.md)) used the 2022 and 2023 logs
from placedata.reddit.com. Automation can now be sourced without the
unread engineering retrospective. Falmagne et al. put cooldown-breaking
changes at under 1% of 2022 changes. Wu and Silva attribute 17.1% of 2023
actions, and 0.3% of 2017 actions, to accounts exceeding one action per
five minutes. Unverified accounts sometimes had 10- or 20-minute cooldowns
(Falmagne et al., SI). The planning layer this case calls the influence
canvas is observed directly for one artwork in [LIT-1037](../literature.d/LIT-1037.md). There the
design was negotiated in a forum of 161 accounts while about 77,000 placed
tiles ([THEORY-218](../theory.d/THEORY-218.md)).

## Note of 2026-11-04: accommodation that enlarges what is feasible, from "Organizational Nucleation and SLT"

The owner's U16 pointed to the Twitch Plays Pokémon cases and this one.

What A16 adds here:

- **A pixel is an intervention on the current state.** In the owner's
  sense (U17, as the owner clarified at review), an intervention is taking
  an action, and placing a pixel changes the canvas. What the placement
  does not show is its motive: it "might express disagreement with an
  artwork, loyalty to a template, or merely participation in a local
  contest" (A16 §3).
- **Off-canvas plans enlarge the complex.** A16 §6: negotiated boundaries
  or shared plans may change "the *actual conditions under which groups can
  realize their preferred outcomes*. That can expand compatibility at fixed
  tolerances." It is "organizational accommodation that alters what is
  jointly feasible". Twitch's shown tally only coordinates ([CASE-074](CASE-074.md)).
- **Coordination need not be off the canvas (the owner, at review).**
  Coalitions also form in response to the canvas itself: a participant
  who recognizes a pattern can extend it from the local context alone, so
  allegiance and endorsement can be recruited through indirect
  communication that the canvas mediates. Off-canvas coordination is more
  likely to succeed and persist, but it is not necessary. This qualifies
  "only coordination can build or defend an image" above, and the reading
  of the plans as the only influence canvas: the canvas is a channel too.
  [THEORY-224](../theory.d/THEORY-224.md) (Adams, Fernandez and Witkowski, [LIT-1034](../literature.d/LIT-1034.md)) holds the two
  kinds, objects that spread by a local rule and are predictable from the
  canvas, and objects copied from designs coordinated elsewhere.
- In this record's terms, the first is relief in [CLAIM-347](../claims.d/CLAIM-347.md)'s sense, and
  [QUESTION-133](../questions.d/QUESTION-133.md) asks when differentiation gives it. A16: "Neither is
  necessarily authentic."

No status changes.
