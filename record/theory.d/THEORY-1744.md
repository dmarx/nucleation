---
number: 1744
status: Proposed
formerly:
- THEORY-tmp8127k
title: 'Salemi et al. report that, for LLM agents answering data-science questions over large file collections, a main agent that broadcasts requests to a blackboard and lets file-holding helper agents decide whether to respond outperforms a matched design in which the main agent assigns subtasks to named helpers, in end-to-end accuracy and in file-discovery F1, with the advantage growing with the size of the collection, at roughly 1.8× the per-question cost.'
version: 1
tags:
- information-retrieval
- agency
- anthology-candidate
date: '2026-11-12'
source:
- LIT-2470
promote_when: >-
  a reading of the paper's Table 1, Table 2 and §4.2 confirms that the
  blackboard arm beats the master–slave arm on average across the three
  benchmarks and the four backbone LLMs, and that the relative gain over
  master–slave is larger on the larger data lakes.
bears_on:
- QUESTION-459
summary: >-
  The central account of [LIT-2470](../literature.d/LIT-2470.md), read in [NOTE-1852](../notes.d/NOTE-1852.md). Proposed until
  its promote_when is met.
---

# THEORY-1744: Salemi et al. report that, for LLM agents answering data-science questions over large file collections, a main agent that broadcasts requests to a blackboard and lets file-holding helper agents decide whether to respond outperforms a matched design in which the main agent assigns subtasks to named helpers, in end-to-end accuracy and in file-discovery F1, with the advantage growing with the size of the collection, at roughly 1.8× the per-question cost.

## The account

Salemi et al. report that, for LLM agents answering data-science questions over large file collections, a main agent that broadcasts requests to a blackboard and lets file-holding helper agents decide whether to respond outperforms a matched design in which the main agent assigns subtasks to named helpers, in end-to-end accuracy and in file-discovery F1, with the advantage growing with the size of the collection, at roughly 1.8× the per-question cost.

