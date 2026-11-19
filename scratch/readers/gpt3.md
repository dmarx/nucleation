# Reader notes: gpt3 (Brown et al., "Language Models are Few-Shot Learners")

## Step 1: identifier and copy (2026-11-19)
- arXiv API (export.arxiv.org, no email): id 2005.14165, latest v4 (updated 2020-07-22), published v1 2020-05-28T17:29:03Z. Title matches.
- Copy: https://arxiv.org/pdf/2005.14165v4 (arXiv, the authors' preprint), HTTP 200, 75 pages. Text extracted with pdftotext; kept in my scratchpad, not here.
- Named codes read: CLAIM-756, CLAIM-754, CLAIM-758, TERM-131, QUESTION-493, CASE-294; the lead LEAD-tmpn5ruw.

## Step 2: §§1-3.8 read (pp. 3-21)
- Fig. 1.1 caption defines ICL as the inner loop "which occurs within the forward-pass upon each sequence". Footnote 1 (p. 4): terms "intended to remain agnostic" on learning new tasks vs recognizing patterns seen in training.
- Fig. 1.2 caption (p. 4): "Larger models make increasingly efficient use of in-context information." Measured on symbol removal; accuracy against K, by size. That is accuracy-at-K, not K-to-threshold.
- §2 (pp. 6-7): FT "involves updating the weights"; FS: "no weight updates are allowed". Settings framed as "a spectrum of how much task-specific data they tend to rely on".
- §3.7 (p. 20): "GPT-3 requires less than eight total examples per task to outperform a fine-tuned BERT-Large" (125K fine-tuning examples): closest thing to a cost-to-level comparison, across systems, not across pretraining.
- Cases where few-shot hurts: LAMBADA smallest model -20% with fill-in-blank few-shot (§3.1.2); one-shot always worse than zero-shot there; Winograd no clear ICL; ARC/PIQA flat; WiC at chance.
- No fine-tuning of GPT-3; no pretraining-length variation; scale = model size at fixed 300B tokens.

## Step 3: §§3.9-8 read, appendices skimmed (pp. 21-42; B, C, D, H captions)
- §3.9.2 (p. 24): word-scrambling "the model really does appear to learn these tasks at test time" (zero-shot near nil, artificial tasks), with "although we cannot confirm this with certainty".
- §5 (p. 34): the recognition-vs-learning paragraph, a "spectrum" from same-distribution demonstrations to "learning a skill entirely de novo"; "Where GPT-3 is on this spectrum may also vary from task to task."
- §5: pre-training sample efficiency poor; "it still sees much more text during pre-training than a human sees in the their lifetime".
- §7 (p. 40): inner loop "through computation in the model's activations across timesteps, without updating the weights"; outer loop "implicitly learns the ability to adapt to or at least recognize tasks".
- §6.3: amortization of pretraining compute over a model's lifetime (energy).
- Fig. 1.2 looked at as image (p. 4): by eye, 175B passes ~50% within about 10 examples, 13B reaches ~25% at K~100, 1.3B stays under ~5%. Examples-to-a-level fall with size, but this is my reading of a plot, not a stated measurement; one task.
- Fig. 3.8 (p. 20): at 125M few-shot (K=32) scores below one-shot. LAMBADA §3.1.2: few-shot "decreases the performance of the smallest model by almost 20%".
- Appendix B: all sizes 300B tokens, cosine LR decay; pretraining amount is never varied. No untrained or non-pretrained baseline; no fine-tuning of GPT-3.
- Open doubt: "scale" here is parameters/compute at fixed data, so it shows larger pretrained models adapt in context with fewer examples, not that more pretraining of one learner lowers cost.

## Step 4: bearings searched, quotes checked
- Not held: no LIT carries 2005.14165. Only the lead and CLAIM-756's notes point to the work.
- Bearings: CLAIM-756 (weak instance, cross-model), CLAIM-754 (ICL as a route of the developmental frontier vs operational elicitation), CLAIM-758 (no time course), TERM-131 (authors: no weight updates; inner loop in activations; agnostic on learning vs recognition), QUESTION-493 (background), CASE-294 (A56 ICL arm; recognition controls).
- Related readings: THEORY-2039 (Pan: recognition vs learning, scale), THEORY-2037 (MetaICL), THEORY-2052 (Garg), THEORY-2050 (Akyürek), THEORY-496 (Min), THEORY-683 (order), THEORY-614 (Xie), THEORY-169 (conditioning = training), THEORY-439 (ICL vs TTT), THEORY-2042, THEORY-973/990; CLAIM-118, CLAIM-074, CLAIM-697, QUESTION-020, QUESTION-161, CASE-005.
- All 45 quotes rechecked by script against my extracted text: all found.
- Verdict on the lead: it says Brown "measure how few examples in context reach a level"; they plot accuracy against K and by size; K-to-a-level is readable from Fig. 1.2 only by eye, for one task, and size varies at fixed 300B tokens, so "due to pretraining" is not isolated.
