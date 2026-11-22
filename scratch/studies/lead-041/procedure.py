"""The LEAD-041 procedure: read from a record of conduct which ordering
prevails, how strongly, whether it persists and resumes, and tell
ambivalence from neutrality and from no contest.

It implements the seven steps of QUESTION-268's procedure in the ordinal
form CLAIM-434 and TERM-077/078 require, with the choices LEAD-041 adds:

- contest is read from the perspectives' rankings, measured independently
  of the decisions, never from the decisions themselves (the evaluative
  space model's warning, NOTE-1101: ambivalent and neutral systems can
  choose alike);
- a decision decides only the pairs that contain the option chosen, among
  the options then available;
- a window is "ambivalent" only when its wins reverse more than a null
  allows: the best-fitting ordering, with departures as frequent as on the
  record's uncontested episodes (where no two perspectives disagree);
- a window in which an ordering prevails is "neutral" only if the system
  keeps to its reference course along it, and otherwise signed;
- across windows, alternation of the leading ordering is tested against a
  permutation of decisions among episodes with the same contest structure.

Pure Python plus numpy; deterministic given a seed.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import permutations
from typing import Callable, Dict, List, Optional, Sequence, Tuple

import numpy as np

Ranking = Dict[str, float]  # option -> score, higher preferred; equal = tie


@dataclass
class Episode:
    t: int                      # time index
    window: str                 # window label
    options: Tuple[str, ...]    # options available at t
    rankings: Dict[str, Ranking]  # perspective -> ranking over options
    decision: str
    context: str = ""

    def __post_init__(self):
        if self.decision not in self.options:
            raise ValueError("decision must be among the options available")


# ---------------------------------------------------------------- step 1-2

def strict(r: Ranking, x: str, y: str) -> int:
    """+1 if r ranks x above y, -1 if below, 0 if tied."""
    return int(np.sign(r[x] - r[y]))


def contested_pairs(e: Episode) -> List[Tuple[str, str]]:
    """Pairs on which two perspectives rank strictly and oppositely."""
    out = []
    names = list(e.rankings)
    for i, x in enumerate(e.options):
        for y in e.options[i + 1:]:
            signs = {strict(e.rankings[p], x, y) for p in names}
            if 1 in signs and -1 in signs:
                out.append((x, y))
    return out


def is_contested(e: Episode) -> bool:
    return bool(contested_pairs(e))


def wins(e: Episode) -> List[Tuple[str, str]]:
    """(winner, loser) for each contested pair the decision decides."""
    d = e.decision
    return [(d, y if x == d else x) for x, y in contested_pairs(e) if d in (x, y)]


# ---------------------------------------------------------------- step 3-5

def agreement(order: Sequence[str], ws: Sequence[Tuple[str, str]]) -> float:
    """Share of wins in which the winner stands above the loser in order
    (order lists options best first)."""
    if not ws:
        return float("nan")
    pos = {o: i for i, o in enumerate(order)}
    return sum(pos[w] < pos[l] for w, l in ws) / len(ws)


def fit(ws: Sequence[Tuple[str, str]], options: Sequence[str]):
    """Least reversal fraction and the class of best-fitting orderings.
    Brute force over orderings: fine for the handful of options a
    negotiation faces here."""
    best, cls = -1.0, []
    for order in permutations(sorted(options)):
        a = agreement(order, ws)
        if a > best + 1e-12:
            best, cls = a, [order]
        elif abs(a - best) <= 1e-12:
            cls.append(order)
    return 1.0 - best, cls


# ---------------------------------------------------------------- step 6 nulls

def departure_rate(eps: Sequence[Episode]) -> Optional[float]:
    """How often decisions depart from the common top choice on episodes
    where no pair is contested and the perspectives that rank strictly
    share a unique top. None if there are none."""
    n = dep = 0
    for e in eps:
        if is_contested(e):
            continue
        tops = set()
        for r in e.rankings.values():
            m = max(r[o] for o in e.options)
            top = [o for o in e.options if r[o] == m]
            if len(top) == 1:
                tops.add(top[0])
        if len(tops) == 1:
            n += 1
            dep += e.decision not in tops
    return None if n == 0 else dep / n


def departure_profile(eps: Sequence[Episode]) -> Optional[List[float]]:
    """On episodes where nothing is contested and every perspective that
    ranks strictly ranks the options alike, the share of decisions that
    took the common ranking's first, second, ... option. This keeps the
    record's own pattern of departures: mostly to the compromise, or as
    often to the opposite extreme. None if there are no such episodes."""
    counts: Dict[int, int] = {}
    for e in eps:
        if is_contested(e):
            continue
        strict_r = [r for r in e.rankings.values() if len({r[o] for o in e.options}) > 1]
        if not strict_r:
            continue
        r = strict_r[0]
        order = sorted(e.options, key=lambda o: -r[o])
        k = order.index(e.decision)
        counts[k] = counts.get(k, 0) + 1
    if not counts:
        return None
    m = max(counts) + 1
    tot = sum(counts.values())
    return [counts.get(k, 0) / tot for k in range(m)]


def _profile(eps_rate, m):
    """A departure profile over m positions: a list is used as given
    (truncated and renormalized); a float e means 1 - e on the first and e
    spread evenly over the rest."""
    if isinstance(eps_rate, (list, tuple)):
        q = list(eps_rate[:m]) + [0.0] * max(0, m - len(eps_rate))
    else:
        q = [1 - eps_rate] + [eps_rate / (m - 1)] * (m - 1) if m > 1 else [1.0]
    s = sum(q)
    return [x / s for x in q] if s > 0 else [1.0] + [0.0] * (m - 1)


def simulate_reversal(eps: Sequence[Episode], order: Sequence[str], eps_rate,
                      rng: np.random.Generator, n_sim: int = 2000) -> np.ndarray:
    """Least reversal fractions of records that keep the window's episodes,
    options and contests, and draw each decision by its position in `order`
    among the options available, with the departure profile `eps_rate`
    (a list by position, or a float for even departures)."""
    pos = {o: i for i, o in enumerate(order)}
    opts = sorted({o for e in eps for o in e.options})
    contested = [e for e in eps if is_contested(e)]
    ranked = [sorted(e.options, key=lambda o: pos[o]) for e in contested]
    probs = [_profile(eps_rate, len(r)) for r in ranked]
    out = np.empty(n_sim)
    for k in range(n_sim):
        ws = []
        for e, r, q in zip(contested, ranked, probs):
            d = r[rng.choice(len(r), p=q)]
            ws.extend(wins(Episode(e.t, e.window, e.options, e.rankings, d, e.context)))
        out[k] = fit(ws, opts)[0] if ws else 0.0
    return out


def misfit(ws, named) -> float:
    """1 - the best named candidate's alignment: how much of the record no
    perspective's ordering, and no named candidate such as inertia,
    accounts for."""
    return 1.0 - max(candidate_alignment(ws, named).values())


def ambivalence_test(eps: Sequence[Episode], named, eps_rate, rng: np.random.Generator,
                     n_sim: int = 2000) -> float:
    """Step 6, within a window. The null is that some named candidate
    prevails, with departures as the record makes them where nothing is
    contested (eps_rate: a profile by position, or a float). For each
    ordering of each candidate, simulate the window's contested episodes
    and compare the misfit to the best named candidate. Returns the largest
    p-value over the candidates' orderings: small only when no candidate
    with the record's own noise would leave so much unaccounted for."""
    contested = [e for e in eps if is_contested(e)]
    ws = [w for e in contested for w in wins(e)]
    t_obs = misfit(ws, named)
    pmax = 0.0
    for cls in named.values():
        for order in cls:
            pos = {o: i for i, o in enumerate(order)}
            ranked = [sorted(e.options, key=lambda o: pos[o]) for e in contested]
            probs = [_profile(eps_rate, len(r)) for r in ranked]
            ge = 0
            for _ in range(n_sim):
                sw = []
                for e, r, q in zip(contested, ranked, probs):
                    d = r[rng.choice(len(r), p=q)]
                    sw.extend(wins(Episode(e.t, e.window, e.options, e.rankings, d, e.context)))
                ge += misfit(sw, named) >= t_obs - 1e-12
            pmax = max(pmax, (ge + 1) / (n_sim + 1))
    return pmax


