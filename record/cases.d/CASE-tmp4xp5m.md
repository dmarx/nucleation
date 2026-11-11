---
status: Active
title: 'A former graduate student''s self-reproducing compiler Trojan horse, which kept a lab''s program flashing hateful messages by restoring its source on every compile and restored itself when the compiler was rebuilt from clean source'
version: 1
standing: stipulated
kind: specimen
tags:
- ethics
- epistemology
date: '2026-11-11'
line:
- organizational-normativity
- distributed-agency
reported_in:
- THEORY-tmpn3ohs
illustrates:
- CLAIM-522
summary: >-
  Stute's story ([THEORY-tmpn3ohs](../theory.d/THEORY-tmpn3ohs.md)), the incident form of Thompson's attack
  ([THEORY-tmpkzkpc](../theory.d/THEORY-tmpkzkpc.md)), filed at the owner's request for [QUESTION-tmpmus93](../questions.d/QUESTION-tmpmus93.md).
  Stipulated: told as true, with nothing a reader can check. A mechanism
  formed by one party, reproduced by the host's own routine (compiling),
  hidden from the host, and removed only by replacing the binary that
  produces it.
---
<!-- inactive-ok-file: THEORY-tmpkzkpc THEORY-tmpn3ohs — Proposed; the readings filed with this entry, cited with their standing -->

# CASE-tmp4xp5m: A former graduate student's self-reproducing compiler Trojan horse, which kept a lab's program flashing hateful messages by restoring its source on every compile and restored itself when the compiler was rebuilt from clean source

## The case

A psychologist's research program, written by a former graduate student,
flashes "some white supremacy message" for half a second before each
question. The source is deliberately mangled. A hired programmer cleans
it; on the next compile the mangled files and the messages return. He
recompiles every library from source; they return. The cause is the
compiler binary: it recognizes the program and rewrites its source when it
is compiled. Rebuilding the compiler from its clean source fails too,
because the binary reinserts its own Trojan horse, working in "a hidden
directory" it deletes. The fix is a compiler binary copied from another
machine of the same revision. The compiler also backdoored login.

## What it shows

- **Formation and maintenance come apart.** The mechanism was formed by a
  person who had left. It was kept in being by the lab's own routine
  activity, compiling, which ran it every time.
- **The host did not maintain it; it maintained itself through the host.**
  The lab's process carried the mechanism, but what restored the
  mechanism was the installed component's own code running inside that
  process, and it hid itself from the lab. No one in the story counts the
  payload as the lab's doing.
- **Repair of state does not reach it** ([CLAIM-522](../claims.d/CLAIM-522.md)). Restoring clean
  source, at every level the lab could see, left it in place; only
  replacing the producing binary removed it.

## Bearing on [QUESTION-tmpmus93](../questions.d/QUESTION-tmpmus93.md)

The question asks whether an installed origin matters to whether an
organization's counter-normativity is its own, or whether only whose
process now maintains it decides. The case separates two readings of
"whose process": the host's routine that carries a mechanism, and an
installed component that maintains itself by running inside that routine,
hidden from the host. On the second reading the lab is no maintainer at
all, and the case answers nothing about an organization that reproduces a
mechanism it can see. The reading is the assistant's.

## Standing

Stipulated. The story names no institution, date or record, and follows
Thompson's published construction ([THEORY-tmpkzkpc](../theory.d/THEORY-tmpkzkpc.md)) closely; it is used
for what it makes clear, not as evidence that the incident occurred.
