---
number: 724
status: Read
formerly:
- NOTE-tmp286fw
paper: LIT-1032
title: 'Wu & Silva — How Millions Coordinate at Scale'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the arXiv PDF, v3 of 13 July 2026
    (arxiv.org/pdf/2408.13236, 27 pp. in ACM template). Text extracted with
    pdftotext; tables came out in column order and were read against the
    layout extraction. Read: main text, Tables 1–2, all appendices
    (A.1–A.4), figure captions. The reference list was scanned, not read.
    One sentence is cut off in the PDF itself (the success-status feature
    in §6.3, "retained at least 11"); Appendix A.4 completes it as 11% of
    the drawing's maximum area. Quotations checked by script against the
    extracted text, whitespace normalised.
date: '2026-10-13'
summary: >-
  A descriptive study of all three r/place editions plus a coalition-recovery
  method run on 2017. Participation stays heavy-tailed under the uniform
  five-minute cap; larger coalitions waste more actions and have lower median
  activity per member; participants concentrate into large coalitions as an
  event goes on; and which coalitions survive is barely predictable from
  their size, area, start time and colour entropy until late. Lasting
  artworks are those whose coalitions keep working under continual
  overwriting.
---
<!-- inactive-ok-file: CLAIM-280 CLAIM-272 CLAIM-285 THEORY-214 — Proposed; open claims and readings, cited as what this reading bears on, nothing rests on their being settled -->

# NOTE-724: Wu & Silva — How Millions Coordinate at Scale

## Contribution

It puts the three editions (2017, 2022, 2023) side by side on engagement,
coordination cost and conflict. It adds a method that recovers coalitions,
including failed ones, from the placement log alone. The method combines
image segmentation with Node2Vec embeddings of a graph linking participants
who placed adjacent same-colour pixels, then links clusters across
snapshots by greedy set cover. It is run on 2017 only.

## Key insight

The final canvas is a survivor's record. "less than 7% of individual pixel
updates survive to the final snapshot." Reconstructing the coalitions that
failed shows that early mobilization does not decide the outcome. Lasting
artworks are the ones whose coalitions keep working under continual
attack, and coalitions that look alike early end very differently.

## Assumptions

- **Coalition, operationally (RQ2).** A participant belongs to an
  artwork's coalition if they placed at least one pixel matching its final
  colour. That ties coalitions to final artworks, which is the bias §6
  then tries to escape.
- **Wasted action.** Repainting a pixel its current colour. It is read as
  coordination inefficiency, though the authors list other causes
  (delayed awareness, "redundant defensive behavior").
- **Bot filter.** Accounts above one action per five minutes on average
  are treated as potential bots and excluded (17.1% of 2023 actions, 0.3%
  in 2017).
- **Recovered coalitions (§6, App. A.3).** Validated only against the
  final 2017 Atlas (ARS 0.42 for the dynamic method, 0.58 per snapshot) and
  by visual inspection; "no ground-truth annotations exist for transient or
  failed coalitions".
- **Success.** A coalition at a sampled snapshot is successful if its
  artwork keeps at least 11% of its maximum area to the end (App. A.4).

## Key results

- **Heavy-tailed participation under a uniform cap (§4.1, Table 1).**
  "Activity exhibits a pronounced heavy-tailed distribution". Mean actions
  per account were 14.19 in 2017; the maximum was 545. The takeaway:
  "activity remains highly concentrated among a relatively small subset of
  users despite platform-imposed cooldown constraints".
- **Mobilization over size (§4.2).** Canvas activity is weakly related to
  a subreddit's size; small "r/place only" and geographic communities were
  most active.
- **Coordination cost grows with coalition size (§5.1).** In all editions
  larger coalitions have a higher share of wasted actions, and the slope
  falls from 2017 to 2023. The authors credit, tentatively, overlays,
  extensions, bots and external channels.
- **Smaller coalitions, more active members (§5.2).** Median actions per
  participant are higher in small coalitions in every edition.
- **Consolidation (§6.2, Fig. 7).** Over the 2017 event, the distribution
  of recovered coalition sizes shifts toward larger coalitions.
- **Low predictability (§6.3, Table 2).** A decision tree on start time,
  artwork size, coalition size and colour entropy gives F1 0.09 in the
  first 48 hours and 0.67 later. With stricter success thresholds the
  uncertainty is "even higher" (App. A.4).
- **Lifecycles (§6.4, Fig. 8).** "successful initiatives (e.g.,
  r/AmericanFlaginPlace) remained active despite sustained overwrite
  pressure throughout their lifecycles". Some failures "exhibited activity
  patterns similar to successful ones for extended periods before
  experiencing rapid decline". A first Mona Lisa attempt was abandoned and
  a later one completed.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Participation is heavy-tailed in every edition despite the uniform cooldown | strong | full logs, Table 1, Fig. 2a |
