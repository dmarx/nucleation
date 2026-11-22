---
status: Proposed
promote_when: >-
  An independent simulation or comparative study in which the generative
  entrenchment of elements is computed from a stated causal graph, as
  downstream reach, and is found to predict their evolutionary
  conservatism, with selection preserving the more entrenched elements
  under truncation selection. Simulations that assign selection classes
  without computing entrenchment, as most of this paper's do, do not
  meet it.
title: 'Wimsatt and Schank define the generative entrenchment of an element as the magnitude of what depends on it downstream in a directed causal graph of the organism and relevant environment, a graph that may contain cycles, and argue from network simulations under truncation selection that more entrenched, more strongly selected elements are preserved while weakly selected ones are lost, so that modular change is possible only rarely'
version: 1
source:
- LIT-tmpjv6ez
corroborates:
- CLAIM-531
bears_on:
- QUESTION-093
tags:
- philosophy-of-biology
- complex-systems
date: '2026-11-22'
summary: >-
  Wimsatt and Schank (2004), read in [NOTE-tmpkxkqj](../notes.d/NOTE-tmpkxkqj.md) (Read), a neighbour
  of [LIT-1926](../literature.d/LIT-1926.md). The definition is the paper's; the simulations mostly
  assign selection coefficients by class rather than compute
  entrenchment, so they bear on differential selection in general.
---
<!-- inactive-ok-file: LIT-1926 — Unavailable; the book this paper stands in for -->

# THEORY-tmpk0h4i: Wimsatt and Schank define the generative entrenchment of an element as the magnitude of what depends on it downstream in a directed causal graph of the organism and relevant environment, a graph that may contain cycles, and argue from network simulations under truncation selection that more entrenched, more strongly selected elements are preserved while weakly selected ones are lost, so that modular change is possible only rarely

## Source

William C. Wimsatt and Jeffrey C. Schank (2004), [LIT-tmpjv6ez](../literature.d/LIT-tmpjv6ez.md), read in
[NOTE-tmpkxkqj](../notes.d/NOTE-tmpkxkqj.md).

## What was actually shown

The definition is stipulated (MS p. 2). The simulations (MS pp. 5-14)
compare Kauffman's equal selection coefficients with coefficients rising
with downstream reach, then with assigned fitness classes under a
truncation threshold: the more strongly selected connections are kept
and reverse to near fixation, while the weakest are lost. A uniform
loss across classes, as Kauffman's model gives, is what would have
counted against it.

## What this does not say

- That entrenchment requires closure: reachability is one-way, and a
  tree's root is entrenched.
- That entrenchment is confined to the organism: maintained
  environmental conditions can be nodes.
- That the simulations measure entrenchment: most of them assign
  selection coefficients directly.
