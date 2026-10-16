#!/usr/bin/env python3
"""Validate the Kali Red Dark Android palette and required project metadata."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ROOT / "theme" / "colors.json"
HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    try:
        data = json.loads(PALETTE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        fail("theme/colors.json is missing")
    except json.JSONDecodeError as exc:
        fail(f"theme/colors.json is invalid JSON: {exc}")

    for key in ("name", "version", "source", "target", "colors"):
        if key not in data:
            fail(f"Missing top-level field: {key}")

    if data["name"] != "Kali Red Dark":
        fail("Unexpected theme name")
    if not isinstance(data["colors"], dict) or not data["colors"]:
        fail("'colors' must be a non-empty object")

    for token, value in data["colors"].items():
        if not isinstance(value, str) or not HEX_COLOR.fullmatch(value):
            fail(f"Color token {token!r} must use six-digit hex RGB (example: #EC0101)")

    target = data["target"]
    if target.get("platform") != "Android":
        fail("Target platform must remain Android")
    if target.get("rootRequired") is not False:
        fail("This project must continue to document a no-root setup")

    print(f"OK: {len(data['colors'])} color tokens validated for {data['name']} v{data['version']}")


if __name__ == "__main__":
    main()
