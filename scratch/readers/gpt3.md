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