# ---------------------------------------------------------------- per window

@dataclass
class WindowResult:
    window: str
    n_episodes: int
    n_contested: int
    n_wins: int
    reversal: float = float("nan")
    best_class: List[Tuple[str, ...]] = field(default_factory=list)
    p_ambivalence: float = float("nan")
    perspective_agreement: Dict[str, float] = field(default_factory=dict)
    candidate_alignment: Dict[str, float] = field(default_factory=dict)
    p_lead: float = float("nan")
    by_context: Dict[str, List[Tuple[str, ...]]] = field(default_factory=dict)
    verdict: str = ""
    leading: Optional[str] = None
    sign: Optional[str] = None


def candidate_alignment(ws, named: Dict[str, Sequence[Sequence[str]]]) -> Dict[str, float]:
    """Step 4: for each named candidate (a perspective's ordering, or a
    class such as inertia, hold on top), the share of the wins it agrees
    with, taking the best member of its class."""
    return {n: max(agreement(o, ws) for o in cls) for n, cls in named.items()}


def leading_perspective(align: Dict[str, float], margin: float = 1e-9):
    """The candidate whose alignment is highest; "tied" if two share it."""
    if not align:
        return None
    top = max(align.values())
    names = [n for n, a in align.items() if a >= top - margin]
    return names[0] if len(names) == 1 else "tied"


