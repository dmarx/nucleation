# record/status-review/worklist.py
"""Derive the status-review worklist from the record's frontmatter (ADR-057).

Nothing here is kept by hand: every section is recomputed from the record, so
the worklist cannot fall behind it. The sections that must be empty come first,
then the work in the order a pass takes it (ADR-057 v6): claims ready for a
ruling, grouped by line; the premises that alone hold claims back; blocker
notes a premise has outrun; and what is held or unread. Run from the
repository root, on a freshly fetched origin/main:

    python3 record/status-review/worklist.py            # every section, top 30
    python3 record/status-review/worklist.py --top 60
    python3 record/status-review/worklist.py --show CLAIM-027   # one cluster
"""
import re
from datetime import date, timedelta
from pathlib import Path

import fire
import yaml

SCHEMES = ["claims", "theory", "terms", "questions", "cases", "arguments", "notes", "literature"]
# dependent -> premise edges: what a document needs to be true, or to mean what it says
NEEDS = {"CLAIM": ["rests_on", "grounds", "uses"], "THEORY": ["presupposes"], "ARG": ["rests_on", "grounds"]}
RETIRED = {"Superseded", "Rejected"}
LIVE = {"Active", "Proposed"}
# A dated blocker note: "## Note of 2026-10-28: what holds it back". Within HELD_DAYS
# (luria.yaml's stale_days) the entry is listed as held, not as work (ADR-057).
BLOCKER = re.compile(r"^## Note of (\d{4}-\d{2}-\d{2}): what holds it back", re.M)
HELD_DAYS = 14
# A target filed with a concession already in its text says so, naming the objections:
# "## Note of 2026-10-29: filed with its concessions". A version bump would record a revision
# that never happened, and no rule over dates can tell such a target from an overstated one.
# A sentence that names an objection only to say it is open, filed or given its converse edge
# records the objection, not a revision for it (passes 18 and 19).
MENTION_ONLY = re.compile(r"\bis open\b|\bconverse\b|filed as the objection")
FILED_WITH = re.compile(r"^## Note of (\d{4}-\d{2}-\d{2}): filed with its concessions\n(.*?)(?=^## |\Z)", re.M | re.S)


def as_list(x) -> list[str]:
    return [x] if isinstance(x, str) else [t for t in (x or []) if isinstance(t, str)]


def scheme(code: str) -> str:
    return code.split("-")[0]


