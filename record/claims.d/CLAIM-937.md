---
number: 937
status: Proposed
formerly:
- CLAIM-tmp1o9d0
title: 'Contextuality-by-Default signalling has no unbiased estimator at any finite count, but it has a confidence interval and a no-signalling test that are valid at every count, and a content seen at most twice in each context can never be found signalling by a valid 5% test'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  Any one of three. An estimator from finitely many occurrences that is
  unbiased for the signalling Δ of binary contents over a family of
  systems whose marginals fill an open set; or a binary system and
  occurrence counts at which the simultaneous Clopper-Pearson interval
  for Δ, built as stated here, covers the true Δ with probability below
  its nominal level, by exact computation or beyond Monte Carlo error;
  or a nonrandomized level-α test of equal marginals for one content, from
  n and m occurrences, that rejects some table although
  nⁿmᵐ/(n+m)ⁿ⁺ᵐ exceeds α.
tags:
- mathematical-statistics
- contextuality
date: '2026-11-22'
line:
- pragmatic-transport
- formal-apparatus
grounds:
- CASE-359
- THEORY-177
complements:
- CLAIM-235
- CLAIM-896
summary: >-
  Derived for [LEAD-072](../leads.d/LEAD-072.md) on 2026-11-22 and checked by exact enumeration
  and simulation ([CASE-359](../cases.d/CASE-359.md)). Δ, a sum of absolute differences of
  binomial means, is not a polynomial in the probabilities, so no
  estimator is unbiased for it, whatever the counts; bias can be reduced,
  not removed. The squared difference is unbiasedly estimable, and its
  root halves the plug-in's bias where signalling is small, at a cost
  where it is large. What can be stated is an error: simultaneous
  Clopper-Pearson intervals for every marginal give an interval for Δ
  valid at any count, and exact per-content tests, combined by
  Bonferroni, give a test of the null that no content signals. Neither
  can say anything from one or two occurrences a context. This answers
  the estimator half of [CLAIM-235](CLAIM-235.md)'s request; the data half waits on
  counts [LIT-851](../literature.d/LIT-851.md) does not print. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-359 — new; the study this claim is checked by, filed with it -->
<!-- inactive-ok-file: CLAIM-896 — Proposed; LEAD-182's finding on the plug-in's bias in a power study, which this claim complements -->
<!-- inactive-ok-file: CLAIM-105 — Proposed; the claim whose defeat condition needs a stated sampling error -->

# CLAIM-937: Contextuality-by-Default signalling has no unbiased estimator at any finite count, but it has a confidence interval and a no-signalling test that are valid at every count, and a content seen at most twice in each context can never be found signalling by a valid 5% test

## The claim

Set-up. A binary content q is recorded in two contexts. In the first it
takes the value +1 in x of n occurrences, in the second in y of m, with
true probabilities p and p′. CbD's signalling, as [LIT-851](../literature.d/LIT-851.md) uses it
([THEORY-177](../theory.d/THEORY-177.md)), is Δ = Σ_q |⟨R_q⟩ − ⟨R′_q⟩| = Σ_q 2|p_q − p′_q|. A
rank-2 system has two contents and Δ ≤ 4. The plug-in estimate is
Δ̂ = Σ_q 2|x/n − y/m|.

**1. No unbiased estimator exists, at any counts.** The expectation of
any statistic T(x, y) is Σ T(x, y) C(n,x)pˣ(1−p)ⁿ⁻ˣ C(m,y)p′ʸ(1−p′)ᵐ⁻ʸ, a
polynomial in (p, p′). If it equalled 2|p − p′| on the square, it would
equal 2(p − p′) on the open half p > p′, so, being a polynomial, it would
equal 2(p − p′) everywhere, which is negative where p < p′. For a whole
system, fix every other content's marginals equal across contexts (for
instance, independent of the first): the expectation is still a
polynomial in the first content's two probabilities, and Δ is that
content's term plus a constant. So bias correction can only reduce the
bias, never remove it, and an estimator that removes it at zero
signalling must pay for it elsewhere.

