<!-- scratch/manuscripts/from-obstruction-to-reorganization/README.md -->

# From Obstruction to Reorganization: working draft

A general theory of learning and inquiry, intended to apply to arbitrary systems (Part I). It is shown operationalized in the research record in which it was developed (Part II). The self-reinforcing cycle that record's machinery produced is traced and set against the theory's implications (Part III). The draft succeeds the owner's manuscript "luria: nucleating an argument" (proposed 2026-10-11; root question QUESTION-037). At the owner's ruling of 2026-11-21 the two are one work, whose `works` term is renamed `from-obstruction-to-reorganization` after this directory (ADR-135, Active; pull request 589).

**Provenance.**

1. Written out from the ChatGPT exchange "Branch · Audit Luria Evolution" (2026-11-20) and its measurements.
2. Extended with the predecessor's argument and a mapping of luria onto it.
3. Revised on [REVIEW-2026-11-20.md](REVIEW-2026-11-20.md), adding a census of every decision, a term-change audit, and threats to validity.
4. Restructured at the owner's direction, 2026-11-20, into three parts. Part I now develops the record's theory of learning and inquiry in full, from cited digests of five regions of the record (`background/`). Material was added, not trimmed.

**Refresh of 2026-11-21.** Brought up to date with the night's filings at the owner's request: First Contact in §3.2, engineering as inquiry in §4.1, predicates as constraints and stabilization in §4.2, when an anchor is set in §5.3, and a turn of the cycle in one night as §16.4. A candidate title, the owner's in conversation, not on the record: "(AI) Assisted Inquiry" (AIAI).

**Status.** A working document under version control. It is not part of the record: luria does not read `scratch/`, and codes are cited bare. The ten principles (§7.1), the predicted cycle (§7.2), the mappings (§9) and the census are this draft's own integrations, not entries the record holds. Each step of Part I cites the entries it rests on, with their standing.

**Brought up to date with the record of 2026-11-21.** The formal account of drift (CLAIM-772 with ARG-124, CLAIM-776, CLAIM-777, CLAIM-782, CLAIM-768) is in §§5.3, 5.4, 15.3 and 19.6. The budget tree (CLAIM-770) is in §2.3, and QUESTION-504 in §17.1. §5.3 now states the narrower form of the anchoring link the audit had struck.

**Anchoring, generalized (2026-11-21).** §5.3 now opens with the general account of anchoring in an inquiry (CLAIM-790): one mechanism, a reconstruction pulled toward a fixed reference, which secures what the reference is tied to. Tied to the target, it secures content; tied to the inquiry's earlier states, continuity; tied to nothing, it is bias. It adds the two objections to CLAIM-772 (CLAIM-793, the reader's offset; CLAIM-789, stale exact copies). P9 (§7.1), stage 1 of the cycle (§7.2), §7.4, the P9 row of §9, §14.5, §19.6 (two new measurements), §20 and the abstract follow.

**Refresh of 2026-11-21, evening (Parts II and III).** Brought up to date with the day's progress since `dd6f4e7db`, at the owner's request, in the owner's words in conversation, not on the record ("the manuscript and its neighborhood might merit some updates too to account for the latest progress"):

