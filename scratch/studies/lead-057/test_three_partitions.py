import numpy as np
import pytest

import three_partitions as tp


def test_stationary_cov_solves_lyapunov():
    M = tp.intrinsic() + tp.apparatus_coupling(0.2)
    G = tp.stationary_cov(M, np.eye(4))
    assert np.allclose(G, M @ G @ M.T + np.eye(4))


def test_unstable_rejected():
    with pytest.raises(ValueError):
        tp.stationary_cov(np.eye(2) * 1.1, np.eye(2))


def test_exactly_decoupled_blocks_lose_nothing():
    M = tp.coupling_matrix(4, tp.PAIRINGS["01|23"], 0.3, 0.4, 0.0)
    assert tp.block_loss(M, tp.PAIRINGS["01|23"]) == pytest.approx(0.0, abs=1e-12)
    assert tp.block_loss(M, tp.PAIRINGS["02|13"]) > 0.01


def test_whole_system_as_one_block_loses_nothing():
    M = tp.intrinsic() + tp.apparatus_coupling(0.35)
    assert tp.block_loss(M, [[0, 1, 2, 3]]) == pytest.approx(0.0, abs=1e-12)


def test_analytic_loss_matches_simulation():
    M = tp.intrinsic() + tp.apparatus_coupling(0.35)
    for P in tp.PAIRINGS.values():
        a = tp.block_loss(M, P)
        s = tp.simulated_block_loss(M, P, T=100_000, seed=3)
        assert s == pytest.approx(a, abs=0.01)


def test_recovered_follows_the_stronger_coupling():
    assert tp.recovered(tp.intrinsic())[0] == "01|23"
    assert tp.recovered(tp.intrinsic() + tp.apparatus_coupling(0.35))[0] == "02|13"
    assert tp.recovered(tp.intrinsic() + tp.apparatus_coupling(0.1))[0] == "01|23"


def test_scenario_assignments():
    out = {k: tp.assign(p, M)[0] for k, (M, p) in tp.scenarios().items()}
    assert out["S0 no apparatus"] == {"F": "01|23", "R": "01|23", "Arr": None}
    assert out["S1 apparatus in place, gain g"] == {"F": "01|23", "R": "02|13", "Arr": "02|13"}
    assert out["S2 apparatus in place, gain 0"] == {"F": "01|23", "R": "01|23", "Arr": "02|13"}
    assert out["S3 apparatus removed, its coupling persists"] == {"F": "01|23", "R": "02|13", "Arr": None}
    assert out["S4 no apparatus, internal rewiring to 03|12"]["R"] == "03|12"


def test_probe_joins_the_unit_it_couples():
    best, _, rho = tp.probe_variant()
    assert rho < 1
    assert best == "024|135"


def test_containment_is_a_share():
    M = tp.intrinsic()
    c = tp.containment(M, 0, [0, 1])
    assert 0 < c <= 1
