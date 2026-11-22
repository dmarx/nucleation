import inspect
import sys
from dataclasses import replace
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))

import measures  # noqa: E402
from orgmodel import World, simulate, schedule  # noqa: E402

DENIED = World("denied", auth="none", b=0.4)
UNREG = World("unregistered", g_range=(0, 0), auth="tolerance", b=0.4)
ACCOM = World("accommodation", auth="tolerance", tol_mode="compensation", b=0.6)


def test_schedule_declines_progressively():
    v = schedule()
    assert v[0] == 1.0 and np.isclose(v[-1], -0.8)
    assert np.all(np.diff(v) <= 0)
    assert np.sum(np.diff(v) < 0) > 50  # not a one-step drop


def test_measures_read_observables_only():
    for name in ["registration_passive", "registration_interventional",
                 "authority_interventional", "behaviour_features"]:
        params = list(inspect.signature(getattr(measures, name)).parameters)
        assert params[0] == "obs"
        assert not any(p in ("lat", "world", "latent", "g") for p in params)


def test_denied_and_unregistered_behave_identically_by_construction():
    o1, _ = simulate(DENIED, 50, 7)
    o2, _ = simulate(UNREG, 50, 7)
    assert np.array_equal(o1.pursued, o2.pursued)
    assert np.allclose(o1.assay, o2.assay)
    assert not np.allclose(o1.record, o2.record)


def test_ftest_detects_and_holds_size():
    rng = np.random.default_rng(0)
    X0 = np.column_stack([np.ones(300), rng.standard_normal(300)])
    X1 = rng.standard_normal((300, 3))
    y_null = X0 @ [1, 2] + rng.standard_normal(300)
    y_alt = y_null + X1 @ [0.5, 0, 0]
    assert measures._ftest(y_null, X0, X1) < 2
    assert measures._ftest(y_alt, X0, X1) > 5


def test_interventional_registration_null_is_calibrated():
    o, _ = simulate(UNREG, 300, 3)
    sc = measures.registration_interventional(o)
    frac = np.mean(sc > -np.log10(0.05))
    assert 0.01 < frac < 0.10


def test_interventional_registration_detects_registered():
    o, _ = simulate(DENIED, 100, 4)
    assert np.mean(measures.registration_interventional(o) > 2) > 0.9


def test_decoy_fools_passive_not_interventional():
    w = replace(UNREG, decoy_intero=True)
    o, _ = simulate(w, 200, 5)
    assert np.mean(measures.registration_passive(o) > 2) > 0.5
    assert np.mean(measures.registration_interventional(o) > 2) < 0.05


def test_auc():
    assert measures.auc(np.array([2, 3]), np.array([0, 1])) == 1.0
    assert measures.auc(np.array([0, 1]), np.array([2, 3])) == 0.0
