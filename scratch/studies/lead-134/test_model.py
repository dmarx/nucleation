"""Tests for CASE-114's construction (LEAD-134). Run: python3 -I -m pytest -q"""
import numpy as np
import model as m


def test_simulate_records_true_causes_apart():
    sim = m.simulate(K=5, T=2000, sigmas=[1, 1, 1, 1, 1],
                     fault_rate=0.03, fault_scale=4.0, obs_noise=0.05, seed=0)
    assert sim["fault_t"].shape == sim["fault_j"].shape
    assert len(sim["fault_t"]) == 60               # 0.03 * 2000
    assert sim["obs"].shape == (2000, 5)
    # fault indices are valid components, recorded independently of any model
    assert sim["fault_j"].min() >= 0 and sim["fault_j"].max() < 5


def test_both_models_reconstruct_the_outcome_exactly():
    # the capacity / coarseness defence: both self-models reproduce the
    # aggregate outcome, so neither is a lossy summary of the behaviour.
    sim = m.simulate(6, 1500, [0.5, 0.7, 0.9, 1.1, 1.3, 1.5],
                     0.03, 4.0, 0.05, seed=1)
    acc = m.accurate_attribution(sim["obs"])
    cen = m.centralized_attribution(sim["obs"])
    assert m.aggregate_reconstruction_error(sim["obs"], acc) < 1e-9
    assert m.aggregate_reconstruction_error(sim["obs"], cen) < 1e-9


def test_accurate_localizes_faults_centralized_does_not():
    sim = m.simulate(5, 4000, [0.8, 0.9, 1.0, 1.1, 1.2],
                     0.03, 4.0, 0.05, seed=2)
    ol = m.open_loop(sim)
    loc = ol["localization"]
    # the accurate model names the recorded culprit almost always
    assert loc["accurate_localization_acc"] > 0.9
    # the centralized model, spreading blame uniformly, is near chance and
    # far worse than the accurate one -- a predictable misattribution
    assert loc["centralized_localization_acc"] < 0.5
    assert loc["accurate_localization_acc"] - loc["centralized_localization_acc"] > 0.5


def test_centralized_spreads_mass_uniformly():
    sim = m.simulate(5, 4000, [1, 1, 1, 1, 1], 0.03, 4.0, 0.05, seed=3)
    mass = m.open_loop(sim)["mass"]
    # accurate puts the plurality of attribution mass on the true cause, far
    # more than the uniform 1/K; centralized puts exactly ~1/K on it.
    assert mass["accurate_mass_on_true_cause"] > 0.45
    assert mass["accurate_mass_on_true_cause"] > 2 * mass["centralized_mass_on_true_cause"]
    # centralized puts ~1/K on it (uniform spread -> blames the 'owner')
    assert abs(mass["centralized_mass_on_true_cause"] - 1.0 / 5) < 0.03


def test_authorship_report_centralized_is_near_uniform():
    sim = m.simulate(8, 3000, [1] * 8, 0.03, 4.0, 0.05, seed=4)
    a = m.open_loop(sim)["authorship"]
    # centralized reports near-maximal entropy over components every event
    # (the single owner acting through all effectors); accurate is lower,
    # tracking the one culprit.
    assert a["centralized_report_entropy"] > a["accurate_report_entropy"]
    assert a["centralized_report_entropy"] > 0.9 * a["max_entropy"]


def test_closed_loop_accurate_governs_better():
    kw = dict(K=5, T=4000, sigmas=[0.8, 0.9, 1.0, 1.1, 1.2],
              fault_rate=0.03, fault_scale=15.0, obs_noise=0.05,
              seed=7, rounds=10, lr=0.06)
    acc = m.closed_loop(which="accurate", **kw)
    cen = m.closed_loop(which="centralized", **kw)
    # the robust signature: the centralized model cannot localize the rogue,
    # so to cut errors it suppresses the whole system, stripping more
    # legitimate gain from the INNOCENT components than the accurate model.
    assert acc["innocent_gain_loss_frac"] < cen["innocent_gain_loss_frac"]
    # and it incurs more errors over the course of the revision.
    assert acc["cumulative_err"] < cen["cumulative_err"]


def test_closed_loop_collateral_robust_across_seeds():
    # the collateral signature holds on every seed; the aggregate error favors
    # the accurate model though not on every single seed.
    innocent_wins = 0
    for K, sig in [(3, [0.8, 1.0, 1.2]), (5, [0.8, 0.9, 1.0, 1.1, 1.2])]:
        for seed in range(6):
            kw = dict(K=K, T=4000, sigmas=sig, fault_rate=0.03,
                      fault_scale=15.0, obs_noise=0.05, seed=seed,
                      rounds=10, lr=0.06)
            a = m.closed_loop(which="accurate", **kw)
            c = m.closed_loop(which="centralized", **kw)
            innocent_wins += a["innocent_gain_loss_frac"] < c["innocent_gain_loss_frac"]
    assert innocent_wins == 12


def test_determinism():
    kw = dict(K=4, T=1000, sigmas=[1, 1, 1, 1],
              fault_rate=0.03, fault_scale=4.0, obs_noise=0.05, seed=11)
    a = m.simulate(**kw)
    b = m.simulate(**kw)
    assert np.array_equal(a["obs"], b["obs"])
    assert np.array_equal(a["fault_t"], b["fault_t"])
