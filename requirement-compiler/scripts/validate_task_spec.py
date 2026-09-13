#!/usr/bin/env python3
"""Validate Requirement Compiler v0.3 Mini/Full Task Spec YAML."""
from pathlib import Path
import sys

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

MODES = {"DIRECT", "EXPLORE_GOAL", "DISCOVER_PATH", "CLARIFY_SPEC", "DIAGNOSE", "RECOVER_CONTEXT", ""}
MINI_REQUIRED = {"spec_level", "spec_version", "outcome", "confirmed", "critical_unknowns", "locked", "success_checks", "next_action"}
FULL_EXTRA = {"current_stage", "selected_path", "derived", "assumptions", "flexible", "assets", "superseded", "invalidated", "last_known_good_state"}


def main(path: str) -> int:
    p = Path(path)
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    level = data.get("spec_level")
    if level not in {"mini", "full"}:
        print("spec_level must be mini or full")
        return 1

    required = set(MINI_REQUIRED)
    if level == "full":
        required |= FULL_EXTRA
    missing = sorted(required - data.keys())
    if missing:
        print("Missing required keys:", ", ".join(missing))
        return 1

    mode = ((data.get("next_action") or {}).get("mode") or "").strip()
    if mode not in MODES:
        print(f"Invalid next_action.mode: {mode}")
        return 1

    blockers = []
    for item in data.get("critical_unknowns") or []:
        if isinstance(item, dict) and str(item.get("impact", "")).upper() == "HIGH" and bool(item.get("blocks_execution")):
            blockers.append(item.get("item") or item.get("question") or "unnamed blocker")

    print(f"Task Spec structure: OK ({level})")
    if blockers:
        print("Execution blocked by HIGH unknowns:")
        for b in blockers:
            print(f"- {b}")
    else:
        print("No HIGH execution blockers detected.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: validate_task_spec.py <task-spec.yaml>", file=sys.stderr)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
