<!-- scratch/manuscripts/governance-of-becoming/FACTCHECK-2026-11-25-part-i-refresh.md -->

# Fact-check of the Part I refresh, 2026-11-25

This is an independent check under steps 8 and 9 of the write-manuscript skill ("Checking"). It covers the refresh of Part I:

- `01-identity-of-organization.md`;
- `03-contracts-we-become.md`;
- the head note of `superseded/03-cost-of-becoming.md`;
- `00-overview.md`;
- in the README: the Plan, the Files table, the numbering paragraphs, the Part I step-3a rows, the standing review's "Part I" column and "Part I's own premises", "The joins", the refresh note and the open items;
- the cross-reference edits in files 04 to 06.

It also covers the manuscript governance-of-possibility, Article 2 of the series: its fold of 2026-11-25 (c9df019a) and its full refresh (a1919541), with the codes made permanent, the standings, §14.7 (08-limits item 3) and its README.

The branch is `claude/manuscript-governance-of-becoming-part-i-refresh`, checked at d444f745. The checker did not write, refresh or audit the text. Line numbers are those of the files at d444f745.

**Sources.**

- `record/` as it stands on this branch.
- The verbatim exchanges, share/exchange.txt and share2/exchange.txt, and `motivating/` (A49, A51 and the precursor).
- The curation entries of 2026-11-24 (205621, 231157) and 2026-11-25 (022031).
- REVIEW-2026-11-24.md and REVIEW-2026-11-25.md, and LEFT-OUT-AUDIT-2026-11-25.md.
- The old files at e96cf5f3: `01-becoming-through-relations.md`, `02-contracts-we-become.md`, `03-cost-of-becoming.md`, and governance-of-possibility before the fold.

Another agent filed record entries in this worktree while the check ran (bfe4155b and 24 uncommitted entries). Statements that these overtake are listed in section G, not as errors.

**Method.** The scripts were adapted from the Part II fact-check, and the front-matter index was rebuilt from this worktree (11,271 entries, 10,928 `formerly:` aliases). Everything ran in the checker's scratchpad with `python3 -I`, and nothing in the worktree was changed except this file.

## What was checked

