<!-- scratch/manuscripts/governance-of-becoming/REVIEW-2026-11-25-part-iii.md -->

# Review of Part III's first drafts, 2026-11-25

The independent review (write-manuscript skill step 7) of Articles 7 to 9 (files 07–09), at the owner's "get started on part III". Three readers who did not draft: Part A, the main review; Part B, the joins under ADR-075 step 5; Part C, the points of contact the drafts do not cite. Each part is the reader's report as written, under its own heading. The drafts are committed unchanged.

# Part A. The main review



This is the main reviewer's report under step 7 of the write-manuscript skill. I did not draft Part III.

**What I read.** In full: `07-memes-that-make-worlds.md`, `08-what-we-owe-through-cooperation.md` and `09-political-economy-of-dependence.md`. For their framing I read `00-overview.md`, the README's section list and open items, and Part II's review (Part A) as the house standard. I read A51's Movement III (Articles 7 to 9) and its §5 and §7 (`motivating/A51-publication-programme.md`), and A49's Articles 7 to 9 and its experiment families. I read the three digests' step-3a sections. I also read `analysis/fallback_decay_bargaining.py` and its README, and the verbatim exchange "Memes, Contracts, and Systemic Normativity" (U1 to A49), always under `python3 -I`. I read every cited entry a check needed.

**Which record.** I checked against this branch's working tree, at HEAD c03cb31a. That includes commit 39a0a7dc ("Part III: file the drafts' joins and gaps", 06:31 UTC), which came after the drafts were committed (4a3a6de9, d6f7fa06 and 6b21bd40, 06:13 to 06:15 UTC). Standings come from front matter. No cited entry changed status between e96cf5f3, the drafts' stated base, and HEAD.

**How I worked.** Read-only. I wrote only this file. I ran no git command that changes state, and no `luria` command. I sent nothing to any outside service.

- **Scripts.** Scripts in the reviewer's scratchpad (`rev3/`) indexed `record/*.d`. They checked codes, quotations, parenthetical standings, turn attributions, numerals, reliance counts and membership, and searched held work by mechanism. Every miss was then checked by hand.
- **The kept script.** I reran `analysis/fallback_decay_bargaining.py` with `python3 -I`. Its output is byte-identical to `fallback_decay_bargaining.2026-11-25.txt`. I recomputed CLAIM-602's and CLAIM-605's fixed points and times on my own.
- **Re-checks.** Each correction in section 2 was checked a second time against its entry before I wrote it here, and is marked confirmed.
- **Not done here.** I did not judge whether the joins should be admitted under ADR-075. I did not run the full region-by-region search for points of contact. The contacts in 1.2 came up during the step-3a searches.

## Verdict

At the level of the single step, the drafts are careful and almost always exact.

