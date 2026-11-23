"""Two signalling-aware contextuality tests on the binary 3-cycle (LEAD-191).

The scenario is LIT-844's: observables X1, X2, X3, contexts
c1 = (X1, X2), c2 = (X2, X3), c3 = (X3, X1), outcomes {0, 1}.
An empirical model is a 3x4 array e[c, o], o indexing (a, b) in the order
(0,0), (0,1), (1,0), (1,1), a the first and b the second observable of the
context. Each row sums to 1.

Routes computed by linear programming (scipy.optimize.linprog, HiGHS):

- sheaf side: the contextual fraction CF and the signalling fraction SF of
  LIT-844 section 3a, and the corrected criterion CF > 2|M| SF it applies;
  plus two further readings of "contextual beyond signalling" that the
  record can state without the Vallee et al. paper (see README.md):
  * ns_part_contextual: every no-signalling part of a minimal-SF
    decomposition is contextual;
  * nearest_ns_contextual: the distance from e to the noncontextual set
    exceeds its distance to the no-signalling set, so every nearest
    no-signalling model is contextual (distance: sum over contexts of the
    total-variation distance, or the max over contexts).
- Contextuality-by-Default 2.0: noncontextual iff the six random variables
  R_q^c admit a coupling whose context bunches have e's distributions and
  whose connections are multimaximally coupled. Each content here lies in
  two contexts and is binary, so a multimaximal coupling of a connection is
  its maximal coupling, P(R_q^c = R_q^c') = 1 - |P(R_q^c = 0) - P(R_q^c' = 0)|.
"""

from __future__ import annotations

import itertools

import numpy as np
from scipy.optimize import linprog

CONTEXTS = ((0, 1), (1, 2), (2, 0))  # observable indices of c1, c2, c3
OUTCOMES = ((0, 0), (0, 1), (1, 0), (1, 1))
GLOBAL = list(itertools.product((0, 1), repeat=3))  # 8 global assignments
TOL = 1e-9


def pr_like(eps) -> np.ndarray:
    """LIT-844's PR-like model with parameters eps = (e1, e2, e3) in [-1, 1].

    c1, c2 correlated: (0,0) w.p. (1+e)/2, (1,1) w.p. (1-e)/2.
    c3 anticorrelated: (0,1) w.p. (1+e3)/2, (1,0) w.p. (1-e3)/2.
    With eps_i = 2 P_i(O1) - 1 and outcome 0 = O1, this is the schema's table.
    """
    e1, e2, e3 = (float(x) for x in eps)
    return np.array(
        [
            [(1 + e1) / 2, 0, 0, (1 - e1) / 2],
            [(1 + e2) / 2, 0, 0, (1 - e2) / 2],
            [0, (1 + e3) / 2, (1 - e3) / 2, 0],
        ]
    )


def from_probs(p1, p2, p3) -> np.ndarray:
    """The model from BERT's three normalised probabilities P_i(O1)."""
    return pr_like((2 * p1 - 1, 2 * p2 - 1, 2 * p3 - 1))


def _restriction_matrix() -> np.ndarray:
    """A[(c, o), g] = 1 when global assignment g restricts to o on context c."""
    a = np.zeros((12, 8))
    for gi, g in enumerate(GLOBAL):
        for ci, (i, j) in enumerate(CONTEXTS):
            oi = OUTCOMES.index((g[i], g[j]))
            a[ci * 4 + oi, gi] = 1
    return a


RESTRICT = _restriction_matrix()


def _ns_equalities() -> np.ndarray:
    """Rows saying the marginals of each observable agree across contexts.

    Acting on a vector f of length 12 (f[c*4+o]). Also all contexts share
    one total mass.
    """
    rows = []
    # each observable appears in two contexts; marginal P(obs = 0) agrees
    for obs in range(3):
        cs = [(ci, pos) for ci, ctx in enumerate(CONTEXTS) for pos, x in enumerate(ctx) if x == obs]
        (c_a, p_a), (c_b, p_b) = cs
        r = np.zeros(12)
        for oi, o in enumerate(OUTCOMES):
            if o[p_a] == 0:
                r[c_a * 4 + oi] += 1
            if o[p_b] == 0:
                r[c_b * 4 + oi] -= 1
        rows.append(r)
    # equal total mass per context
    for ci in (1, 2):
        r = np.zeros(12)
        r[0:4] = 1
        r[ci * 4 : ci * 4 + 4] = -1
        rows.append(r)
    return np.array(rows)


NS_EQ = _ns_equalities()


def _lp(c, a_ub=None, b_ub=None, a_eq=None, b_eq=None, bounds=(0, None)):
    res = linprog(c, A_ub=a_ub, b_ub=b_ub, A_eq=a_eq, b_eq=b_eq, bounds=bounds, method="highs")
    if res.status != 0:
        raise RuntimeError(res.message)
    return res


def contextual_fraction(e: np.ndarray) -> float:
    """CF = 1 - max mass of a subnormalised global distribution below e."""
    res = _lp(-np.ones(8), a_ub=RESTRICT, b_ub=e.reshape(-1))
    return 1.0 + res.fun


def signalling_fraction(e: np.ndarray) -> float:
    """SF = 1 - max mass of a subnormalised no-signalling model below e."""
    c = np.zeros(12)
    c[0:4] = -1  # maximise the mass of context 1 (= every context's mass)
    res = _lp(c, a_eq=NS_EQ, b_eq=np.zeros(len(NS_EQ)), bounds=[(0, v) for v in e.reshape(-1)])
    return 1.0 + res.fun


