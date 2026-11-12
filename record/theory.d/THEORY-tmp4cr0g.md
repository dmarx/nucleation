---
status: Proposed
title: 'Halpern and Moses: over a channel that can lose messages, or whose delivery times are uncertain, communication cannot make common knowledge any fact that was not common knowledge at the start, so no protocol guarantees an action that requires it'
version: 1
tags:
- logic
- epistemology
- agency
date: '2026-11-12'
source:
- LIT-1213
promote_when: >-
  The title is checked against the statements and proofs NOTE-1381 records
  for Theorem 5 (communication not guaranteed), Theorem 8 with Lemma 14
  (uncertain start and delivery times) and Corollary 6 and Proposition 10
  (no guaranteed coordinated or eventually coordinated attack), and asserts
  nothing beyond them: no claim about probabilistic coordination, which
  the paper leaves aside, and none resting on Theorems 7, 11 or 12, whose
  proofs NOTE-1381 did not check.
bears_on:
- QUESTION-tmpxq2sb
summary: >-
  The central result of [LIT-1213](../literature.d/LIT-1213.md), read in full in [NOTE-1381](../notes.d/NOTE-1381.md) on 2026-10-29,
  which had no THEORY. Common knowledge of a fact is the greatest fixed
  point of everyone knowing the fact and it; a guaranteed simultaneous
  coordinated action makes itself common knowledge (Proposition 4); over a
  channel that can lose any message, no fact becomes common knowledge that
  was not so at the start (Theorem 5), and the same holds when start and
  delivery times are uncertain, even if every message arrives (Theorem 8);
  so no protocol guarantees coordinated attack, simultaneous or eventual
  (Corollary 6, Proposition 10). Filed so that claims using the result
  ground on a reading, not on the bare work: [CLAIM-tmpyp3u3](../claims.d/CLAIM-tmpyp3u3.md) through
  [ARG-tmpbuocw](../arguments.d/ARG-tmpbuocw.md). [CLAIM-346](../claims.d/CLAIM-346.md), whose third obstruction is this result, grounds
  elsewhere and is left as it is. One of the filer's own ideas from the
  exchange "luria experiment design", accepted by the owner. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpyp3u3 ARG-tmpbuocw — filed from the exchange "luria experiment design", Proposed -->

# THEORY-tmp4cr0g: Halpern and Moses: over a channel that can lose messages, or whose delivery times are uncertain, communication cannot make common knowledge any fact that was not common knowledge at the start, so no protocol guarantees an action that requires it

## The account

Halpern and Moses ([LIT-1213](../literature.d/LIT-1213.md)), as read in [NOTE-1381](../notes.d/NOTE-1381.md), from the authors'
arXiv deposit, which they describe as essentially identical to the Journal
of the ACM version of 1990.

- **The notions.** For a group G: distributed knowledge D_G φ, what someone
  holding all their views together would know; everyone knows, E_G φ, and
  its k-fold nesting; and common knowledge C_G φ, the greatest fixed point
  of X ≡ E_G(φ ∧ X).
- **Why coordination needs it.** In any correct coordinated-attack
  protocol, whenever the generals attack it is common knowledge that both
  are attacking (Proposition 4). No finite E^k suffices: coordinated attack
  reaches E^k for any k when k messages arrive, and still cannot attack
  ([NOTE-1381](../notes.d/NOTE-1381.md)'s C7).
- **Why communication cannot supply it.** If communication is not
  guaranteed, a point of a run satisfies C_G φ exactly when the same point
  of the run with the same start and no messages received does (Theorem
  5). Unreliable channels are not needed: with uncertainty in start and
  delivery times, no fact becomes common knowledge that was not so at the
  start (Theorem 8, through Lemma 14; [NOTE-1381](../notes.d/NOTE-1381.md) checked these except
  Proposition 15's sketch).
- **The consequence.** Any correct coordinated-attack protocol guarantees
  that neither party ever attacks (Corollary 6), and even eventually
  coordinated attack cannot be guaranteed over a lossy channel
  (Proposition 10 via Theorem 9).

## What the account does not cover

- Probabilistic coordination: the paper notes that a high-probability
  attack is achievable and leaves it aside.
- The weaker forms the paper defines for practice, ε-, eventual and
  timestamped common knowledge (§§11–12; [NOTE-1381](../notes.d/NOTE-1381.md)'s C6, moderate), and
  Theorems 11 and 12 about them, whose proofs [NOTE-1381](../notes.d/NOTE-1381.md) did not check.
  They are left out of the title for that reason.
