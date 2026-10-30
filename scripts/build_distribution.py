#!/usr/bin/env python3
"""Build native skill and plugin bundles from one set of maintained rules."""

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_manifest():
    return json.loads((ROOT / "agent.json").read_text(encoding="utf-8"))


def inside_root(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError(f"Path escapes repository: {relative}")
    return path


def expected_files():
    manifest = load_manifest()
    runtime = inside_root(manifest["installation"]["runtime_path"])
    plugin = inside_root(manifest["installation"]["plugin_path"])
    files = {runtime / relative: inside_root(relative).read_bytes()
             for relative in manifest["distribution"]["skill_files"]}
    files[plugin / "LICENSE"] = (ROOT / "LICENSE").read_bytes()
    return files


def check_distribution():
    manifest = load_manifest()
    plugin = inside_root(manifest["installation"]["plugin_path"])
    runtime = inside_root(manifest["installation"]["runtime_path"])
    metadata = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
    if metadata["name"] != manifest["id"] or metadata["version"] != manifest["version"]:
        raise ValueError("Plugin identity or version differs from the skill")
    if runtime != plugin / "skills" / manifest["id"]:
        raise ValueError("Plugin skill is outside the standard skills/<name> location")
    expected = expected_files()
    for path, content in expected.items():
        if not path.is_file() or path.read_bytes() != content:
            raise ValueError(f"Stale distribution file: {path.relative_to(ROOT)}; run scripts/build_distribution.py")
    actual = {p for p in plugin.rglob("*") if p.is_file()}
    if actual != set(expected) | {plugin / "plugin.json"}:
        raise ValueError("Unexpected files in generated plugin package")
    marketplace = json.loads(inside_root(manifest["installation"]["marketplace"]).read_text())
    entries = [entry for entry in marketplace["plugins"] if entry["name"] == manifest["id"]]
    if len(entries) != 1 or entries[0]["source"] != {"source": "local", "path": "./" + str(plugin.relative_to(ROOT))}:
        raise ValueError("Marketplace must point to this repository's plugin")


def write_zip(path, files):
    # Stable metadata makes archives reproducible for a given set of source files.
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, content)


def build_archives(destination):
    manifest = load_manifest()
    plugin = inside_root(manifest["installation"]["plugin_path"])
    runtime = inside_root(manifest["installation"]["runtime_path"])
    destination.mkdir(parents=True, exist_ok=True)
    skill_zip = destination / "xiaoguang-humanizer-skill.zip"
    plugin_zip = destination / "xiaoguang-humanizer-plugin.zip"
    write_zip(skill_zip, {str(Path(manifest["id"]) / p.relative_to(runtime)): p.read_bytes()
                         for p in runtime.rglob("*") if p.is_file()})
    write_zip(plugin_zip, {str(p.relative_to(plugin)): p.read_bytes()
                          for p in plugin.rglob("*") if p.is_file()})
    # Retain earlier export URLs for users who already rely on them.
    exports = []
    for filename in ("xiaoguang-humanizer-full.txt", "quick-start.zh.txt", "quick-start.en.txt"):
        path = destination / filename
        path.write_bytes((ROOT / "prompts" / filename).read_bytes())
        exports.append(path)
    assets = [skill_zip, plugin_zip, *exports]
    (destination / "SHA256SUMS.txt").write_text("".join(
        f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n" for path in assets))
    return assets


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check generated plugin files without writing")
    parser.add_argument("--output-dir", type=Path, help="Also build release archives in this directory")
    args = parser.parse_args()
    if args.check and args.output_dir:
        parser.error("--check cannot be combined with --output-dir")
    if not args.check:
        for path, content in expected_files().items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)
    check_distribution()
    print("Native skill, plugin, and marketplace are consistent.")
    if args.output_dir:
        for path in build_archives(args.output_dir):
            print(f"Built {path.name} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
