# Reader notes, in flight: prepretrain (removed when filed)

Hu, Petty, Shi, Merrill and Linzen, "Between Circuits and Chomsky", arXiv 2502.19249.

## Copies (2026-11-19)
- arXiv abs page: v1 26 Feb 2025, v2 27 May 2025, comment "ACL 2025 Camera Ready". Read v2 PDF (arxiv.org/pdf/2502.19249v2), 19 pp, text extracted with pdftotext.
- ACL Anthology: 2025.acl-long.478, pp. 9691-9709, DOI 10.18653/v1/2025.acl-long.478 (venue verified; anthology PDF not read, v2 is the camera-ready).
- Semantic Scholar API: 429 rate limit, stopped. Code repo on GitHub: 403 from fetch, not needed.

## Reading, step 1: body and appendix read
- 33% (1B run, §6): baseline's final loss reached "after training for only 1.10B total tokens"; efficiency formula in §3.1 counts the pre-pretraining steps ("6,000+500"). So counted including the pre-pretraining tokens (500 steps, ~0.03B).
- Doubt: the 1B MRS 17.3 uses 1.63B-1.10B over 0.03B, treating 1.10B as pretraining tokens, while the efficiency treats it as total. Small inconsistency.
- Control that matters: C4 pre-pretraining (matched natural-language tokens, with a second LR warmup). Table 5 (160M): MRS k-Shuffle Dyck 7.15 vs C4 6.65; LM loss 3.741 vs 3.754. Most of the saving over no-pre-pretraining is had by natural-language pre-pretraining too: a schedule effect is not excluded. The 33% at 1B is against no pre-pretraining only.
- ww (copy language) hurts: MRS -0.25; random binary/ints hurt. Hierarchy criterion.
- Mechanism (§5): heads found by pruning the pre-pretrained model (50% of heads), mean-ablated after pretraining. M beats random and complement (p << 0.001). Shows the heads persist in importance; does not show they cause the saving (no ablation before pretraining, no matched no-ppt model comparison). Largest BLiMP drops are morphology (Fig 9), which the authors call least related to dependency processing.

## Step 2: venue and quotes
- ACL 2025 verified on the ACL Anthology volume page (2025.acl-long.478). 40 quotes checked by script against the downloaded text: all found.
- More doubts: at 160M only k-Shuffle Dyck beats C4 pre-pretraining on MRS (7.15 vs 6.65); 1-Dyck 3.01 and k-Dyck 3.57 are below it. LM loss gaps to C4 are inside the reported spreads (3.741 +/- 0.014 vs 3.754 +/- 0.017). Pre-pretraining (500 steps) lies wholly inside the 1,000-step warmup (App. B).

## Step 3: bearings searched
- Named: CLAIM-756 supports (premise in cost terms, first phase counted); CLAIM-754 parallel (ww and random strings: a first phase can raise the later cost); CLAIM-762 leaves open (analogy at most); TERM-117 the whole phase passes the comparator test, the heads do not (association after the fact, not an intervention on establishment); TERM-131 background; LEAD-tmphfbq0 still needed: no matching on first-phase performance and no disruption of the heads before natural-language training. Metamer control is a partial version of its shortcut arm.
- Found: CLAIM-758 (optimal duration, then harmful: a parallel, without held-capability floor), THEORY-967 (Dyck head in a small transformer, parallel), THEORY-997 (reuse of components), QUESTION-039, THEORY-2046 (MAML, authors cite meta-learning), THEORY-tmpw8s3h (ULMFiT, comparison of cost accounting), QUESTION-495, CASE-294.
