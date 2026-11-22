import numpy as np
import pytest

import coarse
import measures as M
import model


def two_bit_kernel(f):
    """Kernel over (S = bit 0, E = bit 1); E' is a fresh fair coin unless f
    says otherwise; f(s, e) -> (p(S'=1), p(E'=1))."""
    P = np.zeros((4, 4))
    for st in range(4):
        s, e = st & 1, (st >> 1) & 1
        ps, pe = f(s, e)
        for nx in range(4):
            s2, e2 = nx & 1, (nx >> 1) & 1
            P[st, nx] = (ps if s2 else 1 - ps) * (pe if e2 else 1 - pe)
    return P


def test_information_basics():
    assert M.H([0.5, 0.5]) == pytest.approx(1.0)
    assert M.mi_joint(np.outer([0.3, 0.7], [0.5, 0.5])) == pytest.approx(0)
    assert M.mi_joint(np.diag([0.5, 0.5])) == pytest.approx(1.0)


def test_xor_counterexample_of_note_027():
    # S' = S xor E, S and E independent and uniform: A = 1 bit, Ahat = 0.
    P = two_bit_kernel(lambda s, e: (float(s ^ e), 0.5))
    pi = model.stationary(P)
    obs = M.observational(P, pi, 2, [0])
    assert obs["A"] == pytest.approx(1.0)
    assert obs["Astar"] == pytest.approx(0.0, abs=1e-12)
    assert M.ahat(P, pi, 2, [0])[0] == pytest.approx(0.0, abs=1e-12)


def test_common_cause_of_fig_2():
    # E persists and sets S': A* > 0 but Ahat = 0.
    P = two_bit_kernel(lambda s, e: (0.9 if e else 0.1, 0.9 if e else 0.1))
    pi = model.stationary(P)
    assert M.observational(P, pi, 2, [0])["Astar"] > 0.1
    assert M.ahat(P, pi, 2, [0])[0] == pytest.approx(0.0, abs=1e-12)


def test_self_copy_has_one_bit():
    P = two_bit_kernel(lambda s, e: (float(s), 0.5))
    pi = model.stationary(P)
    a, an = M.ahat(P, pi, 2, [0])
    assert a == pytest.approx(1.0) and an == pytest.approx(1.0)
    c2 = M.c2_profile(P, 2, [0])
    assert c2["var"] == pytest.approx(0.0, abs=1e-12)


def test_kernels_are_stochastic_and_stationary():
    for P in (model.scaffold_kernel(0.0), model.scaffold_kernel(1.0),
              model.common_input_kernel()):
        assert np.allclose(P.sum(1), 1.0)
        pi = model.stationary(P)
        assert np.allclose(pi @ P, pi, atol=1e-10)


def test_scaffold_absent_lam0_patch_is_unstructured():
    # lam = 0, scaffold absent in A: a cell of A copies the whole population,
    # never specifically its patch; with a = 0, eps = 0, d = 0 its next-trait
    # probability is the population mean.
    P = model.scaffold_kernel(0.0, a=0.0, eps=0.0, d=0.0)
    s = 0b00000111  # A all ones, B all zeros, both scaffolds absent
    p_cell0 = sum(P[s, x2] for x2 in range(256) if x2 & 1)
    assert p_cell0 == pytest.approx(0.5)
    P1 = model.scaffold_kernel(1.0, a=0.0, eps=0.0, d=0.0)
    assert sum(P1[s, x2] for x2 in range(256) if x2 & 1) == pytest.approx(1.0)


def test_partitions_count():
    assert len(list(coarse.set_partitions(range(6)))) == 203


def test_delta_c_identity_given_environment_is_zero():
    P = model.scaffold_kernel(0.5)
    pi = model.stationary(P)
    ident = [[i] for i in range(6)]
    out = coarse.delta_c(P, pi, ident, 8, 6, model.R_VAR)
    assert out["dC_E"] == pytest.approx(0.0, abs=1e-12)


def test_patch_partition_lumpable_given_environment():
    # exchangeable cells within a patch: the patch counts and r close the
    # dynamics in distribution, so dC|E = 0 even for the distributional form
    P = model.scaffold_kernel(0.3)
    pi = model.stationary(P)
    patches = [[0, 1, 2], [3, 4, 5]]
    for dist in (False, True):
        out = coarse.delta_c(P, pi, patches, 8, 6, model.R_VAR, dist=dist)
        assert out["dC_E"] == pytest.approx(0.0, abs=1e-12)
    cross = [[0, 3], [1, 4], [2, 5]]
    assert coarse.delta_c(P, pi, cross, 8, 6, model.R_VAR,
                          dist=True)["dC_E"] > 1e-3
