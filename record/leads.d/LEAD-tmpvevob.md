---
status: Open
title: 'Build a dry-run retention diagnostic for luria: deterministic worklists from declared roots, reachability, cycles, revision chains, cross-tier dependencies, age and size, with an explanation of why each entry is kept'
version: 1
stage: idea
priority: medium
method:
- operationalization
- conceptual
tags:
- software-engineering
- databases
- design-rationale
date: '2026-11-26'
line:
- record-as-apparatus
- records-of-inquiry
presupposes:
- LEAD-tmp79qro
advances:
- QUESTION-tmpz8xkx
- CLAIM-tmpi0o8t
- CLAIM-tmpby6hz
- CLAIM-tmpdkwbk
summary: >-
  A27 §13 (phases 1 and 2 of its incremental plan) and A29 §§17–19 of the
  exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26): start
  "with graph analysis and non-destructive projections, not an automated
  semantic deletion system", as `luria gc --dry-run`, deterministic
  wherever possible, with language models used "only to generate
  candidates". "A collector should be able to say why it retained
  something, not merely why it recommended forgetting something." The
  command names are A's design proposals, not luria functionality. The
  wording is A's (ChatGPT, in the exchange of 2026-11-26); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpi0o8t CLAIM-tmpby6hz CLAIM-tmpdkwbk CLAIM-tmpwlw8t TERM-tmp96b3g TERM-tmp3t5jq CLAIM-tmpg2wk1 — Proposed; the claims and terms this would operationalize, filed 2026-11-26 -->

# LEAD-tmpvevob: Build a dry-run retention diagnostic for luria: deterministic worklists from declared roots, reachability, cycles, revision chains, cross-tier dependencies, age and size, with an explanation of why each entry is kept

## What to build

A29 §19 separates analysis from transformation:

| Proposed command | Function |
|---|---|
| `luria gc roots` | Inspect and explain declared root sets |
| `luria gc trace` | Calculate maintenance reachability |
| `luria gc candidates` | Generate candidate dispositions |
| `luria gc explain CODE` | Explain what requires an entry to remain available |
| `luria gc cool CODE` | Change default availability without losing the object |
| `luria gc compact` | Propose consolidated representations |
| `luria gc verify` | Check declared preservation invariants |
| `luria gc restore CODE` | Recover an archived representation |

LEAD-tmp79qro, filed from U17 to U19 of the same exchange, is the first
step: a tracing collector from luria's existing patterns and views, with a
worklist outside the closure of declared roots. This lead is the tool it
would grow into. The first version is the analysis half only, `roots`, `trace`,
`candidates` and `explain`, changing nothing (A27 §13's phase 1,
"Recommend candidates without modifying them").

## What it computes

All of it from the tree, without a model (A29 §17): reachability from
declared roots (CLAIM-tmpi0o8t), strongly connected components (clusters
that cite only one another), revision chains, cross-tier dependencies
(CLAIM-tmpdkwbk), entry age and document size; and the retention
requirement each entry inherits from its uses (CLAIM-tmpby6hz), with
alternative support reported, not joined (CLAIM-tmpwlw8t).

## Design choices A names

- **Explanation first.** `explain` says what keeps an entry: which roots
  reach it, through which relations, and what requirement each imposes.
- **Collect against a commit.** A29 §5: a cycle "could operate against a
  particular Git commit, produce a reviewable plan, and then revalidate its
  assumptions before that plan is merged", since a dependency added
  meanwhile can make a proposed cooling wrong.
- **Passes by scope.** A29 §5: opportunistic (entries touched by ordinary
  work), minor (recent additions), regional (one line), major (the whole
  record), compaction (consolidation).
- **Regions.** A29 §14: collect by a completed study or exchange, keeping
  its results, its evidence, its negative results, its open questions and
  its cross-region dependencies. The curation log already groups each
  exchange's filings, so the record has its regions.
- **Reversible operations first.** Tombstones, grace periods, snapshots,
  resurrection without a new identity and pins (A29 §12).
- **Borrow tools.** A29 §18 names NetworkX for graph analysis, git for
  snapshots, LLVM's pass design as a precedent for separately testable
  analysis and transformation passes, and libCacheSim for comparing cache
  policies on retrieval traces.

## What it would move

QUESTION-tmpz8xkx needs a candidate list before it needs a policy; the
diagnostic is the cheapest way to see how many entries no root reaches.
Its own cost counts against it (CLAIM-tmpg2wk1's transition term).
