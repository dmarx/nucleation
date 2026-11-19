# Reader notes: Skill-it! (Chen et al.)

Pilot in-flight notes, 2026-11-19. Lead: LEAD-tmp5lpoy.

## Step 1: identity and copy
- arXiv API (export.arxiv.org, no email): 2307.14430, one version only (v1), published 2023-07-26T18:01:49Z. Authors Mayee F. Chen, Nicholas Roberts, Kush Bhatia, Jue Wang, Ce Zhang, Frederic Sala, Christopher Re. No journal-ref or comment on arXiv, so NeurIPS 2023 not yet verified there.
- Not held in the record (grep for the arXiv id and title: only the lead names it).
- Copy: arxiv.org/pdf/2307.14430v1, 37 pages, fetched 200; text extracted to my scratchpad (not committed).

## Step 2: venue and second copy
- Semantic Scholar API: 429 rate limit, stopped. OpenReview API: search hit a NeurIPS 2023 review; fetching the note gave 403, stopped.
- NeurIPS 2023 confirmed from proceedings.neurips.cc (2023 index lists the title, main conference track). Proceedings PDF (41 pp.) fetched and read for differences: abstract says 37.5 points (arXiv v1: 36.5); LEGO curriculum baseline tables re-run; new Appendix E.5.1 counts the graph-learning cost (Table 13). Core numbers of section 3.2 unchanged (35.9%, 32%, 4.1%).

## Step 3: paper read (arXiv v1 in full, proceedings for changes)
- A skill's "prerequisite" is defined by a MIXTURE, not a sequence: Def. 2.2, edge (si, sj) "if the amount of data needed to learn sj when uniformly sampling from Dsi ∪ Dsj is no more than the amount of data needed when sampling only from Dsj".
- The saving is at a fixed total budget: LEGO skill 3 "in 35.9% fewer training steps" mixture of s1,s2,s3 reaches val loss 0.01 as training on s3 alone; addition 32%; NI Spanish QG 4.1% lower loss using 25% of the Spanish QG data; stance detection 11%. Fig. 3 numbers carry no seeds/error bars that I can see.
- Orderings tested as sequences (Skill-curriculum, from Varshney et al.) do NOT help: on LEGO skill-curriculum avg loss 0.546 vs random 0.542 vs skill-stratified mixture 0.046 (proceedings Table 4). On addition skill-curriculum 0.463 vs random 0.010 (proceedings Table 6). frac=0.0 "resulted in forgetting".
- Edges do not follow the task's own logical chain: D.1, skill 3 does not help skill 4 though they share a chain edge.
- Doubt: no experiment trains prerequisite FIRST, then target, against target-only with the prerequisite's cost stated. The closest to CLAIM-756's shape is the mixture-vs-target-only at equal total steps, where the prerequisite data comes out of the budget.

## Step 4: bearings searched
- Named: CLAIM-756 qualifies-to-supports (an instance of a co-acquired skill lowering the steps to a target at equal total budget; not sequential, no valuation); CLAIM-754 parallel only; CLAIM-758 no bearing (no stabilization time-course); TERM-131 background; CASE-295 parallel in shape, but the paper's "prerequisite" is co-training, not prior acquisition; CASE-294 methods analogy (loss-to-threshold budget; graph-learning brute force is a pairwise cost probe).
- Found by grep: QUESTION-039 (order of acquisition) and THEORY-783 / THEORY-253 / QUESTION-193 (sequential skill onset) parallel; THEORY-688 (ill-fitting options slow learning) parallel to orderings that hurt; CLAIM-761 / CLAIM-303 background; QUESTION-495 bears (the graph must be learned at a cost: Table 13 in the proceedings counts it).
- Main open doubt for the filer: the lead calls the work one that "orders training data by prerequisite skills"; it reweights a mixture, and its own sequential skill curriculum does no better than random on LEGO.

## Done
Quotes rechecked by script against both texts (all found). Final report handed back.