| Check | How | Count |
|---|---|---|
| Codes exist | Every `SCHEME-nnn` and `SCHEME-tmpxxxxx` in the eight governance-of-becoming files in scope and the eleven governance-of-possibility files, checked against `record/*.d/` and `formerly:` | 952 distinct codes, all on the record. The exceptions are file names (`REVIEW-2026`, `FACTCHECK-2026`, `OUT-AUDIT-2026`), ADR-tmpbdfmk named as ADR-143's former code, and the temporary codes that governance-of-possibility names on purpose: its README's map and its nine "filed as" mentions. No temporary code cited in Articles 1 and 3 has been made permanent, so "none has yet been given a permanent code" holds |
| Temporary-code replacement in governance-of-possibility | The README's map of 74 pairs checked against `formerly:`. Occurrences counted at c9df019a in files 00 to 09, the README, `background/` and `analysis/README.md`, leaving out REVIEW-2026-11-23.md and the analysis code. The remaining old codes found at HEAD | All 74 pairs agree with `formerly:`. 943 occurrences of exactly these 74 codes were there before the refresh, against the 942 the README states; the difference of one is the kept "filed as CASE-tmpo8bsc" in §9.1. Nine old codes remain at HEAD, every one in a "filed as" context. Eleven codes still temporary on the record are kept, as the README lists. REVIEW-2026-11-23.md and the analysis code are unchanged, and no record file was touched by a script (RETRO-007) |
| Quotations | Every double-quoted string, 3,305 of them, normalized for link markup, quote marks and whitespace. Each was matched first against the entries cited in its paragraph, then the two exchanges, `motivating/`, any record entry, the curation entries of 2026-11-22 to 25, the reviews and audit, and the old files | 2,657 matched in a cited entry, 223 in an exchange, 5 in a motivating draft and 257 in another entry. 76 were found only in manuscript documents (section titles, the owner's session words recorded in briefs and the README, the joins reader's words). 87 were unmatched. In Part I's files the unmatched ones are nested-quote artefacts and section titles, with one exception (C8). About 60 are in governance-of-possibility's unchanged text, quoting its own motivating draft, A48 of "Explain First Contact RL", which is not in the shares available here; the refresh did not change them, and earlier fact-checks covered them. Every quotation in the fold's seven blocks matched. Problems: 2 (C8, C9) |
| Standings | Four scripts. "CODE (status, warrant)": 1,408. "(CODE, …)" and parentheticals: 1,475. The status word in the 45 characters after a code: 1,873, with the 83 hits triaged by hand. Members of lists sharing one parenthetical: 130 | Problems: 4 (A1 to A4). The remaining hits were multi-code table cells, the "Status before the pass" column, or correct |
| Who made each entry Active | 96 history statements read against `history`: Article 1's six classes (50 entries), Article 3's four (35), governance-of-possibility's §14.7 and README (11). The overview's "Who made the standings" was checked against curation 231157, and the "seven" set Active at the assistant's discretion was counted by grep | Problems: 3 (B5 to B7) |
| Voices | Owner, A and assistant attributions in Article 1 (Voices, §§1.1–1.13) and Article 3 (Voices, the Active-footing list), checked against the summaries and histories of 30 entries | Problems: 1 (C10) |
| Figures | 112 numerals in Articles 1 and 3, each traced to the cited entry, with the bullets under a paragraph traced to its code by hand. The governance-of-possibility fold's figures were traced too: CLAIM-569, CLAIM-tmp8mpgs, CASE-315 and CLAIM-921 | No problems. Three kept scripts were rerun: `self_formation.py` for CASE-191, `maintainer_ladder_check.py` for CASE-268 and `soliton_testbed_checks.py` for CASE-265 (below) |
| Counts by script | The standing review's "Part I" column, against the codes cited in Articles 1 and 3. "Relied on by" in "Part I's own premises", recounted from front matter for 24 codes. The overview's "three not done" and "four". The joins tallies: 25 in Part I, 8 restatements of old file 03 | The Part I column matches for all 36 rows. All 24 reliance counts match. The tallies match |
| Numbering maps | The old and new headings of files 01, 02 and 03 against Article 1's table, Article 3's table, the README's numbering paragraphs and the superseded head note. Old joins checked against the old file's own verdicts | The section and join maps are right. Problem: 1 (D12, the head note and maps leave out Article 2's share of old §§3.2 and 3.6) |
| Drops | Every quoted string in old 01, 02 and 03 searched for in the live articles (01, 03, 04 to 06 and governance-of-possibility). Every code each old file cites, searched the same way. Each miss read by hand | Old 02 drops nothing (3 misses, all reworded in place). Old 01 drops two codes with stated reasons (CLAIM-1104 went with A49's anchors; CLAIM-tmp1nubb is Superseded) and some minor scope sentences (E13). Old 03 drops LIT-489 (North's essay, now cited through THEORY-429) and 101 quoted passages, all in sections its head note says were condensed (E14) |
| The reading of "handle the fixes for the twelve" | Every occurrence in the files in scope and in governance-of-possibility | It is read one way throughout: the owner's ruling on each to fix, then promote, with the fix and the judgement that it was met left to the assistant. Nowhere is "fix, then promote" in quotation marks as the owner's words. It appears only as the README table's "Owner's ruling" cell, a paraphrase of 205621's "promote after a stated fix 12". Problem: 1 (B6, a count, not the reading) |
| Joins test (ADR-075 step 5) | J1.8 and J1.9, against their components, the A51 text and the "Not stated on the record" sections of SYNTHESIS-040, 043, 046, 047, 049, 053, 077 and 079 | Part B below |

**Figures reproduced.**

- **CASE-191.** `self_formation.py` (with the scratchpad's numpy and scipy) gives the following.
  - The maintained state is S = 2.6180.
  - After formation, the internal-maintenance knockout leaves own and pulse at 0 and upheld at 2.6180, and the outside-supply knockout gives the reverse.
  - A frustration-production knockout from t = 0 leaves own at 0 and pulse at 2.6180.
  - This is Article 1 §1.7.3, steps 2 and 3.
- **CASE-268.** `maintainer_ladder_check.py` gives 0.1458 for the constant controller and 0.0104 at a delay of 0.03, and 0 for the exact law. Article 1 §1.5 says 0.146, 0.010 and 0.
- **CASE-265.** `soliton_testbed_checks.py` prints "all passed".

The other figures in Article 1 were traced in their entries' text:

- CASE-161: 80, 48 of 48, 32/36, 36/40, and 1.00, 0.18 and 0.00;
- CASE-163: 0.97055, 0.97093, 25.0 and 100.0;
- CASE-164: 0.42, and 0.55·H₂(1/3) ≈ 0.5051;
- CASE-189: 0.4, 0.5, 0.691 and 0.989;
- CASE-332: 0 of 64 against 64 of 64;
- CASE-333 and CLAIM-903: 0.2 per cent, 30 to 58, 0.47 and 0.996;
- CLAIM-953: 0.02 % to 30 %, and 0.2 % to 65 %;
- CLAIM-590: 1.866;
- CASE-265: c = 0.01;
- CASE-412: 0.147 to 0.894.

PerspectiveLab's runs (CASE-161, CASE-163, CASE-164) cannot be regenerated here, as the article says.

**What checks out.**

- Every promotion class in Article 1's "Who made the standing", all 50 entries, with their dates.
- The overview's seven assistant-discretion promotions. They are CLAIM-tmpq1lyz, CLAIM-tmpqbaic, CLAIM-tmpu5cap, CLAIM-tmpj4pw3, CLAIM-tmpnws9d, CLAIM-tmp8mpgs and CLAIM-tmpvic6m.
- The "twenty entries" of #794.
- The ten of "promote the ten" (CASE-346 and CASE-412 in Article 1, and CASE-326, CLAIM-892, CASE-343, CASE-397 and CASE-412 in Article 3).
- The 25 joins of Part I and their verdicts.
- The standing review's Part I column, and the reliance counts.
- The cross-reference edits in files 04 to 06. They include Article 5's restored CLAIM-603, CLAIM-670, CLAIM-568 and CLAIM-605, each with the right standing and promotion class, and the "old J3.10" label.
- In governance-of-possibility, the fold's standings and voices: CLAIM-571 and CLAIM-569 at delegated reviews; CLAIM-646 and CLAIM-755 Proposed and unchecked; CLAIM-580 the assistant's; CLAIM-tmp8mpgs at the assistant's discretion. Also §14.7 item 3's account of the two sorts of promotion, including its statement that the pass put CLAIM-1093's and CLAIM-1185's promotions to the owner (231157, "For the owner"), and CLAIM-1093's revision "at 'promote the ten'" (its version 2).

## Problems

### A. Standings

1. **Article 5 L49, L110 ("choosing between them is the owner's") and L112–113, README L407, L564 and open item 27 (L1147): TERM-159 and TERM-160 are given as Proposed, with the choice still the owner's.**
   - **The text:** "(TERM-159, Proposed; A58 §3's wording)"; "(TERM-160, Proposed; the assistant's wording)"; "Six choices … TERM-159 against TERM-160 (§5.3)"; README L564 "the owner's choice, open since U30".
   - **The record:** The owner ruled on 2026-11-25: "keep TERM-092 and add the joint term beside it for now". TERM-160 is Active ("Active at the owner's ruling of 2026-11-25", version 2) and TERM-159 is Deferred (version 2). The commit is 4c99f505, which is in the branch's base, e96cf5f3. So the refresh's recheck of standings should have caught it, as should the README's routing of item 27.
   - **The fix:**
     - In §5.3.1, give TERM-160 as Active and TERM-159 as Deferred, at the owner's ruling, quoted, and make the heading's "the term it waits on" past.
     - In L49, five choices, not six.
     - In README L407 and L564, give the ruling.
     - In open item 27, drop the bullet and add the ruling under "Closed since the last list".
2. **Article 1 L15 (the abstract). The count of Proposed executed studies is wrong.**
   - **The text:** "Its executed studies hold in simulated populations whose laws the modeller stipulates, and two of them are Proposed."
   - **The record:** L79 lists seven executed studies, and four of them are Proposed: CASE-163, CASE-332, CASE-333 and CASE-365 (each `status: Proposed`, `kind: executed-study`).
   - **The fix:** "and four of the seven are Proposed".
3. **README L371–372. Several Proposed executed studies are left out.**
   - **The text:** "Of the executed studies the series leans on, all are Active after #794 except CASE-163, and CASE-332 and CASE-333 in Article 1."
   - **The record:** CASE-365, Article 1's own run (§1.6), is Proposed. So are the memetic row's CASE-367, CASE-347, CASE-410 and CASE-362 (L359), and Part II's CASE-382, CASE-355 and CASE-330.
   - **The fix:** "except CASE-163, and CASE-332, CASE-333 and CASE-365 in Article 1". Either scope the sentence to the studies that Part I's designs rest on, or name the memetic and Part II exceptions.
4. **Article 3 L11. Not every temporary code is Proposed or Open.**
   - **The text:** "All are Proposed or Open, except CLAIM-tmp8mpgs (Active, §3.9)."
   - **The record:** CLAIM-tmp1nubb is Superseded, and L256 says so. LIT-tmpm8d98, LIT-tmphhs41, LIT-tmp1xqzu and LIT-tmpwdxhm are Deferred. L95 and L99 give two of these; L96–97 give no standing for the other two.
   - **The fix:** "All claims, cases, terms and leads are Proposed or Open, except CLAIM-tmp8mpgs (Active, §3.9) and CLAIM-tmp1nubb (Superseded, §3.6). The registered works are Deferred." Then add "Deferred" at L96–97.

### B. Who made an entry Active

5. **Article 3 L26. TERM-100 is said to have no promotion note.**
   - **The text:** "TERM-100's history records no promotion note."
   - **The record:** TERM-100, version 2 (2026-11-06): "Adopted at the twenty-fifth status review (ADR-057), at the status review's ruling (the owner delegated these rulings)". Article 1 L52 classes it correctly. The sentence is new at the refresh; neither old 02 nor old 03 has it.
   - **The fix:** Move TERM-100 to the delegated bullet (L24) and delete the sentence.
6. **Overview L33. All twelve are said to have been promoted.**
   - **The text:** "CASE-163 stays Proposed. … So the twelve, among them CLAIM-1115, CLAIM-1190 and CLAIM-1095 (Article 5) and CLAIM-1202 and CLAIM-1185 (Article 6), were promoted at the owner's word".
   - **The record:** Ten of the twelve were promoted. CASE-163 and CASE-164 were kept Proposed, each "with a note headed 'what holds it back'" (curation 231157, "The twelve"). README L465–466 says so.
   - **The fix:** "CASE-163 and CASE-164 stay Proposed" and "So ten of the twelve, among them …, were promoted".
7. **Article 3 L19 (minor). Three Active entries are missing from the list of those cited beside the argument.**
   - **The text:** The list "Further Active entries are cited beside the argument, not as its steps".
   - **The record:** It leaves out three Active entries the article cites: CASE-315 (§3.9.2), THEORY-345 (§3.8.2) and THEORY-1050 (§3.3).
   - **The fix:** Add them. All three were made Active as their histories say; CASE-315 at "promote the ten".

### C. Quotations, pointers and voices

8. **Article 1 L79. The quotation from CASE-161 is altered.**
   - **The text:** CASE-161's figures were "read again" at its promotion "and agree. The runs were not regenerated."
   - **The record:** CASE-161, version 2: "… was read again from … and agrees. The runs were not regenerated."
   - **The fix:** Quote "and agrees", or take the words out of quotation marks.
9. **governance-of-possibility 03-time.md L149 (§7.5, from the fold). A pointer names the wrong source.**
   - **The text:** "(CLAIM-755, Proposed, demonstrated; ChatGPT's, §3.1)".
   - **The record:** CLAIM-755 is "A's, from A39 §3 of the exchange 'Topological protection explained'" (its summary). Old 03 had "ChatGPT's, A39 §3", and Article 3 §3.8.1 has "A39 §3".
   - **The fix:** "ChatGPT's, A39 §3 of 'Topological protection explained'".
10. **Article 1 L441 (G1.7). CASE-265 is counted among the assistant's constructions.**
    - **The text:** "The assistant's constructions and runs cited here as rungs and withdrawals, CASE-265, CASE-268, CLAIM-693, …".
    - **The record:** CASE-265 is A's model, "From A5 §§5.1–5.4 of the exchange 'Explain String Theory'", with every number recomputed by the filer (its summary). Article 1's own Voices (L73) and the README (L350) say A's.
    - **The fix:** "The constructions and runs cited here as rungs and withdrawals (CASE-265, A's model with the filer's numbers; the assistant's CASE-268, CLAIM-693, CASE-332, CASE-333, CASE-365 and CLAIM-953) carry no recorded check by a session other than their filer's."
11. **Article 1 L123. J1.9 is said to have been tested.**
    - **The text:** A51's thesis "is A's integration, and §1.13 tests it against the record (J1.9)".
    - **The other files:** L428 says J1.9 "has [not] been put to ADR-075's step 5", and L431 says "The article reports it and does not assert it".
    - **The fix:** "§1.13 sets it against the record (J1.9)". The verdict in Part B below can then be cited.

### D. The superseded note and the numbering maps

12. **The superseded file's head note (L7 and L9), Article 3's Numbering table (L66–67) and README L220–224 leave out Article 2's share of old §§3.2 and 3.6.**
    - **The text:** §3.2 is "condensed into A51's Article 3 … §3.8". §3.6 is "condensed into Article 3 §3.9 (lock-in and exit), with §3.6.3 in full".
    - **The record:** governance-of-possibility's dated note of 2026-11-25 (README, table under "readiness folded in") also took:
      - §3.2.1 into GoP §11.1, "The three requirements, worked";
      - §3.6.1 and §3.6.2 into GoP §2.4, "Holding, reaching and the direction of travel";
      - §3.6.3's neighbours into GoP §11.3.

      The README's Plan (L164–168) names those sections, but the head note, which says where each section went, does not.
    - **The fix:** Add "and, by governance-of-possibility's own refresh, to Article 2 §11.1" to the §3.2 bullet. Add "and to Article 2 §2.4 (§3.6.1–3.6.2) and §11.3 (§3.6.3's neighbours)" to the §3.6 bullet. Make the same change in the two maps.

### E. What was dropped

13. **Old file 01 (minor).** The cross-reference pass's flag was checked. Old §1.3's sentence was: "So a productive cycle is the minimal structure a persisting capacity needs, under that claim's hypotheses, and having one does not make an organization internally maintained."
    - **It is not dropped.** §1.4 (L154) keeps it in substance:
      - the run-in heading "A persisting capacity needs a productive cycle, and a cycle is not closure";
      - the hypothesis, "Where every constraint capacity turns over and is produced only by others";
      - CLAIM-516's "necessary and not sufficient".
    - **Lost:** the word "minimal", and the explicit consequence that having a cycle does not make an organization internally maintained.
    - **The fix (optional):** Restore the clause after the CLAIM-516 quotation.
    - **Other minor scope sentences of old 01 with no stated home:**
      - CLAIM-194's "The claim does not say that production is measurable wherever coupling is";
      - CLAIM-521's "as tightly integrated at the edge of collapse as well inside the regime";
      - CLAIM-474's note of 2026-11-22 on CASE-333 ("made the achievements … come apart on purpose");
      - QUESTION-281's note, "two of the three achievements come apart, each way";
      - old §1.5.2's critique of A49's design list (removing initiating supports acts on the mechanism that initiated the organization, not the one that maintains it). This one has an implied reason, "A49's Article 1 is background only" (L42).

      None changes an argument. The first and last are worth one clause each.
14. **Old file 03.** 101 quoted passages are not in the live articles. All fall in sections the head note says were condensed, and the substantive points were found in their new homes. Lost in condensing, with "condensed" as the only reason given:
    - CASE-326's three case results (the bugs lose at 1 and 1.5 and win from 2; a saving of 11 turns into a loss of 1 at three uses; "a bin never pays") and its "7 tests" rerun;
    - CLAIM-591's clause that connectivity "does not settle reachability";
    - THEORY-863's "a random walk with absorbing barriers";
    - "Some persistent structure saves no work".

    LIT-489 (North) is cited through THEORY-429. Not an error. A sentence in the README's refresh note saying the cost-model cases are condensed to their terms would make the omission explicit.

### F. For the owner, not an error

- The Part II fact-check (its C6) said that curation entry 231157 lists each of the twelve as "fix, then promote". It does not. The words are the README table's paraphrase, in its "Owner's ruling" column, of 205621's "promote after a stated fix 12". The adopted reading does not depend on it, and no file now quotes the phrase.
- The left-out audit's C4 (extend open item 7 to TERM-123, CLAIM-690 and CASE-264) is a section C item, so the refresh was not bound to take it. Open item 7 still lists TERM-124 only.

### G. Overtaken while the check ran (not errors)

Commit bfe4155b and the uncommitted entries now hold several things the refreshed text calls unfiled or not done.

- **G1.2: done.** It is now CLAIM-tmpv6tw7, whose title begins "With a supply multiplying its production terms, a maintained connector shows the ignition threshold, the collapse below a supply fold and the outage …". This affects:
  - Article 1 L436 (G1.2);
  - README L363, the step-3a row, which says "not done";
  - the overview's "three are not done" (L17);
  - README L380–382 ("only the comparison … and the computation on CASE-189 are not done at all").
- **New leads and questions.**
  - G1.6: LEAD-tmp81wwz.
  - G1.7: LEAD-tmpc0rqa.
  - G3.5 and the fourth item of G4.3: LEAD-tmpobng3.
  - The second item of G4.3, and G6.3: LEAD-tmpotdfw.
  - The recurrence of learned accommodation: LEAD-tmpqn4dk.
  - The second realizer: LEAD-tmpb2w1a.
  - G3.4: QUESTION-tmpp8ue3.
  - G5.6: QUESTION-tmplkq92.
  - G6.1: LEAD-tmpv3s18.
  - J4.1's measurement: LEAD-tmp8nbac.
- **Readings registered.** Coase and Williamson are LIT-tmp9hjn2 and LIT-tmpg47ie. Article 3 L102's "no reading of Coase or Williamson" still holds, since they are registered and not read, but G3.3 can name them.
- **The README's "none made here" (L310–318)** is overtaken for most of the filings it lists.

## Part B. The joins under ADR-075 step 5

The reader tested both new joins against the three routes, which are:

- a coherent case in which every component holds and the join fails;
- a valid, nontrivial derivation held by no CLAIM;
- a discriminating prediction.

It also searched the accounts' "Not stated on the record" sections for an earlier decline.

| Join | What it is | Declined by an account? | Verdict |
|---|---|---|---|
| J1.8 (§1.11) | The negative results as one table, with A51 §5's "what not to infer" column, read as A51's "Behavior does not identify organization" and "Coordination does not establish individuation", "each in its stated model" | Not this join. SYNTHESIS-043's "Capability as not one quantity" declines the same shape: "a conjunction of the separations, which cannot fail while they hold". SYNTHESIS-079's "One ladder of what separates" declines an ordering of such steps, which the table does not make | **RESTATEMENT.** A conjunction of its rows, each held by its own entry in its own model, and the table is A51 §5's (its rows for CASE-161, CASE-163, CASE-164 and CASE-346 are A51's nearly word for word). No case can have every row hold and the table fail, since the table asserts nothing beyond its rows. No derivation is made, and no outcome is settled. The article's own label is right. This is the same verdict as Part II's J6.6, "the four non-equivalences as one list". Two fidelity corrections, below |
| J1.9 (§1.2, §1.13) | A51's thesis that "organizational identity" is "a plurality of related achievements rather than a single equivalence relation", which the article maps to TERM-088, CLAIM-474, CLAIM-405 and CLAIM-590 | No account tests it. The nearest decline is SYNTHESIS-043's "Capability as not one quantity", above. The audit of A49 classes the articles' abstracts as "Recaps (fail: a conjunction or relabel of held entries)" (205621, §4) | **Correctly not made. As a claim it FAILS.** See below |

**J1.8: the fidelity corrections.**

- **Row 6** says "A habit of matched memory reproduces every intervention one model can receive (CASE-346)". CASE-346 says the habit reproduces "the responses to belief correction, authority reset and restored evidence", and "Only interventions on the evaluation tell the two apart". CLAIM-924 says the same. A51's row says "reproduces available interventions". The fix: "reproduces the responses to every intervention but one on the evaluation".
- **Row 8** says "Dependence deepens without a new individual (SYNTHESIS-053; CASE-177)". CASE-177, as §1.8 quotes it, shows dependence growing "with no new collective function", which is not the same as "no new individual". That interdependence is not individuality is held in QUESTION-277's notes (the Black Queen route, as SYNTHESIS-053's "Not stated" section says). The fix: cite QUESTION-277's note beside SYNTHESIS-053, and give CASE-177's result in its own words.

