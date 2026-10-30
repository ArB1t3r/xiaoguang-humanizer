# 把小光Humanizer装进你的 Agent

先[下载技能 ZIP](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-skill.zip)，或把[首页的安装请求](../README.md#交给你的-agent-安装)发给 Agent。安装时保留整个 `xiaoguang-humanizer` 文件夹，里面的规则和例子需要一起加载。

<a id="codex"></a>

## Codex

1. 把首页的安装请求发给 Codex。它可用已有的技能安装器，或将完整技能目录保存到个人技能库。
2. 输入 `$` 或打开技能列表，确认能找到 `xiaoguang-humanizer`。未出现时新开会话或重启 Codex。
3. 新会话输入 `$xiaoguang-humanizer`，再附上原文。

当前文档列出的个人技能目录是 `~/.agents/skills/`，项目目录是 `.agents/skills/`。已有环境可能由安装器管理其他受支持位置；让 Agent 检查实际加载位置，避免重复安装。命令示例见[技术接入说明](agent-integration.md#local-installation)。[官方技能文档](https://learn.chatgpt.com/docs/build-skills)

<a id="claude-code"></a>

## Claude Code

1. 把首页的安装请求发给 Claude Code，让它保存到个人技能库。
2. 新会话输入 `/xiaoguang-humanizer` 并附上原文。

个人技能路径为 `~/.claude/skills/xiaoguang-humanizer/`，项目路径为 `.claude/skills/xiaoguang-humanizer/`。本机目录的安装范围是本机；Cowork 和云端会话请走下面的 Claude 账号技能上传方式。[官方说明](https://code.claude.com/docs/en/skills)

<a id="cursor"></a>

## Cursor

1. 把首页的安装请求发给 Cursor Agent，让它将完整技能保存到 `~/.cursor/skills/xiaoguang-humanizer/`；只给当前项目用时保存到 `.cursor/skills/xiaoguang-humanizer/`。
2. 在新会话里输入 `/`，搜索并选择 `xiaoguang-humanizer`，再发送原文。

这里使用本地技能目录。Cursor 的“从 GitHub 仓库导入”界面另有插件市场格式要求，不要把两种入口混用。本地个人技能也不会自动覆盖所有云端或远程环境。[官方技能文档](https://cursor.com/docs/skills)

<a id="workbuddy"></a>

## WorkBuddy

1. 下载上方技能 ZIP，保留压缩包格式。
2. 打开“专家·技能·连接器 → 技能”，选择“添加技能 → 上传技能”。
3. 选择 ZIP，导入后在“已安装”里确认出现小光Humanizer，并保持启用。
4. 新建任务，选择该技能或发送“使用小光Humanizer改写下面文字”，再附原文。

本项目通过自带技能包导入，尚未发布到 WorkBuddy 技能市场。找不到技能时，先检查“已安装”和启用状态。[官方安装说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)

<a id="doubao"></a>

## 豆包工作

1. 进入**豆包工作**中支持技能管理的界面，打开“技能·连接器·伙伴”。
2. 在技能管理中找到本地技能导入入口。下载技能 ZIP；按界面要求上传压缩包，或先解压后选择整个 `xiaoguang-humanizer` 文件夹。
3. 导入后确认技能列表中出现小光Humanizer。
4. 在新任务的“更多技能”中选择它，再发送原文。

飞书官方介绍确认豆包工作支持自定义技能和本地技能文件导入；具体按钮与可用入口以当前客户端、账号和企业配置为准。若只有普通聊天界面，先进入豆包工作的技能管理环境。[官方功能说明](https://www.feishu.cn/content/article/7677519271848610746)

<a id="claude"></a>

## Claude / Cowork

1. 在 Claude 中打开 **Customize → Skills**。
2. 点击 **+ → + Create skill → Upload a skill**，上传技能 ZIP。
3. 确认技能出现在列表中并启用。
4. 新开对话，要求使用小光Humanizer，再发送原文。账号里启用的技能也用于相应的 Cowork 会话。

如果看不到 Skills，检查代码执行与文件创建能力是否已开启；团队环境还受管理员设置影响。[官方安装说明](https://support.claude.com/en/articles/12512180-use-skills-in-claude)

<a id="chatgpt"></a>

## ChatGPT

**桌面端的本地工作环境：** 把首页的安装请求交给具备本地文件权限的 Agent。它可以按宿主支持的方式安装独立技能，或注册本仓库附带的插件市场。安装后在技能或插件列表中确认，再开新会话输入 `@` 选择小光Humanizer。独立技能与插件的可用范围见[官方技能说明](https://learn.chatgpt.com/docs/build-skills)。

本仓库已经包含插件和市场清单。如果 Agent 选择插件路线，可让它按[技术接入说明](agent-integration.md#chatgpt-plugin)添加市场；在插件目录中选择“小光Skills”来源，安装小光Humanizer。添加市场后可能需要重启桌面端。

**网页端或手机端的工作区：** 由有权限的管理员导入本仓库插件：

1. 打开 **Admin → Plugins → Add → Import marketplace**。
2. Source 填 `https://github.com/ArB1t3r/xiaoguang-humanizer`，Path 留空；要固定版本可填写发布标签。
3. 导入后为相应成员开放插件安装。
4. 成员在插件目录安装小光Humanizer，再开新对话，通过 `@` 选择。

这个入口需要工作区管理员权限。本项目尚未上架公共插件目录；没有本地安装或工作区导入入口的账号，目前不能按本指南直接安装。[官方 GitHub 导入说明](https://learn.chatgpt.com/docs/enterprise/plugin-management)

## 确认它真的装好了

1. **文件或管理器记录存在。** 能找到小光Humanizer的技能条目，或 `xiaoguang-humanizer/SKILL.md` 和 `references/`。
2. **宿主能发现。** 它出现在技能选择器中，或 Agent 能从技能目录读取它。
3. **新会话能调用。** 不粘贴规则，只选择技能并发一段原文。试改中文和英文，检查日期、数字、条件与原意是否保留。

只完成下载或只说“学会了”时，安装还没有验证完。如果当前 Agent 无法替你检查新会话，请自己完成第 3 步。[可直接使用的检查样例](agent-integration.md#verify-installation)

## 更新与卸载

更新时，让 Agent 比较已安装版本与仓库版本，保留你的本地修改，再按原安装方式更新。界面上传的技能使用该平台的更新或重新导入入口。卸载也使用原平台的技能管理器；目录安装只移除对应的技能文件夹。

以上路径于 2026-10-30 核对官方文档。包结构和规则完整性由仓库检查验证；除实际记录过的本地检查外，不能视为各平台均已完成登录后的端到端实测。
