---
number: 943
status: Proposed
formerly:
- THEORY-tmpx9mep
promote_when: >-
  The version of record (Management Science 2005) read and found to state
  Proposition 1 and the example's uninformative equilibria as the January
  2005 draft does; the proof is two lines and was re-checked when filed,
  with the worked example's numbers. It is refuted if, under a common prior,
  a commonly known signal model, stochastic relevance and risk neutrality,
  some rater facing a truthful reference rater does strictly better in
  expectation by misreporting under a strictly proper scoring rule. Evidence
  about whether real raters report truthfully under the scheme, or reach
  the truthful equilibrium rather than another, neither promotes nor
  refutes this; it is a result about equilibria, not behaviour.
title: 'When a center with no ground truth pays each rater a strictly proper scoring rule on the distribution of a reference rater''s report implied by her own report, under a common prior and a known signal model in which raters'' signals are stochastically relevant to one another, truthful reporting is a strict Nash equilibrium, but not the only one: equilibria in which every rater reports the same signal regardless of what she observed also exist'
version: 1
tags:
- game-theory
- epistemology
date: '2026-10-24'
source:
- LIT-1518
summary: >-
  Miller, Resnick and Zeckhauser's Proposition 1, read in full in
  [NOTE-1139](../notes.d/NOTE-1139.md) from the January 2005 draft, with the proof and the worked
  example (p(H) = .5, f(h | H) = .85, f(h | L) = .45; honest l scores
  −0.69, false h −0.75 under the log rule) re-derived. The same example
  has two uninformative equilibria, which the authors set aside as not
  focal. The scheme replaces ground truth with the center's model of how
  honest signals correlate.
---

# THEORY-943: When a center with no ground truth pays each rater a strictly proper scoring rule on the distribution of a reference rater's report implied by her own report, under a common prior and a known signal model in which raters' signals are stochastically relevant to one another, truthful reporting is a strict Nash equilibrium, but not the only one: equilibria in which every rater reports the same signal regardless of what she observed also exist

## Source

Miller, Resnick & Zeckhauser (2005), [LIT-1518](../literature.d/LIT-1518.md), read in [NOTE-1139](../notes.d/NOTE-1139.md)
from the authors' final pre-publication draft: Proposition 1 and its
proof (p. 8), the worked example (pp. 6–8) and footnote 12 (p. 9).

## What was actually shown

- **Truthful equilibrium.** If the reference rater reports truthfully,
  rater i's expected score from announcing a is Σ_n R(s_n | a) g(s_n | s),
  where s is what she saw. A strictly proper rule maximizes this only at
  a = s, so truth is a strict best reply. Stochastic relevance makes the
  posterior differ across announcements, so every lie is strictly worse.
- **The example.** g(h | l) = .536 and g(h | h) = .712. Under the log rule
  a rater who saw l expects −0.690 from reporting l and −0.754 from
  reporting h, although she thinks h the likelier report from her peer.
  Rewarding agreement would have paid her to say h.
- **Uninformative equilibria.** Against a reference rater who always says
  h, reporting h scores ln .712 and l scores ln .536, whatever was seen,
  so always reporting h is an equilibrium; likewise always l. The authors
  call the truthful equilibrium focal and propose that the center punish
  all raters when it detects an uninformative one.

Checked step by step when filed.

## What this does not say

That raters reach the truthful equilibrium, or that the mechanism resists
collusion, which the authors leave open. That it works when the center's
prior or signal model is wrong, or when raters hold private information
the center does not elicit (their Yes-Man case). Or that the scores
measure the quality of a report in any sense beyond its fit to the
center's model of how honest reports correlate.
