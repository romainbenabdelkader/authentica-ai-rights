#!/usr/bin/env python3
"""Validate the AUTHENTICA JSON-LD examples against the manifest JSON Schema.

The JSON Schema (manifest/schema.json) is the source of truth. When the
optional `jsonschema` library is available the examples are validated directly
against it, so the schema and the examples cannot silently drift apart. If
`jsonschema` is not installed the script falls back to an equivalent built-in
check using only the Python standard library, so it still runs anywhere.

Install the schema validator with:  pip install jsonschema
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "examples"
SCHEMA = ROOT / "manifest" / "schema.json"
CONTEXT = ROOT / "manifest" / "manifest-v1.jsonld"

UID_RE = re.compile(r"^[A-Z]{2}-[0-9]{4}-AUTH(-[A-Z]{3})?-[0-9]{6}$")
ORIGINS = {"human", "ai", "hybrid", "unknown"}
AI_TRAINING = {"prohibited", "permitted", "license_required", "unknown"}
HASH_ALGORITHMS = {"sha256", "sha3-256"}


def load_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def builtin_validate(path: Path) -> list[str]:
    """Standard-library fallback mirroring the JSON Schema constraints."""
    data = load_json(path)
    errors: list[str] = []

    for field in [
        "@context",
        "@type",
        "uid_auth",
        "name",
        "creator",
        "origin",
        "issued_at",
        "issuer",
        "rights",
        "hash",
    ]:
        require(field in data, f"missing field: {field}", errors)

    if errors:
        return errors

    require(data["@type"] == "CreativeWork", "@type must be CreativeWork", errors)
    require(bool(UID_RE.match(data["uid_auth"])), "uid_auth format is invalid", errors)
    require(data["origin"] in ORIGINS, "origin value is invalid", errors)

    try:
        datetime.fromisoformat(data["issued_at"].replace("Z", "+00:00"))
    except ValueError:
        errors.append("issued_at must be ISO-8601 date-time")

    issuer = data["issuer"]
    require(isinstance(issuer, dict), "issuer must be an object", errors)
    if isinstance(issuer, dict):
        require(bool(issuer.get("name")), "issuer.name is required", errors)
        require(bool(issuer.get("type")), "issuer.type is required", errors)

    rights = data["rights"]
    require(isinstance(rights, dict), "rights must be an object", errors)
    if isinstance(rights, dict):
        require(rights.get("ai_training") in AI_TRAINING, "rights.ai_training is invalid", errors)
        require(isinstance(rights.get("tdm_opt_out"), bool), "rights.tdm_opt_out must be boolean", errors)

    asset_hash = data["hash"]
    require(isinstance(asset_hash, dict), "hash must be an object", errors)
    if isinstance(asset_hash, dict):
        require(asset_hash.get("algorithm") in HASH_ALGORITHMS, "hash.algorithm is invalid", errors)
        require(bool(asset_hash.get("value")), "hash.value is required", errors)

    return errors


def main() -> int:
    schema = load_json(SCHEMA)
    load_json(CONTEXT)

    try:
        from jsonschema import Draft202012Validator

        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        mode = "jsonschema (schema-driven)"
    except ModuleNotFoundError:
        validator = None
        mode = "built-in fallback (install jsonschema for schema-driven checks)"

    failures = 0
    for path in sorted(EXAMPLES.glob("*.jsonld")):
        if validator is not None:
            errors = [
                f"{list(e.path)}: {e.message}"
                for e in sorted(validator.iter_errors(load_json(path)), key=lambda e: list(e.path))
            ]
        else:
            errors = builtin_validate(path)

        if errors:
            failures += 1
            print(f"INVALID {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK {path.relative_to(ROOT)}")

    print(f"[validated with: {mode}]")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
