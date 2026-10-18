---
# Don't copy this file by hand — run `luria new term`. A TERM is a concept or
# distinction the argument is stated in. It has no credence; it has a
# definition, and when the definition changes, a new TERM supersedes the old
# one so the claims stated in it can be found (ADR-032).

# The standing of the DEFINITION, not a credence (ADR-046):
#   Proposed   a candidate, recorded and not adopted; the body says what it
#              would replace or add, and what would settle it
#   Active     adopted: the argument may be stated in it
#   Deferred   a candidate whose adoption is put off
#   Superseded adopted, then replaced; the successor's `supersedes` names it
#   Rejected   a candidate declined, or retired with nothing in its place
status: Active

# Relations to other terms, each optional (ADR-046). `rivals` and
# `complements` are symmetric: `luria link --fix` writes the other side.
# rivals:       # cannot both be adopted for one use; neither has won yet.
# - TERM-NNN    # A Proposed candidate rivals the Active term it would replace.
# complements:  # in force side by side, for a different sense or dimension
# - TERM-NNN
# refines:      # a special case of this broader term; both stay in force
# - TERM-NNN
# supersedes:   # adopted in place of this term, which goes Superseded
# - TERM-NNN

# The term itself.
title: the term

version: 1
tags:
- agency
date: '2026-01-01'
# line: will-organization

summary: >-
  The definition in one sentence.
---

# TERM-NNN: the term

## Definition

The definition, and the distinction it draws.

## What it is not

The neighbouring term it must not be confused with.
