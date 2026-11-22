# LEAD-140 tables

Starting artifact theta0 on the held-out battery: held-out -0.133, public -0.135, damage recovered 72/72, out-of-family 24/24.

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

## Phase 2: earlier and later improvers from the same start

Each improver applied for 10 generations at 32 episodes each (equal budget; the layered arm's outside veto counted separately), on the same seeds, then scored on the held-out battery. Means over lineages (replicates averaged first). 'orig' is the fresh starting artifact theta0; 'improved' the lineage's evolved artifact. early = the arm's starting improver with an empty record; late = the evolved improver with its record; knowledge = starting settings with the evolved record; organization = evolved settings, empty record.

| arm | orig/early | orig/late | orig/knowledge | orig/organization | improved/early | improved/late |
|---|---|---|---|---|---|---|
| **held-out score** | | | | | | |
| none | -0.099 | -0.099 | -0.099 | -0.099 | -0.071 | -0.071 |
| archive | -0.088 | -0.080 | -0.080 | -0.088 | -0.072 | -0.077 |
| public | -0.099 | -0.089 | -0.099 | -0.090 | -0.087 | -0.087 |
| own | -0.099 | -0.086 | -0.099 | -0.087 | -0.087 | -0.100 |
| external | -0.099 | -0.086 | -0.099 | -0.083 | -0.100 | -0.098 |
| layered | -0.101 | -0.084 | -0.101 | -0.088 | -0.069 | -0.069 |
| **public score** | | | | | | |
| none | -0.095 | -0.095 | -0.095 | -0.095 | -0.062 | -0.062 |
| archive | -0.083 | -0.080 | -0.080 | -0.083 | -0.066 | -0.070 |
| public | -0.095 | -0.086 | -0.095 | -0.086 | -0.067 | -0.067 |
| own | -0.095 | -0.084 | -0.095 | -0.082 | -0.067 | -0.066 |
| external | -0.095 | -0.083 | -0.095 | -0.080 | -0.066 | -0.064 |
| layered | -0.097 | -0.081 | -0.097 | -0.083 | -0.063 | -0.063 |
| **damage recovered /72** | | | | | | |
| none | 72.0 | 72.0 | 72.0 | 72.0 | 71.8 | 71.8 |
| archive | 71.8 | 71.9 | 71.9 | 71.8 | 71.6 | 71.5 |
| public | 72.0 | 72.0 | 72.0 | 72.0 | 68.9 | 68.9 |
| own | 72.0 | 72.0 | 72.0 | 71.8 | 68.8 | 65.9 |
| external | 72.0 | 72.0 | 72.0 | 72.0 | 65.6 | 65.8 |
| layered | 72.0 | 71.9 | 72.0 | 71.8 | 71.9 | 71.9 |
| **out-of-family /24** | | | | | | |
| none | 22.8 | 22.8 | 22.8 | 22.8 | 19.5 | 19.5 |
| archive | 21.2 | 22.6 | 22.6 | 21.2 | 20.4 | 19.5 |
| public | 22.8 | 22.5 | 22.8 | 22.2 | 20.2 | 20.8 |
| own | 22.8 | 22.4 | 22.8 | 21.3 | 19.8 | 21.1 |
| external | 22.8 | 22.6 | 22.8 | 22.3 | 20.0 | 20.3 |
| layered | 22.8 | 21.8 | 22.8 | 21.4 | 20.7 | 20.5 |

Paired contrasts on the held-out score (mean difference; lineages better / worse; Wilcoxon p):

| arm | late - early, from theta0 | knowledge - early | organization - early | improved artifact - orig, early improver | late - early, from improved |
|---|---|---|---|---|---|
| none | +0.0000; 0/0; 1 | +0.0000; 0/0; 1 | +0.0000; 0/0; 1 | +0.0275; 10/2; 0.00244 | +0.0000; 0/0; 1 |
| archive | +0.0084; 8/4; 0.0522 | +0.0084; 8/4; 0.0522 | +0.0000; 0/0; 1 | +0.0162; 11/1; 0.00244 | -0.0046; 4/8; 0.519 |
| public | +0.0100; 8/4; 0.151 | +0.0000; 0/0; 1 | +0.0089; 6/6; 0.424 | +0.0118; 11/1; 0.0342 | -0.0004; 7/5; 0.97 |
| own | +0.0122; 9/2; 0.083 | +0.0000; 0/0; 1 | +0.0112; 8/3; 0.147 | +0.0115; 11/1; 0.0342 | -0.0133; 6/5; 0.898 |
| external | +0.0122; 7/1; 0.0234 | +0.0000; 0/0; 1 | +0.0154; 7/1; 0.0156 | -0.0015; 9/3; 0.064 | +0.0018; 4/4; 0.547 |
| layered | +0.0167; 9/2; 0.00684 | +0.0000; 0/0; 1 | +0.0131; 8/3; 0.0244 | +0.0327; 12/0; 0.000488 | -0.0004; 4/6; 1 |

## Phase 3: damage to the improver's diagnostic machinery

The later improver applied to the lineage's evolved artifact for 10 generations with its suite lesioned from the start: generate (damage and out-of-family cases silently replaced by ordinary ones), admit (failed damage and out-of-family episodes dropped from the score), score (a bonus to the incumbent), obsolete (the successor inherits the starting settings and an empty record); _nocanary removes the suite's self-test. Means over lineages.

| arm | damage | flagged | flagged at gen 0 | held-out | public | damage /72 | oof /24 | self-check off |
|---|---|---|---|---|---|---|---|---|
| none | sham | 0/12 | 0 | -0.067 | -0.058 | 72.0 | 19.4 | 0 |
| none | generate | 12/12 | 12 | -0.071 | -0.064 | 71.8 | 20.2 | 0 |
| none | admit | 12/12 | 12 | -0.071 | -0.064 | 71.8 | 20.2 | 0 |
| none | score | 0/12 | 0 | -0.069 | -0.062 | 71.8 | 20.4 | 0 |
| none | obsolete | 0/12 | 0 | -0.067 | -0.058 | 72.0 | 19.4 | 0 |
| none | generate_nocanary | 0/12 | 0 | -0.351 | -0.053 | 12.0 | 19.2 | 10 |
| none | admit_nocanary | 0/12 | 0 | -0.325 | -0.056 | 17.8 | 17.6 | 9 |
| archive | sham | 0/12 | 0 | -0.073 | -0.065 | 71.5 | 19.2 | 0 |
| archive | generate | 12/12 | 12 | -0.077 | -0.071 | 71.5 | 20.0 | 0 |
| archive | admit | 12/12 | 12 | -0.077 | -0.071 | 71.5 | 20.0 | 0 |
| archive | score | 0/12 | 0 | -0.074 | -0.068 | 71.5 | 19.6 | 0 |
| archive | obsolete | 0/12 | 0 | -0.068 | -0.062 | 72.0 | 20.3 | 0 |
| archive | generate_nocanary | 0/12 | 0 | -0.074 | -0.066 | 71.5 | 18.5 | 0 |
| archive | admit_nocanary | 0/12 | 0 | -0.074 | -0.066 | 71.5 | 18.5 | 0 |
| public | sham | 0/12 | 0 | -0.128 | -0.065 | 60.0 | 21.6 | 2 |
| public | generate | 7/12 | 7 | -0.163 | -0.067 | 54.0 | 20.0 | 3 |
| public | admit | 7/12 | 7 | -0.163 | -0.067 | 54.0 | 20.0 | 3 |
| public | score | 0/12 | 0 | -0.100 | -0.065 | 66.0 | 20.8 | 1 |
| public | obsolete | 0/12 | 0 | -0.068 | -0.062 | 72.0 | 20.2 | 0 |
| public | generate_nocanary | 0/12 | 0 | -0.158 | -0.062 | 54.0 | 19.9 | 3 |
| public | admit_nocanary | 0/12 | 0 | -0.187 | -0.062 | 48.0 | 19.9 | 4 |
| own | sham | 0/12 | 0 | -0.102 | -0.066 | 65.8 | 20.7 | 1 |
| own | generate | 6/12 | 6 | -0.135 | -0.067 | 60.0 | 19.8 | 2 |
| own | admit | 6/12 | 6 | -0.134 | -0.067 | 60.0 | 19.8 | 2 |
| own | score | 0/12 | 0 | -0.103 | -0.066 | 65.8 | 20.1 | 1 |
| own | obsolete | 0/12 | 0 | -0.068 | -0.062 | 72.0 | 20.1 | 0 |
| own | generate_nocanary | 0/12 | 0 | -0.158 | -0.062 | 54.0 | 19.8 | 3 |
| own | admit_nocanary | 0/12 | 0 | -0.129 | -0.062 | 60.0 | 19.8 | 2 |
| external | sham | 0/12 | 0 | -0.098 | -0.066 | 66.0 | 20.4 | 1 |
| external | generate | 8/12 | 8 | -0.155 | -0.064 | 54.0 | 19.8 | 3 |
| external | admit | 9/12 | 8 | -0.126 | -0.064 | 60.0 | 19.8 | 2 |
| external | score | 0/12 | 0 | -0.098 | -0.065 | 66.0 | 21.5 | 1 |
| external | obsolete | 0/12 | 0 | -0.069 | -0.060 | 71.8 | 19.6 | 0 |
| external | generate_nocanary | 0/12 | 0 | -0.237 | -0.060 | 36.0 | 19.5 | 6 |
| external | admit_nocanary | 0/12 | 0 | -0.237 | -0.060 | 36.0 | 19.4 | 6 |
| layered | sham | 0/12 | 0 | -0.075 | -0.067 | 71.2 | 19.1 | 0 |
| layered | generate | 10/12 | 10 | -0.071 | -0.064 | 72.0 | 20.2 | 0 |
| layered | admit | 10/12 | 10 | -0.071 | -0.064 | 72.0 | 20.2 | 0 |
| layered | score | 0/12 | 0 | -0.070 | -0.066 | 72.0 | 21.8 | 0 |
| layered | obsolete | 0/12 | 0 | -0.067 | -0.059 | 72.0 | 19.7 | 0 |
| layered | generate_nocanary | 0/12 | 0 | -0.068 | -0.061 | 71.8 | 19.4 | 0 |
| layered | admit_nocanary | 0/12 | 0 | -0.072 | -0.062 | 71.2 | 17.9 | 0 |