class Record:
    def __init__(self, docs: dict[str, dict], bodies: dict[str, str] | None = None):
        self.docs = docs
        self.bodies = bodies or {}
        self.needed_by: dict[str, set[str]] = {}
        # objections read from the objector's side too: not every `objects_to` has its converse
        self.objectors: dict[str, set[str]] = {}
        # work -> statuses of the NOTEs that read it
        self.read_as: dict[str, set[str]] = {}
        self.notes_on: dict[str, set[str]] = {}
        for code, fm in docs.items():
            if scheme(code) == "NOTE":
                for work in as_list(fm.get("paper")):
                    self.notes_on.setdefault(work, set()).add(code)
                    self.read_as.setdefault(work, set()).add(str(fm.get("status", "")).split()[0] if fm.get("status") else "")
            for target in as_list(fm.get("objects_to")):
                self.objectors.setdefault(target, set()).add(code)
            for field in NEEDS.get(scheme(code), []):
                for target in as_list(fm.get(field)):
                    if target in docs:
                        self.needed_by.setdefault(target, set()).add(code)

    @classmethod
    def load(cls, root: Path) -> "Record":
        docs, bodies = {}, {}
        for d in SCHEMES:
            for p in (root / f"{d}.d").glob("*-*.md"):
                text = p.read_text()
                m = re.match(r"---\n(.*?)\n---\n", text, re.S)
                if m:
                    try:
                        fm = yaml.safe_load(m.group(1))
                    except yaml.YAMLError as e:
                        raise SystemExit(f"{p}: frontmatter does not parse: {e}")
                    if isinstance(fm, dict):
                        docs[p.stem] = fm
                        bodies[p.stem] = text[m.end():]
        return cls(docs, bodies)

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
        """Objections that still stand: Proposed or Active ones whose concession is not written in.

        An objection answered by narrowing its target no longer stands against it (ADR-057).
        """
        fm = self.docs[code]
        named = [t for f in ("objected_by", "countered_by") for t in as_list(fm.get(f))]
        named += sorted(self.objectors.get(code, set()) - set(named))
        return [t for t in dict.fromkeys(named) if self.status(t) in LIVE and not self.written(t, code)]

    def sound(self, arg: str) -> bool:
        """An ARG whose inference is Active and every premise held."""
        return self.status(arg) == "Active" and all(
            scheme(t) == "LIT" or self.status(t) == "Active" for t in self.premises(arg))

    def open_premises(self, code: str) -> set[str]:
        """What the record does not hold that the entry needs.

        A claim with no premise of its own needs one of the ARGs that conclude it to be sound;
        if none is, it waits on what those ARGs wait on.
        """
        own = {t for t in self.premises(code) if scheme(t) != "LIT" and self.status(t) != "Active"}
        if self.premises(code):
            return own
        args = [a for a, fm in self.docs.items() if scheme(a) == "ARG" and code in as_list(fm.get("concludes"))]
        if not args or any(self.sound(a) for a in args):
            return own
        return {t for a in args for t in self.premises(a) + [a] if scheme(t) != "LIT" and self.status(t) != "Active"}

    def written(self, objection: str, target: str) -> bool:
        """Whether the target has been revised for the objection, or says it was filed with it.

        Either record must name the objection: a revision made for something else, after the
        objection was filed, does not write it in.
        """
        on = str(self.docs[objection].get("date", ""))
        revised = [str(h.get("date", "")) for h in self.docs[target].get("history") or []
                   if isinstance(h, dict) and any(objection in s and not MENTION_ONLY.search(s)
                                                  for s in re.split(r"(?<=\.)\s+", str(h.get("note", ""))))]
        filed = [d for d, text in FILED_WITH.findall(self.bodies.get(target, "")) if objection in text]
        return any(d >= on for d in revised + filed)

    def blocker_date(self, code: str) -> str | None:
        """The date of the entry's latest blocker note, however old."""
        return max(BLOCKER.findall(self.bodies.get(code, "")), default=None)

    def held_since(self, code: str, today: date) -> date | None:
        """The date of the entry's latest blocker note, if it is recent enough to stand."""
        dates = [date.fromisoformat(d) for d in BLOCKER.findall(self.bodies.get(code, ""))]
        latest = max(dates, default=None)
        return latest if latest and today - latest <= timedelta(days=HELD_DAYS) else None

    def load_bearing(self, today: date | None = None, held: bool = False) -> list[dict]:
        """Proposed CLAIMs, THEORYs and TERMs that something needs, most-needed first.

        An entry with a recent blocker note is left out, or with `held=True` is all that is listed.
        """
        today = today or date.today()
        rows = []
        for code in self.docs:
            if scheme(code) not in ("CLAIM", "THEORY", "TERM") or self.status(code) != "Proposed":
                continue
            if bool(self.held_since(code, today)) != held:
                continue
            reach = self.dependents(code)
            if reach:
                rows.append({"code": code, "reach": len(reach), "direct": len(self.needed_by[code]),
                             "warrant": self.docs[code].get("warrant"),
                             "open_premises": sorted(self.open_premises(code)),
                             "live_objections": self.live_objections(code)})
        return sorted(rows, key=lambda r: (-r["reach"], -r["direct"], r["code"]))

    def inversions(self) -> list[tuple]:
        """Active CLAIMs that rest on, or are grounded in, something the record does not hold.

        An ARG is not counted: its status is credence in its inference, not in its premises (ADR-059).
        Nor is a LIT: its status is whether the work can be had; an unread one is in unread_grounds.
        """
        return [(c, f, t, self.status(t))
                for c, fm in sorted(self.docs.items()) if scheme(c) == "CLAIM" and self.status(c) == "Active"
                for f in ("rests_on", "grounds") for t in as_list(fm.get(f))
                if t in self.docs and scheme(t) != "LIT" and self.status(t) != "Active"]

    def converse_inversions(self) -> list[tuple]:
        """Proposed readings that still list an Active claim under `supports`.

        The repair bot writes the converse `grounds` onto the claim, and the lint's inverted_ground
        then fails: a stale converse left when an edge moved, which the bot never removes.
        """
        return [(t, c) for t, fm in sorted(self.docs.items())
                if scheme(t) == "THEORY" and self.status(t) != "Active"
                for c in as_list(fm.get("supports")) if scheme(c) == "CLAIM" and self.status(c) == "Active"]

    def sound_unheld(self) -> list[tuple]:
        """Sound ARGs (inference Active, every premise Active) whose conclusion the record does not hold.

        An ARG with a held undercutter is left out: the undercutter already says what it does not carry.
        """
        return [(a, c, self.status(c))
                for a, fm in sorted(self.docs.items()) if scheme(a) == "ARG" and self.sound(a)
                and not any(self.status(u) == "Active" for u in as_list(fm.get("undercut_by")))
                for c in as_list(fm.get("concludes")) if c in self.docs and self.status(c) != "Active"]

    def unwritten_concessions(self) -> list[tuple]:
        """Active objections whose target has not been revised for them.

        An Active objection is one the record holds true, whatever its role: granted, or a counter
        that went Active when it was conceded. ADR-059 records a conceded objection by revising its
        target; a target unchanged since the concession still says what was conceded.
        """
        out = []
        for g, fm in sorted(self.docs.items()):
            if scheme(g) != "CLAIM" or self.status(g) != "Active":
                continue
            for t in as_list(fm.get("objects_to")):
                if t in self.docs and self.status(t) not in RETIRED and not self.written(g, t):
                    revised = [str(h.get("date", "")) for h in self.docs[t].get("history") or []
                               if isinstance(h, dict)]
                    out.append((g, t, str(fm.get("date", "")), max(revised, default="never")))
        return out

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

    def ready(self, today: date | None = None) -> list[str]:
        """Unblocked CLAIMs that no standing blocker note holds: the claims a pass can rule on now."""
        today = today or date.today()
        return [c for c in self.unblocked() if not self.held_since(c, today)]

    def held_unblocked(self, today: date | None = None) -> list[tuple]:
        """Unblocked CLAIMs a standing blocker note holds: what they wait on is not in the graph."""
        today = today or date.today()
        return [(c, d) for c in self.unblocked() if (d := self.held_since(c, today))]

    def sole_blockers(self) -> list[tuple]:
        """Unheld premises ranked by how many claims each is the only thing holding back.

        A claim counts when it has no live objection and exactly one premise the record does not
        hold. Freeing the premise, or showing the edge is corroboration (ADR-058), frees the claim.
        This replaced reach as the order of work once the reliance ranking flattened (ADR-057 v6).
        """
        held_back: dict[str, list[str]] = {}
        for c in sorted(self.docs):
            if scheme(c) != "CLAIM" or self.status(c) != "Proposed" or self.live_objections(c):
                continue
            open_ = sorted(self.open_premises(c))
            if len(open_) == 1:
                held_back.setdefault(open_[0], []).append(c)
        return sorted(held_back.items(), key=lambda kv: (-len(kv[1]), kv[0]))

    def open_sole_blockers(self, today: date | None = None) -> list[tuple]:
        """Sole blockers no standing blocker note already answers: neither the premise is held,
        nor every claim it holds back."""
        today = today or date.today()
        return [(p, cs) for p, cs in self.sole_blockers() if not self.held_since(p, today)
                and not all(self.held_since(c, today) for c in cs)]

    def reading_depth(self, code: str) -> str | None:
        """How deeply a reading's sources are read: Read if any NOTE on a source says so."""
        return self.depth_of(set(as_list(self.docs.get(code, {}).get("source"))))

    def depth_of(self, works: set[str]) -> str | None:
        depths = set().union(*(self.read_as.get(w, set()) for w in works))
        return "Read" if "Read" in depths else "Skimmed" if "Skimmed" in depths else None

    def unread_grounds(self) -> list[tuple]:
        """Live CLAIMs that need a work no NOTE reads: an unread work takes no edge (ADR-058)."""
        return [(c, unread) for c in sorted(self.docs) if scheme(c) == "CLAIM" and self.status(c) in LIVE
                and (unread := [t for t in self.premises(c) if scheme(t) == "LIT" and not self.depth_of({t})])]

    def unread_readings(self) -> list[tuple]:
        """Proposed THEORYs no source of which is read in full: reading, not review, is their next step."""
        return [(t, d) for t in sorted(self.docs) if scheme(t) == "THEORY" and self.status(t) == "Proposed"
                and (d := self.reading_depth(t)) != "Read"]

    def stale_blockers(self) -> list[tuple]:
        """Blocker notes that name something which has moved since the note was written.

        The note says what the entry waits on. When an entry it names is revised, or a work it
        names gets a reading, the wait may be over, so the entry comes back before its timer runs
        out. The timer (HELD_DAYS) only guarantees one look at the latest; this is the earlier one.
        """
        out = []
        for c in sorted(self.docs):
            if self.status(c) != "Proposed" or not (d := self.blocker_date(c)):
                continue
            note = self.bodies[c][self.bodies[c].rfind(f"## Note of {d}: what holds it back"):]
            named = sorted({t for t in re.findall(r"\b[A-Z]+-(?:\d+|tmp[a-z0-9]+)\b", note) if t in self.docs and t != c})
            changed = [t for t in named if self.moved_since(t, d)]
            if changed:
                out.append((c, d, changed))
        return out

    def moved_since(self, code: str, day: str) -> bool:
        """Whether an entry was revised, or a work was read, after the given date."""
        # a work's own history is bookkeeping (status, edges); for a work only a reading counts
        revised = scheme(code) != "LIT" and any(
            str(h.get("date", "")) > day for h in self.docs[code].get("history") or [] if isinstance(h, dict))
        read = any(str(self.docs[n].get("date", "")) > day for n in self.notes_on.get(code, ())
                   if self.status(n) in ("Read", "Skimmed"))
        return revised or read

    def unblocked(self) -> list[str]:
        """Proposed CLAIMs whose premises are all Active and that no live objection stands against."""
        return [c for c in sorted(self.docs) if scheme(c) == "CLAIM" and self.status(c) == "Proposed"
                and not self.open_premises(c) and not self.live_objections(c)]


