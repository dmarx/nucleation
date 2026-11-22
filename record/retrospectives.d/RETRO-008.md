---
number: 8
status: Accepted
formerly:
- RETRO-tmpd00ym
title: "The filing of Rich Get Richer Power Laws and the evening after: an exchange, eight readings, a manuscript refresh and two decisions on how the record files, in five pull requests; what went right was separate readers checking the drafters' work and the owner's corrections becoming rules the same evening, and what went wrong was the assistant settling for one reading, one framing or one file where the owner wanted all of them"
version: 2
history:
- version: 2
  date: '2026-11-21'
  note: >-
    Accepted at the owner's "adopt" of 2026-11-21. The recommendations
    became ADR-140 (1 and 5) and ADR-139 (2 to 4).
tags:
- record
date: '2026-11-21'
reviews:
- ADR-068
- ADR-054
- ADR-061
- ADR-071
- ADR-108
- ADR-121
- ADR-126
- ADR-127
- ADR-128
- ADR-137
- ADR-136
prompted:
- ADR-140
- ADR-139
pull_requests:
- https://github.com/dmarx/nucleation/pull/608
- https://github.com/dmarx/nucleation/pull/609
- https://github.com/dmarx/nucleation/pull/610
- https://github.com/dmarx/nucleation/pull/611
- https://github.com/dmarx/nucleation/pull/612
discussions:
- https://claude.ai/code/session_01HcmtbsHCnWAcGaecC7H4Pn
summary: >-
  At the owner's request ("retro"), on 2026-11-21, after the stretch that
  began with "update the record to account for this discussion, including
  attempting to fill in gaps where you identify them" for the exchange
  "Rich Get Richer Power Laws". The stretch went:
  - the share decoder fixed (pull request 608);
  - the exchange filed, with its gaps, its first eight readings and a
    refresh of the manuscript and its neighbourhood (pull request 609);
  - two decisions on how the record files, gap filling ([ADR-137](../decisions.d/ADR-137.md),
    Proposed) and argument titles ([ADR-136](../decisions.d/ADR-136.md), Active), with a sweep of
    the record's Rejected arguments (pull requests 611 and 612).
  Going well: separate readers checked the drafters' work, and caught
  what the drafters' own reports could not (voice drift, missing
  arguments, misattributed sources, errors in the assistant's own
  entries). Numerical checks caught errors in the other assistant's
  turns. Each of the owner's corrections became a rule the same evening.
  Going wrong: four times the owner caught the assistant settling for
  less than the record wanted. The decoder dropped content; the assistant
  asked which reading was meant instead of filing all three; arguments
  were titled with their conclusions; and a Rejected argument's
  conclusions were left without an entry. Smaller faults came from the
  shared working tree and from writing about work still in flight. And,
  at the owner's earmark, the exchange the regime is named for happened
  mostly off the page, in briefs, commits and pull requests. Five
  recommendations follow, the fifth to think out loud in the chat with
  periodic executive summaries. The review is the assistant's (Claude, in this
  session); adopting its recommendations is the owner's call.
---
<!-- inactive-ok-file: ADR-138 CLAIM-812 CLAIM-801 CLAIM-819 — Proposed, Rejected or new; the entries this review names -->

# RETRO-008: The filing of Rich Get Richer Power Laws and the evening after: an exchange, eight readings, a manuscript refresh and two decisions on how the record files, in five pull requests; what went right was separate readers checking the drafters' work and the owner's corrections becoming rules the same evening, and what went wrong was the assistant settling for one reading, one framing or one file where the owner wanted all of them

## What it covers

From the owner's request of 2026-11-21, about 16:50 UTC, to file the exchange "Rich Get Richer Power Laws" (27 owner turns, 43 visible assistant turns), to the sweep of the Rejected arguments at about 22:20. The devlog notes it reads are those of 2026-11-21 at 18:29:55 (asking instead of filing alternatives) and 21:27:15 (arguments titled with their conclusions), with the earlier note of 07:01:19 (resolving a conflict with `--ours`), whose lesson recurred. It also answers the owner's earmarked note of 22:30:41 ([ADR-126](../decisions.d/ADR-126.md)), added after the review was first filed.

