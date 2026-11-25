---
status: Proposed
title: "Coverage of a region of the record by views has four separable dimensions, source, argument, expository and transition coverage, each of which can be high while another is low, and a view's review status is a different thing from the standing of the claims it presents"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that two of the dimensions cannot come apart: that a region
  rich in entries always has a defensible route from its premises to its
  conclusions, or that a reviewed exposition always has its overlaps with
  neighbouring views checked; or that a view's review status and its
  claims' standing are one judgment.
tags:
- design-rationale
- epistemology
date: '2026-11-25'
line:
- record-as-apparatus
rests_on:
- CLAIM-178
summary: >-
  A53 §5 and A57 §6 of the exchange "Hyper article interpretation"
  (2026-11-25), at the owner's U24 ("what regions of Nucleation already
  have good coverage hyperarticle coverage? can we identify regions which
  are deficient?"). A53 named representational, expository and transition
  coverage; A57 split the first into source and argument coverage. A53's
  figures are checked against the record at the commit A59 names. The
  wording is A's (ChatGPT's, at A53 and A57 of the exchange "Hyper article
  interpretation"); adopting it is the owner's call.
---

<!-- inactive-ok-file: CLAIM-178 ADR-143 CLAIM-tmp6xzjy — Proposed or new; the manuscript-as-view claim it rests on, the manuscript protocol, the report that would measure it and the gap fill on transitions -->

# CLAIM-tmpd1a2h: Coverage of a region of the record by views has four separable dimensions, source, argument, expository and transition coverage, each of which can be high while another is low, and a view's review status is a different thing from the standing of the claims it presents

## The claim

A57 §6, assessing "each candidate view across four dimensions":

- **Source coverage**: "Are the relevant CLAIMs, ARGs, CASEs, TERMs, and
  SYNTHESISes present and appropriately related?"
- **Argument coverage**: "Is there a defensible route from premises and
  evidence to conclusions? Are the objections and limitations visible?"
- **Expository coverage**: "Does a readable, audience-appropriate view
  actually exist? Has it been reviewed against the record?"
- **Transition coverage**: "Are the relationships to neighboring views
  explicit, and are the proposed correspondences supported?"

"A candidate could be strong in one dimension and weak in another. I'd
also distinguish a view's review status from the epistemic standing of
the claims it presents. An excellent exposition of a disputed argument
can be a perfectly good hyperarticle." A53 §5 had drawn the first
distinction as representational against expository coverage, with
transition coverage as a third.

## A53's evidence, checked

A53 reported counts from the generated indexes. The assistant recounted
them from the sources at the commit A59 names (`23b9dff`, 2026-11-24)
with python3 -I: the line counts match A53's table for eleven of the
twelve lines (will-organization is 142 claims, 19 ARGs and 44 cases, not
141, 18 and 43); the record held 124 syntheses, 113 Proposed and 11
Superseded, none Current; the `works` vocabulary had 12 works; two
manuscript workspaces were in `scratch/manuscripts/`; 152 claims were
members of governance-of-possibility and 45 claims and 5 ARGs of
what-survives-translation; no work covered learned-structure. Since then
a thirteenth work, governance-of-becoming, and its workspace have been
added. Its examples of dimensions coming apart are these: distributed
agency, with 428 claims and 193 cases and no manuscript (source without
expository coverage); learning-and-inquiry, with ten syntheses and two
ARGs on its line (accounts without argument on the line). The check is
the assistant's (Claude, in this session).

## Where it is held

That a view's inclusion of a claim is not the claim's standing is held:
"Membership says a claim is in the work; whether the record believes it
is the status" (the `works` vocabulary, ADR-032), and CLAIM-178's
"claims carry status and inclusion separately". ADR-143's second
invariant makes a manuscript show each step's standing. What is new is
the division of coverage, and transition coverage in particular, whose
check CLAIM-tmp6xzjy says must be on cycles of views. A report that
would measure the four is LEAD-tmpsgkxe.

## What it does not say

That counts measure any of the four. A53: "a coverage analysis cannot
just count objects. A line with one decisive formal counterexample may
be better supported than a line containing dozens of anecdotes."
