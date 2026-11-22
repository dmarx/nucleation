# LEAD-160 results (1 mazes, 8x8, seeds 0-0)

Mean over mazes, [min, max] where they differ.

## Test 1: competence at matched levels (same training stream for all three)

| level | transitions | success M / P / D | path excess M / P / D | action agreement M-P / M-D |
|---|---|---|---|---|
| succ>=0.5 | 831 | 0.562 / 0.562 / 0.562 | 1.286 / 1.286 / 1.286 | 1.000 / 0.975 |
| succ>=0.8 | 1203 | 0.879 / 0.879 / 0.879 | 1.034 / 1.034 / 1.040 | 1.000 / 0.950 |
| succ>=1.0 | 1695 | 1.000 / 1.000 / 1.000 | 1.017 / 1.017 / 1.030 | 1.000 / 0.922 |
| full_coverage | 2791 | 1.000 / 1.000 / 1.000 | 1.000 / 1.000 / 1.002 | 1.000 / 0.936 |

Resources at full coverage (first maze): M: memory 256 numbers; P: memory 16384 numbers; D: memory 16384 numbers. Training updates (unit writes to convergence, full coverage): M 2791; P 5632; D 173568

## Test 2: on-demand queries (accuracy against the true maze)

### succ>=0.5

| query | M | P | D | P without extraction |
|---|---|---|---|---|
| Q1_next | 0.848 | 0.848 | 0.848 |  |
| Q2_dist | 0.451 | 0.451 | 0.451 |  |
| Q3_occ | 0.000 | 0.000 | 0.000 |  |
| Q4_dist_do | 0.441 | 0.441 | 0.441 | 0.364 |
| Q4_occ_do | 0.000 | 0.000 | 0.000 |  |

Fraction of pairs whose distance the intervention changes: 0.146

### succ>=0.8

| query | M | P | D | P without extraction |
|---|---|---|---|---|
| Q1_next | 0.949 | 0.949 | 0.949 |  |
| Q2_dist | 0.827 | 0.827 | 0.827 |  |
| Q3_occ | 0.000 | 0.000 | 0.000 |  |
| Q4_dist_do | 0.812 | 0.812 | 0.812 | 0.689 |
| Q4_occ_do | 0.000 | 0.000 | 0.000 |  |

Fraction of pairs whose distance the intervention changes: 0.146

### succ>=1.0

| query | M | P | D | P without extraction |
|---|---|---|---|---|
| Q1_next | 0.992 | 0.992 | 0.992 |  |
| Q2_dist | 0.968 | 0.968 | 0.968 |  |
| Q3_occ | 0.000 | 0.000 | 0.000 |  |
| Q4_dist_do | 0.964 | 0.964 | 0.964 | 0.822 |
| Q4_occ_do | 0.000 | 0.000 | 0.000 |  |

Fraction of pairs whose distance the intervention changes: 0.146

### full_coverage

| query | M | P | D | P without extraction |
|---|---|---|---|---|
| Q1_next | 1.000 | 1.000 | 1.000 |  |
| Q2_dist | 1.000 | 1.000 | 1.000 |  |
| Q3_occ | 1.000 | 1.000 | 1.000 |  |
| Q4_dist_do | 1.000 | 1.000 | 1.000 | 0.854 |
| Q4_occ_do | 1.000 | 1.000 | 1.000 |  |

Fraction of pairs whose distance the intervention changes: 0.146

### Cost of each agent's procedure (elementary operations, S = 64)

| query | M | P | D |
|---|---|---|---|
| Q1_next | 1 | 64 | 4,096 |
| Q2_dist | 256 | 4 | 1,048,832 |
| Q3_occ | 262,144 | 278,528 | 4 |
| Q4_dist_do | 258 | 16,642 | 1,048,834 |
| Q4_occ_do | 262,146 | 278,530 | 20 |
| per-decision budget | 256 | 4 | 4 |

Available within the agent's own per-decision budget:

- Q1_next: M
- Q2_dist: M, P
- Q3_occ: D
- Q4_dist_do: 
- Q4_occ_do: 

