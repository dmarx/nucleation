---
number: 595
status: Active
formerly:
- CLAIM-tmpiyvk1
title: 'Persistence and nucleating productivity in the committor sense vary independently: two intermediates of an assembly can have the same expected residence time and different chances of reaching the target before failure, since the committor depends only on where a state''s exits lead and not on how fast it leaves, and an intermediate can persist while lowering the target''s chance of forming against an admissible alternative'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings; ADR-057, ADR-047 kind 3): the title began
    "Persistence and nucleating productivity vary independently", and
    the body concedes that the independence fails for success by a
    deadline, so the title now says it holds in the committor sense.
    Its one premise, TERM-117, was adopted in the same change; the
    committor argument was followed and the deadline table re-run
    (scratch/formal/dna_origami_toys.py, python3 -I).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the argument: a continuous-time Markov chain in which two
  transient states with equal total exit rates and equal residence times
  must have equal committors, or in which scaling all of one state's exit
  rates by the same factor changes its committor. Not defeated by evidence
  about what nuclei in real organizations do, which the claim does not
  assert.
tags:
- mathematics
- complex-systems
- natural-sciences
date: '2026-11-05'
line:
- realizability
- nucleating-argument
- formal-apparatus
uses:
- TERM-117
bears_on:
- QUESTION-038
- QUESTION-380
summary: >-
  A's candidate claim, from the third synthesis on DNA origami pasted by the
  owner on 2026-11-05 (§§2 and 10): "Persistence and nucleating
  productivity can vary independently." A's example has two intermediates,
  both with total exit rate 0.10 and so expected residence time 10; one
  exits to the target at 0.08 and to a trap at 0.02, the other the reverse.
  Their committors are 0.8 and 0.2. The assistant adds the general reason:
  a state's committor is the exit-probability-weighted average of its
  successors' committors, so its total exit rate, which sets how long it
  persists, cancels. A's second part is that "an intermediate can persist
  while reducing the target's formation probability". It is the trap of
  [CLAIM-184](CLAIM-184.md), shown in DNA origami by Dunn et al.'s seams. The wording is
  A's, with the assistant's proof; adopting it is the owner's call.
complements:
- CLAIM-596
- CLAIM-599
- CLAIM-601
---
<!-- inactive-ok-file: CASE-218 — Proposed or new; cited from the note on A's predictions -->
<!-- inactive-ok-file: CLAIM-184 CLAIM-185 — Proposed, Skimmed or new; entries cited as open -->

# CLAIM-595: Persistence and nucleating productivity in the committor sense vary independently: two intermediates of an assembly can have the same expected residence time and different chances of reaching the target before failure, since the committor depends only on where a state's exits lead and not on how fast it leaves, and an intermediate can persist while lowering the target's chance of forming against an admissible alternative

## The claim

Take a continuous-time Markov chain with rates Q_ij, a target set F and a
failure set K, both absorbing. For a transient state i the committor
satisfies Σ_j Q_ij q(j) = 0, which is

  q(i) = Σ_{j≠i} (Q_ij / λ_i) q(j),  with λ_i = Σ_{j≠i} Q_ij.

The expected residence time in i is 1/λ_i.

1. **Persistence and committor are separate coordinates.** Multiplying every
   exit rate of i by c > 0 changes its residence time by 1/c and leaves the
   ratios Q_ij/λ_i, and so q(i), unchanged. A state can be made as
   persistent as one likes without changing its chance of success, and two
   states of equal persistence can have any committors their exit
   probabilities allow. A's example: λ = 0.10 for both intermediates, with
   q = 0.08/0.10 = 0.8 for one and 0.02/0.10 = 0.2 for the other.
2. **Persistence can lower the target's chance.** If an intermediate N
   exits mainly to K, then forming N and holding it, rather than an
   admissible alternative from which F is likelier, lowers the chance of
   reaching F. In A's words, an intermediate "can persist while reducing
   the target's formation probability relative to an admissible
   alternative".

## Eventual success is not success by a deadline

The committor is an eventual measure, and a productive nucleus is
horizon-relative ([TERM-117](../terms.d/TERM-117.md)). A's review of this pull request draws
the consequence. A state that exits to the target at rate α and to
failure at β succeeds by time T with chance

  P_F(T) = α/(α+β) · (1 − e^{−(α+β)T}).

Scaling both rates by the same factor leaves α/(α+β), and so the
committor, unchanged, but changes P_F(T). At T = 10, computed in
scratch/formal/dna_origami_toys.py:

| Nucleus | Eventual success | Success by T = 10 |
|---|---|---|
| α = 0.08, β = 0.02 | 80 % | 50.6 % |
| both tenfold slower | 80 % | 7.6 % |

So a stabilization that slows every exit from a nucleus keeps its
eventual chance and can make it nearly useless under a deadline. This is
the readiness line's distinction between eventual capability and
capability on time. Point 1 above holds for the committor, and for
deadline success it fails.

## The molecular instance

Dunn et al. ([NOTE-1643](../notes.d/NOTE-1643.md)): long-range seam staples that bind early and
"effectively, irreversibly" trap folding into the wrong fold. The trap
persists, and persisting is what makes it a trap.

## What it qualifies

- **[CLAIM-185](CLAIM-185.md)'s anchor.** "Persistence makes anchoring possible;
  productivity requires demonstrating that the anchor improves subsequent
  development." A: "A stable anchor is not necessarily a good anchor."
  [CLAIM-184](CLAIM-184.md) says early anchors can entrench; this claim says entrenchment
  is invisible in persistence alone.
- **[QUESTION-038](../questions.d/QUESTION-038.md),** what turns a persisting structure into an anchor. This
  claim says it is not persistence.

## What it does not say

- **That a high committor shows a cause.** "The intermediate might simply
  occur along already-favorable trajectories, without being responsible
  for their success" ([TERM-117](../terms.d/TERM-117.md)'s interventional measure).
- **Anything about organizations** beyond the logic. A: "The broader
  organizational interpretation remains to be tested."

## Note of 2026-11-05: A's predictions on productive nucleation

From the fourth synthesis on DNA origami by another assistant (A), "Predicting which organizations will successfully nucleate", pasted by the owner on 2026-11-05.

A's fourth synthesis proposes the claim in a fuller form: "equally persistent intermediate structures can differ in their probability of reaching a target before failure; and strengthening an intermediate can increase initial formation while reducing final yield." The first half is this claim. The second is shown by A's stabilization toy ([CASE-218](../cases.d/CASE-218.md)): yield peaks at s ≈ 1.11 with 40.2 %, and falls beyond as nucleation rises and completion falls. A: "The interpretation in terms of organizational development remains a separate claim."

No status changes.

## Note of 2026-11-05: the readings on correction, repair, replication and nucleation barriers

Read at the owner's invitation to add readings to the DNA origami filing; the works were chosen by the assistant.

**Winfree and Bekbolatov, "Proofreading tile sets".** Supports in kind. The paper's error rate is a committor in an absorbing Markov chain: "the probability that, starting in E, the system reaches F M". Proofreading lowers it by changing where exits lead, since every path to a mismatch needs two unfavourable steps, not by lengthening residence. Left open: residence times are not held equal, so the claim's independence is not tested directly.

No status changes.