| C2 | Larger coalitions have a higher share of repaint-same-colour actions, less so in later editions | moderate | Fig. 5; the measure conflates waste with defence |
| C3 | Median per-member activity is lower in larger coalitions | moderate | Fig. 6 |
| C4 | Participants concentrate into larger coalitions as the 2017 event proceeds | weak to moderate | recovered coalitions, three snapshots; recovery unvalidated for transient coalitions |
| C5 | Coalition success is barely predictable from coalition-state features until late | moderate | decision tree on 219,217 observations, balanced; four features only |
| C6 | Lasting artworks persist under sustained overwriting, not in its absence | weak | ten illustrated lifecycles (Fig. 8) |

## Concepts

- **Action, participant, coalition.** A pixel update; a contributing
  account; the accounts that contributed to one artwork.
- **Final / Match / Adversarial actions.** Updates that survive to the
  end; updates matching the final colour but later overwritten; updates
  differing from it.
- **Coordination inefficiency.** Share of a coalition's actions that
  repaint a pixel its current colour.

## Connections

It extends Rappaz et al. (2018), whose BPR embeddings it beats, and it
leans on the r/place Atlas while criticising its survivorship bias. It does
not cite Falmagne et al. ([LIT-1025](../literature.d/LIT-1025.md)) or Adams et al. ([LIT-1034](../literature.d/LIT-1034.md)), and
it lists Litherland & Mørch ([LIT-1037](../literature.d/LIT-1037.md)) among prior r/place work only.

## Bearing on the record

**[CLAIM-280](../claims.d/CLAIM-280.md) (persistence by contest and repair).** Supported, weakly.
Fig. 8 shows successful coalitions with collaborative and adversarial
actions running together for the whole event. Under 7% of updates survive.
Only ten lifecycles are shown, so this illustrates the regime and does not
measure how common it is. The Mona Lisa abandoned and rebuilt is a case of
a product recurring without the same coalition behind it. The
recovered-coalition data would allow the product/producer split to be
measured, but the paper does not measure it. See [THEORY-216](../theory.d/THEORY-216.md).

**[CLAIM-272](../claims.d/CLAIM-272.md) (equal budgets do not equalize influence).** A qualification
the claim needs. The cooldown is a ceiling, not a quota. Use of it is
heavy-tailed: in 2017 the mean account placed 14 pixels and one placed
545. And 17% of 2023 actions came from accounts exceeding the ceiling.
So influence over the canvas was unequal before any plan directed anyone,
through unequal use of the cap and through automation and multiple
accounts. The claim's "because coordination lets a member's plan direct
other members' actions" names one mechanism of several. The paper does
not measure influence through plans at all. Its RQ2 statistics are action
counts.

**[QUESTION-084](../questions.d/QUESTION-084.md).** The coalition-recovery method infers who worked
together from co-placement. That is behaviour-to-coalition inference, and
its validation stops at final artworks. The authors concede that outcomes
"may also depend on interaction-level processes that are difficult to
observe from behavioral traces alone, including alliance formation,
inter-group negotiations, coordinated attacks, and communication occurring
on external platforms". This is evidence for the question's second horn,
the need for a record of coordination, but it is the authors' judgement and
not a test.

**[QUESTION-093](../questions.d/QUESTION-093.md).** The low early predictability from coalition-state
features is a negative result for one kind of coarse-grained model. Only
four features were tried, and none of them is a latent-coalition dynamic.
It neither meets nor fails A8's test.

**[CASE-079](../cases.d/CASE-079.md).** The 2017 figures (72 hours, 1,166,925 accounts,
16,559,897 actions) match the case. The paper confirms that logs for all
three editions are public (App. A.1). Its Table 1 gives 108,034,224
participants for 2022, against 10.4 million in Falmagne et al.
([LIT-1025](../literature.d/LIT-1025.md)), and a 2017 duration of 89 hours, against 72 in its own
text. Both table entries look wrong and should not be cited.

## Limitations

- Coalitions are defined by final colours in §5 and recovered by an
  unvalidated method in §6. Neither is a membership record.
- "Wasted action" counts defensive repaints and username claims as waste.
- Predictability is tested with four state features and shallow models;
  "difficult to predict" is relative to that feature set.
- Lifecycle analysis is 2017 only, the least automated edition.
- Design implications in §7.2 are suggestions about other platforms not
  studied.
- Table 1 has at least two inconsistent entries (above).

## Open questions

- Run the coalition recovery on 2022 and compare recovered coalitions'
  turnover of members with their artworks' persistence. That is the
  measurement [CLAIM-280](../claims.d/CLAIM-280.md)'s product/producer split needs.
- Does adding interaction features (who attacks whom, shared members)
  raise early predictability? If not, the unpredictability is in the
  dynamics. If it does, it was in the feature set.