- **Codes.** All 276 distinct codes exist.
- **Quotations.** I checked 593 quoted strings. None is wrong in substance. The four misses are quotations within quotations, where the drafts turned the entry's inner `"` into `'`.
- **Parenthetical standings.** All 283 match front matter, for status, warrant and kind.
- **Figures.** Every figure I traced is in its entry or in the script's output. The kept script reproduces byte for byte, and all 36 of §9.4's figures match it.
- **Disclosure.** Each article says early who made its Active entries Active, and the lists are right, with four omissions.
- **Use of A51.** The drafts treat A51 well. They decline A51's closing sentence on morality (J8.5). They decline enshittification as domination (J9.5). They give the cross-domain dependence account at its standing, find that SYNTHESIS-005 is Superseded, and cite executed work A51 does not name.

Five things keep the drafts from going to a fact-check.

1. **They predate the filing of their own joins and gaps.** Sixteen minutes after the drafts, commit 39a0a7dc filed the following:
   - CLAIM-tmp6nzs1, the §9.4 computation;
   - five leads, a question, and Barthes (LIT-tmpflbme);
   - dated notes on eleven entries, which state J7.1, J7.4, J8.1, J8.2 and J8.3;
   - the analysis README and the dated output.

   About thirty sentences now say "not on the record", "no entry states it", "candidate" or "uncommitted". The notes also put the drafter's own joins into the record before ADR-075's test. A join test that asks "Stated by an entry?" would now find the manuscript's own words there.
2. **Step 3a missed held work in four places.** Two of them bear on the drafts' central "not done" claims:
   - **Hidden subsidy.** CASE-412, CASE-343 with CLAIM-921, and CLAIM-679 have run the budget-to-observed-use half of CLAIM-700's loop. CLAIM-679 is CLAIM-700's own premise.
   - **§9.4's missing step.** A24 §4's model, in CLAIM-tmp2jhc1's own body, already moves the split as B's capacity falls.
   - **The seed's withdrawal.** CASE-308 with CLAIM-865, and CASE-365 with CLAIM-952, are executed withdrawal studies of a seed.
   - **The name and the line.** CASE-411 with CLAIM-1158 studies succession from public records: recognition followed the maintainers, not the name.
3. **Scope moves in the headline results.**
   - Article 9 says the terms move while "no term is rewritten". In its model, though, the split, which is the term, is re-bargained at every instant.
   - Its G9.1 says the computation answers LEAD-tmpeo8wq "under both of its readings". On the lead's second reading, the lead's own null applies.
   - Article 8's J8.1 calls defeated standing a "policy-level" failure. Its two cases differ in their histories, which is CLAIM-741's endpoint–history separation, not its policy–history one. SYNTHESIS-102's Arm B has already failed an application of the same form.
   - Article 7's abstract states J7.4 as a finding. It also says no study of real people is the record's own, which CASE-410 contradicts.
4. **One error about A51, and departures from it that go unsaid.** CLAIM-741 is not in A51's backbone, and A51 never names it. Seven backbone accounts go unused and unexplained: SYNTHESIS-025, -038, -092, -093, -101 and -103, the first for Article 7, the second for Article 8 and the last four for Article 9. So do some phrases of A51's abstracts (§1.4).
5. **Consistency.**
   - The overview and README carry nothing of Part III.
   - Article 9 calls Part I's J2.3 "J3".
   - Each article lists different housekeeping leads.
   - Only Article 7 lists the points of contact it leaves out.

None of this needs new research. The revision is:

- a sync pass against 39a0a7dc;
- four step-3a citations, two of which change verdicts;
- three scope corrections in Article 9 and Article 8's J8.1;
- the A51 points;
- editing.

## 1. Structural problems, ranked

### 1.1 The drafts predate the filing of their own joins and gaps (all three articles)

The drafts were committed at 06:13 to 06:15 UTC, and commit 39a0a7dc followed at 06:31. Its changelog fragment reads: "a Proposed claim from the assistant's computation …; five leads …; a question on entrusted authority …; Barthes registered Deferred; dated notes on eleven held entries". These statements are now false or stale:

- **Article 7:**
  - line 76, "Barthes's essay is not yet registered": it is LIT-tmpflbme, Deferred;
  - line 130 and the table's row at line 178, "No field case of hyperstition with a withdrawal is on the record": still true, but LEAD-tmp5msck now holds the search;
  - line 185, LEAD-tmpiktom's "holds none": its note of 2026-11-25 corrects this;
  - line 189 (§7.8), the reading of complex contagion: LEAD-tmplsxtr now holds it;
  - line 208, J7.1, "No entry states it": CLAIM-tmpjitli's note of 2026-11-25 states it;
  - line 211, J7.4, "Not stated, and neither entry cites the other": CLAIM-tmphq6hp's note of 2026-11-25 states it and cites CLAIM-946.
- **Article 8:**
  - line 101, "a candidate dated note", and J8.3, line 267: there are now notes on CLAIM-723 and CASE-316;
  - J8.1 (line 265), "Stated by an entry? No": CLAIM-741's note of 2026-11-25 states it;
  - J8.2 (line 266): there are now notes on CLAIM-1184 and CLAIM-913;
  - G8.2 (line 276), "This needs a dated note on the account": SYNTHESIS-tmp4tvbr carries one, dated 2026-11-25;
  - G8.3 is now LEAD-tmphsmng;
  - G8.4 is now QUESTION-tmpeiurf;
  - G8.5 is filed as the notes above;
  - G8.6 (line 280): CLAIM-741 now has its "what holds it back" note.
- **Article 9:**
  - line 104, "It has not been put to the record … with the script uncommitted";
  - line 146, "What would go back to the record";
  - line 232, "Not on the record; a candidate claim";
  - J9.1 (line 248), "No entry states it";
  - G9.1 to G9.3 (lines 257 to 259).

  These are now CLAIM-tmp6nzs1 (Proposed, demonstrated), `analysis/README.md` with the dated output, LEAD-tmpfzx2c (G9.2) and LEAD-tmp3w42f (G9.3), with notes on LEAD-tmpeo8wq and CLAIM-tmp2jhc1.
- **SYNTHESIS-tmp4tvbr's new note.** It cites "Article 7's list of inconsistencies" for the stale U4 item ("The owner chooses"). Article 7 has no such list, and does not mention that item.

**A process point that goes with the sync.** J7.1, J7.4, J8.1 and J8.2 are joins. All four are untested ("None has been put to ADR-075's step 5 yet"). They were filed as dated notes on their components. Skill step 6 asks that joins no entry maps to be filed as accounts, and as Proposed claims where the join test passes.

Filing them as notes does two things:

- It puts the drafter's sentence into the record before the independent reader sees it.
- It makes the join test's "Stated by an entry?" circular.

The overview already warns that "the record and this draft are not independent everywhere". Each article should say so for these notes. The joins reader should be told that the notes are the manuscript's own. After the verdicts, the joins go where step 6 sends them.

**Recommendation.** Make one pass against 39a0a7dc:

- cite CLAIM-tmp6nzs1 and the new leads, question and LIT;
- turn "candidate" into "filed (date)", with "from this draft" for the notes;
- drop or close the G-items that are now filed;
- restate J7.1, J7.4 and J8.1 to J8.3 as "stated since in a note filed from this draft";
- add Article 7's missing item on SYNTHESIS-tmp4tvbr's U4 part, or correct the account's note.

### 1.2 Step 3a: held work the drafts report as not done (Articles 7 and 9; one in Article 8)

The drafts list held work before proposing anything, and that is good. But four of the "not done" or "no entry" verdicts miss work that does part of the job. One smaller miss is in Article 8.

- **The hidden-subsidy loop (Article 9 §9.6, line 174).** The draft says "No run of the hidden-subsidy loop is held. CLAIM-700's study, A33 §10A … is not run." A33 §10A's design, quoted in CLAIM-700, is "Construct two institutions with identical obligations and equivalent present performance", one with reconfiguration slack and one without, "and introduce a failure that needs a transition". The record holds the following:
  - CASE-412 (Active, executed study): "A matched-performance model of regulation run under six budget regimes: every regime produces the same output until a contingency arrives, while readiness at a deadline of six periods ranges from 0.147 to 0.894". That is A33 §10A's design, run.
  - CASE-343 (Active, executed study) and CLAIM-921 (Active, demonstrated; a member of this work): "a budget that follows observed use has a state in which the capability is never used or funded again".
  - CLAIM-679 (Active, demonstrated), which is in CLAIM-700's own `rests_on`: cutting toward what the present configuration needs "removes exactly the transitions whose threshold lies between the old holding and the new".
  - CLAIM-1099 and CLAIM-1180 (Active, demonstrated), on the peak rule and the reserve.

  None of these cites CLAIM-700. The right verdict is *done in part*. The budget-to-observed-use half and the matched-performance contrast have been run. The coupling has not: compensation masking the shortfall, so that the rule reads it as adequacy. The miss goes back to the digest's §9 row ("not done as a model"). Article 9 should cite them. Part I's file 03 §3.7.4 (J3.7) already joined CLAIM-921 to CLAIM-tmp2jhc1's reserve, so the series has the link. CASE-412 should get a dated note pointing to CLAIM-700.
- **The step §9.4 calls missing (Article 9 line 102).** The draft says "In the second, the outside option is set by hand. No entry joins them, so no model has the terms moving as the fallback decays." But CLAIM-tmp2jhc1's own body, which §9.3 cites, holds A24 §4's model. In it, specialization "lowers B's independent capacity (5(1 − s(1 − p)))", and the split moves from "14.75 to 11.25 in A's favour" to "12.25 to 13.75" with protection (checked with `python3 -I`).
  - That is the terms moving with a fallback that the arrangement erodes, as comparative statics.
  - Part I's file 03 §3.7.4 and its J3.10 say so, as does LEAD-tmpeo8wq's second note of 2026-11-24.
  - The digest's own §9 row reads "done, for the static model … CLAIM-tmp2jhc1's Nash step and A24 §4's model".

  The right verdict is *done in part, statically*. What §9.4 adds is the dynamics, the deadline and the reversal test. "No model has the terms moving as the fallback decays" is literally true only with "decays" read dynamically. Say so.
- **Withdrawing or varying the seed (Article 7 §7.7, lines 172–173).** The draft says "Vary the seed, hold the receiver | not done | none", and gives "Withdraw the seed after formation" as *done in part, formally* by CASE-189, CLAIM-463 and CLAIM-tmpnws9d. The record also holds the following:
  - CASE-308 (Proposed, executed study): a scaffold that forms and holds a nucleus, "withdrawn for good at chosen states". With it, CLAIM-865 (Proposed, demonstrated): "the assembly becomes independent of the support before it is complete only where what it has built holds the nucleus or no longer needs it".
  - CASE-365 (Proposed, executed study): "withdrawal becomes safe on crossing a separatrix". That is CLAIM-tmpnws9d's crossing condition, in an executed kinetic model. With it, CLAIM-952 (Proposed, demonstrated), on repair against production.
  - CASE-389 and CASE-374 (Proposed, executed studies), on which seed sets and which seams yield which organization. They hold the receiver fixed and vary the seed, in assembly models.

  None of these is memetic, so "done in part, in assembly models" is the right verdict. They also bear on J7.2, the one shape of outlasting, and on JR7.1.
- **The name against the line (Article 7 §7.7, lines 174–175).** The rows are "Replace participants | done in part" and "Carrier against concept | not done". CASE-411 (Proposed, executed study, documented) and CLAIM-1158 (Proposed, empirical) code eleven open-source successions from public records. They find that "recognition followed the maintainers and not the name". That is the record's own study of real organizations, on what persists when the carrier (a name) and the organization producing it come apart. It is CLAIM-280's and CLAIM-621's distinction, in a field case. Cite it in both rows. It also falsifies the abstract's "No study of real people … is the record's own here" (correction 2.2).
- **Smaller (Article 8 §8.10, line 242).** "No case of care for non-reciprocators beyond A24's text": THEORY-1569 (Active) reports Gardiner's climate argument. It joins a commons problem to "an intergenerational one that institutions and reciprocity cannot solve, because the generations do not coexist". That is a read case of consideration owed to those who cannot cooperate. It bears on CLAIM-tmpreipd's step 4. Cite it.
- **Smaller (Article 7 §7.3 and Limits, line 52).** CLAIM-415's first clause ("a false unity") has read grounds: Prentice and Miller (LIT-1370), Lerman et al.'s majority illusion (LIT-1390; THEORY-887, Proposed) and Vilone and Polizzi (THEORY-242, Active). The draft cites none of them. The Limits' list of human evidence should include them. NOTE-1085 also discusses threshold models (Granovetter, Watts, Centola) while saying "no contagion is simulated". That bears on §7.8.

### 1.3 Scope moved, mostly one way (Articles 7 to 9)

- **"No term is rewritten" (Article 9, abstract line 7; line 126; line 181).**
  - The abstract: the decaying capacity "moves the split against the party while it never exits and no term is rewritten".
  - Line 126: "The terms move with no exit and no rewritten term".
  - Line 181: justified withdrawal "comes to fail with every term unchanged".

  In the model, P's share is the symmetric Nash split, recomputed at every t against the current fallback (`nash(outside_option(c, 605, R))` at each step). The split is the term, and it is re-bargained continuously. What is fixed is the supply arrangement, and that P stays in. Say "with no exit and no change in the supply arrangement; the split is re-bargained against the current fallback, an assumption of the model". The same wording sits in CLAIM-tmp6nzs1's title ("moves the terms … while it never exits"), which is fine. It also sits in LEAD-tmpeo8wq's new note ("With no transition's price changed"), which needs the next point.
- **"Under both of its readings" (Article 9 §9.4, line 110; result 4, line 129; G9.1, line 257).** LEAD-tmpeo8wq's second note of 2026-11-24 gives two readings:
  - "*Capacity is the actor's state* … the decline meets the success condition";
  - "*What it costs i to reach a configuration includes rebuilding the capacity.* The decline is then a rise in i's incoming costs … and the null applies."

  The draft maps the current-output valuation to the first reading and the forward valuation to the second. On that mapping, the deadline shows in the terms only under the second reading (result 4), and under the second reading the lead's own null holds: the dependence is a price change. So the two headline results hold under different readings:
  - the terms move with no price change, on reading 1;
  - the deadline is a deadline for the terms, on reading 2.

  G9.1's "answers it for a scalar capacity under both of its readings" overstates. Say which result holds under which reading. LEAD-tmpeo8wq's new note ("the terms move on both … so for a scalar capacity the shrinkage moves the terms either way") needs the same qualification.
- **J8.1, "a policy-level failure" (Article 8 §8.4.4, lines 123–125; J8.1, line 265).** CLAIM-741 has two separations.
  - The first is distinctive. Two arrangements produce the same history "whenever the right is not exercised against them". Only the policy differs.
  - The second: "two histories can reach the same endpoint and differ in whether a power was exercised".

  CLAIM-723's case where "the objection would have failed", and ARG-228's utilities, are of the second kind:
  - In CLAIM-723's case, the respecting arrangement hears the objection and the defeating one makes the act irreversible first.
  - In ARG-228's case, O₁ registers the complaint and O₂ files it "as a non-incident".

  The histories differ, and an evaluation over histories can see the difference. Only an evaluation over endpoints cannot. So the join's sentence, "a policy-level failure that no evaluation over realized outcomes can represent", should read "a difference in history that no evaluation over endpoints can represent". The policy reading would apply only where no objection would have been made.

  There is also a precedent the join must face. SYNTHESIS-102's Arm B tested "CLAIM-745 with CLAIM-741: a categorical gate fails a right … at the level of policy" and failed it: "it is a substitution instance of CLAIM-741's second separation …, an inference CLAIM-741 already holds". J8.1's "Declined by an account? No" is true of its exact predicate. But the account declined an analogous application, and the reader should be told. The same correction applies to CLAIM-741's new note of 2026-11-25.
- **J7.4 told as a result (Article 7, abstract line 7).** The abstract says: "A second simulation finds that restoring a deviation, the record's proposed mark of an operative norm in a different setting, is passed by plain conformity." CASE-362 tested restoration as a mark of a shared perspective (TERM-148), not of a norm. Its bearing on CLAIM-tmphq6hp is the article's join J7.4, which "may fail, because the objects differ" (line 161). Say "restoring a deviation, which the record proposes as a mark of a shared perspective, is passed by plain conformity; whether that bears on the operative-norm marker is this article's join".
- **"Only the probe … registered the move" (Article 7 §7.5, line 149, J7.3).** In the adaptive arm, concentration and fit also rose, as they did in the fixed arm. Only the probe *separated* the two arms. Say "separated".
- **"A bargaining disadvantage is not exploitation" (Article 9 §9.9, line 209).** The entry says "not by itself exploitation" (CLAIM-670's note, quoting A22). As written, it denies an identity and drops the scope. Say "does not by itself establish". Do the same for "Dependence is not domination", which is A51 §5's "does not establish".
- **"The record's own position" (Article 9 line 240).** Every entry it names is Proposed: TERM-123, TERM-124, CASE-264 and CLAIM-682. Say "the record's position, in Proposed entries".
- **Two joins not listed.**
  - Article 9 line 181 joins §9.4 to CLAIM-686's exit half ("one way justified withdrawal comes to fail"). In §9.4's arm A, P can still exit. Its exit is worth less (o_P → 0.399 by t = 6), which is not the same thing as exit failing.
  - Article 7 line 93 says "the invitation is the encounter-level form of the seed".

  Each is the article's own integration, and should be numbered among the joins.

### 1.4 Scope against A51

- **A misstatement.** Article 8 line 25: "Two are in A51's backbone for this article: CLAIM-671, and CLAIM-741, which is A51's opening move." A51's Article 8 backbone is SYNTHESIS-038, -092, -102, -103 and -104, with CLAIM-075, -671, -738, -959, -960 and -1155. CLAIM-741 appears nowhere in A51 (correction 2.1).
- **Backbone entries not used, with no reason given.**
  - Article 7: SYNTHESIS-025, the concept account. Article 7's own count, "A51's twelve backbone codes", includes it.
  - Article 8: SYNTHESIS-038, the line account of organizational-normativity, which integrates CLAIM-741.
  - Article 9: SYNTHESIS-092, -093, -101 and -103. Of these, 092 holds CASE-264, 101 is "who controls the terms of waiting and contracting", and 093 is on what those who govern a depended-on arrangement owe.

  Each article lists its departures from A51 (Article 7 five, Article 9 three). These should be among them, or cited.
- **"The centre" (Article 8 lines 25 and 54).** A51 does not call CLAIM-1184 the centre. Under "Actual remaining work", A51 says: "In particular, the record's instrumentalist objection in CLAIM-1184 … deserves sustained treatment." Say "names as the main remaining work".
- **Parts of A51's abstracts left out without notice.**
  - Article 9: "connects these mechanisms to the resource-bounded accessibility of institutional transformation". That is CLAIM-729's reachability bound and the readiness results (CASE-412, CLAIM-679), which 1.2 also calls for.
  - Article 9's list of accounts to integrate includes "specific investment". This appears only as hold-up, in CLAIM-670's note.
  - Article 8: "The final sections connect these to cooperation and moral development." The draft treats morality and cooperation (§8.9) and not moral development.

  Say which are left, and why.
- **A49's experiment families.** Article 8 has a row for family 5. Article 9, also served by families 2 and 5, has none.

### 1.5 Expectations before results

Studies not yet run are introduced with an expectation and a falsifier before any result: LEAD-tmp0w114, LEAD-tmpiktom, CLAIM-700's study, and CLAIM-603's test via LEAD-166 and LEAD-197. Two reported runs also keep the order well: CASE-367 (LEAD-030's criterion) and CASE-362 (its committed failure rule). So does CASE-335 (LEAD-119's "What was to count, before the run"). Four do not:

- **CASE-316 and CLAIM-879 (Article 8 §8.4.2, line 99; Article 9 §9.5, line 155).** Both give the result with no prior criterion. LEAD-068's "What would count", written before the run, reads: "Oversight that loses effect as speed rises, with authority and resources fixed, supports CLAIM-710 and CLAIM-464; no effect of speed defeats them." Quote it first. LEAD-068 is also still Open, with a "met in the model" note: housekeeping (1.6).
- **CASE-347 (Article 7, table row at line 174).** LEAD-026's criterion: "A procedure that recovers the known boundaries and rejects the commonly driven population answers QUESTION-115 and QUESTION-116 for the model." CASE-347 met it only in part ("the common input is rejected only while it is observed"), and the row gives only the half that passed.
- **CASE-410 (Article 7, line 176).** LEAD-188's criterion is "A route through circulation rather than one contributor supports CLAIM-332". Quote it with the "by at most about five to one".
- **§9.4.** The expectation is stated as "set down before running". The draft, the script and the results were committed together in 6b21bd40, so the order cannot be checked from the record. Say so.

  The falsifier ("no change in the rate of fall at the deadline") is weak, since almost any kink near the deadline passes it. The test that actually discriminates is control 3c, CLAIM-602's threshold-free model, and the draft reports it well. Put the falsifier in terms of 3c: a fall concentrated at t ≈ 3.1 in CLAIM-605's model and not in CLAIM-602's.

  The draft does report honestly that the expectation "fails as a step except for a patient party".

### 1.6 Consistency among the articles, with Parts I and II and with the overview

- **The overview and README have nothing of Part III.**
  - The overview's table gives Articles 7 to 9 as "not started", and its Files table stops at 06.
  - Its "Who made the standings" names only Articles 1 and 6 as citing the promotions made at the assistant's discretion on 2026-11-24. Article 7 cites four: CLAIM-tmpvic6m, -tmpnws9d, -tmpj4pw3 and -tmpq1lyz.
  - The README has no Part III rows in "What the record has already done", "Standing review" or "Files". Step 3a asks for the sort in the README.
  - Article 7 (line 23) proposes changing the README's existing row ("Memetic nucleation (Art. 7) | not done") to *done in part*.
- **Part I's join name.** Article 9 line 194 says "Part I's join J3 passed as CLAIM-tmpu77ve". File 02 (line 347) and the overview call it J2.3 ("was J3").
- **Leads that are Open but have been run, listed differently in each article.**
  - Article 7 lists LEAD-030, LEAD-087 and LEAD-188, and omits LEAD-026 (run as CASE-347; "carried out on a simulated model").
  - Article 9 lists LEAD-104 and LEAD-171, and omits LEAD-068.
  - Article 8 lists none, though it cites run notes on LEAD-033 ("Done"), LEAD-068, LEAD-097, LEAD-110, LEAD-119 and LEAD-131.

  Use one convention.
- **Points of contact.** Article 7 has a "Points of contact not cited" section, and Articles 8 and 9 do not. Article 9 drops several entries its own digest lists, with no reason given:
  - CLAIM-760 (Active, interpretive; a member of this work): "work saved, work transferred and valuable capability expanded are three separate achievements", which bears on the regulatory surplus and the hidden subsidy;
  - CASE-tmp3so1p: "the retention figure merges satisfaction with lock-in", which bears on §9.4's exit and on the holder line;
  - THEORY-457: outside options in partner choice;
  - CLAIM-tmp18v1o: an expectation "realized in a capacity it has stopped maintaining".

  CLAIM-597 (Active, demonstrated), "independent of what founded it but never of what feeds it", and CLAIM-652 (Proposed, demonstrated), harm expanding as the harmed leave, also bear on §9.1 and §9.7.
- **Reliance counts.** Article 8 line 105 gives CLAIM-624 "32 dependants by front-matter relation". By script, 34 entries name it in front matter, 33 of them live. Two of those are accounts (`integrates`), so 32 is the count without accounts. Part II's README gave 34, and its review recounted 35. State the rule.
- **The same stale sentence twice.** G8.1 lists SYNTHESIS-102's "Every component is Proposed, or Open for a question". SYNTHESIS-104 line 132 has the same sentence, with CLAIM-1033 Active.
- **Consistent across the three, and with Parts I and II.**
  - CLAIM-523 is the owner's synthesis, made Active at a delegated review.
  - CLAIM-686 is the assistant's, Active and demonstrated.
  - CLAIM-879's 0.994 → 0.396 is given the same way in Articles 8 and 9.
  - CLAIM-671's role is supposed.
  - CLAIM-tmpyp0ju is quoted alike in Articles 7 and 8.
  - Article 6 §6.2 counts CLAIM-703 as the third route, as Article 9 says.
  - Article 5 cites CLAIM-675 in §5.8.2 and LEAD-tmpeo8wq in §5.6, as Article 9 says.
  - Article 3's norm material (CLAIM-tmpjg5gx, CLAIM-tmp0i6c0, QUESTION-tmprudey) is in file 02, as Articles 7 and 8 say.

## 2. Factual corrections

Each one was re-checked against its entry before it was written here. Each is confirmed.

**2.1 CLAIM-741 and A51's backbone (Article 8 line 25).**
- The draft: "Two are in A51's backbone for this article: CLAIM-671, and CLAIM-741, which is A51's opening move."
- A51 line 501: "**Existing backbone:** SYNTHESIS-038, SYNTHESIS-092, SYNTHESIS-102, SYNTHESIS-103, SYNTHESIS-104; CLAIM-075, CLAIM-671, CLAIM-738, CLAIM-959, CLAIM-960, CLAIM-1155." No line of A51 contains "CLAIM-741".
- Fix: "One is in A51's backbone, CLAIM-671. CLAIM-741 holds A51's opening move, which A51 states without a code." *Confirmed.*

**2.2 "No study of real people … is the record's own here" (Article 7, abstract line 7; Limits line 50, "Every executed study here is a model").**
- CASE-410 (executed study, documented): "from production testimony and a circulation-network model … a search of interviews and trade press, coded by rules written first". CASE-411 and CLAIM-1158 (1.2) are a second such study, of real organizations.
- Fix: "Apart from CASE-410's coded testimony, one observation of one case, no study of real people … is the record's own here", and the same in the Limits. *Confirmed.*

**2.3 Barthes (Article 7 line 76).**
- The draft: "Barthes's essay is not yet registered."
- LIT-tmpflbme, "The Death of the Author", is Deferred, registered in 39a0a7dc "because the owner's CLAIM-tmp590sw names …". *Confirmed.* (CLAIM-tmp590sw's own summary still says it is not registered. That is a record correction.)

**2.4 Who coined "perspectival invitation" (Article 7 line 93).**
- The draft: "The record had not used the phrase. A3 'found the nearest entries … and coined it' (CLAIM-430)."
- CLAIM-430's body, line 59, quotes the owner at U2: "interpret the favor as a 'perspectival invitation' in the sense that github.com/dmarx/nucleation has used recently". CLAIM-430's note of 2026-11-24 says A32 "attributes the perspectival invitation correctly to the owner".
- So the phrase is the owner's, and A3 gave it content. The draft repeats an inconsistency in the entry.
- Fix: "The phrase is the owner's (U2); A3 found the nearest entries and gave it its content." File a dated note on CLAIM-430's "coined in A3". *Confirmed.*

**2.5 LEAD-tmp0w114's voice (Article 7 line 116).**
- The draft: "the assistant's design after A8".
- The lead's summary: "A8 §11 … proposes as its 'Formal starting point' …"; "The measure and the anchoring condition come from the assistant's CLAIM-tmpj4pw3"; "The wording is A's".
- Fix: "A8 §11's proposal, with the assistant's measure". *Confirmed.*

**2.6 Temporary codes (Article 7 line 18; Article 9 line 18).**
- The drafts: "All of them are Proposed or Open except four …" and "all of them are Proposed or Open".
- LIT-tmpjl855 and LIT-tmpfj6uj, cited in Article 7, and LIT-tmpgcwyt, cited in Article 9, are `status: Deferred`. ADR-tmpenzcn, cited in all three, is the work's decision and was not filed from the exchange.
- Fix: add "or, for registered works, Deferred", and except the ADR. *Confirmed.*

**2.7 CLAIM-404's standing (Article 7 line 222).**
- The draft: "CLAIM-tmpp0ufw, CLAIM-404 and the agnotology entries (CLAIM-tmpjlxfy, CLAIM-tmpgc8vi; Proposed)".
- CLAIM-404 is Active: "Promoted at the status review's ruling (the owner delegated these rulings); ADR-057, at the twenty-eighth status review" (2026-11-06).
- Fix: give CLAIM-404 as Active. *Confirmed.*

**2.8 The disclosures of who made entries Active (Article 7 lines 31–36; Article 8 lines 13–21; Article 9 lines 26–30).** Every statement made is right (section 3). Four entries are missing.
- Article 7: THEORY-489, CASE-148, CASE-055 and CLAIM-249 are Active and cited, and their histories record no promotion. Add them to "No promotion recorded".
- Article 8: CLAIM-348 is Active and is a premise of ARG-228 ("rests_on: CLAIM-348, CLAIM-523, CLAIM-723"). Its history: "Promoted to Active at the twelfth status review, by the owner's assent in its pull request". Add it under the owner's assent.
- Article 9: TERM-114 (Active, cited at line 144): "Adopted at the twenty-fifth status review … (the owner delegated these rulings)". The draft's sentence "Every Active entry … was made Active at a status review whose rulings the owner delegated" stays true. Add TERM-114 to the list. *Confirmed.*

**2.9 Article 7's non-member list (line 54).**
- "The following are used here and are not members" lists ten entries. Further cited claims with no `works` field include CLAIM-270, CLAIM-635, CLAIM-151, CLAIM-171, CLAIM-620, CLAIM-336, CLAIM-tmps8ou2, CLAIM-tmpyxemn and CLAIM-tmp8l5s9. Others belong to other works: CLAIM-081, CLAIM-056 and CLAIM-090 to what-survives-translation, CLAIM-425 and CLAIM-426 to self-without-a-sovereign, CLAIM-342 and CLAIM-463 to other works.
- Fix: say "among them". *Confirmed.*

**2.10 SYNTHESIS-tmp4tvbr and CLAIM-tmpsh3og (Article 8 line 54; G8.2, line 276).**
- The drafts: "the owner's CLAIM-tmpsh3og is in no account either" and "This needs a dated note on the account."
- No account `integrates` it, so the first statement is right as to integration. But SYNTHESIS-tmp4tvbr's "Note of 2026-11-25: two parts out of date, from the manuscript governance-of-becoming, Articles 7 and 8" names it and the two terms.
- Fix: say "integrated by no account; SYNTHESIS-tmp4tvbr's note of 2026-11-25 records the gap". Mark G8.2 filed. *Confirmed.*

**2.11 SYNTHESIS-104's stale sentence (G8.1, lines 56 and 275).**
- SYNTHESIS-104 line 132: "Every component is Proposed, or Open for a question". Its component CLAIM-1033 is Active (2026-11-23).
- Fix: add SYNTHESIS-104 to G8.1. *Confirmed.*

**2.12 "The centre" (Article 8 lines 25 and 54).**
- See 1.4. A51 line 505 says the objection "deserves sustained treatment", under "Actual remaining work". *Confirmed.*

**2.13 CLAIM-624's count (Article 8 line 105).**
- See 1.6: 34 front-matter citations (33 live), and 32 without the two accounts.
- Fix: "32 dependants, not counting the two accounts that integrate it". *Confirmed.*

**2.14 Part I's join (Article 9 line 194).**
- The draft: "Part I's join J3 passed as CLAIM-tmpu77ve".
- File 02 line 347: "**J2.3 (was J3)**: passed by a separating case, narrowed, and filed as CLAIM-tmpu77ve". The overview says "file 02's J2.3, narrowed; now Article 3's".
- Fix: "Article 3's J2.3 (file 02)". *Confirmed.*

**2.15 The turn behind CLAIM-tmp8bimm (Article 9 line 166).**
- The draft: "A24 §§8–9 and A22 §10, answering the owner's U19".
- In the exchange, the turns run U17, A21, A22, U18, A23, U19, A24. So A22 answers U17.
- Fix: "A24 §§8–9 (at U19), with A22 §10 (at U17)". *Confirmed.*

**2.16 The §9.4 computation is now on the record (Article 9 lines 104, 146, 232, 248, 257–259).**
- See 1.1. CLAIM-tmp6nzs1: `status: Proposed`, `warrant: demonstrated`, `rests_on: CLAIM-605`, `grounds: CASE-264`. The script, `analysis/README.md` and the dated output are committed. G9.2 is LEAD-tmpfzx2c and G9.3 is LEAD-tmp3w42f. *Confirmed.*

**2.17 "Every figure it prints is asserted" (analysis/README.md; CLAIM-tmp6nzs1's summary, "the script asserts its figures").**
- The script asserts the following:
  - the components (0.2764, 0.7, 3.098, 8/9/10, 4/6, 0.7692);
  - C(t) = 0.7e^(−0.3t);
  - the half-unit property, and u_P at t = 0;
  - the steepest fall at the deadline for r ≤ 0.25, and the single crossing;
  - o_P > 3.9 exactly when T < the deadline;
  - control 3a, A* = 0.585 and the settled C, and control 3c's ratio;
  - 3e's factor of two, and the monotone fractions.
- It does not assert these, which the drafts report:
  - the table's values;
  - "33 %", and 85, 73, 56 and 22 %;
  - 0.041 and 0.003;
  - 5.535;
  - 5.547 and 0.005;
  - t = 2.275 and t = 0.225.
- A run that prints "checks pass" therefore does not by itself reproduce them. I reproduced them by diffing against the kept output, which is byte-identical.
- Fix: assert them, or say "it asserts the components and the shape; the figures are reproduced by comparing against the dated output". *Confirmed.*

**2.18 CLAIM-tmp590sw's wording (Article 7 line 76).**
- The draft quotes "Reproduced, the value travels without the rest of the character that produced it. Each carrier that takes it up completes it from its own character", within "(… the owner's)".
- The owner's words are the ruling quoted in the summary. The mechanism is the filer's development, and the entry has no "The wording is …" line.
- Fix: "the owner's thesis; the development is the filer's". A dated note on the entry should add the wording line. *Confirmed.*

**2.19 Minor (each confirmed).**
- **Article 8 line 265.** "its defeater's 'right of appeal'". The defeater reads "a right of refusal (or of appeal, or an easement)". Line 87 quotes it correctly. Quote it the same way at 265.
- **Article 8 lines 56 and 275.** Add SYNTHESIS-104 (2.11).
- **Article 9 line 129.** "Its own fall is steepest at t = 0.225". LEAD-tmpeo8wq's new note says "at the start". Both are right. Use one.

## 3. Checked and found right (a sample)

**Quotations.**
- **The owner's turns of this exchange.** Each matches the verbatim exchange and is credited to the right turn: U2, U4 (with its double space), U5 (with "agnatology"), U6, U7, U8, U9, U17 (with "opposrtunities"), U18 and U19.
- **The turn order.** It confirms A2, A4 and A5 (§8, CLAIM-tmpjitli), A8 §4, A9 (at U8), A10 (at U9), A22 (at U17), A23 (at U18) and A24 (at U19).
- **The owner's ruling of 2026-11-24 on U4** matches CLAIM-tmp590sw and CLAIM-tmp4mk0t. So does U32 as filed in CLAIM-tmpyp0ju.
- **Owner turns of earlier exchanges.** All match their entries: U41, U27, U47, U36, U37, U44, U28, U25, U24, U23, U16, U11, U8 and U7 of "Assess Depp Heard Abuse"; U5 of "About Plantation Paradise"; U27 of the second share of "Individuation, Possibility, and Disposition"; U39 of 2026-10-22; U2 of "Ben Franklin Effect Explained"; U10 of "Topological protection explained"; U12 of 2026-10-26; U37 and U39 behind CLAIM-060; the remark and request of 2026-11-05 behind CLAIM-603 and CLAIM-602. There are 107 U#/A# mentions with a code on the same clause, and every one is in its entry's text.
- **A51 and A49.** All 47 quotations of A51 and A49 are in the file and section named. That includes "already supply", "Supplies the developmental political economy subsequently applied to enshittification", "This requires normative justification, not merely evidence of dependence", "The instrumentalist objection remains substantive" (A51 §7) and A49's "Resources for contestation and renegotiation" and family 5.
- **The curation entry of 2026-11-24 20:56** holds both of its quotations: "are scoped to different wholes … a scope difference" and "belongs to Art. 9".
- **Block-length quotations are exact:**
  - CLAIM-738's title;
  - CLAIM-723's criterion and its four conditions;
  - CLAIM-1184's title and revival condition;
  - CLAIM-tmpsh3og's ruling;
  - CLAIM-415's three routes;
  - the lead criteria of LEAD-030, LEAD-119, LEAD-110 and LEAD-tmpiktom;
  - CLAIM-603's expectation and falsifier;
  - CLAIM-700's prediction and defeater.

**Figures.**
- **Reproduced by running the script.** All 36 of §9.4's figures, the table and controls 3a to 3e.
- **Recomputed independently.**
  - CLAIM-602: kept capacity 0.625, 0.25 and 0.769; recovery 3.83, 6.37 and 11.37 by Euler at 10⁻⁴, against the entry's 3.84, 6.38 and 11.38.
  - CLAIM-605: threshold 0.2764 and deadline ln(0.7/0.276)/0.3 = 3.10.
  - CLAIM-675: 0.7e^(−1.5) = 0.156.
  - CASE-264: 4, 9, and a width of 7.
  - Take-it-or-leave-it: a fall of 3.601 against Nash's 1.801.
- **Present in the entries.** The 216 numerals of two or more digits all trace to the cited entries or to the script. Among them:
  - CASE-367: 600 users, 0.42 → 0.90, 24.5 → 41.1, 0.352 → 0.357, 0.482, 0.344 → 0.466, 0.231, 9.6 against 3.7, 0.86 against −0.01;
  - CASE-362: ρ = 0.024, 0.25 and 0.125;
  - CLAIM-tmpnws9d: 0.806, 0.724, k = 2.5 and 1.5;
  - CASE-335: 2 of 30, 7 of 10, 4 of 30, 9 of 10, seed 119;
  - CLAIM-879: 0.994, 0.396, 0.711, 0.043, 20 seeds;
  - CASE-287: 60, 86 and 63 per cent;
  - CLAIM-605: 9.13 and 95 %; CLAIM-950: 1.98; CLAIM-713: 85 of 100; CLAIM-716: 25 against 20; THEORY-2070: a sixth.

**Reliance and integration counts, by script.**
- CLAIM-151: four live entries rest on it.
- CLAIM-402: six Proposed entries rest on it.
- CLAIM-tmpgvsgg: nothing rests on it.
- CLAIM-741: no dependants, and two accounts integrate it in front matter (SYNTHESIS-100 and -102).
- None of CLAIM-1155, CLAIM-1184, ARG-228, CLAIM-959, CLAIM-960 and ARG-207 is integrated by an account. All six are dated 2026-11-22.

**Standings and who made them.**
- **Parenthetical standings:** 283 checked, 0 wrong.
- **Histories.** I read the histories of the 57 Active entries the articles cite, and every stated promotion is right. Among them:
  - CLAIM-270 and THEORY-155 "at the owner's direction" (2026-10-19);
  - CLAIM-280 "at the owner's ruling" and TERM-075 "on the owner's ruling", at the twelfth review;
  - CLAIM-342 "on the owner's assent", at the ninth;
  - CLAIM-056 (tenth) and CLAIM-081 (eleventh), with no delegation named;
  - THEORY-839 and THEORY-862 filed Active under ADR-047;
  - the four promotions at the assistant's discretion on 2026-11-24;
  - CLAIM-738, -725, -727, -749, -687, -686, -675, -703 and -716 (2026-11-18), CLAIM-740 and -1033 (2026-11-23), CLAIM-523, -546, -547, -602, -604 and -605 and THEORY-1480 (2026-11-06), CLAIM-418 (fifteenth), CLAIM-464 (eighteenth), and THEORY-1048 and -1050 (twenty-fourth), all delegated;
  - CLAIM-075, CLAIM-060 and THEORY-505 with no promotion.
- **The "accepted" entries.** Article 9's reading of the 2026-11-13 acceptances of TERM-123, TERM-124, CLAIM-690, CASE-264 and CLAIM-686 matches their summaries.

**Membership.** 68 statements against the `works` fields, with no error, apart from the incomplete list in 2.9.
- Article 7: 15 members, of which CLAIM-280 and CLAIM-402 are Active. Three of A51's backbone are members. CLAIM-081, CLAIM-426 and CLAIM-270 are where the draft puts them.
- Article 8: 16 non-members.
- Article 9: 17 members, and CLAIM-602 and CLAIM-605 in governance-of-possibility only.

**Restatements as stated.** JR7.1 (CLAIM-tmpnws9d's summary names CASE-189), JR7.2, JR8.1, JR8.2, J9.2 to J9.4, and the declines J8.5 and J9.5.

**Voices.** Every A/assistant/owner assignment in Article 8's two voice lists (40 entries) and Article 7's lists (24 entries) matches the entries' summaries. The exceptions are 2.4, 2.5 and 2.18.

**Step 3a confirmed as done right.**
- No associative-obligation or fair-play reading is on the record. I searched titles and bodies of THEORY, LIT and NOTE for "associative obligation", "fair play", "principle of fairness", Klosko and Simmons. The Scheffler entries are on the afterlife.
- No executed study of complex contagion is on the record.
- Hold-up's sources are Deferred or Unfetched, and Pettit and Hirschman are Unavailable.

## 4. Revision plan

1. **Sync with 39a0a7dc (1.1; corrections 2.3, 2.10, 2.16).**
   - Cite CLAIM-tmp6nzs1, LEAD-tmp5msck, LEAD-tmplsxtr, LEAD-tmphsmng, LEAD-tmpfzx2c, LEAD-tmp3w42f, QUESTION-tmpeiurf and LIT-tmpflbme.
   - Turn each "candidate" or "needs a note" into the filed entry with its date.
   - Restate J7.1, J7.4 and J8.1 to J8.3 as "stated since in a note filed from this draft".
   - Close the G-items that are filed.
   - Resolve the "Article 7's list of inconsistencies" pointer in SYNTHESIS-tmp4tvbr's note: add the U4 item to Article 7, or correct the note.
2. **Route the joins as step 6 asks (1.1).** Tell the ADR-075 reader that the notes on CLAIM-tmpjitli, CLAIM-tmphq6hp, CLAIM-741, CLAIM-1184 and CLAIM-913 are the drafter's. After the verdicts, file each join's outcome in SYNTHESIS-tmp4tvbr's "Not stated", or as a claim, and not only as notes.
3. **Step 3a again (1.2).**
   - Article 9 §9.6, its table row and §9.10: cite CASE-412, CASE-343, CLAIM-921, CLAIM-679, CLAIM-1099 and CLAIM-1180, and make the verdict *done in part* (the coupling open). Put a dated note on CASE-412 pointing to CLAIM-700.
   - Article 9 §9.4's "What was missing": cite A24 §4's model in CLAIM-tmp2jhc1, file 03 §3.7.4 (J3.10) and LEAD-tmpeo8wq's second note, and state the contribution as the dynamics, the deadline and the reversal.
   - Article 7 §7.7, rows "Vary the seed" and "Withdraw the seed": cite CASE-308, CLAIM-865, CASE-365, CLAIM-952, CASE-389 and CASE-374, and make them *done in part, in assembly models*. Bring CASE-365's separatrix into J7.2.
   - Article 7 §7.7, rows "Replace participants" and "Carrier against concept": cite CASE-411 and CLAIM-1158.
   - Article 8 §8.10: cite THEORY-1569.
   - Article 7 §7.3 and the Limits: cite THEORY-242, THEORY-887 and LIT-1370/1390 for CLAIM-415's first clause.
   - Add a dated note to the README's step-3a section saying that the digests missed these.
4. **Scope (1.3).**
   - Article 9: replace "no term is rewritten" and "every term unchanged" (lines 7, 126, 181) with the stated assumption.
   - Article 9: say which result holds under which of LEAD-tmpeo8wq's readings (lines 110, 129, 257). Correct LEAD-tmpeo8wq's note of 2026-11-25 and CLAIM-tmp6nzs1's summary to match.
   - Article 8: restate J8.1 as an endpoint–history difference, cite SYNTHESIS-102's Arm B precedent (CLAIM-745 with CLAIM-741), and correct CLAIM-741's note of 2026-11-25 to match.
   - Article 7's abstract: tell J7.4 as a join.
   - Article 7 line 149: "separated", not "registered".
   - Article 9 line 209: "does not by itself establish". Line 240: "in Proposed entries".
   - Number the joins at Article 9 line 181 and Article 7 line 93.
5. **A51 (1.4; correction 2.1).**
   - Fix the backbone sentence.
   - Give the unused backbone accounts with a reason (SYNTHESIS-025; SYNTHESIS-038; SYNTHESIS-092, -093, -101 and -103), or cite them.
   - Say "main remaining work", not "centre".
   - Say what is left of A51's "resource-bounded accessibility", "specific investment" and "moral development".
   - Add A49's families 2 and 5 to Article 9's table.
6. **Expectations (1.5).**
   - Quote LEAD-068's criterion before CLAIM-879's result, in Articles 8 and 9.
   - Quote LEAD-026's and LEAD-188's in Article 7's table, with CASE-347's partial result.
   - In §9.4, say that the order cannot be checked from the commits, and state the falsifier in terms of control 3c.
7. **Consistency (1.6).**
   - Update the overview: Part III's state, Files, and Article 7's four promotions at the assistant's discretion.
   - Add Part III's rows to the README's "What the record has already done", "Standing review" and "Files".
   - J3 → J2.3.
   - One convention for leads that are Open but have been run: add LEAD-026, LEAD-068, and Article 8's six.
   - Add "Points of contact not cited" to Articles 8 and 9, starting with CLAIM-760, CASE-tmp3so1p, THEORY-457, CLAIM-tmp18v1o, CLAIM-597 and CLAIM-652.
   - State the counting rule for CLAIM-624.
8. **Corrections 2.2 and 2.4 to 2.19, item by item**, with the record corrections they imply:
   - a dated note on CLAIM-430 ("coined");
   - a wording line on CLAIM-tmp590sw, with "not yet registered" dropped;
   - SYNTHESIS-104 added to the synthesis-review list;
   - the analysis README and CLAIM-tmp6nzs1's "asserts its figures".
9. **The standing review (skill step 6a).** It has not yet been done for Part III. Candidates from the premises the drafts use:
   - CLAIM-741 (demonstrated; filer-checked, no premise, no objection);
   - CLAIM-748 and CLAIM-950 (demonstrated; their CASEs filer-run or rechecked by A);
   - CLAIM-879 and CLAIM-954, -955 and -946 (filer-run executed studies; a second-session rerun would clear them);
   - CLAIM-tmp6nzs1 (new; checked only by its filer).

   Put the table to the owner in ADR-124's form.
10. **After revision**, run the independent fact-check of step 8 and the region-by-region search for points of contact. Neither was run here beyond what 1.2 found. Rerun the quotation and standing scripts, since the record moved during drafting.

## 5. What was checked, and how many

| Kind | Checked | Method | Problems found |
|---|---|---|---|
| Codes exist | 276 distinct codes in files 07 to 09 | Against `record/*.d/` | 0 |
| Quotations in double quotes | 593 strings (07: 191, 08: 218, 09: 184) | By script, then by hand. 484 were in an entry cited on the same line, and 30 in one cited up to ten lines above. 25 were elsewhere in the record (phrases and titles, triaged by hand). 2 were in the exchange, and 47 in A51, A49, the digests or other manuscript files; 2 of these were then found in the curation entry by hand. 4 misses were quotation-within-quotation artefacts, checked by hand, and 1 was a table cell the script misparsed | 0 in substance. 1 voice (2.18), 1 quoted fragment (2.19) |
| Turn attributions (U#, A#) | 107 mentions with a code, 12 owner turns of this exchange, 9 A-turn placements | Entry text; the verbatim exchange under `python3 -I`; turn order | 1 (2.15) |
| Parenthetical standings (status, warrant, kind) | 283 | Script against front matter | 0 |
| Who made entries Active | 57 Active entries' histories (07: 26, 08: 17, 09: 14) | Histories read one by one | 0 wrong; 4 omitted (2.8), 1 wrong standing in an uncited list (2.7) |
| Voices | 64 assignments in Articles 7 and 8, and 35 in Article 9 | Summaries' "wording is" lines | 3 (2.4, 2.5, 2.18) |
| Membership | 68 statements | `works` fields | 0 wrong; 1 incomplete list (2.9) |
| Figures | 216 numerals of two or more digits; §9.4's 36 figures; 7 recomputations | Script; the kept script rerun (byte-identical); my own computation | 0 wrong. 1 claim about the script's checks (2.17) |
| Counts | 6 reliance and integration counts, and 6 integration absences | Script over front matter | 1 rule unstated (2.13), 1 stale sentence missed (2.11) |
| Scope against A51 | 3 articles' abstracts, sketches, backbones (12 + 11 + 15 codes) and remaining-work lines | Read side by side | 1 error (2.1), 1 overstatement (2.12), 7 backbone entries unexplained, 4 abstract phrases (1.4) |
| Scope of paraphrases (abstracts, joins, "what the article claims" lists) | about 40 | Against each entry's title, `defeated_if` and "What it does not say", and the model's code | 8 (1.3) |
| Step 3a: studies the drafts or A51 propose | 13 rows of Article 7, 11 of Article 8, 13 rows and 9 prose verdicts of Article 9 | Searched CASEs (executed, construction, reported), demonstrated and empirical CLAIMs, THEORY and LEADs by construction and measure | 4 missed (1.2), 2 smaller |
| Expectations before results | 12 reported runs or derivations, and 6 unrun studies | Leads' "What would count", case histories, commit order | 4 (1.5) |
| Joins against their components | 18 (J7.1–J7.4, JR7.1–2, J8.1–J8.5, JR8.1–2, J9.1–J9.6) | Components read; account "Not stated" and Arm B sections | 1 misstated (J8.1), 2 unlisted, 5 stale "not stated" after 39a0a7dc |
| Cross-file consistency | Articles 7 to 9, overview, README, Parts I and II cross-references | Read side by side | 7 (1.6) |
| Record moved since drafting | 22 files of commit 39a0a7dc | `git show`, read-only | about 30 sentences (1.1) |

The scripts are in the reviewer's scratchpad (`rev3/`), outside the repository. They are not needed to check this review, because each correction names its entry and its text.

# Part B. The joins under ADR-075

## Joins in governance-of-becoming, Articles 7 to 9: verdicts under ADR-075 step 5

I am an independent reader. I tested each join in the closing "Joins" sections of Articles 7, 8 and 9 against ADR-075 step 5. The routes are a separating case; a derivation that is valid, nontrivial and held by no CLAIM; and a discriminating prediction. ADR-072 sets the filing bar. I read every entry each join names, and the dated notes and the claim already filed for them in 39a0a7dc. I also extracted the "Not stated on the record" section of all 125 accounts in `record/syntheses.d/` and searched them for every component's code. Nothing in the repository was edited, and the git state is unchanged. Branch: `claude/manuscript-governance-of-becoming-part-iii-review`, at 543ccb9f.

**Count, by script** (the bold `- **J…` bullets under each `Joins` heading): Article 7 has J7.1 to J7.4, JR7.1 and JR7.2 (6). Article 8 has J8.1 to J8.5, JR8.1 and JR8.2 (7). Article 9 has J9.1 to J9.6 (6). That is 19 in total.

**J9.1's script.** `python3 -I scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py` exits 0 and prints "checks pass". Its output is byte-identical to `fallback_decay_bargaining.2026-11-25.txt`. I wrote a separate check from the claim's stated model, not from the script: RK4 at step 1e-3 with trapezoid quadrature (`review-III-B-indep-check.py`, beside this file). It reproduces these values to three decimals:

- the threshold 0.2764, the deadline 3.0975 and a* = 0.5854;
- o_P and u_P at t = 0, 2, 3, 4 and 6, on both valuations;
- the four restoration values (4.000, 3.917, 0.041, 0.0035);
- the steepest interval at t = 3.075.

On a grid, o_P is nondecreasing in C.

## Table

| Join | What it is | Declined by an account? | Verdict | Filed entry |
|---|---|---|---|---|
| J7.1 | Agreement between a source and a carrier in characteristic relations is not evidence that the relations were transmitted. | No. SYNTHESIS-074's "Stated already" holds the neighbouring "agreement is not fidelity" (TERM-097, CLAIM-496) for routes. | **RESTATEMENT**: CLAIM-270's retention against drift ("convergence is not preservation"; a chain "can also stay close in distribution while scrambling"), with TERM-027, applied to CLAIM-tmpjitli's criterion. | Note on CLAIM-tmpjitli: **right**. It already calls itself an application with no content of its own. |
| J7.2 | Three outlastings share one shape, a second stable state, so none tells nucleation from threshold contagion. | No. SYNTHESIS-074's "Stated already" has "the fold of CLAIM-459 and the hysteresis of CLAIM-463 are one shape". | **RESTATEMENT**: a conjunction of each entry's own bistability, plus JR7.2. **Fidelity:** "a norm outlasting its baseline" misstates CLAIM-tmps8ou2, which separates justification from baseline. | none |
| J7.3 | CASE-367's arms as the model form of A51's distinction, and of self-sealing against self-fulfillment. | No. SYNTHESIS-062 declines two neighbouring mappings onto CLAIM-402 over the same kind of free parameter ("passes through"; whose reading regime). | **MISSTATES COMPONENTS**: CLAIM-402's note of 2026-10-24, and route 3 in CLAIM-415's note. The corrected remainder is a **RESTATEMENT** of CLAIM-954. | none. Residue: a dated note on CLAIM-954. |
| J7.4 | Observed restoration does not tell an enforced norm from a copied majority, so CLAIM-tmphq6hp's marker needs another. | No | **RESTATEMENT** of CLAIM-946's body ("Enforcement by a referee (0.031) … also passed. The condition does not separate them") and CASE-362's enforce arm. The carry-over to behaviour **FAILS as a claim**: it rests on a free parameter, namely who does the restoring. | Note on CLAIM-tmphq6hp: **needs revision**. It misses the enforce arm, and its candidate marker points the wrong way. |
| JR7.1 | The hyperstition model of outlasting is CASE-189 in other variables. | — | **RESTATEMENT** (CLAIM-tmpnws9d's summary) | — |
| JR7.2 | Persistence after withdrawal is not evidence of nucleation. | — | **RESTATEMENT** (LEAD-tmpiktom step 1; CLAIM-tmpgvsgg's defeater) | — |
| J8.1 | Defeated standing is a policy-level failure that no evaluation over realized outcomes represents. | No. SYNTHESIS-102 has CLAIM-741 with CLAIM-745 and with QUESTION-483; SYNTHESIS-038 has it with QUESTION-483. | **MISSTATES A COMPONENT** (CLAIM-741). CLAIM-723's defeat, T_foreclosure < T_opportunity, is an event in the realized history. That is CLAIM-741's *first* separation, which an evaluation of histories can represent. ARG-228's misfiled complaints are also in the history. The corrected remainder is a **RESTATEMENT** (CLAIM-741 applied). | Note on CLAIM-741: **needs revision** ("By this claim's second separation, an evaluation over realized histories 'cannot represent' the difference" is wrong). |
| J8.2 | ARG-228 and CASE-336's C2* and C4* as parallel instrumentalisms. | No | **FAILS as a claim**: "is a candidate in the other" admits no case. The stronger form fails, as the draft says. The shared form is CLAIM-909's, so this is a **RESTATEMENT** of CLAIM-909 applied to ARG-228. | Notes on CLAIM-1184 and CLAIM-913: **right as notes**. They should cite CLAIM-909. |
| J8.3 | CASE-316 measures the occasion of CLAIM-723's foreclosure condition, not the wrong. | No | **RESTATEMENT/gloss**, correctly not a claim. Accurate. | Notes on CASE-316 and CLAIM-723: **right**, with one wording fix ("no affected party"). |
| J8.4 | Three bounds as one claim. Not made. | — | **Correctly not made.** A conjunction of three non-implications. | — |
| J8.5 | A51's closing sentence. Not made. | — | **Correctly not made.** It conflicts with CLAIM-tmpreipd item 4 ("Moral consideration is not earned by cooperating") and CLAIM-547's third achievement. | — |
| JR8.1 | Successful cooperation cannot establish its own legitimacy. | — | **RESTATEMENT** (CLAIM-725, CLAIM-075, CLAIM-060, each in its own scope) | — |
| JR8.2 | Repair need not wait on culpability. | SYNTHESIS-104 leaves "who owes" open | **RESTATEMENT** (CLAIM-742, CLAIM-717) | — |
| J9.1 | Fallback decay in the Nash split. The terms move with no exit, and can be restored before CLAIM-605's deadline and not after. | No. SYNTHESIS-032 declines a neighbouring "funding loop with a deadline" for a premise J9.1 does not need. | **PASSES (derivation)** in a corrected form. The script and my recheck agree. Its content of its own is the deadline in the terms. The first clause is held as comparative statics (CLAIM-tmp2jhc1's A24 §4; CLAIM-670's note). | CLAIM-tmp6nzs1: **right in substance**. Five corrections, below. The notes on CLAIM-tmp2jhc1 and LEAD-tmpeo8wq each overstate one point. |
| J9.2 | §9.4 as a model of CLAIM-670's "terms the party could earlier have refused". | — | **MISSTATES** what §9.4 shows. In the Nash arm, u_P = 4 + o_P/2 ≥ 4 = o_P(0), so P never gets terms it could earlier have refused. That holds only in the take-it-or-leave-it control (3e), or for w > (S − o_R)/2. What §9.4 models is CLAIM-670's note, "what they can afford to refuse has changed", and that much is a **RESTATEMENT**. | none. Residue: a dated note on CLAIM-tmp6nzs1, or its "What it does not say". |
| J9.3 | Control, not reciprocity, sorts dependence. | SYNTHESIS-092 and 095 have CLAIM-690 with CLAIM-682, a different link | **RESTATEMENT** (CLAIM-603's note of 2026-11-12) | — |
| J9.4 | Price and bar as two controls over withdrawal. | — | **RESTATEMENT** (CLAIM-tmpdu9v6's title and "Where the record stands": "not the price of exit"). **Fidelity:** §9.6 calls the fallback channel "a price". CLAIM-tmp6nzs1 and LEAD-tmpeo8wq define it as moving the terms with "no transition's price changed". | — |
| J9.5 | Enshittification as domination. Not made. | — | **Correctly not made**, but the reason **misstates CLAIM-tmpjnly0**. Its institution is an optimizing agent that acts on its constraints, so it is a holder in TERM-124's sense. What is missing is a declared standard. | — |
| J9.6 | Contestation cost and exit cost in one model. Not made. | No | **Correctly not made.** Nothing to test; it is gap G9.3. | — |

In total, 19 joins:

- 1 passes, in a corrected form (J9.1, as CLAIM-tmp6nzs1 with corrections);
- 3 misstate a component (J7.3, J8.1, J9.2), each leaving a restatement;
- 2 fail as claims (J7.4 as a carry-over, J8.2), each otherwise a restatement;
- 4 are correctly not made (J8.4, J8.5, J9.5, J9.6), and J9.5's stated reason needs fixing;
- 9 are restatements (J7.1, J7.2, JR7.1, JR7.2, J8.3, JR8.1, JR8.2, J9.3, J9.4), two of them with a fidelity correction (J7.2, J9.4).

Of the filed entries:

- **Right:** CLAIM-tmp6nzs1 (with corrections), the notes on CLAIM-tmpjitli, CLAIM-1184 and CLAIM-913 (add CLAIM-909), and the notes on CASE-316 and CLAIM-723 (one wording fix).
- **Needs revision:** the notes on CLAIM-tmphq6hp and CLAIM-741.
- **Overstates one point:** the notes on CLAIM-tmp2jhc1 and LEAD-tmpeo8wq.

---

## Article 7

### J7.1: RESTATEMENT

The join says that χ(P_A) ≈ χ(P_B) is not by itself evidence of transmission, so a fidelity test needs the start to matter. CLAIM-270 (Active, demonstrated) holds the distinction between retention, I(U₀; Uₙ), and drift, D[P(Uₙ), P(U₀)]: "A chain can also stay close in distribution while scrambling which individual started where". Agreement between a source and a carrier is low drift. Transmission is retention. TERM-027 adds that an attractor "is where the chain goes whatever its start". "The start matters" is retention by CLAIM-270's definition, and CLAIM-635 gives a sufficient condition for it. So the join is CLAIM-270 applied to CLAIM-tmpjitli's success criterion. That application is unstated, but it is not new content (ADR-072).

The filed note on CLAIM-tmpjitli says exactly this ("no content of its own beyond the application"), and its quotations are accurate. Its practical point is right and worth keeping: CLAIM-tmpjitli's defeater compares memes with propositions, not with an attractor, and LEAD-tmpqucxc should vary the source while holding the reconstruction fixed. The draft's "No entry states it" should read "no entry applies CLAIM-270 to it". SYNTHESIS-074's "Stated already" ("agreement is not fidelity", TERM-097 and CLAIM-496) is the nearest held sentence, but it concerns agreement between routes, so CLAIM-270 is the better premise to cite.

### J7.2: RESTATEMENT, with a fidelity correction

Each of the three entries states its own bistability:

- CLAIM-tmpnws9d: "a second stable state";
- CLAIM-tmpjg5gx: bistability, a threshold and hysteresis;
- CLAIM-463: a bistable range and a hysteresis loop.

"So none distinguishes nucleation from threshold contagion" is LEAD-tmpiktom step 1, which is JR7.2, applied three times. No case can have every component hold and the join fail. SYNTHESIS-074 already records the same kind of "one shape" observation as stated ("the fold of CLAIM-459 and the hysteresis of CLAIM-463 are one shape", CLAIM-459's body). Joining the norm model to the hyperstition result adds only that both are bistable.

**Fidelity.** The joins line says "a norm outlasting its baseline". CLAIM-tmps8ou2's point is the opposite: "a norm that outlasts its justification need not have outlasted its support". In the bistable model a norm outlasts a *weakening* of its baseline within the bistable range, and it ends "by a push past its threshold". §7.4's body states it correctly; the joins line should match.

### J7.3: MISSTATES COMPONENTS. The corrected remainder is a restatement of CLAIM-954.

The join reads the fixed-preference arm as "apparent confirmation by the regime" and the adaptive arm as "a changed referent". It says the run "fills in the cut" of CLAIM-402's decomposition. At the person's scale it calls these self-sealing and self-fulfillment. Two misstatements follow.

- **CLAIM-402's note of 2026-10-24.** The cut is dD̃/dθ = Σ K_r dD_u/dθ (performative change of the world sampled) + Σ (dK_r/dθ) D_u (endogenous change of how it is represented). CASE-367 holds the representation fixed. Its classes are "Inferred once … then held fixed", so dK/dθ = 0 in every arm. Both arms lie in the first term. In one, exposure changes what is sampled while preferences stay fixed; in the other, preferences move too. What CASE-367 does instantiate is the note's *second separating intervention*, "change the policy with raw outcomes observed independently": the randomized probe. Mapping its arms onto the two terms needs exposure counted as part of the reading regime. That is a free parameter of the kind SYNTHESIS-062 declines for neighbouring mappings onto CLAIM-402.
- **A10 §8 in CLAIM-415's note.** Interpretive self-sealing is "Whatever I do is taken as confirmation, regardless of whether my character changes": a changed reading of fixed behaviour. In the fixed-preference arm the behaviour (engagement) does change, steered by exposure, while the reading is fixed. So that arm is not self-sealing. Self-fulfillment corresponds to the adaptive arm and is an illustration. Adversarial constitution has no arm.

What survives is CLAIM-954's title: steering raises concentration, fit and stability "whether or not preferences move", and only the randomized gap moves with the referent. Its own phrase, "an instance of CLAIM-402's worry", already ties the run to CLAIM-402. **Residue: a dated note on CLAIM-954, or CASE-367.** It would say three things:

- the randomized probe is CLAIM-402's second separating intervention, inside the performative term;
- the case holds the reading regime fixed, so it has no arm for the representational term, and none for interpretive self-sealing;
- re-inferring the classes under use would be that arm.

### J7.4: RESTATEMENT of CLAIM-946's body. The carry-over FAILS as a claim, and the filed note needs revision.

- **The comparison the join asks for is in CASE-362 already.** CASE-362 has an enforce arm, "on disagreement a third member referees; the minority moves", with ρ = 0.031, against conform's 0.024. CLAIM-946's body states: "Enforcement by a referee (0.031) and checking against the world (−0.030) also passed. The condition does not separate them." So the draft's "Not stated" and the note's reading of CLAIM-946 as about evaluating against copying miss the arm that is the enforced case.
- **The carry-over has a free parameter.** CLAIM-tmphq6hp's marker is "bringing the behaviour back into line". On a behavioural reading (the deviant's behaviour returns), copying meets it, as the join says. On the reading its summary quotes from A22, "Recruit activity to restore compliance", corrective activity by others separates the two by construction. Until that slot is fixed, no case can be stated.
- **The note's candidate marker points the wrong way.** The note proposes "a disposition to restore that holds against a majority, of the kind CASE-362's evidential condition tests in direction (… toward the world)". There are three problems with it:
  - the evidential arm moves members toward the world, which is the descriptive direction of fit, the opposite of a norm's (TERM-151);
  - CASE-362's enforce arm also moves the minority;
  - the record's own norm model has a bistable norm end "by a push past its threshold" (CLAIM-tmps8ou2), so a genuine enforced norm can fail against a majority deviation. Holding against a majority would misclassify it.
- **The held principle that does the work is CLAIM-522** (Active): "Recovery under interventions on state cannot show where maintenance is realized … only interventions on the production mechanisms … separate the two". LEAD-tmpiktom step 4 already cites it.

**Residue: revise the note on CLAIM-tmphq6hp.** Cite CASE-362's enforce arm and CLAIM-946's sentence. Replace the candidate marker with an intervention on the corrective mechanism: knock out others' corrective activity. Name the free parameter. No claim.

### JR7.1, JR7.2: RESTATEMENTS

Both are confirmed. CLAIM-tmpnws9d's summary: "It is CASE-189's transient encounter and maintained connector, in hyperstition's variables". LEAD-tmpiktom step 1: "a threshold or a lasting regime after withdrawal is not by itself evidence of nucleation".

---

## Article 8

### J8.1: MISSTATES CLAIM-741. The corrected remainder is a restatement.

CLAIM-741 has two separations:

- the *first*, between endpoint and history: "An evaluation of endpoints cannot tell them apart; one of histories can";
- the *second*, between history and policy, on "the history in which the patient consents", where the right is *not exercised*.

CLAIM-723's defeat is "Foreclosure", with T_foreclosure < T_opportunity: the act made the standing ineffective "before it could be exercised". That is an event in the realized history. Where "the objection would have failed", the respecting and the defeating arrangement reach the same endpoint by different histories (heard and refused, or foreclosed). That is the first separation, and a requirement on histories (CLAIM-523's 𝓗_N, "no irreversible step before the window closes") represents it. ARG-228 is the same: in O₂ "the same complaints arrive and have no category to arrive in", which is again in the history. The policy level is reached only on a history where no objection is made, and the two arrangements differ in what they *would* have done with one.

So "a policy-level failure that no evaluation over realized outcomes can represent" is right for endpoints and wrong as "policy-level". The filed note's "By this claim's second separation, an evaluation over realized histories 'cannot represent' the difference" is wrong. **Corrected sentence:**

> Where the objection would have failed, respecting and defeating a standing to contest reach the same endpoint by different histories (CLAIM-741's first separation), so an evaluation of endpoints cannot represent the defeat and one of histories can; only where no objection is made does the difference lie in policy alone (its second separation).

This applies CLAIM-741 to CLAIM-723, and adds no inference. The join's closing clause, "this does not show it is a wrong beyond expected harm", is CLAIM-1184's opening premise and the note's own caution, so it is not a claim. **Residue: revise the note on CLAIM-741 to this sentence.** Its second note ("what holds it back") is not a join and was not tested here.

### J8.2: FAILS as a claim. Its form is CLAIM-909's. The notes are right as notes.

The parallel is accurate:

- ARG-228 holds H, C and expected C fixed ("the match holds ex ante") and varies whether complaints register;
- C2* holds the decisions fixed ("computed mechanically … audited as applying R without error") and varies control of review;
- C4* holds the rules and their timing fixed and varies who holds the power to revise.

But the general form is held. CLAIM-909: matched constructions discriminate "only when they hold fixed what a power's holder would do with it", and "the verdict turns on whether a reason to hold or share a power, apart from its use, is an input". ARG-228 is a construction of that form for standing. "A non-instrumental reason accepted in one is a candidate in the other" admits no separating case, because "candidate" absorbs every outcome. The draft's rejection of "stand or fall together" is right. One detail: C2* (control of review) is nearer to ARG-228's standing than C4* is, and the note's "standing to be heard is not a share of a power to revise" separates ARG-228 from C4* only. **Residue:** add CLAIM-909 to both notes as the entry that holds the form.

### J8.3: RESTATEMENT/gloss, correctly a note

The mapping is accurate. CASE-316 counts, for objectionable actions, how often an act becomes irreversible before suspension can take effect. That is CLAIM-723's "Foreclosure" condition. The note's quotation ("the act made that standing ineffective before it could be exercised") is from CLAIM-723's `defeated_if`, verbatim. Its limits (no failing objections, no attribution, no justification; "Intent to outrun review" under "What it cannot show") are right. **Wording:** "The model has no affected party (the standing is the overseer's power to suspend)". CLAIM-723's party with "standing to authorize, suspend or contest" can be an overseer. What the model lacks is a party harmed by the act. Say that.

### J8.4, J8.5: correctly not made

- **J8.4.** CLAIM-749 (influence ⇏ answerability), A71's rider ("can generate or strengthen responsibilities without granting legitimate authority") and CLAIM-tmpsh3og (no direct authority ⇏ no standing) are three non-implications. Their conjunction adds no inference.
- **J8.5.** "Situated within the legitimate governance of the power … acquire[d] … through cooperation" confines morality to cooperation's powers. CLAIM-tmpreipd item 4 says "Moral consideration is not earned by cooperating", and CLAIM-547 lists concern for those outside one's group as a separate achievement.

### JR8.1, JR8.2: RESTATEMENTS

Both are confirmed against CLAIM-725, CLAIM-075 and CLAIM-060, and against CLAIM-742 and CLAIM-717, with SYNTHESIS-104's "Who owes the correction in any case … leave it open".

---

## Article 9

### J9.1: PASSES (derivation) in a corrected form. CLAIM-tmp6nzs1 is right in substance.

**Derivation, independent of the script.**

1. Under full substitution, P = min(τC, 0) = 0, so C(t) = 0.7e^(−0.3t), strictly decreasing (CLAIM-605).
2. With supply removed, Ċ = f(C) = λ min(τC, 1)C(1 − C) − μC is scalar and autonomous, with f Lipschitz. Solutions from ordered starts stay ordered (the comparison principle), so P's stand-alone output path min(τC_s, 1) is pointwise nondecreasing in its start. Any valuation nondecreasing in the output path therefore makes o_P nondecreasing in C(t). The forward and current-output valuations both qualify.
3. u_P = (S − o_R + o_P)/2 is increasing in o_P, as is take-it-or-leave-it's u_P = o_P. So P's terms are nonincreasing in t, with no exit taken.
4. o_P depends only on the capacity when the supply ends. If it ends at T with C(T) > C_L = 0.2764 (T < 3.098), C → 0.7 and o_P → w. If C(T) < C_L, then C → 0 and o_P → the value of zero output, 0. So the terms are restorable, asymptotically, exactly before the deadline.
5. Without exit (CASE-264 arm B), o_P does not enter u_P.

Steps 2 to 4 are the content. Steps 1 and 5, and the half-unit rate, are held. The first clause is held as comparative statics: CLAIM-tmp2jhc1's A24 §4 ("specialization … lowering B's independent capacity", 14.75 to 11.25), CLAIM-670's note ("As B's relationship-specific investment lowers o_B …") and CLAIM-675. The deadline transferred to the terms is not held. The search found no such claim, and no "Not stated" section declines it. SYNTHESIS-032's "funding loop with a deadline" fails for want of "learning from drills", a premise J9.1 does not need, since P learns by doing its own work. The derivation is short but not trivial: it composes CLAIM-605's bifurcation with the threat point through a monotonicity argument, and ADR-075's A ⇒ C example admits such a step.

**Corrected sentence (title):**

> Where a party's fallback is valued from a capacity learned by doing that needs capacity already present to grow (CLAIM-605), and its terms are bargained by a rule under which a more valuable fallback gets more, supply that does the party's own work lowers the terms it can obtain at any renegotiation while it never exits and no price or rule changes; ending the supply restores them, asymptotically, if it ends before the capacity's deadline and not after; supply that covers only what a party above the threshold cannot yet do leaves the capacity, and so the terms, where they were; and where the party cannot exit, the fallback does not enter the terms.

**Corrections to CLAIM-tmp6nzs1, and to J9.1's line:**

1. **"No term changed" (J9.1) and "no term rewritten" (the summary, §9.4 result 1).** The split *is* the terms, and it is re-solved at each t, so the model assumes renegotiation. What is unchanged is every price, rule and exit. Say so.
2. **"Under capacity-first supply … the decay does not move the terms."** In CLAIM-605's model, capacity-first practice min(τC, 1) is the unsupported dynamics, so there is no decay to move anything. From below the threshold, the capacity decays anyway (CLAIM-605: it "cannot lift a party already below the threshold") and the terms fall. State it as above.
3. **The body should give the derivation.** ADR-075's derived-result route says "the body gives the derivation". The body gives the computation. The derivation above makes the script a check of the qualitative clauses, and the script's own content (steepest at the deadline for r ≤ 0.25; 85 % to 22 % of the fall within half a unit) stays as the "not a step in general" section has it.
4. **The defeater's second clause** ("not monotone in that capacity under any valuation of its stand-alone path") cannot be met as worded, because the current-output valuation is monotone. Name the premise instead: "a valuation of the fallback that is not nondecreasing in the stand-alone output path".
5. **"It answers … under both of its readings, the item LEAD-tmpeo8wq left open"** (the summary, and the note on LEAD-tmpeo8wq) overstates. The lead's second reading is a classification, not a valuation. On it, the decline "is then a rise in i's incoming costs … and the null applies". So "shrinkage, not a price" is answered *yes* on the first reading only. On the second, the computation shows that the terms move, with the movement classed as a price. The forward valuation is not that reading, since it counts natural recovery, not a cost of rebuilding.

Two smaller points:

- State that the capacity is P's *self-supply*, distinct from its contribution to S, which is why S and o_R are held fixed. If R is the supplier and its supply also raised o_R, the fall would be larger.
- The note on CLAIM-tmp2jhc1 says the claim's "changes the terms" now "runs in both directions". The claim's own body already "shows the reverse" (A24 §4). What is new is the decay in time and its deadline.

### J9.2: MISSTATES what §9.4 shows. The restatement is of CLAIM-670's note.

At the article's parameters, u_P = (10 − 2 + o_P)/2 = 4 + o_P/2 ≥ 4 = o_P(0). P's share never falls below its own fallback at t = 0; at t = 6 it is 4.199 against 4.000. So the Nash arm never produces "terms the party could earlier have refused". At t = 0, P would have accepted 4.199 rather than exit. The phrase holds in the take-it-or-leave-it control (3e: u_P = o_P(t) < o_P(0)), or in the Nash arm only when w > (S − o_R)/2 = 4. At w = 4 the parameters sit exactly on that boundary. What the Nash arm models is the *floor*: "what they can afford to refuse has changed" (CLAIM-670's note, quoting A22). The draft's "restates … together with J9.1" holds for that much. **Residue:** say this in §9.2 and §9.4, and add it to CLAIM-tmp6nzs1's "What it does not say", or as a dated note on it.

### J9.3: RESTATEMENT

Confirmed. CLAIM-603's note of 2026-11-12: "mutual dependence of outcomes is not mutual control of terms", which it gives as CLAIM-428's point applied to the reciprocal form.

### J9.4: RESTATEMENT, with a fidelity correction

CLAIM-tmpdu9v6's title, and its "Where the record stands": "the controlled term is the cost and availability of the permissible route … not the price of exit". **Fidelity:** §9.6 says "CLAIM-tmp2jhc1 and §9.4 move terms by a price: the value of the fallback in the disagreement point". But §9.4, CLAIM-tmp6nzs1 and LEAD-tmpeo8wq put that channel as moving the terms with "no transition's price changed". Write "by the value of the disagreement point" and drop "price". The contrast with a bar survives.

### J9.5: correctly not made. The reason misstates CLAIM-tmpjnly0.

§9.7 says that in CLAIM-tmpjnly0 the erosion "can be produced by the optimization itself, with no change in the character of those who run it", and so "may fall outside" TERM-124. But CLAIM-tmpjnly0's institution chooses e_t and a_t, and its actions change C_t. It is an agent holding a "capacity, used or not, to set or change the terms", which is TERM-124's holder. "No change in character" means no intent, which TERM-124 does not require. CLAIM-677's "without any rule requiring it" is the one mechanism that may lack a holder. The right reason for not making the join is that no standard of answerability is declared (TERM-124; CASE-264's "That B is exploitation"), and CLAIM-682's three conditions are not examined for any platform. SYNTHESIS-tmp4tvbr calls A46's "enshittification" link a label. **Residue:** fix §9.7. No record entry is needed.

### J9.6: correctly not made

It is gap G9.3. No account's "Not stated" names CASE-287 with CLAIM-605. SYNTHESIS-098's CASE-287 item concerns CLAIM-724's permitted class.

---

## Items for the drafters

1. **J9.1 / CLAIM-tmp6nzs1** (the claim is merged on staging, so this is a revision):
   - replace "no term changed/rewritten" with "no price, rule or exit changed";
   - restate the capacity-first clause;
   - put the five-step derivation in the body;
   - fix the defeater's quantifier;
   - narrow "under both of its readings" to the first reading;
   - say that the capacity is P's self-supply.

   Revise the notes on LEAD-tmpeo8wq (both readings) and CLAIM-tmp2jhc1 ("runs in both directions" → "the A24 §4 reverse, now in time, with a deadline") to match. In §9.7, "with every term unchanged" contradicts §9.4's moving terms.
2. **J9.2**: in §9.2 and §9.4, the Nash arm models a falling floor, not "terms the party could earlier have refused". That holds in 3e or for w > 4. Add it to CLAIM-tmp6nzs1's limits.
3. **J9.4**: in §9.6, drop "a price" for the fallback channel.
4. **J9.5**: in §9.7, CLAIM-tmpjnly0 has a holder. The reason not to join is the undeclared standard.
5. **J8.1**: rewrite §8.4.4 and the note on CLAIM-741 to the corrected sentence (first separation for a failed objection; second only where none is made). This also changes §8.3's use of CLAIM-741, if it reads defeated standing as policy-level.
6. **J8.2**: cite CLAIM-909 in §8.5 and in the notes on CLAIM-1184 and CLAIM-913. Say that C2*, not C4*, is the near parallel to ARG-228.
7. **J8.3**: in the notes on CASE-316 and CLAIM-723, change "no affected party" to "no party harmed by the act; the party with standing is the overseer".
8. **J7.4**: revise §7.6 and the note on CLAIM-tmphq6hp:
   - CASE-362's enforce arm, and CLAIM-946's "The condition does not separate them", already hold enforcement against conformity;
   - name the free parameter (the deviant's return, or others' recruited activity);
   - drop the "against a majority / evidential direction" candidate, for the three reasons under J7.4;
   - point to CLAIM-522's intervention on the mechanism instead.
9. **J7.3**: in §7.5, CASE-367 holds the classes fixed, so both arms are in CLAIM-402's performative term. The randomized probe is the note's second separating intervention, and the fixed-preference arm is not interpretive self-sealing. File the residue as a dated note on CLAIM-954, and keep only the self-fulfillment illustration.
10. **J7.2**: in the joins line, "a norm outlasting its baseline" → "a norm outlasting a weakening of its baseline within the bistable range" (CLAIM-tmps8ou2). Cite SYNTHESIS-074's "one shape" item as precedent, and recount J7.2 as a restatement.
11. **J7.1**: "No entry states it" → "CLAIM-270's distinction, not yet applied to CLAIM-tmpjitli". Recount it as a restatement.
12. **Counts for the account.** When SYNTHESIS-tmp4tvbr gets its "joins of Part III" section:
    - 1 passed (J9.1, corrected);
    - 3 misstated a component (J7.3, J8.1, J9.2);
    - 2 failed (J7.4, J8.2);
    - 4 were correctly not made (J8.4, J8.5, J9.5, J9.6);
    - 9 were restatements.
13. **For promotion:** CLAIM-tmp6nzs1 has now had a second, independent recomputation (this review: the same figures from separate code, and an analytic derivation of its qualitative clauses). That is the check its "Standing" section asks for. Promotion remains the owner's call.

# Part C. Points of contact the drafts do not cite

## Part C. Points of contact the drafts do not cite, Part III (Articles 7 to 9), 2026-11-25

This is the searcher's report for the review of `scratch/manuscripts/governance-of-becoming/07` to `09`. I read the checkout read-only on branch `claude/manuscript-governance-of-becoming-part-iii-review`, at merge 543ccb9f.

**Method.**

- I collected every code the three drafts cite: 369 distinct codes, temporary ones included.
- I indexed the front matter of 5,450 entries in claims, cases, questions, leads, syntheses, theory, terms, arguments and workbench.
- I listed uncited entries in two ways:
  - by front-matter relation to the codes each article cites, in both directions;
  - by line (`pragmatic-transport`, `distributed-agency`, `organizational-normativity`, `rightful-power`, `dependence-and-domination`, `transient-support`).
- I searched by mechanism: transmission chains, attractors, thresholds and hysteresis, performativity and evaluation regimes, attributed plurality, norm transmission against common input, price shocks, budget rules that follow use, exit-driven drift, outside options, residual control, exit and voice, penalties on recognition, review queues, associative obligation and fair play.
- I read the process history: the curation entries of 2026-11-24 20:56 and 23:11 and of 2026-11-25 02:20; commit 39a0a7dc ("Part III: file the drafts' joins and gaps"); devlog 2026-11-25 03:30 and 2026-11-24 22:29; SYNTHESIS-tmp4tvbr's "Not stated on the record"; the write-manuscript skill (step 3a); the run-lead skill; the reviews of Parts I and II.

I read each entry's title and summary, and its relations, before listing it. Statuses and warrants are from front matter on this branch. "Cite?" is my recommendation.

---

## Region 1. Memes, transmission, hyperstition, norms, culture (Article 7)

### §7.1 What circulation keeps

- **CLAIM-208** (Active, demonstrated, counter; `objects_to` CLAIM-056): "the compositional predictions are upper bounds whose constants cannot be estimated from serial-reproduction data in a metric fixed beforehand, so the compositional half of the success criterion cannot fail". **Qualifies.** The draft gives CLAIM-056 as part of the held floor and omits its Active demonstrated counter. Cite? **Yes.**
- **CLAIM-031** (Active, interpretive, granted; `objects_to` CLAIM-056): a chain "reorganizes observational constraints rather than only accumulating metric error". **Qualifies** the "local fidelity" bullet in the same way. Cite? Yes, with 208.
- **CLAIM-772** (Proposed, interpretive): "Forgetting a source and anchoring to it are one contraction, told apart by what each restatement step conserves exactly". It rests on CLAIM-635. **CLAIM-773 and CLAIM-779** (Proposed, demonstrated) and **CLAIM-768** (Proposed) are its linear-Gaussian forms. **Supports** "What does keep the start", and it is the held form of J7.1's "an invariant ... that the chain conserves". Cite? Yes, 772.
- **CLAIM-068** (Proposed, interpretive): "pragmatic stances, not only lexicon and grammar, can be stabilized by transmission". It rests on CLAIM-090 and uses TERM-027. **CLAIM-059** (Proposed): chains fall into contracting, neutral or amplifying regimes. **Supports** "Where chains settle". Optional.
- **LEAD-187** (Open): "Find or run a transmission chain whose endpoint is compared with a prior measured on its own transmitters before transmission". With it, **QUESTION-137** (Open). This is the work that CLAIM-090 and §7.7 row 1 ("waits on a prior measured beforehand") wait on, and the draft names no lead for it. Cite? **Yes.**
- **CLAIM-002** (Active, interpretive): a text's identity across retellings is "a family of relations ... identity of the artifact, continuity of transmission and similarity of communicative function". It complements CLAIM-621. **Supports** §7.1's caution and §7.2's carrier against concept. Optional.
- **CLAIM-191 and CLAIM-776** (Proposed, interpretive): restating an argument across memoryless sessions is iterated transport, and the ideas "furthest from the collaborators' own framings" are lost soonest. **Bears on** the Limits paragraph. This article's argument was developed with AI assistants who restate it, and these are the record's own claims about what such restatement does. Optional.

### §7.2 Seeds, values and invitations

- **CLAIM-329** (Active, interpretive): a collective that replaces its members persists "by causal transmission of the organization that produces it, not by resemblance: an organization of the same kind that arises independently is not its continuation". CLAIM-tmpgvsgg and CLAIM-tmpjitli both **rest on** it. It is the uncited Active premise of two of A's theses. It also **partly states J7.1**, for collectives: resemblance is not continuation. So J7.1's "No entry states it" needs narrowing to the character-relations case. Cite? **Yes.**
- **CLAIM-420** (Active, interpretive): influence persists "as a story ..., as a perspective transmitted ..., and as later organizations that descend from their activity, and causal descent is not perspectival inheritance: a movement founded to oppose someone can descend from them without continuing their perspective". CLAIM-tmpgvsgg rests on it. It is the held, Active analogue of the owner's CLAIM-tmp590sw ("related but distinct perspectives"), and the draft cites only CLAIM-171 beside that claim. **Supports and sharpens.** Cite? **Yes.**
- **CLAIM-132** (Active, demonstrated, granted): characters classify representations "up to isomorphism only over a field of characteristic zero; they forget the isomorphisms, fix neither the group nor a permutation action". **Misreported standing.** §7.2's "What a character can and cannot carry" quotes this content from SYNTHESIS-077 (Proposed), but it is CLAIM-132's title, Active and demonstrated. CLAIM-tmpjitli rests on CLAIM-132. With it, **CLAIM-tmpqbaic** (Active, demonstrated; a gap fill from this exchange): "The character of a perspective's representation detects the transformations it is blind to, not the states it merges". That is a held limit on both U4 readings, and the draft omits it. Cite? **Yes, both, in place of SYNTHESIS-077 or beside it.**
- **QUESTION-tmprvnp0** (Open): "How do transmissible structures such as memes take part in forming, maintaining and transforming the organizations through which they become consequential, and when does the seed's own persistence matter to the organization's?" Six of the article's claims bear on it, and LEAD-tmpiktom advances it. It is the exchange's question for this article, the curation lists it in A49's Article 7 backbone, and the draft never names it. Cite? **Yes.**
- **CLAIM-595** (Active, demonstrated): "Persistence and nucleating productivity in the committor sense vary independently". **Supports** CLAIM-tmpgvsgg (persistence of the seed against what it nucleates) and CLAIM-tmp4uj40 with a demonstrated result. Part II's review recommended it for Art. 6, and it fits here better. Cite? Yes.
- **CLAIM-185** (Proposed, interpretive): "The nucleation threshold of an argument is whatever makes a structure persist". With it, **CLAIM-184** (Proposed, counter: anchors entrench) and **QUESTION-037** (Open). This is the nucleating-argument line. The curation of 2026-11-24 20:56 found that A4's opening "misses the nucleating-argument line (CLAIM-185, CLAIM-184, QUESTION-037)", and this draft misses it too. Cite? Yes, 185 and 184 in one line.
- **CLAIM-tmpyqjn0** (Proposed, interpretive; a member): the belief that fiduciary duty requires maximizing shareholder value "can bind a corporation more tightly than the applicable law does ... and so help produce the organizational character later presented as a legal necessity". It complements CLAIM-tmpdq0ah and CLAIM-402. It is the record's held instance of a meme carrying a governance protocol (§7.2) and of a representation helping produce what it describes (§7.4). Its note records that eBay v. Newmark "narrows the doctrine–meme gap". Cite? Yes.
- **QUESTION-439 and QUESTION-360** (Open): CLAIM-620 and CLAIM-621 bear on both. QUESTION-439 asks whether rival communities using one expression share "one concept with context-dependent extension, several historically related concepts ..., or an organization of the rivalry". That is CLAIM-621's symbolic-against-conceptual question. Cite? Yes, 439.
- **LIT-tmpflbme** ("The Death of the Author", Deferred; registered in commit 39a0a7dc). **Contradicts** §7.2's "Barthes's essay is not yet registered". Cite? **Yes, must correct.**
- **CASE-147** (Active, reported): Kalla and Broockman's field experiments, in which narrative exchange did what argument did not. It is one of CLAIM-430's grounds. **Bears on** Limits ("The human evidence is read, not gathered"), as a read human study behind perspectival invitation. Optional.

### §7.3 "I am whatever you say I am"

- **CASE-140** (Active, construction): "two people with similar dispositions hear the same negative characterization, one told it comes from a few critics and the other believing it speaks for nearly everyone ..., so that the words are fixed and only their attributed breadth differs". It illustrates CLAIM-415. It is the held matched construction of the false-plurality half, and LEAD-tmp0w114 is close to its operationalization. The section cites CASE-141 and CASE-142 and omits it. Cite? **Yes.**
- **SYNTHESIS-052** (Proposed): the account that integrates CLAIM-415, CLAIM-425, CLAIM-426, TERM-075, CASE-140 to CASE-142 and QUESTION-119 ("What a collective is credited with need not be what its members hold"). §7.3's account goes unnamed. Cite? Yes.
- **CLAIM-493** (Proposed, interpretive): a vocal minority "can fix the fanbase's public stance through a group process and not only through biased sampling of who speaks". **THEORY-1608** (Active, Spears on self-categorization) corroborates it, and **QUESTION-119** (Open) is the question it answers. **Qualifies** CLAIM-415's "false unity": attributed plurality can be produced, not only misperceived. Cite? Yes.
- **CLAIM-424** (Active, interpretive): reflexive governance of perspectival arrangements "is a capacity some organizations of perspective have and others lack ... the capacity to revise those standards is not the capacity to revise them well". CLAIM-tmp5tjtg **rests on** it, as it does on CLAIM-532 (Active) and CLAIM-545 (Proposed). It is the Active premise under "A seeded capacity to revise". Cite? Yes.
- **CLAIM-327** (Proposed): a reputation is part of a collective's dynamics "when its members read it, condition what they do on it, and by doing so regenerate it". It gives the mechanism by which an attribution becomes consequential. Optional.

### §7.4 Hyperstition

- **THEORY-267** (Active): in "a pre-registered randomised experiment on 817 Manifold play-money markets, about 59% of a ±5-point price shock that no trader's information supported was still present after 60 days". **THEORY-810** (Proposed) extends it, and **QUESTION-212** (Open) asks whether "the traders come to believe the shocked price". **Supplies nearer data** than THEORY-2070, which is Proposed and correlational. It is a randomized case of an unsupported representation persisting. QUESTION-212 is §7.5's distinction asked of real people: does the price persist as a fact about markets, or as a belief? Cite? **Yes.**
- **LEAD-tmp5msck** (Open, idea; filed 2026-11-25 in 39a0a7dc): "Find a field case of hyperstition with a withdrawal". It advances CLAIM-426, CLAIM-tmpvic6m, CLAIM-tmpnws9d and CLAIM-tmpyp5bu. **Contradicts by omission** "No field case ... is on the record": the lead for it is now on the record, and §7.7's "a field case with withdrawal" should cite it. Cite? **Yes, must update.**
- **CASE-297** (Proposed): "Communities forming subcommunities on Reddit, the owner's example". With it, **LEAD-003** (Open): "Study community formation on Reddit as it happens ... where founders come from, whether the community individuates and lasts". This is the owner's case in THEORY-2070's setting, and LEAD-003 is the study that would test whether Krohn and Weninger's correlation is formation. Cite? Yes.
- **CASE-111** (Active, construction): "A fold in boundary maintenance ... maintenance lost past the fold is not restored by returning the parameter". It **grounds** CLAIM-463, CLAIM-tmpgvsgg and CLAIM-tmpq1lyz. It is the held construction of J7.2's "second stable state", so J7.2's shared shape is already one construction under three of its components. **Partly states J7.2.** Cite? **Yes, in J7.2's components.**
- **CLAIM-tmpggu4v** (Proposed, interpretive; a member): an anchor "may act by nucleation, helping a new response organization form that then maintains itself, so its influence outlasts the anchor; the mechanisms part on what follows the anchor's removal". It rests on CLAIM-463 and is grounded in CASE-111, and **LEAD-tmp3nqe0** (Open) tests it. It is a fourth place of J7.2's shape, and it states the withdrawal discriminator that J7.2 and CLAIM-tmpyp5bu use. Cite? Yes.
- **CLAIM-600** (Active, interpretive): "Transient support can be withdrawn safely only if it started a process that keeps itself going ..., was large enough to carry the supported party past any threshold". It complements CLAIM-tmpgvsgg. It is the held general condition of which CLAIM-tmpnws9d is the hyperstition instance. **Supports.** Cite? Yes.
- **CASE-191** (Active, construction): formation provenance is told apart only by a knockout during formation. LEAD-tmpiktom's note names it as a formal precedent for A4's interventions. It **bears on** CLAIM-tmpnws9d's "a single withdrawal at an unknown stage does not discriminate". Cite? Yes, in §7.7's "Withdraw the seed" row.
- **CLAIM-408** (Active, demonstrated): a neutral constraint, by weakening, makes unequal authority stable. It is another bistable instance, integrated with CASE-296 in SYNTHESIS-108. Optional for J7.2.

### §7.5 A changed referent against apparent confirmation

- **CLAIM-416** (Active, interpretive): "Competing perspectives compete over the tests that measure them ...: success under an evaluative regime is evidence of competence relative to that regime ..., and a perspective that gains influence over the test can change what later success shows". This is the record's Active statement of A51's "apparent confirmation produced by the evaluation regime". It complements CLAIM-402. **Supplies the missing reading** for the section's title distinction. Cite? **Yes.**
- **CLAIM-297** (Active, interpretive): when authority is updated "by how well it performs on the interpretation it helped make dominant, the coupled meaning and influence ... can amplify an initial interpretive advantage without any gain in fidelity to independent evidence". With it, **CLAIM-330** (Active, demonstrated; CLAIM-620, CLAIM-402 and CLAIM-342 rest on it) and **CLAIM-1202** (Active, demonstrated): evaluator capture with "informational independence" while "a resource channel runs". These are the held mechanism of the fixed-preference arm of J7.3. Cite? Yes, 297 and 1202.
- **THEORY-861** (Active): when a deployed model changes the distribution it is scored on, retraining "converges to a unique performatively stable point when ε < γ/β". It corroborates CLAIM-402, and it is the formal reading of a measure that reshapes what it measures, beside THEORY-839 and THEORY-862. Cite? Yes.
- **SYNTHESIS-108** (Proposed): "How an equivalence becomes a unit". It integrates CASE-296, CLAIM-762, CLAIM-402 and CLAIM-408. **QUESTION-276 and QUESTION-113** (Open) are the questions CASE-367 bears on. This is the line's account of the genres case that CASE-367 built, and the draft uses CASE-367 without it. Cite? Yes, SYNTHESIS-108.
- **CASE-247** (Proposed, construction): "The newsroom that reads low traffic on the investigations it no longer funds ... takes that as evidence they are not wanted, until it no longer has the sources or expertise". It illustrates CLAIM-342, CLAIM-463 and CLAIM-656. It is a held case in which the regime's measures confirm while the referent (the capacity to investigate) is lost: J7.3's two arms in one construction. Cite? Yes.
- **CLAIM-655** (Proposed, demonstrated): the preference an optimizer reads "can move with no one's preferences changing" as the worst-served users leave. With it, **CLAIM-653 and CLAIM-658** (Proposed). These give a third route beside a changed referent and a changed reading: a changed population. It bears on J7.3 and CLAIM-955. Optional.

### §7.6 From regularity to operative norm

- **CASE-101** (Active, construction): "Three simulated populations with the same turnover and the same aggregate statistics: one whose members respond alike to a common input, one that transmits its norms to its replacements, and one held together by an institution". With it, **CLAIM-926** (Proposed, demonstrated; CASE-347's claim): "a priced lagged block test finds a population held together by delayed transmission, with its lag". **Qualifies J7.4.** The draft says the record "does not yet state" a marker beyond observed restoration. The record holds a construction and a test that tell norm transmission from common response. Cite? **Yes.**
- **CLAIM-945** (Proposed, empirical; from CASE-362, complementing CLAIM-946): "the coupling shows in how fast the deviants are drawn back", not in how far the others move. J7.4 cites CLAIM-946 and omits its companion, which bears directly on what restoration does and does not show. Cite? Yes.
- **CLAIM-288** (Active, interpretive, counter): "In a population whose operators each maximize an objective the modeller fixed, the norms the organization appears to maintain are set by the modeller". It is the Active precursor of CLAIM-tmpyxemn and of the norm model's corrected reading. Cite? Yes.
- **QUESTION-128** (Open): "Does the record's organizational account give a path to normativity from first principles". CLAIM-tmphq6hp and CLAIM-tmpjg5gx bear on it. It is the open question under "and not to legitimacy". Cite? Yes.
- **LEAD-tmpuuj6e** (Open), with **ARG-tmpqkfwb and ARG-tmpo7ijm** (Proposed): the reading lead and the two arguments for the owner's race-based-power case behind CLAIM-tmp8l5s9. Cite? Yes, the LEAD, as the "fitted case" of §7.7.
- **THEORY-2120** (Proposed, Schelling on focal points) and **CLAIM-766** (Proposed). These bear on convention as conspicuous solution, beside the ladder. Optional.

### §7.8 External comparison

- **LEAD-tmplsxtr** (Open, idea; filed 2026-11-25): "Read the published rivals of memetic nucleation, complex contagion, cultural attraction and dual-inheritance cultural evolution". **Contradicts by omission** the section's statement of "the gap that matters most": the lead now exists. Cite? **Yes, must update.**

### Cited entries misreported (Article 7)

- **SYNTHESIS-077 for CLAIM-132's content.** See above. The quoted limit has Active, demonstrated standing, not Proposed.
- **Barthes "not yet registered"**: LIT-tmpflbme.
- **J7.1 and J7.4, "Stated by an entry? No".** After 39a0a7dc, dated notes on CLAIM-tmpjitli ("fidelity against convergence") and CLAIM-tmphq6hp ("restoration and a copied majority") state them, and LEAD-tmpiktom carries the note "the first site was run". The joins section should say the joins were placed as notes before testing.
- **J7.2's "No entry joins the hyperstition result to the norm model"** is literally true, but CASE-111 grounds three of its components (see above).

---

## Region 2. Obligation, standing, rights, cooperation, repair, answerability (Article 8)

### §8.1 What A51 asks

- **SYNTHESIS-098** (Proposed, version 2, 2026-11-17): "Remedies foreclosed before review, by faits accomplis, speed, friction and siege: acting before an opportunity to intervene can take effect is proposed as a wrong of its own". It integrates CLAIM-723 with CASE-285, the proposed speed study of which **CASE-316 is a variant**, and with CLAIM-722, CLAIM-724, CLAIM-748 and CASE-287. It is the account of §8.4, and §8.1's list of accounts omits it. **Qualifies** J8.3's "No account integrates CASE-316". The account integrates its design beside CLAIM-723. Cite? **Yes.**
- **SYNTHESIS-094** (Proposed): "The wrong beyond harm and how an organization becomes normatively less informed". It integrates CLAIM-614, CLAIM-624, CASE-229, ARG-055, QUESTION-441 and QUESTION-449. It is the account of §8.4.3, which the section never names. Cite? **Yes.**
- **SYNTHESIS-100** (Proposed, version 5): the map of "Assess Depp Heard Abuse". It integrates SYNTHESIS-098 and SYNTHESIS-101 to SYNTHESIS-104, and also CLAIM-704, CLAIM-705, CLAIM-706, CLAIM-711, CLAIM-750, CLAIM-751, CLAIM-905, CLAIM-1033 and CLAIM-1062. The draft cites it only for CLAIM-741. It is the parent account of A51's four, and it holds the speed and blameless-review entries that §8.4.2 and §8.8 use. Cite? Yes.
- **SYNTHESIS-038** (Proposed, version 9): "The organizational-normativity line is four accounts that meet at its root questions". This is the line account above A51's four. Optional.

### §8.2 Rights, demands and commitments

- **CLAIM-752** (Proposed, interpretive, counter; `objects_to` CLAIM-729): the duties to comply and to support "may be one duty, as Rawls's natural duty treats them". **Qualifies** the "Duties to institutions" bullet, which gives CLAIM-729 without its counter. It also bears on §8.7's "no principle of fair play of the kind Hart and Rawls stated": the record holds Rawls's natural duty as a counter. Cite? **Yes.**
- **CLAIM-722** (Proposed, interpretive): "Succeeding in making a remedy unreachable gains a wrongdoer no normative power over what is owed". It complements CLAIM-720 and CLAIM-743. It sits with "A demand's ending", and it is the bridge from §8.2 to §8.4. Cite? Yes.
- **CASE-286** (Proposed, construction): "Voluntary submission against alienation of standing". It illustrates CLAIM-720 and is the matched case the section's CLAIM-720 bullet lacks. Optional.
- **CLAIM-tmpe6yfm** (Proposed; the owner's U14): "Processes need not owe one another moral duties for a system of them to enter a pathological regime". It complements CLAIM-075 and CLAIM-725, and it bears on JR8.1 and on §8.9's separation of cooperation from its assessment. Optional.
- **CLAIM-363** (Active, interpretive) and **TERM-059** (Active): a normative judgment "is well-defined only once its relata are fixed ... and that dependence does not by itself make it relative". This is the frame under "none establishes another". Optional.

### §8.3 A right as a constraint on policy

- **ARG-043** (Proposed): "one end state with opposite verdicts, show a normative judgment about an organization that depends on a history its end state does not show". With it, **CLAIM-608** (Proposed): histories add a relatum. **Qualifies.** CLAIM-741 holds that respecting a choice-protecting right is "a property of its policy ..., not of any realized history". The record also holds that some judgments depend on histories that the end state does not show. The two are compatible: a policy is not an end state, and a history is not an outcome. But the section's "an evaluation over endpoints or realized histories cannot represent such rights" should be set beside it. Cite? Yes.
- **QUESTION-454** (Open): "What makes one agent's authority to decide about another's body legitimate when the other has standing but cannot decide". With it, **THEORY-1649** (Proposed; Eyal on informed consent: an "invasive-refusal core" plus a weaker "rim"). These are the held question and reading next to CASE-283's competent patient. Cite? Yes, QUESTION-454.
- **CLAIM-tmpxl4mg** (Proposed): "a statistical tolerance for failures does not make any failure within it acceptable". This is a rights-against-rates statement close to CLAIM-741's "not of any realized history". Optional.

### §8.4 Defeated standing

- **CLAIM-705** (Proposed, demonstrated): "When an institution produces challengeable decisions faster than its corrective process can resolve them, the formal right to challenge stays with everyone while its preventive effect cannot: ... at most a share μ/λ can ever be resolved in time". With it, **CLAIM-704** (Proposed, demonstrated): the order of review decides whose right still prevents anything. Both are in SYNTHESIS-100, and CLAIM-705 complements CLAIM-740 and CLAIM-464. They are demonstrated derivations of CLAIM-723's second condition by timing, beside CASE-316. **Qualifies §8.4.2's "the record has not linked"**: the record links timing to the entitlement through CLAIM-740, and to defeated standing through SYNTHESIS-098. Cite? **Yes.**
- **CLAIM-462** (Active, interpretive): "An arrangement of institutions can keep, or increase, its capacity for effective action while its capacity to be effectively corrected by others degrades". CASE-316 **illustrates** it and CLAIM-879 **corroborates** it. **Contradicts** J8.3's "No account integrates CASE-316 or CLAIM-879" only in spirit, since CLAIM-462 is a claim and not an account. But CASE-316 is linked to an Active claim, and the draft says it is unlinked. Cite? **Yes.**
- **LEAD-216** (Open): "Extend the oversight queueing model with an affected party who petitions ... and measure the harm done to that party before the limit can be revised". It advances CLAIM-879. It is the lead that would give CASE-316 the affected party whose absence the J8.3 note on CASE-316 names. Cite? Yes.
- **QUESTION-441** (Open): "What exactly is the counter-normativity committed by a self-maintaining organization that harms and reproduces the representational projections". LEAD-097 advances it, and CLAIM-1155, CLAIM-1184 and CLAIM-614 bear on it. It is §8.4.3's question, unnamed. Cite? **Yes.**
- **CLAIM-403** (Active, interpretive): admission, recognition, credibility, uptake and revision of standards "are separable". CLAIM-1155 **rests on** it. It is an Active premise of the claimant's side, and the section omits it. Cite? Yes.
- **CLAIM-652** (Proposed, demonstrated), **CASE-246** and **ARG-092** (Proposed): "as the harmed leave, the recognized cost of the practice falls ... with no act against complaint". They bear on QUESTION-441 and sit in SYNTHESIS-094. A demonstrated route by which an organization's harm stops registering, beside ARG-228's taxonomy route. Optional.

### §8.5 The instrumentalist objection

- **QUESTION-481 and QUESTION-484** (Open): who has standing to authorize changes to an arrangement's governing structure, and how feasibility bears on the governing principles. LEAD-033 advances both, and CASE-336, CLAIM-908, CLAIM-909 and CLAIM-913 bear on them. These are J8.2's questions on the CASE-336 side. Cite? Yes, 481.
- **CLAIM-431** (Proposed, counter): "A corporation's functional remorse cannot be told from prudence". With it, **ARG-tmp4er8c** (Proposed): the sanction-lift test separates normative from instrumental recognition "only with reputation and other benefits held fixed". **LEAD-tmp466iv** (Open) tests whether answerability survives perturbations "that make it unprofitable". These are a third held instance of the instrumentalist residue in §8.5's structure (normative or instrumental, with the instrumental difference matched). Cite? Yes, ARG-tmp4er8c.

### §8.6 Standing and answerability

- **CLAIM-tmpa61rf** (Proposed, interpretive; a member; A48 from this exchange): "To have standing toward an agent is to have claims that can constrain what it is entitled to optimize, not only to enter its objective". It complements CLAIM-738, CLAIM-739 and CLAIM-tmptrn75. It is the exchange's own account of standing as a directed constraint, and the section quotes A51's "directed relationships" without it. Cite? **Yes.**
- **SYNTHESIS-121** (Proposed): "Correcting a regulator and keeping a plurality correctable". It integrates CLAIM-523, CLAIM-727, CLAIM-740 and TERM-126. With it, **QUESTION-482 and QUESTION-485** (Open). QUESTION-485 asks "From where does a relationship, a capability or a restriction derive its legitimacy". That is SYNTHESIS-103's "why anyone is owed an answer at all". Cite? Yes, QUESTION-485.
- **SYNTHESIS-093** (Proposed): "What is owed by those who govern an arrangement others depend on". It integrates CLAIM-687, CLAIM-673, CLAIM-678 and CLAIM-684. It is the account behind "Influence is not enough" and CLAIM-687, and it bears on Article 9 §9.7. Cite? Yes.
- **CLAIM-678** (Active, interpretive): power over a technological arrangement has "operational ..., economic ... and epistemic power ... held and distributed separately". It complements CLAIM-523. It sits with the bounds on authority. Optional.
- **CLAIM-tmp2kfwd** (Proposed): formulating, standing, resources and consequence are "four separate achievements". It complements CLAIM-523. Optional.

### §8.7 The grounds of special obligation

- **LEAD-tmphsmng** (Open, idea; filed 2026-11-25 in 39a0a7dc): "Read the works on associative obligation and fair play, for whether membership in a cooperative scheme grounds obligations of its own". It advances QUESTION-460, CLAIM-959, CLAIM-960 and CLAIM-671. **Contradicts** G8.3 ("This is a candidate reading LEAD for QUESTION-460"), because the lead is filed. Cite? **Yes, must update.**
- **QUESTION-tmpeiurf** (Open; filed 2026-11-25; `refines` QUESTION-460): "Do entrusted authority, or control over the essential conditions of another's participation, ground obligations to those affected in their own right". **Contradicts** G8.4 ("A QUESTION ... would hold whether either grounds an obligation"), and the table's last two rows should cite it. Cite? **Yes, must update.**
- **CLAIM-673** (Active, interpretive; rests on CLAIM-605): "the arrangement can erode the capacity to govern it, so that whether a collective can correct an arrangement is not independent of the arrangement". It advances LEAD-131 and complements CLAIM-876. It bears on the bearer question (§8.4.3's last paragraph; CLAIM-876 against CLAIM-877) and on the "Control over essential conditions" row. Cite? Yes.
- **CLAIM-457** (Active, demonstrated): "That no single institution can bring about a remedy does not imply that no combination of them can". It complements CLAIM-418, the premise of CLAIM-960's bearer step. **Supports** that step in a demonstrated form. Cite? Yes.
- **THEORY-1819** (Proposed; Lovett and Riedener): organizations "have no moral status, and ... what we seem to owe them ... we owe to their members". It corroborates CLAIM-075 and bears on QUESTION-460. With it, **THEORY-1823** (Proposed; Kittay): "nested relations of dependency are the basis of society", with doulia owed by the wider society. It bears on QUESTION-460 and QUESTION-461. These are held readings on both sides of CLAIM-960 against CLAIM-959. §8.7 says the only readings pointing toward CLAIM-959 are Thompson and Fineman, and Kittay is a third. Cite? **Yes, both.**
- **QUESTION-461** (Open): "When an organization comes to depend on the contributions of participants it subordinates, under what conditions does that dependence increase their effective authority over it". It is a refinement point for the "Vulnerability and control" row and for Article 9. Cite? Yes, in Art. 9 at least.

### §8.8 Repair without blame

- **CLAIM-1062** (Proposed, interpretive, counter; `objects_to` CLAIM-750; in SYNTHESIS-100): "A single postmortem's causes and action items are the wrong unit for testing where a blameless practice's trace stops: Google's practice routes questions about priorities set above the team to reviews of repeated incidents ...". **Qualifies CASE-335 and CLAIM-905.** The draft says the pilot "corroborates CLAIM-750 weakly" and lists what remains, but omits the held objection to the pilot's unit. Cite? **Yes.**
- **CLAIM-751** (Proposed, interpretive): "The upstream provenance of a failure can be carried without blame". It is grounded in the Tempe NTSB investigation (CASE-292). With it, **QUESTION-476** (Open; refines QUESTION-470) and **LEAD-189** (Open). These are the held answer to CLAIM-733's "blame gives us provenance" and the question LEAD-119 advances. §8.8 cites CLAIM-1033 on Tempe and not this. Cite? **Yes, 751 and QUESTION-476.**
- **CLAIM-1064** (Active, demonstrated; a member) and **CASE-396** (Active, executed): "In an institution each of whose recognized violations is penalized, newly recognized ones included, whose discovery of requirements earns nothing ..., inquiry ... never raises its score"; in the run, the institution "learns to make no inquiry in every setting while its internal record shows almost no violations". This is the record's executed and Active result for why penalizing recognition, a blame-like regime, suppresses the discovery that correction needs. It is the mechanism behind the blameless rationale, and §8.8 cites no executed result for it. LEAD-181 is now Done on this run (curation 2026-11-25 02:20). Cite? **Yes.**
- **CASE-284** (Proposed, construction): "Identical harm, different remedial assignments ... the duty to address the wrong is the same and the corrective paths differ, assigned without inventing blame". It illustrates CLAIM-717 and CLAIM-742. It is the held matched construction for JR8.2's open item, who owes the repair. Cite? Yes.
- **CLAIM-707, CLAIM-708 and CLAIM-714** (Proposed; in SYNTHESIS-104 or SYNTHESIS-038). CLAIM-707: blame placed "where failure becomes visible, so that those blamed ... can be those with the least control". CLAIM-714: "where no one is culpable for the incapacity the duty to repair still stands". With them, **QUESTION-473 and QUESTION-449** (Open). Cite? Yes, 714 (it is CLAIM-742's thesis from the incapacity side) and 707.

### §8.9 Morality and cooperation

- **THEORY-457** (Proposed; `rivals` THEORY-468): "When people can choose their cooperation partners and have equal outside options, the stable division ... is in proportion to each partner's contribution, and partner choice selects for a genuine sense of fairness". This is the mutualistic rival to morality-as-cooperation, and the section omits it. It also bears on Article 9's outside options. Cite? **Yes.**
- **CLAIM-766** (Proposed): in children's equal division, "the joint 'we' supplies the motive ... and the equal split supplies its content". It is grounded in THEORY-495, THEORY-2120 and THEORY-2111. With it, **LEAD-198** (Open) and **ARG-123** (Proposed). This is the record's own claim on joint commitment and obligation, beside THEORY-2109 (Tomasello). Cite? Yes.
- **QUESTION-371** (Open): "Can a moral norm work among cooperating groups as a stabilizing mechanism does in coexistence theory". CLAIM-547 bears on it. It bears on the second held result (CLAIM-546, CLAIM-547). Optional.
- **QUESTION-128** (Open): a path to normativity from first principles. CLAIM-tmp1fj5p and CLAIM-tmpreipd bear on it, and it refines QUESTION-460. Cite? Yes.
- **CASE-257** (Proposed, reported): the theatres of colonial Saint-Domingue, where people contributed while excluded from standing. It illustrates CLAIM-546, CLAIM-403 and CLAIM-348. It is the region's documented case of exploitation within successful cooperation (CLAIM-tmpreipd's step 2), and §8.10's row "No case of care for non-reciprocators" has no counterpart for step 2 either. Optional.

### Cited entries misreported (Article 8)

- **G8.3 and G8.4 as "candidate" LEAD and QUESTION**: both filed (LEAD-tmphsmng, QUESTION-tmpeiurf).
- **J8.1, J8.2, J8.3 and G8.5, "Stated by an entry? No" and "No entry links"**: after 39a0a7dc, dated notes state them on CLAIM-741 ("defeated standing"), CLAIM-1184 and CLAIM-913 ("a parallel instrumentalism"), and CASE-316 and CLAIM-723 ("the timing of defeated standing, modelled"). **G8.6 is done** (CLAIM-741's "what holds it back" note).
- **§8.4.2's "the record has not linked"**: the link was there in substance. SYNTHESIS-098 integrates CLAIM-723 with CASE-285 (CASE-316's parent design), and CLAIM-462 is illustrated by CASE-316 and corroborated by CLAIM-879.
- **§8.7's "The only readings pointing this way are of collective agents (Thompson, THEORY-1814; Fineman, THEORY-1818)"**: Kittay (THEORY-1823) is also held.

---

## Region 3. Dependence, bargaining, capability substitution, exploitation, domination, exit (Article 9)

### Limits and §9.1 Dependence produced by successful provision

- **THEORY-1492** (Active): three Food for Peace projects in Kenya, followed two to three years after exit, where "impact at exit did not necessarily predict sustained benefit". It **corroborates** CLAIM-602 and CLAIM-605. With it, **THEORY-1466** (Active; Baird, McKenzie and Özler): cash transfers "without an employment focus leave prime-age adults' work and earnings little changed". It corroborates CLAIM-600. **THEORY-1461** (Active; the TVA's subsidies and their withdrawal) and **THEORY-1496** (Active; Food for Peace India handover) are also held. These **qualify** Limits ("Every result here is a model") and §9.1's Samaritan bullet. The record holds field readings that corroborate the mechanism, and one Active review (THEORY-1466) that bounds the "aid weakens upkeep" reading. §9.1 cites only THEORY-1480, whose evidence is "five short illustrative field cases". Cite? **Yes, 1492 and 1466.**
- **CLAIM-600** (Active, interpretive): withdrawal is safe "only if it started a process that keeps itself going ..., was large enough to carry the supported party past any threshold ..., and left the work to the party throughout". It rests on CLAIM-597, CLAIM-602, CLAIM-604 and CLAIM-566, and it is grounded in THEORY-1461, THEORY-1465 and THEORY-1492. It corroborates CLAIM-603 and THEORY-1480 and complements CLAIM-605. It is the held Active condition joining §9.1's models to field readings, and it states "left the work to the party throughout", which is the order-of-supply point. Cite? **Yes.**
- **CLAIM-597** (Active, demonstrated): "an organization can become independent of what founded it but never of what feeds it". It complements CLAIM-602 to CLAIM-604. It is the held boundary between dependence on supply and dependence on founding. Cite? Yes.
- **CLAIM-673** (Active, interpretive; rests on CLAIM-605): an arrangement that "does the work through which [governing capacities] are exercised ... can erode the capacity to govern it". This is CLAIM-605's mechanism applied to governance, Active. It bears on §9.7's third condition (the dependent's means of challenge decay by the same mechanism). Cite? **Yes.**
- **CLAIM-721** (Proposed; in SYNTHESIS-101): "a restriction justified by a lack of competence lowers the competence it waits for". It corroborates CLAIM-950 and is illustrated by CASE-364, and LEAD-104 advances it. It is the interpretive statement of the "restriction twin" that §9.1 gives only as CLAIM-950. Cite? Yes.
- **CLAIM-558** (Active, interpretive): "a capability kept for rare events is maintained by practice outside operation, not by operation". It complements CLAIM-602 and corroborates CLAIM-600. Optional.
- **CLAIM-676** (Active, interpretive): "Two forms of assistance that deliver the same outcome can leave the person different participation in worthwhile activity". It complements CLAIM-675. With it, **CLAIM-688** (Active): a collective's capacity to decline a technology can depend on competition. Optional.
- **QUESTION-398** (Open): "Under what conditions does a partial organization become independent of the intervention that originally established it?" With it, **QUESTION-399** (Open). CLAIM-602, CLAIM-603 and CLAIM-604 bear on both, and LEAD-025 and LEAD-197 advance them. This is §9.1's open question. Cite? Yes, 398.
- **QUESTION-526** (Open): "What standard makes the loss of a pathway to alternatives justified by the benefits of consolidation, so that destructive lock-in can be told from productive specialization?" This is the standard that CLAIM-603's "dependency or division of labour" needs. Cite? Yes.
- **CLAIM-tmpb1wyc** (Proposed; a member): "A provider whose realized reliability exceeds its declared guarantee can lower the resilience of the organization built on it: those who depend on it stop maintaining the fallbacks". It is grounded in **CASE-tmp3xxqg** (Proposed, the Chubby outage, which **illustrates CLAIM-603**). With it, **ARG-tmptccms** and **CLAIM-tmpzas6q** (Proposed). These are the exchange's own documented specimen of dependence produced by successful provision, and the curation assigns them to Art. 10. §9.1's cross-domain account lists Black Queen, Samaritan and endosymbiosis but not the engineering specimen that illustrates CLAIM-603. Cite? **Yes, CASE-tmp3xxqg and CLAIM-tmpb1wyc.**
- **CLAIM-tmpv5sry** (Proposed; a member; the Part IV close, passed ADR-075 by discriminating prediction): "reliable provision, cooperation that works and optimization that meets its objective can each produce [pathologies] ..., so ... the pathology can deepen while ordinary performance holds". It rests on CLAIM-670, CLAIM-tmp8bimm, CLAIM-700 and CLAIM-tmpb1wyc. It is the held integration of §9.1's "Service is whole throughout, so nothing looks wrong" with §9.6, and A51's "integrates the record's accounts" (§9.11) should name it. Cite? **Yes.**
- **CLAIM-1054** (Proposed; a member): "a query-induced capability trap ... the one that optimized away capacities only an unasked query needs is rewarded". It bears on CLAIM-tmp2jhc1's "optimizing away every apparently unused capacity". Optional.

### §9.2 Producing a dependency, and encumbering one

- **CASE-tmp3so1p** (Proposed, stipulated): "a service of quality 80 that costs nothing to leave and one of quality 20 that costs 60 to leave keep the same 63.5 percent of their customers, so the retention figure merges satisfaction with lock-in". It **illustrates CLAIM-670**. This is a held construction on the exit side of the encumbrance, which §9.2 omits, and it is a ground of CLAIM-tmpv5sry. Cite? **Yes.**
- **CLAIM-684** (Proposed): "the burden of justifying it should rise with the size and the irreversibility of the narrowing". It complements CLAIM-677 and sits in SYNTHESIS-093. It is the normative side of CLAIM-747's "not a neutral baseline". Optional.
- **SYNTHESIS-117** (Proposed): the flourishing line, which integrates CLAIM-675 and CLAIM-677. Optional.

### §9.3 Control over the terms, and §9.4

- **CLAIM-428** (Proposed, interpretive): "the same dependence can be organized as mutual opportunity, as competitive vulnerability or as coercive leverage". CLAIM-690 and ARG-110 **rest on** it. It is the uncited premise of the article's thesis. Cite? **Yes.**
- **THEORY-1979** (Proposed; Hart, "Incomplete Contracts and Control", LIT-2776, Active) and **THEORY-1985** (Proposed; Grossman and Hart, LIT-2745, Active). Both read residual control rights, and both **corroborate CLAIM-728**. They are the readings by which ARG-210 was Rejected ("the readings tell against step 3"). **Contradicts** Limits ("The record has read almost none of the rival fields ... Hart and Moore is LIT-2742 (Unfetched)"): the incomplete-contracts field is read in two works. §9.3's residual-control paragraph should cite them. Cite? **Yes, must correct.**
- **THEORY-457** (Proposed): with equal outside options, the stable division is proportional to contribution. It is a held reading on outside options in bargaining, beside CASE-264's symmetric Nash split. Cite? Yes.
- **LEAD-133** (Open): "Read the works on exploited commitment, with Hart and Moore on control rights". It advances CLAIM-703, CLAIM-713, CLAIM-728, CLAIM-682, CLAIM-690 and QUESTION-472. This is the held lead for G9.4 and Limits. Cite? **Yes.**
- **CLAIM-tmp6nzs1** (Proposed, demonstrated; filed 2026-11-25 in 39a0a7dc): §9.4's candidate claim, filed. It rests on CLAIM-605 and is grounded in CASE-264. **Contradicts** §9.4's "It has not been put to the record" and G9.1's "as a Proposed claim" (future tense). The notes on LEAD-tmpeo8wq and CLAIM-tmp2jhc1 that G9.1 asks for are also filed, and so are `analysis/README.md` and the dated output `fallback_decay_bargaining.2026-11-25.txt` ("uncommitted" in §9.4). Cite? **Yes, must update.**
- **LEAD-tmpfzx2c** (Open; filed 2026-11-25): "Price the provider's side of the decaying fallback". This is G9.2, now filed. **LEAD-tmp3w42f** (Open; filed 2026-11-25): "Put a claimant's runway and a capacity learned by doing in one model". This is G9.3 and J9.6, now filed. Cite? **Yes, must update.**
- **CLAIM-571** (Active, demonstrated): "the resource threshold for reaching a target configuration ... is the least, over admissible transition paths, of the peak requirement". LEAD-tmpeo8wq advances it. It bears on §9.4's "Anything about reach over TERM-114" disclaimer. Optional.

### §9.5 The cost of contesting

- **CLAIM-601** (Active, demonstrated): "A savings buffer is a stock of time: ... households with the same preferences decline profitable delayed investments below it, a choice that reads as impatience and is the right policy for survival by a deadline". It complements CLAIM-604, CLAIM-744 and CLAIM-748. It is the held demonstrated form of CASE-287's runway (siege) and of CLAIM-744's patience. **Supports**, and it is a natural component for G9.3. Cite? **Yes.**
- **CLAIM-736** (Proposed; in SYNTHESIS-101): an opposition "can be independent as an actor ... while its capacity to change the arrangement it opposes depends on another party's control of its resources, standing, corrective authority or time; that controlled incapacity ... is what makes a contained opposition a mark of domination". It bears on QUESTION-479 and complements CLAIM-686. It is the bridge from the cost of contesting (§9.5) to domination (§9.7). Cite? Yes.
- **CLAIM-705 and CLAIM-704** (Proposed, demonstrated): see Region 2. These are speed results beside CLAIM-879, and **CLAIM-711** (Proposed, counter; illustrated by CASE-316) holds that "A process with no procedural friction can still be interruptible", which objects to CLAIM-710 behind CLAIM-731. **Qualifies** "Friction moves" and "Speed". Cite? Yes, 711.
- **LEAD-216** (Open): see Region 2, the oversight model with an affected party. **LEAD-152** (Open): "Read the works on procedural friction". Optional.
- **SYNTHESIS-098** (Proposed): the account of friction, siege and speed (it integrates CLAIM-748, CASE-287, CLAIM-716, CLAIM-731 and QUESTION-479). §9.5's account goes unnamed. Cite? Yes.

### §9.6 Conscientiousness, commitment, and the hidden subsidy

- **CASE-343** (Active, executed; promoted 2026-11-24 23:11 after a rerun byte for byte): "a budget that follows observed activity loses a capability used once in two and a half years or more rarely in every run or nearly ... and none when maintenance is funded apart from activity". With it, **CLAIM-921** (Active, demonstrated; promoted the same pass; in the `governance-of-becoming` work), **CLAIM-577** (Active, demonstrated: "A budget set each period to the peak resource spent the period before never rises") and **CASE-412** (Active, executed: a matched-performance model in which "every regime produces the same output until a contingency arrives, while readiness ... ranges from 0.147 to 0.894"). **Contradicts in part** "No run of the hidden-subsidy loop is held". The half of CLAIM-700 in which "the organization budgets to what it observes" and "reconfigurations ... pass out of reach while the present arrangement stays feasible" is executed and Active, at matched present performance. That is A33 §10A's design without the conscientious compensator. What is not run is the compensation masking the shortfall. The draft's "CLAIM-700 ... uncorroborated; no run" (§9.11) should become *done in part*. This is the step-3a miss the devlog of 2026-11-25 03:30 predicted (a result filed under its mechanism's name). Cite? **Yes, must correct.**
- **CLAIM-679 and CLAIM-549** (Active, demonstrated): CLAIM-700 **rests on** both. CLAIM-679: cutting the resource held "toward what holding its present configuration requires ... removes exactly the transitions whose threshold lies between". The draft gives CLAIM-700 as uncorroborated and omits that two of its four premises are Active and demonstrated. Cite? **Yes.**
- **LEAD-022** (Open) and **CASE-290** (Proposed study): "Run the study of a fall in complaints: with working conditions fixed, measure separately whether members find them acceptable, see the discrepancy, are motivated and are able to voice it". LEAD-022 advances CLAIM-700. **Contradicts** "Its only lead is a regime of LEAD-tmp5l71z". Cite? **Yes, must correct.**
- **QUESTION-386** (Open): "Under what funding and incentive rules does allocating resources according to observed activity cause an organization to lose capabilities". CLAIM-602, CLAIM-700 and CLAIM-921 bear on it. **SYNTHESIS-124** (Proposed): "Keeping a route to reorganization under a budget rule that follows use". Cite? Yes, QUESTION-386.
- **THEORY-1917** (Proposed; Keller, LIT-2670): a person "can wrongfully place another under a genuine moral obligation ... fiduciary roles expose those who hold them to this moral blackmail". It **corroborates** CLAIM-703, CLAIM-713 and CLAIM-708, and it bears on QUESTION-472. §9.6 names Keller three times and cites no code for the reading. Cite? **Yes.**
- **QUESTION-477** (Open): "Is there a resource theory of moral commitments ... is the leverage one party gains from another's commitment a conversion that is free for the one and costly for the other?" It bears on CLAIM-713 and on the "price or bar" distinction (J9.4). Cite? Yes.
- **CLAIM-707 and CLAIM-708** (Proposed): blame placed downstream of control; responsibility for one's own conduct against responsibility for another's conditions. Both complement CLAIM-700, CLAIM-702 and CLAIM-703. CLAIM-702's measurement link ("The system's failure is attributed to the person who stopped compensating") is CLAIM-707's mechanism. Cite? Yes, 707.
- **QUESTION-487** (Open): "What lets those who act for an organization hold the principals who direct them accountable for the conditions under which they are required to act". Optional.

### §9.7 Domination, and who holds it

- **THEORY-1918** (Proposed; Frey and Schneider): "online platforms make exit and affective voice cheap while effective voice is nearly absent under consolidated control". It corroborates CLAIM-523. It is the held reading closest to A51's enshittification, and it locates the failure in voice under a holder's control. That bears on J9.5's "correctly not made". With it, **THEORY-152** (Proposed; Hirschman's "Further Reflections", LIT-750, Active), the first-hand reading of exit and voice. LIT-748's own status note says the book's argument "is read first-hand" there. **Contradicts** Limits' list ("Hirschman's *Exit, Voice, and Loyalty* (LIT-748) [is] Unavailable"), which omits that Hirschman is read. Cite? **Yes, must correct.**
- **THEORY-1960** (Proposed; Pettit, *On the People's Terms*, LIT-2760, Active): legitimacy under "individualized, unconditioned and efficacious" popular control. It bears on QUESTION-482. **Qualifies** "Pettit's *Republicanism* (LIT-1614) [is] Unavailable": a later Pettit book is read. It also gives a reading for CLAIM-682's "influence, challenge". Cite? **Yes.**
- **CLAIM-tmpvmd97** (Proposed; a member): "an accurate metric can still dominate where it gives a controller unanswerable discretion over those who depend on the arrangement". It complements CLAIM-682. It is a held domination-by-holder mechanism for the enshittification article, in TERM-124's sense, beside CLAIM-tmpjnly0's holderless erosion. Cite? Yes, in §9.7's holder line.
- **CLAIM-652, CASE-246 and ARG-092** (Proposed; CLAIM-652 demonstrated): "exit-driven drift". A practice expands "with no act against complaint" as the harmed leave. With them, **CLAIM-655** (Proposed, demonstrated). These are a demonstrated holderless mechanism (the optimizer's honest count of present users) of exactly the kind §9.7 says "may fall outside CLAIM-682's test". It is also the exit-side twin of §9.4: exit that worsens the terms for those who stay. Cite? **Yes.**
- **CLAIM-709 and CASE-279** (Proposed): "Equality of wrongdoing and equality of power are separate questions". This is a TERM-124 use beside CLAIM-690. Optional.
- **QUESTION-461** (Open): see Region 2. It has 11 links into this article's codes (CASE-264, CLAIM-669, CLAIM-670, CLAIM-682, CLAIM-686, CLAIM-690 and more), the most of any uncited entry, and it is the article's question about when dependence raises or lowers the dependent's authority. Cite? **Yes.**
- **SYNTHESIS-093** (Proposed): see Region 2 (CLAIM-687's account). **SYNTHESIS-101** (Proposed): it integrates CLAIM-728, CLAIM-744, CLAIM-721, CLAIM-736 and CASE-281. Cite? Yes, both, as the accounts §9.3, §9.6 and §9.7 draw on.

### Cited entries misreported (Article 9)

- **Limits, "The record has read almost none of the rival fields"**: Hart (THEORY-1979), Grossman and Hart (THEORY-1985), Pettit (THEORY-1960), Hirschman first-hand (THEORY-152), and Frey and Schneider on exit and voice (THEORY-1918) are all read. Restate it as "the founding books are unread; the field is read in these readings".
- **Limits, "Every result here is a model"**: true of the record's own results, but Active field readings corroborate CLAIM-602, CLAIM-605 and CLAIM-600 (THEORY-1492, THEORY-1466).
- **§9.6 "No run of the hidden-subsidy loop is held" and "Its only lead"**: see CASE-343, CLAIM-921, CASE-412 and LEAD-022 above.
- **§9.4 and G9.1 to G9.3**: filed as CLAIM-tmp6nzs1, LEAD-tmpfzx2c and LEAD-tmp3w42f, with notes on LEAD-tmpeo8wq and CLAIM-tmp2jhc1. The script's output is committed.
- **§9.3, ARG-210 "Rejected" because "the readings tell against step 3"**: the readings (THEORY-1979, THEORY-1985) are not cited.

---

## Region 4. Process history

- **Commit 39a0a7dc (2026-11-25 06:31), "Part III: file the drafts' joins and gaps".** It followed the three drafts (4a3a6de9, d6f7fa06, 6b21bd40). It filed CLAIM-tmp6nzs1, LEAD-tmp5msck, LEAD-tmplsxtr, LEAD-tmphsmng, LEAD-tmpfzx2c, LEAD-tmp3w42f, QUESTION-tmpeiurf and LIT-tmpflbme. It placed joins as dated notes on CLAIM-723, CASE-316, CLAIM-741, CLAIM-1184, CLAIM-913, CLAIM-tmpjitli, CLAIM-tmphq6hp, CLAIM-tmp2jhc1, LEAD-tmpiktom, LEAD-tmpeo8wq and SYNTHESIS-tmp4tvbr. Every "candidate LEAD", "not registered", "no entry states it" and "not put to the record" in the three drafts that these answer is now stale. This is the Part III analogue of Part II's top item. **Each draft needs a pass for it.** Two further consequences:
  - The joins now sit on the record as notes before ADR-075's step 5. The joins section of each article should say so ("placed as notes, untested").
  - CLAIM-tmp6nzs1 is filed as Proposed, demonstrated, with `grounds: CASE-264`. The computation itself is in `analysis/`, not in a CASE. Step 4 says "A result that bears on an entry goes back to the record as a CASE or a dated note". The claim's ground is a fictional toy, and the executed computation has no CASE. Flag for the reviewer.
- **Devlog 2026-11-25 03:30** ("Step 3a ran on Part II's drafts and still missed held work"): "A digest searched by the article's terms ... does not find a result filed under its mechanism's name." Part III repeats the pattern, and the clearest misses are by mechanism:
  - CASE-343, CLAIM-921, CASE-412 and CLAIM-577 for §9.6's "no run";
  - CASE-396 and CLAIM-1064 for §8.8;
  - CASE-101 and CLAIM-926 for J7.4's "a marker beyond restoration";
  - CASE-111 for J7.2;
  - THEORY-267 for §7.4's "nearest data";
  - THEORY-1492 for Art. 9's "every result here is a model".

  A note under that devlog is warranted: step 3a found held work by the drafts' terms and missed it by mechanism a second time.
- **Curation 2026-11-24 23:11** (status pass). It made CASE-343, CASE-412, CASE-397 and CLAIM-921 Active, along with CLAIM-1093 and CLAIM-1180 (both in Art. 5's region). These bear on Art. 9 §9.6 (above). The drafts' standing date ("after the merge of Part II's revision, e96cf5f3") postdates the pass, so the omission is a search miss, not staleness.
- **Curation 2026-11-25 02:20** (reruns). LEAD-181 is now Done on CASE-396's run, the run behind CLAIM-1064, which bears on §8.8. Its choice between CLAIM-1120 and CLAIM-997 stays the owner's, and §8.8 could name it. Article 7 (§7.7: LEAD-030, LEAD-087, LEAD-188) and Article 9 (§9.10: LEAD-104, LEAD-171) leave closing as "the owner's call". That is consistent with the run-lead skill ("Do NOT change the lead's status or stage; the owner marks it Done"); LEAD-089 and LEAD-181 were closed under the owner's "go ahead with the reruns". No correction is needed. The owner's choices section of each article could list the five closings together.
- **Curation 2026-11-24 20:56** (the exchange and A49's audit). Three points bear on Part III:
  - (a) A4's opening "misses the nucleating-argument line (CLAIM-185, CLAIM-184, QUESTION-037)", and Art. 7 misses it too.
  - (b) The A49 backbone for Art. 7 lists QUESTION-tmprvnp0, and Art. 7 does not cite it.
  - (c) The Part IV close CLAIM-tmpv5sry passed ADR-075 "by discriminating prediction" on components that are Art. 9's (CLAIM-670, CLAIM-tmp8bimm, CLAIM-700). Art. 9 should name it as the held integration.

  Its Miscitations section also records that "A46 says the record has no remorse account, but CLAIM-431, CLAIM-432 and CLAIM-1169 exist". Art. 8 §8.5 likewise does not use CLAIM-431 or ARG-tmp4er8c.
- **SYNTHESIS-tmp4tvbr, "Not stated on the record", A22 §22 bullet**: "dependency-mediated norm formation and asymmetric contractual organization: a map of CLAIM-tmp18v1o, CLAIM-tmpjg5gx, CLAIM-tmp8bimm and CLAIM-tmp4zii5 ... nothing further". It is an adjacent decline for Art. 9 (asymmetric contractual organization), not a decline of J9.1. Art. 9's statement that it searched "the 'Not stated on the record' sections of every account" and found no decline should mention the bullet as adjacent. Part I's review faulted J3 for missing the same bullet.
- **Part I review (REVIEW-2026-11-24), Part C items 8 and 9.** It recommended CLAIM-690, CLAIM-682 and CLAIM-686 for Art. 2's boundary, and CLAIM-tmpyp5bu and CLAIM-tmpgvsgg for Art. 1. Part III now cites all of these. It also flagged QUESTION-468 for "what separates exploitation from dependence and domination". Art. 9 cites QUESTION-468, so that is fine.
- **Part II review, Part C, Art. 6 contacts** (CLAIM-tmpdq0ah, CLAIM-595, CLAIM-462, CLAIM-tmpefeb7). CLAIM-tmpdq0ah is now cited in Art. 7. CLAIM-595 and CLAIM-462, recommended there for Art. 6, bear more directly on Art. 7 §7.2 and Art. 8 §8.4.2, and Part III cites neither. CLAIM-tmpefeb7 (monitoring manufactures conformity; complements CLAIM-402) bears on §7.6's restoration marker. Optional.
- **Write-manuscript skill step 3a** ("Do it again after drafting ... each [gap] is checked the same way before it is filed as a LEAD or a QUESTION"). LEAD-tmphsmng and QUESTION-tmpeiurf were filed from G8.3 and G8.4. I found no held reading of associative obligation or fair play, so LEAD-tmphsmng is not redundant. QUESTION-tmpeiurf partly overlaps CLAIM-739's grounds and CLAIM-690's bearer clause, and the question says so in its relations (it refines QUESTION-460). No redundancy found.

---

## Counts

| Region | Uncited codes listed (by script over this file) | Of which "must correct" or "must update" |
|---|---|---|
| 1. Article 7 | 72 | 4 (CLAIM-132 standing; LIT-tmpflbme; LEAD-tmp5msck; LEAD-tmplsxtr), plus J7.1 and J7.4 now noted |
| 2. Article 8 | 72 | 3 (LEAD-tmphsmng; QUESTION-tmpeiurf; the J8.1 to J8.3 notes), plus §8.4.2's "not linked" |
| 3. Article 9 | 77 | 6 (Hart readings; Hirschman and Pettit readings; CASE-343 and CLAIM-921; LEAD-022; CLAIM-tmp6nzs1; LEAD-tmpfzx2c and LEAD-tmp3w42f) |
| 4. Process history | 9 items | 1 (the 39a0a7dc pass over all three drafts) |

The counts include every code listed in the region's entries, with companions, so some codes recur across regions (CLAIM-705, SYNTHESIS-093, QUESTION-461, THEORY-457).

---

## The contacts that matter most, strongest first

1. **Commit 39a0a7dc filed the drafts' own gaps and joins, so the drafts are stale against the record.**
   - Filed: CLAIM-tmp6nzs1 (§9.4's claim, Proposed, demonstrated), LEAD-tmpfzx2c (G9.2), LEAD-tmp3w42f (G9.3), LEAD-tmphsmng (G8.3), QUESTION-tmpeiurf (G8.4), LEAD-tmp5msck (§7.4 "no field case"), LEAD-tmplsxtr (§7.8) and LIT-tmpflbme (Barthes, "not yet registered").
   - Notes: dated notes now state J7.1, J7.4, J8.1, J8.2, J8.3 and J9.1, untested under ADR-075.
   - **Must update** in all three articles.
2. **Art. 9 §9.6: the hidden-subsidy loop is half run, Active.**
   - CASE-343 (Active, executed): a budget that follows observed activity loses rarely used capabilities, and none when maintenance is funded apart. CLAIM-921, CLAIM-577 and CASE-412 (all Active) go with it, and CLAIM-700's premises CLAIM-679 and CLAIM-549 are Active and demonstrated.
   - LEAD-022 (Open) advances CLAIM-700.
   - "No run ... is held" and "Its only lead" are wrong. The right verdict is *done in part*: only the compensation that masks the shortfall is unrun. **Must correct.**
3. **Art. 9 Limits: the rival fields are read.** Hart (THEORY-1979), Grossman and Hart (THEORY-1985), Pettit's *On the People's Terms* (THEORY-1960), Hirschman's "Further Reflections" (THEORY-152) and Frey and Schneider on platform exit and voice (THEORY-1918). The first two are the readings by which ARG-210 was Rejected, and they go uncited in §9.3. THEORY-1918 bears on J9.5 (enshittification). **Must correct.**
4. **Art. 8 §8.8: the record's executed result on blame-like penalties goes unused, and the pilot's held objection is omitted.**
   - CLAIM-1064 (Active, demonstrated) and CASE-396 (Active): penalizing recognized violations makes an institution stop inquiring. LEAD-181 is Done on it.
   - CLAIM-1062 (Proposed, counter to CLAIM-750) objects to CASE-335's unit of measurement.
   - CLAIM-751 (Proposed) and QUESTION-476 (Open) hold upstream provenance without blame.
5. **Art. 8 §8.4.2 and J8.3: the timing link was held in substance.**
   - SYNTHESIS-098 integrates CLAIM-723 with CASE-285, CASE-316's parent design.
   - CLAIM-462 (Active) is illustrated by CASE-316 and corroborated by CLAIM-879.
   - CLAIM-705 and CLAIM-704 (Proposed, demonstrated) derive the share of challenges that can be resolved in time.
   - LEAD-216 adds the affected party.
   - SYNTHESIS-094 is §8.4.3's account, with QUESTION-441 its question.
6. **Art. 7 §7.2: Active premises and a standing error.**
   - CLAIM-329 and CLAIM-420 (Active) are premises of CLAIM-tmpgvsgg and CLAIM-tmpjitli. CLAIM-329 partly states J7.1 ("not by resemblance"). CLAIM-420 is the Active analogue of the owner's CLAIM-tmp590sw.
   - The character limit is quoted from SYNTHESIS-077 (Proposed) but is CLAIM-132's (Active, demonstrated). CLAIM-tmpqbaic (Active, demonstrated) is a second held limit on both U4 readings.
   - QUESTION-tmprvnp0, the article's own question, goes unnamed.
7. **Art. 7 §7.5: the held statement of "apparent confirmation by the evaluation regime" goes uncited.** CLAIM-416 (Active), with CLAIM-297 (Active), CLAIM-1202 (Active, demonstrated), THEORY-861 (Active, performative prediction), SYNTHESIS-108 (the genres account) and CASE-247 (the newsroom, both of J7.3's arms in one case).
8. **Art. 7 §7.4 and J7.2: nearer data and the held construction of "a second stable state".**
   - THEORY-267 (Active) is a randomized price-shock experiment in which 59% persists for 60 days. QUESTION-212 asks whether traders come to believe the price. This is nearer data than THEORY-2070.
   - CASE-111 (Active) grounds three of J7.2's components.
   - CLAIM-tmpggu4v, CLAIM-600 (Active) and CASE-191 (Active) give the withdrawal discriminator and its general condition.
   - CASE-297 and LEAD-003 hold the owner's Reddit case and its formation study.
9. **Art. 7 J7.4: the record holds a marker beyond restoration.** CASE-101 (Active) and CLAIM-926 (Proposed, demonstrated, CASE-347's claim) tell norm transmission to replacements from common response by a lagged block test. CLAIM-945 is CLAIM-946's companion from the same run. "The record does not yet state it" should be qualified.
10. **Art. 9 §9.1 and Limits: field readings and the engineering specimen.**
    - Field readings: THEORY-1492 and THEORY-1466 (Active) corroborate CLAIM-602, CLAIM-605 and CLAIM-600 or bound them. CLAIM-600 (Active) joins the models to field cases.
    - Mechanism: CLAIM-673 (Active) applies CLAIM-605 to the capacity to govern.
    - Engineering specimen: CASE-tmp3xxqg (the Chubby outage, illustrating CLAIM-603), CLAIM-tmpb1wyc and CASE-tmp3so1p (retention merging satisfaction with lock-in, illustrating CLAIM-670).
    - Integration: CLAIM-tmpv5sry, which passed ADR-075, is the held integration of §9.1 with §9.6.
    - Premise: CLAIM-428 is the uncited premise of CLAIM-690.
    - Question: QUESTION-461 (Open) is the article's own question, with 11 links into its codes.

Further contacts with a clear "Yes" that fall outside the top ten:

- CLAIM-208 against CLAIM-056 (§7.1);
- LEAD-187 (§7.1, §7.7);
- CASE-140 and SYNTHESIS-052 (§7.3);
- CLAIM-752 against CLAIM-729 (§8.2);
- THEORY-1823 (Kittay) and THEORY-1819 (§8.7);
- THEORY-457 (§8.9 and §9.3);
- THEORY-1917 (Keller, §9.6);
- CLAIM-601 (§9.5);
- CLAIM-652 and CASE-246, exit-driven drift (§9.7).
