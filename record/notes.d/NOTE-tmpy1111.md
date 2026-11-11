---
status: Read
paper: 'LIT-tmpng40s'
title: 'Thompson — Reflections on trusting trust'
version: 1
history:
- version: 1
  date: '2026-11-11'
  note: >-
    Read in full from a course copy of the journal pages (d.umn.edu, three
    pages, text extracted with pdftotext; the figures' code is partly
    garbled by the scan and was read for its structure only).
date: '2026-11-11'
summary: >-
  Thompson's three stages: a self-reproducing program, a compiler that
  "learns" an escape sequence and keeps it in binary only, and a compiler
  Trojan horse that miscompiles login and reinserts itself when the
  compiler is rebuilt from clean source. Read for QUESTION-tmpmus93.
---

# NOTE-tmpy1111: Thompson — Reflections on trusting trust

## Contribution

A construction, described as built: a compiler binary that carries two
Trojan horses, one for the login command and one that reinserts both into
the compiler whenever the compiler is compiled, so that "the login command
will remain bugged with no trace in source anywhere".

## Key results

- **Stage I** (p. 761): a self-reproducing program "can contain an
  arbitrary amount of excess baggage that will be reproduced along with the
  main algorithm".
- **Stage II** (p. 762): the compiler is taught what "\v" means once, in
  source, and thereafter "knows" it in binary only: "This is a deep
  concept. It is as close to a "learning" program as I have seen."
- **Stage III** (p. 763): the second pattern "is aimed at the C compiler.
  The replacement code is a Stage I self-reproducing program that inserts
  both Trojan horses into the compiler." Then: "We can now remove the bugs
  from the source of the compiler and the new binary will reinsert the
  bugs whenever it is compiled."
- **Moral** (p. 763): "You can't trust code that you did not totally create
  yourself." "No amount of source-level verification or scrutiny will
  protect you from using untrusted code." The lower the level (assembler,
  loader, microcode), the harder to detect.

## Assumptions

The attacker can once install a binary as the official compiler; the
compiler is compiled by itself; nobody compares the binary against one
built by an independent compiler.

## Concepts

Self-reproduction carrying "excess baggage"; knowledge held only in a
binary ("learning"); a Trojan horse as a deliberate miscompilation.

## Bearing on the record

- **QUESTION-tmpmus93.** The mechanism is installed once by one party and
  then reproduced by the host's own process (each compile) with no trace
  in the source the host maintains. The lecture's answer to "whose is it"
  is the installer's: "Perhaps it is more important to trust the people who
  wrote the software." It does not ask whether the host, by running the
  process, comes to own what it reproduces.
- **CLAIM-522.** An intervention on the visible state (restoring clean
  source) leaves the mechanism in place; only replacing the producing
  binary removes it. That is the shape of CLAIM-522's point, in software.

## Limitations

A lecture, three pages; the construction is described, not published as
code. Thompson credits the idea to an Air Force critique of Multics he
could not cite.
