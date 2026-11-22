# LEAD-061: Golub & Jackson's Proposition 2 with several closed groups

Checks whether Proposition 2 of Golub & Jackson (2010; LIT-999), "a sequence
of convergent stochastic matrices is wise iff s_1(n) -> 0", holds when the
networks have several minimal closed groups, with influence as Theorem 3
defines it and wisdom as Definition 3 defines it.

- `gj_closed_groups.py`: Theorem 3's influence vector and DeGroot limits on a
  several-group matrix; exact probabilities for the audit's counterexample
  (m = n // k groups of size k = ceil(sqrt(ln n)), equal weights,
  Bernoulli(1/2) signals); contrasts that are wise; a Monte Carlo check.
- `test_gj_closed_groups.py`: pytest tests.
- `results.md`: the output of the last run.

Rerun, from this directory (CPU, about a second):

    python3 -m pytest -q -p no:cacheprovider test_gj_closed_groups.py
    python3 -I gj_closed_groups.py > results.md

A `-inf` in the last column of section 3 means the binomial tail is below the
float range (log10 under about -300), not an error.
