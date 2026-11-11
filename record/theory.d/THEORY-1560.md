---
number: 1560
status: Proposed
formerly:
- THEORY-tmpkzkpc
promote_when: >-
  A reading of the lecture in full finds the construction described as
  the title states: a compiler binary whose Trojan horse miscompiles the
  login command and reinserts itself when the compiler is rebuilt from
  source cleaned of it, and the moral that source-level scrutiny cannot
  protect against such a binary. Whether the attack is practical, or how
  it is detected, is not asked.
title: 'Thompson describes a compiler binary that miscompiles the login command to accept a known password and reinserts that Trojan horse, and itself, whenever the compiler is compiled, so that it persists after every source has been cleaned, and concludes that no source-level verification protects a user from code they did not create'
version: 1
tags:
- epistemology
date: '2026-11-11'
source:
- LIT-2332
bears_on:
- QUESTION-449
summary: >-
  Thompson's Turing lecture ([NOTE-1715](../notes.d/NOTE-1715.md)). A mechanism installed once in
  a binary is reproduced by the host's own compiling and lives in no
  source. It bears on [QUESTION-449](../questions.d/QUESTION-449.md): an installed mechanism the host
  reproduces, whose author the lecture holds responsible ("trust the
  people who wrote the software").
---

# THEORY-1560: Thompson describes a compiler binary that miscompiles the login command to accept a known password and reinserts that Trojan horse, and itself, whenever the compiler is compiled, so that it persists after every source has been cleaned, and concludes that no source-level verification protects a user from code they did not create

## The account

Thompson builds, in three stages, a C compiler binary with two Trojan
horses. One miscompiles login to accept a known password; the other
recognizes the compiler's own source and inserts both, "a Stage I
self-reproducing program". Installed once, the binary "will reinsert the
bugs whenever it is compiled", and login "will remain bugged with no trace
in source anywhere". Hence: "No amount of source-level verification or
scrutiny will protect you from using untrusted code."

## Evidence

The lecture itself ([NOTE-1715](../notes.d/NOTE-1715.md)): the construction described as built,
with figures of its structure. It credits the idea to an uncited Air Force
critique of Multics.

## What it bears on

[QUESTION-449](../questions.d/QUESTION-449.md): the mechanism is formed by one party and reproduced by
the host's process; the lecture places responsibility with "the people who
wrote the software".
