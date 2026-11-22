### Added

- ADR-tmpvqx5l and ADR-tmpyb409, two alternative decisions on making long-running and delegated work persist its progress as it goes. (a) supersedes ADR-108 with one general rule; (b) leaves ADR-108 standing and adds lead workers and long computations. Both were filed on the owner's request of 2026-11-22.
- The run-lead skill (`.claude/skills/run-lead/SKILL.md`), the lead-worker brief moved out of the session's scratchpad. It now pushes the branch at once, pushes after every step, keeps a PROGRESS file, writes computed results per item, and budgets time. This is both decisions' first application.
- A devlog note, tagged retro, on work held until the end being lost or put at risk three ways on 2026-11-22.
