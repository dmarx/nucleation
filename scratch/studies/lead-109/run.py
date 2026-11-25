"""Produce the headline numbers for LEAD-109. Run: python3 -I run.py"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import factorization as F


def main():
    out = {}

    # 1. Exhaustive crosscut search over random couplings.
    rng = np.random.default_rng(0)
    n = 6
    trials = 2000
    crosscut_ties = 0
    nonempty = 0
    max_family = 0
    for _ in range(trials):
        A = rng.random((n, n))
        M = np.triu(A, 1)
        M = M + M.T
        for tau in (1.0, 1.25, 1.5, 2.0, 3.0, 5.0):
            fam = F.self_consistent_family(M, n, tau)
            if fam:
                nonempty += 1
                max_family = max(max_family, len(fam))
                if not F.is_chain(fam):
                    crosscut_ties += 1
    out["trials"] = trials
    out["tau_values_per_trial"] = 6
    out["nonempty_families"] = nonempty
    out["crosscutting_ties_found"] = crosscut_ties
    out["max_family_size"] = max_family

    # 2. Symmetric 4-ring: the two rotation-related pairings never both clear.
    M = F.np.full((4, 4), 0.3, float)
    for i in range(4):
        M[i, (i + 1) % 4] = M[(i + 1) % 4, i] = 1.0
    np.fill_diagonal(M, 0.0)
    A = F.as_partition([{0, 1}, {2, 3}])
    B = F.as_partition([{1, 2}, {3, 0}])
    out["ring4_pairingA_gap"] = round(F.gap(M, A), 4)
    out["ring4_pairingB_gap"] = round(F.gap(M, B), 4)
    out["ring4_either_clears_tau_1.01"] = bool(
        F.clears_test1(M, A, 1.01) or F.clears_test1(M, B, 1.01))

    # 3. Watchmaker hierarchy: two grains both clear test 1.
    H = np.full((4, 4), 0.02, float)
    H[0, 1] = H[1, 0] = 1.0
    H[2, 3] = H[3, 2] = 1.0
    H[1, 2] = H[2, 1] = 0.3
    np.fill_diagonal(H, 0.0)
    fine = F.as_partition([{0, 1}, {2, 3}])
    coarse = F.as_partition([{0, 1, 2, 3}])
    out["watchmaker_fine_gap"] = round(F.gap(H, fine), 4)
    out["watchmaker_coarse_gap"] = (
        "inf" if np.isinf(F.gap(H, coarse)) else round(F.gap(H, coarse), 4))
    fam1 = F.self_consistent_family(H, 4, 2.0)
    out["watchmaker_test1_family_size"] = len(fam1)
    out["watchmaker_test1_finest_is_singletons"] = bool(
        F.finest(fam1) == F.as_partition([{0}, {1}, {2}, {3}]))
    # with full agent tests: both grains are agents -> 2 factorizations
    t2 = {frozenset({0, 1}): (9.0, 2.0), frozenset({2, 3}): (9.0, 2.0),
          frozenset({0, 1, 2, 3}): (16.0, 3.0)}
    fam2 = F.self_consistent_family(H, 4, 2.0, test2=t2)
    out["watchmaker_agent_factorizations"] = [
        [sorted(b) for b in P] for P in fam2]
    out["watchmaker_agent_family_is_chain"] = bool(F.is_chain(fam2))

    print(json.dumps(out, indent=2))
    with open("results.json", "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
