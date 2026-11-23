# LEAD-181 results

a: inquiry units per period (of B = 10); b: remediation cap. 'tied a range': inquiry levels of the policies within two paired standard errors of the best. Learned: 16 gradient-bandit learners, 1500 episodes each; hidden found is the fraction of the 20 hidden requirements recognized by the end; violations at the end of the episode, of 30 requirements (about 9 violated at the start).

| setting | regime | optimal (a, b) | tied a range | learned mean a | learned hidden found | true viol (learned) | recognized viol (learned) |
|---|---|---|---|---|---|---|---|
| S1 costly inquiry | pen | (0, 6) | 0-0 | 0.12 (sd 0.06) | 0.04 | 5.85 | 0.01 |
| S1 costly inquiry | amnesty | (0, 6) | 0-0 | 0.78 (sd 0.49) | 0.33 | 4.14 | 0.06 |
| S1 costly inquiry | none | (0, 0) | 0-0 | 0.01 (sd 0.00) | 0.00 | 7.38 | 1.33 |
| S1 costly inquiry | disc | (1, 6) | 1-1 | 1.56 (sd 0.32) | 0.73 | 1.72 | 0.09 |
| S1 costly inquiry | ext | (5, 6) | 5-6 | 4.75 (sd 0.67) | 1.00 | 0.05 | 0.03 |
| S2 costless inquiry and remediation | pen | (0, 6) | 0-0 | 0.93 (sd 0.61) | 0.28 | 4.46 | 0.05 |
| S2 costless inquiry and remediation | amnesty | (0, 6) | 0-4 | 2.91 (sd 0.44) | 0.84 | 1.04 | 0.09 |
| S2 costless inquiry and remediation | none | (0, 0) | 0-6 | 3.00 (sd 0.00) | 0.84 | 3.03 | 2.04 |
| S2 costless inquiry and remediation | disc | (4, 6) | 3-4 | 3.12 (sd 0.44) | 0.91 | 0.66 | 0.10 |
| S2 costless inquiry and remediation | ext | (6, 6) | 6-6 | 5.13 (sd 0.67) | 1.00 | 0.03 | 0.02 |
| S3 S1 + surfacing s=0.03 | pen | (0, 6) | 0-0 | 0.46 (sd 0.38) | 0.59 | 2.57 | 0.11 |
| S3 S1 + surfacing s=0.03 | amnesty | (0, 6) | 0-0 | 0.69 (sd 0.44) | 0.65 | 2.21 | 0.11 |
| S3 S1 + surfacing s=0.03 | none | (0, 0) | 0-0 | 0.08 (sd 0.24) | 0.49 | 4.80 | 1.73 |
| S3 S1 + surfacing s=0.03 | disc | (1, 6) | 1-1 | 1.61 (sd 0.38) | 0.90 | 0.69 | 0.10 |
| S3 S1 + surfacing s=0.03 | ext | (5, 6) | 5-5 | 4.57 (sd 0.69) | 1.00 | 0.06 | 0.04 |
| S4 S3 + cost of being found out sigma=3 | pen | (0, 6) | 0-0 | 1.46 (sd 0.31) | 0.83 | 1.15 | 0.11 |
| S4 S3 + cost of being found out sigma=3 | amnesty | (1, 6) | 1-1 | 1.81 (sd 0.44) | 0.91 | 0.67 | 0.11 |
| S4 S3 + cost of being found out sigma=3 | none | (1, 0) | 1-1 | 1.18 (sd 0.34) | 0.94 | 5.32 | 4.97 |
| S4 S3 + cost of being found out sigma=3 | disc | (2, 6) | 2-2 | 2.31 (sd 0.53) | 0.95 | 0.40 | 0.09 |
| S4 S3 + cost of being found out sigma=3 | ext | (5, 6) | 5-5 | 4.53 (sd 0.70) | 1.00 | 0.05 | 0.03 |
