"""CASE-186 organization: maintained inquiry under damage (LEAD-048).

A reusable, event-light simulation. One call to `run(cfg, seed)` simulates
one organization in one world and returns a dict of endpoints. LEAD-140 can
import `Config`, `World`, `Org` and `run`, or subclass `Org` to change a
mechanism, without touching the driver.

World. Hidden regime H in {+1, -1, 0}; P(Y=1 | a=1) is 0.75, 0.25, 0.5.
Partial monitoring: ordinary operation yields no informative feedback;
only audits (which set a=1 and sample Y) inform.

Apparatus. Three separately lesionable operations:
  generate  - draws n = round(N_AUDIT * A) samples (A = diagnostic
              integrity). Lesion: stale replay of the last pre-lesion batch.
  admit     - protected (all admitted) or selective (agreeing 0.9,
              contradicting 0.1). Protection is maintained work: it holds
              only while G >= G_MIN, else admission falls back to
              selective. Lesion: agreeing 0.95, contradicting 0.05.
  score     - independent (admitted mean, rule mean > 1/2; adequacy flag
              0.42 < mean < 0.58) or captured (mean shifted by KAPPA
              toward the current interpretation). 'ipw' is the
              selection-aware baseline (inverse-propensity weights).
              Lesion: an extra KAPPA_LESION shift toward the interpretation.

Self-check. Every SELF_CHECK_EVERY steps, with probability A, the apparatus
tests each operation on known inputs against its commissioning values
(reference coin p=0.75 for generate; a fixed balanced batch for admit and
score). A deviating operation is flagged; outputs of a flagged apparatus are
not acted on; a flagged operation is rebuilt after REPAIR_STEPS if the
maintenance arrangement can rebuild (see `can_rebuild`).

Maintenance of A (diagnostic) and G (evidence governance, which also
carries the teacher-to-student copier's fidelity):
  reciprocal - dA = R*G*(1-A) - WEAR*A ; dG = R*A*(1-G) - WEAR*G
  external   - dA = R*(1-A) - WEAR*A, likewise G, by an outside service
  none       - dA = -WEAR*A, likewise G
Production of either kind is paid from the same fuel at COST_PROD per unit.

Fuel. Stock F, +RHO per step. Priority: operation, maintenance, copying,
diagnosis (audit, then self-check). A shortfall skips the lower items.

Teacher and student. The teacher's interpretation updates from scored
admitted evidence. The acting student is erased every ERASE_EVERY steps and
reconstructed through the copier, which succeeds with probability G; on
failure it acts on the habit (+1) until the next reconstruction.

Schedule (steps): + until T1, - from T1. S1 judged at T1 + W1. Injury
(the lesion branch) at T_INJ. Second change at T2 to +1 (in-family) or 0
(out of family). S2 judged at T2 + W2 (= end).
"""
from __future__ import annotations

import zlib
from dataclasses import dataclass, field
import numpy as np

P1 = {1: 0.75, -1: 0.25, 0: 0.5}

LESIONS = ("sham", "generate", "admit", "score", "A_partial", "G_partial",
           "producer_interrupt", "internal_producer", "double")
COMPONENT_LESIONS = ("generate", "admit", "score")


@dataclass(frozen=True)
class Config:
    maintenance: str = "reciprocal"     # reciprocal | external | none
    admission: str = "protected"        # protected | selective
    scoring: str = "independent"        # independent | captured | ipw
    env2: str = "in_family"             # in_family (-> +) | out_family (-> 0)
    lesion: str = "sham"
    matched: bool = False               # start at a matched corrected state
    self_check: bool = True
    audits: bool = True                 # False: no-audit (habit) baseline
    # schedule
    T1: int = 100
    W1: int = 150
    T_INJ: int = 300
    T2: int = 400
    W2: int = 300
    # apparatus
    N_AUDIT: int = 256
    AUDIT_EVERY: int = 10
    A_MIN: float = 0.2
    G_MIN: float = 0.4
    KAPPA: float = 0.4
    KAPPA_LESION: float = 0.45
    SEL_AGREE: float = 0.9
    SEL_CONTRA: float = 0.1
    LES_AGREE: float = 0.95
    LES_CONTRA: float = 0.05
    ADEQ_LO: float = 0.42
    ADEQ_HI: float = 0.58
    SELF_CHECK_EVERY: int = 20
    N_REF: int = 64
    REPAIR_STEPS: int = 30
    REBUILD_MIN: float = 0.5
    # maintenance
    R: float = 0.05
    WEAR: float = 0.001
    PARTIAL: float = 0.25               # A_partial / G_partial multiply by this
    INTERRUPT: int = 300                # producer outage length
    # copying
    ERASE_EVERY: int = 50
    # fuel
    F0: float = 50.0
    RHO: float = 0.6
    COST_OP: float = 0.1
    COST_PROD: float = 2.0
    COST_COPY: float = 0.5
    COST_SAMPLE: float = 2.0 / 256
    COST_CHECK: float = 1.0
    # viability
    A_VIABLE: float = 0.3
    G_VIABLE: float = 0.4

    @property
    def end(self) -> int:
        return self.T2 + self.W2

    def key(self) -> str:
        return (f"{self.maintenance}|{self.admission}|{self.scoring}|{self.env2}"
                f"|{self.lesion}|{'M' if self.matched else 'N'}"
                f"|{'sc' if self.self_check else 'nosc'}"
                f"|{'aud' if self.audits else 'noaud'}|rho{self.RHO:g}")