| Pull request | What it did |
|---|---|
| 608 | The share decoder kept all the assistant's content, after the owner asked why 96 assistant turns became 43 |
| 609 | The exchange: 51 works, 92 entries, two part accounts; [ADR-137](../decisions.d/ADR-137.md); terms for "sloppy" and "separation"; eight readings with three supplements; the manuscript and its neighbourhood, fact-checked |
| 610 | The promotion pull request, kept in marked sections ([ADR-128](../decisions.d/ADR-128.md)) |
| 611 | [ADR-136](../decisions.d/ADR-136.md) (Active) and [ADR-138](../decisions.d/ADR-138.md) (Rejected); the five arguments of the day retitled; [CLAIM-801](../claims.d/CLAIM-801.md), [CLAIM-819](../claims.d/CLAIM-819.md) |
| 612 | The sweep of 35 older Rejected arguments; two questions and a case for conclusions with no entry; one question from a review of all 37 |

## What went well, and why

- **Separate readers caught what the drafters' reports could not.** Five drafters filed the exchange by theme. Then a coverage reread and a synthesis audit, each by a reader briefed only with the source and the files, found the following:
  - three owner entries told in the other assistant's framing (U18, U23, U25);
  - two missed ideas, and six contested support judgements with no argument;
  - the other assistant's closing syntheses telling the owner's ideas as its own.

  None of this was in the drafters' reports, because a drafter reports what it filed, not what it framed wrongly. This is read-and-file step 10's rule ("Agents' reports say what they filed, not what they were never asked to file") working as intended. The manuscript refresh got the same treatment: a fact-checker found seven errors and reproduced every figure.
- **Readers of the cited works corrected the record's own entries.** The readings found an inverted formula in [CLAIM-812](../claims.d/CLAIM-812.md) (widths go as √λ, not 1/√λ) and a wrong inverse temperature. They found that BBP covers only complex Gaussian data, so the spectral entries rested on three other papers. And they found that a capacity bound needs fewer conditions than the record had said. Each became an argument for a work that carried less than it was cited for.
- **Checking the numbers caught the other assistant's errors.** Every drafter computed what it filed, with `python3 -I`. That caught eight errors in the other assistant's turns: wrong chart values, a wrong delay formula, a misattributed author, a table that says "three" and lists four. Without the checks they would have entered the record as the source's word.
- **Each of the owner's corrections became a rule the same evening.**
  - "Attempting to fill in gaps" became [ADR-137](../decisions.d/ADR-137.md), with the skill's step 9a.
  - The objection to an argument titled with its conclusion became [ADR-136](../decisions.d/ADR-136.md), filed with an alternative, adopted at "go with your lean" and swept through the 35 older arguments.
- **A question review that found almost nothing, usefully.** A review of all 37 Rejected arguments found one undocumented question. The rest are held as open hypotheses by Proposed claims. That is evidence the record keeps its open questions in claims more than in QUESTION entries, which the owner may want to know when looking for what is open.

## What did not go well

- **Four times, the owner caught the assistant settling for less.**
  1. *The decoder* kept the visible turns and dropped code output and uncounted hidden content. The owner caught it from a turn count: "I'm concerned your bespoke decoder might be throwing away content."
  2. *Separability.* The assistant found three senses and then asked which was meant, filing the substantive note for one. CLAUDE.md says to file each reading (devlog, 18:29:55). The owner: "err on the side of adding richness to the record."
  3. *Argument titles.* The assistant titled five Rejected arguments with their conclusions. It then framed the owner's choice as "keep Rejected, or state the failure as a claim", which missed that the conclusion was what was at risk (devlog, 21:27:15).
  4. *Untouched conclusions.* The sweep's drafters, following the assistant's brief, set aside three conclusions with no entry "for the owner", where the decision just adopted said to hold them. The owner: "they don't look useless."

  The common pattern is not a missing rule; in cases 2 and 4 the rule existed. It is a reach for the smallest thing that answers the question asked, where the record's conventions ask for the fullest thing the material supports.
- **The shared working tree.** Five drafters, then two filers and two writers, worked in one checkout:
  - A commit of the assistant's own files took in a filer's uncommitted note (28ec330cf).
  - CI's repairs, pulled in mid-work, conflicted with files still being edited, three times. Each was resolved with `--ours` after reading the conflict, but that is the practice the devlog of 07:01:19 warned about, where it reverted three of the owner's rulings.
