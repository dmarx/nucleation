---
status: Read
paper: LIT-tmpkfcwr
title: 'Han and others 2026 — Weight Decay Improves Language Model Plasticity'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2602.11137 (served as
    arXiv:2602.11137v2, 28 May 2026; 32 pages). The PDF states it appears in
    the Proceedings of the 43rd International Conference on Machine Learning
    (ICML 2026), PMLR 306. Kind of copy (step 5): arXiv preprint, the
    authors' own manuscript on arXiv. Lawful. Date: 2026-11-19. HTTP 200, no
    bot check, no refusal. No email address sent. Text extracted with
    pdftotext to dl/text.txt; PDF in dl/paper.pdf. Read: abstract, §1-§6 in
    full (pp. 1-9), Appendix A (additional discussion and limitations), the
    setup and results text of Appendix E (sweeps over pre-training and fine-
    tuning hyperparameters). Skipped: Appendices B, C, D and F, except
    headings (pre-training details, per-task fine-tuning results, trade-off
    analyses, mechanism figures). Figure values were read from captions and
    text only.
date: '2026-11-19'
---

# NOTE-tmps6j9j: Han and others 2026 — Weight Decay Improves Language Model Plasticity

## Contribution

Han, Bordt, Zhang and Kakade pre-train Llama-2 and OLMo-2 models (0.5B-4B, at 20 and 140 tokens per parameter) at a range of AdamW weight decay values. They then fine-tune each model on twelve downstream tasks (chain-of-thought reasoning, commonsense benchmarks, safety). Plasticity is measured as how well the model does on the fine-tuning task after fine-tuning. Weight decay above the default 0.1 gives better fine-tuned performance, including where it gives a worse pre-training loss, so pre-training loss does not rank models by what they become after further training. They report three correlates of higher weight decay: more linearly separable representations, lower-rank query–key products, and a smaller train–validation gap.

## Key results

- The main finding (abstract, p. 1): "larger weight decay increases the plasticity of the pretrained model, resulting in greater performance gains downstream after finetuning".
- Worse now, better later, in the overtrained regime (§4.3, p. 6): "OLMo-2-1B-140x pretrained with weight decay 0.3 or 1.0 performs slightly worse after pretraining" than at 0.1 (losses 2.6208 and 2.7064 against 2.6088), "but the former two pretrained models perform noticeably better after fine-tuning".
- Pre-training loss is not a sufficient statistic (Fig. 3 caption, p. 6): "models with similar pretraining losses can perform differently downstream".
- The effect holds across fine-tuning hyperparameters, fine-tuning weight decay included (App. E.2, p. 23): "In all these analyses, we find that higher pretraining weight decay leads to better fine-tuning performance."
- Plasticity is measured only on the target task (§3, p. 3): "To assess the plasticity of a pretrained model, we fine-tune the model on a task and then measure its performance on this task."
- Attention rank (§5.2, p. 8): larger weight decay lowers the rank of the query–key and value–projection products, the query–key product more. At the default, "the default weight decay parameter of 0.1 yields near full-rank matrices". Beyond a weight decay of 1.0 for Llama-2, the value–projection rank collapses, "a transition that correlates with a significant drop in performance".
- The mechanisms are correlational, and the effect causal (App. A, p. 13): "these mechanisms are correlational in nature", while weight decay's effect on plasticity "is causal (since the experiments vary only weight decay and keeps other variables constant)".
- A limit the authors draw (§6, p. 9): "In heavily overtrained scenarios or for very large models trained for many steps", "the benefits of markedly lower pretraining validation loss may outweigh those of plasticity".

## Assumptions

- That the fine-tuned score on the target task measures plasticity. Forgetting of pre-trained capability during fine-tuning is not measured.
- That weight decay changes nothing else that matters. All other hyperparameters are fixed per sweep, and the sweep over pre-training learning rate is small (3 × 3).
- That results at 0.5B-4B and up to 140 tokens per parameter bear on larger and longer runs. The authors limit them to that scope.

## Concepts

- Plasticity (after Berariu et al. and Dohare et al.): the ability of a trained model to adapt to new data upon further training, without reinitialization.
- The "end-to-end" choice of pre-training hyperparameters: choosing them by the post-trained model's performance, not the base model's validation loss.
- Train–val gap: validation loss minus loss on the training data, read as overfitting to (less forgetting of) pre-training data.

## Bearing on the record

- CLAIM-tmp8ljvp: supports a clause, not the core. Two pre-training regimes reach similar or better present loss and differ in how much later fine-tuning yields, which is the claim's frontier difference. But the paper varies weight decay, not training length. It never shows plasticity falling as one run continues, so it says nothing about continued stabilization as such. The authors' own limit (heavily overtrained runs may favour low loss) matches the claim's clause that the failure is relative to a declared family.
- CLAIM-tmp5vg7p: leaves open. Weight decay is applied throughout pre-training, a preventive rather than a late intervention. Fine-tuning-time weight decay, learning rate and batch size were swept, and the pre-training weight decay advantage persisted in each setting. The paper does not report whether fine-tuning weight decay alone recovers plasticity, so it does not test a late direct intervention.
- CASE-tmphsr99: supports the preventive arm (higher pre-training weight decay) as an arm worth having. It also warns that the case's design needs a forgetting axis this paper lacks: Han measures only gain on the new task.
- CLAIM-675: supports. Similar or worse present capability (pre-training loss) with better later capability (fine-tuned score) is the claim's point that present capability sets do not rank what comes after, here for training regimes. It is the strongest direct case of A71 §10's prediction about matched present performance among these works.
- THEORY-1353: related, not the same construct. Han finds higher weight decay lowers query–key rank and improves fine-tuning. Dong finds a query–key reset restores learnability on an aged substrate. Both put the plasticity-relevant structure in the query–key product. Neither tests the other's intervention.
- THEORY-213 (found at the recheck): consistent within a window. Ziyin predicts that weight decay above a critical value drives weights into symmetric, reduced-rank subspaces, with loss of plasticity as a consequence. Han sees rank fall with weight decay, plasticity rise up to about 0.5-1.0, and a value–projection rank collapse past 1.0 that goes with a drop in performance.

## Limitations

- Plasticity is measured on the fine-tuning task only. What fine-tuning costs in pre-trained capability is not measured, so stability and plasticity are not separated.
- Few pre-training runs per group (n ≤ 10, and fewer at 4B and at 140 tokens per parameter), one seed of pre-training per setting as far as the main text says, and correlations "suggestive rather than conclusive" by the authors' account.
- Training length is varied only between 20 and 140 tokens per parameter, between groups, not along one run.
