---
status: Proposed
title: "A synthesis states its scope's argument as one argument, not an inventory of its components; an exchange is taken into account by revising the syntheses of the lines it advanced; and a manuscript argues for its reader, with the record's apparatus in its README"
version: 1
tags:
- record
date: '2026-11-25'
# frontmatter is data and stays plain.
summary: >-
  At the owner's word of 2026-11-25: "an 'account' of a discussion should
  not be a play-by play. it should be updating the nucleation record to
  *take into account* the progress that was made in the conversation.
  synthesis 'accounts' suffer a same issue. listing items is not a
  synthesis of them", and "maybe the word choice of 'synthesis' or
  'account' is a source of confusion". The scheme had taken "account" in
  its bookkeeping sense, an itemized statement, and its syntheses had
  become inventories: each component with its status, voice and a
  quotation. Now a SYNTHESIS states its scope's argument as one argument,
  in prose, in the order its steps depend on each other, citing its
  components where it uses them; the inventory is the data the entries
  carry and the generated views render, and is not restated. "Account"
  is kept only in the sense of an explanation. An exchange gets no
  synthesis of its own: its filing ends by revising the syntheses of the
  lines it advanced, so that they take its progress into account, and the
  curation entry keeps the map of turns. A manuscript argues for a reader
  outside the record, citing codes in parentheses, with standings, voices
  and provenance in its README. Rejected: renaming the scheme, since its
  code and entries stay; and keeping the inventory beside the prose, which
  is a hand-kept projection of what the entries already say (DP-003).
---

# ADR-tmpw306d: A synthesis states its scope's argument as one argument, not an inventory of its components; an exchange is taken into account by revising the syntheses of the lines it advanced; and a manuscript argues for its reader, with the record's apparatus in its README

<!-- inactive-ok-file: SYNTHESIS-114 SYNTHESIS-122 SYNTHESIS-100 SYNTHESIS-tmp4tvbr — Proposed; the syntheses this decision rewrites or retires -->

## Context

ADR-084 made a SYNTHESIS "an account of a scope of the record's argument"
that "asserts nothing of its own", with every component in `integrates`
and each link attributed to the entry that states it. ADR-083 gave each
scope one. In practice the word "account" was read in its bookkeeping
sense. Syntheses became inventories: SYNTHESIS-114, for example, lists
its components one by one, each with status, voice, role and a quotation,
and then a section of notes listing more. The read-and-file skill filed an
account of each exchange (SYNTHESIS-100, SYNTHESIS-122,
SYNTHESIS-tmp4tvbr), which retell the exchange turn by turn. The
write-manuscript skill asked every step of a draft to cite its entry
"with its standing", and the drafts read as audits of the record:
governance-of-possibility opens each part with what it rests on and who
made it so.

On 2026-11-25 the owner ruled that this is the wrong kind of object, in all
three places, and that the words may be the source of the confusion.

## Decision

- **Words.** A synthesis is the integration of parts into one argument.
  "Account" is used only in the sense of an explanation, an account of
  something; never a ledger. The SYNTHESIS scheme's description and the
  skills are reworded to match. The scheme's code and entries stay.
- **What a synthesis says.** Its body states, in prose:
  - the scope's question;
  - the argument that answers it, in the order its steps depend on each
    other, each step citing in parentheses the entry that holds it;
  - where the argument is firm and where it is open, said where it
    matters, not item by item;
  - what the components do not establish: a link no entry states is filed
    as a claim when it passes ADR-075's test, or named as open.

  It still adds nothing (ADR-084): a step no component holds is not
  asserted by the synthesis. Its `integrates` field is the list of
  components. Their statuses and voices are in their own entries and the
  generated views; the body does not restate them, and names a voice only
  where the argument turns on whose a step is.
- **Exchanges.** An exchange gets no synthesis of its own. Its filing ends
  by revising the syntheses of the lines it advanced, as new versions, so
  that they take its progress into account. The map of turns to codes
  stays in the curation entry. The exchange syntheses held (SYNTHESIS-100,
  SYNTHESIS-122, SYNTHESIS-tmp4tvbr) are Superseded as their lines'
  syntheses are revised.
- **Manuscripts.** A draft argues for its thesis to a reader outside the
  record. Its steps cite the entries that hold them, in parentheses, as
  the owner asked of the hyperarticle drafts (U20 of "Hyper article
  interpretation"). Standings, voices, provenance, reviews and the
  record's process go in the README and a short note on method, not in the
  argument. The draft still keeps its scope conditions, and its joins
  still go back to the record (the write-manuscript skill, step 6).

## Consequences

- The synthesis-review, read-and-file and write-manuscript skills change
  in this pull request, with the scheme's description in luria.yaml.
- First applications, in this pull request:
  - SYNTHESIS-114 is rewritten as a synthesis, as a new version;
  - the line scholarly-publishing gets its first synthesis, which takes
    the exchange "Hyper article interpretation" into account (the exchange
    has no synthesis of its own);
  - governance-of-possibility's Part A is rewritten as a manuscript.
- Sweeps follow in pull requests of their own: the remaining syntheses,
  line by line; the exchange syntheses, as their lines are revised; and
  the other manuscript drafts.
