"""LEAD-121: share-dependent advantage with interpretation-independent scoring.

CASE-155 part 4's two-process walk, with a separate interpretation field m
added that authority shapes (b, CASE-099's beta) and that the authority
score never reads (gamma = 0, CASE-099's Regime B):

    l_{t+1} = l_t + h + c (2 pi_t - 1),    pi = sigmoid(l)
    m_{t+1} = (1 - rho) m_t + rho (e + b (2 pi_t - 1))

h  : per-step log likelihood ratio of evidence scored independently (h < 0 favours B)
c  : share-dependent advantage (the score rises with the incumbent's own share)
e  : independent evidence about the interpretation (e < 0 favours B)
b  : authority's effect on interpretation
"""
import math


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def run(pi0, h=-0.2, c=1.0, e=-0.5, b=1.0, rho=0.2, steps=2000, clip=40.0):
    l = math.log(pi0 / (1.0 - pi0))
    m = 0.0
    for _ in range(steps):
        pi = sigmoid(l)
        l = max(-clip, min(clip, l + h + c * (2.0 * pi - 1.0)))
        m = (1.0 - rho) * m + rho * (e + b * (2.0 * pi - 1.0))
    return sigmoid(l), m


def threshold(h, c):
    return (1.0 - h / c) / 2.0


if __name__ == "__main__":
    print("pi* =", threshold(-0.2, 1.0))
    for c in (1.0, 0.0):
        for pi0 in (0.55, 0.59, 0.61, 0.65, 0.9):
            pi, m = run(pi0, c=c)
            print(f"c={c} pi0={pi0}: pi_final={pi:.4f} m_final={m:+.4f}")