class World:
    """Hidden regime path and the audit-sample stream.

    The stream is drawn from a generator seeded by (seed, purpose) so that
    arms sharing a seed see the same world (matched environmental streams).
    """

    def __init__(self, cfg: Config, seed: int):
        self.cfg = cfg
        self.seed = seed

    def regime(self, t: int) -> int:
        c = self.cfg
        if t < c.T1:
            return 1
        if t < c.T2:
            return -1
        return 1 if c.env2 == "in_family" else 0

    def sample(self, t: int, n: int) -> tuple[int, int]:
        """n audit draws with a=1; returns (ones, zeros).

        Draws are fixed per (seed, t): an arm drawing fewer samples sees a
        prefix of the same stream, so arms are matched draw for draw.
        """
        if n <= 0:
            return 0, 0
        u = np.random.default_rng([self.seed, 1, t]).random(self.cfg.N_AUDIT)
        k = int((u[:n] < P1[self.regime(t)]).sum())
        return k, n - k


@dataclass
class State:
    A: float = 1.0
    G: float = 1.0
    F: float = 50.0
    interp: int = 1                 # teacher: +1, -1, or 0 (family flagged)
    student: int = 1                # what the acting copy holds
    broken: dict = field(default_factory=dict)   # op -> True (lesioned)
    flagged: dict = field(default_factory=dict)  # op -> time flagged
    stale: tuple | None = None
    last_batch: tuple = (0, 0)
    prod_off_until: int = -1
    internal_prod_dead: bool = False


def admit_probs(cfg: Config, st: State, y: int) -> float:
    """P(admit) of an observation Y=y given the current interpretation."""
    if st.interp == 0:
        agree = None
    else:
        agree = (y == 1) == (st.interp == 1)
    if st.broken.get("admit"):
        if agree is None:
            return 1.0
        return cfg.LES_AGREE if agree else cfg.LES_CONTRA
    selective = cfg.admission == "selective" or st.G < cfg.G_MIN
    if not selective or agree is None:
        return 1.0
    return cfg.SEL_AGREE if agree else cfg.SEL_CONTRA


def score(cfg: Config, st: State, k1: int, k0: int, p1: float, p0: float) -> float | None:
    """Scored statistic in [0,1]-ish: estimated P(Y=1|a=1)."""
    if cfg.scoring == "ipw":
        w1, w0 = k1 / p1, k0 / p0
        tot = w1 + w0
        m = w1 / tot if tot > 0 else None
    else:
        tot = k1 + k0
        m = k1 / tot if tot > 0 else None
    if m is None:
        return None
    shift = 0.0
    if cfg.scoring == "captured":
        shift += cfg.KAPPA
    if st.broken.get("score"):
        shift += cfg.KAPPA_LESION
    return m + shift * st.interp


