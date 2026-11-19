# Reader notes: Wang, Mittal, Song, Jia, "Data Shapley in One Training Run" (arXiv 2406.11011v3, ICLR 2025)

## 2026-11-19 copy located and read
- arxiv.org/pdf/2406.11011 (v3, 7 Jun 2025), 38 pp, fetched without obstruction. Text extracted to the reader's scratchpad (not committed).
- Read in full: Abstract, Sec 1-6, App A.2-A.3, B, E.1-E.5. Skimmed: proofs (C), ghost techniques (D), E.6.
- What is measured: per-step Shapley value of a training point toward the loss change on a validation point, under a first- or second-order Taylor approximation of the one-step loss change; summed over steps. First-order = TracIN-Ideal ("equivalent to the TracIN-Ideal score", Sec 4.1). Second-order adds a within-batch interaction term.
- Model/data: GPT2 (124M) and Pythia-410M on the Pile; batch 16, seq 1024, AdamW in training but SGD formulas as proxy (App E.1, Remark 7).
- Sec 5.3.2: one math validation corpus, second-order value, domain composition over first 10,000 iterations (figure x-axis to ~5000). ArXiv dominates; Pile-CC "initially shows positive contributions during the first few iterations. However, its value quickly drops to negative and eventually converges to zero." No order intervention.
- App E.4: average per-point value shrinks toward zero over steps; "Data points introduced in later stages of training contribute less".
- Doubt: the intro's "later stages ... domain-specific corpora becomes dominant" overstates Fig 3, where ArXiv dominates from early on; what changes is Pile-CC dropping out. Also ~10k steps x 16 x 1024 is ~164M tokens: very early in training.
- Key structural point for the lead: the measure is local per step (gradient alignment at that step), so it cannot credit early data for making later learning easier; it is not a test of facilitation.

## 2026-11-19 figure checked, bearings searched
- Fig 3 (p. 9), read visually from a render: Pile-CC about a fifth of the positive value at step 0, gone by roughly 800 steps (inside the 2000-step warmup); ArXiv about 55-60% thereafter; Github about 15-20% throughout; PubMed Central about 15%. x-axis ends near 5000 though the text says 10,000. Percentages exclude negative-total domains, so "drops to negative" means Pile-CC leaves the chart.
- Fig 11 (App E.4): per-domain average value per point falls toward zero over 10k steps for every domain; the authors read it as order-dependence of value (diminishing returns), not facilitation.
- Record: no LIT for 2406.11011; no entry on data valuation/Shapley/TracIn in the ML sense (Shapley hits are game-theory: QUESTION-354, TERM-076/077, THEORY-896).
- Bearings: CLAIM-756 (background; the measure cannot see the claim's effect by construction), QUESTION-039 (parallel), TERM-131 (background: In-Run value is a per-step counterfactual within one run), CLAIM-596 (parallel: per-step value, like yields, cannot tell facilitation from head start), THEORY-279 (parallel), THEORY-tmpd6smn, THEORY-tmpd6l4a, THEORY-tmp0lbb1, THEORY-tmpk9cmk (background/qualify the owner's recollection), CASE-294.
- Verdict for the lead: this is not the owner's recalled result. It measures immediate gradient alignment of Pile-CC with a math target, not later ease of learning; no order intervention.
