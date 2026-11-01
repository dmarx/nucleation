### Changed

- `line:` takes several values in QUESTION, CASE, TERM and ARG, as it already did in CLAIM ([ADR-067](record/decisions.d/ADR-067.md)), at the owner's word.
  - [QUESTION-365](record/questions.d/QUESTION-365.md) gets `distributed-agency` back, and [ARG-050](record/arguments.d/ARG-050.md) gets `formal-apparatus` back. Both had been cut to pass lint.
- `line:` is required in CASE and ARG, as it already was in QUESTION and CLAIM. TERM stays optional.
  - Every ARG already had a line. The nine CASEs without one got lines from a graph query over `luria export`, recorded in ADR-067: CASE-006, CASE-007, CASE-014, CASE-025, CASE-028, CASE-034, CASE-151, CASE-181 and CASE-182.
