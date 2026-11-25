---
number: 393
status: Active
formerly:
- CASE-tmp4niuz

title: 'Coding the restatements the workbench reconstructions report finds them recorded almost only when they fail: 76 re-derived as new against one retrieved by its code, coded content re-derived in 20 of 48 reconstructions, and too few quoted pairs to measure a restatement''s distance from its original'

version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Proposed to Active at the status review's ruling (the owner delegated
    these rulings): restatement.py with rules v1 and v2, rerun on the
    current tree, gives results and events byte-identical to the committed
    files; tests pass. Its limits (one coder, no agreement measure) are
    stated, and its title claims only counts.

standing: documented

kind: executed-study

tags:
- epistemology
- design-rationale

date: '2026-11-23'

line:
- nucleating-argument

bears_on:
- QUESTION-038

summary: >-
  Run for [LEAD-107](../leads.d/LEAD-107.md). A rule-based coding of the 265 restatement events that
  48 reconstructions of exchanges report. Re-derived as new: 76. Retrieved
  by citation: 1. Coded content was re-derived in 20 reconstructions. Too
  few quotations pair a restatement with its original to measure distance.
  The reconstructions record restatements almost only when they fail, so
  they cannot give the coded-against-uncoded rate or the distance test.
  One coder, no agreement measure. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-180 CLAIM-182 CLAIM-191 — Proposed; the claims this study was run to test, cited as under test -->
<!-- inactive-ok-file: CASE-306 CASE-372 — Proposed; earlier studies of the same reconstructions, cited for comparison, nothing here rests on them -->
<!-- inactive-ok-file: CLAIM-1068 CLAIM-1023 — new; filed by the lead run of 2026-11-23 -->

# CASE-393: Coding the restatements the workbench reconstructions report finds them recorded almost only when they fail: 76 re-derived as new against one retrieved by its code, coded content re-derived in 20 of 48 reconstructions, and too few quoted pairs to measure a restatement's distance from its original

## What was done

[LEAD-107](../leads.d/LEAD-107.md) asks for three measurements in the record's reconstructed
exchanges. [CLAIM-180](../claims.d/CLAIM-180.md) and [CLAIM-182](../claims.d/CLAIM-182.md) name them. The first is a restatement's
distance from its original, set against whether it was re-derived as
though new. The second is a count of re-derivation of coded items against
uncoded ones. The third is re-derivation of the same content before and
after its parts got addresses.

The study codes every restatement event that the reconstructions report.
The rules are in a codebook, and a script applies them. Its tests pass.
Everything is in `scratch/studies/lead-107/`: `CODEBOOK.md`,
`restatement.py`, `test_restatement.py`, `results_v1.json`,
`results_v2.json` and `AUDIT.md`. The run is CPU only, needs no network
and takes about a second. The workbench entries were read, never edited.

The rules, in brief:

- **Corpus.** A workbench entry counts when its title begins "Session",
  "Exchange", "The exchange" or "Branch" and it carries at least ten turn
  labels or names a shared exchange. That gives 48 entries, covering
  exchanges from 2026-10-04 to 2026-11-06.
- **Unit.** A sentence that carries a restatement cue.
- **Outcome.** Cue words decide it.
  - *Re-derived as new*: "re-derived", "uncited", "without citing",
    "as new", "re-proposed", "reintroduced", or "already held" next to a
    turn or a proposal.
  - *Retrieved*: "cites", "with its code", "pointing back", unless
    negated.
  - *Conflict*: both kinds of cue.
  - *Neutral*: only a recurrence word ("restated", "came back", "again").
- **Items.** The codes the sentence names. An item counts as *coded at the
  time* when its entry's date is strictly before the exchange began.
- **Distance.** Computed only where the sentence quotes the restatement and
  names one code. It is a lexical distance between the quotation and the
  code's title: word-set Jaccard, character 4-gram cosine, or the share of
  the quotation's words found in the title.

The codebook was fixed before the comparisons were run (rules v1). Four
retrieval codes in the first run were false positives, such as "of the 133
codes cited", so four repairs followed (rules v2). Both runs are kept.
Figures below are v2, with v1 in brackets where they differ.

## Counts

