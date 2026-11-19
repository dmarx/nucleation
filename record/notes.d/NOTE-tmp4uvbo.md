---
status: Read
paper: LIT-tmp42j5k
title: 'Zhang and colleagues — Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2506.11300v2 (PDF,
    28 Jan 2026): the body, pp. 1–9, in full; appendices A–H skimmed with
    captions; figure values not read. Running notes on the branch
    claude/readers/scheduling-followups (the procedure proposed in pull
    request 537). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Difficulty-ordered pretraining at fixed tokens: faster early progress,
  convergence by the end under strict ordering, a lasting gain when used
  as a warm-up. Within one distribution; mostly single runs; constant
  learning rate.
---
<!-- inactive-ok-file: CLAIM-756 THEORY-tmp0lbb1 THEORY-tmpd6l4a THEORY-tmprqq7k THEORY-tmpk9cmk — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmp4uvbo: Zhang and colleagues — Beyond Random Sampling: Efficient Language Model Pretraining via Curriculum Learning

## Contribution

A large comparison of curricula in pretraining, "over 200 models trained
on up to 100B tokens" (abstract): six difficulty metrics, strict,
paced and interleaved orderings, and curricula as warm-up.

## Key results

1. **Speed.** "curriculum learning consistently accelerates convergence in
   early and mid-training phases, reducing training steps by 18-45% to
   reach baseline performance" (abstract). Steps are tokens here, and the
   curriculum's tokens are counted.
2. **Convergence.** "The advantage of curriculum learning narrows as
   training progresses, with performances converging or remaining slightly
   higher than the baseline by the end of training." (§4.1)
3. **Warm-up.** Continuing curriculum and baseline models "using the same
   10B new data which is randomly shuffled" (§4.4), MTLD ends 3.5 and 2.6
   per cent higher, "and the baseline never surpasses the first phase of CL
   training with double the data"; at 100B tokens "the warmup model
   achieves an absolute performance improvement of approximately 3.1%"
   (App. G.3).
4. **Ordering, not filtering.** Shuffling the data seen before the best
   checkpoint helps, but "the ordered curriculum versions still achieve
   superior performance" (§5.3).

## Assumptions

Static difficulty per document; average zero-shot accuracy as the measure;
"a fixed learning rate of 2 × 10−4" throughout.

## Concepts

Vanilla, paced and interleaved curricula; curriculum as warm-up; steps to a
baseline's best; ordering against filtering.

## Bearing on the record

- **[CLAIM-596](../claims.d/CLAIM-596.md)**, the closest any of these readings comes to the rate it
  asks for: strict curricula look like head starts (early lead, then
  convergence), while the warm-up arm keeps improving after the baseline
  converges. Read from a figure, one run, no rate quantity.
- **[QUESTION-397](../questions.d/QUESTION-397.md)**, by the same contrast: partial organization changing
  later dynamics against a more advanced start.
- **[CLAIM-756](../claims.d/CLAIM-756.md)**, analogy: order at fixed total data with the earlier tokens
  counted, but within one acquisition; phase 2 is the same distribution.
- **[QUESTION-039](../questions.d/QUESTION-039.md)**, partial: order moves when aggregate competence arrives,
  mostly not the endpoint.
- **[THEORY-tmp0lbb1](../theory.d/THEORY-tmp0lbb1.md)** (Bengio and colleagues), parallel, qualifying: easy to
  hard helps at language-model scale, with lasting gains mainly as warm-up.
- **[THEORY-tmpd6l4a](../theory.d/THEORY-tmpd6l4a.md)** (Skill-it), contrast: different units ordered and
  different measures, not a contradiction.
- **[THEORY-tmprqq7k](../theory.d/THEORY-tmprqq7k.md)** (Feng, Goodman and Frank), parallel: order within a
  corpus washes out at the end under strict ordering.
- **[THEORY-tmpk9cmk](../theory.d/THEORY-tmpk9cmk.md)**, parallel: both count the earlier phase's tokens.

## Limitations

Single runs except six settings with three; constant learning rate;
small-model zero-shot accuracy near chance on several tasks; best-
checkpoint comparisons favour noisy arms; the best-checkpoint warm-up arm
not token-matched.
