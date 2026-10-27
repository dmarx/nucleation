# record/status-review/worklist.py
"""Derive the status-review worklist from the record's frontmatter (ADR-057).

Nothing here is kept by hand: every section is recomputed from the record, so
the worklist cannot fall behind it. Run from the repository root, on a freshly
fetched origin/main:

    python3 record/status-review/worklist.py            # every section, top 30
    python3 record/status-review/worklist.py --top 60
    python3 record/status-review/worklist.py --show CLAIM-027   # one cluster
"""
import re
from pathlib import Path

import fire
import yaml

SCHEMES = ["claims", "theory", "terms", "questions", "cases", "arguments"]
# dependent -> premise edges: what a document needs to be true, or to mean what it says
NEEDS = {"CLAIM": ["rests_on", "grounds", "uses"], "THEORY": ["presupposes"], "ARG": ["rests_on", "grounds"]}
RETIRED = {"Superseded", "Rejected"}
LIVE = {"Active", "Proposed"}


def as_list(x) -> list[str]:
    return [x] if isinstance(x, str) else [t for t in (x or []) if isinstance(t, str)]


def scheme(code: str) -> str:
    return code.split("-")[0]


class Record:
    def __init__(self, docs: dict[str, dict]):
        self.docs = docs
        self.needed_by: dict[str, set[str]] = {}
        for code, fm in docs.items():
            for field in NEEDS.get(scheme(code), []):
                for target in as_list(fm.get(field)):
                    if target in docs:
                        self.needed_by.setdefault(target, set()).add(code)

    @classmethod
    def load(cls, root: Path) -> "Record":
        docs = {}
        for d in SCHEMES:
            for p in (root / f"{d}.d").glob("*-*.md"):
                m = re.match(r"---\n(.*?)\n---\n", p.read_text(), re.S)
                if m:
                    try:
                        fm = yaml.safe_load(m.group(1))
                    except yaml.YAMLError as e:
                        raise SystemExit(f"{p}: frontmatter does not parse: {e}")
                    if isinstance(fm, dict):
                        docs[p.stem] = fm
        return cls(docs)

    def status(self, code: str) -> str | None:
        s = self.docs.get(code, {}).get("status")
        return str(s).split()[0] if s else None

    def title(self, code: str) -> str:
        return str(self.docs.get(code, {}).get("title", "?"))

    def dependents(self, code: str) -> set[str]:
        seen, stack = set(), [code]
        while stack:
            for d in self.needed_by.get(stack.pop(), ()):
                if d not in seen:
                    seen.add(d)
                    stack.append(d)
        return seen

    def premises(self, code: str) -> list[str]:
        fm = self.docs[code]
        return [t for f in NEEDS.get(scheme(code), []) for t in as_list(fm.get(f)) if t in self.docs]

    def live_objections(self, code: str) -> list[str]:
        fm = self.docs[code]
        return [t for f in ("objected_by", "countered_by") for t in as_list(fm.get(f)) if self.status(t) in LIVE]

    def load_bearing(self) -> list[dict]:
        """Proposed CLAIMs, THEORYs and TERMs that something needs, most-needed first."""
        rows = []
        for code in self.docs:
            if scheme(code) not in ("CLAIM", "THEORY", "TERM") or self.status(code) != "Proposed":
                continue
            reach = self.dependents(code)
            if reach:
                rows.append({"code": code, "reach": len(reach), "direct": len(self.needed_by[code]),
                             "warrant": self.docs[code].get("warrant"),
                             "open_premises": [t for t in self.premises(code)
                                               if scheme(t) != "LIT" and self.status(t) != "Active"],
                             "live_objections": self.live_objections(code)})
        return sorted(rows, key=lambda r: (-r["reach"], -r["direct"], r["code"]))

    def inversions(self) -> list[tuple]:
        """Active CLAIMs and ARGs that rest on, or are grounded in, something the record does not hold."""
        return [(c, f, t, self.status(t))
                for c, fm in sorted(self.docs.items()) if scheme(c) in ("ARG", "CLAIM") and self.status(c) == "Active"
                for f in ("rests_on", "grounds") for t in as_list(fm.get(f))
                if t in self.docs and self.status(t) != "Active"]

    def retired_premises(self) -> list[tuple]:
        """Live entries that need something retired, with its named successor."""
        return [(c, f, t, self.status(t), self.live_successors(t))
                for c in sorted(self.docs) if self.status(c) in LIVE
                for f in NEEDS.get(scheme(c), []) for t in as_list(self.docs[c].get(f))
                if self.status(t) in RETIRED]

    def live_successors(self, code: str) -> list[str]:
        """Follow `superseded_by` until it reaches entries that are not retired."""
        out, stack, seen = [], as_list(self.docs.get(code, {}).get("superseded_by")), {code}
        while stack:
            s = stack.pop(0)
            if s in seen:
                continue
            seen.add(s)
            if self.status(s) in RETIRED:
                stack += as_list(self.docs.get(s, {}).get("superseded_by"))
            else:
                out.append(s)
        return out

    def open_with_active_answer(self) -> list[tuple]:
        return [(q, a) for q, fm in sorted(self.docs.items())
                if scheme(q) == "QUESTION" and self.status(q) == "Open"
                for a in [[t for t in as_list(fm.get("answered_by")) if self.status(t) == "Active"]] if a]

    def unblocked(self) -> list[str]:
        """Proposed CLAIMs whose premises are all Active and that no live objection stands against."""
        return [c for c in sorted(self.docs) if scheme(c) == "CLAIM" and self.status(c) == "Proposed"
                and all(scheme(t) == "LIT" or self.status(t) == "Active" for t in self.premises(c))
                and not self.live_objections(c)]


def short(r: Record, code: str, n: int = 90) -> str:
    t = r.title(code)
    return f"{code} [{r.status(code)}] {t[:n]}{'…' if len(t) > n else ''}"


def main(root: str = "record", top: int = 30, show: str | None = None):
    r = Record.load(Path(root))
    if show:
        fm = r.docs[show]
        print(short(r, show, 200), f"| {fm.get('role')} {fm.get('warrant')}")
        print("defeated_if:", fm.get("defeated_if"))
        for f in NEEDS.get(scheme(show), []) + ["objected_by", "countered_by", "objects_to", "answers"]:
            for t in as_list(fm.get(f)):
                print(f"  {f}: {short(r, t)}")
        for d in sorted(r.needed_by.get(show, ())):
            print(f"  needed by: {short(r, d)}")
        return
    print(f"## Load-bearing Proposed entries (top {top})\n")
    for x in r.load_bearing()[:top]:
        print(f"- {x['reach']:3d}/{x['direct']:<2d} {short(r, x['code'])}  "
              f"open premises: {x['open_premises'] or '-'}; live objections: {x['live_objections'] or '-'}")
    print("\n## Credence inversions: Active resting on what is not held\n")
    for row in r.inversions():
        print("- {} {} {} [{}]".format(*row))
    print("\n## Premises that are retired\n")
    for row in r.retired_premises():
        print("- {} {} {} [{}] -> {}".format(*row))
    print("\n## Open questions with an Active answer\n")
    for q, a in r.open_with_active_answer():
        print(f"- {short(r, q, 70)} <- {', '.join(a)}")
    ub = r.unblocked()
    print(f"\n## Unblocked Proposed CLAIMs ({len(ub)}): premises held, no live objection\n")
    for c in ub:
        print(f"- {short(r, c)}")


if __name__ == "__main__":
    fire.Fire(main)
