"""LEAD-142: the decision signature for the directed case.

Operator T: L2(P_A) -> L2(P_X), (T g)(x) = E[g(A) | X=x], for a joint law
P+(x,a). SVD gives singular values s_i and left/right singular functions
mu_i (functions of x), nu_i (functions of a). The candidate "signature" for
directed transformations (QUESTION-052) is span{mu_1..mu_d}, the top-d left
singular space.

Whitened kernel K[x,a] = P+(x,a)/sqrt(P_X(x) P_A(a)); SVD(K)=U S V^T. Left
singular functions mu_i(x) = U[x,i]/sqrt(P_X(x)) are L2(P_X)-orthonormal.

Findings (each checked below, results -> results.json):
  A  reduction: span{mu_1..mu_d} = top-d eigenspace of the self-adjoint
     two-step X-chain M (x->a->x'), M = T T*, which is reversible wrt P_X.
     So the directed x-decision case = a symmetric case with operator M.
  B  reproduction of the directed linear result (THEORY-239): a non-reversible
     three-state chain; left != right singular functions; and the worst-case
     compatible linear-probe tie (spans tie even with a spectral gap).
  C  beyond linear probes: a nonlinear readout of the top-d encoder recovers a
     stable interaction target outside the top-d LINEAR span (product chain),
     so the signature is the encoder/sigma-algebra, not the subspace, and a
     smaller d can suffice; and sufficiency for a single stated compatible
     decision is decision-relative (a non-top span can serve a compatible
     target the top span does not).
  D  direction obstruction: the left signature is a function of x only, so no
     direction-dependent decision (forward vs reverse pair) is a function of
     it at any d.
"""
import json
import numpy as np


def stationary(P):
    """Stationary distribution of a row-stochastic matrix P (left eigvec, ev 1)."""
    w, V = np.linalg.eig(P.T)
    i = np.argmin(np.abs(w - 1.0))
    pi = np.real(V[:, i])
    pi = pi / pi.sum()
    return pi


def joint_from_kernel(P, pi=None):
    """P+(x,a) = pi(x) P(a|x); returns (Pplus, P_X, P_A)."""
    if pi is None:
        pi = stationary(P)
    Pplus = pi[:, None] * P
    P_X = Pplus.sum(1)
    P_A = Pplus.sum(0)
    return Pplus, P_X, P_A


def svd_operator(Pplus, P_X, P_A):
    """Whitened kernel SVD. Returns s, mu (cols, L2(P_X)-orthonormal),
    nu (cols, L2(P_A)-orthonormal), K."""
    K = Pplus / np.sqrt(np.outer(P_X, P_A))
    U, s, Vt = np.linalg.svd(K)
    mu = U / np.sqrt(P_X)[:, None]        # mu[:, i] = left singular function
    nu = Vt.T / np.sqrt(P_A)[:, None]     # nu[:, i] = right singular function
    return s, mu, nu, K


def two_step_chain(Pplus, P_X, P_A):
    """M[x, x'] = sum_a P(a|x) P(x'|a): the induced same-kind X-pair chain."""
    Pa_given_x = Pplus / P_X[:, None]        # P(a|x)
    Px_given_a = (Pplus / P_A[None, :]).T    # [a, x'] = P(x'|a)
    return Pa_given_x @ Px_given_a           # [x, x']


def worst_case_linear_error(P_V, s2, one_minus_eps):
    """Worst-case residual ||f - P_V f||^2 over unit targets f with
    sum s_i^2 u_i^2 >= (1-eps)^2 (THEORY-239's compatible class), via the
    S-procedure dual: min_{lam>=0} lam_max(I - P_V + lam(diag s2 - c I))."""
    n = len(s2)
    c = one_minus_eps ** 2
    D = np.diag(s2) - c * np.eye(n)
    A0 = np.eye(n) - P_V

    def g(lam):
        return np.linalg.eigvalsh(A0 + lam * D).max()

    lams = np.concatenate([[0.0], np.geomspace(1e-4, 1e3, 4000)])
    vals = np.array([g(l) for l in lams])
    return float(vals.min())


