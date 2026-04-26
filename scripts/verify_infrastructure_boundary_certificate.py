#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from infrastructure_boundary_certificate import infrastructure_boundary_certificate


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def main() -> int:
    doc = ROOT / "docs/status/INFRASTRUCTURE_BOUNDARY_CERTIFICATE.md"
    source = ROOT / "src/infrastructure_boundary_certificate.py"
    status = ROOT / "STATUS.md"
    if not status.exists():
        status = ROOT / "README.md"
    require(doc.exists(), "missing infrastructure boundary certificate doc")
    require(source.exists(), "missing certificate source")
    require(status.exists(), "missing status/readme boundary source")
    boundary_text = doc.read_text(encoding="utf-8") + "\n" + status.read_text(encoding="utf-8")
    cert = infrastructure_boundary_certificate(
        ROOT,
        [
            "docs/status/INFRASTRUCTURE_BOUNDARY_CERTIFICATE.md",
            "scripts/verify_infrastructure_boundary_certificate.py",
            "src/infrastructure_boundary_certificate.py",
            "tests/test_infrastructure_boundary_certificate.py",
        ],
        boundary_text,
    )
    require(cert.theorem_id == "SI-IBC-1", "wrong theorem id")
    require(cert.status == "PASS", f"certificate failed: {cert}")
    require(cert.all_required_present, "required manifest is incomplete")
    require(cert.boundary_declared, "infrastructure boundary missing")
    doc_text = doc.read_text(encoding="utf-8")
    for literal in [
        "Status: CLOSED repository-scope certificate.",
        "Theorem ID: SI-IBC-1.",
        "No repository-level claim of universal reproducibility across all machines.",
        "No repository-level claim of peer-reviewed acceptance.",
        "No repository-level claim of external validation unless explicitly documented.",
        "No repository-level claim that infrastructure closure equals theorem-level completion.",
    ]:
        require(literal in doc_text, f"missing doc literal: {literal}")
    print(json.dumps(cert.__dict__, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
