# LEAD-014 pilot: scoring codebook

Fixed 2026-11-22, before any replay was run.

## Units of an accounting

Every accounting (the replay's, the filing's, and the corrections') is
reduced to a list of **items**, each of one of four types:

- **W (work registered or mapped)**: a work the source cites, with its
  disposition: held (with code), to register, or left (with reason).
- **C (claim or idea)**: an idea, construction, distinction, proposal,
  question or argument the source states, with its disposition: held
  (code), to file (with the kind of entry: CLAIM, QUESTION, CASE, TERM,
  ARG, LEAD, THEORY, NOTE paragraph), or left (reason).
- **G (gap named)**: a gap in the source's own argument (ADR-137): an
  unstated premise, an unchecked number, a test without a design, a wrong
  attribution.
- **R (relation)**: a stated link from source content to a held entry that
  the accounting asserts (supports, qualifies, objects to, bears on,
  duplicates), beyond the plain "held as X" mapping of a C or W item.

Dispositions of the items do not split them: an item is one unit whatever
it was disposed as.

## Ground-truth sets

- **F (filed)**: the items of the filing itself: its curation entry's
  "held", "filed", "left" and "gaps" parts, plus entries the filing commit
  added that the curation entry omits.
- **K (corrections)**: items that later corrections added: works
  registered later from the same source, ideas filed later as missed,
  gaps or duplicates later named, and corrections of a disposition (e.g.
  "left" that should have been "filed").
- **U = F ∪ K.**

## Matching rules

1. A replay item **matches** a ground-truth item when both name the same
   work (same identifier, or same title and first author), or the same
   idea at the same grain: a reader of both would say they are the same
   point. Wording need not agree.
2. **Grain.** If the replay splits one ground-truth item into several, the
   first counts as the match and the rest are scored as extras (not
   penalised in recall, counted in "extra"). If the replay merges several
   ground-truth items into one, it matches one; the others are misses,
   unless the merged item names each explicitly.
3. **Disposition** is scored separately: a matched item agrees in
   disposition when both say held (same code, or a code the record at the
   parent commit shows holds the same thing), both say file, or both say
   left. A replay "to file" against a ground-truth "held" is a
   **duplicate**.
4. **Voice.** A matched C item whose attribution differs (owner vs source
   assistant vs filer) is a **misattribution**.
5. Relations (R) match only when both ends match.
6. Items of K that correct F (a disposition change) count as matched when
   the replay gives the corrected disposition.
7. Scoring is done item by item in `scores/<case>.md`, with a one-line
   reason for each match judgement.

## Measures

For each replay and pooled:

- **Recall vs F**: matched F items / |F|, overall and per type.
- **Recall vs K**: matched K items / |K| — the question the study asks:
  would the replay have caught what the filing missed?
- **Extra**: replay items in neither F nor K, sorted after checking into
  (a) genuine finds: real content of the source that no accounting held,
  checked against the source text; (b) noise: wrong, duplicate or of no
  content.
- **Duplicates** and **misattributions** as counts.
- **Disposition agreement** on matched items.

## Blinding

The scorer is the assistant who ran the pilot. Before reading a filing's
curation entry and later corrections, the scorer freezes the replay's
item list (`accountings/<case>.md`) and its reduction to items. The
reduction of F and K is made after, so the scorer knows the replay when
reading the ground truth: this is not blind, and the scores say so.
