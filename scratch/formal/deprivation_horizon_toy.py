# scratch/formal/deprivation_horizon_toy.py: reproduces and asserts the numbers of the buffer-as-time toy filed with the
# owner's reading that deprivation adds time pressure to decisions. A household's savings w move +1 or -1 each period
# with equal chance; it is ruined (absorbing) if w falls below 0. It can pay k now for G > k received L periods later.
# Two objectives over a horizon T: survival S = P(not ruined by T), and expected wealth E at T with ruined paths at 0.
# Run: python3 -I scratch/formal/deprivation_horizon_toy.py
# The parameters are invented to show a mechanism; none is a measurement of any household.


def close(x, y, tol=5e-4):
    assert abs(x - y) <= tol, (x, y)


def run(w0, T, invest, k, G, L, stipend=0):
    """Return (S, E). With stipend m, shocks in the first m periods are covered (no loss), as a consumption stipend."""
    start = w0 - (k if invest else 0)
    if start < 0:
        return 0.0, 0.0
    dist = {start: 1.0}
    for t in range(1, T + 1):
        new = {}
        for w, p in dist.items():
            moves = (0, 1) if t <= stipend else (-1, 1)
            for dw in moves:
                nw = w + dw
                if nw < 0:
                    continue
                new[nw] = new.get(nw, 0.0) + p * 0.5
        dist = new
        if invest and t == L:
            dist = {w + G: p for w, p in dist.items()}
    return sum(dist.values()), sum(w * p for w, p in dist.items())


def thresholds(T, k, G, L, stipend=0, top=80):
    """Smallest starting buffer at which investing beats not investing, for survival and for expected wealth."""
    th_s = th_e = None
    for w0 in range(top):
        s0, e0 = run(w0, T, False, k, G, L)
        s1, e1 = run(w0, T, True, k, G, L, stipend if stipend else 0)
        if th_s is None and s1 > s0:
            th_s = w0
        if th_e is None and e1 > e0:
            th_e = w0
    return th_s, th_e


T, K, G = 40, 3, 6

# 1. The buffer needed before a profitable delayed investment is worth taking rises with the delay.
expected = {1: (4, 3), 4: (5, 4), 9: (6, 4), 16: (9, 5), 25: (14, 6)}
for L, (ts, te) in expected.items():
    assert thresholds(T, K, G, L) == (ts, te), (L, thresholds(T, K, G, L))

# 2. Survival, the objective deprivation makes binding, needs a deeper buffer than expected wealth does. At L = 16 and
#    w = 8, investing raises expected wealth (8.154 -> 10.304) and lowers survival (0.846 -> 0.835).
s0, e0 = run(8, T, False, K, G, 16)
s1, e1 = run(8, T, True, K, G, 16)
close(s0, 0.846)
close(s1, 0.835)
close(e0, 8.154)
close(e1, 10.304)

# 3. Below the threshold, declining is right by either objective: at w = 3, investing cuts survival from 0.467 to 0.188.
close(run(3, T, False, K, G, 16)[0], 0.467)
close(run(3, T, True, K, G, 16)[0], 0.188)

# 4. Covering shocks through the delay buys the time: with a stipend for the L periods before the payoff, the survival
#    threshold at L = 16 falls from 9 to 3 (only the outlay k must be affordable).
assert thresholds(T, K, G, 16, stipend=16)[0] == 3, thresholds(T, K, G, 16, stipend=16)

print("all deprivation-horizon toy numbers reproduce")
