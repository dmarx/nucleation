---
number: 330
status: Proposed
formerly:
- CASE-tmpjw1l1
title: 'The Federal Open Market Committee''s policy-rate decisions, 1966–2026, read with the dual mandate''s inflation and employment channels as perspectives ranking cut, hold and hike from what was known at the time: the channels contest about a quarter of quarters, nearly all in stagflation; a channel''s lead is shown in one window only, on four contests, a compromise of holding prevails in two, ambivalence is shown only for Burns''s tenure and 1980–81 and only under some readings, and no persistence or resumption can be read'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant carrying out LEAD-041, whose record of
    conduct was left open. The record was chosen, the data fetched and the
    procedure (CLAIM-899) run in this session; scripts and small
    results are committed under scratch/studies/lead-041/, the downloads
    are not.
standing: documented
kind: executed-study
tags:
- society-and-governance
- emotion-and-affect
- self-governance
date: '2026-11-22'
line:
- organizational-affect
- distributed-agency
bears_on:
- QUESTION-268
illustrates:
- CLAIM-897
summary: >-
  [LEAD-041](../leads.d/LEAD-041.md) asked for the procedure of [QUESTION-268](../questions.d/QUESTION-268.md) to be applied to one
  record of conduct. The record chosen is the FOMC's: public, kept in time
  for sixty years, with two statutory channels that mirror the evaluative
  space model's two, whose rankings can be computed from real-time data
  apart from the decisions. 243 quarters; the channels contest in 43 to 72
  of them, by specification, 49 of the 59 under the main one in quarters
  with inflation and unemployment both above their references. Across 18
  specifications a channel is shown to prevail in one window only, a
  compromise of holding prevails in 1994–97 and 2014–17 under some, the
  Burns tenure (1970–78) and 1980–81 are ambivalent under one reading each,
  and no persistent potential, so no resumption, appears. The procedure
  separates no contest, indeterminacy, a prevailing compromise and
  ambivalence on this record; it returns neutrality once, on four
  contests. The binding limit is contests per window at the record's own
  noise. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-897 CLAIM-899 CLAIM-898 — new on 2026-11-22; the argument, the procedure and the alternative reading filed with this case for LEAD-041 -->

# CASE-330: The Federal Open Market Committee's policy-rate decisions, 1966–2026, read with the dual mandate's inflation and employment channels as perspectives ranking cut, hold and hike from what was known at the time: the channels contest about a quarter of quarters, nearly all in stagflation; a channel's lead is shown in one window only, on four contests, a compromise of holding prevails in two, ambivalence is shown only for Burns's tenure and 1980–81 and only under some readings, and no persistence or resumption can be read

## Why this record

[LEAD-041](../leads.d/LEAD-041.md) leaves the record open. Wells Fargo ([CASE-151](CASE-151.md)), [QUESTION-268](../questions.d/QUESTION-268.md)'s
example, is a narrative investigation; turning it into a record of
contests would mean coding decisions the report describes, with the
perspectives' rankings read off the same text as the decisions, which is
what [CLAIM-897](../claims.d/CLAIM-897.md) says a record must avoid. The FOMC's record was chosen
because:

- it is public and lawfully readable (US federal statistics, served by the
  Federal Reserve Board and the Federal Reserve Bank of Philadelphia);
