"""Append coded items to coded.jsonl, skipping ids already present.
Usage: python3 -I append.py <coded.jsonl> <batch.json>  (batch: a JSON list of items)."""
import json, os, sys

REQ = {"id", "arm", "org", "url", "H", "SYS", "A", "ABOVE", "COMM", "vendor", "H_evidence", "A_evidence"}


def check(item):
    missing = REQ - set(item)
    assert not missing, (item.get("id"), missing)
    assert item["H"] in range(6) and item["A"] in range(6), item["id"]
    assert item["ABOVE"] == int(item["A"] >= 3), item["id"]
    assert item["SYS"] in (0, 1) and item["COMM"] in ("internal", "independent"), item["id"]


def main(out, batch):
    have = set()
    if os.path.exists(out):
        have = {json.loads(l)["id"] for l in open(out)}
    items = json.load(open(batch))
    with open(out, "a") as f:
        for it in items:
            check(it)
            if it["id"] in have:
                continue
            f.write(json.dumps(it, ensure_ascii=False) + "\n")
            have.add(it["id"])


if __name__ == "__main__":
    main(*sys.argv[1:3])
