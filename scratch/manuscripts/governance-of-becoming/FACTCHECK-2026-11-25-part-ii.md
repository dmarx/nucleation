<!-- scratch/manuscripts/governance-of-becoming/FACTCHECK-2026-11-25-part-ii.md -->

# Fact-check of Part II's revision, 2026-11-25

This is an independent check under step 8 of the write-manuscript skill. It covers the revision of Articles 4 to 6 (files 04 to 06), the overview, and the README's Part II material: its two Part II tables, the standing review's Part II rows, "Part II's joins", open items 19 to 26, the step-3a section and its dated note. The branch is `claude/manuscript-governance-of-becoming-part-ii-revision`. The revision followed REVIEW-2026-11-25.md §4. The checker did not write or revise the text.

**Sources.** `record/` as it stands on this branch. No record file differs from staging's merge of #798, so front matter is as of commit 974a1f2b and #798. The verbatim exchange (share2, a superset of share 6b05ee39 that runs to A53). `motivating/`. The review's Parts A to C. The curation entries 2026/11/24/205621, 231157 and 2026/11/25/022031. The kept scripts in `scratch/formal/`.

**Method.** The scripts ran in the checker's scratchpad with `python3 -I`. They were adapted from Part I's fact-check, and the front-matter index was rebuilt on this branch. The kept scripts also ran from the scratchpad. `git status` was clean afterwards. Line numbers are those of the files as checked.

## What was checked

| Check | How | Count |
|---|---|---|
| Codes exist | every `SCHEME-nnn` and `SCHEME-tmpxxxxx` in the five files, against `record/*.d/` and `formerly:` | 504 distinct codes, all of which exist. Exceptions: ADR-tmpbdfmk is named as ADR-143's former code, and `REVIEW-2026` and `FACTCHECK-2026` are file names |
| Quotations | every double-quoted string (943), normalized for link markup, quote marks and whitespace. Each was matched first against the entries cited in its paragraph, then the exchange, `motivating/`, any record entry, the curation entries of 2026-11-24 and 25, the review, and the other manuscript files. The rest were read by hand | 723 matched in a cited entry, 98 in the exchange, 3 in a motivating draft, and 92 elsewhere. The 92 were nearly all in an entry cited a paragraph above, "ibid.", or a README or review section title. The 27 unmatched were triaged by hand. 17 were artefacts of nested quotation marks. 6 were section titles. 4 were the owner's session words of 2026-11-25 ("go ahead with the revision plan" ×3; "keep A49's order; continue with Part II"), which are recorded only in briefs and, paraphrased, in ADR-tmpenzcn's history. Problems: 2 (C7, D8) |
| Standings | four scripts. "(CODE, status, warrant)": 482. "CODE (… status …)": 506. The status word in the 45 characters after each code: 725. Lists sharing one parenthetical, each member checked: 100. Each warrant was compared with `warrant` and each status with `status` | 0 wrong. The 28 window hits in Part II material were multi-code table cells and were triaged one by one |
| Who made each entry Active | 61 history statements read against the entries' `history` notes: Article 4's standing list (22), Article 5's (21), Article 6's (18). The status-pass formula for the twelve was also read in all five histories | Problems: 2 (A1, A2) |
| Voices | 13 owner quotations from this exchange located to their turns (U5, U6, U10, U11, U14 ×2, U31, U32 ×3). 143 quoted strings located in exchange turns by script. The only mismatches are U and A numbers that recur across exchanges, and each was resolved to the exchange named. Attributions in the README's premises table were checked against summaries for 29 entries. The reading of "handle the fixes for the twelve" was compared across all files | Problems: 2 (C6, C7) |
| Figures | 481 numerals extracted. 34 are not in an entry cited in the same paragraph: section numbers, plus CASE-162's and CASE-396's figures, cited in the paragraph above. Those were grepped there and found. All five kept scripts were rerun (below). Reliance counts in the README's "Part II's own premises" were recounted from front matter for 60 codes | 0 wrong. All 60 counts agree |
| Membership | every membership statement in files 04 to 06 checked against `works`: 16 in Article 4, 36 in Article 5, 31 in Article 6 | 0 wrong |
| Joins and gaps | the 17 joins in the articles' closing sections, against Part B's table and SYNTHESIS-tmp4tvbr's section "The joins of the manuscript governance-of-becoming, Part II" (version 4), and against the entries filed for them | The verdicts agree. Problems: 2 (B3, E9) |
| README against the articles | the Files table, the Part II step-3a table, the standing review's Part II rows, "Part II's joins", "The review's plan, item by item", and open items 19 to 26 | Problems: 4 (B4 in part, F10, F11, F12) |
| Consistency of "handle the fixes for the twelve" | overview L33, README L311 and L449–455, Article 5 L29 and L53, Article 6 L32 | Problems: 1 (C6) |
| Points of contact (light, plan item 9) | the review's Part C list against what the articles now cite. A script listed Active entries in each article's lines whose titles match its constructions and which no Part II file or the review cites. The three curation entries were read for the process history | Problems: 5 (G13 to G17) |

