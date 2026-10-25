#!/usr/bin/env python3
"""Run the finite scientific checks and optionally save their outputs."""
from __future__ import annotations

import argparse
import importlib.metadata
import json
from pathlib import Path
import sys

import verify_bounds
import verify_protocols
import verify_rounding


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()
    result = {
        "environment": {"python": sys.version.split()[0], "numpy": importlib.metadata.version("numpy")},
        "protocols": verify_protocols.run(),
        "bounds": verify_bounds.run(),
        "rounding": verify_rounding.run(),
        "result": "All finite checks passed",
    }
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
