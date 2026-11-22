"""LEAD-084 study. Run: OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 python3 -I run.py
Writes results.json and results.md next to this file. About a minute."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
from augment import *

OUT = {}


def psd_min(M):
    return float(np.linalg.eigvalsh((M + M.T) / 2).min())


# 1. Finite-lag error = Riccati from the stationary prior; the bound.
rng = np.random.default_rng(20261122)
ident, low, high, ratios, n_models = 0.0, np.inf, np.inf, [], 0
for trial in range(400):
    n = int(rng.integers(2, 8)); m = int(rng.integers(1, n))
    A, L, S = random_model(n, m, rng, radius=0.97, corr=bool(trial % 2))
    n_models += 1
    for p in (1, 2, 4, 8, 12):
        Ps = riccati_seq(A, L, S, p)
        ident = max(ident, np.abs(L @ Ps[p] @ L.T - regression_error(A, L, S, p)).max()
                    / np.abs(L @ Ps[0] @ L.T).max())
        exc, bnd, Acl = excess_and_bound(A, L, S, p)
        sc = np.abs(L @ Ps[0] @ L.T).max()
        low = min(low, psd_min(exc) / sc)
        high = min(high, psd_min(bnd - exc) / sc)
        if np.trace(bnd) > 1e-12 * sc:
            ratios.append(float(np.trace(exc) / np.trace(bnd)))
OUT["bound"] = dict(models=n_models, lags=[1, 2, 4, 8, 12],
                    riccati_vs_regression_rel=float(ident),
                    min_eig_excess_rel=float(low), min_eig_bound_minus_excess_rel=float(high),
                    tightness_trace_ratio_median=float(np.median(ratios)),
                    tightness_trace_ratio_min=float(np.min(ratios)))

# 2. Exact augmentation: k_min, Markov, error, TE; against MZ Hankel and Krylov.
rows = []
rng = np.random.default_rng(11)
def aug_row(name, A, L, S):
    W, k = predictive_coords(A, L, S)
    Pinf = steady(A, L, S)
    row = dict(name=name, n=A.shape[0], m=L.shape[0], k_min=k,
               mz_hankel_rank=mz_hankel_rank(A, L, S), krylov=krylov_dim(A, L))
    F, Q, M = joint_state(A, L, S, W)
    c1 = cond_cov_lags(F, Q, M, 1)
    row["markov_gap"] = markov_defect(F, Q, M)
    if k > 0:
        # drop each coordinate in turn; report the smallest resulting defect
        row["markov_gap_k_minus_1"] = min(
            markov_defect(*joint_state(A, L, S, np.delete(W, i, axis=0))) for i in range(k))
    row["aug_err_minus_Einf"] = float(np.abs(c1[:L.shape[0], :L.shape[0]] - L @ Pinf @ L.T).max())
    cx = cond_cov_lags(F, Q, M, 1, extra=True)
    row["TE_Z"] = float(logdet_range(c1, cx)); row["TE_Y"] = float(transfer_entropy_Y(A, L, S))
    return row

# structured examples
A = np.array([[0.5, 0.4], [0.0, 0.3]]); S = np.eye(2) - A @ A.T
rows.append(aug_row("CLAIM-389 counterexample (zero memory, not closed)", A, np.array([[1.0, 0.0]]), S))
A = np.array([[0.6, 0.0, 0.0], [0.3, 0.5, 0.0], [0.0, 0.4, 0.2]])
rows.append(aug_row("closed coarse variable (Y drives the rest)", A, np.array([[1.0, 0, 0]]), np.eye(3)))
A = np.array([[0.5, 0.4, 0.0], [0.3, 0.6, 0.0], [0.0, 0.0, 0.8]])
rows.append(aug_row("loop plus an independent unobserved AR(1)", A, np.array([[1.0, 0, 0]]), np.eye(3)))
A = np.array([[0.5, 1.0, 0.0, 0.0], [0.0, 0.6, 1.0, 0.0], [0.0, 0.0, 0.7, 1.0], [0.0, 0.0, 0.0, 0.8]])
rows.append(aug_row("one-way chain into Y (driven chain)", A, np.array([[1.0, 0, 0, 0]]), np.eye(4)))
# well-conditioned random models
for i in range(12):
    n = int(rng.integers(3, 7)); m = int(rng.integers(1, n))
    A, L, S = random_model(n, m, rng, radius=0.9, corr=True)
    A = 0.9 * A / rho(A)
    rows.append(aug_row("random %d" % i, A, L, S))
OUT["augmentation"] = rows

# 3. Rate: rho(A_cl) against the eliminated spectrum.
rng = np.random.default_rng(7)
cnt = dict(models=0, gt_rho_A22=0, gt_rho_Atil=0, Atil_unstable=0,
           nm1_models=0, nm1_gt_Atil=0, gt_c=0, normed_gt_c=0, full_vs_reduced=0.0)
worst = 1.0
for trial in range(2000):
    n = int(rng.integers(2, 7)); m = int(rng.integers(1, n))
    A, L, S = random_model(n, m, rng, radius=0.97, corr=bool(rng.integers(0, 2)))
    nonnormal = rng.random() < 0.3
    if nonnormal:
        T = np.eye(n) + 3 * np.triu(rng.standard_normal((n, n)), 1)
        A = T @ A @ np.linalg.inv(T); A *= 0.95 / rho(A)
    c, normed, rf = contraction_factor(A, L, S)
    Pinf = steady(A, L, S)
    Acl = A - gain(A, L, Pinf) @ L
    r, ra, rt = rho(Acl), rho(rf["A22"]), rho(rf["Atil"])
    ev_full = np.sort(np.abs(np.linalg.eigvals(Acl)))[m:]
    ev_red = np.sort(np.abs(np.linalg.eigvals(rf["Acl_r"])))
    cnt["full_vs_reduced"] = max(cnt["full_vs_reduced"], abs(r - rho(rf["Acl_r"])))
    if not nonnormal:
        cnt["full_vs_reduced_normalish"] = max(cnt.get("full_vs_reduced_normalish", 0.0), float(np.abs(ev_full - ev_red).max()))
    cnt["models"] += 1
    cnt["gt_rho_A22"] += int(r > ra + 1e-9)
    cnt["gt_rho_Atil"] += int(r > rt + 1e-9)
    cnt["gt_rho_Atil_not_nonnormal"] = cnt.get("gt_rho_Atil_not_nonnormal", 0) + int(r > rt + 1e-6 and not nonnormal)
    cnt["Atil_unstable"] += int(rt >= 1)
    cnt["gt_c"] += int(r > c + 1e-9)
    cnt["normed_gt_c"] += int(normed > c + 1e-9)
    if r > rt + 1e-9:
        worst = max(worst, r / rt)
    if n - m == 1:
        cnt["nm1_models"] += 1
        cnt["nm1_gt_Atil"] += int(r > rt + 1e-9)
cnt["worst_ratio_rho_Acl_over_rho_Atil"] = float(worst)
OUT["rate"] = cnt

# 3b. Scalar Y: nonzero eigenvalues of A_cl = CLAIM-398's moving-average zeros.
rng = np.random.default_rng(5); dz = 0.0
for i in range(50):
    n = int(rng.integers(2, 6))
    A, L, S = random_model(n, 1, rng, radius=0.9)
    Pinf = steady(A, L, S)
    ev = np.linalg.eigvals(A - gain(A, L, Pinf) @ L)
    ev = np.sort_complex(ev[np.abs(ev) > 1e-8])
    z = ma_zeros_scalar(A, L, S)
    if len(z) == len(ev):
        dz = max(dz, float(np.abs(np.sort(np.abs(z)) - np.sort(np.abs(ev))).max()))
    else:
        dz = max(dz, 1.0)
OUT["ma_zeros_vs_closed_loop"] = dz

# 3c. Nilpotent eliminated dynamics: finite memory kernel, no finite AR.
NA = np.array([[0.1, 0.3, -1.0], [0.6, 0.0, -0.7], [0.1, 0.0, 0.0]])
NL = np.array([[1.0, 0.0, 0.0]]); NS = np.eye(3)
rfn = reduced_filter(NA, NL, NS)
nil = dict(A=NA.tolist(), rho_Atil=rho(rfn["Atil"]), rho_Acl=rho(rfn["Acl_r"]),
           kernel_natural=[float((NA[:1, 1:] @ np.linalg.matrix_power(NA[1:, 1:], j - 1) @ NA[1:, :1])[0, 0])
                           for j in range(1, 5)],
           excess=[float(excess_and_bound(NA, NL, NS, p)[0][0, 0]) for p in (1, 2, 3, 4, 6)])
OUT["nilpotent_example"] = nil

# 4. Weak inward coupling: A12 = eps.
sweep = []
for eps in (0.4, 0.2, 0.1, 0.05, 0.025):
    A = np.array([[0.5, eps, 0.0], [0.3, 0.7, 0.2], [0.1, -0.2, 0.6]])
    L = np.array([[1.0, 0, 0]]); S = np.eye(3)
    rf = reduced_filter(A, L, S)
    exc, bnd, Acl = excess_and_bound(A, L, S, 3)
    sweep.append(dict(eps=eps, rho_Acl=rho(Acl), rho_Atil=rho(rf["Atil"]),
                      excess_p3=float(exc[0, 0]), excess_over_eps2=float(exc[0, 0] / eps ** 2),
                      bound_p3=float(bnd[0, 0])))
OUT["weak_coupling"] = sweep

# 5. QUESTION-222's own example, sampled at h = 0.1 with unit white noise.
Ac = np.array([[-1.0, 1.0], [0.2, -0.3]])
Ah, Sh = exact_discretization(Ac, 0.1)
L = np.array([[1.0, 0.0]])
rf = reduced_filter(Ah, L, Sh)
c, normed, _ = contraction_factor(Ah, L, Sh)
ex = dict(A_h=Ah.tolist(), rho_Acl=None, rho_A22_mori=rho(rf["A22"]),
          a_yy=float(Ah[1, 1]), rho_Atil=rho(rf["Atil"]), c=float(c), lags=[])
Pinf = steady(Ah, L, Sh)
ex["rho_Acl"] = rho(Ah - gain(Ah, L, Pinf) @ L)
ex["ma_zero"] = [abs(complex(z)) for z in ma_zeros_scalar(Ah, L, Sh)]
ex["E_inf"] = float((L @ Pinf @ L.T)[0, 0])
for p in (1, 2, 5, 10, 20, 40):
    exc, bnd, _ = excess_and_bound(Ah, L, Sh, p)
    ex["lags"].append(dict(p=p, excess=float(exc[0, 0]), bound=float(bnd[0, 0])))
OUT["question_222_example"] = ex

with open(os.path.join(HERE, "results.json"), "w") as f:
    json.dump(OUT, f, indent=1, default=float)

# markdown
md = ["# LEAD-084 results", "", "Generated by run.py.", ""]
b = OUT["bound"]
md += ["## 1. Finite-lag error and the bound", "",
       f"{b['models']} random models (n 2-7, m 1 to n-1), lags {b['lags']}.", "",
       f"- p-lag regression error vs Riccati from the stationary prior: max relative difference {b['riccati_vs_regression_rel']:.1e}",
       f"- min eigenvalue of E_p - E_inf (relative): {b['min_eig_excess_rel']:.1e}",
       f"- min eigenvalue of B_p - (E_p - E_inf) (relative): {b['min_eig_bound_minus_excess_rel']:.1e}",
       f"- tightness tr(E_p - E_inf)/tr(B_p): median {b['tightness_trace_ratio_median']:.3f}, min {b['tightness_trace_ratio_min']:.3f}", ""]
md += ["## 2. Exact augmentation", "",
       "| model | n | m | k_min | MZ Hankel rank | Krylov | Markov gap | gap with k_min-1 | T(X->Z) | T(X->Y) |",
       "|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['name']} | {r['n']} | {r['m']} | {r['k_min']} | {r['mz_hankel_rank']} | {r['krylov']} | "
              f"{r['markov_gap']:.1e} | {r.get('markov_gap_k_minus_1', float('nan')):.1e} | {r['TE_Z']:.4f} | {r['TE_Y']:.4f} |")
c = OUT["rate"]
md += ["", "## 3. Rate against the eliminated spectrum", "",
       f"{c['models']} random models, 30% made non-normal.", "",
       f"- rho(A_cl), full filter vs reduced filter of R: max difference {c['full_vs_reduced']:.1e}; all nonzero |eigenvalues|, models not made non-normal: {c['full_vs_reduced_normalish']:.1e}",
       f"- rho(A_cl) > rho(A22) (Mori frame): {c['gt_rho_A22']}",
       f"- rho(A_cl) > rho(Atilde): {c['gt_rho_Atil']} (worst ratio {c['worst_ratio_rho_Acl_over_rho_Atil']:.3f}); by more than 1e-6 among models not made non-normal: {c['gt_rho_Atil_not_nonnormal']}",
       f"- Atilde unstable: {c['Atil_unstable']}",
       f"- n - m = 1: {c['nm1_models']} models, rho(A_cl) > |atilde| in {c['nm1_gt_Atil']}",
       f"- rho(A_cl) > c: {c['gt_c']}; P_R-norm of A_cl > c: {c['normed_gt_c']}",
       f"- scalar Y, nonzero |eig(A_cl)| vs moving-average zeros of phi(B)Y: max difference {OUT['ma_zeros_vs_closed_loop']:.1e}", ""]
md += ["Nilpotent eliminated dynamics, A = " + str(nil["A"]) + ", L = e1, Sigma = I:",
       f"rho(Atilde) = {nil['rho_Atil']:.1e}, rho(A_cl) = {nil['rho_Acl']:.4f}; natural-frame memory kernel at lags 1-4: "
       + ", ".join(f"{v:.3g}" for v in nil["kernel_natural"])
       + "; excess error at p = 1, 2, 3, 4, 6: " + ", ".join(f"{v:.3e}" for v in nil["excess"]), ""]
md += ["## 4. Weak inward coupling", "", "| eps | rho(A_cl) | rho(Atilde) | excess p=3 | excess/eps^2 | bound p=3 |", "|---|---|---|---|---|---|"]
for s in sweep:
    md.append(f"| {s['eps']} | {s['rho_Acl']:.4f} | {s['rho_Atil']:.4f} | {s['excess_p3']:.3e} | {s['excess_over_eps2']:.3e} | {s['bound_p3']:.3e} |")
md += ["", "## 5. QUESTION-222's example, h = 0.1", "",
       f"rho(A_cl) = {ex['rho_Acl']:.5f}; MA zero = {ex['ma_zero']}; rho(A22, Mori) = {ex['rho_A22_mori']:.5f}; "
       f"a_yy = {ex['a_yy']:.5f}; rho(Atilde) = {ex['rho_Atil']:.5f}; c = {ex['c']:.5f}; E_inf = {ex['E_inf']:.5e}", "",
       "| p | excess | bound |", "|---|---|---|"]
for r in ex["lags"]:
    md.append(f"| {r['p']} | {r['excess']:.3e} | {r['bound']:.3e} |")
with open(os.path.join(HERE, "results.md"), "w") as f:
    f.write("\n".join(md) + "\n")
print("\n".join(md))
