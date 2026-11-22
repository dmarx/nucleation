"""One cost model for stored work (LEAD-108).

A store is anything that holds the result of earlier work so that a later
demand can be met by reading it instead of redoing the work: speed bugs, a
filed argument, a LEGO bin. The model compares two routes for a stream of
demands:

  on demand   compute (reconstruct, search) each time;
  store       pay once to build the store, keep it, and read it back,
              falling back to computing when it does not serve or is wrong.

Every quantity is in one unit of work. Each piece of work is multiplied by
the price of work at the moment it is done (lam), so moving work from a busy
moment to a quiet one can pay even when the total is unchanged. The terms:

  F, lam_F        construction, and the price of work when it is paid
  U, lam_U        upkeep over the store's life (keeping it present and current)
  pi              predictability: the chance a demand is one the store serves
  rho             retrieval per served demand: recognizing that the store
                  serves it, searching for the item, reading it
  miss            cost of finding out that the store does not serve a demand
  v, delta        verification per use, and the chance it catches a wrong result
  sigma           staleness or bias: chance the stored result is wrong for
                  the demand at hand
  L               loss when a wrong result is used undetected
  R               revision when a wrong stored result is caught
  eps             erosion: fractional rise in the on-demand cost, paid
                  whenever the store route falls back on it
  spill, n_other  added retrieval cost the store imposes on each of n_other
                  other demands (more bins to scan, more filings to recognize
                  among)
  c, sigma_A, L_A the on-demand route's cost, error chance and loss
  B               the work available for one demand at the moment it comes

Three verdicts are kept apart (CLAIM-761, CLAIM-760):

  feasible      per demand, does the route's work fit within B (TERM-055's
                availability, as a probability over the paths a demand takes)
  lifetime      priced total over the horizon, construction included
  distributed   the same totals split by the party that pays each item

Choices made here, not given by the lead: costs are expectations (risk
neutral) except feasibility, which is a chance over paths; no discounting;
erosion is a fixed fraction, not a function of how long the store has been
relied on; a wrong stored result that is caught is replaced by computing on
demand, plus revision.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import math

INF = math.inf


@dataclass
class OnDemand:
    c: float               # work to compute on demand
    sigma_A: float = 0.0   # chance the on-demand result is wrong
    L_A: float = 0.0       # loss when it is wrong and used
    party: str = "user"


@dataclass
class Demands:
    n: float               # expected number of demands over the horizon
    lam: float = 1.0       # price of work at the moment of demand
    B: float = INF         # work available per demand at that moment
    pi: float = 1.0        # chance a demand is one the store serves
    party: str = "user"


@dataclass
class Store:
    F: float
    lam_F: float = 1.0
    U: float = 0.0
    lam_U: float = 1.0
    rho: float = 0.0
    miss: float = 0.0
    v: float = 0.0
    delta: float = 0.0
    sigma: float = 0.0
    L: float = 0.0
    R: float = 0.0
    eps: float = 0.0
    spill: float = 0.0
    n_other: float = 0.0
    lam_other: float = 1.0
    party_F: str = "user"
    party_U: str = "user"
    party_other: str = "user"


def fallback_cost(s: Store, a: OnDemand) -> float:
    """On-demand cost when the store route falls back on it, after erosion."""
    return a.c * (1.0 + s.eps)


def per_demand_store(s: Store, a: OnDemand, d: Demands) -> float:
    """Expected unpriced work for one demand on the store route."""
    fb = fallback_cost(s, a)
    served = (s.rho + s.v
              + s.sigma * (s.delta * (fb + s.R + a.sigma_A * a.L_A)
                           + (1.0 - s.delta) * s.L))
    unserved = s.miss + fb + a.sigma_A * a.L_A
    return d.pi * served + (1.0 - d.pi) * unserved


def per_demand_on_demand(a: OnDemand) -> float:
    return a.c + a.sigma_A * a.L_A


def lifetime(s: Store, a: OnDemand, ds: list[Demands]) -> dict:
    """Priced totals of both routes, and their split by party."""
    store_items = [(s.party_F, s.lam_F * s.F), (s.party_U, s.lam_U * s.U),
                   (s.party_other, s.lam_other * s.spill * s.n_other)]
    od_items = []
    for d in ds:
        store_items.append((d.party, d.n * d.lam * per_demand_store(s, a, d)))
        od_items.append((d.party, d.n * d.lam * per_demand_on_demand(a)))
    def split(items):
        out: dict[str, float] = {}
        for p, x in items:
            out[p] = out.get(p, 0.0) + x
        return out
    st, od = sum(x for _, x in store_items), sum(x for _, x in od_items)
    return {"store": st, "on_demand": od, "saving": od - st,
            "store_by_party": split(store_items),
            "on_demand_by_party": split(od_items)}


def availability_store(s: Store, a: OnDemand, d: Demands) -> float:
    """Chance a demand is met correctly within B on the store route."""
    fb = fallback_cost(s, a)
    ok = lambda work: 1.0 if work <= d.B else 0.0
    fresh = (1.0 - s.sigma) * ok(s.rho + s.v)
    caught = s.sigma * s.delta * ok(s.rho + s.v + fb) * (1.0 - a.sigma_A)
    served = fresh + caught          # a wrong result used undetected fails
    unserved = ok(s.miss + fb) * (1.0 - a.sigma_A)
    return d.pi * served + (1.0 - d.pi) * unserved


def availability_on_demand(a: OnDemand, d: Demands) -> float:
    return (1.0 if a.c <= d.B else 0.0) * (1.0 - a.sigma_A)


def break_even_n(s: Store, a: OnDemand, d: Demands) -> float:
    """Demands of one class needed for the store to pay over its life.

    Fixed costs (construction, upkeep, spill) are divided by the priced
    saving per demand. Infinite when a demand costs no less on the store
    route.
    """
    fixed = s.lam_F * s.F + s.lam_U * s.U + s.lam_other * s.spill * s.n_other
    per = d.lam * (per_demand_on_demand(a) - per_demand_store(s, a, d))
    if per <= 0:
        return INF
    return fixed / per
