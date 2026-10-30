# 小光Humanizer

给你的 Agent 装上中英文写作编辑技能。改掉空话、套话和翻译腔，保留原意与作者的语气。

安装后，直接说“用小光Humanizer改这段文字”。技能保存在你选择的个人技能库或项目中，后续会话可以继续调用。

[English](README.en.md) · [下载技能包](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-skill.zip) · [各平台安装步骤](docs/platform-guide.md) · [给 Agent 的安装入口](INSTALL.md)

<a id="复制到聊天框直接用"></a>

## 交给你的 Agent 安装

把下面这段发给能读取仓库、安装技能的 Agent：

```text
请学习并安装小光Humanizer：
https://github.com/ArB1t3r/xiaoguang-humanizer

先阅读 INSTALL.md，按当前环境支持的方式，将完整技能安装到我的个人技能库，供以后新会话调用。
保留 SKILL.md 和它引用的全部规则、例子与资料；已有同名技能时先检查版本和本地修改。
安装后检查宿主能否发现技能，告诉我安装位置、版本和调用方式。
能验证新会话调用时请验证；做不到就明确告诉我还需完成哪一步。
```

Agent 会按[安装入口](INSTALL.md)处理完整技能包。需要手动上传的平台，下载上方 ZIP，按下面的步骤导入即可。

## 你用哪个平台？

| 环境 | 安装方式 | 以后怎么用 |
|---|---|---|
| **Codex** | 把安装请求发给 Codex，安装到个人技能目录。[步骤](docs/platform-guide.md#codex) | 输入 `$xiaoguang-humanizer`，再附上原文 |
| **Claude Code** | 把安装请求发给 Claude Code。[步骤](docs/platform-guide.md#claude-code) | 输入 `/xiaoguang-humanizer`，再附上原文 |
| **Cursor** | 让 Agent 将完整技能保存到个人或项目技能目录。[步骤](docs/platform-guide.md#cursor) | 输入 `/`，选择小光Humanizer |
| **WorkBuddy** | “技能 → 添加技能 → 上传技能”，选择技能 ZIP。[步骤](docs/platform-guide.md#workbuddy) | 在新任务中选择技能，或要求使用小光Humanizer |
| **豆包工作** | 在“技能·连接器·伙伴”中导入本地技能文件。[步骤](docs/platform-guide.md#doubao) | 在新任务的“更多技能”中选择小光Humanizer |
| **Claude / Cowork** | “Customize → Skills → + Create skill → Upload a skill”，上传技能 ZIP。[步骤](docs/platform-guide.md#claude) | 启用后在新对话中要求使用小光Humanizer |
| **ChatGPT** | 桌面端可加载本地技能或本仓库插件；网页端的工作区插件需管理员导入。[步骤](docs/platform-guide.md#chatgpt) | 安装后输入 `@` 选择技能 |

ChatGPT、豆包的普通聊天窗口与支持技能的工作环境有所不同。请按实际可见的技能或插件入口安装；没有入口时，见平台说明。

## 装好后，怎么用？

新建一个会话，选择已安装的技能，再发送：

```text
用小光Humanizer改写下面这段，保留原意，只给最终稿：

在快速变化的时代，沟通的重要性不言而喻。值得注意的是，周会从周四改到周五，地点不变。让我们共同开启高效协作的新篇章。
```

改写示例：

> 周会从周四改到周五，地点不变。

不需要重新粘贴规则。想少改一点，就加“轻改，保留结构和语气”；也可以要求深改、只诊断、保持正式或输出中英双语。

确认安装时，看两件事：技能列表中能找到它；新会话中能调用它。只回复“我已学会”还不足以说明安装完成。不同模型的改写效果会有差异，请核对数字、条件和原意。

## 技能里有什么？

- `SKILL.md`：适用任务、编辑流程、保真要求和交付约定。
- 24 类共用写作问题：每类都有判断方法、修法和中英对照例子。
- 中文、英文各 6 项专项规则，以及完整改写示例。
- 12 个检查用例，覆盖语义、双语、引文和技术内容保护。

Agent 使用时会读取主规则，再按稿件语言加载对应资料。规则整理参考了 8 个 Wikipedia 页面和 10 个公开 humanizer 技能，出处和取舍见[来源记录](references/sources.md)。

## 让 agent 自动接入

[INSTALL.md](INSTALL.md) 是安装入口，[agent.json](agent.json) 提供版本、文件路径和安装包地址，[接入文档](docs/agent-integration.md) 说明各宿主路径、加载顺序、更新和验证方法。

仓库同时提供原生 Skill 包和 ChatGPT/Codex Plugin 包，两种包装使用同一套完整规则。本项目不需要额外的模型服务或 API key；尚未上架各平台的公共技能市场。

[技能规则](SKILL.md) · [检查用例](references/evaluation-cases.md) · [MIT License](LICENSE)
