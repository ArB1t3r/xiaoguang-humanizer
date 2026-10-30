#!/usr/bin/env python3
"""Validate this skill package with Python 3.10+ and no dependencies."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

from build_portable import build as build_portable
from build_distribution import check_distribution

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_file(relative):
    path = (ROOT / relative).resolve()
    require(path.is_relative_to(ROOT), f"Path escapes package: {relative}")
    require(path.is_file(), f"Missing file: {relative}")
    return path


def frontmatter_value(frontmatter, key):
    match = re.search(r"^" + re.escape(key) + r":\s*([^\n]+)", frontmatter, re.M)
    require(match is not None, f"Missing metadata field: {key}")
    return match.group(1).strip().strip('"').strip("'")


def validate():
    skill = local_file("SKILL.md").read_text(encoding="utf-8")
    header = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
    require(header is not None, "SKILL.md needs YAML frontmatter")
    name = frontmatter_value(header.group(1), "name")
    require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) is not None,
            "Skill name must use lowercase letters, numbers, and hyphens")
    require(len(name) <= 64, "Skill name is too long")
    require(name == ROOT.name, "Skill name must match the directory name")
    require(re.search(r"^description:\s*\S", header.group(1), re.M),
            "Missing description")
    version_match = re.search(r'^  version: "([^"]+)"$', header.group(1), re.M)
    require(version_match is not None, "Missing quoted metadata.version")

    manifest = json.loads(local_file("agent.json").read_text(encoding="utf-8"))
    require(manifest["schema_version"] == "1", "Unsupported discovery manifest version")
    require(manifest["id"] == name, "Manifest ID differs from skill name")
    require(manifest["version"] == version_match.group(1), "Version mismatch")
    require(manifest["display_name"] == "小光Humanizer", "Display name mismatch")
    local_file(manifest["entrypoint"])
    local_file(manifest["integration_guide"])
    local_file(manifest["installation"]["entrypoint"])
    check_distribution()
    for kind in ("quick_zh", "quick_en", "full"):
        local_file(manifest["chat_entrypoints"][kind])
    portable = local_file(manifest["chat_entrypoints"]["full"])
    require(portable.read_text(encoding="utf-8") == build_portable(),
            "Portable instructions are stale; run python3 scripts/build_portable.py")
    for paths in manifest["references"].values():
        require(isinstance(paths, list), "Reference groups must be arrays")
        for path in paths:
            local_file(path)
    require(manifest["license"] == frontmatter_value(header.group(1), "license"),
            "License mismatch")
    local_file("LICENSE")

    ui = local_file("agents/openai.yaml").read_text(encoding="utf-8")
    require('display_name: "小光Humanizer"' in ui, "UI display name mismatch")
    require("$" + name in ui, "UI prompt invokes a different skill")

    markdown_files = sorted(ROOT.rglob("*.md"))
    for path in markdown_files:
        if ".git" in path.parts:
            continue
        body = path.read_text(encoding="utf-8")
        require("[TODO:" not in body, f"Unfinished scaffold: {path.relative_to(ROOT)}")
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target_path = unquote(target.split("#", 1)[0])
            destination = (path.parent / target_path).resolve()
            require(destination.is_relative_to(ROOT), f"Link escapes package: {target}")
            require(destination.is_file(),
                    f"Broken link in {path.relative_to(ROOT)}: {target}")

    cases = local_file("references/evaluation-cases.md").read_text(encoding="utf-8")
    fixtures = re.findall(r"~~~~markdown\n(.*?)\n~~~~", cases, re.S)
    require(len(fixtures) == 2, "Expected a before/after Markdown preservation fixture")
    before, after = fixtures
    for pattern, flags in [
        (r"\A---\n.*?\n---", re.S),
        (r"^# Setup$", re.M),
        (r"```sh\n.*?\n```", re.S),
        (r"https://[^)]+", 0),
    ]:
        require(re.findall(pattern, before, flags) == re.findall(pattern, after, flags),
                "The example changes a protected technical span")

    return {
        "skill": name,
        "version": manifest["version"],
        "status": "passed",
        "checks": ["metadata consistency", "reference files", "local links", "portable bundle freshness",
                   "native skill and plugin parity", "marketplace target",
                   "protected fixture spans"],
        "note": "Package validation only; model writing quality is not evaluated.",
    }


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, json.JSONDecodeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
