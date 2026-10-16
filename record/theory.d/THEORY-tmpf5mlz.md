---
status: Proposed
promote_when: >-
  A systematic measurement of neighbour-set stability (a turnover or rank
  measure stated in advance) against word frequency across several corpus
  increments and several random seeds, in static and in contextual
  models. It is promoted if turnover falls with frequency and consistency
  of use beyond seed noise, and if frequent words keep their
  neighbourhoods under additions that move every similarity value. It is
  refuted if frequent words' neighbourhoods turn over as much as rare
  words' once seeds are controlled. More before-and-after tables for
  hand-picked words cannot settle it.
title: "If a word's meaning in a distributional model is read differentially, as its relations to its nearest neighbours rather than its coordinates, then adding text moves every similarity value slightly but leaves the neighbourhoods of frequent, consistently used words intact and shifts those of rare words that the new text uses heavily, so the instability that holism implies is local and graded rather than total"
version: 1
tags:
- philosophy-of-language
- linguistics
date: '2026-10-16'
source:
- LIT-208
summary: >-
  Grindrod, Porter and Hansen (2024), [LIT-208](../literature.d/LIT-208.md), read in full in [NOTE-158](../notes.d/NOTE-158.md).
  The conceptual reply to the instability objection is argued; the
  empirical half is four hand-picked words in two before-and-after
  demonstrations (a count model on Stein plus a Hemingway story; Word2vec
  on Wikipedia plus the SEP), top-10 lists, one run each, no metric. The
  abstract's proportionality of resistance to frequency is not measured,
  the criterion used (a preserved neighbour list) is not the one defined
  (relative distances), and static embeddings only are tested.
---
<!-- inactive-ok-file: THEORY-159 THEORY-tmpx81wa — Proposed; neighbouring relational accounts of meaning, cited as open -->
<!-- inactive-ok-file: LIT-106 — Unavailable; Marabini on Brandom, a seeded skim, named and not leaned on -->
<!-- inactive-ok-file: LIT-208 — Proposed; the reading that sources this account, which is itself Proposed and says so -->

# THEORY-tmpf5mlz: If a word's meaning in a distributional model is read differentially, as its relations to its nearest neighbours rather than its coordinates, then adding text moves every similarity value slightly but leaves the neighbourhoods of frequent, consistently used words intact and shifts those of rare words that the new text uses heavily, so the instability that holism implies is local and graded rather than total

## Source

Grindrod, Porter and Hansen (2024), [LIT-208](../literature.d/LIT-208.md) (arXiv 2405.12084 v2; also a
chapter in Cappelen and Sterken (eds.), OUP, not read), read in full in
[NOTE-158](../notes.d/NOTE-158.md).

## What was actually shown

**The objection and the reply.** The instability objection to meaning
holism (Fodor and Lepore 1992; Pagin's "total change thesis") says any
change ripples through the system, so speaker and hearer never share
meanings. The paper takes holism as determination by relations (Dresner
2012), not priority, and reads meaning similarity off nearest neighbours,
which survive rotation and change of dimensionality and can be compared
across spaces, as in Hamilton et al. (2016). Fodor and Lepore's
dimension-selection objection lapses, since distributional dimensions are
not semantic properties (§4; C2, C3 moderate).

**Count model (§4, pp. 12–17).** A ±10-word window on Stein's *The Making
of Americans* (about 522k tokens). "know" has neighbours understand
0.95231, it 0.94286, see 0.93759, think 0.93293 (Table 4). After adding
Hemingway's "A Clean, Well-Lighted Place" (under 1,500 words) all ten
values move in the fourth or fifth decimal place (e.g. understand
0.95231 → 0.95284) and the order is unchanged (Table 6). "glass", 2 uses
in Stein and 5 in Hemingway, changes from chandeliers, prisms, brocade to
saucer, waiter, table (Table 5).

**Word2vec model (§4, pp. 18–20).** CBOW on 372,194 Wikipedia articles
(about 143M words), then with all 1,763 SEP articles added (about 21M
words). "atomism", 9 uses in Wikipedia and 662 in the SEP, reorders and
gains neighbours (Table 7). "can" keeps its neighbours, with values
changing by at most 0.003 and a swap at positions 9–10 (Table 8).

**The stronger thesis (§5).** The residual instability is a virtue: it
registers idiolect and diachronic change (C8, weak, by appeal to Hamilton
et al.).

**What could have come out otherwise.** "know" or "can" could have lost
neighbours under the addition, or "glass" and "atomism" could have kept
theirs. Neither happened in the one run shown.

## What this does not say

- **That resistance to change is proportional to frequency.** The
  abstract says "roughly proportional"; the body shows four words and one
  before-and-after pair per model (C6, weak). That models grow more stable
  with size rests on a citation to Antoniak and Mimno (2018), not on the
  authors' two corpus sizes (C7).
- **That the contrasts exceed seed noise.** The authors raise run-to-run
  randomness and report no repeated runs, so "can"'s swap at positions
  9–10 cannot be separated from noise.
- **That relative distances are preserved.** The definition of
  differential stability is relative distances, but the cosine values do
  change; what the tables show preserved is the ranked neighbour list.
  The paper does not reconcile the two ([NOTE-158](../notes.d/NOTE-158.md), Corrections).
- **That transformer models behave the same way.** Asserted (C10), with
  no experiment on contextual embeddings, where a word has no single
  neighbourhood.
- **That distributional models capture meaning, or what similarity
  suffices for communication.** The first is bracketed (§2). The second is
  answered informally, as graded success or an untested empirical
  threshold (C9).
- **Anything new for machine-learning practice.** Comparing embedding
  spaces by neighbour sets, and expecting rare words to be unstable, is
  already practice, with Antoniak and Mimno as its operational source.
  [NOTE-158](../notes.d/NOTE-158.md) recommends no anthology filing.

## Connections

- The paper acknowledges Brandom's inferentialism as a holist alternative
  and does not adopt it (fn. 15). Brandom's account of content as
  inferential role is [THEORY-tmpx81wa](THEORY-tmpx81wa.md); [LIT-106](../literature.d/LIT-106.md) (Marabini on Brandom) is
  read only in a seeded skim.
- Saussure's value fixed by relations among coexisting terms
  ([THEORY-159](THEORY-159.md)) is the structuralist form of the same relational view of
  meaning. This paper does not cite it, and no relation is declared.
