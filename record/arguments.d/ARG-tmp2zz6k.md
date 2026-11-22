---
status: Proposed
title: "Natschläger, Bertschinger and Legenstein's driven threshold networks, whose readout does best near the order-to-chaos line when averaged over many tasks, as evidence, support the claim's memory-against-separation strand and leave its thesis standing, since a task-averaged optimum with no per-task optima does not meet its defeater"
version: 1
form: evidence
grounds:
- THEORY-tmps8t83
concludes:
- CLAIM-809
tags:
- complex-systems
- neuroscience
- information-theory
date: '2026-11-22'
line:
- formal-apparatus
- learned-structure
summary: >-
  CLAIM-809 grounded Bertschinger and Natschläger (LIT-2991) unread for
  strand 1. That article is unreachable; its abstract says "only near the
  critical boundary can such networks perform complex computations on time
  series", and its NIPS companion (LIT-tmpdsowv, read in NOTE-tmpi5t3r)
  restates the programme. The companion supports strand 1 (order is fading
  memory; chaos leaves "spurious" information about initial conditions).
  Its headline is the universal reading the thesis rejects, but the
  optimum is averaged over many tasks by design and no per-task optima are
  reported, which the thesis allows and the defeater does not reach. The
  reading joins the claim's grounds beside the unread LIT. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-809 THEORY-tmps8t83 LIT-2991 CLAIM-814 THEORY-tmpye6xs ARG-tmps7n0g — Unavailable, Proposed or new; the claim, the reading, the work it stands in for and the entries it is set against -->

# ARG-tmp2zz6k: Natschläger, Bertschinger and Legenstein's driven threshold networks, whose readout does best near the order-to-chaos line when averaged over many tasks, as evidence, support the claim's memory-against-separation strand and leave its thesis standing, since a task-averaged optimum with no per-task optima does not meet its defeater

## The inference

CLAIM-809, strand 1: "An ordered network forgets; a chaotic one separates
but cannot be read reliably; near the transition both can hold". Its
defeater: "every component of that measure is maximized at the transition
for every task in a stated family and every finite integration window";
"A single task whose optimum sits at the transition does not defeat it."

THEORY-tmps8t83: fading memory "is equivalent to the requirement that all
state differences vanish, i.e. being in the ordered phase"; in chaos the
state "contains “spurious” information about the initial conditions";
"The highest performance is clearly achieved for parameter values close
to the critical line"; the networks "are not optimized for any specific
task but their computational capabilities are assessed by evaluating them
for many different tasks."

## Critical questions

- **Is the evidence what strand 1 needs?** Yes, in substance: order is
  fading memory, and chaos fails because separation is polluted by
  initial conditions, which NM-separation subtracts (f*). The mechanism is
  not readout noise; the strand's "cannot be read reliably" should be read
  that way.
- **Does the headline defeat the thesis?** No. "Only near" and §7's
  "general property of input driven dynamical systems" are the universal
  reading, but what is shown is a maximum of performance averaged over
  delayed parity and random Boolean functions. The paper reports no
  per-task or per-component optima and no total capacity, so it shows
  neither that every task peaks at the line nor that capacity is
  redistributed. It is silent on the redistribution clause.
- **Is it the original's evidence?** Not quite. It is the companion paper
  by the same group, generalizing the original's zero-mean model; the
  original's abstract carries the same headline, and its body is unread.
- **How far does it reach?** One model class (driven random threshold
  networks), one input statistic, tasks with a few steps of memory, the
  annealed mean field. The edge is damage spreading, not branching of
  activity.

## Verdict

Supports strand 1; qualifies the thesis without defeating it. The
record's cases now run three ways: CLAIM-814 (readout noise pushes the
optimum toward the transition), Azizpour and colleagues (THEORY-tmpye6xs,
subcritical for every finite window), and this one (near the order–chaos
line, task-averaged). Calvet, Reulet and Rouat add that the alignment
depends on the system (ARG-tmps7n0g). Proposed.
