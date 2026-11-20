<!-- scratch/manuscripts/from-obstruction-to-reorganization/README.md -->

# From Obstruction to Reorganization: working draft

The successor to the owner's manuscript "luria: nucleating an argument" (the work `luria-nucleating-an-argument`, proposed 2026-10-11; root question QUESTION-037). It carries the predecessor's account of drift and anchoring, the account of what a record of inquiry can secure, and the account of inquiry as specification. These are used as an interpretive framework. It then studies how the record changed its own grammar over its first eight weeks, through a census of all 114 of its decisions.

**Provenance.** The draft went through three versions.

1. Written out from the ChatGPT exchange "Branch · Audit Luria Evolution" (2026-11-20) and its measurements.
2. Extended at the owner's direction with the argument and the mapping (§§2–3).
3. Revised on the plan in [REVIEW-2026-11-20.md](REVIEW-2026-11-20.md). This version added:
   - a census of every decision, coded against a fixed codebook, with a second coder;
   - an audit of every change to a vocabulary term;
   - attribution corrected: assistants and procedures noticed most grammar changes;
   - refinement kept apart from revision;
   - stated falsifiers, threats to validity and the factual corrections.

**Status.** A working document under version control. It is not part of the record: luria does not read `scratch/`, and codes are cited bare. The framework F1–F4 (§2.7), the mapping tables (§§3.3–3.4) and the census are this draft's own, not entries the record holds.

## Files, in reading order

| File | Sections |
|---|---|
| [00-abstract-introduction.md](00-abstract-introduction.md) | Title, abstract, §1 (including a table of terms) |
| [01-argument.md](01-argument.md) | §2 The framework and its provenance |
| [02-luria-mapped.md](02-luria-mapped.md) | §3 Luria mapped onto it; expectations E1–E6 with falsifiers |
| [03-related-work-and-method.md](03-related-work-and-method.md) | §4 Related work, §5 Method, growth and rates |
| [04-cases.md](04-cases.md) | §6 The census, eight cases drawn from it, and grammar changes that went wrong |
| [05-governance.md](05-governance.md) | §7 Four loops: decisions, reviews of the argument, POSTMORTEM, the tool |
| [06-results.md](06-results.md) | §8 Results against E1–E6 |
| [07-discussion.md](07-discussion.md) | §9 Delegation, when to draw a distinction, maintained capacity, signatures |
| [08-threats-evaluation-conclusion.md](08-threats-evaluation-conclusion.md) | §10 Threats to validity, §11 Future evaluation, §12 Conclusion |
| [09-appendices.md](09-appendices.md) | Figures to produce, source map, references |

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

1. **The framework as claims.** F1–F4 integrate entries the record holds. The census findings (§8) are new results about the record. Should either be filed, for example as claims and an executed-study CASE in `record-as-apparatus`?
2. **ADR-048's flag.** The 237 entries carrying `anthology-candidate` were never revisited when its meaning changed (§8.2). That is a finding, and also a repair the record may want.
3. **POSTMORTEM-002's summary** (§7.5). Cite it as of a dated commit, or correct it in the record.
4. **The work.** Keep `luria-nucleating-an-argument` with its blurb revised, or give this paper a new `works` term?
5. **A human coder.** All census coders were instances of one model (§10). A human second coder on the 30-decision sample would address the largest reliability threat.
6. **Unread sources.** Dewey, Collingwood, Rheinberger, Bowker & Star, Stojanovic and Allspaw are cited but unread on the record (§4). They should be read, or supplied, before submission.
7. **Missing references:** the luria repository, Nygard, Tyree & Akerman, the qualitative-codebook literature, PRISM, PROV, and work on LLM agents with memory.
8. **Length and venue.** About 15,000 words with tables. A workshop version would keep §§1, 2.7, 3.6, 5.3, 6.1, 8 and 9.1.
9. **Authorship and disclosure** of AI assistance (§10).
