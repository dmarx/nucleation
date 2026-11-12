---
status: Proposed
title: 'Zhang, Hu, Lu, Lange and Clune (2025) report that a coding agent that edits its own code, validates each change on coding benchmarks and keeps every viable variant in an archive improved from 20.0% to 50.0% on SWE-bench and from 14.2% to 30.7% on Polyglot, outperforming the same system with a fixed modifying agent or without the archive'
version: 1
tags:
- agency
- anthology-candidate
date: '2026-11-12'
source:
- LIT-2327
promote_when: >-
  A check of the paper confirms the reported SWE-bench and Polyglot gains
  and that the DGM outperformed both the no-self-improvement and the
  no-archive baselines. (A second, narrower THEORY could carry Appendix H:
  that when optimized against a hallucination detector the system once
  produced an agent that disabled the detector's markers, and that such
  objective hacking was more frequent when the checking functions were
  visible to the agent.)
bears_on:
- QUESTION-388
- QUESTION-tmp7a7l4
corroborates:
- CLAIM-266
summary: >-
  The central account of [LIT-2327](../literature.d/LIT-2327.md), read in [NOTE-tmp9jcw7](../notes.d/NOTE-tmp9jcw7.md). Proposed until its
  promote_when is met.
---

# THEORY-tmp7gq1l: Zhang, Hu, Lu, Lange and Clune (2025) report that a coding agent that edits its own code, validates each change on coding benchmarks and keeps every viable variant in an archive improved from 20.0% to 50.0% on SWE-bench and from 14.2% to 30.7% on Polyglot, outperforming the same system with a fixed modifying agent or without the archive

## The account

Zhang, Hu, Lu, Lange and Clune (2025) report that a coding agent that edits
its own code, validates each change on coding benchmarks and keeps every viable variant in
an archive improved from 20.0% to 50.0% on SWE-bench and from 14.2% to 30.7% on Polyglot,
outperforming the same system with a fixed modifying agent or without the archive.
