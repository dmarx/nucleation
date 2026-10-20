---
# Don't copy this file by hand — run `luria new note`, which assigns the
# code and fills in what a machine can compute.
#
# A NOTE is a READING of a paper: what it contains, what it assumes, what it
# proves, and how strongly. It is not the paper's standing in this record
# — that is the LIT note's job, and the two are allowed to disagree
# (ANTH-ADR-025).

# Read | Skimmed | Unread | Superseded, from statuses.yaml beside this file.
# This says HOW DEEPLY THE PAPER WAS READ, not whether it is any good.
# Be honest here. `Skimmed` is a useful, respectable status and is
# deliberately not in force: it is not enough to source a practice from,
# and the whole scheme exists because the record could not previously tell
# a read paper from an unread one.
status: Skimmed

# REQUIRED. The LIT code this is a reading of. The bibliography — title,
# authors, year, arxiv — lives there and is NOT repeated here.
paper: LIT-tmp0wmvt

# Repeat the paper's short name as the body's `# NOTE-xxx:` heading; the
# lint checks that the two agree.
title: 'Consciousness and the Collapse of the Wave Function'

version: 1

# There is deliberately no `tags:` line here either, for the same reason and a
# stronger one. A reading's topics are DERIVED from the paper named in `paper:`
# above — a note and its paper are the same paper, so a second copy of its
# subject is a second copy free to disagree, and four of them were
# (ANTH-ADR-038). Retag the LIT note; the reading follows.

date: '2026-10-20'

# There is deliberately no `published:` line here. A reading's publication date
# is DERIVED from the paper named in `paper:` above, and writing it down is a
# lint violation — the value has one home and this is not it.

# What the index table shows. One or two sentences: the finding, not the
# subject area. Prose, so bare codes get linked by `luria link --fix`.
summary: >-
  Chalmers and McQueen make consciousness-collapse precise as a
  super-resistance model (IIT's Q-shape resisting superposition, with a
  continuous-collapse dynamics), find simple versions refuted by the
  quantum Zeno effect, and argue that collapse is the gap in causal
  closure that interactionist property dualism needs. Skimmed: the
  introduction, the objections and §8 were read, the formal §§2-7 were not.

---
<!-- inactive-ok-file: THEORY-485 — Proposed; the entry this reading checks, nothing in the reading rests on it -->

# NOTE-tmpoa1mw: Consciousness and the Collapse of the Wave Function

**Depth.** Read 2026-10-20 from the arXiv text (2105.02314v1), in part: §1
(introduction, with the three common objections to consciousness-collapse)
and §8 (the causal role of consciousness) were read in full, the headings and
opening paragraphs of §§2-7 were read, and the mathematics of §§2-7
(superselection, the IIT Q-shape, the continuous-collapse dynamics and the
proposed experiments) was not checked. Filed in batch 059 of the promotion
audit to check how [LIT-164](../literature.d/LIT-164.md) represents this work.

## Contribution

The most developed attempt to turn "consciousness collapses the wave
function" into a dynamics with definite conditions. It sorts collapse
proposals into super-resistance models, in which some property resists
superposition, and takes consciousness, measured by integrated information
theory, to be that property. Simple versions are refuted, which makes the
thesis empirical rather than merely philosophical.

## Key insight

The usual objections cancel when the two views are taken together: physicists
reject consciousness-collapse because it is dualist, and philosophers reject
interactionist property dualism because it breaks causal closure, but collapse
"appears to be precisely such a gap" in closure as a non-physical
consciousness might fill (§1).

## Assumptions

- Integrated information theory, or some measure like it, fixes which
  physical states are conscious and with what Q-shape (§4, not checked).
- Consciousness is super-resistant: superpositions of distinct Q-shapes are
  suppressed by a collapse dynamics (§2).
- The collapse dynamics is continuous, of the CSL family, rather than an
  instantaneous superselection (§6, not checked).

## Key results

Stated at the level of the parts read; the formal statements were not checked.

- **The Zeno problem** (§3). An absolute super-resistance (superselection)
  model is refuted by the quantum Zeno effect, since constant collapse onto
  Q-shape eigenstates freezes the evolution of consciousness. This is what
  forces the move to continuous dynamics.
- **Testability** (§7). Continuous-collapse versions are said to be testable
  in principle, with quantum computers as the candidate apparatus.
- **The causal role** (§8). On a materialist IIT the law is fundamental
  physics about a complex physical property. On a property-dualist reading a
  consciousness-to-physics law gives non-physical consciousness a causal role.

## Claims

Not filled: this note is Skimmed.

## Connections

Builds on Wigner and on von Neumann's measurement-collapse picture, on
continuous spontaneous localization, and on Tononi's integrated information
theory. It is one of the accounts [LIT-164](../literature.d/LIT-164.md) sorts.

## Bearing on the record

[THEORY-485](../theory.d/THEORY-485.md), via [LIT-164](../literature.d/LIT-164.md) and [NOTE-112](NOTE-112.md). [NOTE-112](NOTE-112.md) records Poltorak representing
this work as a mind-modified collapse law, that is, new dynamics and a rival
hypothesis that is explicit and testable. That representation is accurate:
the authors present consciousness-collapse as a dynamics alongside Bohm,
Everett and GRW, and devote §7 to tests.

The work also bears on [THEORY-485](../theory.d/THEORY-485.md) in a second way. The authors explicitly
argue the opposite of [THEORY-485](../theory.d/THEORY-485.md)'s conclusion: that collapse is a gap in
causal closure. Whether that conflicts with "closure relative to fundamental
physics" turns on whether a law linking consciousness to collapse counts as
fundamental physics. On the materialist reading it does, and on the
property-dualist reading the authors intend it does not. That is the
criterion-of-the-physical problem [THEORY-485](../theory.d/THEORY-485.md) already names. So the work sits
where [THEORY-485](../theory.d/THEORY-485.md) puts it, and is also the clearest rival statement that its
"no causal gap" clause has to answer. Nothing here argues P7, the
dynamical-to-causal bridge.

No instruction for machine-learning practice; nothing for the Anthology.

## Limitations

- The authors do not argue that the thesis is true, only that it is coherent,
  precise in parts and not ruled out by known physics.
- IIT itself is contested, and the model inherits that.
- This reading did not check the dynamics or the experimental proposals.

## Open questions

- Is a consciousness-collapse law physical? This is the reading's question
  for [THEORY-485](../theory.d/THEORY-485.md), and the authors leave it to the interpretation of IIT.
- Do the §7 experiments separate consciousness-collapse from other
  continuous-collapse models at accessible scales?
