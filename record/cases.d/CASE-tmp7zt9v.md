---
status: Proposed
title: 'Share-dependent advantage under interpretation-independent scoring: in the replicator walk for two processes with a separate interpretation field that authority shapes and the authority score never reads, an incumbent the evidence disfavours keeps its authority above the threshold, and the interpretation follows it against the evidence'
version: 1
standing: stipulated
kind: construction
tags:
- probabilistic-modeling
- self-governance
- epistemology
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
variant_of:
- CASE-155
illustrates:
- CLAIM-tmpsjab8
summary: >-
  Built for [LEAD-121](../leads.d/LEAD-121.md), to separate the two senses of independent scoring in
  [TERM-tmp4iqiv](../terms.d/TERM-tmp4iqiv.md). It is [CASE-155](CASE-155.md) part 4's walk with one change: the
  interpretation is a second state, as in [CASE-099](CASE-099.md), which authority shapes
  and which the authority score never reads. Scoring is then independent of
  the interpretation ([CASE-099](CASE-099.md)'s γ = 0) and not of the loop's state, since
  the score rises with the incumbent's share. Above the threshold
  π* = (1 − h/c)/2 the disfavoured process keeps its authority and the
  interpretation settles on its side against the evidence; with no
  share-dependence it does not. Checked by script (scratch/studies/lead-121/).
  The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmp4iqiv CLAIM-tmpsjab8 CLAIM-tmp528xy — new; filed with this case for LEAD-121 -->

# CASE-tmp7zt9v: Share-dependent advantage under interpretation-independent scoring: in the replicator walk for two processes with a separate interpretation field that authority shapes and the authority score never reads, an incumbent the evidence disfavours keeps its authority above the threshold, and the interpretation follows it against the evidence

## The case

Two processes, A and B, share authority; ℓ is the log odds of A's share π. As in [CASE-155](CASE-155.md) part 4,

    ℓ′ = ℓ + h + c(2π − 1),

with h the log likelihood ratio per step of evidence scored independently (h < 0 favours B) and c > 0 the share-dependent advantage. Added here: an interpretation m, the organization's lean toward A, kept apart from authority as in [CASE-099](CASE-099.md), and moved by its own independent evidence e and by authority (b, [CASE-099](CASE-099.md)'s β):

    m′ = (1 − ρ)m + ρ(e + b(2π − 1)).

Nothing in the authority score reads m. That is [CASE-099](CASE-099.md)'s γ = 0, Regime B ("scoring operators by independently assessed relevance"). The score does read the share.

With h = −0.2, c = 1, e = −0.5, b = 1 and ρ = 0.2, the threshold is π* = 0.6. Runs of 2,000 steps:

| start π₀ | c | final π | final m |
|---|---|---|---|
| 0.55, 0.59 | 1 | 0.0000 | −1.50 |
| 0.61, 0.65, 0.90 | 1 | 1.0000 | +0.50 |
| 0.55 to 0.90 | 0 | 0.0000 | −1.50 |

Above the threshold, A, which the evidence disfavours, takes all the authority, and the interpretation settles at e + b = +0.5, on A's side, against evidence that favours B. With c = 0 every start goes to B, and the interpretation to e − b = −1.5. With |h| ≥ c (h = −1.2) the lock-in is gone from π₀ = 0.99, as [CASE-155](CASE-155.md) says. The script and five tests are in scratch/studies/lead-121/.

## What it can show

That the two senses of independent scoring in [TERM-tmp4iqiv](../terms.d/TERM-tmp4iqiv.md) give different verdicts on one loop. In the first sense this loop's scoring is independent: nothing reads the interpretation. In the second it is not: the score reads the share of authority the interpretation's carrier holds. The loop locks in, interpretation included. So on the first sense it is a loop "whose evidence is scored independently of the interpretation it tests ... shown to lock in all the same", [CLAIM-342](../claims.d/CLAIM-342.md)'s first defeater; on the second it is not.

In [CASE-155](CASE-155.md) itself the senses cannot separate, since belief and authority are one vector there ([CLAIM-444](../claims.d/CLAIM-444.md)): reading the share is reading the interpretation. They come apart only once the interpretation is a state of its own, which is what this case adds.

## What it cannot show

- Which sense [CLAIM-342](../claims.d/CLAIM-342.md) means. That is argued in [CLAIM-tmp528xy](../claims.d/CLAIM-tmp528xy.md) and [CLAIM-tmpsjab8](../claims.d/CLAIM-tmpsjab8.md), filed as alternatives.
- Anything about a finite population, noise, or an organization whose scoring has this form ([CASE-155](CASE-155.md)'s limits carry over).
- That the interpretation's lock-in is self-confirmation. Here m is held by authority, not by evidence it selected; the defeater asks only that the loop lock in.

The wording is the assistant's (Claude, in this session); adopting it is the owner's call.