**Figures reproduced.** The five kept scripts were rerun with `python3 -I`, and each printed "checks pass".

- **`inquiry_frontier_constructions_check.py`.** Construction 1: [] against [(q, a)] at B = 12. Construction 2: the joint sets were recovered at every B in 0…39. Construction 3: sequential [] against parallel [(q, a)] at 6 + 6 > 10. Construction 4: least costs 5 against a true cost of 9, wrong at B = 5 and 8. The negative control was exact.
- **`response_kernel_bisimulation_check.py`.** The pair s, t gives 0, 1 and 0. The pair u, v gives 0, 1 and 5.4. This is Article 5's table.
- **`inquiry_coupling_bounds_check.py`.** H = 4, with posing and answering 3 days each. The three organizations finish at 4, 6 and 6, and the bounds held on 484,000 cases. Construction 4's 5 against 9 and both controls also reproduced.
- **`inquiry_depth_check.py`.** Days left 8, 4 and 1. The sides agreed to four decimals at the refined maximizer and not at the grid point, as Article 5 says. The mixture case gives a drop at about H = 7.04.
- **`maintained_nuclei_check.py`.** The run ends at 1.74 to 1.84 over 50 runs. The 1.61 is not reproduced, as Article 5 and the README say.

The following figures were traced in their entries' text.

- **CASE-325.** 80 of 80. Medians 17.1 (10.0 to 22.2) and 61.3 (49.1 to 70.7). 0.015 and 0.03–0.26. 0.08–0.11, 0.022–0.034 and 0.009–0.018. 0.9 to 2,551. 10 to 82. 0.26–0.32 against 0.16–0.20. Parameter counts 16, 128, 14, 38 and 64 against 4.
- **CASE-162.** The four-column table, −0.193 and +0.184, 39 of 64, and 41 to 34.
- **CASE-396.** 30 = 10 + 20, 0.01–0.36, 0.00 and 0.10, 6.08 and 3.36, 5–6 and 1–4 units.
- **CASE-346.** 400 safe steps, 43 %, median 6, 87 %, 99 [95, 103], median 44, 17 to 30, κ ≥ 1.48, h = 0.002 and 99.5 %.
- **The capture components.** CLAIM-1183: 0.044, 40 of 40 and 0.40. CLAIM-1185: 0.360 and 0.361. CASE-401: 1,802 of 1,802.
- **Other entries.** CASE-382's 122 participants. THEORY-903's d = 0.43 and 0.65. THEORY-900's 116 studies. CASE-412's 0.147 to 0.894. CASE-397's 120 periods. CASE-386's 11 > 10. CLAIM-1016's widget, 12 against 8. CLAIM-tmp2jhc1's 14.75/11.25 and 12.25/13.75. CLAIM-1114's 2,037 of 20,000.

**What was not reproducible here.** CASE-162 has no script in this repository (its note of 2026-11-25), and CASE-346, CASE-396, CASE-401 and CASE-325 were not rerun by this check. Their figures match the entries' text and the entries' own rerun notes.

**What checks out and was rewritten in the revision.** The following were all checked against their entries and found right:

- **The sync with the reruns.** It is now right everywhere: CASE-325's note, LEAD-089 and LEAD-181 Done, the five claims "rerun, and what holds it back", and CLAIM-1114 as the chain's bottom.
- **The step-3a corrections.** These cover CASE-382, CLAIM-981, LEAD-128, CLAIM-358's note of 2026-11-22, CASE-109, CLAIM-1139, LEAD-141, QUESTION-015 (Answered), CLAIM-552's note, QUESTION-128, and CLAIM-758's six readings.
- **The rest of the review's corrections.** The scope corrections (1.3) and the pre-run criteria (1.4) are right. So is the `rests_on` chain of §5.5.2 (2.11), and CLAIM-1203's and CLAIM-1195's voices (2.12). The promotion dates of 2.10 are corrected.

## Problems

### A. Who made an entry Active

