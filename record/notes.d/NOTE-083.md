---
number: 83
status: Read
formerly:
- NOTE-tmpy611h
paper: LIT-079
title: 'Garg & Fetzer, causal claims in economics'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2501.06873v2 (submitted 24 Feb 2026,
    dated 25 Feb 2026, 71 pp.), which is the latest version per the arXiv
    abs page re-checked 2026-09-26. I read §1–7, the whole appendix (A LLM
    retrieval; B JEL matching, limitations and replication; C edge-overlap
    robustness, Figs A1–A6; D validation, Tables A6–A9; E paper-level
    measures, Figs A7–A12, Tables A1–A5, A10–A11) and the references (text
    in rawC4/2501.06873.txt). Several figures (7–9, A1–A12) have no numeric
    content in the text layer, so I read their notes only. For the reframing
    I also downloaded v1 (12 Jan 2025, 73 pp., rawC4/2501.06873v1.pdf) and
    read its abstract, introduction, regression framework (§6.1–6.3),
    validation appendices B.1 and C, and Tables A2–A3. The rest of v1 was
    compared by search, not read closely. I did not read the OSF or SSRN
    versions.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  GPT-4o-mini is run in nine passes per paper over the first 30 pages of
  44,852 NBER/CEPR working papers. Edges kept in at least 4 of 9 passes,
  JEL-mapped, give "claim graphs" in which the share of edges backed by
  DiD/IV/RCT/RDD/synthetic control rises from 7.7% (1990) to 31.7% (2020).
  In year-fixed-effect-only regressions, doubling causal edges is
  associated with +1.36 pp top-five probability and +11.2% citations,
  while non-causal counterparts are flat or negative. The validation
  checks paper-level method labels, and only weakly: RCT and field labels
  have precision ≤ 0.10. It never checks the edges themselves against
  human labels.
---

<!-- inactive-ok-file: LIT-079 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-083: Garg & Fetzer, causal claims in economics

## Contribution

The paper builds and releases a paper-level representation of economics working papers as directed graphs over JEL concepts. Edges are labelled by evidentiary basis, and "causal" means supported by DiD (including TWFE/event study), IV, RCT, RDD or synthetic control (§2.2). The pipeline has three stages: summary, edge extraction, and embedding-based JEL mapping. It runs a 3 × 3 repeated-extraction design and aggregates edges by "edge overlap" (EO), the number of the nine runs in which an edge appears. Prompts, schemas, code and derived data are on GitHub. The substantive application documents the rise of causally supported edges by year and field, and relates graph measures to publication tier and citations.

## Key insight

Scoring causality per *relationship*, not per paper, makes it possible to ask whether journals reward causal structure specifically or narrative size in general. The paper's answer is that associations are positive for causal variants and flat or negative for non-causal ones. The answer is only as good as the edge labels, and those are validated indirectly.

## Assumptions

- **Scope.** Only the first 30 pages of each paper are read, and only papers over 1,000 characters (§2.1). Outcomes are fixed at a September 2024 snapshot.
- **Causal = design label.** "Structural estimation and causal language without an identified design" are non-causal (§2.2, A.1.2). The paper extracts what papers claim, not whether the claims are true (fn. 1).
- **The LLM is a faithful extractor.** GPT-4o-mini output under a fixed JSON schema is treated as measurement. Instability is handled by repetition, not by ground truth.
- **JEL mapping.** Each free-text node gets the single best cosine match to text-embedding-3-large embeddings of JEL descriptions (App. B.0.2–B.0.3). No similarity threshold, no multi-code mapping.
- **EO ≥ 4 baseline.** Chosen at an "inflection point in the stability profile" (§2.3). This leaves 42,404 papers (Table A10), not 44,852.
- **Publication matching.** A priority order: Baumann–Wohlrabe (9,139), then OpenAlex exact title (10,840), then NBER metadata (15,872), then an LLM-assisted residual step (1,707) (§2.5).
- **Regression model.** Eq. (1): y_p = α + β M_p^(type) + δ_t(p) + ε_p, one measure at a time, year fixed effects only, no field or method controls. The four outcomes are Top 5, Top 6–20, Top 21–100 and log(Cites + 1).

## Key results

