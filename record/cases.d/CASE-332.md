---
number: 332
status: Active
formerly:
- CASE-tmpl0ccq
title: 'Maintained inquiry under lesioned operations'
statement: >-
  A simulation of the organization of the study of maintained inquiry under
  damage, with evidence generation, admission and scoring lesionable one at
  a time: a second correction after an undisclosed lesion of any one
  operation succeeds only where the apparatus tests itself and a producer
  rebuilds it, in 64 of 64 worlds for reciprocal and external maintenance
  and 0 of 64 without production, and in no arrangement without the
  self-test; only destroying both capacities separates reciprocal from
  external maintenance
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-048 as a delegated
    lead worker. The code, its tests and the results are committed under
    scratch/studies/lead-048/.
- version: 2
  date: '2026-11-25'
  note: >-
    Promoted to Active under the owner's delegation of 2026-11-24
    ("handle the fixes for the twelve ... use your best judgement"),
    as the status pass of 2026-11-24 and the reruns of 2026-11-25
    applied it to independently recomputed demonstrated claims and
    executed studies, in the recomputation pass of 2026-11-25
    (LEAD-tmpc0rqa). Rerun by a session other than the filer's from a
    copy of scratch/studies/lead-048/ with its results set aside: all
    1,836 cells in core1, core2, core3 and baselines are identical to
    the stored ones but for timings, results/tables.md is byte for
    byte the stored one, and the 7 tests pass; every count quoted in
    the body was compared and matches. An executed study, with no
    premise of its own; nothing targets it.
standing: documented
kind: executed-study
tags:
- self-governance
- epistemology
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-186
bears_on:
- QUESTION-086
- QUESTION-285
- QUESTION-271
- QUESTION-279
- QUESTION-016
illustrates:
- CLAIM-414
summary: >-
  [LEAD-048](../leads.d/LEAD-048.md) asked for [CASE-186](CASE-186.md) to be run. A reduced version was
  simulated (scratch/studies/lead-048/): a hidden regime + then −, then
  either + again or 0, outside the organization's family; partial
  monitoring; an audit whose generate, admit and score operations are
  lesioned one at a time without disclosure; diagnostic integrity A and
  evidence-governance integrity G (which also carries the copier from
  teacher to erased student) maintained reciprocally, by a paid outside
  service, or not at all; finite fuel; a self-test of each operation on
  known inputs; 1,836 cells of 64 matched worlds, natural and
  matched-first-stage branches. With protected admission and independent
  scoring, every arrangement corrects the first reversal (61 to 64 of 64).
  After an undisclosed lesion of one operation the second correction
  succeeds in 64 of 64 worlds for reciprocal and external maintenance and
  0 of 64 without production when the self-test runs, and in 0 of 64 for
  every arrangement when it does not; which operation is lesioned makes no
  difference. Partial loss of A or G separates production from none (64
  against 0); destroying both separates reciprocal (0) from external (64),
  [CASE-161](CASE-161.md)'s finding again. The capture arms repeat [CASE-162](CASE-162.md). Much of
  this follows from the rules the model states; what the run adds is that
  they compose as stated. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-265 CLAIM-901 — Proposed or new; CASE-265 cited for its constant outside controller, CLAIM-901 as the claim filed from this run -->

# CASE-332: Maintained inquiry under lesioned operations

## What was done

[LEAD-048](../leads.d/LEAD-048.md) asks for [CASE-186](CASE-186.md) to be run: an organization corrects once after
a regime reversal, its diagnostic and copying machinery is injured, and a
second challenge follows, in-family or out of the hypothesis family, with
evidence generation, admission and scoring lesioned one at a time. The
model is `scratch/studies/lead-048/model.py`, documented in its docstring;
`README.md` there says how to rerun it, `results/tables.md` holds every
table, and `results/*.jsonl` one line per cell. It is written to be reused
by [LEAD-140](../leads.d/LEAD-140.md): `Config`, `Org` and `run` import, and a mechanism changes by
subclassing `Org`.

**The world** is [CASE-186](CASE-186.md)'s: P(Y=1 | a=1) is 0.75, 0.25 and 0.5 in +, − and
0. It is + until step 100 and − from 100; at step 400 it becomes + again
(in-family) or 0 (out of family). Monitoring is partial: only audits
inform. Audit draws are fixed per world and step, so arms sharing a seed
see the same stream draw for draw.

**The apparatus.** Every 10 steps an audit runs:
- **generate** draws 256·A samples;
- **admit** is protected or selective (0.9 agreeing, 0.1 contradicting);
- **score** is independent (mean > ½ for +; 0.42 < mean < 0.58 flags the
  family, and the neutral response follows), captured (the mean shifted
  0.4 toward the current interpretation), or inverse-propensity weighted,
  the selection-aware baseline.

