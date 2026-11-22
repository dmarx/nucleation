### Changed

- The run-lead skill's shared-machine rule now forbids deleting or overwriting anything outside a worker's own scratchpad subdirectory and worktree, naming shared device nodes in particular. A [LEAD-023](record/leads.d/LEAD-023.md) run of 2026-11-22 ran `mv <file> /dev/null` as root, replacing /dev/null for every worker on the machine for about a minute before it was restored.
