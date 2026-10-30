---
number: 943
status: Active
formerly:
- THEORY-tmpx9mep
title: 'When a center with no ground truth pays each rater a strictly proper scoring rule on the distribution of a reference rater''s report implied by her own report, under a common prior and a known signal model in which raters'' signals are stochastically relevant to one another, truthful reporting is a strict Nash equilibrium, but not necessarily the only one: in the authors'' two-signal example under the log rule, every rater always reporting h, or always reporting l, is also an equilibrium'
version: 2
history:
- version: 2
  date: '2026-10-30'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings), under ADR-065 §5. Narrowed under ADR-047's "Where a
    narrowing's dropped claims go". A second checker re-derived
    Proposition 1 and the worked example by script (status review 22). The
    expected score of a false h was corrected from −0.754 to −0.760;
    −0.754 is what the posteriors rounded to .54 and .71 give. The last
    clause of the title was narrowed to the authors' example: stated
    generally it is false, since under the quadratic rule a four-signal
    model satisfying every hypothesis has no equilibrium in which all
    raters report one signal. It is routed as kind 3, a clause shown
    false, in the note of 2026-10-30. The demand for the version of record
    (Management Science 2005) is dropped under ADR-065 §4: no discrepancy
    between versions is named, and NOTE-1139 records the copy read (the
    January 2005 final pre-publication draft). The old title: "When a
    center with no ground truth pays each rater a strictly proper scoring
    rule on the distribution of a reference rater's report implied by her
    own report, under a common prior and a known signal model in which
    raters' signals are stochastically relevant to one another, truthful
    reporting is a strict Nash equilibrium, but not the only one:
    equilibria in which every rater reports the same signal regardless of
    what she observed also exist". The old promote_when: The version of
    record (Management Science 2005) read and found to state Proposition 1
    and the example's uninformative equilibria as the January 2005 draft
    does; the proof is two lines and was re-checked when filed, with the
    worked example's numbers. It is refuted if, under a common prior, a
    commonly known signal model, stochastic relevance and risk neutrality,
    some rater facing a truthful reference rater does strictly better in
    expectation by misreporting under a strictly proper scoring rule.
    Evidence about whether real raters report truthfully under the scheme,
    or reach the truthful equilibrium rather than another, neither
    promotes nor refutes this; it is a result about equilibria, not
    behaviour.
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
  −0.69, false h −0.76 under the log rule) re-derived. The same example
  has two uninformative equilibria, which the authors set aside as not
  focal. The scheme replaces ground truth with the center's model of how
  honest signals correlate.
---

# THEORY-943: When a center with no ground truth pays each rater a strictly proper scoring rule on the distribution of a reference rater's report implied by her own report, under a common prior and a known signal model in which raters' signals are stochastically relevant to one another, truthful reporting is a strict Nash equilibrium, but not necessarily the only one: in the authors' two-signal example under the log rule, every rater always reporting h, or always reporting l, is also an equilibrium

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
  a rater who saw l expects −0.690 from reporting l and −0.760 from
  reporting h, although she thinks h the likelier report from her peer.
  Rewarding agreement would have paid her to say h.
- **Uninformative equilibria.** Against a reference rater who always says
  h, reporting h scores ln .712 and l scores ln .536, whatever was seen,
  so always reporting h is an equilibrium; likewise always l. The authors
  call the truthful equilibrium focal and propose that the center punish
  all raters when it detects an uninformative one.

Checked step by step when filed, and again on 2026-10-30 (notes below).

## What this does not say

That raters reach the truthful equilibrium, or that the mechanism resists
collusion, which the authors leave open. That it works when the center's
prior or signal model is wrong, or when raters hold private information
the center does not elicit (their Yes-Man case). Or that the scores
measure the quality of a report in any sense beyond its fit to the
center's model of how honest reports correlate.

## Note of 2026-10-30: the second check and a corrected figure

The second check at the status review (ADR-065 §5) followed each step.

Proposition 1. If the reference rater is truthful, announcing a earns Σ_n
g(n | s) S(g(· | a), n), where s is what the rater saw. A strictly proper
rule makes this largest only at g(· | a) = g(· | s). Stochastic relevance
makes g(· | a) differ from g(· | s) for every a ≠ s, so every lie is
strictly worse.

The example. P(h) = .5 × .85 + .5 × .45 = .65, and P(H | h) = .425/.65 =
.6538, so g(h | h) = .6538 × .85 + .3462 × .45 = .7115. P(H | l) =
.075/.35 = .2143, so g(h | l) = .2143 × .85 + .7857 × .45 = .5357. A rater
who saw l expects .5357 ln .5357 + .4643 ln .4643 = −0.6906 from reporting
l, and .5357 ln .7115 + .4643 ln .2885 = −0.7595 from reporting h. The
file had −0.754 for the second, which is what the posteriors rounded to
.54 and .71 give (−0.7544), and how the paper reaches its −0.75. The
conclusion holds with a wider margin.

The uninformative equilibria. Against a reference rater who always says h,
reporting h scores ln .7115 = −0.340 and l scores ln .5357 = −0.624,
whatever was seen. Against one who always says l, l scores ln .4643 =
−0.767 and h scores ln .2885 = −1.243.

A script (numpy, in the session's scratchpad) reproduced these figures and
ran the search reported in the next note.

## Note of 2026-10-30: the clause the narrowing drops

The title said, under its general hypotheses, that equilibria in which
every rater reports the same signal regardless of what she observed also
exist. The paper says only that "there may be non-truthful equilibria" (p.
9), and its example has them. Stated generally, the clause is false.

Against a reference rater who always announces m, a rater's expected score
from announcing a is S(g(· | a), m), whatever she saw. So all raters
always announcing m is an equilibrium only if a = m maximises it.

A counterexample, under the quadratic rule S(p, m) = 2p_m − Σ_n p_n²,
which is strictly proper. There are two types with prior (.375, .625) and
four signals, drawn independently given the type, with f(· | t₁) = (.220,
.094, .023, .663) and f(· | t₂) = (.675, .022, .130, .173). The posteriors
over a reference rater's signal are g(· | 1) = (.6006, .0338, .1125,
.2531), g(· | 2) = (.3477, .0738, .0530, .5255), g(· | 3) = (.6313, .0289,
.1197, .2200) and g(· | 4) = (.3579, .0722, .0554, .5145). They are
distinct, so stochastic relevance holds. Against a reference rater who
always announces 1, the scores by announcement are (.7626, .2901, .8005,
.3147), so the best reply is 3. Against one who always announces 2 they
are (−.3710, −.2577, −.4043, −.2567), best reply 4. Against 3 they are
(−.2136, −.2992, −.2227, −.2902), best reply 1. Against 4 they are (.0677,
.6457, −.0221, .6279), best reply 2. No signal is its own best reply, so
no equilibrium has every rater report one signal.

A random search over models with 2 to 4 signals found 8 such models in
about 20,000 under the quadratic rule, none of them with two signals, and
none at all under the log rule. For two signals the clause does hold in
general, but that is the record's own derivation and is not filed. The
general clause is shown false, so it is recorded here only (ADR-047's kind
3), and the title now states the authors' example.