Available within a common budget of 256 (the planner's):

- Q1_next: M, P
- Q2_dist: M, P
- Q3_occ: D
- Q4_dist_do: 
- Q4_occ_do: D

## Test 3: targeted intervention on the unit carrying a passage (block it)

Success in the blocked maze before and after the edit; 'repaired' is the share of the pairs the unedited agent failed that the edited one solves.

| agent | success before | success after | repaired | path excess after | numbers written |
|---|---|---|---|---|---|
| M | 0.798 [0.763, 0.838] | 1.000 | 1.000 | 1.000 | 2 |
| P | 0.798 [0.763, 0.838] | 0.823 [0.775, 0.898] | 0.133 [0.000, 0.372] | 1.000 | 128 |
| D | 0.814 [0.779, 0.874] | 0.832 [0.790, 0.904] | 0.110 [0.011, 0.236] | 1.002 [1.001, 1.002] | 128 |

## Test 4a: environmental change (block), recovery by online learning from a random walk (5 runs)

| steps | M success | P success | D success | M excess | P excess | D excess |
|---|---|---|---|---|---|---|
| 0 | 0.798 [0.763, 0.838] | 0.798 [0.763, 0.838] | 0.814 [0.779, 0.874] | 1.000 | 1.000 | 1.002 [1.001, 1.003] |
| 30 | 0.818 [0.763, 0.873] | 0.802 [0.763, 0.838] | 0.816 [0.779, 0.874] | 1.000 | 1.000 | 1.002 [1.001, 1.003] |
| 100 | 0.818 [0.763, 0.873] | 0.802 [0.763, 0.838] | 0.816 [0.779, 0.874] | 1.000 | 1.000 | 1.002 [1.001, 1.003] |
| 300 | 0.915 [0.813, 1.000] | 0.821 [0.793, 0.898] | 0.829 [0.781, 0.904] | 1.000 | 1.000 | 1.002 [1.001, 1.003] |
| 1000 | 0.952 [0.873, 1.000] | 0.847 [0.796, 0.919] | 0.860 [0.795, 0.952] | 1.000 | 1.000 | 1.002 [1.001, 1.002] |
| 3000 | 1.000 | 0.900 [0.881, 0.942] | 0.900 [0.862, 0.968] | 1.000 | 1.000 | 1.002 [1.002, 1.003] |
| 10000 | 1.000 | 0.989 [0.977, 1.000] | 0.971 [0.944, 1.000] | 1.000 | 1.000 | 1.002 [1.001, 1.004] |

## Test 4a: environmental change (shortcut), recovery by online learning from a random walk (5 runs)

| steps | M success | P success | D success | M excess | P excess | D excess |
|---|---|---|---|---|---|---|
| 0 | 1.000 | 1.000 | 1.000 | 1.063 [1.056, 1.067] | 1.063 [1.056, 1.067] | 1.065 [1.058, 1.070] |
| 30 | 1.000 | 1.000 | 1.000 | 1.057 [1.031, 1.067] | 1.060 [1.051, 1.067] | 1.063 [1.054, 1.070] |
| 100 | 1.000 | 1.000 | 1.000 | 1.057 [1.031, 1.067] | 1.060 [1.051, 1.067] | 1.063 [1.054, 1.070] |
| 300 | 1.000 | 1.000 | 1.000 | 1.038 [1.000, 1.067] | 1.047 [1.018, 1.067] | 1.049 [1.020, 1.070] |
| 1000 | 1.000 | 1.000 | 1.000 | 1.019 [1.000, 1.067] | 1.026 [1.001, 1.067] | 1.032 [1.010, 1.069] |
| 3000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.001 [1.000, 1.003] | 1.006 [1.002, 1.009] |
| 10000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.000 | 1.002 [1.001, 1.002] |

## Test 4b: damage to 0.1 of the units, recovery by online learning (2 runs)

| steps | M success | P success | D success | M excess | P excess | D excess |
|---|---|---|---|---|---|---|
| 0 | 0.258 [0.240, 0.276] | 0.369 [0.357, 0.380] | 0.384 [0.382, 0.385] | 1.034 [1.020, 1.047] | 1.003 [1.002, 1.005] | 1.004 [1.002, 1.006] |
| 30 | 0.268 [0.253, 0.284] | 0.377 [0.367, 0.387] | 0.393 [0.392, 0.394] | 1.034 [1.019, 1.048] | 1.003 [1.002, 1.004] | 1.011 [1.002, 1.020] |
| 100 | 0.279 [0.271, 0.287] | 0.383 [0.377, 0.388] | 0.404 [0.401, 0.407] | 1.030 [1.018, 1.042] | 1.003 [1.002, 1.004] | 1.015 [1.003, 1.027] |
| 300 | 0.435 [0.376, 0.494] | 0.437 [0.422, 0.451] | 0.487 [0.465, 0.509] | 1.015 [1.015, 1.015] | 1.003 [1.002, 1.004] | 1.003 [1.003, 1.004] |
| 1000 | 0.686 [0.649, 0.723] | 0.536 [0.531, 0.541] | 0.664 [0.618, 0.710] | 1.010 [1.007, 1.012] | 1.005 [1.002, 1.008] | 1.008 [1.002, 1.015] |
| 3000 | 1.000 | 0.653 [0.619, 0.688] | 0.829 [0.769, 0.889] | 1.000 | 1.000 [1.000, 1.001] | 1.002 [1.001, 1.002] |
| 10000 | 1.000 | 0.931 [0.916, 0.946] | 0.935 [0.905, 0.965] | 1.000 | 1.000 | 1.001 [1.001, 1.001] |

Detection by the agent's own error signal at the first revisit of each unit:

| agent | damaged units changed | hit rate | false alarm rate |
|---|---|---|---|
| M | 26 | 1.000 | 0.000 |
| P | 26 | 1.000 | 0.570 [0.530, 0.609] |
| D | 26 | 1.000 | 0.578 [0.548, 0.609] |

## Test 4b: damage to 0.3 of the units, recovery by online learning (2 runs)

| steps | M success | P success | D success | M excess | P excess | D excess |
|---|---|---|---|---|---|---|
| 0 | 0.116 [0.115, 0.116] | 0.122 [0.110, 0.133] | 0.124 [0.117, 0.130] | 1.055 [1.040, 1.070] | 1.003 [1.002, 1.005] | 1.003 [1.002, 1.003] |
| 30 | 0.123 [0.121, 0.124] | 0.124 [0.113, 0.135] | 0.125 [0.117, 0.133] | 1.050 [1.045, 1.055] | 1.006 [1.002, 1.010] | 1.005 [1.002, 1.008] |
| 100 | 0.142 [0.135, 0.149] | 0.148 [0.145, 0.151] | 0.147 [0.143, 0.151] | 1.044 [1.043, 1.044] | 1.004 [1.004, 1.004] | 1.004 [1.003, 1.004] |
| 300 | 0.237 [0.230, 0.244] | 0.217 [0.215, 0.218] | 0.223 [0.214, 0.232] | 1.038 [1.026, 1.049] | 1.002 [1.001, 1.003] | 1.002 [1.001, 1.003] |
| 1000 | 0.482 [0.466, 0.498] | 0.308 [0.285, 0.332] | 0.379 [0.326, 0.432] | 1.002 [1.001, 1.002] | 1.003 [1.002, 1.004] | 1.005 [1.003, 1.006] |
| 3000 | 0.792 [0.773, 0.811] | 0.469 [0.421, 0.518] | 0.569 [0.502, 0.636] | 1.007 [1.005, 1.010] | 1.001 [1.000, 1.002] | 1.001 [1.001, 1.001] |
| 10000 | 1.000 | 0.909 [0.906, 0.913] | 0.896 [0.874, 0.918] | 1.000 | 1.000 [1.000, 1.000] | 1.003 [1.001, 1.005] |

Detection by the agent's own error signal at the first revisit of each unit:

| agent | damaged units changed | hit rate | false alarm rate |
|---|---|---|---|
| M | 75 [73, 77] | 1.000 | 0.000 |
| P | 75 [73, 77] | 1.000 | 0.845 [0.842, 0.849] |
| D | 76 [75, 77] | 1.000 | 0.844 [0.840, 0.849] |

