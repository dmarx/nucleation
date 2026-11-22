"""Abstract-level pre-screen for LEAD-047.

Each work in results/hits.jsonl is flagged on the lead's four criteria by
keyword patterns over title and abstract:

  C1 threat objectively specified (a conditioning or avoidance task, a known
     or instructed contingency or probability);
  C2 an intervention on the defensive process's authority or evidence access
     (cost or availability of avoidance, response prevention, instruction,
     drug, lesion or stimulation of the arbitration);
  C3 represented threat measured or fixed (expectancy, belief rating,
     explicit probability);
  C4 approach, exploration or later avoidance as an outcome.

The flags only rank. A work with all four flags is read at abstract level by
hand and coded in screening.tsv; the flags never decide inclusion.

    python3 -I scratch/studies/lead-047/screen.py > scratch/studies/lead-047/results/prescreen.tsv
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

PATTERNS = {
    "C1": r"conditioning|avoidance (task|paradigm|learning)|shock|aversive (stimulus|outcome)|unconditioned stimulus|\bUS\b|threat probabilit|loss probabilit|approach.avoidance conflict|instructed",
    "C2": r"instruct|cost(ly)?|response prevention|block(ed|ing)? (the )?avoidance|prevent(ed|ion)? (of )?avoidance|lorazepam|benzodiazepin|diazepam|lesion|stimulation|\bTMS\b|tDCS|manipulat|availab(le|ility) of avoidance|safety behavio(u)?r(s)? (were|was)? ?(eliminat|fad|remov|withdraw)",
    "C3": r"expectanc|threat belief|belief rating|harm expectan|explicit(ly)? (stated |known )?probabilit|threat probabilit|contingency (awareness|knowledge)",
    "C4": r"avoid|approach|exploration|explor",
}
COMPILED = {k: re.compile(v, re.I) for k, v in PATTERNS.items()}


def flags(text):
    """Return the set of criteria whose pattern matches text."""
    return {k for k, rx in COMPILED.items() if rx.search(text or "")}


def load(path):
    with open(path) as f:
        return [json.loads(line) for line in f if line.strip()]


def main():
    hits = load(os.path.join(HERE, "results", "hits.jsonl"))
    rows = []
    for h in hits:
        fl = flags((h.get("title") or "") + " " + (h.get("abstract") or ""))
        rows.append((len(fl), "".join(sorted(fl)), h))
    rows.sort(key=lambda r: (-r[0], str(r[2].get("year"))))
    w = sys.stdout
    w.write("n_flags\tflags\tyear\tdoi\tpmcid\tfirst_author\ttitle\tqueries\n")
    for n, fl, h in rows:
        fa = (h.get("authors") or "").split(",")[0]
        w.write(f"{n}\t{fl}\t{h.get('year')}\t{h.get('doi') or ''}\t{h.get('pmcid') or ''}\t{fa}\t{h.get('title')}\t{','.join(h['queries'])}\n")
    counts = {}
    for n, _, _ in rows:
        counts[n] = counts.get(n, 0) + 1
    print("flag counts:", dict(sorted(counts.items())), file=sys.stderr)


if __name__ == "__main__":
    main()
