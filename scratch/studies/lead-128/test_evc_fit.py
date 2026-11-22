#!/usr/bin/env python3
"""Tests for evc_fit: parameter recovery and model comparison on synthetic data.

Run: python3 -I -m pytest test_evc_fit.py -q
"""
import os, tempfile
import numpy as np
import evc_fit as E


def _simulate(n_trials=4000, beta=2.5, c=(0.0, 0.3, 0.6, 1.0), seed=0):
    """Make synthetic (dr, dcost, y) from the model, mimicking the paradigm:
    one option fixed at 2.0, the other titrated in [1.0, 2.0], distinct levels."""
    rng = np.random.default_rng(seed)
    rows = []
    levels = (1, 2, 3, 4)
    for _ in range(n_trials):
        a, b = rng.choice(levels, size=2, replace=False)
        # randomly assign which is fixed at 2.0
        if rng.random() < 0.5:
            rA, rB = 2.0, round(float(rng.uniform(1.0, 2.0)), 2)
        else:
            rA, rB = round(float(rng.uniform(1.0, 2.0)), 2), 2.0
        vA = rA - c[a - 1]
        vB = rB - c[b - 1]
        p = 1.0 / (1.0 + np.exp(-beta * (vA - vB)))
        y = int(rng.random() < p)
        rows.append(("S", a, rA, b, rB, y))
    return rows


def test_nll_matches_hand_value():
    # single trial, dr=1.0, no cost, beta=1 -> p=sigmoid(1), y=1
    dr = np.array([1.0])
    dcost = np.zeros((1, 3))
    y = np.array([1.0])
    got = E._nll(np.array([1.0]), dr, dcost, y, with_cost=False)
    exp = np.logaddexp(0.0, 1.0) - 1.0 * 1.0  # -(y*v - logaddexp)
    assert abs(got - exp) < 1e-12


def test_recovers_parameters():
    rows = _simulate(seed=1)
    dr, dcost, y = E._design(rows)
    res = E.fit(dr, dcost, y, with_cost=True)
    beta, c2, c3, c4 = res.x
    assert abs(beta - 2.5) < 0.5
    assert abs(c2 - 0.3) < 0.15
    assert abs(c3 - 0.6) < 0.15
    assert abs(c4 - 1.0) < 0.15
    # cost increases with level -> intensity falls with cost
    assert c2 < c3 < c4


def test_full_beats_null_when_cost_present():
    rows = _simulate(seed=2)
    out = E.fit_all(rows)
    assert out["nll_full"] < out["nll_null"]
    assert out["aic_full"] < out["aic_null"]
    assert out["lr_p"] < 1e-6
    assert out["beta_full"] > 0


def test_null_adequate_when_no_cost():
    # data generated with zero cost: full model should not improve much
    rows = _simulate(beta=2.5, c=(0.0, 0.0, 0.0, 0.0), seed=3)
    out = E.fit_all(rows)
    # LR improvement should be small (not significant at 1e-6)
    assert out["lr_stat"] < 20  # 3 df; large would be false positive


def test_load_trials_parses(tmp_path=None):
    d = tempfile.mkdtemp()
    p = os.path.join(d, "X01_ED.csv")
    with open(p, "w", encoding="utf-8") as f:
        f.write("Currentstep,EDclick.clicked_name,EDleftbutton.wasclicked,"
                "EDrightbutton.wasclicked,EDleftbutton.value,EDrightbutton.value,"
                "EDleftbutton.nback,EDrightbutton.nback\n")
        f.write(",,,,,,,\n")  # header-ish blank row
        f.write("0,EDleftbutton,1,0,2.00,1.00,1,2\n")
        f.write("1,EDrightbutton,0,1,2.00,1.50,3,4\n")
    rows = E.load_trials(d)
    assert len(rows) == 2
    assert rows[0] == ("X01", 1, 2.0, 2, 1.0, 1)
    assert rows[1] == ("X01", 3, 2.0, 4, 1.5, 0)
