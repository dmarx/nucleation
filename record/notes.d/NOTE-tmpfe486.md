---
status: Read
paper: LIT-tmpnkxqn
title: 'Meng et al. — Sparse but Critical'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2603.22446v1, https://arxiv.org/pdf/2603.22446,
    text by pdftotext. Read: the abstract, §1, §2.1–2.2 (JS divergence,
    sparsity), §3.1–3.2 (the cross-sampling framework and results), §4.2
    (does RL invent or select?) and §7. Skimmed or skipped: §2.3–2.6
    (positional, entropy, semantic and SFT comparisons), §4.1, §4.3, §5
    (divergence-weighted advantage) and the appendices; figures not seen.
    The filer rechecked every quote below against the downloaded text. The
    DAPO forward result reads "are are enough" in the text (a typo), so it
    is paraphrased, not quoted; the filer added from Table 1 that DAPO's
    7.8% is about 280 effective tokens per response.
date: '2026-11-15'
summary: >-
  Base and RLVR models differ at few token positions; swapping in the other
  model's token at only the highest-divergence positions moves AIME
  accuracy all the way from one model's level to the other's, in both
  directions. RLVR mostly reallocates mass among tokens the base model
  already ranks highly. Token-level support for Yue et al.'s sharpening.
---
<!-- inactive-ok-file: THEORY-tmp9rnyv THEORY-tmppt44k — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 — Proposed; the claim this reading bears on indirectly -->

# NOTE-tmpfe486: Meng et al. — Sparse but Critical

## Contribution

A token-level comparison of base and RLVR next-token distributions
(Qwen2.5-32B with DAPO, and with GRPO in SimpleRL; extensions to
Qwen2.5-Math-7B, Qwen3-8B-Base and Mistral-Small-24B), by Jensen–Shannon
divergence on the models' own AIME generations, and "cross-sampling": the
other model's token is sampled only at positions whose divergence exceeds
a threshold, under a budget on the number of swaps.

## Key insight

What RLVR changes is concentrated: a handful of decisions per response,
where the RL model picks among tokens the base model already considers,
carry the whole accuracy difference.

## Assumptions

- Divergence is computed on top-p truncated distributions under the
  sampling configuration (robustness in App. A.5, not read).
- Accuracy is Mean@32 on AIME 2024 and 2025.
- Positions are chosen by divergence, which needs both models at every
  step.

## Key results

- **Sparsity** (§2.2): "Under DAPO, more than 83% of token positions
  exhibit near-zero divergence, while this proportion exceeds 98% under
  SimpleRL." Even without KL, DAPO "maintains near-zero divergence at most
  token distributions."
- **The rule** (§3.1): S(x<t) = 1{D_JS(πprim‖πint) > ε}, "so that
  cross-sampling intervenes only at high-divergence positions".
- **Forward, SimpleRL** (§3.2, AIME 2024): "Injecting fewer than 4%
  RL-sampled tokens per sequence on average, corresponding to fewer than
  40 effective token substitutions per response, is sufficient to close the
  performance gap from the base model (approximately 8%) to the RL model
  (approximately 25%)". On AIME 2025 the mixed policy exceeded the RL
  policy.
- **Forward, DAPO** (§3.2): about 7.8% of effective tokens (280 per
  response, Table 1) take accuracy from about 8% to over 44%.
- **Reverse** (§3.2): "replacing approximately 5% of high-divergence
  distributions, corresponding to less than 30 effective base-sampled
  tokens per response, is sufficient to collapse accuracy from RL levels
  (around 25%) back to base-level performance (around 8%)"; for DAPO,
  "reverting roughly 10% of effective tokens". The substituted base tokens
  "are mostly plausible and semantically reasonable ... yet they
  nonetheless progressively derail the reasoning process."
- **Invent or select** (§4.2): under DAPO "only about 5% (among
  high-divergence positions) of RL top-1 tokens have base probability below
  0.01", nearly none under SimpleRL; "RLVR rarely elevates tokens that were
  highly unlikely in the base model".
- **Conclusion** (§7): RLVR refines behaviour "by reallocating probability
  mass within an existing candidate set", though the rare promotions "may
  still be important".

## Concepts

Token-level JS divergence; sparse distributional shift; forward and
reverse cross-sampling; intervention budget; trajectory sensitivity;
reallocation within the candidate set.

## Bearing on the record

- **Yue et al. ([THEORY-tmp9rnyv](../theory.d/THEORY-tmp9rnyv.md))**: supports the sharpening reading at the
  token level. RL mostly reallocates mass among tokens the base model
  already ranks, and only at a few positions. Its rare promotions of
  low-probability tokens are where expansion, if any, would live.
- **[QUESTION-392](../questions.d/QUESTION-392.md) and [CLAIM-576](../claims.d/CLAIM-576.md)**: indirect. Reallocation within an existing
  candidate set fits RL as making reachable paths reliable rather than
  adding reachable ones; it does not test whether any new path is added.
- **Balasubramanian and Kasiviswanathan ([THEORY-tmppt44k](../theory.d/THEORY-tmppt44k.md))**: their formal
  result that a tilt can only reweight modes present in the reference is
  the idealized counterpart; this paper measures something close to it
  without a KL anchor.
- **[CLAIM-118](../claims.d/CLAIM-118.md)**: no bearing.

## Limitations

- Per model pair, on two AIME years.
- §5 and the appendices not read; the semantic content of the critical
  positions (§2.5) not read.
- Cross-sampling shows that decisions at divergent positions suffice; it
  does not show what they are.
