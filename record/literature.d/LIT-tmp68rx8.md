---
status: Active
status_note: 'read in part on 2026-09-26, alongside the nLab page it supersedes ([LIT-040](LIT-040.md)) — §1–3, §4.7 and §5 in full, §4.3–4.6 at the level of statements; no NOTE yet, so a full reading is still owed'
title: 'Two-Level Type Theory and Applications'
version: 1
tags:
- mathematics
date: '2026-09-26'
published: '2017-05-09'
arxiv: '1705.03307'
doi: '10.1017/S0960129523000130'
first_author: 'Annenkov'
keywords:
- 'two-level type theory'
- 'homotopy type theory'
- 'Reedy fibrations'
- 'semisimplicial types'
implementations: []
summary: >-
  Annenkov et al. (2017), [ARXIV-1705.03307](https://arxiv.org/abs/1705.03307); Mathematical Structures in
  Computer Science 2023. Two-level type theory (2LTT) pairs a fibrant inner
  theory (HoTT) with an outer theory with strict equality, so that coherence
  towers such as semisimplicial types can be stated internally. Basic 2LTT is
  conservative over HoTT (Props 2.18–2.19): an inner type inhabited in 2LTT
  is already inhabited in HoTT. A fibrant-replacement type former would force
  UIP on the inner level (Thm 2.20).
---

<!-- inactive-ok-file: LIT-040 — Superseded by this paper; named as the page this one replaces -->

# LIT-tmp68rx8: Two-Level Type Theory and Applications

Danil Annenkov, Paolo Capriotti, Nicolai Kraus & Christian Sattler (2017;
MSCS 2023) — [ARXIV-1705.03307](https://arxiv.org/abs/1705.03307)

## Key takeaways

- The reference presentation of two-level type theory: an inner, fibrant
  level where homotopy type theory holds and an outer level with strict
  equality, related by a fibrancy predicate.
- **Conservativity over HoTT (Props 2.18–2.19).** Results about inner types
  proved in basic 2LTT hold in HoTT. This answers, for basic 2LTT, the
  "open question" the nLab page ([LIT-040](LIT-040.md)) still records. A stronger,
  bijective conservativity is conjectured (§5), with an argument credited to
  Kovács 2022.
- **A limit (Thm 2.20).** Adding a fibrant-replacement type former forces
  uniqueness of identity proofs on the inner level.

## Standing in the record

Filed on 2026-09-26 as the successor to the nLab page "two-level type
theory" ([LIT-040](LIT-040.md)). That page's close reading found it an accurate but thin
gloss on this paper and its predecessor (arXiv 1604.03799), with no result,
argument or citation not traceable to them. The same reading read this paper
in part (above) to settle that. It is `Active` on that reading; a `Read` NOTE
is still owed, and until one exists its results are cited from its
statements, not from checked proofs. Riehl & Shulman's synthetic
∞-categories ([LIT-032](LIT-032.md)) names this approach as the alternative way to make
coherence towers internal to HoTT, and this paper names theirs.