- **Trend (§3, Fig. 2a).** 23.8% of baseline edges are causal. The mean per-paper causal share is 7.7% (1990), 8.6% (2000), 21.5% (2010), 31.7% (2020) and 32.6% (2023).
- **By field, pre- → post-2000 (§3, Fig. 2b).** Health 9.7 → 41.9%; Urban 9.0 → 37.4; Development 6.9 → 37.2; Behavioral 6.5 → 33.4; Finance 6.6 → 22.1; Econometrics 15.3 → 21.2; Macro 6.3 → 12.9.
- **Methods over time (§3.1, Fig. 3).**
  - DiD 10.5% of papers (1980) → 20.3% (2023); IV 3.3 → 7.6; RCT 0.8 (2000) → 8.0; RDD 1.3 → 2.5.
  - Theoretical/non-empirical 51.0 → 28.0; simulation 7.2 → 3.1.
  - A DiD rate of 10.5% and an RDD rate of 1.3% in 1980 look implausibly high for that era. That suggests label noise, which is my inference; the paper does not comment.
- **Headline coefficients (§5.2; Table A4 translations; top-five baseline rate 11.35%).**

  | measure | top five | citations |
  |---|---|---|
  | share causal | β = 0.027 [0.018, 0.037]; +10 pp share → +0.27 pp | β = 0.190 [0.151, 0.229] |
  | log causal edges | β = 0.020; doubling → +1.36 pp (+12% relative) | β = 0.153; doubling → +11.2% |
  | log causal new edges | β = 0.025; doubling → +1.71 pp (+15%) | β = 0.147; doubling → +10.7% |
  | non-causal edges, doubling | −0.94 pp | −1.9% |
  | non-causal new edges, doubling | −0.39 pp | −11.2% |
  | non-causal topic centrality | positive | β = 0.129 [0.114, 0.144] |
  | causal source–sink ratio | β = 0.009 | β = 0.091 |
  | non-causal source–sink ratio | β = −0.008 | β = −0.021 |

- **Redundancy (Table A3).** Share causal and log causal edges correlate at 0.935, so these two "families" are nearly the same variable.
- **Validation.**
  - Brodeur benchmark at EO ≥ 4, n = 285 (Table A6):

    | label | precision | recall | F1 |
    |---|---|---|---|
    | DiD | 0.74 | 0.68 | 0.71 |
    | RDD | 0.73 | 0.75 | 0.74 |
    | IV | 0.93 | 0.53 | 0.68 |

  - Per-run F1 (Table A7): RCT 0.03, Urban 0.18, Macro 0.12, Development 0.10, Finance 0.59.
  - Plausibly Exogenous, n = 491 (Table A8): mean cosine 0.175 (cause), 0.144 (effect), 0.268 (exogenous source). Random baselines are 0.006–0.045, permutation p = 0.001.
  - Snippet self-consistency (Table A9):

    | EO proxy | precision | recall |
    |---|---|---|
    | EO ≥ 1 | 0.778 | 0.779 |
    | EO ≥ 2 | 0.894 | 0.594 |
    | EO = 3 | 0.936 | 0.417 |

- **Threshold sensitivity (Table A10).** The mean causal share rises monotonically with the threshold: 0.152 (EO = 1) … 0.225 (EO = 4) … 0.270 (EO = 9).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Claim graphs can be extracted at scale with a stable, transparent pipeline | moderate | Nine-run EO design; open code and prompts; stability of signs across EO ≥ 1–4 (Figs A1–A6, shown only as figures) |
| C2 | The extracted method labels are accurate | moderate for DiD/RDD/IV, weak for RCT and fields | Tables A6–A7 on 285 matched papers. RCT precision ~0.02; field precision 0.05–0.43 |
| C3 | The extracted *edges* (cause → effect, with causal label) are accurate | weak | No human edge-level benchmark. The snippet check is self-consistency and stops at EO = 3. Plausibly Exogenous similarity is low in absolute terms (0.14–0.27) |
| C4 | The share of causal edges rose from 7.7% (1990) to 31.7% (2020) | moderate as a trend in the measure | Fig. 2a. The direction is robust across EO (Fig. A1), but the level depends on EO (Table A10) and the trend nearly vanishes with method-mix and volume controls (+0.0011/decade) |
| C5 | Causal narrative structure and novelty are positively associated with top-five publication and citations | moderate as associations | Year-FE bivariate regressions, n ≈ 12k for causal variants (my calculation: 42,404 × 28.2%; the paper reports no regression Ns). No field controls, although field drives both method and top-five rates (Fig. A10) |
| C6 | Non-causal complexity and novelty are weakly or negatively related | weak–moderate | Same design, on a different subsample from C5 |
| C7 | Editorial selection and citation diffusion reward different things (causal structure vs central topics) | informal argument | A contrast of coefficients from separate bivariate regressions, not a joint model |
| C8 | Top-tier journals reward gap filling "especially when supported by credible identification" | weak | §4.2.3 says causal gap filling shows "very little difference across tiers". The summary sentence contradicts the paragraph above it |
| C9 | The measure families were "pre-specified" | assertion | No pre-registration is cited. v1 used different headline measures (proportions, longest path). §4 says "three pre-specified families" and §5 says "five" |

