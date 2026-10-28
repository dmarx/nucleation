# scratch/formal/trust_loop.py: the construction behind CLAIM-277's two loops
"""Durable authority from endorsement alone, and entrenchment from the same loop.

Run: python3 scratch/formal/trust_loop.py

Operators share one update rule and differ only in accuracy and history. Each
round one operator acts, chosen with probability softmax(beta * E). Every
operator's endorsement E_i moves toward its observed outcomes,
E_i <- E_i + eta * (outcome - E_i). Nothing marks any operator as an
authority. Two regimes differ in what is observed:

- scored: every operator's prediction is scored every round, so the
  track record does not depend on who acted;
- exposure: only the operator that acted is scored, so influence buys the
  chance to show competence.
"""
import numpy as np


def run(p, eta, beta, T, scored, E0, rng):
    E = np.array(E0, float)
    top = np.empty(T, int)
    for t in range(T):
        w = np.exp(beta * (E - E.max()))
        actor = rng.choice(len(p), p=w / w.sum())
        right = rng.random(len(p)) < p
        if scored:
            E += eta * (right - E)
        else:
            E[actor] += eta * (right[actor] - E[actor])
        top[t] = actor
    return E, top


def main(seeds: int = 200, T: int = 4000):
    p = np.array([0.8, 0.6])          # operator 0 is right more often
    rng = np.random.default_rng(0)

    print("1. Scored, fair start (E0 = 0.5, 0.5), eta = 0.01, beta = 8:")
    share, ahead = [], 0
    for _ in range(seeds):
        E, top = run(p, 0.01, 8, T, True, [0.5, 0.5], rng)
        share.append((top[T // 2:] == 0).mean())
        ahead += E[0] > E[1]
    print(f"   late share of rounds acted by the better operator: {np.mean(share):.3f}")
    print(f"   seeds ending with the better operator more endorsed: {ahead}/{seeds}")

    print("2. Same, with an early advantage for the worse operator (E0 = 0.3, 0.9):")
    share = []
    for _ in range(seeds):
        E, top = run(p, 0.01, 8, T, True, [0.3, 0.9], rng)
        share.append((top[T // 2:] == 0).mean())
    print(f"   late share acted by the better operator: {np.mean(share):.3f}  (scoring undoes the head start)")

    print("3. Exposure, early advantage for the worse operator (E0 = 0.3, 0.9), eta = 0.01:")
    print("   beta = sharpness of selection; recovery = first round the better operator acts in most of")
    print("   the next 200 rounds, or never within T")
    for beta in (8, 30, 100):
        never, rec = 0, []
        for _ in range(seeds):
            E, top = run(p, 0.01, beta, T, False, [0.3, 0.9], rng)
            good = np.convolve((top == 0).astype(float), np.ones(200) / 200, "valid") > 0.5
            if good.any():
                rec.append(int(np.argmax(good)))
            else:
                never += 1
        med = f"{int(np.median(rec))}" if rec else "-"
        print(f"   beta = {beta:>3}: never recovers in {never}/{seeds} seeds; median recovery round {med}")

    print("4. Exposure, fair start (E0 = 0.5, 0.5), beta = 100:")
    locked = 0
    for _ in range(seeds):
        E, top = run(p, 0.01, 100, T, False, [0.5, 0.5], rng)
        locked += (top[T // 2:] == 0).mean() < 0.5
    print(f"   seeds in which the worse operator acts in most late rounds: {locked}/{seeds}")
    print("   control, scored regime, same beta and early advantage:")
    locked = 0
    for _ in range(seeds):
        E, top = run(p, 0.01, 100, T, True, [0.3, 0.9], rng)
        locked += (top[T // 2:] == 0).mean() < 0.5
    print(f"   seeds in which the worse operator acts in most late rounds: {locked}/{seeds}")

    print("5. Durability under scoring, fair start: how often the lead in endorsement changes hands")
    print("   in the late half, slow (eta = 0.01) against fast (eta = 0.3) memory:")
    for eta in (0.01, 0.3):
        changes = []
        for _ in range(seeds):
            E = np.array([0.5, 0.5])
            lead = []
            for t in range(T):
                right = rng.random(2) < p
                E += eta * (right - E)
                lead.append(E[0] > E[1])
            lead = np.array(lead[T // 2:])
            changes.append(np.mean(np.diff(lead.astype(int)) != 0))
        print(f"   eta = {eta}: lead changes per round in the late half = {np.mean(changes):.4f}")


if __name__ == "__main__":
    main()
