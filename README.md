# 小光Humanizer

去掉中英文里的 AI 味，保留原意和作者声音。

[English](README.en.md) · [技能规则](SKILL.md) · [Agent 接入](docs/agent-integration.md) · [来源](references/sources.md)

处理空泛开场、假对比、机械排比、重复解释、翻译腔和模板结尾。先调整结构，再改句子和用词，最后检查残留。支持中文、英文和中英混合文本，默认只给最终稿。

## 看一个例子

**改写前**

> 在快速变化的时代，沟通的重要性不言而喻。值得注意的是，周会从周四改到周五，地点不变。让我们共同开启高效协作的新篇章。

**改写后**

> 周会从周四改到周五，地点不变。

原有信息留下，空话删掉。数字、条件、引用和作者立场同样要保留。

## 安装

使用 [Skills CLI](https://github.com/vercel-labs/skills)，选择要安装到的 agent：

```bash
npx skills add ArB1t3r/xiaoguang-humanizer --skill xiaoguang-humanizer
```

安装命令需要 Node.js 22.20+。也可以下载 [Release 技能包](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest)，将整个文件夹放进你的 agent 支持的 skills 目录。

## 使用

在支持技能调用的 agent 中输入：

```text
使用 $xiaoguang-humanizer 去掉下面文字的 AI 味，保留原意，只给最终稿：

粘贴你的文字
```

也可以指定“轻改”“深改”“只诊断”“保持正式”或“输出中英双语”，并附上自己的文风样本。英文稿默认仍输出英文。

## 让 agent 自动接入

把下面这段交给你的 agent：

```text
请安装并使用小光Humanizer：
https://github.com/ArB1t3r/xiaoguang-humanizer

读取仓库的 agent.json 和 docs/agent-integration.md，
安装到当前项目适用的 skills 目录。已有同名技能时先检查版本和本地改动。
安装后读取 SKILL.md，并按输出语言加载它引用的规则。
用“值得注意的是，登记截至周五。”试改，返回结果、安装位置和版本。
```

自动化环境可指定目标 agent，以下示例安装到当前项目的 Codex：

```bash
npx --yes skills add ArB1t3r/xiaoguang-humanizer --skill xiaoguang-humanizer --agent codex --yes
```

| 入口 | 用途 |
|---|---|
| [agent.json](agent.json) | 机器可读的名称、版本、规则路径与能力清单 |
| [llms.txt](llms.txt) | 给 agent 的简短导航 |
| [SKILL.md](SKILL.md) | 实际执行的编辑规则 |
| [接入说明](docs/agent-integration.md) | 加载顺序、任务约定、固定版本与检查方法 |

这是由你的 agent 执行的文本技能，无需本项目的 API key 或服务端。检查仓库文件可运行 `python3 scripts/validate.py`，只需 Python 3.10+ 标准库。

## 内容与来源

- 24 类共用反模式，附中英前后对照。
- 中文、英文各 6 项专项规则和完整改写示例。
- 12 个回归用例，覆盖语义保真、双语对齐、引文和技术内容保护。

整理自 8 个 Wikipedia 页面与 10 个公开技能，包括 [Wikipedia 英文指南](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)、[中文指南](https://zh.wikipedia.org/wiki/Wikipedia:AI生成文的特徵)、[blader/humanizer](https://github.com/blader/humanizer)、[Humanizer-zh](https://github.com/op7418/Humanizer-zh) 和 [stop-slop](https://github.com/hardikpandya/stop-slop)。完整比较和固定版本见[来源记录](references/sources.md)。

本技能优化文字表达，不输出作者身份结论或检测器通过承诺。已有 12 个编写者手工试改用例；尚未进行独立模型盲测。

[MIT License](LICENSE) · 原创规则、例子与脚本；参考来源保留各自许可。
