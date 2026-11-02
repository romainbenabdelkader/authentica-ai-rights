#!/usr/bin/env python3
"""Validate the AUTHENTICA JSON-LD examples against the manifest JSON Schema.

The JSON Schema (manifest/schema.json) is the source of truth. The jsonschema
library is required; if it cannot be imported, validation stops with exit code 2.
No reduced validation mode is used. Date and URI formats remain annotations.
This script does not verify asset hashes, signatures or issuer authority.

Install the schema validator with: python3 -m pip install 'jsonschema>=4,<5'
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
SCHEMA = ROOT / "manifest" / "schema.json"
CONTEXT = ROOT / "manifest" / "manifest-v1.jsonld"

def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        print(
            "Schema validation unavailable: jsonschema and its dependencies are required. "
            "Install with: python3 -m pip install 'jsonschema>=4,<5'",
            file=sys.stderr,
        )
        return 2

    schema = load_json(SCHEMA)
    load_json(CONTEXT)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)

    failures = 0
    for path in sorted(EXAMPLES.glob("*.jsonld")):
        errors = [
            f"{list(e.path)}: {e.message}"
            for e in sorted(validator.iter_errors(load_json(path)), key=lambda e: str(list(e.path)))
        ]
        if errors:
            failures += 1
            print(f"INVALID {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {path.relative_to(ROOT)}")

    print("[validated with: jsonschema (schema-driven)]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