def sheaf_corrected(e: np.ndarray) -> bool:
    """LIT-844's criterion (3.4): contextual when CF > 2|M| SF."""
    return contextual_fraction(e) > 2 * 3 * signalling_fraction(e) + TOL


def _feasible(c, **kw) -> bool:
    res = linprog(c, method="highs", **kw)
    return res.status == 0


def ns_part_contextual(e: np.ndarray) -> bool:
    """Every no-signalling part of a minimal-SF decomposition is contextual.

    True when no noncontextual subnormalised model of mass 1 - SF lies below
    e. False when SF = 1 (there is no NS part).
    """
    sf = signalling_fraction(e)
    if sf > 1 - 1e-7:
        return False
    w = 1 - sf - 1e-9
    feas = _feasible(
        np.zeros(8), A_ub=RESTRICT, b_ub=e.reshape(-1), A_eq=np.ones((1, 8)), b_eq=[w], bounds=(0, None)
    )
    return not feas


def _distance_lp(e: np.ndarray, target: str, norm: str) -> float:
    """Distance from e to the NS set or the NC set.

    Variables: f (12, the model), t (12, |e - f| per cell), and for NC the
    8 global weights g with f = RESTRICT g. norm 'sum' minimises the sum
    over contexts of the TV distance 0.5*sum|e-f|; 'max' minimises the max
    over contexts.
    """
    ev = e.reshape(-1)
    nf, nt = 12, 12
    ng = 8 if target == "nc" else 0
    nz = 1 if norm == "max" else 0
    n = nf + nt + ng + nz
    a_ub, b_ub, a_eq, b_eq = [], [], [], []
    # t >= f - e, t >= e - f
    for k in range(12):
        r = np.zeros(n); r[k] = 1; r[nf + k] = -1; a_ub.append(r); b_ub.append(ev[k])
        r = np.zeros(n); r[k] = -1; r[nf + k] = -1; a_ub.append(r); b_ub.append(-ev[k])
    # each context normalised
    for ci in range(3):
        r = np.zeros(n); r[ci * 4 : ci * 4 + 4] = 1; a_eq.append(r); b_eq.append(1.0)
    if target == "ns":
        for row in NS_EQ:
            r = np.zeros(n); r[:12] = row; a_eq.append(r); b_eq.append(0.0)
    else:
        for k in range(12):
            r = np.zeros(n); r[k] = 1; r[nf + nt : nf + nt + 8] = -RESTRICT[k]; a_eq.append(r); b_eq.append(0.0)
    c = np.zeros(n)
    if norm == "sum":
        c[nf : nf + nt] = 0.5
    else:
        c[-1] = 1
        for ci in range(3):
            r = np.zeros(n); r[nf + ci * 4 : nf + ci * 4 + 4] = 0.5; r[-1] = -1
            a_ub.append(r); b_ub.append(0.0)
    res = _lp(c, a_ub=np.array(a_ub), b_ub=b_ub, a_eq=np.array(a_eq), b_eq=b_eq)
    return float(res.fun)


def nearest_ns_contextual(e: np.ndarray, norm: str = "sum") -> bool:
    """Every NS model nearest to e is contextual: d(e, NC) > d(e, NS)."""
    return _distance_lp(e, "nc", norm) > _distance_lp(e, "ns", norm) + 1e-7


# ---------------------------------------------------------------- CbD 2.0

# the six random variables R_q^c, as (content, context) pairs
CBD_VARS = [(0, 0), (1, 0), (1, 1), (2, 1), (2, 2), (0, 2)]
ATOMS = list(itertools.product((0, 1), repeat=6))


def _marg0(e: np.ndarray, content: int, context: int) -> float:
    pos = CONTEXTS[context].index(content)
    return float(sum(e[context, oi] for oi, o in enumerate(OUTCOMES) if o[pos] == 0))


def cbd_noncontextual(e: np.ndarray) -> bool:
    """CbD 2.0: a coupling of the six variables exists with bunches as in e
    and every connection multimaximally (here: maximally) coupled."""
    a_eq, b_eq = [], []
    for ci, (i, j) in enumerate(CONTEXTS):
        vi, vj = CBD_VARS.index((i, ci)), CBD_VARS.index((j, ci))
        for oi, o in enumerate(OUTCOMES):
            a_eq.append([1.0 if (x[vi], x[vj]) == o else 0.0 for x in ATOMS])
            b_eq.append(e[ci, oi])
    for q in range(3):
        (va, ca), (vb, cb) = [(CBD_VARS.index(v), v[1]) for v in CBD_VARS if v[0] == q]
        p_eq = 1 - abs(_marg0(e, q, ca) - _marg0(e, q, cb))
        a_eq.append([1.0 if x[va] == x[vb] else 0.0 for x in ATOMS])
        b_eq.append(p_eq)
    res = linprog(np.zeros(64), A_eq=np.array(a_eq), b_eq=b_eq, bounds=(0, None), method="highs")
    return res.status == 0


def cbd_contextual(e: np.ndarray) -> bool:
    return not cbd_noncontextual(e)


# ---------------------------------------------------------------- closed forms


def closed_form(eps):
    """LIT-844's closed forms: SF = max|e_i|, Delta, and the two verdicts."""
    e1, e2, e3 = eps
    sf = max(abs(e1), abs(e2), abs(e3))
    delta = abs(e1 - e2) + abs(e2 - e3) + abs(e3 + e1)
    return {"SF": sf, "Delta": delta, "sheaf": sf < 1 / 6, "cbd": delta < 2}
