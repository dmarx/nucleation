"""The floor on any valid test of no-signalling for one content.

A nonrandomized level-alpha test of H0: p = p' from x ~ Bin(n, p), y ~ Bin(m, p')
can put a table (x, y) in its rejection region only if sup_p P_p(x, y) <= alpha.
This script computes min over tables of sup_p P_p(x, y), checks that it equals
the extreme table's value n^n m^m / (n+m)^(n+m) for n, m <= 40, and prints the
least m for each n at which a 5% (and a 2.5%, Bonferroni for two contents)
test can reject anything. Rerun: python3 -I floor.py > floor.md
"""
from math import comb, log, exp


def sup_table(n, m, x, y):
    N, s = n + m, x + y
    v = log(comb(n, x)) + log(comb(m, y))
    if 0 < s < N:
        v += s * log(s / N) + (N - s) * log((N - s) / N)
    return exp(v)


def extreme(n, m):
    return exp(n * log(n) + m * log(m) - (n + m) * log(n + m))


def main():
    for n in range(1, 41):
        for m in range(1, 41):
            mn = min(sup_table(n, m, x, y) for x in range(n + 1) for y in range(m + 1))
            assert abs(mn - extreme(n, m)) < 1e-12 * max(1, mn), (n, m)
    print("Checked: for all n, m <= 40 the least sup-null probability of any table is n^n m^m/(n+m)^(n+m).\n")
    print("| n (occurrences in one context) | least m for a 5% test to reject anything | least m at 2.5% |")
    print("|---|---|---|")
    for n in range(1, 9):
        l5 = next(m for m in range(1, 1000) if extreme(n, m) <= 0.05)
        l25 = next(m for m in range(1, 1000) if extreme(n, m) <= 0.025)
        print(f"| {n} | {l5} | {l25} |")


if __name__ == "__main__":
    main()
