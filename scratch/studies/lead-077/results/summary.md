# LEAD-077 results

Post-reversal held-out MSE (episodes 42–83), mean over seeds; governance (G) against router (R) paired by seed. A win is lower error. serve_old: weight still on each region's pre-reversal specialist over the last 10 episodes.

## full

| tau | n | fixed | oracle | governance | conformity | router |
|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1626 (0.00) | 0.2762 (0.04) | 0.1688 (0.01) |
| 0.1 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1625 (0.00) | 0.2767 (0.02) | 0.1660 (0.01) |
| 0.3 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1557 (0.03) | 0.2656 (0.02) | 0.1534 (0.05) |

- tau 0.03: governance vs router: pre-reversal diff -0.0101 (G wins 12); post: governance wins 12/12, mean diff -0.0062 (sd 0.0029), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff -0.0078 (G wins 11); post: governance wins 11/12, mean diff -0.0034 (sd 0.0023), sign p = 0.00635
- tau 0.3: governance vs router: pre-reversal diff -0.0070 (G wins 12); post: governance wins 1/12, mean diff +0.0023 (sd 0.0022), sign p = 0.00635

## bandit

| tau | n | fixed | oracle | governance | conformity | router | governance_explore | router_explore |
|---|---|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.2104 (0.04) | 0.2762 (0.04) | 0.1681 (0.02) | 0.1790 (0.00) | 0.1730 (0.02) |
| 0.1 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1851 (0.01) | 0.2767 (0.02) | 0.1663 (0.02) | 0.1741 (0.01) | 0.1694 (0.03) |
| 0.3 | 8 | 0.2530 (0.25) | 0.1489 (0.00) | 0.1679 (0.04) | 0.2708 (0.02) | 0.1635 (0.08) | 0.1640 (0.04) | 0.1687 (0.08) |

- tau 0.03: governance vs router: pre-reversal diff -0.0082 (G wins 10); post: governance wins 0/12, mean diff +0.0422 (sd 0.0198), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff -0.0040 (G wins 9); post: governance wins 1/12, mean diff +0.0187 (sd 0.0146), sign p = 0.00635
- tau 0.3: governance vs router: pre-reversal diff -0.0121 (G wins 8); post: governance wins 2/8, mean diff +0.0044 (sd 0.0089), sign p = 0.289
- tau 0.03: governance_explore vs router_explore: pre-reversal diff -0.0110 (G wins 12); post: governance_explore wins 2/12, mean diff +0.0059 (sd 0.0057), sign p = 0.0386
- tau 0.1: governance_explore vs router_explore: pre-reversal diff -0.0110 (G wins 12); post: governance_explore wins 3/12, mean diff +0.0047 (sd 0.0066), sign p = 0.146
- tau 0.3: governance_explore vs router_explore: pre-reversal diff -0.0188 (G wins 8); post: governance_explore wins 8/8, mean diff -0.0047 (sd 0.0037), sign p = 0.00781


## Each method at its best pre-reversal temperature

| arm | pair | tau G | tau R | G pre | R pre | G post | R post | G wins post | p |
|---|---|---|---|---|---|---|---|---|---|
| full | governance vs router | 0.3 | 0.3 | 0.1374 | 0.1444 | 0.1557 | 0.1534 | 1/12 | 0.00635 |
| bandit | governance vs router | 0.3 | 0.1 | 0.1410 | 0.1523 | 0.1679 | 0.1684 | 5/8 | 0.727 |
| bandit | governance_explore vs router_explore | 0.3 | 0.1 | 0.1413 | 0.1614 | 0.1640 | 0.1705 | 7/8 | 0.0703 |
