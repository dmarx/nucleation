"""scratch/formal/redesign_reserve_check.py

Checks the assistant's gap fill on the manuscript governance-of-possibility,
A48 section 9: under a budget set each period to the last period's peak use
(CLAIM-577's rule), is a redesigned transition kept without a reserve?

A transition's threshold is the least peak over its paths (CLAIM-571).
Holding configuration A uses r(A) = 1 per period. Run: python3 -I this file.
"""
PATHS = {"orig": [1, 3, 1], "staged": [1, 2, 1]}


def threshold(arch):
    return min(max(PATHS[p]) for p in arch)


def run(next_budget, arch, periods=5, b0=3):
    """Budget each period, and whether the transition is affordable."""
    b, out = b0, []
    for _ in range(periods):
        out.append((b, b >= threshold(arch)))
        b = next_budget(b)
    return out


def main():
    peak_rule = lambda b: 1             # a holding period's peak use is r(A) = 1
    reserve = lambda k: (lambda b: k)   # a budget held at k whatever the use
    cases = {
        "I   peak rule, original": run(peak_rule, {"orig"}),
        "II  reserve 3, original": run(reserve(3), {"orig"}),
        "III peak rule, redesigned": run(peak_rule, {"orig", "staged"}),
        "III reserve 2, redesigned": run(reserve(2), {"orig", "staged"}),
    }
    for name, out in cases.items():
        print(name, out)
    # The claim: under the peak rule a route is kept after a holding period
    # exactly when its threshold is at most r(A).
    for th in (1, 2, 3):
        PATHS["probe"] = [1, th, 1]
        kept = run(peak_rule, {"probe"})[1][1]
        assert kept == (th <= 1), th
    assert not cases["III peak rule, redesigned"][1][1]
    assert cases["III reserve 2, redesigned"][1][1]
    print("checks pass")


if __name__ == "__main__":
    main()
