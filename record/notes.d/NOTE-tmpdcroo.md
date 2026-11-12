---
status: Read
paper: LIT-tmp5jugw
title: 'He — Does Failure Feedback Direct Agent Self-Modification?'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2610.14662. Read
    (2026-11-12). A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper asks whether a self-improving agent's edits actually respond to
  the failure they were shown. It separates three quantities: -
  **Directedness:** is the shown failure repaired more often than the
  parent's other failures? - **Category-level spread:** are other failures
  in the same category repaired? - **Net score change:** failures repaired
  minus correct answers broken. In the Darwin Gödel Machine (DGM) the target
  failure is drawn at random, which makes an exact randomization or e-value
  test possible.
---
<!-- inactive-ok-file: CASE-194 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpdcroo: He — Does Failure Feedback Direct Agent Self-Modification?

## Contribution

1. A per-modification randomized test of directedness that stays valid in adaptive populations.
2. A null result on DGM.
3. A pre-specified second study.
4. An explanatory model of directedness against net gain.
5. A reporting recommendation for evaluations of agent self-modification.

## Key results

- **Abstract:** "Across 145 eligible modifications in public Darwin Gödel Machine logs, we find no detectable target-specific advantage."
- **§3.2:** "Of 145 eligible modifications, 12 repaired their target and 16.4 were expected under the null". Also: "The e-value for a directed effect is 0.15, far below the value of 20 required for evidence at the 5% level".
- **§3.5:** "We do not find that better agents make better edits". Viability is the difference instead: 49% of attempts with self-editing against 33% with the fixed editor on SWE-bench.
- **§4.3:** "Directed revisions did not raise the score of the clean playbook". The instance children lost 19.0 points on average.
- **§4.5:** of the planted-rule diagnoses, "No diagnosis stated that a rule was erroneous."
- **§5.4:** "Screening improves returned agents by discarding bad candidates, which is a property of selection rather than of the edits."
- **§6:** "Directedness measures whether the editor discriminates among causes, not whether the edit is useful".
- **Abstract:** "Target repair did not reliably imply held-out improvement." Also: "Held-out gains were concentrated in settings with identifiable, repairable failure mechanisms".
- **Abstract:** "Evaluations should report target repair, transfer to related failures, and held-out net change separately."

## Assumptions

- The target failure is drawn uniformly from the parent's failures (Eq. 2).
- Under the null, the drawn target affects neither viability nor the evaluation set.
- The controlled studies use small open models on BIG-Bench Hard and on a synthetic shop API with planted bugs.
- Each DGM agent is evaluated once, and noise is assumed comparable across runs.

## Concepts

- directedness, category-level spread, net score change
- randomized target selection, e-value and Ville's inequality
- viability of edits
- editable vs unreachable causes
- repair–breakage balance
- regression screening, edit localization (including oracle localization)
- improver vs product (§7.3)

## Bearing on the record

The LIT's gloss is accurate: no detectable target-specific repair advantage across 145 modifications in public Darwin Gödel Machine logs, and target repair not implying held-out improvement. Two corrections:
- The paper also finds that directed repair does occur when the editor sees the failure and the answer, as in study 1 and in Qwen's H1 result in study 2.
- The DGM null does not show the feedback was useless (§2.4).

- **QUESTION-tmp7a7l4 (can a collective become a better improver without losing failure detection): supports the question's framing and supplies a method.**
  - The paper separates the outcome of selection from the quality of edits, and finds that improvement in a selected population can arise without directed edits.
  - It recommends logging target repair, spread and net change separately, which is a ready protocol for the question's "later improver vs earlier improver" test.
  - §3.5 bears on the improver side directly: self-editing raised the viability of edits, not their quality.
  - It is about single agents and benchmark scores. It does not address shared records or collectives.
- **CASE-194 (three organizations at equal performance, separated only by intervention): qualifies by analogy.**
  - Equal score trajectories in DGM are "compatible" with selection over undirected variation. Only a randomized intervention on the evidence shown separates the explanations.
  - That is the same methodological point CASE-194 makes, that equal performance does not identify the cause.
  - The paper's editable vs unreachable causes (§6) parallel CASE-194's actuation vs observation limits.
  - It does not instantiate CASE-194's three arms.

## Limitations

- Single author.
- DGM is one system with one model pair, and each agent was evaluated once.
- The controlled studies use 4B-scale models.
- The diagnosis coding was done by one coder, an AI assistant.
- The H2 effects are near the noise from prompt perturbation.
- The explanatory model is qualitative and not fitted.
