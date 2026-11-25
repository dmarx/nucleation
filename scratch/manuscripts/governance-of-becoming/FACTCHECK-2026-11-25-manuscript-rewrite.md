<!-- scratch/manuscripts/governance-of-becoming/FACTCHECK-2026-11-25-manuscript-rewrite.md -->

# Fact-check of the rewrite of Articles 1 and 3–9 under ADR-tmpw306d (2026-11-25)

An independent check (write-manuscript skill, step 8) of the rewrite on branch
`claude/manuscript-governance-of-becoming-as-manuscript` (head 60e37792). The
checker did not write the text. It compared each article and its apparatus
with the previous version (`origin/staging`) and with the record's entries on
this branch. ADR-tmpw306d was read from `origin/claude/views-synthesize`. The
README and the overview are out of scope. Scripts were run with `python3 -I`
from the checker's scratchpad and are not kept. Nothing in the record was
changed.

## Counts by check

| Check | Scope | Result |
|---|---|---|
| 1. Nothing moved | All eight articles compared with the old versions section by section, using the apparatus numbering maps. Old quotations of six words or more were diffed against the new article plus its apparatus by script: 89 candidates, about 30 of them real quotations after removing mispaired quote marks. All but three survive in substance. The abstract, introduction, discussion and conclusion of each article were read against the old "what the article claims" sections. | **7 problems** (strengthening), 1.1–1.7 |
| 2. No new unsupported steps | The framing sections of all eight articles (introductions, objections, discussions, conclusions, notes on method) and the 8 rewriter flags | **8 problems**, 2.1–2.8. The other flagged items pass (see "Rewriter flags") |
| 3. Citations | Codes: 1,378 article–code pairs across the eight articles and their apparatus. Quotations: 1,634 of five words or more, checked by script. Author–year citations: 166 | Codes: 0 missing (ADR-tmpw306d exists on claude/views-synthesize). Quotations: 1,451 match an entry cited within three lines and 42 match elsewhere in the record. The remaining 141 were inspected: mispaired quote marks, the apparatus quoting old drafts, reviews or A51, and 4 in the articles, of which 3 are verbatim once links and blockquotes are normalized. Author–year: 15 year differences, each explained by the LIT entry's own note (preprint or reprint dates: Polski and Ostrom, Dohare, Lerman, Athreya, Hirschman). **3 problems**, 3.1–3.3 |
| 4. Apparatus | 757 table rows checked against front matter by script. "Made Active by" checked against history notes for 98 entries (45 table rows and 53 entries named in prose). Code sets diffed, old against new plus apparatus | Status mismatches 0, warrant mismatches 0. 5 rows omit a field. Who made each Active: 2 wrong. Code diff: 01, 03, 04, 06, 07 and 08 lose nothing; 05 loses 1 code (harmless); 09 loses 4. **4 problems**, 4.1–4.4 |
| 5. ADR-tmpw306d's form | Article bodies grepped for standing tags, voice names, turn numbers, "the record holds" and the jargon "held" | Standing tags, warrant tags, turn numbers, voice names and "the record holds": 0 each. "The record" appears 20 times, every use about method or the record as a case, which is appropriate. **1 problem** (record jargon "held"), 5.1 |

**Total: 23 problems.** 2.1, 2.2, 1.3 and 1.5 are the most consequential.

## Problems

### Check 1: something now stated more strongly

**1.1 — 01, line 289 (§1.13, reply to the strongest objection).**
- Text: "a theory of organizational identity that required boundaries to be discovered rather than declared would demand more than any account of constitution offers (CLAIM-530)".
- The record: CLAIM-530 is about mutual manipulability, the mechanist account, only. The old §1.6 said "The mechanist account of constitution reaches the same place", and so does the new §1.6 (line 97).
- Fix: "…would demand more than the mechanist account of constitution offers (CLAIM-530)".

**1.2 — 01, lines 15 and 297 (§1.1 and §1.14).**
- Text, line 15: "The difference matters because the two fail differently, respond differently to the withdrawal of support…". Text, line 297: "An arrangement that observes outputs, coordination or survival cannot tell whether the organization it governs keeps itself…".
- The record: both are model results stated as facts about organizations. The article's own scope (line 19, and §1.13 "It does not show that any real organization differs…") says otherwise.
- Fix: add "in the models below" at line 15. At line 297, write "On these results, an arrangement…" or "In the models, an arrangement…".

