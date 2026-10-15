---
status: Read
paper: LIT-tmpk7x9f
title: Snell, Lee, Xu & Kumar — Scaling LLM test-time compute optimally
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 in two versions. (1) The arXiv preprint, arxiv.org/pdf/2408.03314,
    which is v1 (submitted 2024-08-06, 37 pp.); the arXiv abstract page and the
    arXiv API both list v1 as the only version, so v1 is the latest arXiv version.
    (2) The ICLR 2025 conference version, open access in the ICLR proceedings (proceedings.iclr.cc/paper_files/paper/2025/hash/1b623663fd9b874366f3ce019fdfdd44-Abstract-Conference.html,
    PDF .../file/1b623663fd9b874366f3ce019fdfdd44-Paper-Conference.pdf, 35 pp.),
    retitled "Scaling LLM Test-Time Compute Optimally Can be More Effective than
    Scaling Parameters for Reasoning". The two do not match: the ICLR version is
    a revision that was never posted to arXiv (differences listed under Key results).
    Text extracted with pdftotext; Figure 1 and the FLOPs-matched figure (v1 Figure
    9, ICLR Figure 8) were also read from page images at 110–130 dpi, and the bar
    labels of Figure 1 were checked against the extracted text of both PDFs, which
    agree. Read: all main sections and all appendices of both versions. Skimmed:
    the appendix figures of sample model outputs (v1 Figures 17–29, ICLR Figures
    20–32), captions only. OpenReview refused requests from this environment (challenge
    page), so reviews were not read; OpenAlex and Semantic Scholar were rate-limited.
    Every quotation below was checked against the extracted text of the version
    named, by script, with whitespace normalised. Section and figure numbers are
    v1's unless marked ICLR.
date: '2026-10-15'
summary: >-
  On MATH with PaLM 2-S*, which way of spending test-time compute works best (beam
  search against a process reward model versus best-of-N; sequential self-revision
  versus parallel sampling) depends on how hard the question is for the base model,
  and choosing the method per difficulty bin matches best-of-N with up to about
  4× less test-time compute (the discussion says 2–4×). In a FLOPs-matched comparison
  with a ~14× larger model, the extra test-time compute a small model may spend
  is set by R, the ratio of total inference tokens to pretraining tokens: when R
  is small the larger model's pretraining cost buys many samples per query and test-time
  compute wins on easy and medium questions; when R is large the budget per query
  falls toward the parameter ratio and the larger model wins, always on the hardest
  questions. Difficulty estimation (2048 samples per question) and verifier and
  revision-model finetuning are not counted in the compute, R is an aggregate token
  ratio with no term for which queries recur, and the evidence is one model family
  on one benchmark of 500 test questions.
---

# NOTE-tmpeazah: Snell, Lee, Xu & Kumar — Scaling LLM test-time compute optimally

## Contribution

An empirical study of how to spend inference compute on a single prompt, framed as two "knobs" on the model's output distribution: changing the proposal distribution (a model finetuned to revise its own previous attempts, sampled sequentially) and searching against a verifier (a process reward model, PRM, used for best-of-N, beam search or lookahead search). It defines a per-prompt "test-time compute-optimal scaling strategy", approximates it by choosing the best hyperparameters per bin of estimated question difficulty, and then asks whether such test-time compute can substitute for pretraining a larger model when the total FLOPs of pretraining plus inference are held equal.

## Key insight

No single way of spending inference compute is best; the best one depends on how far the question is from what the base model can already do. Where the first samples are near right, local refinement (sequential revision) pays and stronger search over-optimizes the verifier; where they are far off, broad parallel sampling or tree search pays; where the model almost never gets it, nothing at test time helps much. And whether inference compute beats a bigger model depends on how much inference there will be: the bigger model's pretraining cost is paid once, the small model's extra sampling is paid on every query.

## Assumptions

