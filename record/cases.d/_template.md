---
# Don't copy this file by hand — run `luria new case`. A CASE is an example,
# thought experiment or historical episode the argument uses, filed once so
# that every claim it serves points at the same thing (ADR-032).

# Active | Proposed | Deferred | Superseded | Rejected — whether the record
# still uses it. A case retired for a better one names it in `superseded_by`.
status: Active

title: A short name for the case

version: 1

# documented | stipulated | fictional — how much of it is fact.
standing: fictional

# specimen | thought-experiment | construction | reported-study |
# proposed-study | executed-study — what kind of thing it is (ADR-042).
# Orthogonal to standing. A steel-man is not a kind: it is a CLAIM with
# role counter, and the case relates to it.
kind: thought-experiment

tags:
- agency
date: '2026-01-01'

# illustrates: [CLAIM-000]        # makes a claim vivid, bears no weight
# counterexample_to: [CLAIM-000]  # shows a claim false as stated
# variant_of: [CASE-000]          # alters another case in a stated respect
# substitutes_for: [CASE-000]     # stands in for another case
# line: will-organization

summary: >-
  The case in two sentences, and what it is used to show.
---

<!-- unresolved-ok-file: CLAIM-000, CASE-000 — the placeholders a new document replaces -->

# CASE-NNN: A short name for the case

## The case

What happens, and what is held fixed.

## What it can show

And, given its standing, what it cannot.
