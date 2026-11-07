# scratch/formal/line_parts.py
"""How a line's parts relate: the signal for splitting a line (ADR-tmpyihxy).

Counts the relations among the components of a line's parts, part by part,
so that a review can see whether the parts hang together or are separate
inquiries filed under one line. It decides nothing.

Usage (run from the repository root, with python3 -I):

    python3 -I scratch/formal/line_parts.py SYNTHESIS-a SYNTHESIS-b ...
        one part per synthesis: the part is that synthesis's `integrates`

    python3 -I scratch/formal/line_parts.py --sections SYNTHESIS-x
        one part per "## " section of one synthesis's body: a component
        belongs to the first section whose bullets lead with its code

Each relation from a component of one part to a component of another counts
once, in the row of the part it starts in. A component in two parts is
counted in the first. Converse fields are derived (ADR-079), so only stored
sides are read and nothing is counted twice.
"""
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(".")
DIRS = {"CLAIM": "claims.d", "CASE": "cases.d", "QUESTION": "questions.d",
        "TERM": "terms.d", "ARG": "arguments.d", "THEORY": "theory.d",
        "SYNTHESIS": "syntheses.d", "LIT": "literature.d", "NOTE": "notes.d"}
RELATIONS = ("rests_on", "grounds", "uses", "illustrates", "counterexample_to",
             "refines", "answers", "bears_on", "objects_to", "undercuts",
             "complements", "concludes", "corroborates", "integrates", "premises")
SKIP = ("The account", "The integration", "Not stated", "What it does not",
        "Admission", "Correction")


def load(code: str) -> tuple[dict, str]:
    path = ROOT / "record" / DIRS[code.split("-")[0]] / f"{code}.md"
    text = path.read_text()
    front, body = text.split("\n---\n", 1)
    return yaml.safe_load(front.split("---", 1)[1]) or {}, body


def codes(value) -> list[str]:
    if not value:
        return []
    return [str(v) for v in (value if isinstance(value, list) else [value])]


def parts_from_syntheses(names: list[str]) -> dict[str, list[str]]:
    return {n: codes(load(n)[0].get("integrates")) for n in names}


def parts_from_sections(name: str) -> dict[str, list[str]]:
    meta, body = load(name)
    members = set(codes(meta.get("integrates")))
    parts = {}
    for section in re.split(r"(?m)^## ", body)[1:]:
        head = section.split("\n", 1)[0].strip()
        if head.startswith(SKIP):
            continue
        found = []
        for bullet in re.findall(r"(?m)^- (.*)", section):
            found += [c for c in re.findall(r"\b[A-Z]+-\d+\b", bullet.split(":")[0])
                      if c in members]
        parts[head] = list(dict.fromkeys(found))
    return parts


def matrix(parts: dict[str, list[str]]) -> tuple[list[str], dict]:
    home = {}
    for name, members in parts.items():
        for c in members:
            home.setdefault(c, name)
    counts = {}
    for c, part in home.items():
        meta, _ = load(c)
        for field in RELATIONS:
            for target in codes(meta.get(field)):
                if target in home:
                    key = (part, home[target])
                    counts[key] = counts.get(key, 0) + 1
    return list(parts), counts


def main(argv: list[str]) -> None:
    if argv[:1] == ["--sections"]:
        parts = parts_from_sections(argv[1])
    else:
        parts = parts_from_syntheses(argv)
    names, counts = matrix(parts)
    print("rows: the part a relation starts in; columns: the part it points into\n")
    print(f"{'':32}" + "".join(f"{i:>6}" for i in range(len(names))))
    for i, a in enumerate(names):
        cells = "".join(f"{counts.get((a, b), 0):>6}" for b in names)
        print(f"{i} {a[:29]:30}{cells}   ({len(parts[a])} components)")
    inside = sum(counts.get((a, a), 0) for a in names)
    total = sum(counts.values())
    print(f"\nwithin parts: {inside} of {total} relations")
    for a in names:
        out = sum(v for (x, y), v in counts.items() if x == a and y != a)
        into = sum(v for (x, y), v in counts.items() if y == a and x != a)
        print(f"  {a[:40]:42} inside {counts.get((a, a), 0):3}  out {out:3}  in {into:3}")


if __name__ == "__main__":
    main(sys.argv[1:])
