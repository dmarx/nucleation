"""The lower rungs of LEAD-177's ladder, in the owner's alarm world.

One chain, as in CASE-242: an injector, a sensor, a relay and an actuator.
Fires come and go; the ambient is hot in daytime blocks; two further
ambient features (humid, weekend) are irrelevant.  Every rung reads the
SAME passive sensor channel (identical sensory correlations, measured as
I(reading; smoke)); the rungs differ only in what they keep, how long, and
what the kept state does.

  R0 relay      CASE-238: the sensor's all-clear current holds the valve
                shut; the valve opens whenever the current stops.  Nothing
                is kept.
  R1 tester     CASE-240: a normal (not fail-safe) chain; every P steps, at
                night, it injects test smoke, waits W steps for the expected
                response, retests once on silence, and on a second silence keeps a fault flag and switches to a
                healthy backup chain.  Kept: an interval, an expectation, a
                flag.
  R2 diagnoser  CASE-242: R1, and on a registered fault it runs four probes
                (injector, relay bypass, actuator command, independent
                smoke), matches the signature to its catalog by likelihood,
                and replaces the component it names.  Kept: a catalog.
  R3 reviser    R2, and it keeps a record of real fires (put out or not) with
                the ambient features; when failures concentrate on a feature
                value (Fisher exact, p < 0.01, at least 3 failures) it adds a
                test run under that condition.  Kept: a history; revised: its
                probe schedule.  The candidate conditions are the features it
                senses; it cannot invent a new one (A10's caveat in CASE-242).

Faults (one per episode, from t_fault): none, sensor, relay, actuator,
injector, heat-relay (the relay fails only while hot).  Readout error on
every probe: 2 %.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.stats import fisher_exact

FAULTS = ["none", "sensor", "relay", "actuator", "injector", "heat-relay"]
RUNGS = ["R0-relay", "R1-tester", "R2-diagnoser", "R3-reviser"]
COMPONENTS = ["injector", "sensor", "relay", "actuator"]
EPS = 0.02

# CASE-242's table: response under (injector, relay bypass, actuator command,
# independent smoke) for each single-fault state.
CATALOG = {
    "healthy": (1, 1, 1, 1),
    "sensor": (0, 1, 1, 0),
    "relay": (0, 0, 1, 0),
    "actuator": (0, 0, 0, 0),
    "injector": (0, 1, 1, 1),
}


def probe_truth(ok: dict) -> tuple:
    """Noise-free response of the chain under the four probes, given which
    components work at this moment."""
    inj = ok["injector"] and ok["sensor"] and ok["relay"] and ok["actuator"]
    bypass = ok["relay"] and ok["actuator"]           # enters at the relay
    command = ok["actuator"]
    indep = ok["sensor"] and ok["relay"] and ok["actuator"]
    return (int(inj), int(bypass), int(command), int(indep))


def posterior(obs: tuple, eps: float = EPS) -> dict:
    """Posterior over CATALOG states under a uniform prior, readout error eps."""
    like = {}
    for s, sig in CATALOG.items():
        k = sum(o != g for o, g in zip(obs, sig))
        like[s] = (eps ** k) * ((1 - eps) ** (len(obs) - k))
    z = sum(like.values())
    return {s: v / z for s, v in like.items()}


def mutual_information(a: np.ndarray, b: np.ndarray) -> float:
    """Plug-in mutual information (bits) between two binary arrays."""
    mi = 0.0
    for u in (0, 1):
        for v in (0, 1):
            p = np.mean((a == u) & (b == v))
            if p > 0:
                mi += p * math.log2(p / (np.mean(a == u) * np.mean(b == v)))
    return mi


class Env:
    def __init__(self, seed: int, T: int = 6000, t_fault: int = 500,
                 p_fire: float = 0.004):
        rng = np.random.default_rng(seed)
        self.T, self.t_fault = T, t_fault
        t = np.arange(T)
        self.hot = ((t % 100) >= 40) & ((t % 100) < 80)          # daytime block
        self.night = (t % 100) >= 90
        self.humid = rng.random(T) < 0.5
        self.weekend = ((t // 100) % 7) >= 5
        self.fire_start = rng.random(T) < p_fire
        # readout flips: col 0 the test, col 1 its retest, cols 2-5 the probes
        self.readout = rng.random((T, 6)) < EPS
        self.sensor_noise = rng.random(T) < EPS                  # passive flips
        smoke = np.zeros(T, bool)
        for s in np.flatnonzero(self.fire_start):
            smoke[s:s + 5] = True
        self.smoke = smoke
        self.rng = rng


def run(rung: str, fault: str, seed: int, P: int = 100, W: int = 3) -> dict:
    env = Env(seed)
    T = env.T
    broken = {c: False for c in COMPONENTS}
    replaced = set()
    on_backup = False
    flag = None                     # time a fault was registered
    registrations = []
    locs = []                       # (t, state named by the probes)
    heat_probe = False              # R3's added probe condition
    heat_probe_t = None
    added_condition = []
    fires = []                      # (start, hot, humid, weekend, put_out)
    valve_open_no_fire = 0
    reading = np.zeros(T, bool)

    def ok_now(t):
        o = {c: not broken[c] or c in replaced for c in COMPONENTS}
        if fault == "heat-relay" and t >= env.t_fault and env.hot[t] and "relay" not in replaced:
            o["relay"] = False
        return o

    def run_probes(t):
        truth = probe_truth(ok_now(t))
        obs = tuple(int(v) ^ int(f) for v, f in zip(truth, env.readout[t, 2:]))
        post = posterior(obs)
        return max(post, key=post.get)

    for t in range(T):
        if t == env.t_fault and fault in COMPONENTS:
            broken[fault] = True
        ok = ok_now(t)
        # the passive channel every rung reads
        reading[t] = (env.smoke[t] and ok["sensor"]) ^ env.sensor_noise[t]
        # --- what the reading does
        if rung == "R0-relay":
            current = ok["sensor"] and not reading[t]      # all-clear current
            valve_open = (not current) or (not ok["relay"])  # spring opens
            valve_open = valve_open and ok["actuator"]
            put_out = valve_open
        else:
            chain_ok = ok["sensor"] and ok["relay"] and ok["actuator"]
            if on_backup:
                chain_ok = True
            put_out = env.smoke[t] and chain_ok
            valve_open = put_out
        if valve_open and not env.smoke[t]:
            valve_open_no_fire += 1
        if env.fire_start[t]:
            fires.append([t, bool(env.hot[t]), bool(env.humid[t]), bool(env.weekend[t]), False])
        if env.smoke[t] and put_out and fires:
            fires[-1][4] = True
        if rung == "R0-relay":
            continue
        # --- R1: scheduled test at night: expectation, interval, flag
        scheduled = (t % P == 95)
        heat_test = heat_probe and env.hot[t] and (t % P == 60)
        if (scheduled or heat_test) and not on_backup:
            o = ok_now(t)
            truth = o["injector"] and o["sensor"] and o["relay"] and o["actuator"]
            responded = bool(truth) ^ bool(env.readout[t, 0])
            if not responded:   # silence: retest once before registering
                responded = bool(truth) ^ bool(env.readout[t, 1])
            if not responded:
                registrations.append(t)
                if flag is None:
                    flag = t
                if rung == "R1-tester":
                    on_backup = True
                else:
                    name = run_probes(t)
                    locs.append((t, name))
                    if name != "healthy":
                        replaced.add(name)
        # --- R3: review of real fires, revising the probe schedule
        if rung == "R3-reviser" and not added_condition and t % 50 == 0 and len(fires) >= 4:
            done = [f for f in fires if f[0] + 5 <= t]
            fails = [f for f in done if not f[4]]
            if len(fails) >= 3:
                for j, name in ((1, "hot"), (2, "humid"), (3, "weekend")):
                    a = sum(f[j] for f in fails)
                    b = len(fails) - a
                    c = sum(f[j] for f in done if f[4])
                    d = sum(1 for f in done if f[4]) - c
                    p = fisher_exact([[a, b], [c, d]])[1]
                    if p < 0.01 and a > b:
                        heat_probe, heat_probe_t = name == "hot", t
                        added_condition.append(name)
                        break
    post = [f for f in fires if f[0] >= env.t_fault and f[0] + 5 <= T]
    return dict(
        rung=rung, fault=fault, seed=seed,
        mi_pre=mutual_information(env.smoke[:env.t_fault], reading[:env.t_fault]),
        mi_post=mutual_information(env.smoke[env.t_fault:], reading[env.t_fault:]),
        fires_after=len(post),
        put_out_after=sum(f[4] for f in post),
        hot_fires_after=sum(f[1] for f in post),
        hot_put_out=sum(f[4] for f in post if f[1]),
        valve_open_no_fire=valve_open_no_fire,
        registrations=len(registrations),
        located=[n for _, n in locs if n != "healthy"],
        located_t=next((tt - env.t_fault for tt, n in locs if n != "healthy"), None),
        backup=on_backup, flag_t=None if flag is None else flag - env.t_fault,
        added_condition=added_condition,
        heat_probe_t=None if heat_probe_t is None else heat_probe_t - env.t_fault,
    )
