"""Tests for geometry.py and lmnp.py on constructed subspaces and tiny random models.

Run: python3 -I -m pytest -q scratch/studies/lead-073   (from the repository root)
"""
import os
import sys

import numpy as np
import pytest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import geometry as geo  # noqa: E402
import lmnp  # noqa: E402
import measure  # noqa: E402


def _orth(rng, d, k):
    q, _ = np.linalg.qr(rng.standard_normal((d, k)))
    return q


# ------------------------------------------------------------ geometry

def test_b5_counterexample_gives_one_dimensional_m_and_n():
    # NOTE-746, App. B.5: g(y0)=(1,0), g(y1)=(1,1), g(y2)=(1,-1), so G = span(e2).
    Gm = np.array([[1.0, 0.0], [1.0, 1.0], [1.0, -1.0]])
    QG, _ = geo.pivot_span(Gm, 1e-9)
    rng = np.random.default_rng(0)
    QF, _ = geo.span_basis(rng.standard_normal((50, 2)), 1e-9)
    QM, QN, _ = geo.m_and_n(QF, QG, 1e-9)
    assert QM.shape[1] == QN.shape[1] == 1
    e2 = np.array([[0.0], [1.0]])
    assert geo.containment(QM, e2)["worst_out"] < 1e-12
    assert geo.containment(QN, e2)["worst_out"] < 1e-12


def test_pivot_span_does_not_depend_on_pivot():
    rng = np.random.default_rng(1)
    Gm = rng.standard_normal((30, 5)) @ rng.standard_normal((5, 8)) + rng.standard_normal(8)
    Q, _ = geo.pivot_span(Gm, 1e-9)
    for y0 in (0, 7, 29):
        Qp, _ = geo.span_basis(Gm - Gm[y0], 1e-9)
        assert Qp.shape == Q.shape
        assert geo.containment(Qp, Q)["worst_out"] < 1e-10


@pytest.mark.parametrize("seed", [2, 3, 4])
def test_lemma2_dims_and_logit_identity(seed):
    rng = np.random.default_rng(seed)
    d = 9
    QG0 = _orth(rng, d, 5)                       # G: 5-dim
    Gperp = np.linalg.svd(np.eye(d) - QG0 @ QG0.T)[0][:, :d - 5]
    # F: 4-dim, one direction of it inside G^perp, so dim M = 4 - 1 = 3.
    Fbasis = np.concatenate([_orth(rng, d, 3), Gperp[:, :1]], 1)
    Fm = rng.standard_normal((200, 4)) @ Fbasis.T
    Gm = rng.standard_normal((300, 5)) @ QG0.T + rng.standard_normal(d)
    QF, _ = geo.span_basis(Fm, 1e-9)
    QG, _ = geo.pivot_span(Gm, 1e-9)
    QM, QN, _ = geo.m_and_n(QF, QG, 1e-9)
    assert QF.shape[1] == 4 and QG.shape[1] == 5
    assert QM.shape[1] == QN.shape[1] == 3
    # Eq. 8: f^T g0 = (P_M f)^T (P_N g0)
    g0 = Gm - Gm[0]
    lhs = Fm @ g0.T
    rhs = (Fm @ QM @ QM.T) @ (g0 @ QN @ QN.T).T
    assert np.allclose(lhs, rhs, atol=1e-8)
    assert geo.containment(QM, QF)["worst_out"] < 1e-10
    assert geo.containment(QN, QG)["worst_out"] < 1e-10


def test_containment_angles():
    e = np.eye(3)
    assert geo.containment(e[:, :1], e[:, :2])["worst_out"] < 1e-15
    assert abs(geo.containment(e[:, 2:3], e[:, :2])["worst_out"] - 1) < 1e-15
    v = np.array([[np.cos(np.pi / 6)], [0.0], [np.sin(np.pi / 6)]])
    c = geo.containment(v, e[:, :2])
    assert abs(c["worst_out"] - 0.25) < 1e-12 and abs(c["max_angle_deg"] - 30) < 1e-9
    assert abs(geo.energy_outside(v, e[:, :2]) - 0.25) < 1e-12


