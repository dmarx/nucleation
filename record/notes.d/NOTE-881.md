---
number: 881
status: Read
formerly:
- NOTE-tmpshw57
paper: LIT-1070
title: 'Sardana, Portes, Doubov & Frankle — Beyond Chinchilla-optimal: accounting
  for inference in scaling laws'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full on 2026-10-15 from the authors' arXiv preprint, version 3 (arxiv.org/pdf/2401.00448v3,
    stamped 14 Apr 2025, 16 pp.: 8 pp. of text, references, appendices A–D). arXiv
    lists three versions: v1 of 2023-12-31 (8 pp., by Sardana and Frankle only,
    "To appear in the 3rd NeurIPS Workshop on Efficient Natural Language and Speech
    Processing (ENLSP), 2023", with no training experiments), v2 of 2024-07-18 and
    v3 of 2025-04-14. v2 and v3 carry the four-author byline and the footer "Proceedings
    of the 41 st International Conference on Machine Learning, Vienna, Austria.
    PMLR 235, 2024" (as extracted); their extracted texts are identical except for
    the arXiv stamp. The ICML 2024 version proper (PMLR 235, proceedings.mlr.press/v235/sardana24a.html,
    PDF at raw.githubusercontent.com/mlresearch/v235/main/assets/sardana24a/sardana24a.pdf)
    was also fetched and diffed against v3: v3 is that paper with small edits (wording;
    one added reference, Porian et al. 2024; and Section 5's remark on poor parametric
    fits, which in PMLR concerns the "extremely long-ratio (5,000 tokens/param)"
    runs and in v3 the "150M long-ratio training results"). The tables, equations
    and numbers are the same in both. Text extracted with pdftotext. Read: abstract,
    all eight sections, appendix A (the proof of no analytic solution), B (Tables
    2 and 3 and GPU prices), C (training set-up, Table 4) and D (category results,
    by caption; the figure panels themselves were not inspected as images). Figures
    1–7 were read by their captions and the text's statements about them; curves
    were not read off the plots. Equations 2, 3, 5 and 6 are garbled by extraction
    and were reconstructed from the fragments and checked against appendix A's restatement
    (C = 6N·Dtr + 2N·Dinf). The compute-optimal numbers in Section 2, Figure 1 and
    Table 2 were reproduced independently by a numerical minimisation with the paper's
    constants (A = 406.4, B = 410.7, E = 1.69, α = 0.336, β = 0.283); all matched,
    and the reproduction exposed two typographical errors in the tables (below).
    The dollar results (Table 3) were not reproduced. Every quotation below was
    checked by script, with whitespace normalised, against the extracted v3 text,
    or, where marked, the PMLR PDF, the v1 arXiv page, or the record entries quoted.
date: '2026-10-15'
summary: >-
  Fixing a target pre-training loss and adding inference FLOPs (2N per token over
  a known lifetime demand D_inf) to training FLOPs (6N per token), the compute-minimising
  model is smaller and trained on more data than Chinchilla-optimal, increasingly
  so as D_inf approaches and exceeds the training-set size; the optimum has no closed
  form and is found numerically. The savings are modest in FLOPs (for a 30B-Chinchilla-quality
  model with 10^13 inference tokens, 28% by training 13.6B on 2.84× the data) and
  larger in dollars once inference's low hardware utilisation is priced in (17%
  to 58% in the paper's examples). 47 training runs (150M–6B parameters, 10–10,000
  tokens per parameter) find loss still falling at extreme ratios, but more slowly
  than Chinchilla-fitted laws predict, so the formula overstates the gain from long
  training. Demand is assumed known before training and fixed given quality; there
  is no term for uncertainty, discounting, obsolescence or a model being replaced.
---
<!-- inactive-ok-file: CLAIM-303 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# NOTE-881: Sardana, Portes, Doubov & Frankle — Beyond Chinchilla-optimal: accounting for inference in scaling laws

## Contribution

The Chinchilla scaling law (Hoffmann et al. 2022) chooses parameters N and training tokens D_tr to minimise loss for a training-compute budget. This paper asks the converse question with inference added: for a fixed loss ℓ and a given lifetime inference demand, which (N, D_tr) minimises training plus inference cost? "Accounting for both training and inference, how does one minimize the cost required to produce and serve a high quality model?" It answers in FLOPs (Section 2) and in dollars with hardware utilisation (Section 6), trains 47 models to check that very long training keeps improving quality (Sections 3–4), and refits the Chinchilla law on its own runs to see whether it extrapolates to extreme ratios (Section 5).

