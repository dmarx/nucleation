---
status: Read
paper: LIT-tmpu5ktj
title: Bruno & Chaudhuri — An online approach to physical design tuning
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full 2026-10-15 from the PDF that Microsoft Research's own publication
    page for the paper links (www.microsoft.com/en-us/research/publication/an-online-approach-to-physical-design-tuning/,
    which points to www.microsoft.com/en-us/research/wp-content/uploads/2007/01/continuous.pdf;
    the link was confirmed through the MSR site's JSON record for the item, msr-research-item/154423).
    Both authors were at Microsoft Research, so this is the authors' institution's
    copy. It is 10 pages in IEEE two-column camera-ready layout with no IEEE page
    numbers or copyright line (PDF created 23 Nov 2006), so it is the accepted version,
    not the publisher's typeset copy. The page range 826–835 was not confirmed from
    it. Unpaywall, OpenAlex and Semantic Scholar all report the paper closed and
    list no copy. Text was extracted with pdftotext. The extraction scrambles subscripts,
    summations and the figures, so the cost definition, Definition 1, Figures 2–4
    and Theorems 1 and 2 were checked against page images of pages 3 and 4. Read:
    abstract, Sections 1–6, all figures, Table 1, Figure 9 and the references. Nothing
    skipped. Every quotation from the paper was checked by script against the extracted
    text, with whitespace normalised. One, "< 3 since ε > 0", loses its symbols
    in extraction and was confirmed on the page image. Quotations from record entries
    were checked against those entries. The ratio of 3 was also tested by a simulation
    of my own, which is not part of the paper and is labelled where it is used.
    The works it builds on (Agrawal, Chu and Narasayya 2006; Bruno and Chaudhuri
    2006) and its competitors (COLT, QUIET) were not read.
date: '2026-10-15'
summary: >-
  An always-on index tuner for SQL Server. It keeps, for each candidate or existing
  index, the running sum of what each query would have saved with it (what-if optimizer
  estimates, with update costs counted as losses). It creates an index once that
  sum has risen by the index's build cost above its lowest point, and drops it once
  the sum has fallen by the build cost from its highest point. For one index with
  no space limit, the authors call this 3-competitive against the optimal schedule
  that knows the workload in advance. The proof only gives a workload on which the
  ratio approaches 3, and the paper cites no competitive-analysis work, ski rental
  included. The general case (many interacting indexes and a storage limit) uses
  heuristics with no guarantee. All costs in the experiments are optimizer estimates,
  on synthetic and TPC-H workloads.
---

# NOTE-tmpcs92s: Bruno & Chaudhuri — An online approach to physical design tuning

## Contribution

Offline index tuning tools need a DBA to pick a representative workload and to decide when to tune. The paper replaces this with algorithms that "are always-on and continuously modify the current physical design reacting to changes in the query workload", and that "take into account storage constraints, update statements, and the cost to create temporary physical structures". It frames the task as choosing a schedule of configurations for a sequence of statements, priced by the queries' costs plus the cost of every index built. It gives an exact offline algorithm (Opt-SI) and an online version (Online-SI) for one index, and a heuristic online tuner (OnlinePT) for many indexes under a space limit. The tuner was built in Microsoft SQL Server 2005 within the AutoAdmin project.

The motivating case is a changing mix of reads and writes. In a bug tracker, most days are reads and some "bug-bash" days are mostly inserts. Over a month, "chances are that no index is globally useful", because update costs during the insert days cancel the gains. A schedule that builds an index for the reading days and drops it for the inserting days beats any fixed set. Such a tuner "must also balance the cost of transitioning between physical design configurations and the potential benefits of such design changes for the future workload". And "reacting too quickly can result in unwanted oscillations, in which the same indexes are continuously created and dropped."

## Key insight

Hold an index's history as one number: Δ, the running sum, over statements so far, of cost without the index minus cost with it. Queries the index would speed up push Δ up, and updates that would have to maintain it push Δ down. The offline optimum, looking at Δ's future path, builds the index when Δ will rise by the build cost B_I before falling back below its current level, and drops it when Δ will fall by B_I before recovering. The online algorithm makes the same moves late. It acts once the past path shows that the optimum would have made them: "we transition configurations after gathering the information that proves that the optimal strategy would have done so at a past point in time." So the rule is: build once the benefit missed since the last low point equals the build cost, and drop once the loss since the last high point equals the build cost. Bookkeeping is three numbers per index (Δ, Δmin, Δmax).

## Assumptions

- **Workload.** A sequence W = (q1, …, qn) of queries and updates. When it fixes the configuration s_i, the online algorithm knows only q1 … q_i. Nothing is assumed about the future: no distribution, no frequencies, no stationarity. The paper says when this pays: "If a DBA has full information about the workload characteristics, then a static analysis and deployment by existing tools (e.g., [2, 3]) would be a better alternative."
- **Cost.** cost(W, S) = Σ_i [ c_i^{s_i} + transition(s_{i−1}, s_i) ], with transition(s0, s1) = Σ_{I ∈ s1 − s0} B_I^{s0}. Only creation is charged. Dropping is free, in both the single-index model (transition = B_I if 0→1, "0 otherwise") and the general one.
- **Build cost depends on the configuration.** B_I^s depends on which indexes exist. An index whose key matches an existing one needs no sort, so it is cheap (I1 costs 1.33 against I2's 8.96 in Section 4.1). After the wide merged index I5 exists, I2 and I4 cost 1.2.
- **Upkeep enters per statement.** The cost of an INSERT/UPDATE/DELETE under a configuration includes maintaining its indexes, and enters Δ as negative benefit (the O^U, N^U terms). There is no separate upkeep term, and nothing for drift or reorganisation over time.
- **Storage** is a hard limit in the multi-index case only. The single-index analysis has none.
- **Costs are optimizer estimates.** The cost of the configuration not in force comes from a local rewrite of the plan (getCost), with no re-optimization. That gives "an approximation (tight upper bound) of the global optimal plan". The experiments report estimated costs.
- **Index creation is instantaneous in the analysis and synchronous in the experiments** ("we enforce that each physical change is done before evaluating new queries (i.e., index creation and drops are synchronous)"). Section 3.3 discusses asynchronous online creation, but does not evaluate it.
- **Single-index analysis:** one index, configuration-independent B_I, no storage limit, no interaction with other indexes.

## Key results

- **Theorem 1.** Opt-SI gives the optimal schedule for a known workload (single index). The proof covers Case A2 and says "The remaining cases are proved analogously, but we omit the details due to space constraints." Footnote 2: "there are simpler ways to obtain the optimal schedule (e.g., see [2])". Definition 1 as printed calls c_i^0 the cost "when index I is present", which is the reverse of its own gloss and of Figure 4. The gloss (c^0 = without the index) is the intended reading.
- **Online-SI (Figure 4).** After each query: δ = c_i^0 − c_i^1; Δ += δ; update Δmin, Δmax. If the index is absent and Δ − Δmin ≥ B_I, create it and set Δmax = Δ. If present and Δmax − Δ ≥ B_I, drop it and set Δmin = Δ.
- **Theorem 2.** "Algorithm Online-SI is three-competitive (i.e., it is no worse than 3 times the optimal algorithm Opt-SI)." The proof gives one workload: alternating q1, q2 with cost(q1,0) = ε + B_I, cost(q1,1) = ε, cost(q2,0) = ε, cost(q2,1) = ε + B_I. Opt pays B_I + 2ε per pair and Online-SI pays 3B_I + 2ε, a ratio "< 3 since ε > 0". The authors introduce this as "a worst-case scenario". That shows the ratio can come arbitrarily close to 3. It does not show it can never exceed 3, and no upper-bound argument is given. Conditions as stated: one index, no space limit, B_I fixed.
- **My check, not the paper's.** I wrote a short simulation (exact dynamic program for the optimum, Online-SI as in Figure 4, random workloads; L44_scripts/). It finds the ratio exceeds 3 when a single statement's saving is a large fraction of B_I: up to 4.7 with |δ| ≤ B_I. The ratio is unbounded when one statement's saving exceeds B_I. For example, with one query costing K without the index and 0 with it, the optimum pays B_I and Online-SI pays K. With every |δ| at most a tenth of B_I, no random workload exceeded 3 (worst 2.4). So the stated ratio needs an unstated condition: each statement's cost difference must be small relative to the build cost, as with ski rental's unit rent. The paper's own example sits exactly at |δ| = B_I.
- **Multi-index case.** "(but cannot guarantee three-competitiveness anymore)". OnlinePT runs Online-SI per candidate index. A candidate is the best index for some access-path request of a query. It adds heuristics: interaction adjustments by "usefulness level" (one index's columns containing another's), scaled by size ratios, with "While ours is not a definitive solution"; residual(I, s) = B_I^s − (Δmax − Δ) and benefit(I, s) = (Δ − Δmin) − B_I^s, so a new index may evict a set of existing ones whose combined residual is less than its benefit; index merging to make candidates; and an anti-oscillation rule. Without that rule a full disk gives "an endless oscillation although the relative benefit of all indexes is similar". The rule lowers the benefit of absent candidates while existing indexes keep paying. No guarantee is claimed for any of this.
- **Extras (Section 3.3), not evaluated.** Throttling (Δ updates every query, decisions periodically); aborting an index build if its Δ falls by more than B_I meanwhile; "suspend" instead of drop where the DBMS allows it, which changes B_I to the cheaper cost of restarting; manual changes adjust Δs the same way; statistics built once Δ − Δmin passes a fraction (e.g. 0.8) of B_I.
- **Simple workloads (Table 1).** Table R, two select queries, one insert, five candidate indexes, estimated costs, Opt "manually constructed". OnlinePT against Opt: W1 (250 q1 then 250 q2, 135 MB) 85.77 vs 62.92; W2 (250 interleaved pairs) 180.01 vs 173.96 at 135 MB, 79.71 vs 69.21 at 138 MB, 75.16 vs 56.86 at 150 MB; W3 (100 q1 then 100 inserts) 199.92 vs 164.69. Ratios 1.04–1.36. In W3 the indexes are dropped after 4 and 22 inserts, "it takes longer to drop I2 because its creation time is larger". The text and table disagree in places: 38 vs 31 executions, 207 vs 214, "q4" for q2, I2's cost 8.96 vs 8.69, totals 180.1 vs 180.01 and 75.36 vs 75.16.
- **TPC-H (Figures 7, 8).** 1 GB database plus 1 GB for indexes, 60 batches, each a permutation of all TPC-H queries. Design changes cluster in batches 1–15, then stop. After that, per-batch cost is "almost indistinguishable" from the offline tools'. Adding a block of updates to lineitem after batch 14, OnlinePT and the offline sequence tool drop the lineitem indexes and rebuild them afterwards. The offline set tool never builds them. Overall (Figure 8, bars only, no numbers): "As expected, OnlinePT is slightly worse than Offline-Seq, which knows the future", and sometimes better than Offline-Set.
- **Overhead (Figure 9).** 19.8 ms per statement on TPC-H (1.7% of the lesser of optimization and execution time), 0.12 ms (0.82%) on the simple workload. The text says 0.41% for the simple one. The per-statement part (lines 1–8) is under 0.2%. The rest can be throttled.

## Relation to Karlin et al. and ski rental

The paper never mentions ski rental, rent-or-buy, competitive analysis as a field, Karlin et al., or Sleator and Tarjan. Its reference list is eleven database papers. The term "three-competitive" is used without citation. The connection is structural only, and the record should not attribute it to the authors.

The structure matches. Online-SI's create rule is Karlin et al.'s rule ([LIT-tmpwhdfd](../literature.d/LIT-tmpwhdfd.md)): switch state once the extra cost accumulated in the current state equals the cost of switching. The extra cost is the benefit missed since Δ's last low, and the switching cost is the build cost B_I. There are three differences. (1) It is two-sided: the drop rule mirrors the create rule with the same threshold B_I, though dropping is free. Paying again to rebuild is what the drop guards against, and that gives hysteresis against oscillation. (2) "Accumulated" means since the last minimum or maximum of Δ, not since the last switch. Evidence that has been reversed does not count. (3) The ratio rises from Karlin et al.'s proved 2 to an asserted 3, because the online rule can pay for the same mistake in both directions on each cycle. Karlin et al.'s bound assumes unit rent steps. This paper's needs the same thing and does not say so.

## Bearing on the record

**On [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md). The survey's description is right in substance and overstated in one point.** This is the first paper the question has read whose model holds the parts the earlier readings each lacked:

- one-time organising cost: B_I, charged at each build and dependent on what is already built (Finkelstein et al., Chaudhuri & Narasayya 1997 and Harinarayan et al. had none);
- per-query savings: c^0 − c^1 per statement;
- upkeep: per update statement, as negative savings;
- space: a hard limit in the general case;
- an unknown, changing workload, with nothing assumed about the future.

The optimum is defined over schedules, so building, keeping and dropping are priced together. Is it the joint cost model? For indexes, largely yes, with limits the record should state:

1. Guarantee and model are split. The single-index case, the only one with a guarantee, has no space limit and no interaction, and its stated 3 is shown only as a lower bound. By my check it holds only when each statement's saving is small next to the build cost. The case with space, interaction and merging is heuristic.
2. Dropping is free and staleness is not modelled. Upkeep is paid statement by statement, never deferred. It has no term for letting a structure drift and re-sorting later, which is [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md)'s "staleness".
3. Build time is instantaneous in the analysis. The paper does not model the build's own duration or queries waiting for it, beyond the asynchronous-build remarks.
4. It prices access paths to stored rows, not stored answers. So, like Finkelstein et al., it does not cover the cockpit's bugs. That would need Harinarayan et al.'s views put on the same schedule. The paper says nothing about views.
5. All its numbers are optimizer estimates.

The survey describes the paper as applying the competitive, rent-or-buy framing. That is true of the structure and false of the citation. The record's summary of [LIT-tmpu5ktj](../literature.d/LIT-tmpu5ktj.md) should say it is a rent-or-buy rule in structure, not by citation, and should report the ratio as asserted, with its unstated condition.

**On [CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md) (set a hard-to-find brick aside when found).** In this model the practice is right when the build cost is near zero, which is the case's own premise. With B_I ≈ 0 the create rule fires on the first positive saving, so the bin is made at the first retrieval that would have gone faster with it. That agrees with Karlin et al. and Sleator and Tarjan as the record already reads them. The model adds two things the case lacks. First, a symmetric rule for removing the bin: once the bin has cost more than it saved, by as much as it would cost to make again. A bin "costs" by taking shelf space under a limit, or by slowing other searches, or by making new bricks costlier to put away. Second, the bin's cost depends on the bins already made (B_I^s). A brick set aside next to a related bin is cheaper to place, much as an index that shares a sort order is cheap to build. If the build cost is near zero the drop threshold is also near zero, and the rule would remove bins at the first loss. The case's practice needs some hysteresis that the near-zero cost does not give.

**On [CLAIM-tmp6u639](../claims.d/CLAIM-tmp6u639.md) (carve when retrieval fails).** The paper's criterion is a different one, and it narrows the claim's retrieval criterion. It does not carve when one retrieval fails or misses a deadline. It carves when the accumulated excess search, summed over retrievals since the last low point and net of what the bin would cost on other operations, reaches the cost of making the bin. That is the claim's own sentence: "A bin pays when the search it saves, summed over the retrievals expected, exceeds its cost". But it uses retrievals already made, not expected ones, and needs no forecast of use. In the claim's terms the per-retrieval saving is about m/(c+1) less the cost of searching the bin. For one rare, often-wanted brick that saving is large, so the threshold is reached in few retrievals, which fits "very few of but use often". There are two differences. (a) The paper minimises total cost and has no deadline, so it says nothing about "can it be reached in time?", which is the claim's distinction. A deadline criterion and a cumulative-cost criterion can disagree: a brick wanted once, urgently, never pays for a bin under this rule. (b) The rule's guarantee needs each retrieval's saving to be small next to the bin's cost. A single search through 200 similar bricks may cost more than making a tiny bin. That is the regime where Online-SI has no guarantee, and where acting at once beats waiting to accumulate evidence. So the LEGO case sits at the edge of the paper's guarantee, not inside it. Nothing here bears on the claim's evidence criterion (d'² against the Occam cost), which the paper does not have.

## Limitations

- The one proved-optimal result (Theorem 1) has its proof mostly omitted. The competitive result (Theorem 2) is supported only by an example, and by my simulation needs a bound on per-statement savings that is not stated.
- No guarantee for the general algorithm. Interaction handling is approximate by the authors' own account.
- Costs are optimizer estimates throughout. Index builds are synchronous in the experiments. TPC-H results are shown as charts without numbers. The Table 1 text and table differ in several figures.
- Dropping is free, upkeep is per statement, and there is no staleness, deferred maintenance or build duration.
- Indexes only. No views or precomputed answers.
- The authors call their evaluation "preliminary": "Our preliminary evaluation demonstrates the promise of our online tuning approach."

## Open questions

- Is Online-SI 3-competitive when every |c_i^0 − c_i^1| ≤ B_I, or only in the limit of small steps? My simulation found 4.7 at |δ| ≤ B_I, so the right condition is probably smaller steps, or a ratio that grows with step size. A later analysis of this algorithm would settle it. None is held.
- A schedule model that also has deferred upkeep (let new items pile up, sort later) and a deadline on retrieval would be the joint model [QUESTION-tmplg07t](../questions.d/QUESTION-tmplg07t.md) asks for. Neither this paper nor the earlier readings supply both.
