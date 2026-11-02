### Changed

- `line:` takes several values in QUESTION, CASE, TERM and ARG, as it already did in CLAIM ([ADR-067](record/decisions.d/ADR-067.md)), at the owner's word.
  - [QUESTION-365](record/questions.d/QUESTION-365.md) gets `distributed-agency` back, and [ARG-050](record/arguments.d/ARG-050.md) gets `formal-apparatus` back. Both had been cut to pass lint.
- `line:` is required in CASE and ARG, as it already was in QUESTION and CLAIM. TERM stays optional.
  - Every ARG already had a line. The nine CASEs without one got lines from a graph query over `luria export`, recorded in [ADR-067](record/decisions.d/ADR-067.md): [CASE-006](record/cases.d/CASE-006.md), [CASE-007](record/cases.d/CASE-007.md), [CASE-014](record/cases.d/CASE-014.md), [CASE-025](record/cases.d/CASE-025.md), [CASE-028](record/cases.d/CASE-028.md), [CASE-034](record/cases.d/CASE-034.md), [CASE-151](record/cases.d/CASE-151.md), [CASE-181](record/cases.d/CASE-181.md) and [CASE-182](record/cases.d/CASE-182.md).
