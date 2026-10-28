### Changed

- Fourth status review (ADR-057; workbench entry of 2026-10-28).
- **CLAIM-277 promoted.** It is promoted on CASE-tmpasrij, a construction
  of its two loops (scratch/formal/trust_loop.py). It now rests on
  CLAIM-282, as its body said. QUESTION-083 is split, and
  QUESTION-tmpl8ywi is Answered.
- **168 offered answers moved.** Of the 240 Proposed `answers` edges on
  Open questions, 168 move to `bears_on`. ADR-060 version 2 covers offered
  part-answers.
- **The worklist** leaves out sound arguments whose held undercutters
  already narrow them (ADR-059).
- **Blockers recorded:** CLAIM-063's and CLAIM-004's are now on the
  entries.
- **luria 1.3.0 adopted (ADR-057, mechanisms 3–5).**
  - `reliance` ranks the pending report by dependents, and `load_bearing: 5`
    names the most relied on (38, a warning).
  - Four credence checks are reported patterns and fail the lint (all 0).
  - Acknowledgements of retired premises without `until` are held at a
    baseline of 41.