class Org:
    """The organization. Override methods to change a mechanism."""

    def __init__(self, cfg: Config, seed: int):
        self.cfg = cfg
        self.world = World(cfg, seed)
        self.rng = np.random.default_rng([seed, 2, zlib.crc32(cfg.key().encode())])
        self.st = State(F=cfg.F0)
        self.log = {"interp_changes": [], "flags": [], "fuel_short": 0,
                    "fuel_short_w2": 0, "regret_w2": 0, "regret_all": 0,
                    "audits": 0, "fuel_spent": 0.0, "prod_fuel": 0.0}
        self.first_update_after_lesion: int | None = None

    # -------------------------------------------------- fuel
    def pay(self, cost: float, t: int) -> bool:
        if self.st.F >= cost:
            self.st.F -= cost
            self.log["fuel_spent"] += cost
            return True
        self.log["fuel_short"] += 1
        if t >= self.cfg.T2:
            self.log["fuel_short_w2"] += 1
        return False

    # -------------------------------------------------- maintenance
    def producing(self, t: int) -> bool:
        c, st = self.cfg, self.st
        if c.maintenance == "none":
            return False
        if t < st.prod_off_until:
            return False
        if c.maintenance == "reciprocal" and st.internal_prod_dead:
            return False
        return True

    def maintain(self, t: int):
        c, st = self.cfg, self.st
        dA, dG = -c.WEAR * st.A, -c.WEAR * st.G
        pA = pG = 0.0
        if self.producing(t):
            if c.maintenance == "reciprocal":
                pA, pG = c.R * st.G * (1 - st.A), c.R * st.A * (1 - st.G)
            else:
                pA, pG = c.R * (1 - st.A), c.R * (1 - st.G)
            cost = c.COST_PROD * (pA + pG)
            if not self.pay(cost, t):
                pA = pG = 0.0
            else:
                self.log["prod_fuel"] += cost
        st.A = min(1.0, max(0.0, st.A + dA + pA))
        st.G = min(1.0, max(0.0, st.G + dG + pG))

    def can_rebuild(self, t: int) -> bool:
        c, st = self.cfg, self.st
        if not self.producing(t):
            return False
        if c.maintenance == "reciprocal":
            return st.A >= c.REBUILD_MIN and st.G >= c.REBUILD_MIN
        return True

    # -------------------------------------------------- apparatus
    def generate(self, t: int) -> tuple[int, int]:
        c, st = self.cfg, self.st
        n = int(round(c.N_AUDIT * st.A))
        if st.broken.get("generate"):
            return st.stale
        if not self.pay(c.COST_SAMPLE * n, t):
            return (0, 0)
        b = self.world.sample(t, n)
        st.last_batch = b
        return b

    def audit(self, t: int):
        c, st = self.cfg, self.st
        if not c.audits or st.A < c.A_MIN:
            return
        y1, y0 = self.generate(t)
        if y1 + y0 == 0:
            return
        self.log["audits"] += 1
        p1, p0 = admit_probs(c, st, 1), admit_probs(c, st, 0)
        k1 = int(self.rng.binomial(y1, p1))
        k0 = int(self.rng.binomial(y0, p0))
        m = score(c, st, k1, k0, p1, p0)
        if m is None or st.flagged:
            return  # a flagged apparatus's output is not acted on
        if c.ADEQ_LO < m < c.ADEQ_HI:
            new = 0
        else:
            new = 1 if m > 0.5 else -1
        if new != st.interp:
            st.interp = new
            self.log["interp_changes"].append((t, new))
            if t >= c.T_INJ and self.first_update_after_lesion is None:
                self.first_update_after_lesion = t

    def self_check(self, t: int):
        c, st = self.cfg, self.st
        if not c.self_check or st.A < c.A_MIN:
            return
        if self.rng.random() > st.A:
            return
        if not self.pay(c.COST_CHECK, t):
            return
        n = c.N_REF
        # generate: reference coin p=0.75; stale replay repeats the last batch
        if st.broken.get("generate") and "generate" not in st.flagged:
            # a fresh reference draw almost surely differs from the replay
            ref1 = int(self.rng.binomial(n, 0.75))
            s1, s0 = st.stale
            m_stale = s1 / max(1, s1 + s0)
            if abs(m_stale - 0.75) > 0.15 or ref1 != s1:
                st.flagged["generate"] = t
        # admit: n agreeing and n contradicting known tokens; commissioning
        # rate is the arm's design rate, a lesion lowers contradicting admits
        if "admit" not in st.flagged:
            design_c = 1.0 if c.admission == "protected" else c.SEL_CONTRA
            rate_c = c.LES_CONTRA if st.broken.get("admit") else design_c
            got = self.rng.binomial(n, rate_c) / n
            if design_c - got > 0.5 * design_c and design_c - got > 3 * np.sqrt(design_c * (1 - design_c) / n + 1e-9):
                st.flagged["admit"] = t
        # score: balanced batch scored as if under interp +1; commissioning
        # shift is KAPPA (captured) or 0; a lesion adds KAPPA_LESION
        if "score" not in st.flagged and st.broken.get("score"):
            st.flagged["score"] = t
        for op, tf in list(st.flagged.items()):
            if tf == t:
                self.log["flags"].append((t, op))

    def repair(self, t: int):
        st, c = self.st, self.cfg
        for op, tf in list(st.flagged.items()):
            if t - tf >= c.REPAIR_STEPS and self.can_rebuild(t):
                st.broken.pop(op, None)
                del st.flagged[op]
                if op == "generate":
                    st.stale = None

    # -------------------------------------------------- copying
    def copy(self, t: int):
        c, st = self.cfg, self.st
        if t % c.ERASE_EVERY == 0:
            st.student = 1  # erased: habit
            if self.pay(c.COST_COPY, t) and self.rng.random() < st.G:
                st.student = st.interp
        elif st.student != st.interp and self.rng.random() < 0.1:
            # opportunistic teacher correction between erasures
            if self.pay(c.COST_COPY, t) and self.rng.random() < st.G:
                st.student = st.interp

    # -------------------------------------------------- lesions
    def injure(self, t: int):
        c, st = self.cfg, self.st
        L = c.lesion
        if L in COMPONENT_LESIONS:
            st.broken[L] = True
            if L == "generate":
                st.stale = st.last_batch
        elif L == "A_partial":
            st.A *= c.PARTIAL
        elif L == "G_partial":
            st.G *= c.PARTIAL
        elif L == "double":
            st.A = st.G = 0.0
        elif L == "producer_interrupt":
            st.prod_off_until = t + c.INTERRUPT
        elif L == "internal_producer":
            st.internal_prod_dead = True

    def matched_state(self):
        """A matched, successfully corrected first-stage state."""
        st = self.st
        st.A = st.G = 1.0
        st.F = self.cfg.F0
        st.interp = st.student = -1
        st.broken, st.flagged = {}, {}
        # one fresh audit batch, so a stale replay has content
        st.last_batch = self.world.sample(self.cfg.T_INJ - 1,
                                          self.cfg.N_AUDIT)

    # -------------------------------------------------- loop
    def preferred(self, t: int) -> int:
        return self.world.regime(t)

    def step(self, t: int):
        c, st = self.cfg, self.st
        st.F += c.RHO
        self.pay(c.COST_OP, t)
        self.maintain(t)
        self.copy(t)
        if t % c.AUDIT_EVERY == 0:
            self.audit(t)
        if t % c.SELF_CHECK_EVERY == 0:
            self.self_check(t)
        self.repair(t)
        pref = self.preferred(t)
        if pref != 0 and st.student != pref:
            self.log["regret_all"] += 1
            if t >= c.T2:
                self.log["regret_w2"] += 1