def analyse_window(label: str, eps: Sequence[Episode], named: Dict[str, Sequence[Sequence[str]]],
                   eps_rate: float, rng: np.random.Generator, min_contested: int = 4,
                   alpha: float = 0.05, n_sim: int = 2000,
                   progress: Optional[Callable[[str, Sequence[Episode]], Optional[float]]] = None,
                   reference: Optional[float] = None, tol: float = 0.0) -> WindowResult:
    contested = [e for e in eps if is_contested(e)]
    ws = [w for e in contested for w in wins(e)]
    res = WindowResult(label, len(eps), len(contested), len(ws))
    if len(contested) < min_contested:
        res.verdict = "no contest" if not contested else "too few contests"
        return res
    opts = sorted({o for e in eps for o in e.options})
    res.reversal, res.best_class = fit(ws, opts)
    persp = sorted({p for e in contested for p in e.rankings})
    for p in persp:
        res.perspective_agreement[p] = _persp_agreement(contested, p)
    for c in sorted({e.context for e in contested}):
        wc = [w for e in contested if e.context == c for w in wins(e)]
        res.by_context[c] = fit(wc, opts)[1]
    res.candidate_alignment = candidate_alignment(ws, named)
    res.p_ambivalence = ambivalence_test(eps, named, eps_rate, rng, n_sim)
    res.leading = leading_perspective(res.candidate_alignment)
    if res.leading not in (None, "tied"):
        res.p_lead = prevalence_test(contested, named, res.leading, rng)
    if res.p_ambivalence < alpha:
        res.verdict = "ambivalent"
    elif len(res.by_context) > 1 and _disjoint_classes(res.by_context):
        res.verdict = "split by context"
    elif not (res.p_lead < alpha):
        res.verdict = "indeterminate"
    else:
        res.verdict = "prevails"
        if progress is not None and res.leading is not None:
            p = progress(res.leading, eps)
            if p is not None and reference is not None:
                d = p - reference
                res.sign = "neutral" if abs(d) <= tol else ("positive" if d > 0 else "negative")
    return res


def prevalence_test(contested: Sequence[Episode], named, lead: str,
                    rng: np.random.Generator, n_boot: int = 2000) -> float:
    """Bootstrap over contested episodes: the share of resamples in which
    the leading candidate's alignment does not exceed every rival's. Small
    values mean the lead is shown, not just observed."""
    ws_by = [wins(e) for e in contested]
    best = {n: max(cls, key=lambda o: agreement(o, [w for x in ws_by for w in x]))
            for n, cls in named.items()}
    agree = {n: np.array([sum(_above(best[n], w, l) for w, l in x) for x in ws_by])
             for n in named}
    tot = np.array([len(x) for x in ws_by])
    k = len(contested)
    fails = 0
    for _ in range(n_boot):
        idx = rng.integers(k, size=k)
        T = tot[idx].sum()
        if T == 0:
            fails += 1
            continue
        a = {n: agree[n][idx].sum() / T for n in named}
        if any(a[n] >= a[lead] for n in named if n != lead):
            fails += 1
    return fails / n_boot


