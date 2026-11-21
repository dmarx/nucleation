---
status: Proposed
title: 'Copying exactly anchors a copy to the version it was taken from, so where the source is revised the copy keeps what the revision removed: exact copying conserves staleness as faithfully as content, and what anchors a derived text to a revisable source is a tie to the source that a revision has to pass through, not exactness'
version: 1
role: counter
warrant: empirical
defeated_if: >-
  Evidence that the record's derived texts that copy their sources
  exactly, such as summaries, titles and carried-over fields, are no more
  often left behind by a revision of their source than derived texts
  that paraphrase it; or a reading of RETRO-004 on which its summary was
  not copied from a source that had already been corrected.
tags:
- design-rationale
- epistemology
date: '2026-11-21'
line:
- nucleating-argument
- record-as-apparatus
objects_to:
- CLAIM-772
rests_on:
- CLAIM-635
grounds:
- THEORY-332
summary: >-
  CLAIM-772 makes exact copying the record's means of anchoring content.
  Exact copying conserves whatever the copied version held, including what
  the source has since corrected. RETRO-004 is the case: a postmortem's
  body was corrected the day it was filed, its summary was not, and when it
  became RETRO-004 the summary was carried over exactly, with the
  sentence the body had withdrawn. For a source that is revised, the
  hazard is not drift but staleness, and what guards against it is a
  revision that must pass through every copy, or a copy that records the
  version it came from. Raised in the owner's exchange of 2026-11-21. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-772 RETRO-004 — Proposed or Draft; the claim objected to and the case -->

# CLAIM-tmp0kqq4: Copying exactly anchors a copy to the version it was taken from, so where the source is revised the copy keeps what the revision removed: exact copying conserves staleness as faithfully as content, and what anchors a derived text to a revisable source is a tie to the source that a revision has to pass through, not exactness

## The objection

[CLAIM-772](CLAIM-772.md) says the record "copies content exactly, by code and verbatim
reading", and that exactness is what keeps the start. [CLAIM-635](CLAIM-635.md) is
about a start that never changes. The record's sources do change: entries
carry versions, titles are rewritten, bodies are corrected. Against a
source that changes, an exact copy is anchored to the version it was taken
from. It keeps the source's value at the time of copying, which after a
revision is the value the revision removed.

**The case.** POSTMORTEM-002, in its first version, called the missing
converse fields a defect. The filer corrected the body the same day, on
reading luria's code. The summary in the frontmatter was not corrected.
When the review became [RETRO-004](../retrospectives.d/RETRO-004.md), the summary was carried over exactly,
and still says the converses "are declared but never written". The copy
was faithful, and faithful to a sentence its own source had withdrawn.

**What this changes.** For a derived text whose source can be revised,
the failure to guard against is not drift but staleness, the problem of
keeping copies coherent with a source that is written to. Exactness does
not help with it, and makes it harder to see, since an exact copy looks
right. What helps is one of two ties:

- a revision that has to pass through every copy (the copy is regenerated
  from the source, as the record's generated views are), or
- a copy that records the version it was taken from, so that a reader or
  a check can see it is behind (as a citation of an entry at a dated
  commit would).

The online rule for when to bring a copy up to date, at a standing cost
against a one-time price ([THEORY-332](../theory.d/THEORY-332.md)), is a question that only arises
once the second tie exists.

**So** the record's anchoring of a derived text to a revisable source is a
matter of what ties the copy to the source's current version, not of how
exactly it copies.

## What it does not say

- Not that exact copying is a mistake. Against a source that is not
  revised, it is [CLAIM-635](CLAIM-635.md)'s case and keeps the start.
- Not that the record's generated views are stale. They are regenerated,
  which is the first tie. The hazard is in what is copied by hand or
  carried over: summaries, titles quoted in other entries, fields carried
  from a superseded entry to its successor.
- Not how common this is. One case, found by a reader of the manuscript.
