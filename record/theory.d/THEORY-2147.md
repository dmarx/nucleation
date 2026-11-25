---
number: 2147
status: Proposed
formerly:
- THEORY-tmp3tb8i
promote_when: >-
  An independent study, with users other than the authors, finds that
  command-to-transition mutual information ranks interfaces in line with
  ground-truth task reward across several domains, and that maximizing it
  without task reward yields an interface users operate better than a
  random one.
title: 'Command–transition MI scores assistive interfaces'
statement: >-
  Reddy, Levine and Dragan propose that an assistive interface can be scored
  and trained, with no knowledge of the user's task, by the mutual
  information between the user's command and the state transition it
  induces, on the premise that a more intuitive interface makes commands
  less noisy; they find it ranks interfaces with task reward in four of five
  offline domains and learns usable interfaces online, with the time offset
  needing prior knowledge of the timescale of the user's desired influence
version: 1
tags:
- learning-theory
- information-theory
- agency
date: '2026-11-21'
source:
- LIT-2956
bears_on:
- QUESTION-404
summary: >-
  First Contact's central account, read locally on 2026-11-21 ([NOTE-2236](../notes.d/NOTE-2236.md)).
  The record's use of it is [CLAIM-788](../claims.d/CLAIM-788.md) (a channel formed to repair a
  failure of information) and [CLAIM-787](../claims.d/CLAIM-787.md) (the horizon as a level).
  Proposed until an independent replication.
---
<!-- inactive-ok-file: CLAIM-788 CLAIM-787 — Proposed; the claims that use this reading -->

# THEORY-2147: Command–transition MI scores assistive interfaces

## Source

Reddy, Levine and Dragan (2022), [LIT-2956](../literature.d/LIT-2956.md), read as [NOTE-2236](../notes.d/NOTE-2236.md).

## The account

The score is I(x_t, (s_t, s_{t+Δ})), a perception term and a control term.
It needs no task, because a channel the user cannot use leaves commands
uninformative about what follows, whatever they were for. Offline, over
540K timesteps from four prior studies and five domains, it ranked
interfaces with task reward in four (average Spearman ρ = 0.43 over all
five), and the top-scoring interface in each domain had the top reward.
Online, maximized over a one-parameter cursor interface with 12 users, it
tracked reward at ρ = 0.87 and converged on no rotation or exact inversion;
over an eight-parameter gesture interface, one user came to avoid crashing.

What could have come out otherwise: the offline ranking was tested against
ground truth the method never saw, and in one domain it failed outright at
Δ = 1, which is how the horizon limit was found.

## What it does not show

- Not that the score measures intuitiveness. Users adapt (assumed, Fig. 1),
  and an inversion scores as well as no rotation; the anthology's reading,
  [ANTH-THEORY-091](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-091.md), is that it rewards a learnable channel.
- Not that learned interfaces transfer, to new targets, tasks or users; no
  such test is run.
- Not that assistance it scores well leaves the user's own skill intact;
  unassisted skill is not measured.
- Not a general rule for Δ; the authors call its choice the primary limit.
