### Changed

- The run-lead skill's step 5 now says that workers share one machine: stop only the processes you started, by PID, never by `pkill` or `killall` on a name, and keep scratch files in a subdirectory named after the lead. [LEAD-077](record/leads.d/LEAD-077.md)'s run was killed twice on 2026-11-22 by another worker's process kill.
