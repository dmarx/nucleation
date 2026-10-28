### Added

- [ADR-057](record/decisions.d/ADR-057.md) (Proposed): status review is ranked by reliance, derived from
  the record on each pass, covers relations as well as statuses, and makes
  its changes in the pull request that decides them. It proposes five lint
  forcing functions against a repeat of the backlog.
- `record/status-review/worklist.py`, with tests: load-bearing Proposed
  entries, credence inversions, retired premises, Open questions with an
  Active answer, and unblocked Proposed claims.
- [CLAIM-tmpnp8w6](record/claims.d/CLAIM-tmpnp8w6.md): a reply to [CLAIM-089](record/claims.d/CLAIM-089.md) on [CLAIM-434](record/claims.d/CLAIM-434.md)'s result.
- [TERM-tmppwzer](record/terms.d/TERM-tmppwzer.md): inquiry, as (Σ, A, 𝓘, 𝓞, 𝓚, 𝓑).

### Changed

- `stale_days: 14`. The default of 90 could not name a stale document in
  a record a month old.
- [CLAIM-365](record/claims.d/CLAIM-365.md) `complements` [CLAIM-347](record/claims.d/CLAIM-347.md) instead of resting on it.
  [CLAIM-159](record/claims.d/CLAIM-159.md) `objects_to` [CLAIM-024](record/claims.d/CLAIM-024.md). [CLAIM-470](record/claims.d/CLAIM-470.md) and [CLAIM-475](record/claims.d/CLAIM-475.md) use the new
  TERM.
- The workbench entry of 2026-10-27 records the pass.
- The owner's rulings, 2026-10-27:
  - [ADR-057](record/decisions.d/ADR-057.md) is Active and [ADR-047](record/decisions.d/ADR-047.md) Superseded.
  - [CLAIM-tmpnp8w6](record/claims.d/CLAIM-tmpnp8w6.md) is held, and [CLAIM-089](record/claims.d/CLAIM-089.md) is Rejected.
  - [TERM-tmppwzer](record/terms.d/TERM-tmppwzer.md) (inquiry) is adopted.
  - Mechanism 2 is declined ([DP-3](docs/design-principles.md#dp-3)), and mechanism 5 is adopted as a
    convention.
- The five promotions [ADR-047](record/decisions.d/ADR-047.md)'s audit decided and never carried out:
  - [CLAIM-322](record/claims.d/CLAIM-322.md), [CLAIM-328](record/claims.d/CLAIM-328.md) and [CLAIM-046](record/claims.d/CLAIM-046.md) are Active.
  - [CLAIM-241](record/claims.d/CLAIM-241.md) is Active, and [CLAIM-217](record/claims.d/CLAIM-217.md) concedes it at version 2: uptake is
    a defeasible standard.
  - [THEORY-073](record/theory.d/THEORY-073.md) is narrowed to Friston's 2013 formulation and promoted. The
    wider form is [THEORY-tmplg04q](record/theory.d/THEORY-tmplg04q.md), Proposed.
- Pass 2 (workbench entry of 2026-10-27):
  - [CLAIM-283](record/claims.d/CLAIM-283.md), [CLAIM-025](record/claims.d/CLAIM-025.md) and [CLAIM-177](record/claims.d/CLAIM-177.md) are promoted. [CLAIM-283](record/claims.d/CLAIM-283.md) and
    [CLAIM-177](record/claims.d/CLAIM-177.md) are narrowed, with their dropped halves filed as
    [CLAIM-tmpxb1wf](record/claims.d/CLAIM-tmpxb1wf.md) and [CLAIM-tmpuhp12](record/claims.d/CLAIM-tmpuhp12.md).
  - [TERM-tmp3mqer](record/terms.d/TERM-tmp3mqer.md) (Frijda's action readiness) and [CASE-tmpv0eej](record/cases.d/CASE-tmpv0eej.md)
    (Frankfurt's unwilling addict) take the place of contested THEORYs as
    the grounds of claims that used only their concept or case.
  - Four claims move off Superseded TERMs.
  - The worklist counts inversions on ARGs.
- Pass 3 (workbench entry of 2026-10-27):
  - [ADR-058](record/decisions.d/ADR-058.md): a THEORY can corroborate a CLAIM. 16 edges move from
    `grounds` to `corroborated_by`.
  - [THEORY-tmp5sao6](record/theory.d/THEORY-tmp5sao6.md) states Blackwell's definitions and easy direction with
    a proof, and ten claims move onto it. Five claims move from [THEORY-174](record/theory.d/THEORY-174.md)
    to [THEORY-720](record/theory.d/THEORY-720.md).
  - Credence inversions go from 38 to 3. The three that remain need the
    owner's ruling.
  - Eight questions are split under [ADR-049](record/decisions.d/ADR-049.md). [ADR-049](record/decisions.d/ADR-049.md) version 2 sizes
    splits by [ADR-057](record/decisions.d/ADR-057.md)'s pass.
- The owner's rulings on pass 3:
  - [CLAIM-069](record/claims.d/CLAIM-069.md) and [CLAIM-438](record/claims.d/CLAIM-438.md) are Proposed.
  - [ADR-060](record/decisions.d/ADR-060.md) adds `bears_on` and `bearing`, and moves 102 Active `answers`
    edges on Open questions to `bears_on`.
  - [ADR-059](record/decisions.d/ADR-059.md) (Proposed) says what a status means for an ARG (credence in
    its inference) and for a conceded counter (recorded by the target's
    revision).
- ADR-059 is accepted. The worklist lists sound arguments with unheld
  conclusions in place of ARG premise inversions, and the claims template's
  convention for conceded counters is rewritten.
