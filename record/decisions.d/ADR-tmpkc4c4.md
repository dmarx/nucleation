---
status: Active
title: 'Titles are addresses; statements hold the assertion'
version: 1
tags:
- record
date: '2026-11-25'
summary: >-
  An entry's title is a short label that addresses it, 30 to 50 characters
  as a target, with no code in it. It is an address first and a distillation
  second. The full assertion the title used to carry moves, verbatim, to a
  new `statement:` field on CLAIM, THEORY, ARG, SYNTHESIS, CASE and TERM. The rules that said a title must assert something ([ADR-065](ADR-065.md),
  [ADR-075](ADR-075.md), [ADR-136](ADR-136.md), [ADR-138](ADR-138.md)) now apply to the statement. Moving a title into
  `statement:` changes no claim, so it takes no version bump under [ADR-120](ADR-120.md).
  TERMs are retitled first. Rejected: keeping sentence titles and deriving
  labels for graphs, and shortening titles without keeping the assertion.
---

# ADR-tmpkc4c4: Titles are addresses; statements hold the assertion

## Context

The record's own entries carry sentence titles. On 2026-11-25 their median
lengths were 82 words for SYNTHESIS, 60 for THEORY, 55 for CLAIM, 43 for
CASE, 38 for ARG and 27 for TERM. Nearly all of them ran past 15 words. LIT and NOTE titles,
which are the works' own titles, had medians of 8 and 9 words.

The long titles follow rules, not drift. [ADR-065](ADR-065.md) has a reading's
`promote_when` ask for what its title asserts. [ADR-075](ADR-075.md) has a synthesis
title state its integrating claim. [ADR-136](ADR-136.md) and [ADR-138](ADR-138.md) have an
argument's title state its route, its grounds and the record's verdict.

The cost is that a title cannot address anything. The owner wants to
draw the record's argument graphs with dmarx/strata-g, which labels each
node with its title. A 60-word sentence is useless as a node label, and so
is an index row or a search card that wraps for six lines. The owner put it as follows: "A
title should generally be an address first and a distillation second."

The owner also asked that the code not be repeated in a title. No frontmatter
title on the record contains its own code; the repetition is luria's, which
writes `# CODE: title` as each body heading and names each site page
`CODE: title`. That is taken upstream as dmarx/luria#405 and is not decided
here.

## Decision

- **A title is an address.** It names the entry so that a reader, a graph or
  an index can point at it. Target 30 to 50 characters, and as short as
  identifies the entry. It contains no code. It may distil the entry, but
  only as far as the length allows.
- **The assertion moves to `statement:`.** CLAIM, THEORY, ARG, SYNTHESIS,
  CASE and TERM may carry a `statement:` field. When an entry is
  retitled under this decision, its old title is moved to `statement:`
  verbatim. A new entry states its assertion there and gives a short title.
- **Rules about what a title asserts now apply to the statement.** Where
  [ADR-065](ADR-065.md), [ADR-075](ADR-075.md), [ADR-136](ADR-136.md) and [ADR-138](ADR-138.md) speak of a title stating
  or asserting something, read "statement". An entry with no statement yet is
  read as before, from its title.
- **Moving a title to `statement:` is not a change of claim.** The assertion
  is kept word for word, so the move takes no version bump and no history
  note under [ADR-120](ADR-120.md). Changing a statement's wording is a change of claim,
  and does.
- **Titles stay distinct.** Where several entries share a name, a short
  parenthetical says which: `fidelity (inferential sufficiency)`.
- **First application: TERMs.** Each TERM is retitled with the term itself, and a sense in
  parentheses where several TERMs share the term. The schemes then follow
  one at a time, each in its own pull request, with a sample reviewed before
  the bulk.

## Alternatives considered

- **Keep sentence titles and derive labels** (first clause, truncation, or a
  separate `label:` field for graphs). Truncation makes poor labels, and a
  separate label field leaves the title doing neither job well. The index,
  search and graph would each pick one or the other.
- **Shorten titles and let the body hold the assertion.** No config change is
  needed. But nothing machine-readable would then hold the exact assertion that
  [ADR-065](ADR-065.md) and [ADR-138](ADR-138.md) test against, and the chain views would have
  nothing to show but labels.
- **Status quo.** The graph view stays unusable and the indexes stay hard to
  scan.

## Consequences

- Indexes, graphs and search cards become scannable. A reader who needs the
  assertion reads the statement, which the page shows in its properties.
- Views that render titles as prose, such as argument chains ("From …"),
  will read as lists of labels until they render `statement:`. That is a
  follow-up for luria's chain views. Until then the chains are less
  self-explanatory.
- About 7,000 entries in five schemes remain to be retitled after TERM. Each
  sweep is its own pull request.
- `luria new` does not yet scaffold `statement:`. A filer adds it by hand
  until it does.
- `statement:` is not declared in `luria.yaml`. Luria 1.11 refuses a field
  declared without a constraint (a vocabulary, `required`, `many`, `unique`
  and the like), and an optional prose field has none. So, like `summary:`,
  it is an undeclared key, and `docs/record.md` does not list it. Letting
  luria declare a field for its label and blurb alone is an upstream
  question.