**1.3 — 03, line 7 (abstract) and line 309 (§3.14).**
- Text, line 7: "shows … that an obligation bars exit rather than raising its price".
- Text, line 309: §3.14 states the contract claims in the indicative, for example "Processes can come to stand in relations that function as contracts…", "Contracts give processes an operational standing…", "an obligation bars exit rather than raising its price".
- The record: CLAIM-tmpdu9v6 is Proposed and interpretive, and it is argued, not shown. The old §3.13 tagged each of these items Proposed, and said "No item about contracts is Active". The new §3.13 says "Every claim about contracts is a conjecture", but the conclusion drops that.
- Fix: in the abstract, "argues … that an obligation bars exit". Open §3.14 with one sentence saying that what follows about contracts is the account proposed, on the demonstrated cost geometry.

**1.4 — 07, line 71 (§7.4) and line 7 (abstract).**
- Text, line 71: "This is the precise form of the self-governing rule of CLAIM-425".
- Text, line 7: "this is the formal content of the phrase".
- The record: the old draft said it was "the precise form of CLAIM-425's 'both let the judgements set the terms of response'". That is the failure of absorbing and of resisting, not the rule. CLAIM-tmpj4pw3 itself says "Not that a small reversing part is self-governance". The phrase also covers three routes, which the result does not decide (line 73).
- Fix: "This is the precise form of CLAIM-425's point that absorbing and resisting 'both let the judgements set the terms of response'". In the abstract, "this makes exact one part of the phrase…".

**1.5 — 09, line 7 (abstract), line 153 (§9.11) and line 165 (§9.12).**
- Text, line 7: "What it establishes is the mechanism by which an exploitative or dominating relation can be built while ordinary performance looks fine."
- Text, line 153: "The argument shows … what would make it presumptively dominating."
- Text, line 165: §9.12 opens with model results in the indicative ("Supply that does the work erodes the capacity it replaces…").
- The record: the mechanism is demonstrated in models with invented parameters (the new §9.11, "Models, mostly"). The presumption test, CLAIM-682, is Proposed and interpretive. The political economy rests on the Proposed CLAIM-690 and CLAIM-670, which the new §9.11 itself says.
- Fix: "What it establishes, in models, is a mechanism…"; "…and proposes what would make it presumptively dominating". Put "In the models of §§9.2–9.5" at the head of the conclusion.

**1.6 — 06, line 174 (§6.11).**
- Text: "…because a demonstrated objection stands against it: the anchor that makes correction possible fixes its own error in place."
- The record: CLAIM-1185 was narrowed to its model at the owner's word of 2026-11-24. The general form, "an anchor a system can neither rewrite nor reject imports its own errors whole", is CLAIM-tmpjdml5, which is Proposed. §6.7 keeps that distinction. The conclusion drops it.
- Fix: "…in the sensor model the anchor that makes correction possible fixes its own error in place, and the general form is proposed".

**1.7 — 08, lines 176 and 194–196 (§8.10 and §8.11).**
- Text: §8.10's "frame" includes CLAIM-741 ("A choice-protecting right is not represented by an evaluation of endpoints…"), and line 196 says "the frame is firm". §8.11 states "Repair does not wait on culpability" and "Morality evaluates the terms of cooperation and is not confined to cooperators" in the indicative.
- The record: CLAIM-741 is Proposed, though demonstrated. CLAIM-742, CLAIM-714 and CLAIM-tmpreipd are Proposed and interpretive. The old §8.11 tagged each.
- Fix: say in §8.10 that CLAIM-741 is a construction not yet adopted. In §8.11, write "On the proposals of §§8.8–8.9, repair does not wait…, and morality evaluates…".

### Check 2: new steps no cited entry holds

**2.1 — 06, line 118 (§6.7). Flagged by the rewriter.**
- Text: "The least it must concede is that protection is a condition of correction only together with the anchor's correctness, which nothing inside the protected system can check."
- The record: the concession on CLAIM-1024 "is now due (ADR-059) and is the owner's to write" (CLAIM-1024, note of 2026-11-24). No entry states this minimum. "Nothing inside … can check" generalizes CLAIM-1125, which is about one sensor network.
- Fix: cut the sentence, or mark it: "On this article's reading, which is not the owner's concession, the least it would concede is…, in the sensor model (CLAIM-1125)".

**2.2 — 06, line 140 (§6.9) and line 182 (note on method). Flagged by the rewriter.**
- Text, line 140: "That is the formal echo of section 6.2: a coarse description that merges what a claim distinguishes leaves no trace in the contrasts it supports."
- The record: no entry links CLAIM-tmpqbaic's merged states to CLAIM-350's fibres. The note on method at line 182 says "It asserts no step that no cited entry states". This sentence contradicts that note.
- Fix: cut it. Or mark it as the article's remark, a link not on the record, and soften the note on method.

