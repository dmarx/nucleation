---
status: Proposed
title: 'A record of conduct returns, for each window, one of six verdicts, no contest, too few contests, indeterminate, prevails, split by context or ambivalent, and across windows persistence, resumption and alternation, when contest is read from the perspectives'' rankings measured apart from the decisions, alignment is scored for each candidate ordering including a compromise, ambivalence is a misfit to every candidate larger than the record''s own departures on uncontested decisions would produce, and prevalence is a lead over every rival that survives resampling; it measures actual potential, the conflicts won, not dispositional potential'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant carrying out LEAD-041. It specifies
    QUESTION-268's seven-step procedure as code
    (scratch/studies/lead-041/procedure.py) with twelve synthetic cases,
    and adds what applying it to a real record required. Its thresholds
    and nulls are the assistant's choices, listed in the study's README.
role: thesis
warrant: interpretive
defeated_if: >-
  A record, with perspectives' rankings measured apart from the decisions,
  on which the procedure calls a window ambivalent while an independent
  mark (arousal, conflict behaviour, a reported shift of the governing
  view) shows one ordering governing throughout, or calls it prevailing or
  no contest while such marks show the alternation; or a demonstration
  that the verdicts depend on the choice of null in a way no record could
  constrain, so that ambivalence and indeterminacy cannot be told apart in
  principle rather than for want of contests.
tags:
- emotion-and-affect
- psychometrics
- self-governance
date: '2026-11-22'
line:
- organizational-affect
- formal-apparatus
answers:
- QUESTION-268
rests_on:
- CLAIM-434
- CLAIM-440
complements:
- CLAIM-tmp0uism
- CLAIM-451
grounds:
- CASE-tmpjw1l1
- LIT-1438
uses:
- TERM-077
- TERM-078
- TERM-076
summary: >-
  QUESTION-268 asks for a procedure that, applied to a record of conduct,
  returns which ranking prevails and how strongly, separates ambivalence
  from neutrality on a case, and says whether it measures actual or
  dispositional potential. Its body drafts seven steps. This claim
  specifies them as code with tests and adds five things a real record
  needed: contest is read from rankings, never from choices; a compromise
  (inertia) is scored as a candidate, so a middling output that prevails is
  not taken for ambivalence; ambivalence needs a misfit to every candidate
  beyond the record's own noise; a lead must survive resampling, and
  otherwise the verdict is indeterminate, a state the question did
  not name; and how many contests a window needs is computed from that
  noise (about 16 to 24 at the FOMC's). Applied in CASE-tmpjw1l1. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-440 TERM-076 CLAIM-451 THEORY-252 — Proposed; the claim and term whose measure this specifies, the narrowing it keeps and the dilemma it answers for this measure, cited as open -->
<!-- inactive-ok-file: CLAIM-tmp0uism CASE-tmpjw1l1 — new on 2026-11-22; the argument and the application filed with this claim for LEAD-041 -->

# CLAIM-tmpkcsp7: A record of conduct returns, for each window, one of six verdicts, no contest, too few contests, indeterminate, prevails, split by context or ambivalent, and across windows persistence, resumption and alternation, when contest is read from the perspectives' rankings measured apart from the decisions, alignment is scored for each candidate ordering including a compromise, ambivalence is a misfit to every candidate larger than the record's own departures on uncontested decisions would produce, and prevalence is a lead over every rival that survives resampling; it measures actual potential, the conflicts won, not dispositional potential

## The procedure

Input: episodes in time, each with the options then available, each
perspective's ranking of them (measured apart from the decision), the
decision, and a context label; and candidate orderings, each a class
(every perspective's, and a compromise class such as "hold on top").
The code is scratch/studies/lead-041/procedure.py.

1. **Contest from rankings.** A pair is contested in an episode when two
   perspectives rank it strictly and oppositely. A perspective indifferent
   between the two contests nothing. A decision decides only the contested
   pairs that contain the option chosen (QUESTION-268, step 1; CLAIM-434,
   part 5: never net).
2. **No contest is its own verdict.** A window with no contested episode
   returns "no contest"; one with fewer than a stated minimum (four here)
   returns "too few contests". Neither is neutrality (CLAIM-440,
   consequence 1).
3. **Fit.** The least reversal fraction of the window's wins and the class
   of best-fitting orderings, by brute force over the options (TERM-077).
4. **Alignment per candidate.** For each candidate, the share of the wins
   its best member agrees with (QUESTION-268, step 4). The leading
   candidate is the one with the highest share.
5. **Ambivalence.** The null is that some candidate prevails with the
   record's own noise: on episodes where nothing is contested and the
   perspectives that rank strictly agree, the share of decisions that took
   the common ranking's first, second and third option. For each
   candidate ordering, decisions are simulated on the window's contested
   episodes from that profile, and the misfit to the best candidate,
   1 − its alignment, is compared with the observed. The window is
   "ambivalent" when the largest p-value over the candidates is below
   0.05: no candidate, at the record's noise, would leave so much
   unaccounted for.
6. **Split.** If the best classes of two contexts in the window share no
   ordering, "split by context" (QUESTION-268, step 6: a change in the
   options available is not ambivalence).
7. **Prevalence.** Otherwise the leading candidate "prevails" if its
   alignment exceeds every rival's in 95% of bootstrap resamples of the
   window's contested episodes; if not, "indeterminate". Strength is the
   alignment.
8. **Sign, for a prevailing perspective.** The rate at which the gap it
   governs closes, against a reference course (here, its mean rate over
   the windows it leads): "neutral" within a tolerance, else positive or
   negative. Only here is neutrality returned.
9. **Across windows.** Persistence is a run of windows the same candidate
   prevails in; resumption, a run of at least two, then other verdicts,
   then a return, read off the record, not inferred (TERM-078).
   Alternation of the leading candidate is tested against permutations of
   decisions among episodes of identical contest structure.

On synthetic records (test_procedure.py) it returns each verdict where it
should: no contest for both perspectives indifferent; prevails for one
ordering with noise; ambivalent for hike and cut alternating under
contest; prevails, with inertia leading, for holds under contest; split
for a context change; indeterminate for a mixed record; and it detects
regime change (fewer switches than chance) and stop–go (more).

## Actual, not dispositional

Every quantity is computed from conflicts actually decided in a window.
A perspective that would win contests never posed contributes nothing.
So the procedure measures actual potential, and the counterfactual eraser
(THEORY-252) does not apply to what it returns, which is QUESTION-268's
second half answered for this measure. Whether actual and dispositional
potential agree is not answered: that needs interventions that pose the
contests (step 5 of QUESTION-268), which a record of conduct alone does
not supply.

## What a window needs

At the FOMC's noise (on uncontested quarters, 0.39 of decisions took the
common first choice, 0.42 the second, 0.19 the third), power.py finds a
lead of 0.75 shown in about 60% of windows with 8 contests and in over 80%
with 16; and strict alternation shown as ambivalence reliably from 16
contests, unreliably below. A record with fewer contests per window
returns "indeterminate" whatever governs it. This is the procedure's
main practical limit and is a property of the record's noise, not of the
procedure.

## What it does not say

- That its thresholds (band, minimum contests, α, windows) are the right
  ones. They are choices, stated in the README, and the application varies
  the ones it can.
- That a prevailing ordering is the organization's. CLAIM-448 applies: the
  verdict is about the admitted contests.
- That alternation is all ambivalence (CLAIM-451).
- That the Hodge decomposition is used. It is not; margins here are not
  intensities (QUESTION-268, step 7).
