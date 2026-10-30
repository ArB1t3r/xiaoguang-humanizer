# 在你常用的 AI 里使用小光Humanizer

第一次使用，直接复制[首页的快用指令](../README.md#复制到聊天框直接用)，发进 AI 聊天框，再发原文。下面介绍如何复用。

<a id="chatgpt"></a>

## ChatGPT

**马上用：** 打开 [ChatGPT](https://chatgpt.com/)，新建对话，先发送[快用指令](../prompts/quick-start.zh.txt)，收到准备好的回复后再发正文。

**想有一个专用写作空间：**

1. 在 ChatGPT 新建项目，命名为“小光Humanizer”。
2. 打开该项目的指令设置，把快用指令全文粘贴进去并保存。
3. 在这个项目里新建对话，发送“请用小光Humanizer改写下面文字”，后面附上原文。

需要全部规则和例子时，把[完整指令 TXT](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-full.txt)加入项目文件，并在项目指令末尾补上：

```text
进行改写任务前，读取项目文件 xiaoguang-humanizer-full.txt 中的编辑规则。
如果文件无法读取，使用本项目保存的快用规则，并简短告知我。
```

项目指令适用于该项目内的对话。没有项目入口时，直接使用普通对话。项目功能说明见 [ChatGPT 官方文档](https://learn.chatgpt.com/docs/projects)。

<a id="doubao"></a>

## 豆包

1. 打开[豆包](https://www.doubao.com/chat/)或豆包 App，开始一个新对话。
2. 将[快用指令](../prompts/quick-start.zh.txt)全文复制到输入框，发送。
3. 收到准备好的回复后，发送要处理的文字。后续可以继续在这个对话里改稿。

例如：

```text
轻改，保留我的语气，只给最终稿：
把这里换成你的文字
```

可以将对话命名为“小光Humanizer”以便找回（若当前版本提供重命名）。新开对话时重新粘贴指令。这个用法不依赖智能体创建入口，也不要求豆包能打开 GitHub。

若当前界面支持 TXT 附件，也可上传[完整指令](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-full.txt)，并让它先读取规则。看不到上传入口或文件读不出时，继续用快用版即可。

<a id="workbuddy"></a>

## WorkBuddy

**马上用：** 在 [WorkBuddy](https://www.codebuddy.cn/work/)新建任务，粘贴[快用指令](../prompts/quick-start.zh.txt)，再发正文。只需要当前对话改稿时，到这里就够了。

**保存为可重复调用的技能：**

1. [下载小光Humanizer技能包](https://github.com/ArB1t3r/xiaoguang-humanizer/releases/latest/download/xiaoguang-humanizer-skill.zip)，保留 ZIP 格式。如果浏览器自动解压，请保留或重新下载原 ZIP。
2. 在 WorkBuddy 左侧打开“专家·技能·连接器”，进入“技能”。
3. 点击“添加技能 → 上传技能”，选择下载的 ZIP 文件。
4. 在“已安装”里确认出现小光Humanizer（或标识 `xiaoguang-humanizer`），并保持启用。
5. 新建任务，发送：

```text
请使用已安装的小光Humanizer，改写下面文字，保留原意，只给最终稿：
值得注意的是，登记截至周五。
```

期望得到“登记截至周五。”若它说找不到技能，先检查“已安装”和启用状态。

这是通过自带 ZIP 导入的安装方式；本项目尚未发布到 WorkBuddy 技能市场。WorkBuddy 官方文档说明，对话内搜索安装面向市场内技能，自带技能包使用上传入口。菜单和可用功能以你使用的版本为准。见[官方安装说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)和[技能包结构](https://open.workbuddy.cn/docs/skill)。

## 常见情况

| 遇到的情况 | 怎么处理 |
|---|---|
| AI 说打不开 GitHub | 复制首页的完整快用指令给它，不要只发网址。 |
| 不知道怎么复制文件 | 用首页文本框的复制按钮，或打开 TXT 后全选复制。手机可长按文字选择。 |
| 提示输入太长 | 改用快用版；长文章按章节分批发，每批都附上必要上下文。 |
| 只说“收到”，没有改写 | 指令发送后，还需要发你自己的原文。 |
| 新对话忘记规则 | 重新粘贴指令，或回到已经配置的项目／已安装技能环境。 |
| 改得太多 | 说“轻改，保留结构和语气”，并指出必须保留的句子。 |
| 对话很长后开始不按规则写 | 再发一次快用指令与当前原文，或在专用项目里开新对话。 |

快用版、完整指令版和技能包都支持中文、英文与中英混合稿。快用版压缩了规则；完整指令版和技能包包含相同的全部编辑规则与教学例子，技能包另有来源、检查用例和接入文档。

本指南于 2026-10-30 核对 ChatGPT 和 WorkBuddy 官方文档；豆包提供普通对话粘贴方案。已检查文件与包结构，尚未在三个平台逐一完成登录后的端到端实测。
