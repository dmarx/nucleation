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
| 0.3 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1664 (0.05) | 0.2656 (0.02) | 0.1620 (0.08) | 0.1625 (0.04) | 0.1666 (0.07) |

- tau 0.03: governance vs router: pre-reversal diff -0.0082 (G wins 10); post: governance wins 0/12, mean diff +0.0422 (sd 0.0198), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff -0.0040 (G wins 9); post: governance wins 1/12, mean diff +0.0187 (sd 0.0146), sign p = 0.00635
- tau 0.3: governance vs router: pre-reversal diff -0.0125 (G wins 12); post: governance wins 3/12, mean diff +0.0044 (sd 0.0097), sign p = 0.146
- tau 0.03: governance_explore vs router_explore: pre-reversal diff -0.0110 (G wins 12); post: governance_explore wins 2/12, mean diff +0.0059 (sd 0.0057), sign p = 0.0386
- tau 0.1: governance_explore vs router_explore: pre-reversal diff -0.0110 (G wins 12); post: governance_explore wins 3/12, mean diff +0.0047 (sd 0.0066), sign p = 0.146
- tau 0.3: governance_explore vs router_explore: pre-reversal diff -0.0172 (G wins 12); post: governance_explore wins 12/12, mean diff -0.0041 (sd 0.0037), sign p = 0.000488

## capture50

| tau | n | fixed | oracle | governance | conformity | router |
|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1789 (0.00) | 0.2762 (0.04) | 0.1831 (0.01) |
| 0.1 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1787 (0.00) | 0.2767 (0.02) | 0.1797 (0.02) |
| 0.3 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1711 (0.02) | 0.2656 (0.02) | 0.1634 (0.04) |

- tau 0.03: governance vs router: pre-reversal diff -0.0214 (G wins 12); post: governance wins 10/12, mean diff -0.0042 (sd 0.0038), sign p = 0.0386
- tau 0.1: governance vs router: pre-reversal diff -0.0192 (G wins 12); post: governance wins 8/12, mean diff -0.0011 (sd 0.0037), sign p = 0.388
- tau 0.3: governance vs router: pre-reversal diff -0.0138 (G wins 12); post: governance wins 0/12, mean diff +0.0077 (sd 0.0030), sign p = 0.000488

## capture80

| tau | n | fixed | oracle | governance | conformity | router |
|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1929 (0.00) | 0.2762 (0.04) | 0.1729 (0.01) |
| 0.1 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1919 (0.00) | 0.2767 (0.02) | 0.1713 (0.01) |
| 0.3 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1827 (0.02) | 0.2656 (0.02) | 0.1588 (0.02) |

- tau 0.03: governance vs router: pre-reversal diff -0.0083 (G wins 11); post: governance wins 0/12, mean diff +0.0200 (sd 0.0051), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff -0.0075 (G wins 11); post: governance wins 0/12, mean diff +0.0206 (sd 0.0052), sign p = 0.000488
- tau 0.3: governance vs router: pre-reversal diff -0.0060 (G wins 12); post: governance wins 0/12, mean diff +0.0239 (sd 0.0049), sign p = 0.000488

## scale

| tau | n | fixed | oracle | governance | conformity | router | governance_raw | router_std |
|---|---|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1628 (0.00) | 0.2762 (0.04) | 0.2200 (0.22) | 0.2606 (0.24) | 0.1706 (0.01) |
| 0.1 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1609 (0.00) | 0.2767 (0.02) | 0.2118 (0.18) | 0.2402 (0.17) | 0.1676 (0.02) |
| 0.3 | 12 | 0.2484 (0.25) | 0.1472 (0.00) | 0.1720 (0.10) | 0.2656 (0.02) | 0.2195 (0.18) | 0.2380 (0.17) | 0.1608 (0.03) |