## Key insight

Loss is held fixed, so the two ways of reaching it are interchangeable in quality and differ only in when the cost is paid. A larger model reaches ℓ with less training but costs more per inference token (2N); a smaller model needs disproportionately more training to reach the same ℓ but is cheaper on every later token. Training compute is paid once and every inference token is paid per use, so expected use decides: the paper says the extra compute to train a smaller model "pays off after enough inference requests". The demand term enters the objective linearly in N, which tilts the optimum toward smaller N as D_inf grows.

## Assumptions

- **Quality is pre-training loss** under the Chinchilla third law, L(N, D_tr) = E + A/N^α + B/D_tr^β, with Chinchilla's constants (α = 0.336 and β = 0.283, De Vries's unrounded values, not the published 0.34 and 0.28). Downstream accuracy is checked against loss empirically (Fig. 3c), not assumed.
- **FLOPs are 6N per training token and 2N per inference token** (Kaplan et al. 2020), input and output tokens alike.
- **Demand is known before training.** "our analysis is predicated on the assumption that LLM practitioners can estimate their inference demand prior to training." It is a single number D_inf, the sum of tokens over all requests over the model's lifetime.
- **Demand does not depend on model size at fixed quality.** "we assume that conditioned on pre-training loss, inference demand is independent of model size and token count." A footnote concedes the opposite is plausible: "In practice, smaller models of equivalent quality may have greater demand since they can have lower inference latency."
- **Data is unlimited, compute is the constraint.** "We assume we are data rich but compute constrained", single epoch, no repeated data.
- **The dollar variant** assumes "MFU and cost per FLOP do not depend on model size, configuration, or sequence length" and leaves aside latency.
- No discounting of future cost, no model lifetime other than the demand total, no retraining, no fine-tuning or other post-training cost, no storage or serving overhead beyond FLOPs, no uncertainty in D_inf or in the fitted law.

## Key results

**The objective (Eq. 2, compute).**

N*(ℓ, D_inf), D_tr*(ℓ, D_inf) = argmin over (N, D_tr) with L(N, D_tr) = ℓ of [ T_FLOPs(N, D_tr) + Σ_i I_FLOPs(N, D_inf^(i)) ],

which with the FLOP approximations "simplifies to" (Eq. 3) argmin of 6N·D_tr + 2N·D_inf under L(N, D_tr) = ℓ. The paper calls this "the 'converse' of the Chinchilla optimization problem".