# ---------------------------------------------------------------- A, reduction
def check_reduction(P):
    Pplus, P_X, P_A = joint_from_kernel(P)
    s, mu, nu, K = svd_operator(Pplus, P_X, P_A)
    M = two_step_chain(Pplus, P_X, P_A)
    # M mu_i = s_i^2 mu_i  (M acts on function values)
    resid = [float(np.linalg.norm(M @ mu[:, i] - s[i] ** 2 * mu[:, i]))
             for i in range(len(s))]
    # reversibility of M wrt P_X
    rev = float(np.max(np.abs(P_X[:, None] * M - (P_X[:, None] * M).T)))
    # mu orthonormal in L2(P_X)
    gram = mu.T @ (P_X[:, None] * mu)
    orth = float(np.max(np.abs(gram - np.eye(len(s)))))
    return dict(singular_values=s.tolist(),
                M_eigfun_residual_max=float(np.max(resid)),
                M_reversible_defect=rev,
                mu_orthonormality_defect=orth)


# ---------------------------------------------- B, three-state non-reversible
def check_three_state():
    P = np.array([[0.1, 0.8, 0.1],
                  [0.1, 0.1, 0.8],
                  [0.6, 0.2, 0.2]])
    Pplus, P_X, P_A = joint_from_kernel(P)
    s, mu, nu, K = svd_operator(Pplus, P_X, P_A)
    # left vs right differ => genuinely directed
    left_right_gap = float(np.linalg.norm(np.abs(mu[:, 1]) - np.abs(nu[:, 1])))

    def norm1(v):
        return (v / np.abs(v[np.argmax(np.abs(v))]) * 1.30).round(2).tolist()

    return dict(pi=P_X.round(3).tolist(),
                singular_values=s.round(3).tolist(),
                mu2=norm1(mu[:, 1]), nu2=norm1(nu[:, 1]),
                left_right_gap=left_right_gap)


def check_tie():
    """Reproduce THEORY-239's tie: s=(1,.9,.8,.5,.1), eps=.15, d=2, r*=0.7708;
    top span and tilted spans V=span{mu1, cos th mu2 + sin th mu4} all tie."""
    s = np.array([1.0, 0.9, 0.8, 0.5, 0.1])
    eps = 0.15
    d = 2
    s2 = s ** 2
    one_minus_eps = 1 - eps
    r_star = (s2[0] - one_minus_eps ** 2) / (s2[0] - s2[d])  # 0.7708

    def P_span(cols):  # orthonormal standard basis columns -> projector
        B = np.zeros((5, len(cols)))
        return None, cols

    def proj(vecs):
        Q, _ = np.linalg.qr(np.array(vecs).T)
        return Q @ Q.T

    top = proj([np.eye(5)[0], np.eye(5)[1]])
    e_top = worst_case_linear_error(top, s2, one_minus_eps)
    tilts = {}
    for th in [0.05, 0.2, 0.5, 1.0]:
        v = np.cos(th) * np.eye(5)[1] + np.sin(th) * np.eye(5)[3]
        e = worst_case_linear_error(proj([np.eye(5)[0], v]), s2, one_minus_eps)
        tilts[f"theta={th}"] = round(e, 4)
    return dict(r_star=round(float(r_star), 4), e_top=round(e_top, 4),
                tilts=tilts)


# ------------------------------------------------- C, beyond linear probes
def product_chain(rho_a, rho_b):
    """Two independent 2-state symmetric chains, tensor product; uniform pi.
    Eigenfunctions chi_a=( +1,-1)x1, chi_b=1x(+1,-1), chi_a*chi_b."""
    def two_state(rho):
        p = (1 + rho) / 2
        return np.array([[p, 1 - p], [1 - p, p]])
    Pa, Pb = two_state(rho_a), two_state(rho_b)
    P = np.kron(Pa, Pb)
    return P