**J1.9: why it fails.** The thesis has two readings.

- **The weak reading** says that no single equivalence relation fixes identity across the senses and criteria the record keeps apart. It follows trivially from TERM-088's "are not stages", with CLAIM-405's relativity to a criterion and CLAIM-590's relativity to a category. It is a restatement, and the derivation is too short to be a contribution.
- **The strong reading** says that even for a fixed sense and criterion an organization's identity is a plurality rather than one relation. It has a free parameter. Neither "organizational identity" nor "related" is fixed by any component.
  - The components concern senses of individuation (TERM-088), an order of achievements (CLAIM-474), verdicts relative to a fixed criterion (CLAIM-405, which says that "once the criterion is fixed a verdict can be false") and the sameness of configurations, not of organizations (CLAIM-590).
  - Any case in which a single fixed-criterion relation decides identity is absorbed by counting it as one member of the plurality, so no separating case can be stated. This is ADR-075's third guarded failure.
  - No prediction separates it from its components.

The record also holds a single criterion for identity over time, causal transmission (CLAIM-329, Active; CLAIM-615, Proposed). It also keeps "Numerical organizational identity" apart from resemblance and descent (A40, in CLAIM-417). So the weak reading is about individuation rather than identity.

**The fix:** §1.13's last bullet should name CLAIM-329 and CLAIM-615 beside the four parts, as the record's one criterion of identity over time. The verdict goes to SYNTHESIS-tmp4tvbr's Part I joins section, under "Not stated on the record", as "a recap on the weak reading, a free parameter on the strong". J1.8 goes there as a restatement.

