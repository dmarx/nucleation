# LEAD-014 pilot: selection rule

Written 2026-11-22, before any candidate filing, its curation entry or its
corrections was opened. Only file names and commit subjects may be listed
while applying it.

## Population

Filings into this record (an exchange, a pasted synthesis, an upload or a
single work) that have a curation entry under `record/curation.d/`.

## Eligibility (all must hold)

1. **Source reachable.** The source text is either held in the repository
   at or before the filing commit (an exchange transcript, a pasted
   synthesis or upload saved under `record/` or `scratch/`), or is an arXiv
   paper fetchable from arxiv.org. Share links are not used: their decode
   can drift and the pilot cannot check it.
2. **A later correction exists, identifiable from metadata.** At least one
   of: a curation entry dated after the filing that names the filing's
   curation entry or source; a commit after the filing whose subject says
   correction, missed, omitted, left out, backfill, or re-registration for
   that source; a dated "Correction" section in the filing's own curation
   entry, detected by grep for the heading, not by reading it.
3. **Size.** Source no longer than about 25,000 words, so a replay fits the
   pilot's budget.
4. **Parent commit identifiable**: the first commit that adds the filing's
   curation entry has a parent on which the source exists and the filing's
   entries do not.

## Ordering and choice

List eligible candidates newest first by filing date. Take the first four,
with at most two of any one source type (exchange, synthesis/upload,
single work), so the pilot does not test one shape only. Ties go to the
smaller source. No candidate is skipped once listed, except for failing an
eligibility condition, and each skip is recorded with its reason.

## What is not used to choose

The size, content or number of corrections, and whether the original
filing looks good or bad.

## Applying the rule (2026-11-22)

**No exchange, synthesis or upload is held in the repository.** No
transcript or pasted text is saved under `record/` or `scratch/`; exchange
filings cite share links only. So condition 1 leaves single arXiv works,
and the cap of two per source type cannot be met: all four are single
works. This is the pilot's largest departure from CASE-251, whose named
episodes are exchanges.

Candidates were found from metadata only
(`cands.py` in this directory): readings (NOTE) of LITs with an `arxiv:`
field, and later commits touching that NOTE whose subject says correct,
missed, omitted, wrong, re-read or backfill, less sweeps (directive,
status review, promotion, lint, repair, stale). Condition 2 was read
strictly: the subject must name the work, its reading, or an entry the
filing commit added.

Newest first, skipped for condition 2 (subject names no entry of the
filing): LIT-2973 (owner's corrections on bulk and learning), LIT-1309,
LIT-1310, LIT-1336, LIT-1334, LIT-1326, LIT-1316 (one review commit
naming other entries), LIT-997 (CLAIM-115/139), and every reading whose
only later commit is a batch "apply the corrections" commit not naming it.

**Selected**, newest first:

| # | Work | arXiv | Filing commit (parent) | Naming correction |
|---|------|-------|------------------------|-------------------|
| S1 | LIT-970 | 2506.13018 | 33ed07ba3 (4fa4bfaa9), 2026-10-12 | 52f75cb94 "correct THEORY-210" (THEORY-210 was added by the filing as THEORY-tmpvl6ed) |
| S2 | LIT-882 | 1410.3831 | a277d428f (4da41298e), 2026-10-09 | 4a01ae541 "correct THEORY-197 and NOTE-683" |
| S3 | LIT-842 | 2107.14589 | b5ba76499 (a90aa7964), 2026-10-09 | 90f3ecd06 "Correct NOTE-645's account of the journal follow-up's significance claim" |
| S4 | LIT-669 | 2211.08422 | 02cbb441a (d2aadd3e0), 2026-10-03 | 24d31d943 "correct the Lubana reading" |

S2, S3 and S4 were filed in batch commits with other works; only the named
work is replayed and scored, and F is restricted to the entries and
curation lines for that work.

Known before the replay, from the subjects alone: that each filing was
later corrected, and which entry. Not known: what the correction said.