**2. The squared difference is estimable without bias.** With n, m ≥ 2,
U = x(x−1)/(n(n−1)) − 2xy/(nm) + y(y−1)/(m(m−1)) has expectation
(p − p′)² exactly, since x(x−1)/(n(n−1)) is unbiased for p². Its root,
Δ̃ = Σ_q 2√max(0, U_q), is a bias-reduced estimator of Δ. By exact
enumeration ([CASE-359](../cases.d/CASE-359.md)), for one content with p = p′ = 1/2 the
plug-in's mean is 0.75 at two occurrences a context, 0.35 at ten and
0.11 at a hundred, against the root's 0.25, 0.15 and 0.05; where the
true term is 1.0 the root falls short (0.64 at two occurrences, 0.90 at
ten) while the plug-in is nearly right. Neither dominates; which to
report is a choice, and the interval below makes it matter less.

**3. A stated sampling error that holds at every count.** Give each of
the 2k context marginals of a system with k contents a Clopper-Pearson
interval at level α/(2k). With probability at least 1 − α all hold at
once (Bonferroni, and Clopper-Pearson's exact coverage). On that event
each |p_q − p′_q| lies between max(0, L_q − U′_q, L′_q − U_q) and
max(U_q − L′_q, U′_q − L_q), so Δ lies between the sums of these bounds.
That interval covers Δ with probability at least 1 − α for any counts
and any joint distribution within the contexts, since Bonferroni needs
no independence between contents that share a context. It is
conservative: its exact per-content coverage was at least 0.999 in
every cell checked. The approximate alternative, Newcombe's
hybrid-score interval folded and summed, is narrower but not valid: its
coverage of Δ fell to about 0.93 at ten occurrences a context with no
signalling.

**4. A test with a stated null.** H₀: no content signals, p_q = p′_q
for every q. Fisher's exact test on each content's 2×2 table of value by
context, at α/k, rejecting H₀ if any content rejects, has size at most α
whatever the joint distributions. Boschloo's unconditional test can
replace Fisher's for more power at the same guarantee.

**5. A floor no test passes.** A nonrandomized level-α test of p = p′
can reject a table only if the table's probability is at most α at
every p on the null. The least such worst-case probability over all
tables is nⁿmᵐ/(n+m)ⁿ⁺ᵐ, attained by the table where every occurrence
takes one value in the first context and the other in the second
(checked for all n, m ≤ 40 in [CASE-359](../cases.d/CASE-359.md)). It is 1/4 at one occurrence
each and 1/16 at two each. So no valid 5% test can find a content
signalling from two or fewer occurrences in each context, or from one
occurrence in one context and fewer than seven in the other; at the
2.5% that Bonferroni gives each of two contents, two occurrences need
four on the other side. Whatever Δ̂ such a system shows, it is not
evidence of signalling.

## What it does not say

- That the plug-in estimate is useless. It is the maximum-likelihood
  estimate and nearly unbiased once a content's true signalling is
  large beside its standard error; the bias that matters is at small Δ,
  as [CLAIM-235](CLAIM-235.md) and [CLAIM-896](CLAIM-896.md) say.
- That the interval of item 3 is the best valid one. It is simple and
  guaranteed; an exact unconditional interval for each difference would
  be shorter.
- Anything about the contextual fraction or deficiency, the other two
  quantities [CLAIM-235](CLAIM-235.md) finds without estimators, or about the
  correlation term of the CbD criterion.
- That [LIT-851](../literature.d/LIT-851.md)'s systems do or do not signal. Its appendix gives no
  counts ([NOTE-654](../notes.d/NOTE-654.md)).

## What it bears on

[CLAIM-235](CLAIM-235.md) asks for "estimators with bias correction and a stated
sampling error, or a test for signalling with a stated null hypothesis,
applied to [LIT-851](../literature.d/LIT-851.md)'s systems with their occurrence counts". Items 2 to
4 supply the estimators, the error and the test; item 1 says why "bias
correction" cannot mean an unbiased estimate. The application is not
possible from the published paper, and [CASE-359](../cases.d/CASE-359.md) applies them
instead to the three binary systems that [LIT-842](../literature.d/LIT-842.md) prints as fractions.
Item 5 sharpens [CLAIM-235](CLAIM-235.md)'s worked case: with one occurrence a
context, a system's Δ̂ of 2 or 4 is not merely biased but could not be
told from no signalling by any valid test. [CLAIM-105](CLAIM-105.md)'s defeat condition
counts changes "beyond sampling error"; item 3 is a sampling error for
the signalling term that holds without assumptions on the counts.
