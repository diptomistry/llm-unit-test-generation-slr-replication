#!/usr/bin/env python3
"""
Reproduce core corpus statistics from the frozen CSVs in ../data/.

Usage (from public-replication-package/):
  python3 scripts/reproduce_statistics.py

Requires only the Python standard library. Uses paths relative to this package.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(name: str) -> list[dict]:
    with (DATA / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def split_codes(s: str) -> list[str]:
    if not s or s.strip() in {"NR", "n/a", ""}:
        return []
    return [c.strip() for c in re.split(r"[;|,]+", s) if c.strip()]


def pct(n: int, d: int) -> str:
    return f"{n}/{d} ({100.0 * n / d:.1f}%)"


def main() -> None:
    prim = load("final_primary_corpus.csv")
    sec = load("final_secondary_studies.csv")
    stats = load("final_corpus_statistics.csv")
    cfe = load("coverage_fault_evidence.csv")

    n = len(prim)
    assert n == 64, f"expected 64 primaries, found {n}"
    assert len(sec) == 10, f"expected 10 secondaries, found {len(sec)}"

    ids = [r["Paper_ID"] for r in prim]
    assert ids == [f"P{i:03d}" for i in range(1, 65)], "Paper_ID sequence mismatch"

    e = Counter()
    for r in prim:
        for c in split_codes(r.get("Evaluation_Codes", "")):
            e[c] += 1

    e4 = e["E4"]
    e5 = e["E5"]
    bugs = sum(1 for r in prim if (r.get("Real_Bugs") or "").lower() == "yes")
    mut = sum(1 for r in prim if (r.get("Mutation") or "").lower() == "yes")

    p061 = next(r for r in prim if r["Paper_ID"] == "P061")
    p037 = next(r for r in prim if r["Paper_ID"] == "P037")

    print("=== Frozen corpus ===")
    print(f"Primary studies: {n}")
    print(f"Secondary surveys: {len(sec)}")
    print()
    print("=== Evaluation hierarchy (multi-label) ===")
    for code in [f"E{i}" for i in range(7)]:
        print(f"  {code}: {pct(e[code], n)}")
    print()
    print("=== Flags ===")
    print(f"  Mutation flag yes: {pct(mut, n)}")
    print(f"  Real_Bugs flag yes: {pct(bugs, n)}")
    print()
    print("=== Audited targets ===")
    print(f"  E4 (mutation evaluation): {pct(e4, n)}  [expect 12/64 (18.8%)]")
    print(f"  E5 (real-fault evidence): {pct(e5, n)}  [expect 13/64 (20.3%)]")
    assert e4 == 12 and e5 == 13 and bugs == 13 and mut == 12
    print()
    print("=== Spot checks ===")
    print(f"  P061 Evaluation_Codes={p061['Evaluation_Codes']} Real_Bugs={p061['Real_Bugs']} Mutation={p061['Mutation']}")
    assert "E5" not in split_codes(p061["Evaluation_Codes"])
    assert (p061.get("Real_Bugs") or "").lower() == "no"
    print(f"  P037 Venue={p037['Venue']}")
    print(f"  P037 DOI={p037['DOI']}")
    assert "ICST" in (p037.get("Venue") or "")
    assert "ICST69053" in (p037.get("DOI") or "").upper()
    print()
    print("=== Precomputed statistics file (sample) ===")
    for row in stats:
        if row["Statistic"] in {
            "evaluation_E3",
            "evaluation_E4",
            "evaluation_E5",
            "reports_mutation_flag",
            "reports_real_bugs_flag",
            "repository_level_yes",
        }:
            print(f"  {row['Statistic']}: {row['Fraction']} ({row['Percent']})")
    print()
    cfe_bugs = [r["Paper_ID"] for r in cfe if (r.get("Real_Bugs") or "").lower() == "yes"]
    print(f"coverage_fault_evidence Real_Bugs=yes: {len(cfe_bugs)} -> {', '.join(cfe_bugs)}")
    assert len(cfe_bugs) == 13
    print()
    print("OK: core statistics checks passed.")


if __name__ == "__main__":
    main()
