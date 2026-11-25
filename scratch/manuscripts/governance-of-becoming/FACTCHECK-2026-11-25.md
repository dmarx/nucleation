<!-- scratch/manuscripts/governance-of-becoming/FACTCHECK-2026-11-25.md -->

# Fact-check of the revised draft, 2026-11-25

An independent check (write-manuscript skill, step 8) of the revision of
the overview, the README and Articles 1 to 3, on the branch
`claude/manuscript-governance-of-becoming-revision` after staging, with the
status pass of #794, was merged into it. The checker did not write or
revise the text. Sources: `record/` as it stands on this branch, the
verbatim exchange (share 6b05ee39), `motivating/`, and the stored scripts.
Line numbers are those of the files as checked.

## What was checked

| Check | How | Count |
|---|---|---|
| Codes exist | every `SCHEME-nnn` and `SCHEME-tmpxxxxx` in the five files against `record/*.d/` | 325 distinct codes; all exist. ADR-tmpbdfmk is named as ADR-143's former code; `REVIEW-2026` is a file name |
| Quotations | every double-quoted string (847) matched, after normalizing link markup, quote marks and whitespace, against the entry cited beside it, then the exchange, `motivating/`, the other files, the review and the curation entries; the rest read by hand | 401 in the adjacent cited entry; 241 in the exchange, a motivating draft or (README) the articles it quotes; 195 triaged by hand. Problems: 5 |
| Standings | every parenthetical "(CODE, status, warrant)" and "CODE (status …)" by script (312), and every mention of the 20 promoted entries read in context (69) | Problems: 23, all but one from the status pass |
| Voices | 33 turn attributions (U#, the owner's, A's) against the entries' texts; 194 quotations located to their turn in the exchange | Problems: 1 |
| Figures | 250 numerals checked present in the cited entries; the figures below reproduced by script or rerun in a scratch copy (no file in the repository written) | Problems: 2 (a membership count, a reliance count) |
| Joins and gaps | the 25 joins and the gaps against SYNTHESIS-tmp4tvbr's section "The joins of the manuscript governance-of-becoming, Part I" and the entries cited | verdicts and sections agree. Problems: 7 stale statements that notes are unfiled |
| README against the articles | the standing-review table's "Part I" column, the counts, the membership lists, the joins lists | Problems: 2 |

**Figures reproduced.**

- CLAIM-tmpjg5gx: equilibria 0.0483, 0.6886, 0.9925 at b = −3, λ = 8; diagonal threshold s ≈ 0.689; the established and fresh columns of the table exactly (0.933 at b = −4.33, collapse at −4.35).
- CASE-tmptpna1: schedules LMMMMMLLLH (M 6, L 9, H 10) and LLLLHMMMMM (L 4, H 5, M 10); H and L five earlier, M four later, total down by six.
- CLAIM-tmp18v1o (A20's widget rule): capacity 0.418 at withdrawal, minimum functioning 0.339.
- CLAIM-tmp8mpgs: 150, 120, 111.5, 126.5. CLAIM-tmp2jhc1 (A24's widget): 14.75/11.25 and 12.25/13.75. ARG-tmpa5ped: n > 4.8.
- Arithmetic of CLAIM-761 (12, 3, 5), CLAIM-569 (X and Y), CLAIM-571 (0.7, 1.3, gap 0.6), CLAIM-591 (1 and 3), CLAIM-760 (3 to 1; 4 to 5).
- CASE-326 (lead-108): 7 tests pass; `price_cases.py` regenerates `results.json` and `results.md` byte for byte; saving 11 to −1 at three uses, the bugs losing at 1 and 1.5 and winning from 2, break-even 1.667 and 3.333, the bin at once, the pop-out brick never.
- CASE-343 (lead-036): rerun from empty, `results.jsonl` and `results.txt` byte-identical, 17 tests pass; loss 1.000 at one occasion in ten quarters, 0.386 at four a year, none decoupled.
- CASE-315 (lead-080): rerun byte-identical, 13 tests pass.
- CASE-412 and CASE-397 (governance-of-possibility analysis): rerun identical but for the runtime line, 21 tests pass; 0.147 and 0.894 in the table.
- CASE-333 (lead-098): 347 items rerun, all identical to the stored results. They include the cited follow fractions 0.0022, 0.300 and 0.584 and the orders 0.467 and 0.996. The 300 sheaf items, which are not cited, were not rerun. scipy was installed into the scratchpad for this run.
- CASE-191 (`scratch/formal/self_formation.py`): the knockout table (0 and 2.618) and the frustration knockout from t = 0.
- Overview standings recounted from the curation map rows. The README's "Relied on by" was recounted for 24 codes; 23 agree.

**Not reproducible here**: CASE-189 (no stored script), CASE-161 and CASE-163 (PerspectiveLab, no script on the record) and CASE-332 (lead-048, not rerun). Their figures match the entries' text.

## Problems

### A. Standings changed by the status pass (#794): update to Active

The README and the overview say the drafts give pre-pass standings and that this check updates them. Each item gives the file, the text and the fix.

1. **README L143.** "CASE-412 and CASE-315 (Proposed, executed-study) … CLAIM-1099 (Proposed, demonstrated)". Change all three to Active.
2. **README L144.** "CASE-343 (Proposed, executed-study); CLAIM-921 (Proposed, demonstrated)". Change both to Active.
3. **README L145.** "CASE-397 (Proposed, executed-study)". Change to Active.
4. **README L146.** "CASE-346 (Proposed, executed-study) … CASE-401 (Proposed, executed-study)". Change both to Active.
5. **README L149.** "CASE-326 (Proposed, executed-study) … CASE-343 (Proposed, executed-study) with CLAIM-921 (Proposed, demonstrated)". Change all to Active.
6. **README L157–158.** "CASE-161, CASE-162, CASE-325 and CASE-396 are Active and the rest Proposed". Of the executed studies the series leans on, all are Active except CASE-163 (with CASE-332 and CASE-333 in Article 1). Also drop "Standings are as of 2026-11-24, before the status pass" (L126) once the table is updated.
7. **Overview L32.** "is promoting several entries Part I cites … possibly CLAIM-921, CLAIM-1095 and CASE-163. The drafts give each entry's standing as it stood before the pass. The fact-check … brings them up to date". The pass promoted twenty entries, among them CASE-326, CASE-343, CLAIM-892, CLAIM-921 and CLAIM-1095. CASE-163 stays Proposed. State that.
8. **Overview L35.** "Statuses are given as of 2026-11-24, before the status pass." Change to "after the status pass of #794".
9. **Overview table, L47–64, and L66.** The counts are "before the status pass". After it, Article 3 is **7/6/2** (not 5/8/2; CASE-326 and CLAIM-921), Article 5 is **4/7/1** (not 3/8/1; CLAIM-1115) and Article 10 is **2/14/1** (not 1/15/1; CLAIM-921). Every other row is unchanged. Delete "The status pass will change some counts …".
10. **Art. 1 L210.** "CASE-346 (Proposed, an executed study)". Change to Active.
11. **Art. 1 L50 and L338.** "Four executed studies are cited" and "three of the four executed studies: CASE-163, CASE-332 and CASE-333". Article 1 also cites CASE-346, an executed study (§1.5.5, Gaps), now Active. Make it five, two of them Active (CASE-161, CASE-346), and "three of the five".
12. **Art. 2 L11.** "Nothing in this article's own argument is Active. Every claim … that states it is Proposed … CLAIM-1095 … demonstrated". CLAIM-1095 is Active since #794. Make it: "Nothing in the argument is Active except CLAIM-1095, the formal correction §2.8 follows (Active since #794)".
13. **Art. 2 L275.** "CLAIM-1095's correction (Proposed, demonstrated, counter)". Change to Active.
14. **Art. 2 L311.** "CASE-397 (Proposed)". Change to Active.
15. **Art. 3 L7 (abstract).** "A cost model run on three cases … It is Proposed". CASE-326 is Active; the claim drawn from it, CLAIM-891, is Proposed. Say so.
16. **Art. 3 L23 and L97.** "(CASE-326, Proposed)" and "(CASE-326, Proposed, executed study)". Change both to Active.
17. **Art. 3 L131.** "(CLAIM-892, Proposed, demonstrated; …)". Change to Active.
18. **Art. 3 L191 and L256.** "CASE-343 (Proposed, executed study …)". Change both to Active.
19. **Art. 3 L262.** "(CASE-315, Proposed, executed study; rerun 2026-11-24)" and "(CASE-412, Proposed, executed study)". Change both to Active.
20. **Art. 3 L273.** "CASE-397 (Proposed, executed study)". Change to Active.
21. **Art. 3 §3.9 table, L384, L386 and L389.** "the cases Proposed, executed" (CASE-412, CASE-397, CASE-315), and "Proposed" for CASE-326 and CLAIM-892, and for CLAIM-921 and CASE-343. All are Active now. CLAIM-891 stays Proposed.
22. **Art. 3 L258–260: a narrowed title is quoted.** The blockquote gives CLAIM-921's old title ("… so at the same expected funding a rarer capability is lost sooner …"), with "(CLAIM-921, Proposed, demonstrated)". Version 4 narrowed the title to "… any stretch without occasions long enough for competence to decay there reaches it whatever each use was paid, so at the same expected funding the chance of loss within a given time has a lower bound that rises as occasions grow rarer and does not depend on the payment per use …". Version 5 made it Active. Quote the current title, mark it Active, and replace "Its scope is narrower than its title … states the ordering" with "Its title was narrowed to the lower bound on 2026-11-24 (version 4)".

### B. Statements that a note is unfiled, though the README says it was filed (on the record now)

23. **Art. 2 L346 (J2.2).** "that belongs in a dated note on CLAIM-tmp7hqtl, which has not been filed". The note is filed: CLAIM-tmp7hqtl, "Note of 2026-11-24: from the revision …", "Does 'violation' presuppose a requirement?". Make it "filed as a dated note on CLAIM-tmp7hqtl".
24. **Art. 2 L348 (J2.4).** "No note has been filed." The note is filed on CASE-tmptpna1 (same heading). Fix it the same way.
25. **Art. 3 L191.** "No dated note on the lead says this yet." LEAD-tmp14n26 carries the revision's note of 2026-11-24. Delete the sentence or say the note says it.
26. **Art. 3 L416 (J3.5).** "belongs in a dated note on TERM-116 or CLAIM-591, which has not been filed". The note is filed on TERM-116.
27. **Art. 3 L418 (J3.10).** "a pointer for a dated note on LEAD-tmpeo8wq, which has not been filed". The note is filed (LEAD-tmpeo8wq's second note of 2026-11-24, as the README says).
28. **Art. 3 L422 (G3.1).** "No entry holds this gap yet." SYNTHESIS-106 carries the revision's note of 2026-11-24 saying so.
29. **Art. 3 L423 (G3.2).** "The question carries no note saying so." QUESTION-tmpzhnqy carries the revision's note of 2026-11-24.
30. **Art. 1 L366 (minor).** "is a computation, for a note on CASE-189 … Not done." CASE-189's note of 2026-11-24 is filed; only the computation is not done. Make it "recorded in CASE-189's note of 2026-11-24; the computation is not done".

### C. Quotations

31. **Art. 2 L38, an attribution error.** "it calls the programme 'our theory' throughout (curation entry …, §3)". A49 never says "our theory". Its first-person phrases are "our account", "our earlier manuscript", "our discussion" and "our conversation". "our theory" is the owner's, from U31 ("articles that develop our theory"). The curation entry's §3 makes the same error; it is a record correction for the owner's next pass. Fix: "it speaks of 'our account' and 'our conversation' and credits no owner turn".
32. **Art. 2 L171.** CLAIM-788 forms "a new channel, a maintained capacity". The title reads "the record's new channel, a maintained capacity". Quote it so, or quote only "a new channel".
33. **Overview L31, Art. 1 L29 and Art. 2 L23.** "(the owner delegated these rulings)". The histories read "(the owner delegated these rulings; ADR-057)". Add "; ADR-057", or close the quotation before the parenthesis.
34. **Art. 2 L81.** "('because it governs deviation')", given as TERM-tmplpplx's first-version wording. Version 1 is not kept, and the history says only "'because' for 'only if'". Quote the history.
35. **Art. 1 L296.** The six probes are joined into one quotation with semicolons. The words are verbatim from CLAIM-tmpersgx's bulleted list, so this is not an error, but "(listed in …)" would be cleaner. No fix needed.

### D. Membership and counts

36. **README L50 and overview L66: 122 members.** ADR-tmpenzcn gave 122 when it was filed. 121 entries carry `governance-of-becoming` now (119 CLAIMs and 2 ARGs), because CLAIM-tmp1nubb left the work when it was Superseded (its history). Make it "122 at filing, 121 now".
37. **README L485–486 (open item 14).** CLAIM-tmp05a1l, CLAIM-523 and CLAIM-690 are listed as membership candidates, but all three already carry the work's field. Keep CLAIM-tmppx64t, CLAIM-tmpu77ve and CLAIM-716 as candidates.
38. **README L490 and Art. 3 L11: "CLAIM-tmp8mpgs (a borderline member of ADR-tmpenzcn)".** ADR-tmpenzcn names CLAIM-tmp8mpgs among the gap fills that "are not members … unless the owner adds it". The 13-entry borderline list is not on the record: the curation entry's "§6 table" was not found, as `background/contracts-and-standing.md` also notes. Make it "a gap fill, not a member (ADR-tmpenzcn)".
39. **README, the "Part I's own premises" table: CLAIM-tmpersgx "8".** Seven entries name it in a relation field: SYNTHESIS-tmp4tvbr (integrates), LEAD-tmpbqj9u, LEAD-tmpl9349 and LEAD-tmpfq5cj (advances), ARG-tmp2dpcv (concludes), CLAIM-tmp0d1fq (complements), and CLAIM-tmp1nubb (complements and superseded_by). That is 8 links from 7 entries. CLAIM-tmpkvzcn and QUESTION-tmpp8flf name it only in their summaries. The other 23 counts match one per entry. Minor: say 7, or say the count is of links.

## Tally

| Kind | Count |
|---|---|
| Standing out of date after #794 (A) | 21 items (1–21), covering about 40 citations |
| Quoted title superseded by narrowing (A22) | 1 |
| Stale "not filed" statements (B) | 8 |
| Quotation or attribution (C) | 4, plus 1 noted without a fix |
| Membership and counts (D) | 4 |
| **Total needing a fix** | **38** |

## Verdict

The revision is sound on what it quotes and computes. Every code exists.
Every quotation checked is verbatim but for the four above. Every figure
that has a stored script reproduces, most of them byte for byte. The
voices are attributed correctly but for A49's "our theory". The joins
agree with SYNTHESIS-tmp4tvbr. What needs fixing is bookkeeping that the
pass and the revision's own closing work overtook. Standings must be
brought up to #794, including CLAIM-921's narrowed title. The articles
still say that notes are unfiled after the closing pass filed them. The
membership statements need correcting (121 now, three listed candidates
already members, CLAIM-tmp8mpgs a gap fill). None of these changes an
argument.
