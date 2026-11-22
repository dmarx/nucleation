"""Tables for LEAD-048 from results/core*.jsonl -> results/tables.md.

    python3 -I analyze.py
"""
import glob, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
MAINT = ("reciprocal", "external", "none")
LES = ("sham", "generate", "admit", "score", "A_partial", "G_partial",
       "producer_interrupt", "internal_producer", "double")


def load():
    rows = {}
    for p in sorted(glob.glob(os.path.join(HERE, "results", "core*.jsonl"))):
        with open(p) as fh:
            for line in fh:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                rows[(d["maintenance"], d["admission"], d["scoring"], d["env2"],
                      d["lesion"], d["matched"], d["self_check"], d["fuel"])] = d
    return rows


def g(rows, *k):
    return rows.get(k)


def cell(d, f):
    return "·" if d is None else f(d)


def lesion_table(rows, adm, sc, selfc, fuel, out):
    out.append(f"\n### admission {adm}, scoring {sc}, self-check "
               f"{'on' if selfc else 'off'}, fuel {fuel}\n")
    out.append("Natural branch: S1∧S2 / 64 (S2|S1 in brackets); matched "
               "branch: S2 / 64.\n")
    hdr = "| injury | " + " | ".join(
        f"{m[:5]} in nat | {m[:5]} in mat | {m[:5]} out nat | {m[:5]} out mat"
        for m in MAINT) + " |"
    out.append(hdr)
    out.append("|" + "---|" * (1 + 4 * len(MAINT)))
    for L in LES:
        cells = []
        for m in MAINT:
            for e in ("in_family", "out_family"):
                n = g(rows, m, adm, sc, e, L, False, selfc, fuel)
                t = g(rows, m, adm, sc, e, L, True, selfc, fuel)
                cells.append(cell(n, lambda d: f"{d['S1andS2']} [{d['S1andS2']}/{d['S1']}]"
                                  if d["S1"] else f"{d['S1andS2']} [S1=0]"))
                cells.append(cell(t, lambda d: str(d["S2"])))
        out.append(f"| {L} | " + " | ".join(cells) + " |")


def capture_table(rows, out):
    out.append("\n### admission × scoring, sham injury, self-check on, ample fuel\n")
    out.append("S1 / 64; S1∧S2 / 64; matched-branch S2 / 64 (in-family, out-of-family).\n")
    out.append("| maintenance | admission | scoring | S1 | S1∧S2 in | S1∧S2 out | matched S2 in | matched S2 out |")
    out.append("|---|---|---|---|---|---|---|---|")
    for m in MAINT:
        for a in ("protected", "selective"):
            for s in ("independent", "captured", "ipw"):
                ni = g(rows, m, a, s, "in_family", "sham", False, True, "ample")
                no = g(rows, m, a, s, "out_family", "sham", False, True, "ample")
                mi = g(rows, m, a, s, "in_family", "sham", True, True, "ample")
                mo = g(rows, m, a, s, "out_family", "sham", True, True, "ample")
                out.append(f"| {m} | {a} | {s} | {cell(ni, lambda d: d['S1'])} | "
                           f"{cell(ni, lambda d: d['S1andS2'])} | {cell(no, lambda d: d['S1andS2'])} | "
                           f"{cell(mi, lambda d: d['S2'])} | {cell(mo, lambda d: d['S2'])} |")


def flag_table(rows, out):
    out.append("\n### Self-flagging of a damaged apparatus (matched branch, in-family, ample fuel)\n")
    out.append("Flagged its own apparatus before acting on its output / 64; median delay in steps.\n")
    out.append("| maintenance | admission | scoring | generate | admit | score |")
    out.append("|---|---|---|---|---|---|")
    for m in MAINT:
        for a in ("protected", "selective"):
            for s in ("independent", "captured", "ipw"):
                cs = []
                for L in ("generate", "admit", "score"):
                    d = g(rows, m, a, s, "in_family", L, True, True, "ample")
                    cs.append(cell(d, lambda d: f"{d['flag_before_act']} ({d['flag_delay_med']})"))
                out.append(f"| {m} | {a} | {s} | " + " | ".join(cs) + " |")


def secondary(rows, out):
    out.append("\n### Secondary, reference apparatus, matched branch, in-family, self-check on\n")
    out.append("| maintenance | injury | fuel | S2 | correct | viable | budget | detected | delay | final A | final G | fuel spent | production fuel |")
    out.append("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for m in MAINT:
        for L in LES:
            for f in ("ample", "tight"):
                d = g(rows, m, "protected", "independent", "in_family", L, True, True, f)
                if d is None:
                    continue
                out.append(f"| {m} | {L} | {f} | {d['S2']} | {d['S2_correct']} | {d['S2_viable']} | "
                           f"{d['S2_budget']} | {d['detected']} | {d['delay_med']} | {d['final_A_mean']} | "
                           f"{d['final_G_mean']} | {d['fuel_spent_mean']} | {d['prod_fuel_mean']} |")


def main():
    rows = load()
    out = [f"# LEAD-048 tables\n\n{len(rows)} cells of 64 seeds.\n",
           "## Reference apparatus by injury"]
    for selfc in (True, False):
        for fuel in ("ample", "lean", "tight"):
            lesion_table(rows, "protected", "independent", selfc, fuel, out)
    out.append("\n## Capture arms")
    capture_table(rows, out)
    flag_table(rows, out)
    secondary(rows, out)
    path = os.path.join(HERE, "results", "tables.md")
    with open(path, "w") as fh:
        fh.write("\n".join(out) + "\n")
    print(path)


if __name__ == "__main__":
    main()