- tau 0.03: governance vs router: pre-reversal diff -0.0615 (G wins 12); post: governance wins 12/12, mean diff -0.0572 (sd 0.0094), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff -0.0585 (G wins 12); post: governance wins 12/12, mean diff -0.0509 (sd 0.0075), sign p = 0.000488
- tau 0.3: governance vs router: pre-reversal diff -0.0548 (G wins 12); post: governance wins 12/12, mean diff -0.0476 (sd 0.0053), sign p = 0.000488
- tau 0.03: governance vs router_std: pre-reversal diff -0.0145 (G wins 12); post: governance wins 12/12, mean diff -0.0078 (sd 0.0034), sign p = 0.000488
- tau 0.1: governance vs router_std: pre-reversal diff -0.0132 (G wins 12); post: governance wins 12/12, mean diff -0.0066 (sd 0.0029), sign p = 0.000488
- tau 0.3: governance vs router_std: pre-reversal diff +0.0060 (G wins 3); post: governance wins 1/12, mean diff +0.0112 (sd 0.0055), sign p = 0.00635
- tau 0.03: governance_raw vs router: pre-reversal diff +0.0415 (G wins 0); post: governance_raw wins 0/12, mean diff +0.0405 (sd 0.0077), sign p = 0.000488
- tau 0.1: governance_raw vs router: pre-reversal diff +0.0311 (G wins 0); post: governance_raw wins 0/12, mean diff +0.0284 (sd 0.0056), sign p = 0.000488
- tau 0.3: governance_raw vs router: pre-reversal diff +0.0249 (G wins 0); post: governance_raw wins 0/12, mean diff +0.0184 (sd 0.0050), sign p = 0.000488

## cycles

| tau | n | fixed | oracle | governance | conformity | router |
|---|---|---|---|---|---|---|
| 0.03 | 12 | 0.2090 (0.33) | 0.2322 (0.00) | 0.2174 (0.34) | 0.2410 (0.31) | 0.2073 (0.33) |
| 0.1 | 12 | 0.2090 (0.33) | 0.2322 (0.00) | 0.2142 (0.34) | 0.2410 (0.31) | 0.2043 (0.33) |
| 0.3 | 12 | 0.2090 (0.33) | 0.2322 (0.00) | 0.2098 (0.34) | 0.2374 (0.25) | 0.1949 (0.33) |

- tau 0.03: governance vs router: pre-reversal diff +0.0081 (G wins 1); post: governance wins 0/12, mean diff +0.0101 (sd 0.0048), sign p = 0.000488
- tau 0.1: governance vs router: pre-reversal diff +0.0086 (G wins 1); post: governance wins 0/12, mean diff +0.0099 (sd 0.0051), sign p = 0.000488
- tau 0.3: governance vs router: pre-reversal diff +0.0147 (G wins 0); post: governance wins 0/12, mean diff +0.0150 (sd 0.0055), sign p = 0.000488

## training

| tau | n | fixed | oracle | governance | conformity | router |
|---|---|---|---|---|---|---|
| 0.03 | 7 | 0.2554 (0.25) | 0.1495 (0.00) | 0.1652 (0.00) | 0.2170 (0.04) | 0.1700 (0.01) |

- tau 0.03: governance vs router: pre-reversal diff -0.0078 (G wins 7); post: governance wins 7/7, mean diff -0.0049 (sd 0.0028), sign p = 0.0156


## Each method at its best pre-reversal temperature

| arm | pair | tau G | tau R | G pre | R pre | G post | R post | G wins post | p |
|---|---|---|---|---|---|---|---|---|---|
| full | governance vs router | 0.3 | 0.3 | 0.1374 | 0.1444 | 0.1557 | 0.1534 | 1/12 | 0.00635 |
| bandit | governance vs router | 0.3 | 0.3 | 0.1384 | 0.1509 | 0.1664 | 0.1620 | 3/12 | 0.146 |
| bandit | governance_explore vs router_explore | 0.3 | 0.3 | 0.1383 | 0.1555 | 0.1625 | 0.1666 | 12/12 | 0.000488 |
| capture50 | governance vs router | 0.3 | 0.3 | 0.1392 | 0.1530 | 0.1711 | 0.1634 | 0/12 | 0.000488 |
| capture80 | governance vs router | 0.3 | 0.3 | 0.1396 | 0.1457 | 0.1827 | 0.1588 | 0/12 | 0.000488 |
| scale | governance vs router | 0.1 | 0.1 | 0.1450 | 0.2035 | 0.1609 | 0.2118 | 12/12 | 0.000488 |
| scale | governance vs router_std | 0.1 | 0.3 | 0.1450 | 0.1517 | 0.1609 | 0.1608 | 6/12 | 1 |
| scale | governance_raw vs router | 0.1 | 0.1 | 0.2346 | 0.2035 | 0.2402 | 0.2118 | 0/12 | 0.000488 |
| cycles | governance vs router | 0.3 | 0.3 | 0.2100 | 0.1953 | 0.2098 | 0.1949 | 0/12 | 0.000488 |
| training | governance vs router | 0.03 | 0.03 | 0.1525 | 0.1603 | 0.1652 | 0.1700 | 7/7 | 0.0156 |
