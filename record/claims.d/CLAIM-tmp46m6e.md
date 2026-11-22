---
status: Proposed
title: 'Read at the grain of features, the toy study narrows the alignment test of mechanism to where a same-mechanism control connects and the probe separates the candidate mechanisms, rather than defeating it'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-157, as one of two
    alternative readings of CASE-tmphfmrb for the owner to choose between;
    the other is CLAIM-tmpv22hv.
role: thesis
warrant: interpretive
defeated_if: >-
  At a width where same-mechanism control pairs are connected after
  alignment, pairs whose features do not correspond after alignment (low
  matched-unit correlation) are found connected on a probe set that
  separates their mechanisms, such as inputs on which the candidate cues
  disagree; or pairs whose features correspond closely stay separated by
  a barrier that an exact search over the full group cannot remove.
tags:
- loss-landscapes
- representation-learning
date: '2026-11-22'
line:
- learned-structure
rests_on:
- CLAIM-tmpr7v4j
bears_on:
- QUESTION-069
summary: >-
  The other reading of [CASE-tmphfmrb](../cases.d/CASE-tmphfmrb.md), an alternative to [CLAIM-tmpv22hv](CLAIM-tmpv22hv.md).
  [CLAIM-263](CLAIM-263.md)'s defeater lists "the same features up to alignment" beside
  "the same input attributes relied on". Read at the grain of features,
  the toy does not defeat the protocol; it adds two preconditions. First,
  the test runs only at a capacity where a same-mechanism control pair
  connects after alignment. At width 5 none reliably does. There the
  barrier tracks how well matched units correlate (0 at 0.92 and 0.66,
  0.25 at 0.48 and 0.03), which is step 4's "features with no counterpart"
  ([THEORY-113](../theory.d/THEORY-113.md)), not a difference of cue. Second, the probe must separate
  the mechanisms. The wide A-net and B-net were compared only on inputs
  where both cues agree, so their connection there is [CLAIM-142](CLAIM-142.md)'s caution,
  not a counterexample. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmphfmrb CLAIM-tmpr7v4j CLAIM-tmpv22hv — new; the study, the finding this rests on, and the alternative reading -->
<!-- inactive-ok-file: CLAIM-263 CLAIM-142 — Proposed; the claim this narrows and the probe caution it invokes, open -->

# CLAIM-tmp46m6e: Read at the grain of features, the toy study narrows the alignment test of mechanism to where a same-mechanism control connects and the probe separates the candidate mechanisms, rather than defeating it

## The claim

[CLAIM-tmpr7v4j](CLAIM-tmpr7v4j.md) states what [CASE-tmphfmrb](../cases.d/CASE-tmphfmrb.md) measured. [CLAIM-263](CLAIM-263.md)'s protocol
survives it if "share a mechanism" is read
at the grain of features, the second test its defeater names. But it
needs two preconditions that its text does not state:

1. **A connected control at the same capacity.** Read a surviving barrier
   as a difference only where two networks known to share the mechanism,
   at the same width and regime, connect after alignment. In the toy,
   that holds from width 64. Below it, same-cue pairs keep barriers.
   Their size follows the matched units' activation correlation, as
   step 4's "features with no counterpart" ([THEORY-113](../theory.d/THEORY-113.md)) would predict, so
   at narrow width the test "cannot run", which is not the same as "no".
2. **A probe that separates the candidate mechanisms.** The wide A-net and
   B-net were connected on inputs where both cues agree, and there a
   mixture of the two mechanisms does as well as either. [CLAIM-142](CLAIM-142.md) warns
   that what the probes cannot see they cannot separate. The comparison
   that would test the protocol uses inputs on which the cues disagree.
   That probe was not run, and it is the first thing a rerun should add.

On this reading the toy supports step 1 (the full group: the rescaled twin
is separated by permutations and joined once rescaling is quotiented). It
leaves step 2 untested rather than defeated, and it gives step 4 a
measurable form: matched-unit correlation below a control's.

## What it does not say

- It does not say the protocol has been confirmed. No pair here is
  separated by a barrier that a connected control at the same width
  lacks.
- It does not decide between this reading and [CLAIM-tmpv22hv](CLAIM-tmpv22hv.md). That is the
  owner's choice.
