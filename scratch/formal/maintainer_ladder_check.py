# scratch/formal/maintainer_ladder_check.py: a ladder of outside maintainers for the mutual-maintenance model
# c' = -c + 4 r c (1 - c), r' = -r + 4 c (1 - r) (CASE-tmp3ioyf). The capacity r is supplied from outside by
# (a) a constant controller r = r+, (b) a controller running the same production law on a delayed reading of c,
# r' = -r + 4 c(t - tau)(1 - r), and (c) the same law on c(t) itself (CLAIM-522's state feedback). The check shows
# how far an intervention on state alone separates each from internal production: (a) by a gross perturbation,
# (b) by a brief pulse, with a separation that shrinks to zero with tau, (c) by none, until the mechanism is cut.
# Filed with the assistant's ladder claim (2026-11-15). Run: python3 -I scratch/formal/maintainer_ladder_check.py
import math

DT = 1e-3
C_HI = (3 + math.sqrt(5)) / 8
R_HI = 4 * C_HI / (1 + 4 * C_HI)


def run(controller, tau=0.0, pulse=None, start=(C_HI, R_HI), t1=20.0, cut_internal=False):
    """Euler-integrate; controller in {'internal', 'constant', 'delayed'}; pulse = (t0, width, size) kicks c down."""
    c, r = start
    hist = []
    lag = int(round(tau / DT))
    out = []
    t = 0.0
    while t < t1:
        hist.append(c)
        c_seen = hist[-1 - lag] if len(hist) > lag else start[0]
        if controller == "constant":
            dr = 0.0
            r = R_HI
        elif controller == "internal":
            dr = -r + (0.0 if cut_internal else 4 * c * (1 - r))
        else:  # 'delayed' (tau = 0 is CLAIM-522's exact state feedback)
            dr = -r + 4 * c_seen * (1 - r)
        dc = -c + 4 * r * c * (1 - c)
        if pulse and pulse[0] <= t < pulse[0] + pulse[1]:
            dc -= pulse[2]
        c += DT * dc
        if controller != "constant":
            r += DT * dr
        out.append((c, r))
        t += DT
    return out


def gap(a, b):
    return max(abs(x[0] - y[0]) + abs(x[1] - y[1]) for x, y in zip(a, b))


pulse = (2.0, 0.2, 2.0)  # a brief knock to c
internal = run("internal", pulse=pulse)

# (a) a constant controller is separated by the pulse already (and grossly by starting from c = 0.01, CASE-tmp3ioyf).
g_const = gap(internal, run("constant", pulse=pulse))
assert g_const > 0.05, g_const

# (b) a delayed copy of the law is separated by the pulse, by an amount that shrinks as the delay shrinks.
gaps = [(tau, gap(internal, run("delayed", tau=tau, pulse=pulse))) for tau in (1.0, 0.3, 0.1, 0.03)]
for (t1, g1), (t2, g2) in zip(gaps, gaps[1:]):
    assert g2 < g1, gaps
assert gaps[0][1] > 0.01 and gaps[-1][1] < gaps[0][1] / 5

# (c) the exact law as state feedback is not separated by any state intervention tried: the pulse, or other starts.
for p in (pulse, (1.0, 0.5, 1.0), None):
    for s in ((C_HI, R_HI), (0.3, 0.2), (0.12, 0.3)):
        assert gap(run("internal", pulse=p, start=s), run("delayed", tau=0.0, pulse=p, start=s)) < 1e-9
# ... but cutting the internal production pathway separates it at once.
assert gap(run("internal", cut_internal=True), run("delayed", tau=0.0)) > 0.3

for tau, g in gaps:
    print(f"delay {tau:>5}: max separation under the pulse {g:.4f}")
print(f"constant controller: {g_const:.4f}; exact feedback: 0 under every state intervention tried")
print("maintainer ladder check: all passed")
