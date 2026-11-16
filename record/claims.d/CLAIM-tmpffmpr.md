---
status: Proposed
title: 'When a corrective process is overloaded, its order of review decides whose right to challenge still prevents anything: first-come review spends its capacity on challenges whose windows have already closed and, in the limit, resolves none in time, while an order that skips expired challenges resolves the largest share possible, μ/λ, so the choice of review discipline is a choice about whose rights stay preventive'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation; or a showing that what it assumes away
  carries the result: that a challenge resolved after its window still
  prevents the harm it targets (so that "expired" is not expired), that
  windows cannot be known or estimated when challenges are ordered (so that
  no process could skip expired ones), or that serving expired challenges
  first is required by an obligation the claim ignores, which would make
  the choice not a free one without making the arithmetic false.
tags:
- society-and-governance
- operations-research
- ethics
date: '2026-11-16'
line:
- distributed-agency
rests_on:
- CLAIM-tmpfmmkt
uses:
- TERM-085
bears_on:
- QUESTION-279
summary: >-
  The assistant's, offered at step 12 of the filing of the exchange "Assess
  Depp Heard Abuse" and accepted by the owner on 2026-11-16 ("file your
  ideas as well"). [CLAIM-tmpfmmkt](CLAIM-tmpfmmkt.md) bounds the share of challenges an
  overloaded corrective process can resolve in time at μ/λ, whatever the
  order. This claim says which orders reach the bound and which fall to
  zero: first-come review, the default and the one that looks fair, falls
  to zero because after t* = Fμ/(λ − μ) everything it resolves is already
  too late; serving the newest first, or the oldest challenge whose window
  is still open, reaches μ/λ. So under overload no order preserves everyone's
  right, and choosing one distributes which rights stay preventive. Checked
  by simulation. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpfmmkt CLAIM-tmpuiaop — filed from the exchange "Assess Depp Heard Abuse", Proposed -->

# CLAIM-tmpffmpr: When a corrective process is overloaded, its order of review decides whose right to challenge still prevents anything: first-come review spends its capacity on challenges whose windows have already closed and, in the limit, resolves none in time, while an order that skips expired challenges resolves the largest share possible, μ/λ, so the choice of review discipline is a choice about whose rights stay preventive

## The claim

The setting of [CLAIM-tmpfmmkt](CLAIM-tmpfmmkt.md): valid challenges arrive at rate λ, the
corrective process resolves them at rate μ < λ, and a challenge resolved
more than F after filing comes after the harm it targets has become
irreversible.

1. **Capacity spent on an expired challenge is lost to prevention.** By
   time T at most μT challenges are resolved. Every resolution of a
   challenge whose window has closed is one of those μT that prevents
   nothing. So the number resolved in time is μT minus the resolutions
   spent on expired challenges.
2. **First-come review spends all of it so, eventually.** A challenge filed
   at t waits (λ − μ)t/μ, which exceeds F for every t > t* = Fμ/(λ − μ).
   From the time the challenges filed at t* come up, every resolution is of
   an expired challenge. The number resolved in time stops growing, and its
   share of those filed tends to zero ([CLAIM-tmpfmmkt](CLAIM-tmpfmmkt.md), step 3).
3. **An order that never serves an expired challenge reaches μ/λ.** Serve
   the oldest challenge whose window is still open, and set expired ones
   aside. Once the backlog of open challenges exceeds μ, every resolution is
   in time, so μT − O(1) are, and the share tends to μ/λ, the bound of
   [CLAIM-tmpfmmkt](CLAIM-tmpfmmkt.md). Serving the newest first does the same.
4. **So the order decides who keeps a preventive right.** Under first-come
   review, everyone filed after t* has a right to challenge that prevents
   nothing. Under oldest-open-first, a share μ/λ do, and the rest are set
   aside to remedy. Under newest-first, the same share do, and the oldest
   are never heard. No order preserves everyone's right; each distributes
   which rights stay preventive.

## Check

A day-by-day simulation (`python3 -I`, scratchpad, 2026-11-15) with
A35's numbers, λ = 100, μ = 50, F = 10 days: by day 1,000 first-come
review resolves 1.05% of challenges in time; newest-first and
oldest-open-first each resolve 50.0%, the bound. Under oldest-open-first,
48,950 of the 100,000 challenges filed had expired unheard by day 1,000.

## Why it matters

First-come is the order that looks fair, and under overload it is the one
that defeats prevention entirely: it gives everyone the same right, and
past t* the same right is worth nothing. A process that keeps the formal
right for all and the preventive effect for none fits
[CLAIM-462](CLAIM-462.md)'s separation of effective action from
effective correction, at the level of the reviewer's own procedure: an
overloaded corrector can comply with every rule of review and still have
chosen, by its order, that no one is protected.

The owner's procedural-friction claim ([CLAIM-tmpuiaop](CLAIM-tmpuiaop.md)) says where
opportunities to intervene sit in a process. This claim adds that once a
corrector is overloaded, which of them still matter is fixed by an
administrative choice that is rarely made as a choice.

## What it does not say

- **Which order is just.** Oldest-open-first and newest-first reach the
  same share and distribute it differently; the claim does not choose. Nor
  does it say that triage by severity, which the derivation ignores (all
  challenges are alike here), is wrong.
- **That real correctors run first-come.** It says what first-come does
  under sustained overload, not who uses it.
- **That setting expired challenges aside abandons them.** They remain open
  to remedy after the fact; what they have lost is prevention.