Protection of admission is maintained work: below G = 0.4 it lapses to
selective. The undisclosed lesions are:
- of generate, a stale replay of the last batch;
- of admit, 0.95 agreeing and 0.05 contradicting;
- of score, a further shift of 0.45 toward the interpretation.

Every 20 steps, with probability A, a self-test runs each operation on
known inputs against its commissioning values. A flagged apparatus's
output is not acted on, and a flagged operation is rebuilt after 30 steps
if the arrangement's producer can rebuild it.

**Maintenance** of A and G, against a wear of 0.001 a step:
- reciprocal: dA = 0.05·G·(1 − A), dG = 0.05·A·(1 − G);
- external: an outside service restores each at 0.05·(1 − x), paid from
  the same fuel at the same price;
- none: nothing regenerates.

Fuel is replenished at ρ, and operation, production, copying and diagnosis
draw on it in that order. A teacher holds the interpretation; the acting
student is erased every 50 steps and rebuilt through a copier that
succeeds with probability G.

**The injury**, at step 300, is one of:
- a sham;
- a lesion of generate, admit or score;
- A or G cut to a quarter;
- the producer stopped for 300 steps;
- the internal producer destroyed;
- both A and G set to zero.

**Endpoints.**
- S1: by step 249, the teacher and student hold − and the apparatus is
  viable (A ≥ 0.3, G ≥ 0.4).
- S2, judged at step 699: the new regime was detected, the teacher and
  student hold it, no fuel shortfall occurred after step 400, and the
  apparatus is viable with no unrepaired lesion.

A matched branch starts every arm at step 300 from the same corrected
state: belief −, A = G = 1, full fuel, nothing broken.

**Cells run.** With 64 worlds per cell, 1,836 cells were run, about 10 minutes
of CPU on three processes:
- the reference apparatus (protected, independent) in every combination;
- the other five admission × scoring arms under ample fuel;
- the reference apparatus under tight fuel;
- a no-audit baseline.

## Results

**The reference apparatus, self-test on, ample fuel** (natural branch S1 ∧ S2,
and matched-branch S2, of 64; in-family / out-of-family):

| injury | reciprocal | external | none |
|---|---|---|---|
| sham | 64/64; 64/64 | 64/64; 64/64 | 63/53; 64/63 |
| generate, admit or score | 64/64; 64/64 | 64/64; 64/64 | 0/0; 0/0 |
| A or G to a quarter | 64/64; 64/64 | 64/64; 64/64 | 0/0; 0/0 |
| producer stopped 300 steps | 64/64; 64/63 | 64/64; 64/64 | 63/56; 64/60 |
| internal producer destroyed | 64/63; 64/63 | 64/64; 64/64 | 64/57; 64/61 |
| A and G zeroed | 0/0; 0/0 | 64/64; 64/64 | 0/0; 0/0 |

The unmaintained arrangement has no producer to stop or destroy, so its
last two rows differ from its sham only by the draws of admission and
copying.

S1 was 61 to 64 of 64 in every reference cell, so P(S2 | S1) equals
P(S1 ∧ S2) to within three worlds, and the matched branch agrees with the
natural one. Selection at the first stage does not arise here.

**Without the self-test**, the three component lesions give 0 of 64 in
every arrangement and both branches. The other injuries are unchanged.

**Which operation was lesioned made no difference.** Generate, admit and
score gave the same counts in every arrangement. The self-test flagged
each lesion at its first run, in 64 of 64 worlds and before the apparatus
acted on its output. The run cannot report a detection delay, because the
injury fell on a self-test step. The one exception is a lesion of admit
in the selective arms: it moves the contradicting rate from 0.1 to 0.05,
which the test at 64 tokens does not detect, and those arms fail anyway.

**Capture** (sham, self-test on, ample fuel; reciprocal and external alike, and the unmaintained arrangement the same except out of family):

| admission | scoring | S1 | S1 ∧ S2, in / out | matched S2, in / out |
|---|---|---|---|---|
| protected | independent | 64 | 64 / 64 | 64 / 64 |
| protected | captured | 6 | 0 / 0 | 11 / 0 |
| protected | inverse-propensity | 64 | 64 / 64 | 64 / 64 |
| selective | independent | 0–1 | 0 / 0 | 0–1 / 0 |
| selective | captured | 0 | 0 / 0 | 0 / 0 |
| selective | inverse-propensity | 63–64 | 63–64 / 63–64 | 62–64 / 63–64 |

**Out of family.** The adequacy test, which the architecture supplies,
catches regime 0 as often as the in-family reversal wherever the apparatus
is maintained. Without production, out-of-family detection falls to 53–57
of 64, against 63–64 in-family: as A wears, the audit draws fewer samples
and the band test becomes noisier.

