# Reader notes: zhangcurr (arXiv 2506.11300)

## Copy located (2026-11-19)
- https://arxiv.org/abs/2506.11300 (200); PDF https://arxiv.org/pdf/2506.11300 = v2 (28 Jan 2026), 19 pp. Lawful (arXiv author upload).
- Title: "Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning". Authors: Yang Zhang, Amr Mohamed, Hadi Abdine, Guokan Shang, Michalis Vazirgiannis (Ecole Polytechnique; MBZUAI).

## Read in full (body pp.1-9), appendices A-H skimmed
- Setup: 0.5B LLaMA3.2-like, 10B CulturaX-en tokens, constant LR 2e-4 (no decay), batch ~1.08M tokens; 8 zero-shot benchmarks averaged.
- Six metrics (from 15 by Spearman): compression ratio, fertility, Flesch reading ease, MTLD, #tokens, KenLM perplexity.
- Exp1 vanilla strict order (S1, same 10B reordered vs shuffled); Exp2 pacing linear/quad/inv-quad, 10 groups (S2); Exp3 interleaved 10x1B (S2); Exp4 CL as warmup then 10B new random (S3).
- Step savings are "fewer steps to reach the baseline's best/peak", one seed per arm except App. D (3 runs, six pacing/interleave settings).
- Warmup: baseline is also continued on the same 10B new shuffled data; "best checkpoint" arm started from a checkpoint before 10B, so fewer total tokens.
- Gains concentrated early/mid; vanilla converges to baseline at end (p5). Warmup gives +2.0 to +3.5% at end; 100B run +~3.1%.
- Open doubt: fixed LR throughout; no LR decay, so "endpoint" is a constant-LR endpoint.
