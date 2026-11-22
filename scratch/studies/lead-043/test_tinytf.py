import numpy as np
import tinytf as tt
import probes


def _small():
    rng = np.random.default_rng(0)
    p = tt.init_params(rng, vocab=11, n_pos=3, d=8, n_heads=2, d_mlp=12, n_out=5)
    tok = rng.integers(0, 11, (6, 3))
    tgt = np.eye(5)[rng.integers(0, 5, 6)]
    tgt[0] = 1 / 5  # one soft (uniform) target
    w = np.array([1, 1, -0.5, 1, 2, 1.0])  # one ascent row
    return p, tok, tgt, w


def test_gradient_matches_finite_differences():
    p, tok, tgt, w = _small()
    logits, cache = tt.forward(p, tok)
    _, dlog = tt.loss_grad(logits, tgt, w)
    g = tt.backward(p, cache, dlog)
    rng = np.random.default_rng(1)
    eps = 1e-6
    for name in [k for k in p if k != "_meta"]:
        for _ in range(4):
            idx = tuple(rng.integers(0, s) for s in p[name].shape)
            old = p[name][idx]
            p[name][idx] = old + eps
            lp = tt.loss_grad(tt.forward(p, tok)[0], tgt, w)[0]
            p[name][idx] = old - eps
            lm = tt.loss_grad(tt.forward(p, tok)[0], tgt, w)[0]
            p[name][idx] = old
            num = (lp - lm) / (2 * eps)
            assert abs(num - g[name][idx]) < 1e-6 + 1e-4 * abs(num), (name, num, g[name][idx])


def test_causal_mask_last_position_ignores_nothing_but_first_ignores_later():
    p, tok, _, _ = _small()
    _, c1 = tt.forward(p, tok)
    tok2 = tok.copy()
    tok2[:, 2] = (tok2[:, 2] + 1) % 11
    _, c2 = tt.forward(p, tok2)
    # position 0 of layer-0 input is unchanged by a change at position 2
    assert np.allclose(c1["layers"][1][0][:, 0], c2["layers"][1][0][:, 0])


def test_block_of_covers_all_params():
    p, *_ = _small()
    assert {tt.block_of(k) for k in p if k != "_meta"} == set(tt.BLOCKS)


def test_training_memorizes_a_small_table():
    rng = np.random.default_rng(2)
    p = tt.init_params(rng, vocab=20, n_pos=2, d=16, n_heads=2, d_mlp=32, n_out=6)
    tok = np.stack([np.arange(10), 10 + rng.integers(0, 2, 10)], 1)
    y = rng.integers(0, 6, 10)
    opt = tt.Adam(p, 3e-3)
    for _ in range(300):
        lg, c = tt.forward(p, tok)
        _, d = tt.loss_grad(lg, np.eye(6)[y], np.ones(10))
        opt.step(p, tt.backward(p, c, d))
    assert (tt.predict(p, tok).argmax(1) == y).all()


def test_linear_probe_recovers_linear_labels():
    rng = np.random.default_rng(3)
    X = rng.normal(size=(300, 10))
    W = rng.normal(size=(10, 4))
    y = (X @ W).argmax(1)
    pr = probes.fit_linear(X[:200], y[:200], 4)
    assert (probes.predict(pr, X[200:]).argmax(1) == y[200:]).mean() > 0.85


def test_mlp_probe_fits_xor_like_labels():
    rng = np.random.default_rng(4)
    X = rng.normal(size=(400, 2))
    y = ((X[:, 0] > 0) ^ (X[:, 1] > 0)).astype(int)
    pr = probes.fit_mlp(X[:300], y[:300], 2, hidden=32, steps=1500, seed=0)
    assert (probes.predict(pr, X[300:]).argmax(1) == y[300:]).mean() > 0.85
