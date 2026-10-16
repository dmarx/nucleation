---
number: 912
status: Read
formerly:
- NOTE-tmparaq2
paper: LIT-1109
title: Olston, Loo & Widom — Adaptive precision setting for cached approximate values
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the copy in the University of Pennsylvania's
    institutional repository (ScholarlyCommons, oai:repository.upenn.edu:cis_papers-1351;
    Loo's institution), the open-access location that Unpaywall, OpenAlex and Semantic
    Scholar all give. The listed download link returns the repository's JavaScript
    front end, so the file was fetched through the repository's REST endpoint for
    the same bitstream (https://repository.upenn.edu/server/api/core/bitstreams/92340f91-673c-435e-9b4e-b24072d4d96b/content,
    file name p355_olston.pdf, 12 pp.). It carries the ACM SIGMOD 2001 notice and
    printed pages 355–366, so it is the camera-ready text, although Unpaywall labels
    it a submitted version. Text extracted with pdftotext; the extraction drops
    the Greek letters (ρ, Ω, α, τ₀, τ∞, δ, κ), so Table 1, Sections 2–3, Section
    4.2, Section 4.7, Figures 10–13 and Appendix A were checked against page images
    of printed pages 358–360, 364 and 366. Read: abstract, Sections 1–5, Table 1,
    Figures 1–15, Appendix A and the reference list. Nothing skipped. Every quotation
    below was checked against the extracted text by script, with whitespace normalised;
    the five whose symbols or line breaks the extraction mangles (those containing
    W*, 1/W², and "rough approximation", which the two-column extraction interleaves)
    were checked against the page images instead.
date: '2026-10-15'
summary: >-
  Olston, Loo and Widom set the width of each cached interval adaptively to minimize
  total refresh traffic. A narrow interval is escaped often (value-initiated refreshes,
  cost C_vr); a wide one is too imprecise for queries more often (query-initiated
  refreshes, cost C_qr). Under a model in which these probabilities go as 1/W² and
  W, the expected cost rate is least where ρ·P_vr = P_qr, ρ = 2C_vr/C_qr, and a
  rule that widens on value-initiated and narrows on query-initiated refreshes,
  with probabilities set by ρ, reached within 1% to 5% of the best fixed width in
  simulation. That the rule converges is argued, not proved. With exact copies required
  it matched an adaptive exact-caching algorithm, and where imprecision was allowed
  it beat it. Staleness is priced as refresh traffic only: there is no build cost,
  no cost of a wrong answer, and the interval is never wrong.
---

# NOTE-912: Olston, Loo & Widom — Adaptive precision setting for cached approximate values

## Contribution

TRAPP ([LIT-1117](../literature.d/LIT-1117.md)) took cached bounds as given. This paper asks how wide they
should be. "approximations that are too precise easily become invalid,
requiring frequent refreshing, while overly imprecise approximations are
likely to be useless to applications, which must then bypass the cache." It
gives a parameterized algorithm that adjusts each cached interval's width at
every refresh, justifies its balancing rule from a cost model, tests it in
simulation on a random walk and on network-traffic traces, shows that it
reduces to adaptive exact caching as a special case, and compares it with
Divergence Caching.

## Key insight

Both kinds of refresh are signals. A value-initiated refresh says the interval
was too narrow; a query-initiated one says it was too wide. If the cost of
each is weighted correctly, the width at which the weighted chances of the two
are equal is the width of least expected cost, so a rule that widens on one
signal and narrows on the other, without measuring update rates, query rates
or precision demands, moves toward the optimum and follows it as they change.

## Assumptions

- **Source-side validity.** Whenever a value changes, the source tests each
  cached approximation and sends a new one if it is no longer valid. "Under
  this protocol, caches are guaranteed to always contain valid
  approximations, modulo communication overhead."
- **Intervals, centred, constant in time.** Validity is L ≤ V ≤ H;
  precision is 1/(H − L). Each new interval is centred on the current value,
  so one number W describes it. Uncentred and time-varying intervals are
  tested in Section 4.5 and mostly lose.
- **Cost = communication.** "Let us assume that our goal is to minimize
  overall network traffic." Costs C_vr and C_qr are fixed per refresh. Space
  enters only through a cache that holds κ ≤ n intervals and evicts the
  widest.
- **Refresh probabilities.** For the analysis, P_vr = K₁/W² and P_qr = K₂·W
  with K₁, K₂ depending on data, updates, query frequency and precision
  demands. Appendix A derives them in a simplified model: a one-dimensional
  random walk with step s, one value per query, precision constraints uniform
  on [0, δ_max]. P_qr = W/(T_q·δ_max) exactly for W ≤ δ_max. P_vr ∝ 1/W² comes
  from Chebyshev's inequality, P ≤ t·(s/k)² with k = W/2, giving
  P_vr ≈ t·(2s/W)² after t steps, with "the upper bound as a rough
  approximation"; it is a bound used as an estimate, not a derived
  probability.
- **The only assumption the algorithm needs**, per the authors: "for each
  approximate value, the probability of a query-initiated refresh is
  proportional to the width of the approximation."
- **No staleness in transit.** Refresh delay is ignored ("modulo
  communication overhead"). No insertions or deletions are modelled.

## Key results

- **The cost rate and its minimum (Section 3).** Ω(W) = C_vr·K₁/W² + C_qr·K₂·W.
  Setting the derivative to zero gives W* = (2·(C_vr/C_qr)·(K₁/K₂))^(1/3) =
  (ρ·K₁/K₂)^(1/3), with cost factor ρ = 2·C_vr/C_qr, and at W*, ρ·P_vr = P_qr.
  With ρ = 1 the optimum is where the two refreshes are equally likely
  (Figure 2). This is calculus on the assumed forms; nothing more is proved.
- **The algorithm (Section 2).** On a value-initiated refresh, with probability
  min{ρ, 1} set W′ = W·(1 + α); on a query-initiated refresh, with probability
  min{1/ρ, 1} set W′ = W/(1 + α). Widths below τ₀ are sent as 0 (exact) and
  widths at or above τ∞ as ∞ (effectively not cached), while the source keeps
  the unthresholded width. The claim that this reaches W* is argued from the
  balancing condition: "our algorithm adapts to always move W toward the
  optimal width W*". No convergence theorem, rate or stationary
  distribution is given.
- **Model check and optimality, simulated (Section 4.2).** One value on a
  random walk with steps uniform in [0.5, 1.5], T_q = 2, δ_avg = 20, Δδ = 1,
  ρ = 1. With W fixed per run, measured P_vr and P_qr were "indeed
  proportional to 1/W² and W", and the least cost fell where they were equal
  (Figure 3). The adaptive rule converged to W = 3.11, "within 1% of the
  optimal W*"; over all combinations of T_q ∈ {1, 2}, δ_avg ∈ {10, 20},
  ρ ∈ {1, 4}, within 5% of optimal.
- **Real traces (Sections 4.3–4.4).** 50 most heavily trafficked hosts in a
  two-hour wide-area trace (Paxson and Floyd), one-minute moving averages
  every second; queries every T_q seconds take SUM or MAX over 10 random
  sources, with the TRAPP refresh selection. ρ ∈ {1, 4}, from C_qr = 2 (a
  remote read) and C_vr = 1 (updates simply sent) or 4 (two-phase locking).
  Recommended settings: α = 1 (double on widen, halve on narrow); τ₀ a small
  constant below the smallest meaningful precision constraint (1K here, costing
  under 1% for constraints of 5K–15K); τ∞ = ∞ for mixed workloads, τ∞ = 0 for
  SUM workloads that demand exact answers; for MAX, τ∞ = ∞ is best even then.
  Varying the spread of precision constraints changed performance by 1.9%
  (δ_avg = 100K), 5.5% (10K) and under 1% (5K).
- **Variations that lost (Section 4.5).** Uncentred intervals did worse except
  on a biased random walk. Widths growing as t^(1/2) or t^(1/3) did worse than
  constant intervals on the traces and the unbiased walk, which runs against
  the square-root bound functions [LIT-1117](../literature.d/LIT-1117.md) suggested. Deciding from the
  last r refreshes did no better than r = 1.
- **Exact caching as a special case (Section 4.6).** With τ∞ = 0 every interval
  is exact or absent, and the rule "dynamically chooses whether or not to cache
  each data value". Against an adaptive exact-caching rule derived from Wolfson,
  Jajodia and Huang (cache iff w·C_vr < r·C_qr over the last x reads and writes,
  x tuned per run), it "almost precisely matches the exact caching algorithm
  under all workloads, cache sizes, and cost configurations tested" (Figures
  10–13). With τ∞ = ∞ it does markedly better where queries tolerate imprecision,
  slightly worse for exact SUM workloads, much better for MAX; with a small
  cache (κ = 20) the gain mostly disappears because inexact intervals are
  evicted.
- **Staleness by update count (Section 4.7).** Bounding the number of
  unreflected updates instead of the value, with ρ′ = C_vr/C_qr from "A similar
  (simplified) analysis", it showed "a modest performance improvement over
  Divergence Caching" (Figures 14–15, T_q ∈ {1, 5}).
- **Unsupported in the paper.** The introduction says naive choices give gains
  "a factor of two (or more) less" than careful ones; no experiment isolates
  that figure.

## Bearing on the record

**[QUESTION-114](../questions.d/QUESTION-114.md) and staleness.** This is the nearest the record now holds to a
price for staleness. Staleness is the width W a cached copy may drift before it
must be refreshed. Narrow costs upkeep (the source pushes more often); wide
costs per-use fallbacks (queries fetch the exact value more often). Both are in
one objective, Ω(W) = C_vr·P_vr(W) + C_qr·P_qr(W), with a closed-form optimum
under stated assumptions and a balancing rule that needs no forecast of update
or query rates. [THEORY-348](../theory.d/THEORY-348.md) forbids stale reads, [THEORY-350](../theory.d/THEORY-350.md) refreshes all views
in a batch, and [THEORY-332](../theory.d/THEORY-332.md) has upkeep without staleness. This has staleness and
upkeep traded against each other, and its exact-caching special case is the
keep-or-drop choice that [THEORY-348](../theory.d/THEORY-348.md) and [THEORY-332](../theory.d/THEORY-332.md) analyse.

What it does not price. (1) Build cost and space: there is no one-time cost and
the cache limit is handled by a heuristic. (2) Stored answers: the cached items
are base values; aggregates are computed at query time. (3) The cost of a
wrong answer: validity is guaranteed by the source, so a stale read is
imprecise, never wrong. The price of staleness here is the communication that
keeps it bounded, plus the fallbacks when the bound is too loose for a query,
not the damage done by reusing something obsolete. (4) Worst cases: the
guarantee, such as it is, is in expectation under a stationary stochastic
model, and the adaptive rule's optimality is shown only in simulation.

**[CLAIM-303](../claims.d/CLAIM-303.md).** The paper gives [CLAIM-303](../claims.d/CLAIM-303.md)'s u and c_a a common parameter. If
"checking it is still current" is paid by whoever owns the source, and each
use asks whether the filed item is precise enough for it, then u falls and
the fallback rate rises as the filed item claims less, and there is a best
level of claim between them. For a filed argument that would mean a filed
conclusion stated with a tolerance, upkeep triggered when its premises move
beyond it, and reconstruction when a use needs more than it states. Section
4.7 shows the scheme works when staleness is counted as unreflected updates,
which for an argument would be changes to what it rests on. But the
precondition does not transfer: the scheme needs a source that sees every
change and tests every copy. A filed argument has none, and A11's term, the
cost of reusing an obsolete conclusion, is exactly what the scheme removes by
that assumption. So it does not price that term. It shows a form in which
staleness can be priced when such monitoring exists, and implies that the
record would have to pay for monitoring to use it.

**[CLAIM-308](../claims.d/CLAIM-308.md).** Two points. First, with τ∞ = 0 the rule is an adaptive
cache-or-not decision driven by counted events (value-initiated against
query-initiated refreshes, weighted by ρ), with no forecast. That is the same
family as the break-even rule, and like it, it matched a reuse-counting
benchmark. But its justification is an expected-cost balance, ρ·P_vr = P_qr,
not a worst-case ratio, so it neither adds to nor weakens [CLAIM-308](../claims.d/CLAIM-308.md)'s
"within twice the hindsight optimum". Second, it reaches past [CLAIM-308](../claims.d/CLAIM-308.md)'s
stated limit "with staleness left out": once a copy may be inexact, the choice
is no longer two states but a continuum of widths, and the optimum is an
interior balance. That bears on [CLAIM-308](../claims.d/CLAIM-308.md) the way its own "more than two
options" caveat does: in a model that admits staleness, the two-state theorem
is the special case, not the general answer. It does not show that a worst-case
bound fails there; nobody here analysed one.
