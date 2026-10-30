# 小光Humanizer · Xiaoguang Humanizer

Give your agent a reusable editing skill for Chinese and English. Remove filler, stock phrases, and awkward translations while preserving meaning and voice.

Install it in your personal skill library or a project, then ask your agent to use Xiaoguang Humanizer whenever you need an edit.

[中文](README.md) · [Download the skill](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-skill.zip) · [Platform setup](docs/platform-guide.md) · [Agent installation entrypoint](INSTALL.md)

<a id="copy-paste-and-start"></a>

## Give this to your agent

Send this request to an agent that can read repositories and install skills:

```text
Learn and install Xiaoguang Humanizer:
https://github.com/ArB1t3r/xiaoguang-humanizer

Read INSTALL.md first. Use this host's supported installation mechanism to add the complete skill to my personal skill library for future sessions.
Keep SKILL.md and all its referenced rules, examples, and resources. Check versions and local edits before replacing an existing installation.
Verify that the host can discover the skill, then report its location, version, and invocation method.
Test it in a fresh session when possible. Otherwise, tell me exactly which verification step remains.
```

The [installation entrypoint](INSTALL.md) tells the agent how to persist the complete package. For apps with an upload interface, download the skill ZIP above and import it through their skill manager.

## Choose your app

| Environment | Install | Invoke later |
|---|---|---|
| **Codex** | Give Codex the installation request. Use its personal skill directory. [Details](docs/platform-guide.md#codex) | `$xiaoguang-humanizer`, followed by the draft |
| **Claude Code** | Give Claude Code the installation request. [Details](docs/platform-guide.md#claude-code) | `/xiaoguang-humanizer`, followed by the draft |
| **Cursor** | Ask Agent to save the complete skill in a personal or project skill directory. [Details](docs/platform-guide.md#cursor) | Type `/` and select the skill |
| **WorkBuddy** | Skills → Add skill → Upload skill. Select the skill ZIP. [Details](docs/platform-guide.md#workbuddy) | Select the skill in a new task or ask for it by name |
| **Doubao Work** | Import the local skill files through its Skills · Connectors · Partners area. [Details](docs/platform-guide.md#doubao) | Select it from More skills in a new task |
| **Claude / Cowork** | Customize → Skills → + Create skill → Upload a skill. Upload the ZIP. [Details](docs/platform-guide.md#claude) | Enable it, then ask for it in a new conversation |
| **ChatGPT** | Use a local skill or this repository's plugin on desktop. A workspace admin can import the plugin for web use. [Details](docs/platform-guide.md#chatgpt) | Type `@` to select the installed skill |

Ordinary chats and skill-enabled work environments have different capabilities. Follow the route available in your app; the platform guide explains what to do if the skill or plugin entrypoint is missing.

## Use the installed skill

Start a new conversation, select the skill, and send:

```text
Use Xiaoguang Humanizer to rewrite this. Preserve meaning and return only the final text:

It is worth noting that registration closes Friday. In other words, Friday is the registration deadline.
```

Example result:

> Registration closes Friday.

You do not need to paste the editing rules again. Ask for a light edit, a deep rewrite, an audit, formal language, or Chinese and English versions.

Check that the host lists the skill and can invoke it in a fresh conversation. An “I have learned it” reply alone does not establish installation. Results vary by model; check facts and meaning before using the rewrite.

## What the skill contains

- `SKILL.md`: task scope, editing workflow, meaning preservation, and delivery rules.
- 24 shared writing patterns, each with a remedy and Chinese/English examples.
- Six additional rules for each language, with complete rewrite examples.
- 12 evaluation cases covering meaning, bilingual alignment, quotations, and technical content.

The agent reads the main instructions and loads the references for the draft's language. We drew on eight Wikipedia pages and ten public humanizer skills; see [sources and design decisions](references/sources.md).

## Let an agent connect automatically

Start with [INSTALL.md](INSTALL.md). [agent.json](agent.json) lists the version, package paths, and download URLs. The [integration guide](docs/agent-integration.md) covers host directories, loading order, updates, and verification.

The repository provides a native Skill package and a ChatGPT/Codex Plugin package built from the same complete rules. No additional model service or API key is required. The project is not listed in the platforms' public skill marketplaces.

[Skill rules](SKILL.md) · [Evaluation cases](references/evaluation-cases.md) · [MIT License](LICENSE)
