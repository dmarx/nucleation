---
status: Proposed
title: 'Recurrence is the nucleation threshold: coding a thing the second time it turns up captures exactly the drift that defeats an argument, and keeps capture from flooding the record'
version: 1
role: thesis
defeated_if: >-
  A record that codes on first occurrence, or only on request, shows
  less drift for the same filing cost. Or the drift turns out to sit
  mostly in things said only once, which a second-occurrence rule never
  codes.
tags:
- design-rationale
- epistemology
date: '2026-10-11'
line: nucleating-argument
works:
- luria-nucleating-an-argument
answers:
- QUESTION-tmpdj25c
rests_on:
- CLAIM-tmp4qgbo
grounds:
- LIT-tmplhx5f
summary: >-
  The filing rule of [ADR-032](../decisions.d/ADR-032.md) ("a thing gets a code the second time it
  turns up"), read as the mechanism the manuscript's title names. The
  same threshold appears in three places in luria and was found
  independently each time. Proposed: the rule has been applied, but no
  other threshold has been compared with it.
complements:
- CLAIM-tmp6b44r
- CLAIM-tmpvc1pj
objected_by:
- CLAIM-tmpas8q0
---
<!-- inactive-ok-file: CLAIM-017 — Superseded; cited as the history of a thesis or term, whose change is the point -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-tmp4qgbo CLAIM-tmpvc1pj — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->

# CLAIM-tmp2jolp: Recurrence is the nucleation threshold: coding a thing the second time it turns up captures exactly the drift that defeats an argument, and keeps capture from flooding the record

## The claim

[ADR-032](../decisions.d/ADR-032.md): "The drift the exchange shows is exactly the set of things that
recurred. When an agent does the filing, the risk is no longer that capture
stops but that it floods, and this rule is the throttle."

The rule does two jobs. Something said once cannot be redefined silently or
re-derived as though new. Every failure [CLAIM-tmp4qgbo](CLAIM-tmp4qgbo.md) lists needs a second
occurrence, so coding at the second occurrence catches each failure the
first time it could happen. It also leaves alone the many things that are
said once and never come back.

The code is the nucleation site. Once a thing is coded, later turns can
point at it rather than restate it. Restating is where redefinition creeps
in. Structure then forms on the code: `rests_on`, `objects_to`,
`supersedes`. The chains render that structure, so that "the thesis moved"
becomes something visible, [CLAIM-017](CLAIM-017.md) to [CLAIM-115](CLAIM-115.md), and no longer something a
reader has to notice.

Luria arrived at the same threshold separately, more than once:

- its design-principles layer has the test "have we re-derived this
  reasoning more than once?" ([LU-ADR-001](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-001.md));
- its working agreement says "One catch is the net working; the same catch
  twice means the hazard is upstream";
- [LU-DP-015](https://github.com/dmarx/luria/blob/main/docs/design-principles.md#dp-15) was written after a premise "had been re-derived four times
  without once being written down".

That convergence is itself an instance of the claim. The idea reached its
second occurrence across separate sessions, and this filing gives it a code.

## What it does not say

- It does not say a second occurrence is always enough. Some first
  occurrences are worth coding at once: a decision, or a source.
- It does not say the record should capture everything that recurs, for
  ever. Luria is named for a mnemonist whose total recall crowded out
  meaning ([LU-ADR-011](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-011.md)). Codes are retired by status, and a principle stands
  in for every instance of its argument.
- Whether "second" is the right number, or only a convenient one, has not
  been tested.

## Note of 2026-10-11: what the readings say about the threshold

Two works the claim's analogy draws on were read the same day, and neither
supports a threshold that is a count. In Ostwald 1897 ([NOTE-tmpn2e2e](../notes.d/NOTE-tmpn2e2e.md)) the
thresholds are a degree of supersaturation, past which the new phase forms
without a seed, and a minimum seed size. In Vekilov 2010 ([NOTE-tmpmm4u0](../notes.d/NOTE-tmpmm4u0.md))
the critical nucleus is a size, n* = 64Ω²α³/Δμ³, that falls as the driving
force rises and reaches one molecule at a solution–crystal spinodal. If the
analogy is kept, the number of occurrences that earns a code should depend
on how far the exchange is from settling, and at the fast end
([CLAIM-tmpvc1pj](CLAIM-tmpvc1pj.md)) a first occurrence may be enough. A nucleus is also only a
point of even odds of growth and decay, so a code at the threshold gives a
thing an even chance of persisting, no more. None of this tests the
filing rule itself. It narrows what the physics can be cited for.
