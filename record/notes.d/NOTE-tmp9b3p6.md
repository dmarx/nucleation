---
status: Read
paper: LIT-tmp1bfvb
title: 'Bisiani and others (2026) — The hollowing out of local newspapers: A longitudinal study of journalistic performance decline and content homogenisation at a major UK publisher'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 for the reading pass the owner asked for ("read the
    works you can reach"), from a reader's draft the filer verified against
    the downloaded text. Copy and extent: - Read: OSF preprint (SocArXiv),
    DOI 10.31235/osf.io/ujmfq_v2, file
    "Bisiani_et_al_Hollowing_out_Preprint_V2.pdf", downloaded from
    https://osf.io/download/d9vcz/ on 2026-11-12, PDF, 8 pages of main text
    plus supplementary appendices. Read: abstract, §1–§5 in full, reference
    list scanned. Skipped: the supplementary appendices A–E (sampling
    details, coding schema, full model tables), beyond their first
    paragraph. - The preprint's title is "The Hollowing Out of Local
    **News**: ..."; the published title (Crossref) is "The hollowing out of
    local **newspapers**: ...". Outcome as the reader gave it: **Read** (the
    authors' preprint, version 2, main text in full). The version of record
    at Sage was not reached (Cloudflare challenge), so wording may differ
    from the published article.
date: '2026-11-12'
summary: >-
  A longitudinal content analysis of 27 Reach plc local newspapers (seven
  regional hubs) sampled monthly in 2019, 2022 and 2025 (55,332 articles),
  measuring Napoli et al.'s three dimensions of "journalistic performance":
  originality (no near-duplicate in the corpus, MinHash Jaccard ≥ 0.7),
  locality, and coverage of Friedland et al.'s eight Critical Information
  Needs (CIN), coded by a fine-tuned Qwen 2.5 1.5B (F1 0.85).
  Within-newspaper fixed effects show originality, localness and CIN all
  falling; a decomposition shows original local CIN content displaced
  ("crowding out") by duplicated non-local content; an E-I index shows
  content sharing moving from hub-confined to group-wide, coinciding with
  Reach's 2024 Content Hub and AI rewriting tool "Guten". The authors read
  this as UK evidence for "zombie" papers.
---
<!-- inactive-ok-file: CASE-tmpd5eqf CLAIM-tmpifp69 — Proposed; filed from the same exchange -->

# NOTE-tmp9b3p6: Bisiani and others (2026) — The hollowing out of local newspapers: A longitudinal study of journalistic performance decline and content homogenisation at a major UK publisher

## Contribution

First longitudinal content-level evidence for the UK hub model; a
crowding-out-versus-dilution decomposition; an organisational-boundary
measure (E-I index) of where homogenisation is organised.

## Key results

1. **Declines (§4.1, Table 1).** "Relative to 2019, originality decreases by
   22.9 percentage points by 2025 (β = −22.89, SE = 3.36, p < .001), while
   localness declines by 14.8 points (β = −14.79, SE = 2.20, p < .001) and CIN
   coverage by 6.3 points". Raw shares: local 66.5% → 51.5%, original 79.7% →
   56.5%, CIN 57.3% → 50.8%.
2. **Variance shrinks (§4.1).** "standard deviations decrease across all three
   measures ... indicating a reduction in between-outlet variation."
3. **Timing (§4.1).** Volume losses concentrate in 2019–2022; "declines in
   originality and localness intensify between 2022 and 2025", "though the
   panel design does not permit causal attribution to any specific
   organisational change."
4. **Crowding out (§4.2).** "original local CIN journalism — the civic core of
   each newspaper — fell from a median of 30.0 to 13.5 articles per edition
   between 2019 and 2025", while "duplicated non-local content increased more
   than sixfold, from 2.0 to 13.5 articles". "This pattern constitutes
   crowding out rather than dilution".
5. **What gets shared (§4.2).** "nationally focused articles were over seven
   times more likely to be syndicated than locally focused ones (OR = 7.28 ...)";
   "political coverage showed no significant elevation (OR = 0.96, n.s.)".
6. **Hub boundaries dissolve (§4.3).** "In 2019, 88.1% of all duplicated
   articles were shared only within hubs"; "By 2025, cross-hub syndication had
   more than doubled to 27.7% (E-I = −0.446)." "the further content travels,
   the less local and less civically relevant it becomes."
7. **Zombie trajectory (§5).** "original local CIN content halved over six
   years"; "The papers are not yet fully hollowed out — a substantial floor of
   original local reporting persists".
8. **Policy (§5).** Indicators "calibrated to outlet counts rather than
   content properties may fail to detect where local journalism is in
   performative decline."

## Assumptions

- Originality = no near-duplicate *within this corpus*; wire copy is not
  detectable, so (the authors say) estimates are conservative.
- LLM coding of locality and CIN is accurate enough (F1 0.85 against two
  coders with α = 0.898).
- PressReader's archived print editions represent the titles; dailies
  over-represented.
- Mechanisms (economies of information goods, "distance decay", metric
  regimes) are theorised from the literature, not measured.

## Concepts

Hub model; Content Hub; zombie / ghost papers; news deserts; journalistic
performance (originality, locality, CIN); crowding out vs dilution; E-I index;
distance decay; Shoemaker and Reese's hierarchy of influences; market-driven
journalism (McManus), information goods (Hamilton).

## Bearing on the record

**On the LIT's and the exchange's characterization.** A33's account ("follows 27 Reach newspapers in 2019, 2022 and 2025 and reports
falling originality, local relevance and coverage of critical information
needs, with homogenization") is **accurate**. Two things it leaves out matter
for the claim it supports: (a) the paper measures print *content*, not
investigative journalism or attention metrics; political coverage is not
preferentially syndicated, and CIN falls least (6.3 points); (b) the mechanism
the paper favours is cost-driven replication across a consolidated owner (hub
centralisation, Content Hub, AI rewriting), with pageview targets as one of
three mechanisms, and the design "does not support strong causal attribution".

- **[CLAIM-tmpifp69](../claims.d/CLAIM-tmpifp69.md)** (attention-weighted demand selects against investigative
  journalism): **qualifies**. It documents the content-level outcome the
  claim predicts (loss of original local civic reporting, displacement by
  scalable non-local lifestyle content) and names metric regimes ("pageview
  targets and story-per-shift quotas") among its mechanisms. But it does not
  isolate attention optimization from cost-driven syndication under
  consolidation, which it treats as the principal logic; it is closer to A's
  own "strongest rival" (collapse of the older subsidy, with optimization as
  adaptation) than to a test between them. It does not measure investigations.
- **[CASE-tmpd5eqf](../cases.d/CASE-tmpd5eqf.md)** (the newsroom that reads low traffic on investigations it
  no longer funds): **leaves open / weakly supports**. The paper shows the
  structural pre-condition (newsrooms moved away from communities, "distance
  decay", fewer original local stories) and a self-reinforcing direction, but
  it has no traffic data and does not observe the feedback loop from measured
  demand to further cuts.

Other held entries it bears on (found on recheck):
- **[CLAIM-602](../claims.d/CLAIM-602.md)** and **[CLAIM-605](../claims.d/CLAIM-605.md)** (capacity learned by doing and decaying with
  disuse; outside supply that does the work first lowers the capacity kept):
  centrally supplied duplicated content filling a shrinking edition while
  local origination halves is a field instance of the pattern; the paper does
  not measure capacity, only output.
- **[CLAIM-463](../claims.d/CLAIM-463.md)** (restoring conditions need not restore capacity): the paper
  bears only by its policy remark that funding indexed to outlet presence may
  miss hollowed titles; no hysteresis is shown.
- **[CLAIM-404](../claims.d/CLAIM-404.md)** (governance through evidence and criteria): pageview targets
  as criteria redirecting labour (§2.2) are an instance, theorised not measured.

Searched `record/` on origin/main for: zombie, homogeni(s/z)ation, Reach plc,
news desert, local news, crowding out, Napoli, Hollowing Out, the DOI and the
OSF id. "zombie" hits are philosophical zombies (unrelated); "homogeni" hits
are unrelated (cultural transmission, neuroscience). Found the related claims
[CLAIM-602](../claims.d/CLAIM-602.md), [CLAIM-605](../claims.d/CLAIM-605.md), [CLAIM-558](../claims.d/CLAIM-558.md), [CLAIM-463](../claims.d/CLAIM-463.md) (capacity decay), not named by the
LIT. **Not already held**: no LIT on main or the branch carries this DOI, the
OSF DOI, or the title.

## Limitations

Single publisher; observational panel; print editions only; no measure of
investigative output, traffic, or audience demand; duplicates only within the
sampled corpus; LLM-coded categories; the authors' own limitation list
(numbered "First, Second, ... Fourth" with no third) concedes that audience
demand and platform logics "may independently or interactively shape content
output".
