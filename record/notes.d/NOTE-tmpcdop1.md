---
status: Read
paper: LIT-tmpb6e1c
title: 'Jiang and colleagues — Procedural Pretraining: Warming Up Language Models with Abstract Data'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2601.21725v2 (HTML,
    CC BY 4.0): §§1–7 and limitations in full; appendices A–N skimmed with
    their tables; figures not seen. Running notes on the branch
    claude/readers/scheduling-followups (the procedure proposed in pull
    request 537). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  A procedural warm-up of well under one per cent of tokens lowers the
  semantic tokens needed to reach baseline loss; structure, not
  statistics, carries it. Savings in semantic tokens; no seeds; no
  natural-language warm-up control.
---
<!-- inactive-ok-file: CLAIM-756 THEORY-tmpk9cmk THEORY-tmpsewbi CLAIM-758 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpcdop1: Jiang and colleagues — Procedural Pretraining: Warming Up Language Models with Abstract Data

## Contribution

A front-loaded phase of abstract procedural data, studied in additive and
substitutive settings, with localisation of what transfers and
interventions that rule out simple explanations.

## Key results

1. **Savings.** "with C4, we can maintain the baseline loss and save about
   45 % of semantic tokens (and thus FLOPs) by using only 2.1 M procedural
   tokens"; "For CodeParrot and DeepMind-Math, a 33 % and 14 %
   tokens/FLOPs saving can be achieved with 2.1 M and 10.4 M procedural
   tokens" (§5.2). The abstract pairs a 0.1 per cent share with the 14 per
   cent saving, which in fact needed about 0.6 per cent.
2. **How the saving is counted.** Semantic tokens such that "training on
   (T_{2}-\Delta T_{2}) semantic tokens with T_{1} procedural tokens
   matches the performance of a T_{2} -only model" (§5.2); the procedural
   tokens are named, not netted into a FLOP total.
3. **Scale.** At 1.3B, "we use only 82M procedural tokens" to "match
   baseline performance using just 66% of the C4 data and 75% of the
   CodeParrot data" (App. L).
4. **Structure carries it.** "If we remove the structure within the
   procedural data by shuffling the sequences (Best model shuffled), the
   performance falls to the baseline." (Fig. 2); shuffling weights per
   layer also removes it (§4.3).
5. **Amount and kind.** "the improvement is not clearly correlated with
   the amount of procedural pretraining tokens" (§5.1); a phase whose loss
   is driven too low hurts (App. I); some procedures harm some later
   skills (Table 8).
6. **Localisation.** "the attention layers are more important for
   structured, language-free domains like pure code, while MLP layers help
   natural language more" (§1).

## Assumptions

Equal semantic-token loss as equal cost; procedure and length chosen by
downstream grids, uncosted; single semantic runs.

## Concepts

Procedural pretraining; additive and substitutive settings; selective
transfer; structure against statistics.

## Bearing on the record

- **[CLAIM-756](../claims.d/CLAIM-756.md)**, evidence for its premise: an earlier acquisition of
  negligible cost and no direct value on the target (its vocabulary is
  discarded) lowers a later acquisition's token cost substantially. Cost
  in semantic tokens, selection uncosted, no seeds.
- **[THEORY-tmpk9cmk](../theory.d/THEORY-tmpk9cmk.md)** (Hu and colleagues), a second, independent instance
  with different procedures, domains and scale; it lacks Hu's matched
  natural-language first-phase control, so it cannot say procedural data
  beats as much natural text. It does not test Hu's non-hierarchical arm.
  It does not by itself meet that THEORY's promote_when, which asks for
  Hu's specific findings.
- **[THEORY-tmpsewbi](../theory.d/THEORY-tmpsewbi.md)** (Stern and colleagues): the compute-matched dispute
  this paper does not answer.
- **[TERM-117](../terms.d/TERM-117.md)**, application: productivity is a vector over targets (Union
  raises multiplication and collapses sorting) and the phase has an
  optimal length.
- **[CLAIM-754](../claims.d/CLAIM-754.md)**, by analogy: the same phase lowers some later costs and
  raises others.
- **[CLAIM-758](../claims.d/CLAIM-758.md)**, a weak instance: a first phase stabilized too far worsens
  later transfer, small-scale and read from a figure.
- **[QUESTION-039](../questions.d/QUESTION-039.md)**, partial: front-loaded structure changes later
  acquisition, non-monotonically in its length.

## Limitations

Up to 1.3B; no seeds or variance on semantic runs; no natural-language or
code warm-up control; unclear whether substitutive points come from
re-scheduled shorter runs.
