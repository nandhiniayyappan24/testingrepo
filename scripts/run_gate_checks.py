#!/usr/bin/env python3
"""Run quality-gate checks and emit artifacts expected by taxonomy scanners."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    install = "--install" in sys.argv
    if install:
        cmds = [
            [sys.executable, "-m", "pip", "install", "-e", ".[dev]", "coverage>=7.10"],
        ]
        for cmd in cmds:
            print("+", " ".join(cmd), flush=True)
            if subprocess.call(cmd, cwd=ROOT) != 0:
                return 1

    test_cmd = [
        sys.executable,
        "-m",
        "pytest",
        "-c",
        str(ROOT / "pytest.gate.ini"),
        str(ROOT / "gate_tests"),
    ]
    print("+", " ".join(test_cmd), flush=True)
    rc = subprocess.call(test_cmd, cwd=ROOT)
    if rc == 0:
        print("Gate artifacts:", ROOT / "coverage.xml", ROOT / "coverage.json", flush=True)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
