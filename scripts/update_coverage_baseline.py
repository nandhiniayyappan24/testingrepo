#!/usr/bin/env python3
"""Regenerate coverage-baseline.json from a local coverage.json run."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE_JSON = ROOT / "coverage.json"
BASELINE = ROOT / "coverage-baseline.json"


def main() -> None:
    if not COVERAGE_JSON.is_file():
        raise SystemExit(
            "Run tests with coverage first, e.g.\n"
            "  coverage run -m pytest testing/test_bench.py -q\n"
            "  coverage json -o coverage.json"
        )
    data = json.loads(COVERAGE_JSON.read_text(encoding="utf-8"))
    totals = data.get("totals", {})
    baseline = {
        "format": "coverage-baseline-v1",
        "generated_by": "scripts/update_coverage_baseline.py",
        "totals": {
            "percent_covered": round(totals.get("percent_covered", 0), 2),
            "percent_branches_covered": round(
                totals.get("percent_branches_covered", 0), 2
            ),
            "percent_statements_covered": round(
                totals.get("percent_statements_covered", 0), 2
            ),
        },
    }
    BASELINE.write_text(json.dumps(baseline, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {BASELINE}")


if __name__ == "__main__":
    main()