**Fuel.** At ρ = 0.6 and 0.36 no run ever ran short. Ordinary spending is
about 0.36 a step, and the starting stock covers the rest. At ρ = 0.25, in
the natural branch, the reciprocal and external arrangements ran short in
64 of 64 worlds. They still corrected and stayed viable, but failed S2's
budget condition, while the unmaintained arrangement passed the sham. It
pays for no production, and its audits shrink as A wears. In the matched
branch, which restores the fuel, all passed.

**No audit.** The habit baseline never corrected: S1 and S2 were 0 of 64.

## What it shows, and what it does not

[CASE-186](CASE-186.md)'s readings, taken in turn:

- **"The first correction succeeds and the second fails, in the
  matched-first-stage branch."** Found for the unmaintained arrangement
  after any lesion of an operation or a capacity. Found for reciprocal
  maintenance after the double lesion, which leaves the reciprocal law at
  its fixed point at zero, as in [CASE-161](CASE-161.md).
- **"Internal and external restoration are alike normally but diverge
  after producer-specific lesions."** Found only for the double lesion.
  Interrupting the producer did nothing at this wear rate. Destroying the
  internal producer had not yet cost the reciprocal arrangement a
  correction by step 699, with A at 0.66; a longer horizon would. The
  double lesion is an intervention on state. It separates the two because
  the outside service here restores at a constant rate and does not supply
  the internal law as state feedback, which is [CASE-265](CASE-265.md)'s case, not
  [CLAIM-522](../claims.d/CLAIM-522.md)'s ideal one. Nothing here bears against [CLAIM-522](../claims.d/CLAIM-522.md).
- **"Protecting admission fixes capture and maintenance does not matter."**
  True under the sham. False under injury, where maintenance decides the
  second correction.
- **"Familiar reversals are caught and out-of-family change is missed."**
  Not found where the apparatus is maintained, because the adequacy test is
  built in. The run does not test the spontaneous recognition of an
  inadequate family.
- **[LEAD-048](../leads.d/LEAD-048.md)'s test**, "a second correction that fails when one component is
  lesioned and survives the others". Not found. Every component lesion is
  fatal without the self-test and survivable with it wherever a producer
  rebuilds. What the lesions separate is the capacity to diagnose and
  rebuild, not the operation lesioned. Correction did not survive every
  lesion in any arrangement but the external one, and no lesion here
  removed the outside service for good. That is the outer-boundary twin of
  the internal-producer lesion, and it was not run.

Most of this follows from rules the model states. The self-test detects a
changed operation; repair needs a producer; protection lapses with G. What
the run adds is that these rules compose as stated across the arms,
counted on matched worlds. It is a construction checked by computation,
not evidence about any real organization. It illustrates [CLAIM-414](../claims.d/CLAIM-414.md): under
the sham every maintained arrangement corrects alike, and the injuries
expose differences that the matched ordinary trajectories conceal.

**Not run:**
- the router baseline and the full-feedback condition;
- the non-reference arms under lean or tight fuel;
- a permanent loss of the outside service;
- a longer horizon after the internal-producer lesion;
- self-test schedules that do not coincide with the injury.

[LEAD-140](../leads.d/LEAD-140.md) can run these on the same code.

The claim drawn from the run is [CLAIM-901](../claims.d/CLAIM-901.md).

## Note of 2026-11-25: rerun by a session other than the filer's

Rerun on 2026-11-25 by the assistant, a session other than the filer's, in the recomputation pass of [LEAD-tmpc0rqa](../leads.d/LEAD-tmpc0rqa.md), at the owner's go-ahead of 2026-11-25 ("go ahead with the reruns"). From a copy of `scratch/studies/lead-048/` in the session's scratch space, with `results/` set aside and every part regenerated as the README directs (`study.py core1`, `core2`, `core3`, `baselines`, then `analyze.py`). The 7 tests in `test_model.py` pass. All 1,836 cells (432, 1,080, 216 and 108) agree with the stored `results/*.jsonl` in every field but the timings, and `results/tables.md` is the stored one byte for byte. Every figure above was compared and matches: the reference table row by row (sham 63/53 and 64/63 without production; the component and partial lesions 64 against 0; the producer stopped 64/64 and 64/63 reciprocal, 63/56 and 64/60 unmaintained; the internal producer destroyed 64/63 and 64/63, and 64/57 and 64/61; the double lesion 0 reciprocal, 64 external), 0 of 64 for the component lesions without the self-test, out-of-family detection 53 to 57 of 64 without production, and the tight-fuel shortfall of the maintained arrangements in all 64 worlds of the natural branch. Nothing failed to reproduce. Promoted in the same pass (history, version 2). The note is the assistant's (Claude, in this session).
