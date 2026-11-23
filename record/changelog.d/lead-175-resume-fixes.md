### Changed

- [LEAD-175](record/leads.d/LEAD-175.md)'s study scripts resume safely. `posterior.py` keeps one atomic checkpoint (block count, configuration, chains, step sizes, generator state) reconciled with its output, and fails when it cannot be. `sgd_sweep.py` counts completion per run, not per job. Both drop a final line torn by an interruption. Tests simulate each interruption. The committed SGD results are complete. The posterior outputs show no sign of a resume, though a stale resume would leave none. Found by a code review the owner forwarded.
