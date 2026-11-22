"""Tests for LEAD-142's directed-signature study."""
import numpy as np
import directed_signature as d


def test_reduction_identity():
    """Top-d left singular span = eigenspace of the self-adjoint two-step
    chain M, which is reversible: M mu_i = s_i^2 mu_i to machine precision."""
    P = np.array([[0.1, 0.8, 0.1], [0.1, 0.1, 0.8], [0.6, 0.2, 0.2]])
    r = d.check_reduction(P)
    assert r["M_eigfun_residual_max"] < 1e-10
    assert r["M_reversible_defect"] < 1e-10
    assert r["mu_orthonormality_defect"] < 1e-10


def test_reduction_random_nonreversible():
    rng = np.random.default_rng(0)
    for _ in range(20):
        P = rng.random((4, 4)) ** 2
        P = P / P.sum(1, keepdims=True)
        r = d.check_reduction(P)
        assert r["M_eigfun_residual_max"] < 1e-9
        assert r["M_reversible_defect"] < 1e-9


def test_three_state_reproduction():
    r = d.check_three_state()
    assert r["pi"] == [0.287, 0.338, 0.374]
    assert r["singular_values"] == [1.0, 0.655, 0.534]
    # left != right singular functions: genuinely directed
    assert r["left_right_gap"] > 1.0


def test_tie():
    r = d.check_tie()
    assert abs(r["r_star"] - 0.7708) < 1e-3
    assert abs(r["e_top"] - r["r_star"]) < 2e-3
    for th in ["theta=0.05", "theta=0.2", "theta=0.5"]:
        assert abs(r["tilts"][th] - r["e_top"]) < 2e-3  # spans tie
    assert r["tilts"]["theta=1.0"] > r["e_top"] + 0.1   # tilt eventually costs


def test_nonlinear_beats_linear_on_stable_interaction():
    r = d.check_nonlinear()
    # interaction target is stable (view-invariant) yet outside the top-2 span
    assert r["stability_inter"] > 0.5
    assert r["inter_linear_residual_top2"] > 0.99      # linear probe fails
    assert r["inter_nonlinear_residual_top2"] < 1e-9   # nonlinear readout wins


def test_decision_relative_insufficiency():
    r = d.check_nonlinear()
    # a compatible target the top-1 span cannot serve but a competitor can
    assert r["chi_b_residual_from_top1"] > 0.99
    assert r["chi_b_residual_from_competitor"] < 1e-9


def test_direction_obstruction():
    r = d.check_direction()
    assert r["pair_asymmetry"] > 0.05                      # non-reversible
    assert r["direction_error_from_x_only"] > 0.1          # x cannot determine it
    assert r["direction_error_from_pair"] < 1e-12          # the pair determines it