1. **Art. 4 L15. CLAIM-436 is grouped with promotions "at the status review's ruling (the owner delegated these rulings)".**
   - **The text:** "CLAIM-502, CLAIM-436 (re-derived at its ninth review), CLAIM-549 and CLAIM-550 were promoted or re-derived at status reviews 'at the status review's ruling (the owner delegated these rulings)'".
   - **The record:** CLAIM-436 went "Proposed to Active" at "The ninth status review (ADR-057; ADR-047's ruling that a checked re-derivation meets a request for a proof)" (version 3), and that note names no delegation. The formula appears only in its version 4, an edge change at the nineteenth review. This is the same case as THEORY-335 (review 2.10), which Article 6 now handles correctly.
   - **The fix:** Take CLAIM-436 out of that sentence. Say instead: "CLAIM-436 was promoted at the ninth status review, whose note names no delegation".
2. **Art. 4 L13–22, "What is Active, and who made it so" (minor).**
   - **The text:** The list stops at the first draft's entries.
   - **The record:** The revision added Active entries that the list omits: CLAIM-1139, CLAIM-021, CLAIM-467, CLAIM-449, CLAIM-554, CLAIM-569, CASE-036, ARG-007, CASE-153, TERM-078, and THEORY-900, THEORY-903 and THEORY-912. One of them differs from the list's classes. CLAIM-449 was "Promoted at the ninth status review (ADR-057), on the owner's assent in the pull request", which is the class of CLAIM-347, not of a delegated ruling.
   - **The fix:** Add the entries the revision cites, with each history's class. Or say that the list covers the first draft's Active entries, and give CLAIM-449's class where it is cited (§4.6.2).

### B. Statements the record does not hold

3. **Art. 4 L341 (J4.1). The relations of CLAIM-tmp7rl3d.**
   - **The text:** "Its rests_on are CLAIM-347, CLAIM-361, CLAIM-532 and CLAIM-tmpm76n5, its ground is CASE-191, and it complements CLAIM-tmpupcws, CLAIM-tmpisfi1 and CLAIM-tmpgx2ej."
   - **The record:** CLAIM-tmp7rl3d's front matter has `rests_on` and `grounds` as stated. It has no `complements` field, and its body names no complement.
   - **The fix:** Drop the complements clause, or say "it cites" or "it sits beside". Adding `complements` to the entry is a record change, for the next pass.
4. **Art. 4 L132 (§4.4), the §4.10 table row "Directed tolerances" (L287), and G4.3 (L350). CASE-239 is told as unbuilt.**
   - **The text:** "CASE-239 (Proposed, proposed study) is a forager that would learn its own criteria of failure."
   - **The record:** CASE-239's forager was "Built and run for LEAD-177 as CASE-421" (CASE-239). CASE-421 is Active, an executed study whose title includes "a forager that learns its own warning signs". The README's row (L253) says so: "CASE-239's design was run for a forager's criteria of failure as CASE-421 (Active), not for tolerances". The article and the README disagree.
   - **The fix:** In §4.4 add: "Its forager was built and run as CASE-421 (Active, executed study), for criteria of failure, not for tolerances." Add CASE-421 to the §4.10 row as well.
5. **Art. 6 L168 (§6.6), G6.5 (L289) and README L833–835 (open item 21). Which note records that CLAIM-1024's components went Active.**
   - **The text:** "CLAIM-1024's summary still says they are Proposed, and its note of 2026-11-23 records that this no longer holds."
   - **The record:** CLAIM-1024's note of 2026-11-23 records three of the four, CLAIM-1183, CLAIM-1029 and CLAIM-1194, and says "CLAIM-1202 is Proposed". The fourth is recorded by its note of 2026-11-24, "CLAIM-1185 and CLAIM-1202 Active".
   - **The fix:** In all three places, say "its notes of 2026-11-23 and 2026-11-24 record".

### C. Voices and consistency

6. **Art. 5 L53. "Handle the fixes for the twelve" is still read two ways.**
   - **The text:** "A reader should count these standings as the assistant's judgements, made at the owner's word. They are not the owner's rulings on each entry."
   - **The other files:** Overview L33 says this word "is also the owner's ruling on each of the twelve to fix, then promote, with the fix and the judgement that it was met left to the assistant". README L451–455 and Art. 6 L32 say the same, and Art. 5 L29 is compatible with them. Article 5's Limits contradict the reading the revision adopted (plan item 5).
   - **The record:** The curation entry 231157 lists each of the twelve as "fix, then promote". The histories use the one formula.
   - **The fix:** "A reader should count these as the owner's ruling, 'fix, then promote', on each entry, with the fix and the judgement that it was met the assistant's; the owner did not examine each entry."