| | v2 [v1] |
|---|---:|
| Restatement sentences | 265 [292] |
| Re-derived as new | 76 [85] |
| Retrieved by citation | 1 [5] |
| Conflicting cues | 2 |
| Neutral | 186 [200] |

The counts per (reconstruction, item) unit:

| Item | new | retrieved | conflict | neutral |
|---|---:|---:|---:|---:|
| Coded at the time | 159 | 1 | 6 | 137 |
| Not yet coded | 44 | 0 | 0 | 130 |

- Coded content was re-derived as new in 20 of the 48 reconstructions.
- 21 items were re-derived before they had a code. 12 of them had nine or
  more later reconstructions in which they could recur. Four are reported
  re-derived again after their code existed: [TERM-072](../terms.d/TERM-072.md), [CLAIM-414](../claims.d/CLAIM-414.md),
  [QUESTION-271](../questions.d/QUESTION-271.md) and [CASE-156](CASE-156.md). None is reported cited.
- 16 events quote the restatement and name one code. Three are re-derived
  as new and none is retrieved.

Counting a code filed on the exchange's own day as already held, or
dropping the two undated reconstructions, changes none of these patterns.

## What it shows

**The reconstructions are a log of failures.** They report restatements
almost only when the restatement failed. Of all the events, only one names
a coded item restated *with* its code: "[CLAIM-122](../claims.d/CLAIM-122.md) (re-derived again, this
time cited)" (workbench 2026/10/21/025602). Another, [CLAIM-287](../claims.d/CLAIM-287.md), was cited
where other entries held the point. The audit drew 60 events at random,
and none of them was a successful retrieval. So the reconstructions cannot
supply the denominators the lead asks for: how often a coded or uncoded
item recurred and *was* recognised. The coded-against-uncoded comparison
is degenerate, with P(new) at 0.99 against 1.0, and the distance test
cannot be run at all. The before-and-after count runs into the same wall.
When a reconstruction says nothing about an item, the item may have been
cited correctly or may never have come up.

**What the counts do show is that an address did not stop re-derivation
in the exchanges.** Content the record held under codes was re-derived
without them, in 159 units across 20 reconstructions. In at least some of
these exchanges the replies read and cited the record: workbench
2026/10/22/103820 counts 133 codes cited. [CLAIM-1068](../claims.d/CLAIM-1068.md) and
[CLAIM-1023](../claims.d/CLAIM-1023.md) file two readings of that finding. [CLAIM-1056](../claims.d/CLAIM-1056.md) files the
methodological finding.

## What it cannot show

- **One coder.** The lead worker (Claude) wrote the rules after reading
  grep hits and knew the hypothesis. The rules are mechanical and rerun
  identically, but they are not blind to direction except in one respect:
  the distance function never sees the outcome, and the outcome rules
  never see the distance.
- **The rules were checked only by their author.** That check (AUDIT.md)
  found 23 to 25 of 30 sampled "new" codes right. It found about 9 of 30
  "neutral" codes that a reader would call "new". It found no missed
  retrieval. This is not an agreement measure. A human second coder is a
  separate lead.
- **The reconstructions are summaries, not transcripts.** A reconstruction
  reports what its reader judged worth reporting, in that reader's words.
  Its quotations are sometimes of the original rather than the
  restatement.
- **No direction.** [CLAIM-191](../claims.d/CLAIM-191.md)'s defeater asks blind raters which way
  re-derivations drift. This study codes no direction. A reconstruction
  paraphrases a restatement in its own reader's words, so it could not
  support a direction coding.
- **Same owner, one assistant family.** As in [CASE-306](CASE-306.md) and [CASE-372](CASE-372.md), all
  the exchanges have one owner and one assistant family. The counts are
  exact properties of the record's files on 2026-11-23, not rates in
  exchanges.

## What would run the test

The test needs a verbatim transcript coded for every restatement,
successful or not, with each paired to its earlier statement. Such
transcripts are not in the record. [LEAD-079](../leads.d/LEAD-079.md)'s coding of one exchange
([CASE-306](CASE-306.md)) lists the re-derivations with quotations, but not the
restatements that were recognised, so it supplies the failures without
the denominator.
