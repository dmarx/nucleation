"""scratch/formal/response_kernel_bisimulation_check.py

Reconstructs and checks the construction of CLAIM-1095 (the filer's script
was not kept). Written at the status pass of 2026-11-24 by a session other
than the claim's filer, from the entry's text alone. Run: python3 -I this file.

Each state answers each query adequately with a stated probability and moves
deterministically to a next state. Three distances between states:
  answers only:  max over q of the total-variation distance of the adequacy
                 laws now;
  direct S':     the answers-only term plus the discrete metric on the next
                 state (1 if the next states differ), maximised over q;
  bisimulation:  the fixed point of d(S, T) = max_q [TV_q(S, T) + gamma *
                 d(next S, next T)] (deterministic moves, so the transport
                 term is d of the next states), as THEORY-247 holds it.
"""

GAMMA = 0.9
Q = ("q0", "q1")
P = {  # adequacy probability per query, and the next state
    "s": ({"q0": 0.9, "q1": 0.2}, "s1"), "s1": ({"q0": 0.9, "q1": 0.2}, "s1"),
    "t": ({"q0": 0.9, "q1": 0.2}, "t1"), "t1": ({"q0": 0.9, "q1": 0.2}, "t1"),
    "u": ({"q0": 0.9, "q1": 0.2}, "u1"), "u1": ({"q0": 0.9, "q1": 0.7}, "u1"),
    "v": ({"q0": 0.9, "q1": 0.2}, "v1"), "v1": ({"q0": 0.9, "q1": 0.1}, "v1"),
}


def tv(a, b):
    return abs(a - b)  # total variation between two Bernoulli laws


def answers_only(x, y):
    return max(tv(P[x][0][q], P[y][0][q]) for q in Q)


def direct(x, y):
    return max(tv(P[x][0][q], P[y][0][q]) + (P[x][1] != P[y][1]) for q in Q)


def bisimulation(tol=1e-12):
    states = list(P)
    d = {(x, y): 0.0 for x in states for y in states}
    while True:
        new = {(x, y): max(tv(P[x][0][q], P[y][0][q]) + GAMMA * d[(P[x][1], P[y][1])]
                           for q in Q) for x in states for y in states}
        if max(abs(new[k] - d[k]) for k in d) < tol:
            return new
        d = new


def main():
    b = bisimulation()
    rows = {pair: (answers_only(*pair), direct(*pair), b[pair])
            for pair in (("s", "t"), ("u", "v"))}
    for pair, r in rows.items():
        print(pair, "answers only %.3f  direct S' %.3f  bisimulation %.3f (scaled %.3f)"
              % (r[0], r[1], r[2], r[2] * (1 - GAMMA)))
    assert rows[("s", "t")] == (0, 1, 0)
    a, dct, bis = rows[("u", "v")]
    assert a == 0 and dct == 1 and abs(bis - 5.4) < 1e-9
    # control: the metric is a pseudometric that is zero on a state with itself
    assert all(b[(x, x)] == 0 for x in P)
    # control: it separates the learned and suppressed successors directly
    assert abs(b[("u1", "v1")] - 6.0) < 1e-9
    print("checks pass")


if __name__ == "__main__":
    main()