## Method

1. **Stage 1.** GPT-4o-mini reads the first 30 pages and returns a structured summary: research questions, identification strategy, data, metadata and verbatim claim snippets. Run 3 times.
2. **Stage 2.** From each summary, extract edges with source, sink, relationship type and method. Run 3 times per summary, giving 9 edge lists.
3. **Stage 3.** Map source and sink text to the top-1 JEL code by cosine similarity of text-embedding-3-large vectors.
4. **Aggregation.** Keep an edge (source → sink) if it appears in at least 4 of the 9 lists.
5. **Measures, on the full and causal subgraphs.**
   - Log edges, unique paths, longest path.
   - Novel edges and paths against the cumulative prior graph; gap filling (rare JEL pairs).
   - Mean and variance of eigenvector or PageRank centrality in the prior literature graph.
   - Source–sink ratio.
6. **Outcomes.** Journal tier via SJR-standardised names. Citations from CitEc, then Baumann–Wohlrabe, then OpenAlex (coverage 94.6%, 97.7% before 2020).
7. **Estimation.** Eq. (1), one measure per regression.

## Concepts

- **Claim graph G_p = (V_p, E_p).** Nodes are JEL concepts. Edges are stated source → sink relations; "source/sink" denotes narrative direction, not causality (§2.2).
- **Causal edge.** An edge supported by DiD/TWFE/event study, IV/2SLS, RCT, RDD or synthetic control.
- **Edge overlap (EO).** The number of the 9 runs containing the edge. The baseline is EO ≥ 4.
- **Gap filling.** Linking JEL pairs that historically co-occurred rarely.
- **Source–sink ratio.** Distinct sources over distinct sinks. Above 1 is "fan-in"; below 1 is "fan-out".

## Connections

The paper positions itself against the credibility-revolution measurement literature: Angrist–Pischke, Card–DellaVigna, Hamermesh, Currie–Kleven–Zwiers, and especially Goldsmith-Pinkham (2024), with which its field ordering agrees. It also cites economics-of-ideas work (Bloom et al. 2020; Park et al. 2023) and scientometric mapping (Small; Waltman–van Eck). The benchmarks it borrows are Brodeur, Cook & Neisser (2024) and Oh's Plausibly Exogenous Galore. It does not compare against existing LLM-extraction evaluations outside economics.

## Bearing on the record

- This record's own practice is LLM-assisted structured extraction from papers: reading notes, relation graphs. This paper is the closest worked example in the record, and it is mostly a cautionary one.
  - **Repetition plus overlap filtering** gives a real precision–recall knob (Table A9).
  - **Self-consistency is not validation.** The v1 → v2 revision shows how differently the same benchmark reads once positive-class precision and recall are reported. v1 had F1 0.83 for RCT; v2 has 0.03.
- For ML practice, the transferable lessons are evaluation lessons about LLM-as-measurement: report per-class precision and recall on the minority class, validate the unit of analysis you actually use (edges, not paper labels), and hold the analysis sample fixed across compared variants. I did not check which, if any, ANTH- documents cover LLM-as-annotator evaluation, so no specific ANTH- document is named.

## Limitations

