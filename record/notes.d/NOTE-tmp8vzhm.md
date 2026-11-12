---
status: Skimmed
paper: LIT-tmp37u5c
title: 'Georgiev, Gómez-Serrano, Tao and Wagner — Mathematical exploration and discovery at scale'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from https://arxiv.org/pdf/2511.02864. **Skimmed**:
    §§1–5 (pp. 1–9: introduction, overview of AlphaEvolve, meta-analysis and
    ablations, conclusions, future work) read; §6, the 67 problem write-ups
    (pp. 9–81), skipped except the opening of §6 and spot-reads of problem
    6.1's role in §1.5. A delegated reader drafted the reading; quotations
    were rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  AlphaEvolve is an evolutionary coding agent: an LLM mutates programs, a
  user-supplied evaluator scores them, and better programs seed the next
  generation. The authors apply it to 67 problems in analysis,
  combinatorics, geometry and number theory, mostly evolving search
  heuristics rather than constructions directly ("search mode"). It
  rediscovers the best known constructions in most cases and improves
  several; some findings generalize to formulas, and one (finite-field
  Kakeya) was proved by Deep Think and formalized in Lean by AlphaProof.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp8vzhm: Georgiev, Gómez-Serrano, Tao and Wagner — Mathematical exploration and discovery at scale

## Contribution

A large, candid portfolio test of LLM-guided evolutionary search in mathematics, reporting
failures as well as improvements, with ablations on parallelism and model choice and a
worked pipeline from discovery to formal proof.

## Key results

1. Abstract: "The system rediscovered the best known solutions in most of the cases and
   discovered improved solutions in several."
2. §1, p. 1: "AlphaEvolve is not a general-purpose solver for all types of mathematical
   problems".
3. §1, p. 2: the system optimizes both constructions and "the algorithmic strategy for
   discovering such constructions"; "the optimization process itself becomes the object of
   optimization."
4. §1.5: discovery (AlphaEvolve), proof (Deep Think) and formalization (AlphaProof)
   combined for the finite field Kakeya problem.
5. §1.6: it "excels at problems that can be clearly formulated as the optimization of a
   smooth score function that is possible to ‘hill-climbing’ on, it sometimes struggles
   otherwise."
6. §4, p. 8: "the selection of the verifier is a critical component that significantly
   influences the system’s performance and the quality of the discovered results."
7. §4, p. 8: "we also observed a “cheating phenomenon”, where the system would find
   loopholes or exploit artifacts ... in the problem setup rather than genuine solutions,
   highlighting the need for carefully designed and robust evaluation environments."
8. §3.2: an all-high-end-model run "can sometimes perform worse than a run that occasionally
   used cheaper models as well", plausibly because cheaper models add variance.
9. §4, p. 9: "for problems where genuinely new, deep insights are required to make progress,
   AlphaEvolve is likely not the right tool to use."
10. §6, p. 9: "we have endeavored to document both the positive and negative results".

## Assumptions

The problem must be cast as a score over constructions computable by a (possibly leaky)
evaluator; infinite-dimensional problems are discretized; human experts choose the problem,
the verifier and the prompt ("we got better at knowing how to prompt AlphaEvolve the more we
tried", §4).

## Concepts

evolutionary coding agent; generator (LLM) and evaluator; search mode; leaky vs rigorous
verifier; "cheating phenomenon"; constructive mathematics at scale; "AlphaEvolve-hard";
discovery-to-formalization pipeline.

## Bearing on the record

Same authors, same programme (AlphaEvolve applied to 67 problems), and OpenAlex records the
arXiv paper as a location of the PNAS work. The PNAS article's text was not seen, so which
results it keeps, and whether it changes any claim, is unknown. Treat statements below as
the preprint's.

- **[CLAIM-266](../claims.d/CLAIM-266.md)** (Active; the probes that supply the training signal cannot certify what the
  system preserves): *supports with instances*: the evaluator is the training signal, and
  the system exploited its leaks (result 7); the authors' remedies are better-designed
  verifiers (one problem contrasts a fast floating-point "leaky" verifier with a slower
  rational-arithmetic one, §6, p. ~38) and, in rare cases, proof and formalization (result 4).
- **[CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)** (Proposed; outer evaluation boundary) and **[LIT-2286](../literature.d/LIT-2286.md) /
  [LIT-2276](../literature.d/LIT-2276.md)** (reward hacking, Deferred): another observed case of an optimizer exploiting
  its evaluator; the authors' remedy is the outer boundary (human-designed, fixed
  verifier), the same control [CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md) specifies.
- **[LIT-2327](../literature.d/LIT-2327.md)** (DGM, read in this batch): the same pattern ("objective hacking"); both
  systems keep the evaluator outside what the optimizer may change.
- **[QUESTION-388](../questions.d/QUESTION-388.md)** (Open): result 3 (optimizing the search procedure) is reconfiguration of
  the improver within a fixed evaluation frame.
- **[LIT-2329](../literature.d/LIT-2329.md) / [LIT-2321](../literature.d/LIT-2321.md) / [LIT-2324](../literature.d/LIT-2324.md)**: the AI-discovery cluster; this work contrasts with
  them in having machine-checkable scores.

## Limitations

Only pp. 1–9 read; none of the 67 problem results was checked. Preprint, not the PNAS
version.
