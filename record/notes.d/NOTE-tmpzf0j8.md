---
status: Read
paper: LIT-2298
title: 'Hu, Lu and Clune — Automated Design of Agentic Systems'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2408.08435. Read: main
    text in full; appendices skimmed (prompt, pseudocode). A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  The paper names a research area, Automated Design of Agentic Systems
  (ADAS). ADAS searches a space of agent designs with a search algorithm to
  optimize an evaluation function. It proposes searching in code, and gives
  an algorithm, Meta Agent Search.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpzf0j8: Hu, Lu and Clune — Automated Design of Agentic Systems

## Contribution

A framing of agent design as an optimization over code, and an archive-based open-endedness loop driven by a meta agent. Empirical evidence that searched agents beat hand-designed ones and transfer.

## Key results

- Formulation (§2): "Automated Design of Agentic Systems (ADAS) involves using a search algorithm to discover agentic systems across a search space that optimize an evaluation function."
- The loop (§3): the meta agent designs, two self-reflection steps check novelty, the agent is "evaluated using validation data from the target domain", and the agent is "added to the archive along with its evaluation metrics".
- Gains (§1): reading comprehension, "DROP (Dua et al., 2019) by 13.6/100" F1, and math "MGSM (Shi et al., 2023) by 14.4%". After transfer across domains, +25.9% on GSM8K and +13.2% on GSM-Hard.
- The improver is fixed. Self-improvement of the meta agent is left as future work (§6, Higher-order ADAS): "ADAS can become self-referential where the meta agent can be improved through ADAS as well."
- Single objective (§6): "We only consider one objective (i.e., performance) to optimize in this paper".
- Evaluation is coarse (§6): evaluation on the evaluation set "is both expensive and misses a lot of information".
- Safety measures (§6): "containerized execution of all generated code in secure, isolated environments".

## Assumptions

That validation-set accuracy is the right fitness signal. That the meta agent, a fixed FM with a fixed prompt, stays fixed across the search. Single-step QA tasks: the authors note "we only evaluate Meta Agent Search on single-step QA tasks".

## Concepts

ADAS (search space, search algorithm, evaluation function); Meta Agent Search; agent archive; "interestingness"; higher-order ADAS (meta-meta agents); transfer across domains and models.

## Bearing on the record

The exchange calls it "A meta-agent searches over agent designs" and "Strong prior art for automatically evolving agent organization". It also lists it under "Agent-scaffold search and evaluation of generated systems", with the gap being "Governed acceptance and preservation of epistemic commitments". **Accurate.** The paper has no acceptance step beyond the validation score, and preserves nothing other than the archive. "Agent organization" is slightly loose: ADAS evolves an agent's internal workflow of prompts, sub-calls and refinement, not an organization of agents. The paper only gestures at organizations in future work.

- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md)**, which lists [LIT-2298](../literature.d/LIT-2298.md) among the registered prior art: **qualifies the prior-art framing.** In A43's terms, ADAS delivers level 1 (better products, the agents) under a **fixed improver**. Improving the improver is explicitly future work (§6). It is therefore not evidence that an improver improved, and it does not compare earlier and later improvers from the same start. What it does offer is an archive that a later meta agent conditions on. That is a form of inheritance, a product record not a procedure record.
- **[CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)** (improver transplant): ADAS supplies a concrete baseline arm. A fixed meta agent with a growing archive is the control in which the improver does not improve.
- **[CLAIM-266](../claims.d/CLAIM-266.md)**: illustrates. Validation accuracy is both the search signal and the reported held-out measure, though on separate splits.
- **[NOTE-156](NOTE-156.md)** notes that ADAS is its source's ref. 1 and "Neither is held in either record." That is now outdated for this record: [LIT-2298](../literature.d/LIT-2298.md) holds it.

## Limitations

The reader checked the headline numbers from §1 against Table 2 for the transfer figures only. Appendix G was not read.