**No closed form (Theorem A.1).** With D_inf = 0 the problem is solved analytically (it is Chinchilla's). With D_inf > 0, finding N* and D_tr* analytically as functions of ℓ and D_inf "is intractable". By Lagrange multipliers, A/N^α = [3βB·D_tr^(−β) + D_inf·βB·D_tr^(−β−1)]/(3α) (Eq. 11), leaving one equation in D_tr (Eq. 12): 0 = (E − ℓ) + (βB/α + B)·D_tr^(−β) + (D_inf·βB/(3α))·D_tr^(−β−1), which with Chinchilla's constants is of the form a·x^(−1.283) + 756.6·x^(−0.283) + c = 0, "which is not possible in general" to solve analytically. The optimum is found numerically "using the Newton root-finding method", which "converges for relevant inputs". The proof shows that this route gives no closed form; "not possible in general" is asserted for the equation family, not proved.

**How the optimum shifts with demand (compute; all reproduced here).**

- Low demand: "When inference usage is significantly less than the number of pre-training tokens, Chinchilla models are essentially compute-optimal."
- 7B-Chinchilla quality (loss 2.13; 7B on 276B tokens), D_inf = 10^11 tokens: "train a 6B parameter model on 1.18× the original (Chinchilla-prescribed) amount of data". The saving is under 1% (0.86% by the reproduction; the paper does not state it).
- 13B quality, D_inf = 2×10^12 tokens (Figure 1): train a 7B model instead, saving 1.7 × 10^22 FLOPs (17%). The reproduction gives 6.97B on 1.25T tokens (2.16× the Chinchilla 577B, about 179 tokens per parameter).
- 30B quality, D_inf = 10^13 tokens: "reduce their total FLOPs by 28% by training a 13.6B model on 2.84× the data" (about 325 tokens per parameter).
- "For higher quality models (i.e. models that are larger and/or trained for longer), the volume of inference demand required to shift the scaling law increases".
- Table 2 (inference tokens; Chinchilla model → compute-optimal model; FLOP reduction): 50B, 1B on 27.4B → 633M on 46.8B, 9.1%; 200B, 7B on 276B → 5.4B on 367B, 2.6%; 1T, 13B on 577B → 8.32B on 967B, 8.5%; 5T, 30B on 1.56T → 16.4B on 3.27T, 16%; 10T, 70B on 4.26T → 41.6B on 7.92T, 12%. The table prints the first compute-optimal size as "6.33M"; that model would have loss 4.19, not 2.53, and 633M reproduces the row, so it is a typographical error.
- Inference-heavy regimes call for "up to thousands of tokens per parameter".
- Break-even between two fixed designs, worked here from the paper's objective (the paper states it only in words): for the 13B-quality target, a 7B model needs 1.24T training tokens, 7.1×10^21 more training FLOPs than 13B on 577B, and saves 2×6×10^9 FLOPs per inference token, so it pays after about 5.9×10^11 inference tokens. A 10B model costs 1.06×10^21 extra and pays after about 1.8×10^11.

**The dollar variant (Eqs. 5–6).** Training and inference FLOPs are divided by their model-FLOPs utilisations and multiplied by a cost per FLOP: argmin of (C_tr/MFU_tr)·6N·D_tr + 2N·C_inf·(D_inp/MFU_inp + D_out/MFU_out). Settings: training and prompt tokens at 50% MFU, generated tokens at 1% ("MFU can be as low as ~1% for inference"); 70 input and 215 output tokens per request (LMSYS-Chat averages); training on A100-80GB at $1.50/hr, inference on A100-40GB at $1.10/hr after INT8 quantisation. Results:

- 30B-Chinchilla quality, 1.5B requests: "reduce costs by 17% by instead training a 16B model on 3.35T tokens."
- Same demand of 2T tokens (7.02B requests) at 70B quality: Chinchilla-70B "requires only 1.3% extra FLOPs compared to an equal-quality compute-optimal model, but costs 36% more than a cost-optimal model", attributed to "the 50× lower MFU of each inference output token compared to training". (The 1.3% was reproduced.)
- Table 3 (requests; Chinchilla → cost-optimal; savings): 175M requests, 1B → 327M on 152B, 50%; 702M, 7B → 2.90B on 929B, 34%; 3.51B, 13B → "430B" on 3.1T, 49%; 17.5B, 30B → 8.58B on 12.1T, 58%; 35.1B, 70B → 21.5B on 27T, 54%. The 13B row's "430B" must be 4.30B: 4.30B parameters on 3.1T tokens has the row's loss of 2.05, and a 430B model would be larger than the model it replaces. The cost-optimal models run to roughly 300–1,400 tokens per parameter.

**The training runs.** 47 MPT-style models, 150M, 370M, 750M, 1.3B, 2.5B and 6B parameters, at 10 to 10,000 tokens per parameter (Table 4: the 150M at twelve ratios up to 10,000; 370M up to 1,000; 750M up to 500; 1.3B up to 250; 2.5B up to 500; 6B at 20 only), single epoch, on trillions of tokens of web text and code, evaluated on loss and a 29-task "Evaluation Gauntlet" in five categories.

- "loss does not plateau as we scale to 10,000 tokens per parameter for our 150M model"; for larger models, tested only up to 1,000, "we also see no evidence of loss flat-lining".
- Downstream: the Gauntlet average rises with tokens per parameter, with "no evidence of a 'saturation' point", and loss and Gauntlet average "are tightly correlated".
- On loss against FLOPs, for ratios ≥ 20 the trend lines "are nearly parallel": loss falls "at similar rates for each additional FLOP regardless of whether training occurs in the standard Chinchilla regime or at extreme ratios (500 tokens/param)".
- No support for De Vries's critical model size (a size below which no amount of data matches a Chinchilla model), "although further testing is needed at extreme scales".

**The refit (Section 5, Table 1).** Fitting the Chinchilla form to its own runs restricted to ≤100, ≤250, ≤500 tokens per parameter and to all data gives progressively flatter curves (α 0.08 → 0.18, β 0.13 → 0.24, E 0.17 → 1.45, against Chinchilla's 0.34, 0.28, 1.69). "if we only use data from typical token ratios to determine our scaling law coefficients, we will overestimate the impact of additional training data". Models "continue to learn at extreme training durations, they do so more slowly than scaling laws predict", and none of the fits matches the 150M long-ratio runs. The paper does not rerun its Section 2 optimisation with the refitted coefficients, so how much the headline shifts shrink is not stated.

## Bearing on the record

**On [QUESTION-095](../questions.d/QUESTION-095.md): a worked, quantitative case of the first strategy, precompute and leave a result, with expected reuse as an explicit term. It has none of the other terms the question's note says a single account needs.**

- The trade is the question's in its simplest form. Training is paid once, before any request; each inference is paid per use; more up-front work buys a cheaper per-use cost, and expected use, D_inf, sets the optimal split. The paper's own framing is amortisation in all but name: the extra training "pays off after enough inference requests", and the result is a model "optimal over their total lifetime". It is not the retrieval half of the question: nothing is stored and read back. What the up-front work leaves is a cheaper computation (a smaller network), not a looked-up answer. In the question's table it sits nearest "maintain structure that makes search cheap", except that the structure is built once and not maintained.
- **Query predictability.** Partly present, in the form of an assumption. Individual queries are not predicted at all; the model serves whatever comes. What must be predictable is the volume, and the analysis is "predicated on the assumption that LLM practitioners can estimate their inference demand prior to training". It is the cockpit's case with respect to amount (known in advance) and the opposite of it with respect to content.
- **Retrieval cost.** Present and non-zero: 2N FLOPs per token, or in the dollar variant 2N·C_inf/MFU per token, with generation at 1% utilisation. The cheap route costs per use; what the trade buys is a smaller per-use cost, not a free one. The dollar variant shows that the per-use cost's real price (utilisation, quantisation, different hardware) matters more than its nominal FLOPs: 1.3% in FLOPs is 36% in dollars.
- **Staleness.** Absent. Nothing in the model makes a trained network less fit for later queries: no distribution shift, no knowledge cut-off, no replacement by a better model, no lifetime other than the token total. Loss is held fixed for the whole demand. The nearest thing is a passing reference to Llama 2 and Llama 3 being trained on far more data, which is about training practice, not obsolescence.
- **Uncertainty about future demand.** Absent from the model. D_inf enters as a known constant, there is no distribution over it, no expected-cost or regret analysis, and the paper does not say which way to err. The footnote that smaller models may attract more demand names a feedback from the choice to the demand and sets it aside.
- **Expected reuse.** Present, and it is the whole of the paper's addition: D_inf, total lifetime tokens.
- **Erosion of the alternative.** Absent; it has no meaning here, since the larger model is a design not chosen, not a skill that decays.
- **Error in the cost model itself.** The paper's own Section 5 is a version of the record's worry about reusing a stale conclusion, at the level of the forecast rather than the stored result: coefficients fitted at ordinary ratios "overestimate the impact of additional training data" at extreme ones, so the optimiser, which pushes toward extreme ratios, does so on its least reliable ground.

**On [CLAIM-303](../claims.d/CLAIM-303.md): the claim's break-even is this paper's trade with c_a and u set to the per-use cost of the cheap route and zero, and the paper's numbers instantiate it.**

- Compare two designs at the same loss. F is the extra training, 6(N_s·D_s − N_c·D_c); c_r per token is the large model's 2N_c; c_a is the small model's 2N_s; u is 0. The claim's n > F/(c_r − c_a − u) becomes D_inf > 3(N_s·D_s − N_c·D_c)/(N_c − N_s). For a 13B-quality target, 7B pays after about 5.9×10^11 inference tokens (worked here, not stated in the paper). So the claim's arithmetic holds in this domain, which it calls "trivial", and the paper adds what the claim does not have: the up-front cost and the per-use saving are not independent parameters but are tied by a production function (the scaling law), so the question is not whether to file but how much to precompute, a continuous choice whose optimum moves smoothly with n.
- The claim's distinctive terms are missing here. There is no upkeep u, no verification in c_a, and no cost of "incorrectly reusing an obsolete argument". So the paper supports the claim's break-even form and expected-reuse criterion, and says nothing for or against its thesis that staleness and upkeep keep recurrence from being the criterion.
- One narrowing. The claim treats reconstruction cost c_r as fixed. Here the alternative to precomputing more is not reconstruction from nothing but a different amount of precomputation, so whether to file is the endpoint of a dial. The record's second-occurrence rule is a binary approximation to what is, in this case, a continuous allocation.

**On [LIT-1070](../literature.d/LIT-1070.md).** The entry's summary ("with enough expected queries a smaller model trained longer is cheaper overall") is accurate. Two corrections: v1 (2023-12-31) is a two-author workshop paper (Sardana and Frankle, NeurIPS 2023 ENLSP) without the experiments; the four-author paper is v2 (2024-07-18) onward, the ICML 2024 paper (PMLR 235). The `published:` date of 2023-12-31 is v1's.
