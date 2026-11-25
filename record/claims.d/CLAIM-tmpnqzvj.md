---
status: Proposed
title: An editorial tag should be an independently authored record linking an editor to a particular version of a claim, result or work with a stated meaning and reason, so that a journal composed of tags can tell a recommendation from a review and must declare what inclusion in its feed means
version: 3
history:
- version: 2
  date: '2026-11-25'
  note: >-
    Gains the line scholarly-publishing (atlas scope 15) under ADR-
    tmpd3ckn: the entry is in that scope's core fiber in the hyperarticle
    atlas v0.3 (scratch/atlas/atlas-v0.3.md), and each atlas scope is
    documented as a line. No other change.
- version: 3
  date: '2026-11-25'
  note: >-
    Joins the work hyperarticles (ADR-tmp85hdc): Article 3 of A45 in the
    exchange "Hyper article interpretation" states its proposition without
    citing it, in §6. No other change.
role: thesis
warrant: interpretive
defeated_if: >-
  A journal of tags whose readers reliably tell recommendation from
  review without the tags' meanings being stated or the journal's rule
  declared, so that the vocabulary does no work; or a showing that tags
  bound to versions go stale faster than editors re-tag, so that a feed
  of version-bound tags reports mostly on versions no longer current.
tags:
- epistemology
- design-rationale
date: '2026-11-25'
line:
- records-of-inquiry
- scholarly-publishing
complements:
- CLAIM-tmpzsuh2
summary: >-
  A10 of the exchange "Hyper article interpretation" (2026-11-22),
  developing the owner's U4 ([CLAIM-tmpzsuh2](CLAIM-tmpzsuh2.md)): "A tag is an attributable
  editorial act. It has an author, a target, a meaning, and a timestamp",
  "A recommendation should be distinguishable from a formal review", and
  journals "just need to be clear about what their feeds actually mean".
  The record makes the same split for itself, between a claim's credence
  and its membership in a work ([ADR-032](../decisions.d/ADR-032.md), [ADR-104](../decisions.d/ADR-104.md)). The wording is A's
  (ChatGPT's, at A10 of the exchange "Hyper article interpretation");
  adopting it is the owner's call.
works:
- hyperarticles
---

<!-- inactive-ok-file: CLAIM-tmpzsuh2 CLAIM-tmpk6kcf — Proposed; the owner's thesis this refines, and the assistant's claim on citing a version -->

# CLAIM-tmpnqzvj: An editorial tag should be an independently authored record linking an editor to a particular version of a claim, result or work with a stated meaning and reason, so that a journal composed of tags can tell a recommendation from a review and must declare what inclusion in its feed means

## The claim

A10: "A tag is an attributable editorial act. It has an author, a target, a
meaning, and a timestamp. Ideally it also has a short explanation, because
the difference between "I endorse this result" and "I think this is
interesting but probably wrong" is pretty important." Its target is a
version: "I'd model an editorial tag as an independently authored record
linking an editor to a particular versioned scholarly object—not merely as
a hashtag or a Bluesky moderation label."

From that:

- **Recommendation is not review.** "A recommendation should be
  distinguishable from a formal review. A methodological critique should
  identify its target." Peer review becomes "a specialized kind of
  editorial contribution, with explicit criteria, a reviewable record, and
  a status that can change when the underlying work changes." A8 had the
  same: review "attaches to identifiable versions or changes".
- **A journal declares its rule.** Journals differ in what they require,
  and "Both can exist. They just need to be clear about what their feeds
  actually mean."
- **An issue is a release.** "A journal might periodically publish a
  citable snapshot of its feed, essentially turning the traditional
  journal issue into a release rather than a distribution mechanism."

## Where the record meets it

The record keeps the same split for itself. A claim's `status` is the
record's credence; its `works` say which manuscripts marshal it, and
"Membership says nothing of status" ([ADR-104](../decisions.d/ADR-104.md); [ADR-032](../decisions.d/ADR-032.md): "Credence and
inclusion come apart"). A tag that recommends is inclusion; a review is a
judgement of standing. A citation of a version is harder in a luria record
than A10 assumes ([CLAIM-tmpk6kcf](CLAIM-tmpk6kcf.md)).

## What it does not say

Not what vocabulary of tags a field should use.
