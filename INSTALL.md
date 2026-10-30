# Install 小光Humanizer / 安装入口

This is a reusable Agent Skill. If the user asks you to “learn this skill”,
install its complete files so the host can discover it in later sessions.
Do not reduce the skill to a summary or treat an acknowledgment as installation.

用户把仓库交给你“学习”时，请完成可复用的技能安装。使用宿主已有的 Skill 或
Plugin 机制，保留完整规则和引用文件。

## 1. Identify the host and scope

Read [agent.json](agent.json) and the matching section of the
[platform guide](docs/platform-guide.md). Determine which product, local/cloud
environment, and installation mechanism you can actually use.

Honor the user's requested scope. “Install into my personal skill library so I
can reuse it” authorizes the host's user-level installation. For a project-only
request, use that project's skill directory. If scope is unspecified, use the
current project and report that scope. Do not install into unrelated agents.

## 2. Acquire and persist the full package

Choose the host's supported route:

- **Local skill directories:** copy the complete directory at
  `plugins/xiaoguang-humanizer/skills/xiaoguang-humanizer/` into the host's
  supported skills location, or use its installer. See the commands and paths
  in [agent integration](docs/agent-integration.md#local-installation).
- **Skill upload UI:** download the `xiaoguang-humanizer-skill.zip` release asset
  and import it through the host's skill manager. Use authorized UI tools when
  available; otherwise give the user the exact remaining upload step.
- **ChatGPT/Codex plugin distribution:** this repository includes
  `.agents/plugins/marketplace.json` and the plugin at
  `plugins/xiaoguang-humanizer/`. Follow the matching local or workspace route
  in [the platform guide](docs/platform-guide.md#chatgpt).

The runtime directory contains `SKILL.md`, language references, examples,
provenance, and UI metadata. Copy it as a unit. Keep it in a durable location,
not a temporary checkout that will disappear. Do not copy the whole repository
into a skill directory: it also contains a generated plugin copy.

If the same skill is already installed, inspect its version and local changes.
Keep an identical installation. Back up user edits before a requested update;
do not create a second copy under another search path. Respect any host-managed
installation policy. This package needs no MCP server, API key, or new model.

If the current host cannot persist or import skills, report the missing
capability and the supported installation route. Do not silently substitute
the legacy quick prompt and call it installed.

## 3. Verify what actually works

Follow [installation verification](docs/agent-integration.md#verify-installation):

1. Confirm the installed package and all referenced editing files exist.
2. Confirm the host lists or discovers `xiaoguang-humanizer`, reloading or
   starting a new session when required.
3. In a fresh session, invoke the installed skill on the supplied Chinese and
   English smoke cases. Do not paste the editing rules into that session.

Use a fresh session only when your tools and user authorization allow it. If
you cannot create or inspect one, give the user the test request and mark the
fresh-session check as pending. Do not fabricate that result.

## 4. Report installation

Return the version, host, installed path or skill-manager entry, scope,
invocation method, and which checks actually passed. Distinguish “files
installed”, “host discovered the skill”, and “fresh-session invocation passed”.
If a user action is still needed, name it precisely.

“Learning” here means installing reusable instructions and references. It does
not mean training the underlying model or relying on chat memory.
