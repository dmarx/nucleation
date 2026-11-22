# LEAD-140 tables

## Phase 1: the lineages' own products after 60 generations

Means over lineages of the evolved artifact on the frozen held-out battery; the improver each ended with.

| arm | n | held-out | public | damage /72 | oof /24 | self-check off | d_dmg=0 | d_oof=0 | canary off | archive on | n_cand | phi changes | inner eps | outer eps |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| none | 12 | -0.072 | -0.063 | 71.6 | 19.8 | 0 | 0 | 0 | 0 | 0 | 1.00 | 0.0 | 1920 | 0 |
| archive | 12 | -0.076 | -0.069 | 71.2 | 19.0 | 0 | 0 | 0 | 0 | 12 | 1.00 | 0.0 | 1920 | 0 |
| public | 12 | -0.100 | -0.065 | 66.0 | 20.4 | 1 | 2 | 2 | 4 | 7 | 1.42 | 2.4 | 2985 | 0 |
| own | 12 | -0.103 | -0.066 | 65.8 | 20.1 | 1 | 2 | 2 | 5 | 7 | 1.17 | 2.3 | 3029 | 0 |
| external | 12 | -0.130 | -0.065 | 59.8 | 20.9 | 2 | 1 | 1 | 2 | 3 | 1.33 | 1.9 | 2503 | 452 |
| layered | 12 | -0.068 | -0.064 | 72.0 | 21.4 | 0 | 3 | 2 | 2 | 4 | 1.83 | 3.0 | 3041 | 160 |

Evolved procedures (theta) per arm, counts of lineages per value:

- none: AUDIT_EVERY 5:3, 10:9; N_AUDIT 32:2, 64:5, 128:4, 256:1; SELF_CHECK_EVERY 40:3, 80:9; REPAIR_STEPS 30:12; TEACH 0.4:12
- archive: AUDIT_EVERY 10:12; N_AUDIT 32:3, 64:4, 128:4, 256:1; SELF_CHECK_EVERY 20:6, 40:3, 80:3; REPAIR_STEPS 10:10, 30:2; TEACH 0.4:12
- public: AUDIT_EVERY 5:1, 10:10, 20:1; N_AUDIT 64:8, 128:3, 256:1; SELF_CHECK_EVERY 0:1, 10:1, 20:2, 40:2, 80:6; REPAIR_STEPS 10:3, 30:9; TEACH 0.4:12
- own: AUDIT_EVERY 5:2, 10:9, 20:1; N_AUDIT 32:1, 64:6, 128:4, 256:1; SELF_CHECK_EVERY 0:1, 10:1, 20:2, 40:2, 80:6; REPAIR_STEPS 10:2, 30:10; TEACH 0.4:12
- external: AUDIT_EVERY 5:1, 10:11; N_AUDIT 32:1, 64:4, 128:4, 256:3; SELF_CHECK_EVERY 0:2, 40:3, 80:7; REPAIR_STEPS 10:1, 30:11; TEACH 0.4:12
- layered: AUDIT_EVERY 10:11, 20:1; N_AUDIT 64:5, 128:6, 256:1; SELF_CHECK_EVERY 20:2, 40:2, 80:8; REPAIR_STEPS 10:2, 30:10; TEACH 0.4:12

