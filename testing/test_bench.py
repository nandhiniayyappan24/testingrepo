"""Tests for the benchmark script."""

from __future__ import annotations

from pathlib import Path


def test_bench_script_exists_and_references_pytest() -> None:
    bench_path = Path(__file__).resolve().parents[1] / "bench" / "bench.py"
    assert bench_path.is_file()
    content = bench_path.read_text(encoding="utf-8")
    assert "pytest" in content
    assert "cProfile" in content