def test_fit_relation_recovers_exact_affine_map_and_gamma_q():
    rng = np.random.default_rng(5)
    d, n = 12, 80
    QGam = _orth(rng, d, 3)
    Atrue = rng.standard_normal((3, 4)) @ _orth(rng, d, 4).T     # rank 3, rows in a 4-dim space
    X = rng.standard_normal((n, d))
    Z = X @ Atrue.T + np.array([1.0, -2.0, 0.5])
    Fsq = Z @ QGam.T + rng.standard_normal((n, d)) @ (np.eye(d) - QGam @ QGam.T)
    A, a = geo.fit_relation(X, Fsq, QGam, lam=1e-10)
    assert np.allclose(A, Atrue, atol=1e-6) and np.allclose(a, [1.0, -2.0, 0.5], atol=1e-6)
    r2, _ = geo.loo_r2(X, Fsq, QGam, lam=1e-10)
    assert r2 > 0.999999
    Gq = geo.gamma_q_basis(A)
    assert Gq.shape[1] == 3
    assert geo.containment(Gq, geo.span_basis(Atrue, 1e-9)[0])["worst_out"] < 1e-8


def test_visibility_orders_directions():
    d = 4
    Gm = np.random.default_rng(6).standard_normal((500, d)) * np.array([10.0, 1.0, 0.1, 0.01])
    W, s = geo.visibility(Gm, np.eye(d))
    assert np.all(np.diff(s) <= 1e-12)
    assert abs(abs(W[0, 0]) - 1) < 1e-2 and abs(abs(W[3, 3]) - 1) < 1e-2
    assert s[-1] < 2e-3


# ------------------------------------------------------------ tiny random models

def _tiny_gpt2(rng, d=16, V=40, L=2, H=2, T=32, ln_bias=True):
    w = {"wte.weight": rng.standard_normal((V, d)) * 0.5, "wpe.weight": rng.standard_normal((T, d)) * 0.1,
         "ln_f.weight": 1 + 0.1 * rng.standard_normal(d),
         "ln_f.bias": 0.1 * rng.standard_normal(d) if ln_bias else np.zeros(d)}
    for i in range(L):
        p = f"h.{i}."
        w.update({p + "ln_1.weight": np.ones(d), p + "ln_1.bias": np.zeros(d),
                  p + "attn.c_attn.weight": rng.standard_normal((d, 3 * d)) * 0.2, p + "attn.c_attn.bias": np.zeros(3 * d),
                  p + "attn.c_proj.weight": rng.standard_normal((d, d)) * 0.2, p + "attn.c_proj.bias": np.zeros(d),
                  p + "ln_2.weight": np.ones(d), p + "ln_2.bias": np.zeros(d),
                  p + "mlp.c_fc.weight": rng.standard_normal((d, 4 * d)) * 0.2, p + "mlp.c_fc.bias": np.zeros(4 * d),
                  p + "mlp.c_proj.weight": rng.standard_normal((4 * d, d)) * 0.2, p + "mlp.c_proj.bias": np.zeros(d)})
    w = {k: v.astype(np.float32) for k, v in w.items()}
    return lmnp.LM("gpt2", w, {"n_head": H, "n_layer": L, "layer_norm_epsilon": 1e-5})


def _tiny_neox(rng, d=16, V=40, L=2, H=2):
    w = {"gpt_neox.embed_in.weight": rng.standard_normal((V, d)), "embed_out.weight": rng.standard_normal((V, d)),
         "gpt_neox.final_layer_norm.weight": 1 + 0.1 * rng.standard_normal(d),
         "gpt_neox.final_layer_norm.bias": 0.1 * rng.standard_normal(d)}
    for i in range(L):
        p = f"gpt_neox.layers.{i}."
        w.update({p + "input_layernorm.weight": np.ones(d), p + "input_layernorm.bias": np.zeros(d),
                  p + "post_attention_layernorm.weight": np.ones(d), p + "post_attention_layernorm.bias": np.zeros(d),
                  p + "attention.query_key_value.weight": rng.standard_normal((3 * d, d)) * 0.2,
                  p + "attention.query_key_value.bias": np.zeros(3 * d),
                  p + "attention.dense.weight": rng.standard_normal((d, d)) * 0.2, p + "attention.dense.bias": np.zeros(d),
                  p + "mlp.dense_h_to_4h.weight": rng.standard_normal((4 * d, d)) * 0.2, p + "mlp.dense_h_to_4h.bias": np.zeros(4 * d),
                  p + "mlp.dense_4h_to_h.weight": rng.standard_normal((d, 4 * d)) * 0.2, p + "mlp.dense_4h_to_h.bias": np.zeros(d)})
    w = {k: v.astype(np.float32) for k, v in w.items()}
    cfg = {"num_attention_heads": H, "num_hidden_layers": L, "hidden_size": d, "rotary_pct": 0.5,
           "rotary_emb_base": 10000, "layer_norm_eps": 1e-5, "use_parallel_residual": True}
    return lmnp.LM("neox", w, cfg)