- **The census rerun.** The 22 decisions filed on 21 November (ADR-115 to ADR-135, and ADR-tmpcb96w, still temporary) are coded as a fifth batch, by one coder, not recoded (`analysis/census/batch-5.json`). `census.py` gains a fourth period, a table over all decisions, and a check of coded statuses against the record. With the batch: 136 decisions, 91 grammar changes (63 refine, 27 revise, 1 restraint), 61 migrations stating 2,701 entries; 7 of the 22 are Rejected alternatives; the owner decided all 22. Figures for the first 114, and the agreement table, are unchanged.
- **Figures recomputed and dated.** The analytics pipeline was run at `main` `56479304e` (18:20 UTC, after the evening's promotion), pointed at this directory's census. Its outputs are kept as `analysis/analytics-2026-11-21.json` and `analysis/analytics-terms-2026-11-21.json`. Recomputed: the 21 November column of §12.5 (the four earlier columns reproduced exactly), the entry and decision counts of §§8.2 and 14.1, the commit count of §12.1, the census's coverage (0 uncoded) and status drift (34), and the term-change audit to that commit (36 events). Figures not recomputed keep their dates in the text.
- **Integrated, by section.** §8.2 RETRO, staging and the new line; §9.2–9.3 each principle's newer mechanisms; §9.5 and §10 the cross-line audit and a mechanism adopted for this theory; §12 the fifth observation point and batch; §13.1 the fifth batch; §13.8 alternatives filed and not taken; §13.9 errors in first use; §14.1–14.6 statuses, the synthesis review and first cross-line audit, the review loop in use (RETRO-006, RETRO-007), the luria 1.11 pin and the decoder; §14.7 the owner's review point; §15 each expectation against the batch, and the first narrowing in place since the census (ADR-130) as a case for E3's exception; §16.5 lapses the owner caught becoming rules; §17.1 what 21 November delegated; §17.6 RETRO-006 on the drafts; §18 four new threats; §19.8 checks the record can run now; §20; Appendices A–C. Stale temporary codes are replaced by their permanent ones throughout Parts II and III.

The tables, stage labels and readings in §§13.8, 14.7, 15.2 and 16.5 are this draft's integrations, not entries the record holds.

## Files, in reading order

| File | Sections |
|---|---|
| [00-abstract-introduction.md](00-abstract-introduction.md) | Title, abstract, §1 (three claims, questions, contributions, terms, roadmap) |
| **Part I** | **A theory of learning and inquiry** |
| [01-theory-distinctions-and-learning.md](01-theory-distinctions-and-learning.md) | §2 Systems that draw distinctions; §3 Learning as the formation of maintained capacity |
| [02-theory-inquiry-memory-collectives.md](02-theory-inquiry-memory-collectives.md) | §4 Inquiry as specification; §5 Memory, transmission and identity; §6 Collective inquiry |
| [03-theory-implications.md](03-theory-implications.md) | §7 Ten principles, the predicted cycle, and expectations E1–E7 |
| **Part II** | **The theory inside its own investigative machinery** |
| [04-operationalization.md](04-operationalization.md) | §8 Luria and Nucleation; §9 How the record operationalizes each principle; §10 What that does and does not establish |
| [05-related-work-and-method.md](05-related-work-and-method.md) | §11 Related work (including Ashby, Simon, Kuhn); §12 Method, growth and rates |
| **Part III** | **The flywheel** |
| [06-census-and-cases.md](06-census-and-cases.md) | §13 The census and eight cases; grammar changes that went wrong |
| [07-governance.md](07-governance.md) | §14 Four loops: decisions, reviews, RETRO and POSTMORTEM, the tool; the owner's review point |
| [08-results.md](08-results.md) | §15 Results against E1–E7 |
| [09-flywheel.md](09-flywheel.md) | §16 The flywheel stage by stage, the cycle acting on the theory itself, what echoes each principle, a night's turn, and lapses the owner caught becoming rules |
| [10-discussion.md](10-discussion.md) | §17 Delegation, distinction-drawing, maintained capacity, signatures |
| [11-threats-evaluation-conclusion.md](11-threats-evaluation-conclusion.md) | §18 Threats to validity; §19 Future evaluation; §20 Conclusion |
| [12-appendices.md](12-appendices.md) | Figures, source map, references |
| `background/` | Five cited digests of the record's theory, the raw material for Part I |

## Analysis

| File | What it does |
|---|---|
| `analysis/census/CODEBOOK.md` | The census codebook, fixed before coding |
| `analysis/census/batch-1.json` … `batch-4.json` | The 114 coded decisions |
| `analysis/census/batch-5.json` | The 22 decisions of 21 November, single coder, not recoded |
| `analysis/census/recode.json` | The second coder's 30 |
| `analysis/census.py` | Tables and agreement, a fourth period (21 Nov), all decisions by period, and coded statuses checked against the record. Run: `cd analysis && python3 -I census.py census` |
| `analysis/census_report.md` | Its output |
| `analysis/term_changes.py` | Every reworded or removed vocabulary term, with carrying entries touched. Needs full git history. Run from the repository root: `python3 -I scratch/manuscripts/from-obstruction-to-reorganization/analysis/term_changes.py . 09950cdf` |
| `analysis/term_changes.json` | Its output |
| `analysis/analytics-2026-11-21.json`, `analysis/analytics-terms-2026-11-21.json` | Runs of the analytics pipeline (`scratch/formal/analytics/`) at `main` `56479304e`, with `--census_dir` pointed here; the second is the term-change audit to that commit |
| `analysis/test_*.py` | Tests: `cd analysis && python3 -m pytest -q` |

## Open items for the owner

The owner ruled on the earlier list on 2026-11-21 (promotion pull requests 582 and 599). What follows is what remains, with what was done about the rest. Codes made permanent at the promotions are given as they now stand.

**Closed since the last list.**

1. **The principles in the record.** Filed (pull request 557). Cross-line accounts are permitted, with an audit for missing lines (ADR-129, formerly ADR-tmpg1n72, Active). Its first audit found that the eight principle accounts together indicate a candidate line, and the owner added it: `learning-and-inquiry` (ADR-130, Active; pull request 605). Its line account is SYNTHESIS-118 (Proposed), filed at the synthesis review of 2026-11-21.
2. **ADR-075's language.** The owner chose alternative A, "sure, go with A": the test routes and does not reject (ADR-131, Active). B and C are Rejected and kept (ADR-134, ADR-133).
3. **ADR-048's flag.** Closed: the flag did not change meaning (pull request 587).
4. **RETRO-004's summary.** Corrected (pull request 588).
5. **The work.** Same work, renamed (ADR-135, Active).
6. **Figures recomputed on demand.** The analytics pipeline exists (`scratch/formal/analytics/`, pull request 598) and was run for this refresh. Whether it runs in CI, and on which branch, is item 12.

**Still open.**

7. **A human coder.** Filed as LEAD-206 (Open). Who codes is open. The fifth batch now needs a second coder too, and has a weaker claim to one than the first 114: its coder took part in the work it codes.
8. **Unread sources.** All six have LITs, which suffices for now at the owner's ruling. They remain unread.
9. **Missing references:** the luria repository, Nygard, Tyree & Akerman, the qualitative-codebook literature, PRISM, PROV, and work on LLM agents with memory.
10. **Adoption** of the Proposed entries filed from this draft is left to the next adoption review (ADR-124, itself Proposed).
11. **Length** and **authorship and disclosure** of AI assistance (§18), as before.

**New.**

12. **Where the census lives.** Two copies have diverged: `scratch/formal/decision-census/` (the pipeline's default, with `load_rows` and `summary`, 114 decisions, three periods) and this directory's `analysis/` (136 decisions, four periods, the status check). Options: (a) point the pipeline's default at this directory; (b) copy batch 5 and the period change into the formal copy and keep both; (c) make the formal copy the only one and have the manuscript cite it. The lean is (a), which keeps the census with the paper that reads it; (c) suits the census as the record's executed study (CASE-300). Whether the pipeline then runs in CI is the workflow question its README leaves to the owner.
13. **The fifth batch's borderline codes.** ADR-129 (cross-line accounts) is coded not a grammar change, as ADR-075's and ADR-078's audits were, though ADR-083, whose scope rule it widens, was coded one; ADR-135's pure rename is coded refine, which neither regime fits well. Either reading changes the counts by one.
14. **E3's test case.** ADR-130 narrowed `record-as-apparatus` in place and touched 7 of its 80 carriers, deferring the rest to the synthesis review (§15.2). Run the check of §19.8 now, or leave it to the next synthesis review as the decision says?
15. **The term audit's unit under staging.** Since staging, the audit takes the promotion pull request as a decision's unit of work (599 for both new events), which is wider than the decision's own pull request. Teach it to use the pull request into staging, or note the change and leave it?
