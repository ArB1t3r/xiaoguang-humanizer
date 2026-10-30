# 小光Humanizer · Xiaoguang Humanizer

Remove AI writing habits from Chinese and English prose while preserving meaning and voice.

[中文](README.md) · [Skill](SKILL.md) · [Agent integration](docs/agent-integration.md) · [Sources](references/sources.md)

Edit generic openings, hollow contrasts, forced triads, repeated explanations, translation-shaped phrasing, and stock endings. Work on structure first, then sentences and wording, followed by a residue check. Return the finished text by default.

## Example

**Before**

> It is worth noting that registration closes Friday. In other words, Friday is the registration deadline.

**After**

> Registration closes Friday.

Keep the information, including material conditions, numbers, quotations, and the writer's position.

## Install

Use the [Skills CLI](https://github.com/vercel-labs/skills) and select your agent:

```bash
npx skills add ArB1t3r/xiaoguang-humanizer --skill xiaoguang-humanizer
```

The installation command requires Node.js 22.20+. Alternatively, download the [release bundle](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest) and place the complete folder in a skills directory supported by your agent.

## Use

```text
Use $xiaoguang-humanizer to remove AI writing habits from the text below.
Preserve its meaning and voice. Return only the final version.

Paste your text here.
```

Ask for a light edit, deep rewrite, audit only, formal register, or bilingual output. You can supply a writing sample. The original language is preserved unless you request translation.

## Connect an agent

Give your agent this request:

```text
Install and use Xiaoguang Humanizer:
https://github.com/ArB1t3r/xiaoguang-humanizer

Read agent.json and docs/agent-integration.md.
Install into the appropriate project skills directory.
Check versions and local edits before replacing an existing installation.
Load SKILL.md and its references for the requested output language.
Test it on “It is worth noting that registration closes Friday.”
Return the rewrite, installation location, and version.
```

For non-interactive installation into a Codex project:

```bash
npx --yes skills add ArB1t3r/xiaoguang-humanizer --skill xiaoguang-humanizer --agent codex --yes
```

- [agent.json](agent.json): machine-readable discovery metadata.
- [llms.txt](llms.txt): a small navigation index.
- [Integration guide](docs/agent-integration.md): loading order, task conventions, version pinning, and checks.

Your existing agent supplies the model. This repository requires no service account or API key of its own. Validate repository files with `python3 scripts/validate.py` using Python 3.10+ and its standard library.

## Included

24 shared editing patterns with examples in both languages, six additional language rules per language, and 12 regression cases. Language rules overlap with the shared catalog.

Research covers eight Wikipedia pages and ten public skills. See [sources and design decisions](references/sources.md) for attribution and pinned revisions. The cases include an author-run manual review; they are not an independent model benchmark. The skill does not give authorship verdicts or detector guarantees.

[MIT License](LICENSE) for original instructions, examples, and scripts. Referenced projects retain their own licenses.
