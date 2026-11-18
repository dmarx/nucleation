# scratch/formal/reconstruction_channel_checks.py: rebuilds and asserts the worked numbers of the continuation of the
# exchange "Explain String Theory" (filed 2026-11-15): (a) the phase-coded associative memory and its interventions
# (intact, attenuated, readdressed, readout suppressed, deleted), the rank of its measurement operator, and the
# cancellation counterexample; (b) the orthogonal-update merging toy; (c) the XOR-coded concept; (d) the non-normal
# transient; (e) the hidden-mode transfer function; (f) repeated-sampling coverage and the base/sharpened crossing.
# The original study bundle did not reach the record; this is a reconstruction from the text. Where the text leaves
# the construction open (how readout suppression was implemented, where the background associations sat), the choice
# made here is stated in a comment, and the values that depend on it are not asserted.
# Run: python3 -I scratch/formal/reconstruction_channel_checks.py
import cmath
import math

D = 64
STEP = 2 * math.pi / D


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


def key(phi):
    return [cmath.exp(1j * n * phi) / math.sqrt(D) for n in range(D)]


def inner(a, b):  # a^dagger b
    return sum(x.conjugate() * y for x, y in zip(a, b))


def axpy(a, x, y):
    return [a * u + v for u, v in zip(x, y)]


# ---- (a) phase-coded memory -------------------------------------------------------------------------------------
# Choice: nine background associations at canonical addresses 10..18 steps from the target, unit amplitude. The
# target-specific response is the response of the memory minus that of a matched memory without the target, as in
# the text, so it does not depend on where the background sits.
Q0 = 0.0
background = [0.0] * D
for j in range(10, 19):
    background = axpy(1.0, key(j * STEP), background)


def target_response(memory_with, phi):
    return abs(inner(key(phi), memory_with) - inner(key(phi), background))


def memory(amplitude=1.0, address=Q0):
    return axpy(amplitude, key(address), background)


queries = {"original": Q0, "half-step": Q0 + STEP / 2, "new address": Q0 + STEP}
intact, attenuated, readdressed = memory(), memory(0.25), memory(address=Q0 + STEP)
deleted = background
expected = {  # values as given in the text
    "intact": (intact, (1.000, 0.637, 0.000)),
    "attenuated": (attenuated, (0.250, 0.159, 0.000)),
    "readdressed": (readdressed, (0.000, 0.637, 1.000)),
    "deleted": (deleted, (0.000, 0.000, 0.000)),
}
for name, (m, vals) in expected.items():
    for q, v in zip(queries.values(), vals):
        close(target_response(m, q), v, 5e-4)
close(abs(inner(key(STEP / 2), key(0.0))), 1 / (D * math.sin(math.pi / (2 * D))), 1e-12)  # Dirichlet kernel, half step
# Readout suppression, reconstructed as the observation channel at the canonical query q0 returning nothing (A_q0 = 0).
# This reproduces the zero at q0 and the rank result below, but gives 0.637 at the half step, not the text's 0.551,
# which must come from a different suppression (for example a smooth notch around q0). 0.551 is not asserted.


def rank(rows, tol=1e-9):
    m = [r[:] for r in rows]
    r = 0
    for c in range(D):
        piv = max(range(r, len(m)), key=lambda i: abs(m[i][c]), default=None)
        if piv is None or abs(m[piv][c]) < tol:
            continue
        m[r], m[piv] = m[piv], m[r]
        for i in range(len(m)):
            if i != r and abs(m[i][c]) > 0:
                f = m[i][c] / m[r][c]
                m[i] = [a - f * b for a, b in zip(m[i], m[r])]
        r += 1
        if r == len(m):
            break
    return r


canonical = [[x.conjugate() for x in key(k * STEP)] for k in range(D)]
assert rank(canonical) == 64
suppressed = [[0j] * D] + canonical[1:]           # the row for q0 returns nothing
assert rank(suppressed) == 63
assert rank(suppressed + [[x.conjugate() for x in key(STEP / 2)]]) == 64

# Cancellation: two internal pathways h1 = u, h2 = -u, read only through their sum, match "both absent" under every
# query; silencing h2 separates them.
u = key(3 * STEP)
for k in range(D):
    q = key(k * STEP)
    assert abs(inner(q, axpy(1.0, u, [-x for x in u]))) < 1e-12
assert abs(inner(key(3 * STEP), u)) > 0.99      # do(h2 = 0) reveals h1 at its address

# ---- (b) orthogonal parameter updates can interact: f_w(x) = (w.x)^2 -----------------------------------------------
f = lambda w, x: (w[0] * x[0] + w[1] * x[1]) ** 2
x = (1.0, 1.0)
assert f((1, 1), x) - f((1, 0), x) - f((0, 1), x) + f((0, 0), x) == 2

# ---- (c) a concept carried by a product of features is linearly invisible -----------------------------------------
pts = [(a, b, a * b) for a in (-1, 1) for b in (-1, 1)]
assert sum(a * c for a, b, c in pts) == 0 and sum(b * c for a, b, c in pts) == 0

# ---- (d) non-normal transient: J = [[0.8, 8], [0, 0.8]], J^n upper-right = 8 n 0.8^(n-1) ----------------------------
close(8 * 5 * 0.8 ** 4, 16.384, 1e-9)

# ---- (e) hidden mode: x1' = -x1 + e x2 + u, x2' = -3 x2 + x1, y = x1 has H(s) = (s+3)/((s+1)(s+3) - e) -------------
for s in (0.3, 1.7, 2.0 + 0.5j):
    for e in (0.0, 0.4):
        # solve (s+1) X1 - e X2 = 1, (s+3) X2 = X1
        x1 = 1 / ((s + 1) - e / (s + 3))
        assert abs(x1 - (s + 3) / ((s + 1) * (s + 3) - e)) < 1e-12
        if e == 0.0:
            assert abs(x1 - 1 / (s + 1)) < 1e-12   # the second state is invisible without feedback

# ---- (f) coverage under repeated sampling, and the base/sharpened crossing ----------------------------------------
cov = lambda p, n: 1 - (1 - p) ** n
for n, v in ((1, 0.010), (10, 0.0956), (100, 0.634), (500, 0.9934)):
    close(cov(0.01, n), v, 5e-4)
assert math.ceil(math.log(0.05) / math.log(0.99)) == 299
close(cov(0.01, 22), 0.198, 1e-3)
base, sharp = (0.05, 0.005), (0.50, 0.0001)
table = {1: (0.0275, 0.2501), 10: (0.2251, 0.5000), 100: (0.6942, 0.5050), 500: (0.9592, 0.5244)}
for n, (b, s) in table.items():
    close(sum(cov(p, n) for p in base) / 2, b, 2e-4)
    close(sum(cov(p, n) for p in sharp) / 2, s, 2e-4)

print("reconstruction channel checks: all passed")
