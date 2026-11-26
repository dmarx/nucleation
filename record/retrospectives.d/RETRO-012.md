---
number: 12
status: Draft
formerly:
- RETRO-tmpd9oti
title: 'The retitle batch, 2026-11-25'
tags:
- record
date: '2026-11-25'
reviews:
- ADR-148
- ADR-065
- ADR-116
- ADR-125
pull_requests:
- https://github.com/dmarx/nucleation/pull/818
- https://github.com/dmarx/nucleation/pull/819
- https://github.com/dmarx/nucleation/pull/820
- https://github.com/dmarx/nucleation/pull/821
- https://github.com/dmarx/nucleation/pull/822
- https://github.com/dmarx/nucleation/pull/824
- https://github.com/dmarx/nucleation/pull/825
- https://github.com/dmarx/nucleation/pull/826
- https://github.com/dmarx/nucleation/pull/827
- https://github.com/dmarx/nucleation/pull/828
- https://github.com/dmarx/nucleation/pull/829
- https://github.com/dmarx/nucleation/pull/830
- https://github.com/dmarx/nucleation/pull/831
- https://github.com/dmarx/nucleation/pull/832
- https://github.com/dmarx/nucleation/pull/833
discussions:
- https://claude.ai/code/session_01Hcmtbsh1GUyNjm1fyU9KRX
summary: >-
  At the owner's word of 2026-11-25 ("add a retro to that PR"). It reviews
  the assistant's retitling of about 4,700 entries in six schemes under
  [ADR-148](../decisions.d/ADR-148.md), with [DP-007](../../docs/design-principles.md#dp-7)'s sample-first rule, and the promotion that followed.
  What went well: samples caught a wrong form twice before any bulk run,
  every old title was kept verbatim in `statement:`, and checks across a
  whole scheme caught what parallel drafters could not see. What went
  wrong: an untyped field broke luria for the whole branch, drafters
  reused approved examples as labels, a squash-merged back-merge left
  staging and main diverged, and report-and-thesis pairs were misread as
  duplicates. It recommends briefs that mark examples as taken,
  merge commits for back-merges, moving the carry of concretized codes into
  luria, and checking relations before calling entries duplicates.
---

# RETRO-012: The retitle batch, 2026-11-25

## What it covers

One session's work, 2026-11-25, from the owner's "titles across the record
need work" to the promotion of the result:

- **The rule.** [ADR-148](../decisions.d/ADR-148.md) (filed as [ADR-148](../decisions.d/ADR-148.md), [#818](https://github.com/dmarx/nucleation/issues/818)): a title is an
  address, 50 characters as a ceiling, with the assertion moved verbatim
  into `statement:`. The code repeated in headings and page titles went
  upstream as dmarx/luria#405.
- **The method.** [DP-007](../../docs/design-principles.md#dp-7), pilot a change on a sample before sweeping ([#819](https://github.com/dmarx/nucleation/issues/819)),
  distilled at the owner's word from [ADR-043](../decisions.d/ADR-043.md), [ADR-044](../decisions.d/ADR-044.md), [ADR-056](../decisions.d/ADR-056.md) and
  [RETRO-010](RETRO-010.md).
- **The sweeps.** TERM (162 retitled), CASE (427: [#819](https://github.com/dmarx/nucleation/issues/819), [#820](https://github.com/dmarx/nucleation/issues/820)), CLAIM (1,346:
  [#821](https://github.com/dmarx/nucleation/issues/821), [#822](https://github.com/dmarx/nucleation/issues/822)), ARG (260: [#824](https://github.com/dmarx/nucleation/issues/824), [#825](https://github.com/dmarx/nucleation/issues/825)), THEORY (2,310: [#826](https://github.com/dmarx/nucleation/issues/826), [#827](https://github.com/dmarx/nucleation/issues/827)) and SYNTHESIS
  (126: [#829](https://github.com/dmarx/nucleation/issues/829), [#830](https://github.com/dmarx/nucleation/issues/830)). A second CLAIM pass in the THEORY form was sampled and
  closed unmerged at the owner's "close enough" ([#828](https://github.com/dmarx/nucleation/issues/828)).
- **The promotion.** 165 conflicts between the concretized batch on main and
  the retitles on staging ([#831](https://github.com/dmarx/nucleation/issues/831)), a squash merge that undid the fix, and its
  repair through a branch `staging2` ([#832](https://github.com/dmarx/nucleation/issues/832)).
- **A misreading.** 67 THEORY pairs reported as duplicates that were
  [ADR-065](../decisions.d/ADR-065.md)'s reports and their theses ([#833](https://github.com/dmarx/nucleation/issues/833)).

## What went well, and why

1. **The samples caught a wrong form twice, cheaply.** The THEORY sample led
   each label with its source ("Zhuk: the CSP dichotomy"); the owner's "the
   source prefix… is just taking up space" changed 25 labels instead of
   2,310. The CLAIM redo was judged on 40 entries and dropped as not worth
   1,300 more. Both are [DP-007](../../docs/design-principles.md#dp-7) doing what it was written for, and both
   came from the owner reading a table in the pull request, not a description
   of the rule.
2. **Nothing was lost, so everything was reversible.** Every old title went
   verbatim into `statement:` by a script that re-parsed each file and
   compared the result with the original. A wrong label cost an edit, never a
   reconstruction.
3. **Checks across a whole scheme caught what no single drafter could see.**
   Parallel drafters checked their own batches. The assistant's check over the
   whole scheme, ignoring case and punctuation, then found duplicates across
   batches in every sweep ([CASE 2](../cases.d/CASE-002.md), [CLAIM 1](../claims.d/CLAIM-001.md), [ARG 3](../arguments.d/ARG-003.md), [THEORY 13](../theory.d/THEORY-013.md), [SYNTHESIS 3](../syntheses.d/SYNTHESIS-003.md)).
   A neighbour-alignment check backed up the drafters' own. Four drafters
   found and fixed a dropped row that had shifted every later label.
4. **The back-merge was mechanical.** The conflicts had three shapes, and one
   script resolved all 164: main's identity, staging's title and statement.
   Leftover temporary codes were mapped through the `formerly` fields, as
   the 14:43 note had found for the stranded readers.

## What did not go well

1. **An untyped field broke luria for the whole branch.** The first commit
   of [ADR-148](../decisions.d/ADR-148.md) declared `statement:` in `luria.yaml` with only a blurb. Luria
   refuses a field with no constraint, so every command failed to load the
   config, and the owner found it from a traceback. A one-second load check
   would have caught it (devlog 17:29).
2. **Drafters reused the approved examples as labels.** In CASE, ARG and
   SYNTHESIS, a drafter gave a sample label, verbatim, to a different entry
   with similar content. The brief listed the examples as a style guide and
   did not say they were already taken. The whole-scheme check caught every
   case, but each was a predictable error the brief invited.
3. **A squash merge undid the back-merge.** The promotion of [#790](https://github.com/dmarx/nucleation/issues/790) failed its
   docs run, so main's concretized codes never reached staging, while the
   batch went on retitling the same files there. The resolution, [#831](https://github.com/dmarx/nucleation/issues/831), was
   squash-merged; a squash keeps a merge's files and drops its second
   parent, so main and staging still looked diverged. The repair went
   through `staging2`, an "ours" merge recording main, a fast-forward of
   staging and a merge commit into main ([#832](https://github.com/dmarx/nucleation/issues/832)). Deleting the old staging was
   refused; the fast-forward made it unnecessary.
4. **Report-and-thesis pairs were called duplicates.** A heuristic flagged
   67 THEORY pairs, and the assistant proposed retiring the Proposed half of
   each before checking how the pairs were related. 65 carry the `extends`
   edge [ADR-065](../decisions.d/ADR-065.md) §3 prescribes between a reported reading and the thesis
   filed beside it. A first trace blamed one commit for 118 files, because
   the clone was shallow (devlog 21:55).
5. **The retitle gave each pair labels that read as two findings.** The
   drafters labelled report and thesis separately, so on a graph one reading
   appears twice. The `extends` edge tells them apart, and the labels do not.
6. **Smaller slips.**
   - `gh api` was used for reading CI and editing a pull request, which this
     environment reserves for search.
   - A stub changelog fragment was added to a contribution holding only a
     devlog note; the owner: "you don't need to add an empty changelog
     entry just so we can file a devlog entry".
   - Only every third THEORY label was read, about 760 of 2,280; the others
     were checked only by script.
   - Several sweeps were merged before their CI reported; nothing failed,
     but each such merge rested on local checks alone.

## Recommendations

1. **A drafter's brief marks its examples as taken.** "These labels belong
   to the sample's entries; never reuse one." The whole-scheme check stays;
   the brief stops inviting the duplicates it catches.
2. **A back-merge is merged with a merge commit, never a squash.** It
   belongs beside [ADR-125](../decisions.d/ADR-125.md) in CLAUDE.md's working rules or in the repository's
   merge settings; which is the owner's call.
3. **Carrying concretized codes belongs in luria.** The 14:43 note said: if
   it recurs, a `luria carry` or a repair step that maps `formerly` codes on
   a branch. It recurred, at the scale of 165 files. Filed upstream at the owner's
   word as dmarx/luria#406, for implementation later.
4. **Check relations before calling entries duplicates, and fetch the full
   history before tracing origins.**
5. **Load the config after any edit to `luria.yaml`.** One line,
   `python3 -c "import luria.config as c; c.load()"`, outside the rule
   against linting before a push ([ADR-054](../decisions.d/ADR-054.md)).
6. **A devlog-only contribution takes no changelog fragment.** The owner's
   ruling. CLAUDE.md's "the changelog fragment goes in the same contribution"
   could say "where there is a reader-facing change"; the wording is the
   owner's call.
7. **Optional: let a thesis's title show it is one.** Where a THEORY extends
   a reported reading, its label could say so ("…, as a general claim").
   Left as it is unless the owner wants it.

## The devlog notes it answers

- **17:29, an optional prose field cannot be declared.** Item 1 and
  recommendation 5.
- **21:55, the 67 twin readings.** Items 4 and 5, recommendation 4.
- **14:43 of 2026-11-25, readers stranded by a promotion** (another
  session's note, not answered by [RETRO-010](RETRO-010.md) or [RETRO-011](RETRO-011.md)). Its prediction held:
  concretization under work in flight recurred, and its mechanical
  resolution worked again. Recommendation 3 takes up its proposal.

## What it does not say

- Whether the new titles are good. The owner approved each form on a
  sample; the labels nobody read, about 1,500 THEORYs, rest on the checks.
- Why the promotion's docs run after [#790](https://github.com/dmarx/nucleation/issues/790) failed. The run after [#832](https://github.com/dmarx/nucleation/issues/832)
  succeeded; the earlier failure was not traced.
