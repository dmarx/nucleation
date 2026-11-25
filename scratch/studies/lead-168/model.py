"""LEAD-168: three institutions in two arrangements.

An executive E, a reviewer R and an enforcer F. One episode has five stages:

  t0  E acts: 'r' (an act R would uphold) or 'x' (an act R would order reversed)
  t1  a challenger challenges the act, or not (a probe input)
  t2  R rules: 'uphold', 'order' (reverse the act) or 'abstain'
  t3  F executes the order at some time, or does not
  t4  outcome: the act 'stands' or is 'reversed' (before the deadline T)

The two arrangements share every rule except F's:

  I (independent):  F executes an order iff F is able (cap=True).
  C (conditioned):  F executes an order iff F is able AND E's signal permits;
                    E's signal is a function of E's disposition and whether
                    the order runs against E (adverse).  In the delay variant
                    E permits only after d steps.

E's disposition is a probe input in the fixed-policy reading
('acquiesce' or 'withhold'), and is derived from payoffs in the anticipation
reading.  Nothing here is calibrated to any real institution.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product

STAGES = ("action", "challenge", "ruling", "enforcement", "outcome")


@dataclass(frozen=True)
class Probe:
    act: str            # 'r' or 'x'
    challenged: bool
    adverse: bool       # does a reversal order run against E's preference?
    disposition: str    # 'acquiesce' or 'withhold' (E's signal policy in C)
    cap: bool = True    # is F able to execute?
    delay: int = 0      # steps E holds an order before permitting (C only)
    t_order: int = 1    # step at which the order issues
    deadline: int = 10  # step after which the act is irreversible


def ruling(p: Probe) -> str:
    """R rules by law alone (fixed-policy reading)."""
    if not p.challenged:
        return "none"
    return "order" if p.act == "x" else "uphold"


def signal(p: Probe) -> tuple[bool, int]:
    """E's signal in arrangement C: (permits, after how many steps)."""
    if p.adverse and p.disposition == "withhold":
        return (p.delay > 0, p.delay)  # pure withholding when delay == 0
    return (True, 0)


def enforcement(arr: str, p: Probe) -> str:
    """F's event: 'none' (no order), 'executed@t' or 'not_executed'."""
    if ruling(p) != "order":
        return "none"
    if not p.cap:
        return "not_executed"
    if arr == "I":
        return f"executed@{p.t_order}"
    if arr == "C":
        permits, lag = signal(p)
        if not permits:
            return "not_executed"
        return f"executed@{p.t_order + lag}"
    raise ValueError(arr)


def outcome(arr: str, p: Probe) -> str:
    e = enforcement(arr, p)
    if e.startswith("executed@"):
        t = int(e.split("@")[1])
        return "reversed" if t <= p.deadline else "stands"
    return "stands"


def trace(arr: str, p: Probe) -> tuple[str, ...]:
    """The observable trace: E's signal is NOT in it (it is internal to C)."""
    return (p.act, "challenged" if p.challenged else "unchallenged",
            ruling(p), enforcement(arr, p), outcome(arr, p))


def first_divergence(a: tuple, b: tuple) -> str | None:
    for name, u, v in zip(STAGES, a, b):
        if u != v:
            return name
    return None


def routine(p: Probe) -> bool:
    """Routine operation: no order that runs against E (adverse order absent)."""
    return not (ruling(p) == "order" and p.adverse)


def all_probes(delays=(0,), caps=(True,), deadline=10):
    for act, ch, adv, disp, cap, d in product(
            "rx", (False, True), (False, True), ("acquiesce", "withhold"),
            caps, delays):
        yield Probe(act, ch, adv, disp, cap, d, 1, deadline)


# --------------------------------------------------------------------------
# Structural reading: on which inputs does F's decision depend?

def f_depends_on_signal(arr: str) -> bool:
    """Intervene on E's signal with the order fixed: does F's act change?"""
    base = Probe("x", True, False, "acquiesce")        # an order E endorses
    forced = Probe("x", True, True, "withhold")        # do(signal = withhold)
    return enforcement(arr, base) != enforcement(arr, forced)


# --------------------------------------------------------------------------
# Anticipation reading: backward induction on stated payoffs.

@dataclass(frozen=True)
class Payoffs:
    g: float    # E's gain while x stands
    c: float    # E's cost when x is reversed (on top of losing g)
    kw: float   # E's cost of withholding permission from an adverse order
    p: float    # probability that x is challenged
    u: float    # R's cost of upholding an unlawful act (or abstaining)
    l: float    # R's cost of issuing an order that is not enforced


def solve(arr: str, pay: Payoffs, depth: str) -> dict:
    """Equilibrium path stages for one arrangement.

    depth: 'myopic'   E acts as if x is never reversed; R rules by law;
           'reviewer' R anticipates enforcement; E myopic;
           'full'     R and E both anticipate.
    Returns the on-path action, ruling-if-challenged and enforcement.
    """
    # t3: does E withhold an adverse order in C?
    withhold = arr == "C" and pay.g > pay.kw
    enforced = not withhold
    # t2: R's ruling on a challenged x
    if depth in ("reviewer", "full") and not enforced:
        rul = "order" if pay.u > pay.l else "abstain"
    else:
        rul = "order"
    # value to E of x, given the challenge probability
    if rul == "order" and enforced:
        vx = (1 - pay.p) * pay.g - pay.p * pay.c
    elif rul == "order":                     # order issued, E withholds
        vx = pay.g - pay.p * pay.kw
    else:                                    # R abstains
        vx = pay.g
    if depth == "full":
        act = "x" if vx > 0 else "r"
    else:
        act = "x" if pay.g > 0 else "r"
    enf = "executed" if (rul == "order" and enforced) else (
        "not_executed" if rul == "order" else "none")
    return {"action": act, "ruling": rul, "enforcement": enf}


def first_divergence_game(pay: Payoffs, depth: str) -> str | None:
    a, b = solve("I", pay, depth), solve("C", pay, depth)
    if a["action"] != b["action"]:
        return "action"
    if a["action"] == "r":
        return None  # no challengeable act on either path: off path only
    for k in ("ruling", "enforcement"):
        if a[k] != b[k]:
            return k
    return None


# --------------------------------------------------------------------------
# What a non-execution shows (QUESTION-279): F unable vs E withholding.

def p_withheld_given_not_executed(q_cap: float, w: float) -> float:
    """In C: F able with prob q_cap; E withholds an adverse order with prob w.
    P(withheld | not executed).  In I the answer is always 0."""
    p_ne = (1 - q_cap) + q_cap * w
    return 0.0 if p_ne == 0 else q_cap * w / p_ne
