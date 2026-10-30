---
status: Open
title: 'On another database and web stack with native materialized views and queries of graded cost, does a stored query result kept current on every update lose to recomputation exactly when reading it costs about as much as recomputing it and its refresh runs on the resource that serves requests, and win otherwise?'
version: 1
tags:
- databases
- operations-research
date: '2026-10-30'
line: distributed-agency
summary: >-
  The promotion condition formerly on THEORY-383, moved here when the
  status review of 2026-10-30 promoted it under ADR-065. Labrinidis and
  Roussopoulos measured one testbed with cheap indexed selections; their
  cost model's Eq. 9 was never evaluated against measurement.
---

# QUESTION-tmpuhx4v: On another database and web stack with native materialized views and queries of graded cost, does a stored query result kept current on every update lose to recomputation exactly when reading it costs about as much as recomputing it and its refresh runs on the resource that serves requests, and win otherwise?

## Why it is a question

THEORY-383 reports one testbed (LIT-1118, read in NOTE-908): on Apache
and Informix with cheap indexed selections, a query result stored in the
DBMS and refreshed on every update lost to recomputation at five or more
updates per second, which the authors explain by reading the stored result
costing about as much as recomputing it and its refresh loading the same
DBMS. Whether that explanation picks out the condition under which a
stored result loses, on other systems and other query costs, is open.

## What would answer it

A measurement on another database and web stack, with native materialized
views and queries of graded cost, showing that a stored query result kept
current on every update loses to recomputation exactly when reading the
stored result costs about as much as recomputing it and the refresh runs
on the resource that serves requests, and wins otherwise. More runs on one
testbed with cheap indexed selections cannot settle it, since they only
repeat the case held; nor can the paper's Eq. 9, whose values were never
computed against measurement.