- No human-labelled edge-level ground truth. The authors' own limitation list (§6) omits this. v1 had promised author validation.
- Minority-class labels are very poor: RCT precision about 0.02, field precision 0.05–0.43. Yet field breakdowns (Figs 2b, 4) and the RCT trend are reported without error adjustment.
- Outcome regressions are bivariate with year fixed effects only. Field is an obvious confounder: fields differ in both causal-method use and top-five rates (Fig. A10). No field, method, author or institution controls appear. The standard-error method is unstated in v2.
- Causal-variant coefficients are identified on a selected ~28% subsample (papers with at least one retained causal edge), so causal-vs-non-causal comparisons mix samples.
- The trend's robustness table is described but absent, and its unit (per-decade slope of +0.0187) does not obviously match the headline levels.
- The 30-page truncation and one-best JEL code mapping compress claims (App. B.0.3).
- LLM-assisted publication matching for 1,707 papers, plus title-based matching generally, adds unquantified outcome error.

## Open questions

- What is edge-level precision and recall against expert or author annotation, by field and by method, at EO ≥ 4?
- Do the causal-structure associations with top-five placement survive field fixed effects and a common sample (for example, papers with both causal and non-causal edges)?
- How much of the 1990–2020 trend reflects extraction behaviour? Modern papers name their designs explicitly, which could make labelling easier. The +0.0011/decade result with method-mix controls suggests the question matters.

## Corrections to the seeded skim

- **How v2 reframes v1** (the brief asked for this). v1 (Jan 2025) was a substantive credibility-revolution paper built on "knowledge graphs" from "a custom language model". v2 (Feb 2026) presents itself as infrastructure: "evidence-annotated claim graphs", "claim-level infrastructure for cumulative science", and the LLM explicitly "as an information-retrieval engine rather than as an open-ended reasoner". The numbers and hedges moved with it:
  - **Headline trend.** v1: "roughly 4% in 1990 to nearly 28% in 2020". v2: 7.7% → 31.7%. The change follows the new nine-pass edge-overlap (EO ≥ 4) aggregation, which v1 did not have.
  - **Causal language.** v1's abstract: new causal edges "markedly increases" the likelihood of acceptance, and causal complexity "strongly predicts" publication. v2: "positively associated with", and "We interpret β as a conditional association, not a causal effect" (§5.1).
  - **Validation was rewritten, and the new version contradicts the old.**
    - v1 Table A2 reported, against Brodeur et al., F1 = 0.987 (Macro), 0.955 (Urban), 0.930 (Finance), 0.827 (RCT). v2 Table A7 reports per-run F1 on the same benchmark of ≈0.12 (Macro), ≈0.18 (Urban), ≈0.59 (Finance), ≈0.03 (RCT), with RCT precision 0.014–0.032. The v1 figures were evidently not positive-class metrics (my inference).
    - v1 Table A3 reported mean cosine similarity 0.61 / 0.64 / 0.80 (cause / effect / exogenous source) to Plausibly Exogenous Galore. v2 Table A8 reports 0.17 / 0.14 / 0.27 on "deterministic text vectors", with lift over a shuffled baseline.
    - v1 promised "A large scale validation ... contacting corresponding authors to validate the causal graphs in their own papers" (App. B.1). v2 contains no author or human edge-level validation.
  - **Regression specification.** v1 clustered standard errors by year and reported models with and without year fixed effects. v2 reports year-FE models only and does not state its standard-error method.
- **The dossier calls the snippet check a validation and implies it covers the baseline.** It is a self-consistency check, and its EO proxies stop at "EO = 3" (Table A9: precision 0.936, recall 0.417). The EO ≥ 4 baseline is never audited this way.
- **"External checks cover under 2% of papers" (dossier) understates the problem.** The external checks validate *paper-level method and field labels* and *free-text cause/effect/source similarity*, not claim edges. Within them, IV recall is ~0.53, RCT precision ~0.02, and field precision 0.05–0.43.
- **The composition-control robustness undercuts the trend more than the text admits.** §3 reports +0.0187 per decade unadjusted, +0.0174 with field controls, and **+0.0011** with method-mix and graph-volume controls. It calls this "compositional shifts explain part, but not all". I could not find the promised trend-robustness table in the appendix. The unadjusted +0.0187/decade is also hard to reconcile with a 7.7% → 31.7% rise over three decades (≈+0.08/decade); the text does not explain the units.
- **Causal and non-causal coefficients come from different samples.** Causal variants are undefined for 71.76% of papers (Table A2), so causal-measure coefficients are estimated on the roughly 28% of papers with at least one retained causal edge. Non-causal coefficients cover roughly 83% of papers. The dossier's reading of "causal vs non-causal" as a like-for-like contrast does not hold.
