# Working with this skill repository

When a user asks you to learn, install, or adopt 小光Humanizer, follow
[INSTALL.md](INSTALL.md). Persist the complete skill in a location the host
actually discovers. Reading a README or saving a prompt in conversation memory
does not complete an installation.

For editing tasks, read [SKILL.md](SKILL.md) and its relevant language references.
Keep installation work separate from editing the user's draft.

For repository maintenance:

- Edit the root `SKILL.md`, `agents/`, and `references/` as the source of truth.
- Files under `plugins/xiaoguang-humanizer/skills/` are generated copies. Update
  them with `python3 scripts/build_distribution.py`; do not edit them separately.
- After changing rules or versions, run `python3 scripts/build_portable.py` and
  `python3 scripts/build_distribution.py`, then `python3 scripts/validate.py`.
- Keep README onboarding about persistent installation and later invocation.
  Prompt exports remain compatibility resources, not installation paths.
- Distinguish file/package checks, host discovery, and an actual fresh-session
  rewrite when reporting validation. Do not claim a platform was tested without
  observing it.
