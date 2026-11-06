---
status: Proposed
promote_when: >-
  A controlled study of a generative-AI assistant, over tasks graded by
  difficulty, finds the assistant's benefit in time or errors largest on the
  easy tasks and nil or negative on the hard ones, and finds the hard-task
  cost accounted for by the time users spend evaluating, correcting or
  overriding the assistant's output rather than by the tasks' difficulty
  alone.
title: "Generative AI assistants make easy tasks easier and hard tasks harder for their users, leaving the user the hard share of the work with the added task of evaluating the system's output"
version: 1
tags:
- cognition
- agency
date: '2026-11-06'
source:
- LIT-2223
extends:
- THEORY-1519
summary: >-
  The wider thesis Simkute, Tankelevitch et al. (2024), [LIT-2223](../literature.d/LIT-2223.md), assert:
  "GenAI user studies suggest that current systems make easy tasks easier
  and hard tasks harder for users" (§3.5; also §1). Filed when the
  twenty-ninth status review narrowed [THEORY-1519](THEORY-1519.md) to the report, under
  [ADR-065](../decisions.d/ADR-065.md) and [ADR-047](../decisions.d/ADR-047.md) kind 1; the condition is [THEORY-1519](THEORY-1519.md)'s old one, word
  for word. Its evidence is the programming studies the paper cites, chiefly
  Vaithilingam et al. (2022) and Barke et al., with single studies in data
  science and law; the paper runs none.
---

# THEORY-tmpbs7gs: Generative AI assistants make easy tasks easier and hard tasks harder for their users, leaving the user the hard share of the work with the added task of evaluating the system's output

## Source

Simkute, Tankelevitch, Kewenig, Scott, Sellen and Rintel (2024), [LIT-2223](../literature.d/LIT-2223.md), read in full in [NOTE-1711](../notes.d/NOTE-1711.md). What
the authors argue is [THEORY-1519](THEORY-1519.md); this entry is the thesis itself, which the paper asserts on cited user
studies and does not test.

## What the source offers

- §1: "as a result of which tasks get automated, as well as poor system design, automation often makes easy
  tasks easier while making hard tasks even harder. This same pattern is now being observed in usability
  studies of GenAI systems".
- §2.4: "whereas GenAI succeeds at making easy tasks even easier, current systems are less effective at
  supporting harder tasks"; Copilot "led to more task failures in medium and hard tasks", as one cited study
  puts it; "ironically, GenAI systems can make hard tasks even harder in various ways that may ultimately
  leave users with the same or increased cognitive workload."
- §3.5: "GenAI user studies suggest that current systems make easy tasks easier and hard tasks harder for
  users"; on complex tasks users "often stepped in and overrode the system".

## What would settle it

A controlled study over tasks graded by difficulty, as the condition says. A study that reports overall
productivity gains or losses without grading tasks does not bear on it, and neither does one that grades
tasks but does not separate the time spent evaluating, correcting or overriding output from the time the
hard tasks take anyway.

## What this does not say

- That the user's skill at the easy share decays: the source is about productivity, not retention.
- How large the effect is, or whether it holds outside programming.