- **Writing about work still in flight.** The manuscript's Part I was refreshed while the readings were still being filed. It cited works as "being read" that had landed before the writer finished, which the fact-check caught. The writer had been told to say "being read" for such works, so it did what it was told; the ordering was the fault.
- **A chained command that did not gate on its script.** An edit script failed on a line wrap, and the commit in the same shell call went ahead without the edit. The next turn caught it.
- **The exchange happened off the page** (the owner's earmark, devlog of 22:30:41). The regime is called dialectic "to evoke exchanging ideas", and the owner wants "an opportunity to monitor your activity" in the chat. Most of the assistant's turns did otherwise:
  - they announced that delegated work had started, then reported its outcome in a closing "Filed" block;
  - the reasoning that decided what to file lived in drafters' briefs, commit messages and pull-request descriptions.

  The rule, answer first and end with a Filed block ([ADR-127](../decisions.d/ADR-127.md)), was met. But a Filed block is a receipt, not a conversation. The owner could follow the reasoning only through GitHub, "which isn't super convenient". Three of the four corrections above came when the owner happened to read the result, not when the reasoning was laid out in front of them. Laid out in time, they might have come before anything was filed.
- **Mechanical slips CI caught:** LEADs in an account's `integrates` (red once); "about forty" gaps filled where the curation entry listed 54.

## Recommendations

1. **When a turn admits several readings, file them all and lean afterward.** This is CLAUDE.md's rule, and it was missed twice in one evening. The remedy proposed is a habit, not a rule: before any turn that ends in a question to the owner about what they meant, check whether filing each reading would answer it better. A brief for drafters says the same in its opening lines.
2. **In a shared tree, commit only the files each worker lists.** Never use `git add -A` or a directory while another worker is writing, and pull CI's repair only between workers, not under them. A worker's brief asks it to list its files, as the filers did (`mine.txt`).
3. **Sequence writers after the work they describe, or schedule a code pass.** A writer whose material is still being filed should either wait, or be followed by a pass that replaces "being read" with codes. That pass should not be left to the fact-check to find.
4. **Gate every commit on the edit before it.** Use one script that edits and checks, then commit only if it succeeded (`set -e`, or `&&` across the whole chain).
5. **Think out loud in the chat, and check in with an executive summary.** The owner's earmark.
   - **Before or while filing**, the assistant says in the conversation what it is about to file and why: the readings it sees, which entry kind it chooses, its lean, and what it is leaving out. The Filed block then confirms what the owner has already seen proposed.
   - **When delegated work returns**, the assistant relays the substance of what was found and decided, not only the codes.
   - **At the close of each batch, or after a long stretch of filing**, it gives a short executive summary: what changed in the record's argument, what waits on the owner, and what it would do next.
   - **The staging and promotion pull requests stay the place to intervene,** not the place to follow along. This is a change in how the dialectic regime is conducted, so a decision amending [ADR-127](../decisions.d/ADR-127.md)'s practice is the natural home once the owner rules on it.

[ADR-137](../decisions.d/ADR-137.md) (gap filling) waits on the owner's adoption and is not reviewed here beyond its first application, which went well. The four corrections in "What did not go well" each came from the owner; the separate readers caught everything else.

## The owner's responses, 2026-11-21

The owner: "adopt". The assistant read it as covering both things then waiting on the owner: this review with its five recommendations, and [ADR-137](../decisions.d/ADR-137.md). Both were taken ([ADR-140](../decisions.d/ADR-140.md), its first rule).

- **1 and 5:** adopted as [ADR-140](../decisions.d/ADR-140.md), conduct in the dialectic regime: think out loud, relay findings, executive summaries, and file every reading before asking.
- **2, 3 and 4:** adopted as [ADR-139](../decisions.d/ADR-139.md), parallel filing in one working tree.
- **[ADR-137](../decisions.d/ADR-137.md):** Active.


## What it does not say

- That parallel drafting should stop. It made a 646 KB source fileable in an evening, and the separate readers made it safe.
- That the four misses share one cause the assistant can remove by rule. Two of them already had rules.
