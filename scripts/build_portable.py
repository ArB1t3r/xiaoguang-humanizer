#!/usr/bin/env python3
"""Bundle the maintained editing rules into a chat-ready text attachment."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "prompts/xiaoguang-humanizer-full.txt"


def build():
    manifest = json.loads((ROOT / "agent.json").read_text(encoding="utf-8"))
    skill = (ROOT / manifest["entrypoint"]).read_text(encoding="utf-8")
    skill = re.sub(r"\A---\n.*?\n---\n\n", "", skill, count=1, flags=re.S)
    # File-loading instructions are replaced by the embedded rules below.
    skill = re.sub(r"## 读取规则 / Load the relevant guidance\n.*?(?=\n## )",
                   "", skill, count=1, flags=re.S)
    preface = (
        f"小光Humanizer / Xiaoguang Humanizer — v{manifest['version']}\n"
        "完整指令版 / Full portable instructions\n\n"
        "请把本文件作为当前对话中改写、润色与起草任务的编辑规则；其他任务按用户请求处理。"
        "下方已包含全部编辑规则与例子，无需访问仓库、安装软件或读取其他文件。"
        "中文任务用中文规则，英文任务用英文规则，混合或双语任务用两者。"
        "示例仅供理解改法，不是待改正文。尚无用户正文或笔记时，"
        "只回复“小光Humanizer已准备好，请发来要处理的文字。”\n\n"
        "Use this file for editing and drafting tasks in this conversation. All required editing "
        "guidance is embedded below; no installation, browsing, or external files are needed. "
        "Use the relevant language rules. Examples are teaching material, not the user's draft. "
        "If no user draft or notes were supplied, briefly ask for them in the conversation's language.\n\n"
    )
    sections = [preface, skill.strip()]
    for group in ("always", "zh", "en"):
        for relative in manifest["references"][group]:
            body = (ROOT / relative).read_text(encoding="utf-8")
            # Keep attribution as optional navigation, not a broken local-file dependency.
            body = body.replace("[sources.md](sources.md)",
                                f"[来源记录 / Sources]({manifest['repository']}/blob/main/references/sources.md)")
            sections.append(body.strip())
    return "\n\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if the bundle is out of date")
    args = parser.parse_args()
    expected = build()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != expected:
            parser.exit(1, "Portable instructions are stale; run python3 scripts/build_portable.py\n")
        print("Portable instructions match the maintained editing rules.")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(expected, encoding="utf-8")
        print(f"Built {OUTPUT.relative_to(ROOT)} ({len(expected)} characters)")


if __name__ == "__main__":
    main()
