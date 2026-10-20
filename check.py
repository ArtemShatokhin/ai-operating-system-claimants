#!/usr/bin/env python3
"""Re-check that every claimant still says on its own page what this repo records.

Each entry in claimants.yaml carries a `quote` taken from the vendor's own page.
This script fetches that page and fails when the quote is gone, so the table in
README.md cannot quietly go stale. No API keys, no accounts, stdlib only.

    python3 check.py            # check every claimant
    python3 check.py --name "Cloudflare OS"

Exit code 0 when every quote is still present, 1 when one has drifted.
"""
from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load_yaml(path: Path) -> list[dict]:
    """Minimal reader for the flat list this repo keeps: no dependency on PyYAML."""
    entries: list[dict] = []
    current: dict | None = None
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  - "):
            current = {}
            entries.append(current)
            key, _, value = line[4:].partition(": ")
            current[key.strip()] = _value(value)
            continue
        if line.startswith("    ") and current is not None:
            key, _, value = line[4:].partition(": ")
            current[key.strip()] = _value(value)
    return entries


def _value(raw: str):
    raw = raw.strip()
    if raw.lower() in {"true", "false"}:
        return raw.lower() == "true"
    return raw.strip('"').strip("'")


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "ai-operating-system-claimants/1.0"})
    with urllib.request.urlopen(request, timeout=30) as response:  # noqa: S310 - fixed URLs from the repo
        body = response.read().decode("utf-8", "replace")
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", body))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="check one claimant only")
    args = parser.parse_args()

    entries = load_yaml(ROOT / "claimants.yaml")
    if args.name:
        entries = [e for e in entries if e.get("name") == args.name]
        if not entries:
            print(f"no claimant named {args.name!r}")
            return 2

    drifted = 0
    for entry in entries:
        name, url, quote = entry["name"], entry["page"], entry["quote"]
        try:
            text = fetch(url)
        except Exception as error:  # noqa: BLE001 - a fetch failure is a drift signal too
            print(f"FETCH FAILED  {name}: {error}")
            drifted += 1
            continue
        found = re.sub(r"\s+", " ", quote) in text
        print(f"{'OK      ' if found else 'DRIFTED '} {name}")
        if not found:
            print(f"          quote no longer on {url}: {quote}")
            drifted += 1
    print(f"\n{len(entries) - drifted}/{len(entries)} sources still say what this repo records")
    return 0 if drifted == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