def _above(order, w, l):
    return order.index(w) < order.index(l)


def _persp_agreement(contested: Sequence[Episode], p: str) -> float:
    s = []
    for e in contested:
        for w, l in wins(e):
            v = strict(e.rankings[p], w, l)
            if v != 0:
                s.append(v > 0)
    return float("nan") if not s else float(np.mean(s))


def _disjoint_classes(by_ctx: Dict[str, List[Tuple[str, ...]]]) -> bool:
    sets = [set(v) for v in by_ctx.values() if v]
    return len(sets) > 1 and not set.intersection(*sets)


# ---------------------------------------------------------------- across windows

def switches(seq: Sequence[Optional[str]]) -> int:
    s = [x for x in seq if x is not None]
    return sum(a != b for a, b in zip(s, s[1:]))


def persistence_and_resumption(seq: Sequence[Tuple[str, Optional[str]]], name: str,
                               min_run: int = 2):
    """Read persistence and resumption of one named ordering off a sequence
    of (window, leading) pairs. A run is consecutive windows it leads
    (windows with no verdict are skipped, not counted as interruptions).
    A resumption is a run of at least min_run, then one or more windows led
    by another ordering or ambivalent, then a return."""
    s = [(w, x) for w, x in seq if x is not None]
    runs, cur = [], []
    for w, x in s:
        if x == name:
            cur.append(w)
        else:
            if cur:
                runs.append(cur)
            cur = []
            runs.append(("gap", w))
    if cur:
        runs.append(cur)
    resumptions = []
    for i in range(len(runs)):
        if isinstance(runs[i], list) and len(runs[i]) >= min_run:
            j = i + 1
            gap = []
            while j < len(runs) and isinstance(runs[j], tuple):
                gap.append(runs[j][1])
                j += 1
            if gap and j < len(runs):
                resumptions.append({"after": runs[i][-1], "interruption": gap,
                                    "resumed": runs[j][0]})
    longest = max((len(r) for r in runs if isinstance(r, list)), default=0)
    return {"longest_run": longest, "resumptions": resumptions}


def alternation_test(eps: Sequence[Episode], windows: Sequence[str],
                     named: Dict[str, Sequence[Sequence[str]]], rng: np.random.Generator,
                     n_perm: int = 500, min_contested: int = 4):
    """Observed switches of the leading named ordering between consecutive
    windows with enough contests, against a permutation null that shuffles
    decisions among contested episodes of identical contest structure
    (same options, same rankings), across the whole record."""
    def leads(ep_list):
        out = []
        for w in windows:
            ce = [e for e in ep_list if e.window == w and is_contested(e)]
            if len(ce) < min_contested:
                out.append(None)
                continue
            ws = [x for e in ce for x in wins(e)]
            out.append(leading_perspective(candidate_alignment(ws, named)))
        return out

    obs = switches(leads(eps))
    strata: Dict[tuple, List[int]] = {}
    for i, e in enumerate(eps):
        if is_contested(e):
            key = (e.options, tuple(sorted((p, tuple(sorted(r.items()))) for p, r in e.rankings.items())))
            strata.setdefault(key, []).append(i)
    null = np.empty(n_perm)
    for k in range(n_perm):
        dec = [e.decision for e in eps]
        for idx in strata.values():
            perm = rng.permutation(idx)
            for a, b in zip(idx, perm):
                dec[a] = eps[b].decision
        sh = [Episode(e.t, e.window, e.options, e.rankings, dec[i], e.context)
              for i, e in enumerate(eps)]
        null[k] = switches(leads(sh))
    return {"observed": obs, "null_mean": float(null.mean()),
            "p_more": float((np.sum(null >= obs) + 1) / (n_perm + 1)),
            "p_fewer": float((np.sum(null <= obs) + 1) / (n_perm + 1))}