def check_nonlinear():
    rho_a, rho_b = 0.9, 0.8
    P = product_chain(rho_a, rho_b)
    Pplus, P_X, P_A = joint_from_kernel(P)   # symmetric here (reversible)
    s, mu, nu, K = svd_operator(Pplus, P_X, P_A)
    s2 = s ** 2
    # identify eigenfunctions by value pattern on states (a,b) in {0,1}^2
    states = np.array([[a, b] for a in (0, 1) for b in (0, 1)])
    chi_a = np.where(states[:, 0] == 0, 1.0, -1.0)
    chi_b = np.where(states[:, 1] == 0, 1.0, -1.0)
    inter = chi_a * chi_b
    # orthonormalise in L2(P_X) (uniform) -> already norm 1 since +-1 and uniform
    def nrm(v):
        return v / np.sqrt((P_X * v * v).sum())
    chi_a, chi_b, inter = nrm(chi_a), nrm(chi_b), nrm(inter)
    M = two_step_chain(Pplus, P_X, P_A)

    def stability(v):   # 1 - Rayleigh of (I-M): higher = more view-invariant
        return float((v * (M @ v)).sum() / (v * v).sum())

    # top-2 LINEAR span = {chi_a, chi_b} (eigs .9,.8). Target = inter (eig .72).
    # linear-probe residual of inter on span{chi_a, chi_b}:
    V = np.stack([chi_a, chi_b], 1)
    Pv = (P_X[:, None] * V)            # weighted
    G = V.T @ Pv
    coef = np.linalg.solve(G, V.T @ (P_X * inter))
    lin_resid = float((P_X * (inter - V @ coef) ** 2).sum())
    # nonlinear readout from encoder (chi_a, chi_b): inter = chi_a*chi_b exactly
    nonlin_resid = float((P_X * (inter - chi_a * chi_b) ** 2).sum())
    # decision-relative insufficiency: target chi_b, top-1 encoder = chi_a.
    # best readout E[chi_b | chi_a]; chi_a, chi_b independent -> 0.
    # group states by chi_a value, compute conditional mean of chi_b:
    cond = np.zeros_like(chi_b)
    for val in np.unique(chi_a):
        m = chi_a == val
        cond[m] = (P_X[m] * chi_b[m]).sum() / P_X[m].sum()
    top1_resid_chib = float((P_X * (chi_b - cond) ** 2).sum())
    comp1_resid_chib = 0.0  # competitor encoder chi_b recovers chi_b exactly
    return dict(
        stability_chi_a=round(stability(chi_a), 3),
        stability_chi_b=round(stability(chi_b), 3),
        stability_inter=round(stability(inter), 3),
        inter_linear_residual_top2=round(lin_resid, 4),
        inter_nonlinear_residual_top2=round(nonlin_resid, 6),
        chi_b_residual_from_top1=round(top1_resid_chib, 4),
        chi_b_residual_from_competitor=comp1_resid_chib)


# -------------------------------------------------- D, direction obstruction
def check_direction():
    P = np.array([[0.1, 0.8, 0.1],
                  [0.1, 0.1, 0.8],
                  [0.6, 0.2, 0.2]])
    Pplus, P_X, P_A = joint_from_kernel(P)
    # asymmetry of the ordered pair: forward minus reverse
    asym = float(np.max(np.abs(Pplus - Pplus.T)))
    # A decision d(x,a) = sign(x - a) (forward vs reverse order). Its best
    # predictor from x alone is E[d | x]; compare to the full decision.
    xs, as_ = np.meshgrid(range(3), range(3), indexing="ij")
    label = np.sign(xs - as_)                      # function on X x A
    w = Pplus                                        # weight of each ordered pair
    # best predictor from x only: E[label | x]
    pred_x = (w * label).sum(1) / w.sum(1)
    err_from_x = float((w * (label - pred_x[:, None]) ** 2).sum())
    var_label = float((w * (label - (w * label).sum()) ** 2).sum())
    # best predictor from full pair = label exactly -> err 0
    return dict(pair_asymmetry=asym,
                direction_error_from_x_only=round(err_from_x, 4),
                direction_variance=round(var_label, 4),
                direction_error_from_pair=0.0)


def main():
    P1 = np.array([[0.1, 0.8, 0.1],
                   [0.1, 0.1, 0.8],
                   [0.6, 0.2, 0.2]])
    out = dict(
        A_reduction=check_reduction(P1),
        B_three_state=check_three_state(),
        B_tie=check_tie(),
        C_nonlinear=check_nonlinear(),
        D_direction=check_direction(),
    )
    print(json.dumps(out, indent=2))
    with open("results.json", "w") as f:
        json.dump(out, f, indent=2)


if __name__ == "__main__":
    main()