- **One model, one benchmark.** PaLM 2-S* (Codey) on MATH, the 12k-train / 500-test split of Lightman et al. The authors chose math because they "expect test-time compute to be most helpful when models already have all the basic “knowledge” needed to answer a question, and instead the primary challenge is about drawing (complex) inferences from this knowledge." The ICLR version adds PaLM 2-S and PaLM 2-M for the beam-search-by-difficulty analysis only (ICLR Fig. 16) and cites later reproductions by others; the core results remain PaLM 2-S*.
- **Capability-specific finetuning.** Both mechanisms use finetuned models: a PRM trained from Monte Carlo rollouts (Wang et al.'s method, 16 rollouts per step), and a revision model trained on post-hoc chains of up to four incorrect answers followed by a correct one, with an ORM trained on the revision model's outputs for selection. Footnote 1: "Capability-specific finetuning is necessary to induce revision and verification capabilities into the base model on MATH". Finetuning FLOPs are not counted (ICLR footnote: "negligible compared to pretraining FLOPs").
- **Compute counted in generations.** A generation is one sampled answer; beam search with N beams costs N, lookahead costs N × (k + 1). v1 does not count verifier calls; the ICLR version says verifier queries add "a 2x overhead" and that it accounts for it.
- **Difficulty is the base model's.** "we bin the model’s pass@1 rate – estimated from 2048 samples – on each question in the test set into five quantiles". Oracle difficulty uses ground-truth correctness; predicted difficulty bins the PRM's averaged final-answer score over the same 2048 samples. The compute for this is not counted: "our experiments do not account for this cost largely for simplicity". Appendix C: "Technically this procedure is extremely costly because it requires generating many samples."
- **Strategy chosen per bin, not per prompt.** The best setting is picked per difficulty bin, by two-fold cross-validation within each bin of the test set (v1); the ICLR version describes it as estimated "on a validation set" / "using a held-out set" and applied to test questions.
- **The pretraining side scales parameters only.** "We focus on the setting in which model parameters are scaled up and training data amount is fixed", as in LLaMA; Chinchilla-style joint scaling is left to future work. The larger model is not named; it has "∼ 14 times more parameters" and is evaluated by greedy pass@1 with no test-time compute.
- **FLOPs approximations.** Pretraining X = 6N·D_pretrain; inference Y = 2N·D_inference in v1, 4N·D_inference in ICLR ("multiplies the standard 2N Dinference by two to account for the overhead of calling the verifier"). D_inference is "the total number of tokens generated at inference time", over the model's use.
- **The same per-query budget for every query.** In the FLOPs-matched comparison each difficulty bin is plotted separately, and the matched budget is one number applied to all queries; there is no mixture of easy and hard queries sharing a budget.

## Key results

**The two mechanisms (§§5–6).**

- *Search against a PRM.* Best-of-N weighted (sum the PRM's last-step score over samples with the same final answer), beam search (N beams, keep the top N/M steps by PRM score, expand each M ways, up to 40 rounds), and lookahead search (beam search scoring each step by the PRM at the end of a k-step greedy rollout). Beam search beats best-of-N at small budgets and falls below it at large ones; lookahead underperforms at equal cost. The authors attribute the falloff to exploiting the PRM: repetitive low-information steps, or "overly short solutions consisting of just 1-2 steps". By difficulty (Fig. 3 right, budgets 4–256): on bins 1–2 beam search "degrades performance as the generation budget increases"; on bins 3–4 it "consistently outperforms best-of-N"; on bin 5 "no method makes much meaningful progress." Takeaway box: "beam-search is more effective on harder questions and at lower compute budgets, whereas best-of-N is more effective on easier questions and at higher budgets."
- *Revisions of the proposal distribution.* Pass@1 rises along a revision chain, past the four steps trained for. About 38% of correct answers get revised into incorrect ones, so the answer is chosen from the chain by an ORM or majority vote. Sequential revisions "narrowly" beat parallel samples at equal count. At a fixed budget there is a best sequential-to-parallel ratio, and it moves with difficulty: "easier questions benefit from purely sequential test-time compute, whereas harder questions often perform best with some ideal ratio of sequential to parallel compute."

**Compute-optimal allocation by difficulty (§3).** Defined as θ*(q, N) = argmax_θ E_{y∼Target(θ,N,q)}[1{y = y*(q)}], the hyperparameters maximizing accuracy on prompt q at budget N. Approximated by treating difficulty as "a sufficient statistic of a question when designing the compute-optimal strategy": five bins, best setting per bin. Predicted and oracle bins give largely overlapping curves.

**The >4× claim.** The abstract says "more than 4×" over best-of-N; the body is more hedged. Revisions (Fig. 8): "compute-optimal scaling can outperform best-of-N using up to 4x less test-time compute (e.g. 64 samples verses 256)". PRM search (Fig. 4): "can nearly outperform best-of-N using up to 4x less test-time compute (e.g. 16 verses 64 generations)", with the predicted-difficulty gains shrinking at higher budgets. Discussion: "a factor of 2 − 4×". The ICLR version keeps "more than 4×" in the abstract, gives the revision example as "128 samples versus 512" in the Figure 6 caption while the text keeps "64 samples versus 256", and the PRM Figure 4 caption says "32 versus 128" while the text says "16 versus 64". These gains exclude the 2048-sample difficulty estimate.

**The FLOPs-matched comparison and R (§7).** The question: a model pretrained with X FLOPs will run Y FLOPs of inference; with M(X + Y) total FLOPs, spend the increase on a larger model or on test-time compute? Multiplying parameters by M multiplies both pretraining and inference FLOPs by M (the larger model also costs M× per greedy token). To match, the small model's inference compute is multiplied by M + 3(D_pretrain/D_inference)(M − 1) in v1, and by M + (3/2)(D_pre/D_inf)(M − 1) in ICLR. "We refer to the inverse of this ratio as 𝑅 (e.g. 𝐷𝐷inference )" [v1, fraction garbled in extraction: R = D_inference / D_pretrain]. Writing the v1 multiplier as M + 3(M − 1)/R (my rearrangement) shows the amortization: the larger model's added pretraining cost, 6(M − 1)N·D_pretrain, is spread over all inference tokens, so the per-query test-time budget it buys is large when R is small and shrinks toward M as R grows. With M ≈ 14 this gives about 258×, 63× and 16× the greedy budget for v1's R = 0.16, 0.79 and 22, which matches the star positions at 2^8, 2^6 and 2^4 on the figure's x-axis (my calculation; the paper gives only the R values and says "each ratio corresponding to an inference budget"). The ICLR version's R values are 0.08, 0.40 and 11, half of v1's because inference FLOPs were doubled for the verifier; the stars sit at the same budgets. The paper links R to use: "in many large scale production settings, we may expect significantly more inference tokens than pretraining tokens, in which case we would have 𝑅 >> 1", while self-improvement setups that generate their own training data give R << 1.

**Where test-time compute wins and loses.** Figure 1 (right), relative accuracy change from test-time compute versus the ~14× model, both versions identical:

| | R << 1 | R ≈ 1 | R >> 1 |
|---|---|---|---|
| Revisions, easy | +21.6% | +16.7% | +5.4% |
| Revisions, medium | +27.8% | +3.5% | −24.3% |
| Revisions, hard | +11.8% | −11.9% | −37.2% |
| PRM search, easy | +19.1% | +2.2% | +2.0% |
| PRM search, medium | −5.6% | −35.6% | −30.6% |
| PRM search, hard | 0.0% | −35.3% | −52.9% |

(Easy/medium/hard in Figure 1 are not mapped to the five bins in the text.) In Figure 9, by bin: "if we only expect to see very difficult questions (e.g. difficulty bins 4/5) or have a larger 𝐷inference (corresponding to a larger 𝑅 value), then it is often more effective to allocate our budget towards pretraining", and test-time compute is better for "mostly easy or intermediate difficulty questions (e.g. bins 1/2/3 and sometimes 4) or have lower inference requirements". Takeaway: "Test-time and pretraining compute are not 1-to-1 “exchangeable”." The abstract's 14× claim is limited to "problems where a smaller base model attains somewhat non-trivial success rates". v1's introduction says test-time compute is often preferable on "even hard questions (depending on the specific conditions on the pretraining and inference workload)"; the ICLR introduction drops that clause.

**Added in the ICLR version.** The verifier-overhead accounting above; a verifier-quality test of the §7 comparison (ICLR App. K, Fig. 17): majority voting with the base model "generally under-performs the larger pretrained model", a PRM with 20% label-flip noise still wins on easy/medium questions at low inference load, and majority voting over the revision model's samples wins on easy and medium questions with no verifier; PaLM 2-S/2-M replication of the beam-search-by-difficulty pattern; an explicit limitation that "it is unclear to what extent our findings generalize beyond math and easily verifiable domains"; and a note of later reproductions (Beeching et al.; Liu et al. 2025) on open models and AIME 2024, not read here.

## Bearing on the record

**On [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md): this paper prices the machine-learning version of the trade, with expected reuse in it and most of the record's other terms left out.**

- **It is an amortization model, with R as the reuse term.** Pretraining a larger model is computation done before any request and carried by every later query; test-time compute is done per query, at the moment of use. The FLOPs match makes the fixed cost of the larger model's extra pretraining buy test-time compute in proportion to 1/R. So the paper's conclusion that "the scale of test-time compute we can apply is dependent on this ratio" is the record's "worth it when expected reuse covers it", stated in FLOPs. The coordinator's brief called R "the expected number of inference queries"; it is not. R is total inference tokens over pretraining tokens, a volume, with queries and tokens per query multiplied together and nothing about which queries recur. Reuse here is reuse of a capacity across a query distribution, not of a stored result for a repeated query.
- **Query predictability enters as difficulty, and it decides the answer.** Test-time compute wins where the base model already has "somewhat non-trivial success rates", meaning where the query falls near what was precomputed, and loses on the hardest bins at every R tested (PRM search: 0.0% to −52.9%; revisions: +11.8% only at R << 1). Read in the record's terms: per-query computation helps when the stored capacity is nearly enough for the query, and does not substitute for it when the query is outside it. That is the reverse of the cockpit case, where the precomputed result is cheap to use because the query is fixed and known. The paper does not frame it so; this is the record's reading.
- **Retrieval is not free in this model.** The larger model costs M times as much per inference token, so the "store" has a read-back cost that grows with what was stored. This is a retrieval-cost term of the kind [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) asks for, and it is built into the multiplier (the leading M). Amortized-inference models in the record's other readings give retrieval no cost.
- **Costs left out, which narrow its use for a single account.** The per-query difficulty estimate (2048 samples, more than any budget compared) is a cost of predicting the query and is not counted; the authors call it an exploration–exploitation tradeoff and future work. The finetuning of the PRM and revision model is itself up-front computation, also not counted. There is no staleness term (a fixed benchmark, a fixed model) and no erosion term. So of the record's list (query predictability, retrieval cost, staleness, expected reuse, erosion of the alternative), the paper models expected reuse as aggregate volume and retrieval cost as per-token model size, measures query predictability without pricing it, and omits staleness and erosion.
- **Its limits as evidence.** One model family, one math benchmark of 500 test questions, a larger model that scales parameters at fixed data, a compute-optimal policy chosen per bin on the evaluation distribution, and R values that halved between versions under a changed accounting convention. The direction of the result (more inference volume favours up-front compute; harder queries favour up-front compute) is better supported than any crossover point.
- **The converse is named and not done.** The future-work section proposes distilling test-time outputs back into the base model, which is turning per-query computation into amortized computation. That is the owner's trade run in the other direction; the paper does not study it.
