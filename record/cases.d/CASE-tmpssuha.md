---
status: Proposed
title: 'A pilot of the curation-completeness study on four replayed single-work readings: a replay from the source and the record as it stood recovers about two-thirds of what each filing held and none of what later corrections added'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out a pilot of LEAD-014
    at the lead's brief ("Do a pilot, not the full study"). The selection
    rule, codebook, accountings and scores are committed beside it under
    scratch/studies/lead-014/.
standing: documented
kind: executed-study
tags:
- epistemology
- design-rationale
date: '2026-11-22'
line:
- records-of-inquiry
- record-as-apparatus
variant_of:
- CASE-251
bears_on:
- QUESTION-108
summary: >-
  A pilot of CASE-251's design, for LEAD-014. Four past readings of
  arXiv works that a later commit corrected were chosen by a rule written
  first: the parameter-space symmetry survey (LIT-970), Mehta and
  Schwab (LIT-882), Wang et al. on ambiguous phrases (LIT-842) and
  Lubana et al. (LIT-669). For each, an accounting was written from
  the source and a checkout of the record at the filing's parent commit,
  under the read-and-file skill's accounting step and a codebook fixed
  beforehand, then scored item by item. Pooled, the replays recovered 95
  of the 138 items the filings held (0.69; per filing 0.61 to 0.75) and
  none of the 6 items the corrections added. Five of those six needed a
  work other than the source; the sixth was in an appendix the replay did
  not read. The replays also found items neither held, among them an
  error in Wang et al. that NOTE-645 still repeats. The replays were done
  and scored by one assistant instance, not by separate agents, and that
  instance, its scoring and the original filers are one model family; no
  exchange was eligible, because none is held in the repository. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-251 THEORY-210 CLAIM-tmpj6pb6 — Proposed or new; the study this pilots, a reading a correction revised, and the claim filed from this pilot -->

# CASE-tmpssuha: A pilot of the curation-completeness study on four replayed single-work readings: a replay from the source and the record as it stood recovers about two-thirds of what each filing held and none of what later corrections added

## The study

CASE-251 proposes scoring an agent's accounting of a source against the
filing of that source together with its later corrections. This pilot
ran it on four filings, in this order:

1. **Selection, before outcomes.** Readings of arXiv works with a later
   commit whose subject names the reading or an entry it filed as
   corrected, newest first, found from commit metadata alone. The four
   are the readings of LIT-970 (filing 33ed07ba3, corrected in
   THEORY-210 by 52f75cb94), LIT-882 (NOTE-683, THEORY-197;
   4a01ae541), LIT-842 (NOTE-645; 90f3ecd06) and LIT-669 (NOTE-538;
   24d31d943).
2. **A codebook, before any replay.** Units: works (W), ideas (C), gaps
   (G) and relations to held entries (R). F is what the filing held; K is
   what later corrections added. Measures: recall against F, recall
   against K, and extras in neither, checked against the source.
3. **Replay.** For each filing, an accounting from the arXiv source and
   a worktree at the filing's parent commit, committed before any filing
   or correction was opened.
4. **Scoring**, item by item, with a one-line reason for each match.

## Results

| filing | F recall | K recall |
|---|---|---|
| LIT-970, symmetry survey | 23/33 | 0/2 |
| LIT-882, Mehta and Schwab | 22/32 | 0/2 |
| LIT-842, Wang et al. | 30/40 | 0/1 |
| LIT-669, Lubana et al. | 20/33 | 0/1 |
| pooled | 95/138 = 0.69 | 0/6 |

By type, pooled: works 30/39, ideas 36/57, gaps 17/22, relations 12/20.
No duplicate (proposing to file what was held) and no misattribution.

**What the replays missed of F** was mostly what the filer made of the
source by further work: its own derivations (for LIT-882, that the
mapped free-energy criterion measures only normalization), recomputed
figures, open questions, appendix results, later works that cite the
source, and judgements of no bearing.

**What the corrections added** was accuracy, not omission. For LIT-882:
the free-energy point had been credited to the reader alone, and Lin,
Tegmark and Rolnick's appendix makes it, and the authors had conceded
Eq. 8's "iff" in a later comment. For LIT-842: the journal follow-up's
significance claim, relayed as given, holds only one-sided. For LIT-970:
two of the survey's attributions to Neural Mechanics and to Ziyin et al.
do not match those works. For LIT-669: Appendix F.3 proves the converse
of the conjecture, not the conjecture. Only the last is in the source
itself, in an appendix the replay did not read.

**What the replays found that neither held**, checked against the source:
Wang et al. explain the rarity of the bus sense of "coach" in British
corpora by calling it "mainly American", which runs the wrong way, and
NOTE-645 still repeats the explanation; Lubana et al.'s abstract and §6
state as demonstrated what §5 calls a conjecture; the survey's account of
conservation under gradient flow bears on CLAIM-093, which its filing did
not draw. One replay item was an error of the replay's own (a second
fault it claimed in Lubana et al.'s Definition 1).

## What it can and cannot show

- **Not independent.** The record's filers, the replayer and the scorer
  are one model family, Claude. Worse than CASE-251 planned, one
  instance did all four replays and the scoring: the tool for separate
  agents was not available to it. It saw the correction commits'
  subjects while selecting; three replay items they leaked are excluded.
  Scoring was not blind.
- **Not the episodes CASE-251 names.** No exchange, synthesis or upload
  is held in the repository, so the episodes of omission CASE-251 lists
  (works an exchange named that a pass neither registered nor left) were
  not eligible. All four are single works, whose corrections were of
  accuracy.
- **A different skill.** The read-and-file skill postdates all four
  filings; the replay used it, the filers did not have it.
- **Small.** Four filings, six correction items, partial reading of two
  sources.
- **What it does show.** On these four, a source-only accounting
  reproduces most of a filing's map and gaps and none of its later
  corrections, because those corrections came from reading other works.
  And the replays' extras confirm that F together with K is a lower bound,
  CLAIM-266's point about scoring a system by its own probes.

The wording is the assistant's (Claude, in this session); adopting it is
the owner's call.
