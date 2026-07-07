#!/usr/bin/env python3
"""
Validate YAML frontmatter across the pipeline's agent and skill definitions.

Runs in CI and locally:

    python scripts/validate-frontmatter.py

Exits non-zero if any file has broken YAML, is missing a required key, or has a
name that does not match its file/directory. This is the guard against the class
of error where an unquoted description containing ': ' silently breaks parsing.
"""

import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# key sets by file class
AGENT_KEYS = ["name", "description", "tools", "model"]
SKILL_KEYS = ["name", "description", "allowed-tools"]

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

errors = []
checked = 0


def classify(path):
    base = os.path.basename(path)
    if base == "SKILL.md":
        return "skill"
    if os.sep + "agents" + os.sep in path:
        return "agent"
    return "other"


def expected_name(path, kind):
    if kind == "skill":
        # skill name should match its parent directory
        return os.path.basename(os.path.dirname(path))
    if kind == "agent":
        # agent name should match its filename stem
        return os.path.splitext(os.path.basename(path))[0]
    return None


for dp, dn, fn in os.walk(ROOT):
    if os.sep + ".git" in dp:
        continue
    for f in sorted(fn):
        if not f.endswith(".md"):
            continue
        path = os.path.join(dp, f)
        rel = os.path.relpath(path, ROOT)
        kind = classify(path)

        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        m = FM_RE.match(text)

        if not m:
            # agents and skills MUST have frontmatter; other .md need not
            if kind in ("agent", "skill"):
                errors.append(f"{rel}: missing YAML frontmatter")
            continue

        if kind == "other":
            # still confirm any frontmatter present is parseable
            try:
                yaml.safe_load(m.group(1))
            except yaml.YAMLError as e:
                errors.append(f"{rel}: invalid YAML frontmatter -> {str(e).splitlines()[0]}")
            continue

        checked += 1
        try:
            data = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            errors.append(f"{rel}: invalid YAML frontmatter -> {str(e).splitlines()[0]}")
            continue

        if not isinstance(data, dict):
            errors.append(f"{rel}: frontmatter is not a key/value block")
            continue

        required = AGENT_KEYS if kind == "agent" else SKILL_KEYS
        for key in required:
            if key not in data:
                errors.append(f"{rel}: missing required key '{key}'")
            elif data[key] in (None, ""):
                errors.append(f"{rel}: key '{key}' is empty")

        want = expected_name(path, kind)
        got = data.get("name")
        if want and got and got != want:
            errors.append(f"{rel}: name '{got}' does not match expected '{want}'")

if errors:
    print(f"Frontmatter validation FAILED ({len(errors)} problem(s)):\n")
    for e in errors:
        print("  - " + e)
    sys.exit(1)

print(f"Frontmatter validation passed: {checked} agent/skill file(s) OK.")
