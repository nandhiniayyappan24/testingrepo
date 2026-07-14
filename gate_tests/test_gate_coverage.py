"""Lightweight tests for external quality-gate scanners.

These tests are intentionally simple (no pytester) so CI/taxonomy tools can
execute them reliably and produce coverage artifacts.
"""

from __future__ import annotations

from pathlib import Path

from _pytest._code.source import Source


def test_source_getstatementrange_valid_line() -> None:
    src = Source(["x = 1\n", "y = 2\n"])
    start, end = src.getstatementrange(0)
    assert start == 0
    assert end == 1


def test_source_getstatementrange_out_of_range() -> None:
    src = Source(["x = 1\n"])
    try:
        src.getstatementrange(5)
    except IndexError:
        pass
    else:
        raise AssertionError("expected IndexError")


def test_byte_offset_to_character_offset() -> None:
    from _pytest._code.code import _byte_offset_to_character_offset

    text = "hello"
    assert _byte_offset_to_character_offset(text, 0) == 0
    assert _byte_offset_to_character_offset(text, len(text.encode("utf-8"))) == len(text)


def test_bench_script_present() -> None:
    bench = Path(__file__).resolve().parents[1] / "bench" / "bench.py"
    assert bench.is_file()
    assert "pytest" in bench.read_text(encoding="utf-8")