@pytest.mark.parametrize("make", [_tiny_gpt2, _tiny_neox])
def test_forward_is_causal(make):
    rng = np.random.default_rng(7)
    lm = make(rng)
    ids = rng.integers(0, 40, size=(3, 10))
    f = lm.hidden(ids)
    ids2 = ids.copy()
    ids2[:, 6:] = rng.integers(0, 40, size=(3, 4))
    f2 = lm.hidden(ids2)
    assert f.shape == (3, 10, 16)
    assert np.allclose(f[:, :6], f2[:, :6], atol=1e-5)
    assert not np.allclose(f[:, 6:], f2[:, 6:], atol=1e-3)


def test_safetensors_roundtrip(tmp_path):
    rng = np.random.default_rng(8)
    t = {"a": rng.standard_normal((3, 4)).astype(np.float32), "b": rng.standard_normal(5).astype(np.float32)}
    p = tmp_path / "m.safetensors"
    lmnp.save_safetensors(str(p), t)
    r = lmnp.load_safetensors(str(p))
    assert set(r) == {"a", "b"} and np.array_equal(r["a"], t["a"]) and np.array_equal(r["b"], t["b"])


def test_bpe_merges_and_roundtrip():
    b2u = lmnp._bytes_to_unicode()
    vocab = {c: i for i, c in enumerate(b2u.values())}
    sp = b2u[ord(" ")]
    merges = [("h", "e"), (sp, "he"), ("l", "l"), ("he", "ll")]
    for a, b in merges:
        vocab[a + b] = len(vocab)
    tok = lmnp.BPE(vocab, merges)
    ids = tok.encode("hell he hello")
    assert tok.decode(ids) == "hell he hello"
    assert ids[0] == vocab["hell"] and ids[1] == vocab[sp + "he"]


@pytest.mark.parametrize("ln_bias, full", [(True, True), (False, False)])
def test_final_layernorm_span(ln_bias, full):
    # f = gamma * normalized(h) + beta, normalized(h) has mean 0: F is full exactly
    # when beta leaves the hyperplane diag(gamma) 1^perp, and codimension 1 when beta = 0.
    rng = np.random.default_rng(9)
    lm = _tiny_gpt2(rng, ln_bias=ln_bias)
    f = lm.hidden(rng.integers(0, 40, size=(40, 12))).reshape(-1, 16)
    QF, _ = geo.span_basis(f, 1e-5)
    assert QF.shape[1] == (16 if full else 15)
    gam, beta = lm.ln_f()
    assert measure.ln_offset(gam, beta) != 0 if full else measure.ln_offset(gam, beta) == 0


def test_measure_pipeline_on_tiny_model():
    rng = np.random.default_rng(10)
    lm = _tiny_gpt2(rng, V=60)

    class Tok:  # one token per word, words "w0".."w59"
        def encode(self, s):
            return [int(t[1:]) for t in s.split()]

    rels = {"toy": {"query": " w1 w2", "pairs": [(f" w{i}", f" w{40 + i % 5}") for i in range(10, 30)]}}
    res = measure.measure(lm, Tok(), bos=0, relations=rels, rng=rng, n_random=20, len_random=10,
                          n_sample=4, len_sample=4, rtols=(1e-3,), ctol=1e-3, lam=1e-2, tau_v=1e-2)
    s = res["spans"]["1e-03"]
    assert s["dim_F"] == s["dim_G"] == s["dim_M"] == s["dim_N"] == 16
    r = res["relations"]["toy"]
    assert r["n_subjects"] == 20 and r["dim_Gamma"] == 4
    assert r["tests"]["1e-03"]["Gamma_in_N"]["worst_out"] < 1e-8
    assert r["tests"]["1e-03"]["Gamma_q_in_M"]["worst_out"] < 1e-8