def viable(cfg: Config, st: State) -> bool:
    return st.A >= cfg.A_VIABLE and st.G >= cfg.G_VIABLE and not st.broken


def run(cfg: Config, seed: int, org_cls=Org) -> dict:
    o = org_cls(cfg, seed)
    st, c = o.st, cfg
    out = {"key": cfg.key(), "seed": seed}
    t0 = 0
    if cfg.matched:
        # advance the world stream identically, then set the matched state
        t0 = c.T_INJ
        o.matched_state()
        out["S1"] = True
    for t in range(t0, c.end):
        if t == c.T_INJ:
            out["state_at_injury"] = [round(st.A, 3), round(st.G, 3),
                                      round(st.F, 2), st.interp]
            o.injure(t)
        o.step(t)
        if t == c.T1 + c.W1 - 1 and not cfg.matched:
            out["S1"] = bool(st.interp == -1 and st.student == -1
                             and viable(c, st))
        if t == c.T2 - 1:
            out["pre2_viable"] = viable(c, st)
            out["pre2_interp"] = st.interp
    target = 1 if c.env2 == "in_family" else 0
    det = [ti for ti, v in o.log["interp_changes"] if ti >= c.T2 and v == target]
    out["detect_delay"] = (det[0] - c.T2) if det else None
    ok_end = st.interp == target and st.student == target
    out["S2_correct"] = bool(ok_end)
    out["S2_budget"] = o.log["fuel_short_w2"] == 0
    out["S2_viable"] = viable(c, st)
    out["S2"] = bool(ok_end and det and out["S2_budget"] and out["S2_viable"])
    flags = o.log["flags"]
    out["flagged"] = sorted({op for _, op in flags})
    if c.lesion in COMPONENT_LESIONS:
        tf = min([ti for ti, op in flags if op == c.lesion], default=None)
        out["flag_delay"] = (tf - c.T_INJ) if tf is not None else None
        fu = o.first_update_after_lesion
        out["flag_before_act"] = bool(tf is not None and (fu is None or tf <= fu)
                                      and tf < c.T2)
    false_alarms = [ti for ti, v in o.log["interp_changes"]
                    if v != o.world.regime(ti)]
    out["false_changes"] = len(false_alarms)
    out["final"] = [round(st.A, 3), round(st.G, 3), round(st.F, 2), st.interp,
                    st.student]
    for k in ("regret_all", "regret_w2", "audits", "fuel_short", "fuel_short_w2"):
        out[k] = o.log[k]
    out["fuel_spent"] = round(o.log["fuel_spent"], 2)
    out["prod_fuel"] = round(o.log["prod_fuel"], 2)
    return out
