---
number: 372
status: Proposed
formerly:
- CASE-tmpkge6r

title: 'Census of filing dispositions in the workbench'
statement: >-
  A census of filing dispositions in the workbench reconstructions:
  owner-attributed moves filed at a higher rate than the assistant's and
  notes far above fresh claims and terms, over the entries that label their
  moves, with kind confounding contributor and no content-matched pairs
version: 1

standing: documented

kind: executed-study

tags:
- epistemology
- design-rationale

date: '2026-11-22'

line:
- record-as-apparatus

bears_on:
- QUESTION-072
---
<!-- inactive-ok-file: CLAIM-181 CLAIM-182 — Proposed; the claims QUESTION-072 builds on, cited as the question frames them, nothing here rests on their being settled -->

# CASE-372: Census of filing dispositions in the workbench

## The case

Run for [LEAD-122](../leads.d/LEAD-122.md), which advances [QUESTION-072](../questions.d/QUESTION-072.md): in
this record's workbench reconstructions, for moves of comparable content,
the share filed by contributor and by kind of move. The script, its test,
the machine-readable result and a README are at
`scratch/studies/lead-122/` (`python3 -I census.py`, CPU only, no network;
the numbers are exact properties of the record's own files on 2026-11-22).

**What a move is, operationally.** The reconstructions are free prose, but
about a third of them account for their moves with a small set of the
record's own **bold labels**. The census takes each such label span as one
move:

- A span under `**Filed:**` is **filed**; under `**Missed:**`,
  `**Also missed:**`, `**Not filed:**`, `**Struck:**` or
  `**Held, not filed:**` it is **not-filed**. `**Corrected:**` is reported
  apart (it edits a held entry, not a propose-or-file decision). Labels that
  are not filing decisions -- `Right`, `Wrong`, `Already held`, `On file`,
  `Checked`, `Registered` -- are excluded from the shares.
- **Contributor** is read from attribution tokens: owner (an owner turn
  `U\d+`, or "owner"), assistant (an assistant turn `A\d+`, or "the
  assistant"), the reconstruction's own readers, both when owner and
  assistant tokens co-occur, else unattributed. Two attribution windows are
  reported -- the enclosing block and the span alone -- to show sensitivity.
- **Kind** is the scheme the move names: claim, question, term, case, note
  (a span saying "note(s) on ..."), work (a registered LIT), theory.

These choices are the assistant's; the owner may read "move" otherwise. One
alternative cut -- counting each distinct scheme code named, rather than each
span -- is reported alongside as `code_mentions_by_scheme`.

**The count.** 135 workbench files. 47 carry disposition labels; 88 are free
prose and are not captured. 698 label spans; 454 are filed-or-not-filed (209
filed, 245 not), 237 other, 7 corrected.

Share filed by contributor (block context / span-only):

| contributor | filed / total (block) | share | span-only |
|---|---|---|---|
| owner | 19 / 27 | 0.70 | 0.67 |
| assistant | 21 / 37 | 0.57 | 0.41 |
| both | 146 / 355 | 0.41 | 0.38 |
| unattributed | 22 / 34 | 0.65 | 0.55 |

Share filed by kind of move: note 0.79, case 0.59, question 0.55, claim
0.44, term 0.39, work 0.26, theory 0.00.

**What moved.** Owner-attributed moves are filed at a higher rate than
assistant-attributed ones, and the direction holds under both attribution
windows. A note added to a held entry is far likelier to survive than a
freshly proposed claim or term; readings (THEORY) are essentially never
filed as a workbench move, which is expected -- they enter through
read-and-file, not the workbench.

## What it can show

The standing is documented: the shares are an exact recount of the labelled
spans, reproducible from the script. What the count is evidence *for* is
narrower than [QUESTION-072](../questions.d/QUESTION-072.md) part 1 asks.

- It shows the asymmetry the question names is **visible** in the record's
  own accounting: the owner's moves and the assistant's moves are not filed
  at the same rate, and the kinds a contributor characteristically makes
  are filed at very different rates. That is the descriptive half of
  [CLAIM-182](../claims.d/CLAIM-182.md)'s addressability claim and [CLAIM-181](../claims.d/CLAIM-181.md)'s grammar claim made
  countable.
- It **cannot** settle part 1's counterfactual -- whether, content held
  fixed, who made a move changes its chance of being filed. The data has no
  content-matched pairs, so the script cannot hold content fixed. And kind
  confounds contributor: the owner characteristically makes high-file-rate
  kinds (prompts, theses, corrections, notes) and the assistant makes many
  candidate claims and terms of which fewer survive, so the raw owner >
  assistant gap may be composition, not credibility.
- Coverage is partial (47 of 135 entries) and the owner-only and
  assistant-only cells are thin, because most filed spans are co-attributed.
  A finer study would segment reconstructions into single-contributor moves
  and match them by content before comparing -- the matched-pair design the
  question's "comparable content" actually calls for, which this census
  establishes is not extractable from the prose by string rules alone.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