**2.3 — 06, line 168 (§6.10, the strongest objection).**
- Text: "In each case the remedy works because the protected element is right." Also: "…the argument has relocated the problem rather than solved it".
- The record: no entry states this of CASE-396, CASE-346 or CLAIM-1007. The general form is CLAIM-tmpjdml5 (Proposed), which this paragraph does not cite.
- Fix: cite CLAIM-tmpjdml5 for the generalization, and put the claim in the objector's mouth ("The objection holds that in each case…").

**2.4 — 08, line 149 (§8.8).**
- Text: "There is also a reason, from a model, to think that the blameless rationale tracks something real."
- The record: the same paragraph ends "whether blaming practices behave so is not shown". The apparatus's J8.6 says the searcher called CLAIM-1064 "the mechanism behind the blameless rationale" and "the article does not go that far". This opening sentence goes that far.
- Fix: "A model bears on the blameless rationale, though not on blame:" or similar.

**2.5 — 08, line 164 (§8.9).**
- Text: "Consideration owed to those who cannot cooperate has at least one read case."
- The record: THEORY-1569 (Gardiner 2006) concerns "why policy is hard to make, not what a just policy is" (apparatus J8.7). The conditional that follows is a gloss. The lead sentence asserts the case.
- Fix: "One read case bears on consideration owed to those who cannot cooperate", and keep the conditional.

**2.6 — 09, line 161 (§9.11, reply to the strongest objection).**
- Text: "An obligation that controls exit 'without raising its price' (CLAIM-tmpdu9v6) is not a feature of any outside option, and bargaining power does not capture it."
- The record: CLAIM-tmpdu9v6 is Proposed. No entry compares it with bargaining theory. The rewriter flagged this objection as framing.
- Fix: "On CLAIM-tmpdu9v6, which is proposed, such an obligation is not…". Say that the comparison with bargaining theory is the article's own.

**2.7 — 05, line 301 (§5.13.2).**
- Text: "That is a structural fact about the arrangement, not a quantity." Also: "Third, a condition that bars a transition is not a price."
- The record: the circle result holds in a model checked only by its author (§5.13.1). The bar is CLAIM-tmpdu9v6, which is Proposed and interpretive. The reply states both flatly, though it concedes the open join at the end.
- Fix: "In its model, that is a structural fact…"; "Third, on the proposal of §5.9.2, a condition that bars…".

**2.8 — 09, line 149 (§9.10).**
- Text: "…the demand that the mechanisms be connected to 'the resource-bounded accessibility of institutional transformation'".
- The record: the quotation is from the motivating draft A51 and is not attributed in the article. A reader outside the record cannot tell whose demand it is. The step that follows is correctly marked as a reading (J9.11).
- Fix: "the publication plan's demand (A51)…", or drop the quotation marks.

### Check 3: citations

**3.1 — 08, line 135 (§8.7), and apparatus/08, line 306.**
- Text: the article cites "(Hart 1955; Rawls 1964; LEAD-tmphsmng)", and the apparatus says "Simmons (1979) … Hart (1955) and Rawls (1964) likewise. None is registered."
- The record: Hart 1955 is LIT-tmpfhd8f and Rawls 1964 is LIT-tmp4lk5u, both Deferred, filed in 88fcc08a1 ("File the audit's record items…") on 2026-11-25. Simmons 1979 is not registered.
- Fix: cite "(Hart 1955; LIT-tmpfhd8f; Rawls 1964; LIT-tmp4lk5u)". In the apparatus, "Hart and Rawls are registered (Deferred); Simmons is not".

**3.2 — 01, line 97 (§1.6).**
- Text: "(Craver 2007; Craver, Glennan and Povich 2021)" with no entry code.
- The record: these are LIT-1930 (Unavailable) and LIT-1931 (Unfetched). Every other external citation in the series carries its entry.
- Fix: add LIT-1930 and LIT-1931. CLAIM-530 already follows.

**3.3 — 09, line 31 (§9.2).**
- Text: "the thesis by which it reads Moore is not held (CLAIM-603, note of 2026-11-06)".
- The record: the old draft named the thesis's code, THEORY-1459 (Proposed). It now appears nowhere in the article or its apparatus.
- Fix: add "(THEORY-1459)".

### Check 4: apparatus

**4.1 — apparatus/05, lines 45, 78 and 143.**
- Text: CLAIM-403 and CLAIM-675 are given as made Active at the "delegated review (2026-11-06)".
- The record: CLAIM-403 was "Promoted by the fifteenth status review", 2026-10-29 (history v5). CLAIM-675 was "Promoted at the status review's ruling", 2026-11-18 (history v4). Both were delegated. The error is inherited from the old draft (its line 28). The other 96 histories checked agree with the apparatus.
- Fix: correct the dates in the table and in line 143's list.