7. **Art. 6 L222. The claim's title is quoted as the owner's words.**
   - **The text:** "The owner's reading of shareholder value maximization as 'a kind of willful ignorance with respect to the legitimate standing of a corporation's non-shareholder relationships' (CLAIM-tmpbucep …; U30)".
   - **The record:** That is the entry's title, in the filer's wording. The owner's U30 reads "shareholder value maximization as a kind of willful ignorance wrt legitimate standing of non-shareholder relationships" (CLAIM-tmpbucep, summary and body).
   - **The fix:** Quote U30's words, or mark the quotation as the claim's title.

### D. Quotation pointers

8. **Art. 4 L229. A pointer names no section of its source (minor).**
   - **The text:** "(curation entry of 2026-11-24 20:56, Art. 4 standing)".
   - **The record:** The curation entry has no such section. The finding is in the bullet "Standing told as settled", under §2 "Fidelity" of "U31 and A49" ("Art. 4's 'Implicit contracts and learned tolerances are shown to provide' (CLAIM-358, Proposed, interpretive: argued, not shown)"), and in §5's gap "Art. 4's 'are shown' overstates CLAIM-358".
   - **The fix:** Cite "section 'U31 and A49', 'Standing told as settled'".

### E. Joins: the count

9. **README L86 and L496 say "19 joins", and README L545 says "eleven are restatements".**
   - **What the articles hold:** Articles 4 to 6 close with **17** joins: J4.1, J4.2, JR4.1, JR4.2, J5.1 to J5.7 and J6.1 to J6.6.
   - **What Part B holds:** Its table has 17 rows, and its restatements are **ten**: JR4.1, JR4.2, J5.2, J5.3, J5.5, J5.6, J6.1, J6.2, J6.5 and J6.6. Part B's own tally ("In total there are 19 joins", "11 are restatements") is the source of the error. Its six categories sum to 21 because they count J4.1 twice and the two fidelity corrections as well.
   - **The fix in the manuscript:** "all 17"; "ten are restatements"; and "In all, 17: …", counting J4.1 once, as passed in a corrected form.
   - **For the record:** SYNTHESIS-tmp4tvbr repeats "19 joins" in its version-4 history note and in its Part II section ("closed with 19 joins"). This needs a dated note on the account, or a correction at its next review.

### F. README against the articles

10. **README L160, the Files table.**
    - **The text:** Article 4 has "gaps G4.1 to G4.3".
    - **The article:** It has G4.1 to G4.4 (L348–351).
    - **The fix:** "G4.1 to G4.4".
11. **README L730–731. The articles' items are not recorded.**
    - **The text:** "The articles' items are their revisers' (files 04 to 06), and are to be recorded here from their reports."
    - **The record:** Skill step 8 requires the README to say which plan items were taken, which not, and why. Items 3, 4, 7 and 8, and the article sides of items 2 and 5, are not recorded for Part II. Part I's section records them article by article.
    - **The fix:** Add them from the revisers' reports, or from the commits 88cb93af, 725ba896 and 9d5a8123.