def short(r: Record, code: str, n: int = 90) -> str:
    t = r.title(code)
    return f"{code} [{r.status(code)}] {t[:n]}{'…' if len(t) > n else ''}"


def main(root: str = "record", top: int = 30, show: str | None = None):
    r = Record.load(Path(root))
    today = date.today()
    if show:
        fm = r.docs[show]
        print(short(r, show, 200), f"| {fm.get('role')} {fm.get('warrant')}")
        if scheme(show) == "THEORY":
            print("sources read:", r.reading_depth(show) or "no NOTE")
        print("blocker note:", r.blocker_date(show) or "none")
        print("defeated_if:", fm.get("defeated_if"))
        for f in NEEDS.get(scheme(show), []) + ["objected_by", "countered_by", "objects_to", "answers"]:
            for t in as_list(fm.get(f)):
                print(f"  {f}: {short(r, t)}")
        for d in sorted(r.needed_by.get(show, ())):
            print(f"  needed by: {short(r, d)}")
        return
    # 1. What must be empty: each is a finding the record contradicts itself on.
    print("## Credence inversions: Active CLAIMs resting on what is not held\n")
    for row in r.inversions():
        print("- {} {} {} [{}]".format(*row))
    print("\n## Stale converses: a Proposed reading still supports an Active claim\n")
    for t, c in r.converse_inversions():
        print(f"- {t} supports {c}")
    print("\n## Sound arguments whose conclusion is not held\n")
    for row in r.sound_unheld():
        print("- {} concludes {} [{}]".format(*row))
    print("\n## Concessions not written into their targets\n")
    for row in r.unwritten_concessions():
        print("- {} concedes against {} on {}; target last revised {}".format(*row))
    print("\n## Premises that are retired\n")
    for row in r.retired_premises():
        print("- {} {} {} [{}] -> {}".format(*row))
    print("\n## Open questions with an Active answer\n")
    for q, a in r.open_with_active_answer():
        print(f"- {short(r, q, 70)} <- {', '.join(a)}")
    # 2. The work, in the order a pass takes it.
    ready = r.ready(today)
    print(f"\n## Ready for a ruling ({len(ready)}): premises held, no live objection, no standing blocker note\n")
    by_line: dict[str, list[str]] = {}
    for c in ready:
        by_line.setdefault((as_list(r.docs[c].get("line")) or ["(no line)"])[0], []).append(c)  # primary line
    for line, codes in sorted(by_line.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"### {line} ({len(codes)})")
        for c in codes:
            print(f"- {short(r, c)}")
    sole, all_sole = r.open_sole_blockers(today), r.sole_blockers()
    print(f"\n## Sole blockers (top {top} of {len(sole)}; {len(all_sole) - len(sole)} more held by a recent"
          " note): the one unheld premise of each claim listed\n")
    for t, cs in sole[:top]:
        print(f"- {len(cs):2d} {short(r, t, 70)} <- {', '.join(cs)}")
    print("\n## Blocker notes something they name has moved since: an entry revised, a work read\n")
    for c, d, ts in r.stale_blockers():
        print(f"- {c} (note of {d}): {', '.join(ts)} revised since")
    held = r.held_unblocked(today)
    print(f"\n## Held: unblocked, with a blocker note under {HELD_DAYS} days old ({len(held)})\n")
    for c, d in held:
        print(f"- {short(r, c, 70)}  held since {d}")
    unread = r.unread_readings()
    print(f"\n## Proposed readings no source of which is read in full ({len(unread)})\n")
    for t, d in unread:
        print(f"- {short(r, t, 70)}  {d or 'no NOTE'}")
    unread_g = r.unread_grounds()
    print(f"\n## Live claims that need a work no NOTE reads ({len(unread_g)})\n")
    for c, ts in unread_g:
        print(f"- {short(r, c, 70)}  {', '.join(f'{t} [{r.status(t)}]' for t in ts)}")
    rows = r.load_bearing()
    print(f"\n## Load-bearing Proposed entries by reach (top {top} of {len(rows)})\n")
    for x in rows[:top]:
        print(f"- {x['reach']:3d}/{x['direct']:<2d} {short(r, x['code'])}  "
              f"open premises: {x['open_premises'] or '-'}; live objections: {x['live_objections'] or '-'}")


if __name__ == "__main__":
    fire.Fire(main)
