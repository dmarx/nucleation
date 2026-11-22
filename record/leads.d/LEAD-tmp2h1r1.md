---
status: Open
title: 'Judge retention and drift by triangulating three probe families, a mechanical retention measure, blind model raters and the owner on a subsample, and count a finding only where they agree'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, triaging the manuscript's leads at
    the owner's "triage leads relevant to the manuscript that you could
    feasibly handle on your own and get started". One of two alternative
    protocols for the judgement LEAD-201 and LEAD-204 leave open; the other
    is LEAD-tmpxq8z2. Which to adopt is ARG-028's open dispute and the owner's call.
stage: specified
priority: medium
method:
- empirical
- operationalization
tags:
- design-rationale
- epistemology
date: '2026-11-22'
line:
- nucleating-argument
- record-as-apparatus
advances:
- CLAIM-768
- CLAIM-778
- CLAIM-772
- CLAIM-191
- CLAIM-776
summary: >-
  Alternative (b) of two for the judgement LEAD-201 and LEAD-204 leave
  open: it takes CLAIM-206's side of ARG-028, that human judgement is one
  probe family among others, and so asks several families for the same
  judgement and believes only their agreement. (1) A mechanical retention
  measure fixed in advance: the share of the originating turn's content
  words and of its quoted phrases recovered in each version, against a
  shuffled-turn baseline. (2) Model raters given only the turn and the
  version, blind to the hypothesis and to which version is which, scoring
  the same content units as alternative (a)'s rubric. (3) The owner, on a
  random subsample. A claim of retention or of drift is counted only where
  all three agree; disagreement is reported as a finding about the probes.
  The assistant can run (1) alone, and (2) with the caveat that a Claude
  rater shares the record's conventions (CLAIM-266). The other alternative
  is LEAD-tmpxq8z2. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: ARG-028 CLAIM-206 CLAIM-217 — Proposed, Rejected, Deferred or new; the entries this filing made or touched -->

# LEAD-tmp2h1r1: Judge retention and drift by triangulating three probe families, a mechanical retention measure, blind model raters and the owner on a subsample, and count a finding only where they agree

**One of two alternatives.** LEAD-201 and LEAD-204 stop at the same place: who judges, and on what scale, against a reference the record did not supply. ARG-028 leaves that open between CLAIM-217 (raters are the criterion) and CLAIM-206 (human judgements are one probe family among others). This lead takes the second side; LEAD-tmpxq8z2 takes the first. The owner chooses.

## Design

**Material.** As in LEAD-tmpxq8z2.

**Three probe families, each fixed before any data are seen.**

1. **Mechanical.** For each turn–version pair: recall of the turn's content words (stopwords removed, lemmatized) and of its quoted phrases of three or more words, in the version. Baseline: the same measure against a turn from a different claim, shuffled, to give chance retention. A version retains the turn if its recall exceeds the 95th percentile of the shuffled baseline. This family is computed in no grammar of the record's, but it is blind to paraphrase and rewards verbatim quotation, which the record's owner-voice claims do by rule; it is reported with that bias stated.
2. **Model raters.** Given only the turn and one version, in random order, and LEAD-tmpxq8z2's rubric (content units kept, altered, absent; conventionality on the anchored scale), scored by at least two models. A Claude rater shares the conventions under test (CLAIM-266), so its scores count only if a model of another family agrees.
3. **The owner**, on a random subsample of 20 pairs, scoring the same rubric blind to the other families' scores.

**Reading.** A pair counts as retained, or as drifted, only where all three families agree. Where they disagree, which family dissents and in which direction is reported as a finding about the probes, the question ARG-028 asks.

## What the assistant can do alone

Family 1 in full, and family 2 with Claude raters only, marked as not counting until a rater of another family is available. A pilot of family 1 on the owner-voice claims filed since 2026-11-20 would show whether the measure separates the first and current versions at all.

## What would count against it

Families that never agree beyond chance on the pilot: then the judgement is not one any probe family shares, and LEAD-201's distinction cannot be drawn this way.

## Pilot of family 1, 2026-11-22

Run by the assistant the day the lead was filed (script and output kept in the session scratchpad, `lead201pilot/pilot.py` and `results.txt`, not in the repository). Material: entries filed from the exchange "Rich Get Richer Power Laws" whose text names an owner's turn ("the owner's, at U<n>" and variants), 28 entries against 27 owner turns of the verbatim transcript; for each, recall of the turn's content words (stopwords removed, words of three or more letters) in the entry's first git version and its current one, with and without text inside double quotes; baseline, the same recall against 20 shuffled turns per entry.

- **Baseline.** Recall of a shuffled turn in an entry's unquoted text: median 0.000, 95th percentile 0.333.
- **First against current.** Unquoted recall moved by +0.045 on average from first to current version, upward, because dated notes add text; no entry fell.
- **What it measured.** On this material the measure registers quotation, not retention: the owner's turns are short (often under ten content words, so recall jumps between 0 and 1), owner-voice entries quote the turn by rule, and the entries are days old with no substantive rewording to detect. The matcher also picked up entries that only mention an owner's turn (the other assistant's claims about it), which are not owner-voice entries.

So the pilot does not meet this lead's "what would count against it" (it tests no agreement between families), but it shows family 1 cannot carry the judgement as specified. Before family 1 is run in earnest it needs: the population of LEAD-199 (entries with substantive revisions over a longer history), selection by a voice marker rather than by text match, and scoring by content unit (the rubric families 2 and 3 use) rather than by word set.