12. **README open items 19 to 26 leave out owner choices that the Part II articles name as the owner's.** Skill step 6 asks for "Anything left open". The articles and the README's tables call each of the following the owner's, and none has a numbered item:
    - TERM-159 against TERM-160 (Art. 5 §5.3.1; the README only in tables, L262 and L418);
    - TERM-163's definition (§5.8.3);
    - CLAIM-1120 against CLAIM-997 (§6.4; LEAD-181's history says the choice "stays the owner's");
    - the concession of CLAIM-1185 on CLAIM-1024, "the owner's to write" (§6.6);
    - the reading of CLAIM-446's defeater (CLAIM-924; §6.5, §4.8.3);
    - whether CLAIM-1202 moves CLAIM-404's warrant (§6.6);
    - filing LEAD-141's intervention as a proposed study (§4.1.3);
    - whether CASE-382's fit meets LEAD-128's criterion for CLAIM-358 (§4.8.1);
    - the companion paper (§5.9).

    Some predate Part II, among them the CLAIM-1024 concession and TERM-163, which are in the curation entry's "Choices waiting on the owner". They are still not routed from this manuscript.
    - **The fix:** One open item, "Part II's owner choices", listing these with their sections.

### G. Points of contact (light check, plan item 9)

13. **The process history: the status pass's curation entry is cited nowhere in Part II.**
    - **The record:** Curation entry 2026/11/24/231157, "Status pass of 2026-11-24 at the owner's word", is the record of the promotions that the overview, the standing review and Articles 5 and 6 describe at length. Its "For the owner" section puts three of them to the owner's eye: "The interpretive promotion of CLAIM-1093, and the demonstrated promotions of A's CLAIM-1190 and the counter CLAIM-1185".
    - **Where it is plainly needed:**
      - Art. 5 §5.3.2 and G5.8, on CLAIM-1190's thin promotion;
      - Art. 6 §6.6, which gives CLAIM-1185 as Active "on a fix the assistant judged met";
      - Art. 5 §5.8.4, which leans on CLAIM-1093 (Active, interpretive);
      - the overview's "Who made the standings".
    - **The fix:** Cite the entry, and say that the pass itself flagged these three promotions for the owner's review. Add them to the open item proposed in F12.
14. **Art. 6 §6.3 (L122) and §6.7 (L190): CLAIM-340 (Active, demonstrated) is not cited.**
    - **The record:** "Scoring operators on predictions committed before the evidence is not by itself Regime B … commitment removes capture only when the interpretation bends the reading of the evidence no more than it bends the predictions". It is CLAIM-404's premise, and it answers the formal question QUESTION-121 asked.
    - **Why it bears:** §6.3 reports CASE-353's finding that a score the loop's own authority does not set prevents lock-in. In the review's Part C that finding includes commitment before evidence. §6.7 cites QUESTION-121 as Open. CLAIM-340 qualifies the first and is the held formal answer to the second.
    - **The fix:** Cite it in §6.3, and beside QUESTION-121 in §6.7.
15. **Art. 5 §5.4 (L152 onward): CLAIM-294 (Active, demonstrated) is not cited.**
    - **The record:** "Two inquiry histories can agree on every current conclusion and still call for different revisions of it, so a current marginal belief is not a sufficient state for updating on evidence about what it depended on".
    - **Why it bears:** It is the record's held, demonstrated form of "same answers, different development" for inquiry. §5.4 says the nearest statement is CLAIM-1156, which is Proposed.
    - **The fix:** Cite it beside CLAIM-1156 and CLAIM-1095. The section's "the record's nearest statement" holds for organizations only.
16. **Art. 6 §6.6 (L184) and §6.10: CASE-186 (Active, a proposed study) is not cited (optional).**
    - **The record:** A design whose "evidence generation, admission and scoring [are] separately lesionable", and whose admission × scoring arms "repeat CASE-162's".
    - **Why it bears:** It bears on "That would need one model hosting all four, LEAD-220 … which is not built".
    - **The fix:** Cite it as the held design nearest to LEAD-220's single model, or list it with a reason.
17. **Part C contacts neither cited nor listed with a reason.**
    - **Which:** CLAIM-1180 (Active, demonstrated; Part C names it beside CLAIM-1093 for §5.8.4), CLAIM-tmp3cywa (Proposed, member; §6.6), and ARG-218 and ARG-234 (Proposed; behind CLAIM-tmpjdml5, §6.6).
    - **Why it matters:** Article 4 lists its leftovers in "Points of contact not cited". Articles 5 and 6 have no such list, and the README has none for them. The owner's ruling of 2026-11-23, in skill step 8, asks that each be cited or listed with a reason.
    - **The fix:** Add a short list to Articles 5 and 6, or to the README.

## Tally

| Kind | Count |
|---|---|
| Who made an entry Active (A) | 2 (1 an error, 1 incomplete) |
| Statements the record does not hold (B) | 3 (one in three places) |
| Voice or consistency (C) | 2 |
| Quotation pointer (D) | 1 |
| Join count (E) | 1 (three places in the README; also in SYNTHESIS-tmp4tvbr and in the review's Part B) |
| README against the articles (F) | 3 |
| Points of contact (G) | 5 (one optional) |
| **Total needing a fix** | **17** |

## Verdict

The revision carried out the review's plan accurately. Every code exists. No parenthetical standing is wrong after the reruns of 2026-11-25. Every figure traced is in its entry. All five kept scripts reproduce what Article 5 reports. Every membership statement and every reliance count matches front matter. The joins' verdicts agree with Part B and with SYNTHESIS-tmp4tvbr.

The remaining problems are of three kinds:

- **Wording.**
  - Article 5's Limits still read the status pass's "twelve" against the series' adopted reading.
  - CASE-239 is told as unbuilt.
  - CLAIM-tmp7rl3d is given a `complements` it does not carry.
  - Two dates and pointers are off.
- **README bookkeeping.**
  - The joins are 17, not 19.
  - The articles' plan items are unrecorded.
  - Part II's owner choices have no open item.
- **Contacts.** A light pass found one process-history contact that matters: the status pass's own curation entry, which put CLAIM-1190, CLAIM-1185 and CLAIM-1093 to the owner. It also found two held results the articles should cite, CLAIM-340 and CLAIM-294.

None of these changes an argument. The full region-by-region contact search of plan item 9 was run only lightly here, as the brief asked.