- it is kept in time, quarter by quarter since 1966, with interruptions
  (the 1980 credit controls and reversal, two spells at the zero lower
  bound) and a received history to check against (the 1970s "stop–go",
  Volcker's disinflation);
- its two perspectives are named by statute, an inflation channel and an
  employment channel, the organizational twin of the evaluative space
  model's two ([CLAIM-897](../claims.d/CLAIM-897.md)), and each ranks the options from data
  available at the time, apart from the decision;
- its contests have a natural form: the two channels disagree exactly when
  inflation is above its reference and unemployment above its own, or
  both below, which is the model's coactivation.

## The record

- **Decisions.** Quarterly, from the monthly effective federal funds rate
  (H.15, series RIFSPFF_N.M): the change from the last month of one quarter
  to the last month of the next; hike above +0.25 points, cut below −0.25,
  hold otherwise. A second reading uses the change in the real rate (funds
  rate less 12-month CPI inflation as known then). Where the rate stood
  below 0.25 the option to cut is absent (context "zlb").
- **Rankings.** From the Philadelphia Fed's Real-Time Data Set, the
  vintage of each quarter: the inflation channel ranks hike over hold over
  cut when 12-month CPI inflation exceeds its reference by more than 0.5
  points, the reverse when below by as much, and is indifferent between;
  the employment channel likewise on unemployment against its reference.
  Three specifications: A, inflation against 2% and unemployment against
  its trailing ten-year mean; B, both against trailing ten-year means; C,
  inflation against 2% and the twelve-month change in unemployment.
- **Candidates.** The two channels' orderings and inertia, hold on top.
- **Windows.** Two-year blocks, four-year blocks, and chairs' tenures.

Choices, obstacles and how to rerun are in
scratch/studies/lead-041/README.md; all numbers below are in
scratch/studies/lead-041/results/summary.md.

## What it found

1. **Contest is rare and concentrated.** Under A, 59 of 243 quarters are
   contested (43 under C, 72 under B): 25 in the 1970s, 15 in the 1980s,
   13 in the 2010s. 49 of the 59 have inflation and unemployment both
   above their references, the rest both below (2015–16). Where the
   channels agree, as in 2022–23 with high inflation and low unemployment,
   nothing is contested and the procedure returns no verdict: the record's
   largest tightening in forty years says nothing about which channel
   prevails.
2. **A channel's lead is shown once.** In every specification, every
   window with four or more contests in which a channel leads is
   "indeterminate", the lead not surviving resampling, but one: the
   employment channel in Greenspan's tenure under A with real decisions,
   on four contests (finding 5). Leads observed
   are mostly the employment channel's in the 1970s and early 1980s under
   nominal decisions (alignment 0.52 to 0.79), and mixed under real ones.
3. **A compromise prevails twice.** Inertia, hold on top, prevails in
   2016–17 or 2014–17 (A, nominal) and in 1994–97 (B, nominal), with
   alignment 0.9 to 1.0. At the zero lower bound the employment channel
   and inertia are tied (cut is not available, and both rank hold above
   hike): a class the record cannot narrow, as [QUESTION-268](../questions.d/QUESTION-268.md)'s step 5 says
   only an intervention could.
4. **Ambivalence is shown twice, weakly.** The Burns tenure, under A with
   nominal decisions (25 contests; alignment 0.48 inflation, 0.52
   employment, 0.38 inertia; p = 0.043), and 1980–81 under C with nominal
   decisions, in two-year and four-year windows (alignment 0.50 and 0.50;
   p = 0.035 for the two-year window). Neither survives the real-rate
   reading or the other specifications. This is the received "stop–go" and
   the 1980 reversal, read as ambivalence, but at the edge of what the
   record can show.
5. **Neutrality once, thinly.** Greenspan's tenure under A with real
   decisions: the employment channel prevails on four contests and its gap
   closes at the reference rate. Four contests is the minimum the
   procedure admits.
6. **No persistence, so no resumption.** No channel prevails in two
   consecutive windows anywhere; there is no run to interrupt, and
   resumption, including the 1980 interruption of Volcker's tightening,
   cannot be read. Alternation of the leading candidate across windows
   exceeds chance in one of 18 runs (p = 0.046), which is what chance
   gives.
7. **The limit is contests per window.** On uncontested quarters, where
   the channels agree, the FOMC took the common first choice only 0.39 of
   the time (0.42 the compromise, 0.19 the opposite). At that noise the
   procedure needs about 16 contests in a window to show a lead of 0.75
   reliably, or to show strict alternation as ambivalence (power.py). Two
   years of quarterly decisions rarely hold eight.

## What it can show

That the procedure runs on a real organization's record and keeps apart
what [QUESTION-268](../questions.d/QUESTION-268.md) asks it to: no contest (most of the record), a
prevailing compromise (the middling output that is not ambivalence), and
ambivalence (alternation no candidate absorbs), and that it adds a state
the question did not name, contested but indeterminate, which is where
most of this record falls. That the dual mandate's channels meet
[CLAIM-897](../claims.d/CLAIM-897.md)'s three marks in an organization: they rank the options
apart, contest in stagflation, and are granted authority by a committee
that could follow either. And that the record's noise, not the procedure,
binds.

## What it cannot show

- Which channel governs the FOMC. The quarterly record has too few
  contests per window; meeting-level decisions and members' recorded
  dissents, which give each member's preferred direction, would multiply
  them. Not attempted.
- That the channels are the FOMC's perspectives rather than the
  assistant's reconstruction. The rankings are rules applied to data, not
  the committee's own; bands, references and the decision proxy are
  choices, varied but not exhausted. From 1979 to 1982 the Fed targeted
  reserves, so the funds rate's moves were less directly decisions.
- Anything about what the committee contested beyond the funds rate:
  balance-sheet policy and guidance at the zero lower bound are not in
  the record ([CLAIM-448](../claims.d/CLAIM-448.md): the verdict is about the admitted contests).
- Felt ambivalence, or anything about organisms. The evaluative space
  model's channels are argued to be perspectives in [CLAIM-897](../claims.d/CLAIM-897.md), and an
  alternative reading denies it ([CLAIM-898](../claims.d/CLAIM-898.md)); this case concerns an
  organization's.
- Dispositional potential. Every verdict is from conflicts actually
  decided.
