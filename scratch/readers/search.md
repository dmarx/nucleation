# Search notes: LEAD-tmphfbq0 (task composition, matched first stage, intervention on g)

## Step 1: setup
Read the lead. Already in record per lead: Hu et al. (formal-language pre-pretraining, NOTE-tmpm4pxy), Petty et al. (code, THEORY-tmpq9sev), procedural pretraining (THEORY-tmpmy98s), Papadimitriou & Jurafsky (THEORY-tmpf6s7m).
Plan: verify candidate ids via arXiv API; web search for uncertain ones; check record for each.

## Step 2: ML candidates, identifiers verified via arXiv API (titles, authors, dates, abstracts)
Verified: 2402.05785 Thomm+ (samples to learn composition vs relearning subtasks); 2310.10899 Zhang/Lepori/Pavlick (Subtask Induction: transplant subnetwork, data efficiency); 2601.09049 He+ (grokked vs non-grokked, transfer); 2504.13292 Xu+ GrokTransfer (embedding transfer removes delay); 2506.13253 Lee/Lampinen/Singh/Saxe (subtask curricula in ICL); 2209.07431 Ito+ (primitives pretraining -> sample-efficient learning); 2405.05409 Zhang+ (init scale: inferential vs memorizing solutions to composite functions); 2405.15071 Wang+ grokked implicit reasoners; 2505.23683 Wang+ k-fold composition easy-to-hard; 2402.16726 Furuta+ (transfer among grokked modular ops, ablation); 2311.12786 Jain+ (wrappers, sample-efficient revival); 2211.08422 Lubana+ mechanistic mode connectivity; 2106.05418 Gerace+ (transfer of feature map, shared latent); 2006.11650 Tripuraneni+; 2002.09434 Du+; 1809.10374 Lampinen&Ganguli; 2006.10455 Maennel+ (random-label pretraining trains faster downstream); 2410.05464 Panigrahi+; 2311.12997 Ramesh+; 2310.09336 Okawa+; 2409.19808 Zhao+; 2312.15001 Schug+; 2301.10884 Lepori+; 2402.14811 Prakash+; 2310.08744 Merullo+; 2505.22308 Shinnick+ (procedural pretraining; likely THEORY-tmpmy98s, check); 2510.00475 Gu&Shi (shortcut rigidity, adaptation delay); 2601.22510, 2604.08510, 2606.18089 (weak).

## Step 3: neuro/cog candidates (Crossref + PubMed verified)
- Goudar, Peysakhovich, Freedman, Buffalo, Wang 2023 Nat Neurosci doi:10.1038/s41593-023-01293-9 (PMC11559441): "its reuse in new problems facilitates learning by limiting connection weight changes".
- Driscoll, Shenoy, Sussillo 2024 Nat Neurosci doi:10.1038/s41593-024-01668-6 (PMC11239504): "Motifs were reconfigured for fast transfer learning after an initial phase of learning."; pretraining lacking the anti motif -> slower learning of MemoryAnti; only new rule-input trained.
- Tse et al. 2007 Science doi:10.1126/science.1135935: "systems consolidation can occur extremely quickly if an associative "schema" ... has previously been created".
- Harlow 1949 Psychol Rev doi:10.1037/h0062474: metadata only (no abstract available); content not verified.
- Sagiv/Musslick/Niv/Cohen arXiv 2007.03124 (to verify).
Record check: none of the step-2/3 ids in literature.d except 2211.08422 (LIT-669). Record holds Skill-it!, procedural pretraining 2601.21725 (LIT-tmpb6e1c), grokking papers.

## Step 4: section checks on top candidates (arXiv HTML)
- 2310.10899 Zhang/Lepori/Pavlick: subtask S1 = a*b mod 7; T1 = a+ab, T2 = a^2+ab (shared g). Subnetwork for S1 found by mask in T1 model, transplanted frozen into fresh model trained on T2; controls full-model transfer, random same-size subnetwork, scratch; cost = disambiguating samples. "a randomly sampled subnetwork requires on average around 6 times as much data in order to reach perfect generalization accuracy". Best design match (a, partial c); no organization arm.
- 2601.09049 He+: grokked vs "fake grokked" models at "comparable performance on original OOD facts", fine-tuned on 2,000 new atomic facts; "models still require either (i) an additional grokking phase, or (ii) substantially more finetuning data". (a qualitative, b approximate, no weight intervention.)
- 2402.05785 Thomm+: joint training, no staged pretraining; "LLaMA obtains no significant benefit from learning the sub-tasks"; cost = samples to near-perfect accuracy.
- 2209.07431 Ito+: primitives pretraining; vanilla needs up to 4.23x more samples; no lesion.
- 2402.16726 Furuta+: frozen pre-grokked embedding or transformer, min training fraction to grok; transfer "limited to specific combinations".
- 2506.13253 Lee+: no cost comparison, correlational probes only -> weak.
- Also verified: 2007.03124 Sagiv+, 2007.07732 and 2207.00429 Mendez+, 2410.08194 Tahir+, 2007.10527 Ravi+. None in record.
Conclusion: no work runs the full design (matched first stage across organizations + later cost + intervention on g).
