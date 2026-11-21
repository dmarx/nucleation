<!-- scratch/manuscripts/from-obstruction-to-reorganization/README.md -->

# From Obstruction to Reorganization: working draft

A general theory of learning and inquiry, intended to apply to arbitrary systems (Part I). It is shown operationalized in the research record in which it was developed (Part II). The self-reinforcing cycle that record's machinery produced is traced and set against the theory's implications (Part III). The draft succeeds the owner's manuscript "luria: nucleating an argument" (the work `luria-nucleating-an-argument`, proposed 2026-10-11; root question QUESTION-037).

**Provenance.**

1. Written out from the ChatGPT exchange "Branch · Audit Luria Evolution" (2026-11-20) and its measurements.
2. Extended with the predecessor's argument and a mapping of luria onto it.
3. Revised on [REVIEW-2026-11-20.md](REVIEW-2026-11-20.md), adding a census of every decision, a term-change audit, and threats to validity.
4. Restructured at the owner's direction, 2026-11-20, into three parts. Part I now develops the record's theory of learning and inquiry in full, from cited digests of five regions of the record (`background/`). Material was added, not trimmed.

**Refresh of 2026-11-21.** Brought up to date with the night's filings at the owner's request: First Contact in §3.2, engineering as inquiry in §4.1, predicates as constraints and stabilization in §4.2, when an anchor is set in §5.3, and a turn of the cycle in one night as §16.4. The census (§§13–15) still counts the 114 decisions to 2026-11-20; about twenty more were filed on 2026-11-21 and 34 moved to Active, so its figures hold as of 2026-11-20 until the scripts are rerun. A candidate title, the owner's: "(AI) Assisted Inquiry" (AIAI).

**Status.** A working document under version control. It is not part of the record: luria does not read `scratch/`, and codes are cited bare. The ten principles (§7.1), the predicted cycle (§7.2), the mappings (§9) and the census are this draft's own integrations, not entries the record holds. Each step of Part I cites the entries it rests on, with their standing.

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
| [07-governance.md](07-governance.md) | §14 Four loops: decisions, reviews, POSTMORTEM, the tool |
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

1. **The principles in the record.** Filed on dmarx/nucleation#557, now retargeted to staging and refreshed. The census is a CASE and two claims. P1 and P3 are already stated. P2 and P4–P10 are SYNTHESIS accounts. One narrowed part of the cycle is a claim. Section 7.4 reports the audit. Open: whether thematic, cross-line accounts are a kind the record wants (ADR-083).
2. **ADR-048's flag.** The 237 entries carrying `anthology-candidate` were never revisited when its meaning changed (§15.2). That is a finding, and also a repair the record may want.
3. **POSTMORTEM-002's summary** (§14.5). Cite it as of a dated commit, or correct it in the record.
4. **The work.** Keep `luria-nucleating-an-argument` with its blurb revised, or give this paper a new `works` term?
5. **A human coder.** All census coders were instances of one model (§18). A human second coder on the 30-decision sample would address the largest reliability threat.
6. **Unread sources.** Dewey, Collingwood, Rheinberger, Bowker & Star, Stojanovic and Allspaw are cited but unread on the record (§11). They should be read, or supplied, before submission.
7. **Missing references:** the luria repository, Nygard, Tyree & Akerman, the qualitative-codebook literature, PRISM, PROV, and work on LLM agents with memory.
8. **Length.** Material has been added rather than trimmed, at the owner's direction; trimming is left to the owner.
9. **Authorship and disclosure** of AI assistance (§18).
