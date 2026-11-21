<!-- scratch/manuscripts/from-obstruction-to-reorganization/README.md -->

# From Obstruction to Reorganization: working draft

A general theory of learning and inquiry, intended to apply to arbitrary systems (Part I). It is shown operationalized in the research record in which it was developed (Part II). The self-reinforcing cycle that record's machinery produced is traced and set against the theory's implications (Part III). The draft succeeds the owner's manuscript "luria: nucleating an argument" (proposed 2026-10-11; root question QUESTION-037). At the owner's ruling of 2026-11-21 the two are one work, whose `works` term is renamed `from-obstruction-to-reorganization` after this directory (ADR-tmpwgvwk, pull request 589).

**Provenance.**

1. Written out from the ChatGPT exchange "Branch · Audit Luria Evolution" (2026-11-20) and its measurements.
2. Extended with the predecessor's argument and a mapping of luria onto it.
3. Revised on [REVIEW-2026-11-20.md](REVIEW-2026-11-20.md), adding a census of every decision, a term-change audit, and threats to validity.
4. Restructured at the owner's direction, 2026-11-20, into three parts. Part I now develops the record's theory of learning and inquiry in full, from cited digests of five regions of the record (`background/`). Material was added, not trimmed.

**Refresh of 2026-11-21.** Brought up to date with the night's filings at the owner's request: First Contact in §3.2, engineering as inquiry in §4.1, predicates as constraints and stabilization in §4.2, when an anchor is set in §5.3, and a turn of the cycle in one night as §16.4. The census (§§13–15) still counts the 114 decisions to 2026-11-20; about twenty more were filed on 2026-11-21 and 34 moved to Active, so its figures hold as of 2026-11-20 until the scripts are rerun. A candidate title, the owner's: "(AI) Assisted Inquiry" (AIAI).

**Status.** A working document under version control. It is not part of the record: luria does not read `scratch/`, and codes are cited bare. The ten principles (§7.1), the predicted cycle (§7.2), the mappings (§9) and the census are this draft's own integrations, not entries the record holds. Each step of Part I cites the entries it rests on, with their standing.

**Brought up to date with the record of 2026-11-21.** The formal account of drift (CLAIM-772 with ARG-124, CLAIM-776, CLAIM-777, CLAIM-782, CLAIM-768) is in §§5.3, 5.4, 15.3 and 19.6. The budget tree (CLAIM-770) is in §2.3, and QUESTION-tmp6iu8e in §17.1. §5.3 now states the narrower form of the anchoring link the audit had struck.

**Anchoring, generalized (2026-11-21).** §5.3 now opens with the general account of anchoring in an inquiry (CLAIM-tmp1xigl): one mechanism, a reconstruction pulled toward a fixed reference, which secures what the reference is tied to. Tied to the target, it secures content; tied to the inquiry's earlier states, continuity; tied to nothing, it is bias. It adds the two objections to CLAIM-772 (CLAIM-tmppkqzl, the reader's offset; CLAIM-tmp0kqq4, stale exact copies). P9 (§7.1), stage 1 of the cycle (§7.2), §7.4, the P9 row of §9, §14.5, §19.6 (two new measurements), §20 and the abstract follow.

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
| [07-governance.md](07-governance.md) | §14 Four loops: decisions, reviews, RETRO and POSTMORTEM, the tool |
| [08-results.md](08-results.md) | §15 Results against E1–E7 |
| [09-flywheel.md](09-flywheel.md) | §16 The flywheel stage by stage, the cycle acting on the theory itself, and what echoes each principle |
| [10-discussion.md](10-discussion.md) | §17 Delegation, distinction-drawing, maintained capacity, signatures |
| [11-threats-evaluation-conclusion.md](11-threats-evaluation-conclusion.md) | §18 Threats to validity; §19 Future evaluation; §20 Conclusion |
| [12-appendices.md](12-appendices.md) | Figures, source map, references |
| `background/` | Five cited digests of the record's theory, the raw material for Part I |

## Analysis

| File | What it does |
|---|---|
| `analysis/census/CODEBOOK.md` | The census codebook, fixed before coding |
| `analysis/census/batch-1.json` … `batch-4.json` | The 114 coded decisions |
| `analysis/census/recode.json` | The second coder's 30 |
| `analysis/census.py` | Tables and agreement. Run: `cd analysis && python3 -I census.py census` |
| `analysis/census_report.md` | Its output |
| `analysis/term_changes.py` | Every reworded or removed vocabulary term, with carrying entries touched. Needs full git history. Run from the repository root: `python3 -I scratch/manuscripts/from-obstruction-to-reorganization/analysis/term_changes.py . 09950cdf` |
| `analysis/term_changes.json` | Its output |
| `analysis/test_*.py` | Tests: `cd analysis && python3 -m pytest -q` |

## Open items for the owner

The owner ruled on the earlier list on 2026-11-21 (promotion pull request 582). What follows is what remains, with what was done about the rest.

1. **The principles in the record.** Filed (pull request 557). Cross-line accounts are now permitted, with an audit for missing lines (ADR-tmpg1n72, pull request 593). Its first audit finds the eight principle accounts together indicate a candidate line, `learning-and-inquiry`. Open: whether to add it.
2. **ADR-075's language.** Three alternatives are proposed (pull request 594). Open: which, if any.
3. **ADR-048's flag.** Closed: the flag did not change meaning, and revisiting it is the anthology's process (pull request 587). §§1, 15.2, 16 and 20 are corrected.
4. **RETRO-004's summary.** Corrected in the record (pull request 588).
5. **The work.** Same work, renamed (pull request 589).
6. **A human coder.** Filed as a lead (pull request 591). Open: who codes.
7. **Unread sources.** All six have LITs, which suffices for now at the owner's ruling. They remain unread.
8. **Missing references:** the luria repository, Nygard, Tyree & Akerman, the qualitative-codebook literature, PRISM, PROV, and work on LLM agents with memory.
9. **Adoption** of the Proposed entries filed from this draft is left to the next promotion audit.
10. **Figures recomputed on demand.** An analytics pipeline in Apache Hamilton is being built, at the owner's suggestion, so the census and growth figures can be recomputed and dated.
11. **Length** and **authorship and disclosure** of AI assistance (§18), as before.
