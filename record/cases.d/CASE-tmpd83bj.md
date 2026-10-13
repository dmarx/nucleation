---
status: Active
title: 'r/place: a shared pixel canvas on which each Reddit user could place one pixel at a time under a cooldown, and communities coordinated off the canvas to build, defend and overwrite images'
version: 1
standing: documented
tags:
- social-ontology
- complex-systems
date: '2026-10-13'
line: distributed-agency
illustrates:
- CLAIM-tmpxuigm
supports:
- CLAIM-tmpgfyls
- CLAIM-tmpjhd7t
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
---
<!-- inactive-ok-file: CLAIM-tmpgfyls CLAIM-tmpjhd7t CLAIM-tmpxuigm LIT-tmp92m28 LIT-tmplgy5c LIT-tmpmc817 LIT-tmprqknl — Proposed or Deferred; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

# CASE-tmpd83bj: r/place: a shared pixel canvas on which each Reddit user could place one pixel at a time under a cooldown, and communities coordinated off the canvas to build, defend and overwrite images

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
deferring to a template is endorsement ([TERM-tmpij1jr](../terms.d/TERM-tmpij1jr.md)).

- **The same act stabilizes or destabilizes, relative to a plan.** A8 §2:
  restoring a pixel is denoising for the group whose image it is, and the
  opposite edit is denoising for its rival ([CLAIM-tmpgfyls](../claims.d/CLAIM-tmpgfyls.md)).
- **Authority off the canvas.** A8 §3: "a participant who creates a
  successful design template might have almost no direct pixel-writing
  capacity beyond any ordinary user, yet exercise enormous influence over
  the pixels that thousands of other users place." The cooldown gave every
  account the same budget of placements, which is a ban on self-allocation
  at the level of pixels. Effective influence still differed by orders of
  magnitude, through recruitment and plans ([CLAIM-tmpxuigm](../claims.d/CLAIM-tmpxuigm.md) is the design
  question it illustrates). It is the record's constitutive influence
  ([CLAIM-086](../claims.d/CLAIM-086.md)): governing the conditions under which placements count.
- **Persistence by contest and repair.** An artwork defended for days has
  every pixel replaced and its defenders turn over
  ([CLAIM-tmpjhd7t](../claims.d/CLAIM-tmpjhd7t.md)). A8 proposed a conditional repair hazard to measure it.

The case sits beside Twitch Plays Pokémon ([CASE-074](CASE-074.md), [CASE-075](CASE-075.md)). There a
crowd's inputs are aggregated into one avatar's moves by a fixed rule. On
r/place nothing aggregates. Each placement lands where it is put, so
territory is contested and the coalitions, plans and alliances that do the
aggregating form off the canvas. It also sits beside Open Horizon
([CASE-006](CASE-006.md)), an organization that persists through turnover. Here the product
and the producer can be followed separately.

The literature registered with it is unread: Litherland and Mørch 2021
([LIT-tmprqknl](../literature.d/LIT-tmprqknl.md)) on instruction and emergence, Adams, Fernandez and Witkowski
2022 ([LIT-tmpmc817](../literature.d/LIT-tmpmc817.md)) on locality, Wu and Silva 2024 ([LIT-tmplgy5c](../literature.d/LIT-tmplgy5c.md)) on
coordination across the three editions, and Falmagne, Stephenson and Levin
2026 ([LIT-tmp92m28](../literature.d/LIT-tmp92m28.md)) on early warnings of transitions.

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
