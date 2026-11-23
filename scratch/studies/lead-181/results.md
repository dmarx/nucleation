# LEAD-181 results

a: inquiry units per period (of B = 10); b: remediation cap. 'tied a range': inquiry levels of the policies within two paired standard errors of the best. Learned: 16 gradient-bandit learners, 4000 episodes each; hidden found is the fraction of the 20 hidden requirements recognized by the end; violations at the end of the episode, of 30 requirements (about 9 violated at the start).

| setting | regime | optimal (a, b) | tied a range | learned mean a | learned hidden found | true viol (learned) | recognized viol (learned) |
|---|---|---|---|---|---|---|---|
| S1 costly inquiry | pen | (0, 6) | 0-0 | 0.01 (sd 0.00) | 0.00 | 6.07 | 0.00 |
| S1 costly inquiry | amnesty | (0, 6) | 0-0 | 0.32 (sd 0.46) | 0.28 | 4.43 | 0.02 |
| S1 costly inquiry | none | (0, 0) | 0-0 | 0.00 (sd 0.00) | 0.00 | 6.84 | 0.76 |
| S1 costly inquiry | disc | (1, 6) | 1-1 | 0.88 (sd 0.48) | 0.72 | 1.76 | 0.06 |
| S1 costly inquiry | ext | (5, 6) | 5-6 | 4.94 (sd 0.90) | 1.00 | 0.00 | 0.00 |
| S2 costless inquiry and remediation | pen | (0, 6) | 0-0 | 0.01 (sd 0.00) | 0.00 | 6.06 | 0.00 |
| S2 costless inquiry and remediation | amnesty | (0, 6) | 0-4 | 3.19 (sd 1.60) | 0.90 | 0.62 | 0.01 |
| S2 costless inquiry and remediation | none | (0, 0) | 0-6 | 3.00 (sd 0.00) | 0.84 | 3.03 | 2.04 |
| S2 costless inquiry and remediation | disc | (4, 6) | 3-4 | 3.91 (sd 1.52) | 0.99 | 0.08 | 0.01 |
| S2 costless inquiry and remediation | ext | (6, 6) | 6-6 | 5.31 (sd 0.77) | 1.00 | 0.00 | 0.00 |
| S3 S1 + surfacing s=0.03 | pen | (0, 6) | 0-0 | 0.19 (sd 0.39) | 0.55 | 2.81 | 0.09 |
| S3 S1 + surfacing s=0.03 | amnesty | (0, 6) | 0-0 | 0.32 (sd 0.46) | 0.61 | 2.45 | 0.09 |
| S3 S1 + surfacing s=0.03 | none | (0, 0) | 0-0 | 0.13 (sd 0.33) | 0.52 | 4.26 | 1.35 |
| S3 S1 + surfacing s=0.03 | disc | (1, 6) | 1-1 | 1.01 (sd 0.35) | 0.91 | 0.62 | 0.06 |
| S3 S1 + surfacing s=0.03 | ext | (5, 6) | 5-5 | 4.52 (sd 0.93) | 1.00 | 0.00 | 0.00 |
| S4 S3 + cost of being found out sigma=3 | pen | (0, 6) | 0-0 | 0.36 (sd 0.46) | 0.63 | 2.34 | 0.08 |
| S4 S3 + cost of being found out sigma=3 | amnesty | (1, 6) | 1-1 | 0.95 (sd 0.43) | 0.88 | 0.80 | 0.06 |
| S4 S3 + cost of being found out sigma=3 | none | (1, 4) | 1-1 | 1.13 (sd 0.33) | 0.94 | 0.41 | 0.05 |
| S4 S3 + cost of being found out sigma=3 | disc | (2, 6) | 2-2 | 1.74 (sd 0.95) | 0.96 | 0.28 | 0.04 |
| S4 S3 + cost of being found out sigma=3 | ext | (5, 6) | 5-5 | 4.86 (sd 0.90) | 1.00 | 0.00 | 0.00 |
