# scratch/studies/lead-116/test_assembly_committor.py
# Run: python3 -I -m pytest scratch/studies/lead-116/test_assembly_committor.py -q
import numpy as np
import assembly_committor as ac


def test_gamblers_ruin_closed_form():
    ac._check_gamblers_ruin()  # asserts internally to 1e-12


def test_committor_matches_monte_carlo():
    est, exact = ac._check_committor_vs_montecarlo(ac.default_params(), n_runs=40000, seed=3)
    assert abs(est - exact) < 0.02


def test_committor_bounds_and_boundary():
    q, Q = ac.committor(ac.default_params())
    assert np.all(q >= -1e-12) and np.all(q <= 1 + 1e-12)
    # target states are 1, the sink K is 0
    F, Kset = ac.targets_and_failures(ac.default_params())
    for i in F:
        assert abs(q[i] - 1.0) < 1e-12
    assert abs(q[ac.KSTATE] - 0.0) < 1e-12


def test_generator_rows_sum_to_zero():
    Q = ac.build_Q(ac.default_params())
    assert np.allclose(Q.sum(axis=1), 0.0, atol=1e-10)


def test_committor_solves_the_harmonic_equation():
    """On transient states Q q = 0; on absorbing states q is fixed. Verify Qq=0
    on the transient rows directly."""
    p = ac.default_params()
    q, Q = ac.committor(p)
    F, Kset = ac.targets_and_failures(p)
    absorbing = set(F) | set(Kset)
    trans = [i for i in range(ac.NST) if i not in absorbing]
    resid = Q[trans] @ q
    assert np.allclose(resid, 0.0, atol=1e-10)


def test_nonmonotone_two_nuclei_make_a_trap():
    """CLAIM-599: {a} and {b} each productive, {a,b} a trap, from dynamics."""
    p, q, nm = ac.scenario_nonmonotone()
    assert nm["delta_a"] > 0.05
    assert nm["delta_b"] > 0.05
    assert nm["delta_ab"] < 0.0          # the pair is not productive
    assert nm["q_ab"] < nm["q_a"]        # more bonds, lower committor
    assert nm["q_ab"] < nm["q_b"]


def test_nonmonotone_is_symmetric_in_the_two_seams():
    _, _, nm = ac.scenario_nonmonotone()
    assert abs(nm["q_a"] - nm["q_b"]) < 1e-9


def test_committor_ranking_not_monotone_in_bond_count():
    """A higher-bond-count state exists that has a lower committor than a
    lower-count one: progress does not determine the committor (CLAIM-567)."""
    p, q, _ = ac.scenario_nonmonotone()
    rows = ac.committor_ranking(p, q)
    by = {st: (nb, qq) for st, nb, qq in rows}  # st -> (bond_count, committor)
    # {a} has FEWER bonds than {a,b} but a HIGHER committor
    assert by[("a",)][0] < by[("a", "b")][0]
    assert by[("a",)][1] > by[("a", "b")][1]
    # the full 4-bond state is a trap: more progress, far lower committor than {a}
    assert by[("a", "b", "c", "d")][0] > by[("a",)][0]
    assert by[("a", "b", "c", "d")][1] < by[("a",)][1]


def test_factorial_targeted_stabilisation_of_designed_seam_is_productive():
    fac = ac.scenario_factorial()
    for routing in ("A", "B"):
        assert fac[(routing, "targeted")]["delta_q_N"] > 0
        # targeted stabilisation of the designed seam raises assembly chance vs uniform
        assert (fac[(routing, "targeted")]["q_empty"]
                >= fac[(routing, "uniform")]["q_empty"] - 1e-9)


def test_factorial_stabilising_both_seams_traps():
    """Stabilising both seams locks in the incompatible pair: not productive."""
    fac = ac.scenario_factorial()
    assert fac[("both-seams", "targeted")]["delta_q_N"] < 0
    # and its yield is worse than stabilising a single designed seam
    assert (fac[("both-seams", "targeted")]["yield_1e6"]
            < fac[("A", "targeted")]["yield_1e6"])


def test_allocation_selects_the_form_at_fixed_total():
    """QUESTION-400: at fixed total stock, allocation changes which form results
    (share_A sweeps from 1 to 0) while the attainable set {F_A, F_B} is fixed."""
    alloc = ac.scenario_allocation()
    s = alloc["split_seams"]
    assert s[0]["share_A"] > 0.95       # all seam stock on a -> F_A
    assert s[-1]["share_A"] < 0.05      # all on b -> F_B
    shares = [r["share_A"] for r in s]
    assert all(x >= y - 1e-9 for x, y in zip(shares, shares[1:]))  # monotone decreasing
    # even split across the two seams lowers success vs a single-seam allocation
    assert s[0]["q_succeed"] > s[len(s) // 2]["q_succeed"]
    # seam-vs-body has an interior optimum (too little seam can't nucleate,
    # too much starves the body and traps)
    sv = alloc["seam_vs_body"]
    qs = [r["q_succeed"] for r in sv]
    assert max(qs) > qs[0] + 0.02 and max(qs) > qs[-1] + 0.02


def test_allocation_budget_is_conserved():
    alloc = ac.scenario_allocation()
    for r in alloc["split_seams"]:
        total = r["conc_a"] + r["conc_b"] + 1.0 + 1.0  # body 1.0 each
        assert abs(total - alloc["budget"]) < 1e-3


def test_persistence_not_implied_by_reaching():
    """CLAIM-566: warming melts a formed fold (survival falls with T) while the
    fold is still reached from empty -- reaching and persisting are distinct."""
    pers = ac.scenario_persistence()
    cold = [r for r in pers if r["T"] == 300.0][0]
    hot = [r for r in pers if r["T"] == 360.0][0]
    # assembly (reached) and persistence (survival) are distinct: the fold is
    # reached far more often than it is still folded at t=10
    assert cold["reached_F"] > cold["survival_t10"] + 0.05
    # survival decays with time, and warming melts it faster (seen at t=1,10)
    assert cold["survival_t1"] > cold["survival_t10"] > cold["survival_t100"] - 1e-9
    assert cold["survival_t10"] > hot["survival_t10"] + 0.01
