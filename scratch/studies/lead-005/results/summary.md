# LEAD-005 results

Random systems: 4 states, 3-symbol Markov drive, Metropolis kernels (one sweep), energies uniform in [0, 3] k_BT, tau = 6 steps, started in equilibrium.

## Without feedback (the paper's setting): 300 instances

- max |error| of Eq. 14 per step: 1.1e-15; Eq. 17: 2.7e-15; Eq. 19: 2.2e-15; first law: 2.2e-15
- Monte Carlo (200000 trajectories) agrees with exact <W> and <Q> within 4 s.e. in 20 of 20 instances
- relaxation term sum dF_relax <= 0 in 300 of 300
- Eq. 18 lower bound (nostalgia <= beta W_diss) holds in 300 of 300; min slack 0.0095
- Eq. 21 (heat out >= I_e + nostalgia) holds in 300 of 300
- some step's nostalgia negative in 0 of 300; summed nostalgia negative in 0; W_diss negative in 0; W_ex negative in 0; min W_ex 0.0145
- per-protocol reading of Eqs. 9-10: bound holds in 300 of 300; min slack 0.0095

## With feedback (drive depends on the system's state): 500 instances

- max |error| of Eq. 14 per step: 1.2e-15; Eq. 17: 2.2e-15; Eq. 19: 2.0e-15; first law: 1.8e-15
- Monte Carlo (200000 trajectories) agrees with exact <W> and <Q> within 4 s.e. in 20 of 20 instances
- relaxation term sum dF_relax <= 0 in 500 of 500
- Eq. 18 lower bound (nostalgia <= beta W_diss) holds in 500 of 500; min slack 0.1639
- Eq. 21 (heat out >= I_e + nostalgia) holds in 500 of 500
- some step's nostalgia negative in 405 of 500; summed nostalgia negative in 323; W_diss negative in 6; W_ex negative in 6; min W_ex -0.2877

## Feedback toy: partitions of the percept (u, v, y)

- predictive, random actions: {v}
- predictive, own closed loop a = u: {v}
- predictive, fixed action a = 0: {u,v}
- interventional, target the outcome y: {u}
- interventional, target the whole next percept: {u,v}

## Feedback toy: memories (per step, stationary, nats)

| eps | delta | gap | memory | policy | success | I_mem | I_pred | nostalgia | relax | heat/step | H[S_t|S_t+1] |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.1 | 0.05 | 6.0 | none | best | 0.500 | 0.000 | 0.000 | 0.000 | -0.000 | -0.000 | 0.000 |
| 0.1 | 0.05 | 6.0 | predictive {v} | best | 0.500 | 0.676 | 0.364 | 0.312 | 0.285 | 0.597 | 0.334 |
| 0.1 | 0.05 | 6.0 | interventional {u} | best | 0.948 | 0.676 | -0.000 | 0.676 | 2.309 | 2.985 | 0.693 |
| 0.1 | 0.05 | 6.0 | interventional {u} | a=0 | 0.500 | 0.676 | 0.488 | 0.188 | 2.797 | 2.985 | 0.693 |
| 0.1 | 0.05 | 6.0 | u and v | best | 0.946 | 1.335 | 0.360 | 0.975 | 2.293 | 3.268 | 1.035 |
| 0.1 | 0.05 | 6.0 | full {u,v,y} | best | 0.941 | 1.514 | 0.355 | 1.158 | 2.350 | 3.508 | 1.293 |
| 0.02 | 0.0 | 10.0 | none | best | 0.500 | 0.000 | 0.000 | 0.000 | -0.000 | -0.000 | 0.000 |
| 0.02 | 0.0 | 10.0 | predictive {v} | best | 0.500 | 0.693 | 0.595 | 0.098 | 0.102 | 0.200 | 0.098 |
| 0.02 | 0.0 | 10.0 | interventional {u} | best | 1.000 | 0.693 | 0.000 | 0.693 | 4.307 | 5.000 | 0.693 |
| 0.02 | 0.0 | 10.0 | interventional {u} | a=0 | 0.500 | 0.693 | 0.693 | 0.000 | 5.000 | 5.000 | 0.693 |
| 0.02 | 0.0 | 10.0 | u and v | best | 1.000 | 1.385 | 0.595 | 0.790 | 4.309 | 5.099 | 0.792 |
| 0.02 | 0.0 | 10.0 | full {u,v,y} | best | 1.000 | 1.386 | 0.595 | 0.791 | 4.308 | 5.099 | 0.795 |
| 0.3 | 0.1 | 4.0 | none | best | 0.500 | 0.000 | 0.000 | 0.000 | -0.000 | -0.000 | 0.000 |
| 0.3 | 0.1 | 4.0 | predictive {v} | best | 0.500 | 0.603 | 0.076 | 0.527 | 0.630 | 1.157 | 0.622 |
| 0.3 | 0.1 | 4.0 | interventional {u} | best | 0.886 | 0.603 | 0.000 | 0.603 | 1.325 | 1.928 | 0.693 |
| 0.3 | 0.1 | 4.0 | interventional {u} | a=0 | 0.500 | 0.603 | 0.338 | 0.265 | 1.663 | 1.928 | 0.693 |
| 0.3 | 0.1 | 4.0 | u and v | best | 0.872 | 1.124 | 0.072 | 1.053 | 1.366 | 2.419 | 1.325 |
| 0.3 | 0.1 | 4.0 | full {u,v,y} | best | 0.848 | 1.308 | 0.070 | 1.238 | 1.294 | 2.532 | 1.829 |
| 0.1 | 0.05 | 12.0 | none | best | 0.500 | 0.000 | 0.000 | 0.000 | -0.000 | -0.000 | 0.000 |
| 0.1 | 0.05 | 12.0 | predictive {v} | best | 0.500 | 0.693 | 0.368 | 0.325 | 0.875 | 1.200 | 0.325 |
| 0.1 | 0.05 | 12.0 | interventional {u} | best | 0.950 | 0.693 | 0.000 | 0.693 | 5.307 | 6.000 | 0.693 |
| 0.1 | 0.05 | 12.0 | interventional {u} | a=0 | 0.500 | 0.693 | 0.495 | 0.198 | 5.801 | 6.000 | 0.693 |
| 0.1 | 0.05 | 12.0 | u and v | best | 0.950 | 1.386 | 0.368 | 1.018 | 5.582 | 6.600 | 1.018 |
| 0.1 | 0.05 | 12.0 | full {u,v,y} | best | 0.950 | 1.584 | 0.368 | 1.216 | 5.896 | 7.113 | 1.217 |
