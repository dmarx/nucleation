# LEAD-066 progress

- Lead: LEAD-066, "Bound the commutator of Conjecture A's kind for the hierarchy question, reading Nadler and colleagues first".
- Branch: `claude/lead-066-commutator-bound`, cut from origin/staging (15c07a12f).

## Task as understood

The reading half is done: Nadler et al. is LIT-1250, read in NOTE-986; NOTE-985 states the
bound to attempt. LEAD-052 (branch `claude/lead-052-acquisition-phases`, not yet on staging)
shows the exact case: on tree-symmetric data every kernel of inner products and norms commutes
with the level projectors. This lead does the formal half: state and prove a bound on how far
kernel-flow acquisition departs from the level-by-level flow when [A, P_l] != 0, in terms of
the commutator and (corollary) of a perturbation of the data from the tree-symmetric case; say
what it implies for the acquisition order; check numerically with numpy.

## Done

## Next

1. Derivation (README.md).
2. Numerics: `bound.py`, tests, `run.py`, results.
3. File CLAIM (demonstrated) and CASE (executed-study); dated notes on LEAD-066 and QUESTION-217; changelog fragment.

## Choices