**4.2 — apparatus/05, lines 30, 115, 121, 64 and 91.**
- Text: CLAIM-755, CLAIM-1004 and CLAIM-1034 are given without their warrant, and THEORY-247 and THEORY-1483 without a status.
- The record: CLAIM-755 is demonstrated, CLAIM-1004 interpretive and CLAIM-1034 interpretive. THEORY-247 is Active and THEORY-1483 Proposed.
- Fix: fill in the five fields.

**4.3 — 09, §9.8 (lines 133–139), and apparatus/09.**
- Text: the old draft said TERM-124 "carries a note, 'Not adopted: one use departs from the definition', because CLAIM-730 makes a rule the holder". This is in neither the new article nor its apparatus, and CLAIM-730 is no longer cited.
- The record: §9.8 turns on TERM-124's requirement that a holder be an agent or role. That the record has a use making a rule the holder bears directly on it.
- Fix: restore the note, in §9.8 or the apparatus.

**4.4 — apparatus/09 (minor losses).**
- Text: the old draft cited CLAIM-726 in SYNTHESIS-095's list ("none corroborates CLAIM-726, CLAIM-702 or CLAIM-700"). It listed CLAIM-tmpro73c as a member of the work, and the apparatus now lists only non-members. It also said that A22 §11's "Hidden regulatory subsidy" is "A restatement by the same kind of source, not independent evidence" (CLAIM-700, note of 2026-11-24). None of the three is now in the article or its apparatus.
- The record: the losses are harmless to the argument, but against the apparatus's statement that nothing the previous draft held true was dropped (apparatus/09, §§1–6), they are omissions.
- Fix: one line each in the apparatus.

Also checked under this heading, with no problem: 05 loses SYNTHESIS-116, which the old draft named only inside SYNTHESIS-118's quoted statement. The new §5.5 replaces the old "narrower reading" with the failed join J5.1, which the review supports (REVIEW-2026-11-25, line 355, and TERM-131's note), so nothing moved.

### Check 5: ADR-tmpw306d's form

**5.1 — 05, 07, 08 and 09 (lines include 05:53 and 283; 07:41, 57, 75, 99 and 129; 08:99; 09:67).**
- Text: record jargon "held" survives in the argument: "Several held results", "Two held readings", "there is a held proposal", "a held reading", "are held already", "is held for matched constructions".
- The record: these are the record's "on the record", a bookkeeping word that a reader outside the record cannot parse. In places it carries a standing ("held" read as established).
- Fix: say what the entry is ("a derived result", "a proposal", "two readings") or drop the word. This does not apply to "held fixed" or "held back".

## Rewriter flags, each checked

- **06, §6.7 "least it must concede" and §6.9 "formal echo".** Both are problems: 2.1 and 2.2.
- **05, §5.13.2 objection.** Framing that asserts little. The concessions are marked. Two firmness slips: 2.7.
- **01, section order and §1.13 boundary-relativity.** The order changed with no loss (the apparatus maps every old section). §1.13 has one overreach: 1.1.
- **04, renumbering, ARG-215 and "relabels rules-in-use".** The map in apparatus §11 is complete, and the README's old numbers are out of scope here. ARG-215 is Rejected, and "the argument that read it as one fails" is correct. The objection's reply is scoped to "the organization modelled" and to CLAIM-890, and CLAIM-021's summary does give "a common explanatory role across realizers". Pass.
- **09, J9.8–J9.11 and the bargaining-power objection.** J9.8, J9.9 and J9.11 are marked as open or as readings in the text. J9.10 is marked "the article's suggestion and is not tested". The objection's reply asserts one step: 2.6.
- **03, §3.13 open possibility.** Marked "which no claim yet states and which has not been tested". Pass. The abstract and the conclusion are another matter: 1.3.
- **08, J8.6, J8.7 and SYNTHESIS-038.** J8.6 is undercut by the paragraph's own opening sentence (2.4). J8.7's conditional is acceptable, but its lead sentence is not (2.5). The article does not claim that SYNTHESIS-038 integrates CLAIM-741 (it integrates it 0 times in front matter), and the apparatus says so. Pass.
- **07, J7.5, CASE-111, the dropped A22 §3 quotation and threshold contagion.** J7.5 is stated as open (line 57). CASE-111 is cited for CLAIM-463's fold only. No quotation of A22 §3 remains. The threshold-contagion objection is supported by CLAIM-tmpgvsgg and LEAD-tmpiktom, quoted verbatim. Pass. The separate overstatement is 1.4.
