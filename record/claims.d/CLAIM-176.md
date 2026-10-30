---
number: 176
status: Proposed
formerly:
- CLAIM-tmp2jolp
title: 'Recurrence is the trigger of persistence this record is built around: coding a thing the second time it turns up captures exactly the drift that defeats an argument, and keeps capture from flooding the record'
version: 4
history:
- version: 2
  date: '2026-10-11'
  note: >-
    Narrowed on the owner's reframing (CLAIM-185). Version 1 called
    recurrence the nucleation threshold. The threshold is whatever
    triggers persistence, and recurrence is one trigger, the one this
    record is built around. The claim keeps recurrence's particular
    case: it catches exactly the drift and throttles capture.
- version: 3
  date: '2026-10-14'
  note: >-
    After the reading of LIT-787 (NOTE-851). A Connections line adds
    Ashby's recurrent-situation chapter: separate stores keyed to the
    situation, with interference growing with similarity. The claim is
    unchanged.
- version: 4
  date: '2026-10-30'
  note: >-
    The twentieth status review (ADR-058; an unread work takes no edge),
    at the status review's ruling (the owner delegated these rulings).
    LIT-924, De Yoreo and Vekilov's review, Unavailable and read by no
    NOTE, leaves grounds. The body never cites it: the claim stands on
    ADR-032's rule and on CLAIM-177 and CLAIM-483, and the note of
    2026-10-11 records that the two nucleation works since read
    (NOTE-708, NOTE-709) do not support a threshold that is a count. The
    text is unchanged.
role: thesis
warrant: interpretive
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
- QUESTION-037
rests_on:
- CLAIM-185
- CLAIM-177
- CLAIM-483
summary: >-
  The filing rule of [ADR-032](../decisions.d/ADR-032.md) ("a thing gets a code the second time it
  turns up"), read as one trigger of persistence ([CLAIM-185](CLAIM-185.md)), and
  the one this record is built around. Narrowed to that on 2026-10-11,
  on the owner's reframing. The
  same threshold appears in three places in luria and was found
  independently each time. Proposed: the rule has been applied, but no
  other threshold has been compared with it.
complements:
- CLAIM-179
- CLAIM-186
objected_by:
- CLAIM-181
---
<!-- inactive-ok-file: CLAIM-483 — Proposed; the comparative premise split from CLAIM-177 on 2026-10-27 -->
<!-- inactive-ok-file: THEORY-307 — Proposed; the account filed from LIT-787, named in Connections and not leaned on -->
<!-- inactive-ok-file: CLAIM-185 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->
<!-- inactive-ok-file: CLAIM-017 — Superseded; cited as the history of a thesis or term, whose change is the point -->
<!-- inactive-ok-file: CLAIM-115 CLAIM-186 — Proposed; open, and cited as open: the theses and objections of the nucleating-argument line are under test, not settled -->

# CLAIM-176: Recurrence is the trigger of persistence this record is built around: coding a thing the second time it turns up captures exactly the drift that defeats an argument, and keeps capture from flooding the record

## The claim

*Version 2.* What the title of the manuscript names is the threshold at
which a structure persists and becomes an anchor ([CLAIM-185](CLAIM-185.md)).
Recurrence is the trigger this record is built around, and this claim is
about why it is a good one for drift. Other triggers (a choice, a source, a
request) make things persist too, without its throttle.

[ADR-032](../decisions.d/ADR-032.md): "The drift the exchange shows is exactly the set of things that
recurred. When an agent does the filing, the risk is no longer that capture
stops but that it floods, and this rule is the throttle."

The rule does two jobs. Something said once cannot be redefined silently or
re-derived as though new. Every failure [CLAIM-177](CLAIM-177.md) lists needs a second
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
supports a threshold that is a count. In Ostwald 1897 ([NOTE-709](../notes.d/NOTE-709.md)) the
thresholds are a degree of supersaturation, past which the new phase forms
without a seed, and a minimum seed size. In Vekilov 2010 ([NOTE-708](../notes.d/NOTE-708.md))
the critical nucleus is a size, n* = 64Ω²α³/Δμ³, that falls as the driving
force rises and reaches one molecule at a solution–crystal spinodal. If the
analogy is kept, the number of occurrences that earns a code should depend
on how far the exchange is from settling, and at the fast end
([CLAIM-186](CLAIM-186.md)) a first occurrence may be enough. A nucleus is also only a
point of even odds of growth and decay, so a code at the threshold gives a
thing an even chance of persisting, no more. None of this tests the
filing rule itself. It narrows what the physics can be cited for.

The owner's reframing the same day ([CLAIM-185](CLAIM-185.md)) answers this by moving
the threshold from the count to persistence, which is how the physics
defines it. This claim was narrowed to match.

## Connections

- Ashby ([LIT-787](../literature.d/LIT-787.md), Ch. 10; [THEORY-307](../theory.d/THEORY-307.md), read in [NOTE-851](../notes.d/NOTE-851.md)): the
  benefit of a recurrent situation is that the second response can be
  immediate, and that needs a separate store for the situation, selected
  by the situation itself; interference between stores grows with the
  similarity of the situations. Ashby does not say recurrence should
  trigger capture. He says what a system must have for recurrence to be
  exploited. Analogy only.

## Note of 2026-10-27: a second premise

The status review of this date ([ADR-057](../decisions.d/ADR-057.md)) split [CLAIM-177](CLAIM-177.md). Its observed
half stays [CLAIM-177](CLAIM-177.md), which is now Active. Its comparative half,
[CLAIM-483](CLAIM-483.md), is Proposed. This claim's "exactly the drift that defeats
an argument" needs the comparative half, that identity drift and not
missing structure is what defeats such an argument, so it now rests on
both.

## Note of 2026-10-30: what holds it back

Two premises are Proposed: CLAIM-185, which waits on CASE-183's inbound
references per code, and CLAIM-483, whose comparison was counted in one
exchange. The comparison its defeat condition names has not been made: no
record that codes on first occurrence or only on request has had its drift
and filing cost set beside this one's, so whether "second" is the right
number is untested. CLAIM-181's objection, that the grammar a coded thing is
filed in shapes it, is unanswered.