## Tally

| Kind | Count |
|---|---|
| Standings (A) | 4 (A1 in six places) |
| Who made an entry Active (B) | 3 (1 minor) |
| Quotations, pointers and voices (C) | 4 |
| The superseded note and maps (D) | 1 (three places) |
| Drops (E) | 2 (minor; neither changes an argument) |
| **Total needing a fix** | **14** |
| Overtaken (G), not errors | 13 statements |

## Verdict

The refresh carried out A51's order accurately:

- Every code exists.
- Every temporary-code replacement in governance-of-possibility agrees with `formerly:`.
- Every figure traced is in its entry, and the three reruns reproduce Article 1's numbers.
- The section and join maps match the files.
- Article 1's 50 promotion statements, the standing review's Part I column and all 24 reliance counts match the record.
- "Handle the fixes for the twelve" is read one way everywhere, without quoting "fix, then promote".
- Nothing in old file 02 was dropped. The cross-reference pass's flag on old §1.3 is a near miss, not a drop.

The problems that matter are four:

- the owner's ruling on TERM-159 and TERM-160, which landed before the branch was cut and is still shown as open in six places;
- Article 1's abstract, which says two of its executed studies are Proposed where four are;
- Article 3's new and wrong statement that TERM-100 has no promotion note;
- the superseded file's head note, which sends old §§3.2 and 3.6 only to Article 3 when Article 2 took parts of both.

The joins: J1.8 is a restatement, with two fidelity corrections. J1.9 was rightly not asserted, and it would fail if made.
