"""Tests for the LEAD-114 study: group tables, blind irrep recovery, model."""
import numpy as np
import pytest

import groups
import reptheory as rt
import model


def test_s3_is_group_s3_table_only():
    _, C = groups.symmetric_group(3)
    info = groups.is_group_table(C)
    assert info["is_group"]
    assert info["assoc_frac"] == 1.0
    assert info["has_inverses"]


def test_broken_table_not_group():
    _, C = groups.symmetric_group(3)
    B = C.copy()
    B[0, 0] = (B[0, 0] + 1) % 6   # corrupt identity row
    info = groups.is_group_table(B)
    assert not info["is_group"]


def test_s3_classes_blind():
    _, C = groups.symmetric_group(3)
    classes = rt.conjugacy_classes(C)
    sizes = sorted(len(c) for c in classes)
    assert sizes == [1, 2, 3]            # e; two 3-cycles; three transpositions


@pytest.mark.parametrize("n,expected", [
    (3, [1, 1, 2]),
    (4, [1, 1, 2, 3, 3]),
])
def test_recover_sn_dims(n, expected):
    _, C = groups.symmetric_group(n)
    r = rt.recover_irreps(C, seed=1)
    assert r["dims"] == expected
    assert r["sum_d2"] == C.shape[0]
    assert r["ortho_residual"] < 1e-6
    assert r["max_char_imag"] < 1e-6
    # trivial representation present: a row of all ones.
    chi = np.array(r["character_table"])
    assert np.any(np.all(np.abs(chi - 1.0) < 1e-5, axis=1))


def test_recover_z5_all_onedim():
    _, C = groups.cyclic_group(5)
    r = rt.recover_irreps(C, seed=2)
    assert r["dims"] == [1, 1, 1, 1, 1]
    assert r["n_irreps"] == 5


def test_blocks_span_full_space():
    _, C = groups.symmetric_group(3)
    blocks, _, _ = rt.isotypic_blocks(C, seed=0)
    E = np.random.default_rng(0).standard_normal((6, 4))
    fracs, resid = rt.embedding_irrep_content(E, blocks)
    assert abs(resid) < 1e-8          # blocks tile R^m
    assert abs(sum(fracs) - 1.0) < 1e-8


def test_model_trains_s3():
    _, C = groups.symmetric_group(3)
    p, info = model.train(C, d=12, H=48, wd=1e-3, lr=0.5, steps=1500,
                          holdout=0.0, seed=0)
    assert info["train_acc"] > 0.95    # can fit the full table


def test_backprop_matches_numerical():
    _, C = groups.symmetric_group(3)
    p = model.init_params(6, 5, 7, seed=3)
    gid = np.array([0, 1, 2, 3])
    hid = np.array([1, 2, 3, 4])
    y = C[gid, hid]
    loss0, grads, _ = model.loss_and_grads(p, gid, hid, y, wd=1e-3)
    eps = 1e-5
    rng = np.random.default_rng(0)
    for key in ["E", "Wl", "Wu"]:
        idx = tuple(rng.integers(s) for s in p[key].shape)
        orig = p[key][idx]
        p[key][idx] = orig + eps
        lp, _, _ = model.loss_and_grads(p, gid, hid, y, wd=1e-3)
        p[key][idx] = orig - eps
        lm, _, _ = model.loss_and_grads(p, gid, hid, y, wd=1e-3)
        p[key][idx] = orig
        num = (lp - lm) / (2 * eps)
        assert abs(num - grads[key][idx]) < 1e-4
