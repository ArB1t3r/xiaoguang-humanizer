# 研究来源与设计取舍 / Research and design decisions

研究日期：2026-10-30（Asia/Shanghai）。收录 8 个 Wikipedia 页面，比较 10 个公开 humanizer／去 AI 味技能。目标是把 AI 写作特征转成我们的编辑规则，交付可直接运行的中英双语技能。

比较依据是实际读取的 SKILL.md 入口及相关参考文件，不是搜索摘要、星标排行或对第三方技能的效果排名。GitHub 来源固定到本次取得的 commit；下载文件的 SHA-256 与链接保存在 [source-manifest.json](source-manifest.json)。没有运行第三方代码或安装第三方技能。

## Wikipedia 页面

辨识页提供观察线索，我们将其中可迁移的写作问题重新组织为编辑动作。Wikipedia 的页面格式要求不直接套到邮件、博客或技术文档。

| ID | 页面 | 页面性质 | 在本技能中的用途 |
|---|---|---|---|
| W1 | [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) · [本次版本](https://en.wikipedia.org/w/index.php?oldid=1382688615) | 英文专题建议页 | 共用内容、句型、格式与引用问题的主要线索。 |
| W2 | [Wikipedia:AI生成文的特徵](https://zh.wikipedia.org/wiki/Wikipedia:AI生成文的特徵) · [本次版本](https://zh.wikipedia.org/w/index.php?oldid=95337857) | 中文信息页 | 中文用法及过度防御、重复表述等补充；不能假定与英文版同步。 |
| W3 | [Wikipedia:Signs of AI use in comments](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_use_in_comments) | 英文专题建议页 | 评论中的泛化保证、过度程序化说明与交流套语。 |
| W4 | [Wikipedia:WikiProject AI Cleanup/Guide and resources](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup/Guide) | 英文专题操作建议页 | 提供清理工作流程与来源核对背景。 |
| W5 | [Wikipedia:Large language models](https://en.wikipedia.org/wiki/Wikipedia:Large_language_models) | 英文信息页 | 说明虚构、来源错配与内容核验问题，供保真规则参考。 |
| W6 | [Artificial intelligence content detection](https://en.wikipedia.org/wiki/Artificial_intelligence_content_detection) | 英文百科条目 | 理解检测方式和误差；不作为本技能的评分标准。 |
| W7 | [人工智能内容检测](https://zh.wikipedia.org/wiki/人工智能内容检测) | 中文百科条目 | 中文阅读入口，部分研究来自较早年份，不能当成当前工具排名。 |
| W8 | [Wikipedia:Artificial intelligence](https://en.wikipedia.org/wiki/Wikipedia:Artificial_intelligence) | 英文信息索引页 | 追踪 Wikipedia 内相关页面和规则变化，维护时使用。 |

W1、W2 并非通用写作规范，也不是本技能的操作指令。此处按用户要求，把可用的观察反向转化成写作约束；具体怎么改、中文怎样写、如何保留意思，是本技能自己的设计。W6、W7 的检测讨论仅用于解释为何不输出伪精确 AI 概率，日常改写不附这类说明。

## 10 个技能的比较

| ID / 项目 | 已读版本 | 值得借鉴 | 我们的取舍 |
|---|---|---|---|
| H1 · [blader/humanizer](https://github.com/blader/humanizer/blob/0ef9fe5bc3572734fd3ae6c448fe00a30cd5dcf0/SKILL.md) | 3.1.0 · 0ef9fe5b | 把常见 AI 写法整理成可执行编辑模式，并提供复核流程。 | 采用段落与句型层面的清理；改为默认只交付最终稿。取消无样本时一律禁破折号的规定。 |
| H2 · [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh/blob/f4518a8eab97b8bfebc66a89d34320a89bef6930/SKILL.md) | 2026-09-23 revision · f4518a8e | 中文规则保留主张、限定和语域；区分真对比与空对比。 | 采用信息保真检查；补齐英文专项和双语一致性检查。 |
| H3 · [hardikpandya/stop-slop](https://github.com/hardikpandya/stop-slop/blob/8da1f030185bdfe8471220585162991eaeb970e9/SKILL.md) | 固定 commit，入口未标版本 · 8da1f030 | 短入口配独立短语、结构、例子文件；强调直接表达。 | 采用紧凑入口和结构修复；不采用删除所有副词、禁止所有被动句及机械评分门槛。 |
| H4 · [RobinZorro86/humanizer-zh-plus](https://github.com/RobinZorro86/humanizer-zh-plus/blob/f450953d241cb40c7bcc9ccc9b82a56ffa21a088/SKILL.md) | 2.2.0 · f450953d | 在上游模式之外补充中文四字格、书面套语和节奏问题。 | 采用中文专项扫描；不全局接管所有聊天输出，不以“两项优于三项”删掉信息。 |
| H5 · [ai-zixun/humanizer-zh](https://github.com/ai-zixun/humanizer-zh/blob/f75f1ac9735c4f10da1bba0148e0ea7228c5c3b3/SKILL.md) | 固定 commit，入口未标版本 · f75f1ac9 | 重点处理翻译腔、文章主线、中文节奏与可选声音样本。 | 采用中文句法和篇章推进检查；不默认推荐名人声音，不把 PR 固定翻译为代码审查。 |
| H6 · [keez97/humanizer](https://github.com/keez97/humanizer/blob/2d9a116fa9caee2c3466a7c7d419cbe02b35a470/SKILL.md) | 2.9.0 · 2d9a116f | 按篇章、句子、词汇分层；区分场景和修改力度。 | 采用先结构后词句的顺序；不要求故意不通顺、无关插话或补作者立场。其检测器小样本结论未当成普遍规律。 |
| H7 · [Aboudjem/humanizer-skill](https://github.com/Aboudjem/humanizer-skill/blob/a58df065367550b6ce40ff3f648335018d8e0589/skills/humanizer/SKILL.md) | 入口自述 55 patterns · a58df065 | 模式覆盖较广，有诊断、改写、文件模式和语气选择。 | 采用模式分层与场景选择；不照搬句长配额、困惑度目标、AI 百分比或未经核实的具体化。 |
| H8 · [quqxui/context-aware-humanizer](https://github.com/quqxui/context-aware-humanizer/blob/e99e02e3d469d5f9e6c1a387f9e3cb2fb41dc610/SKILL.md) | 固定 commit，入口未标版本 · e99e02e3 | 按语言和写作场景分流；个人声音可独立建档。 | 采用语言分流和语域意识；本版简化为中英两份指南，普通改写无需档案或问卷。 |
| H9 · [thebpandey/write-like-a-human](https://github.com/thebpandey/write-like-a-human/blob/21cb119edc4570211209eb501a62abb498e440bc/SKILL.md) | 固定 commit，入口未标版本 · 21cb119e | 把起草、改写、声音样本与发布渠道组织在一起，提示避免替换后再次模板化。 | 采用检查新模板残留的思路；不强制声音菜单、段落比例、短长句配额或每篇加个人反应。 |
| H10 · [lynote-ai/humanize-text-skill](https://github.com/lynote-ai/humanize-text-skill/blob/9359e17a8d7d54263adb726f4e6c71e0b0940651/SKILL.md) | 0.1.0 · 9359e17a | 分离保护片段、场景规则与一次残留检查，兼顾中英文。 | 采用最终残留检查和文件保护；不把每个常用英文词作为无条件禁词。 |

这些项目并非十份独立证据。多份技能沿用了 Wikipedia 或 blader/humanizer；重复出现的规则不能按项目数量重复计权。上表记录设计启发与具体取舍，没有宣称经过跨模型、跨文体效果验证。

## 我们自己的结构

入口只保留任务约定、改写顺序、保真要求和交付方式。共用库包含 24 类反模式，各有中文和英文例子；中文和英文各有 6 项专项规则与一个完整改写示范。语言规则与共用规则有交叉，不称为 36 个互相独立的检测信号。

处理顺序是：实际内容 → 篇章结构 → 句子与用词 → 残留复核。默认直接交付最终稿；需要诊断或对照时再展开。允许按要求轻改或深改，双语输出按事实和行动要求对齐，句式分别自然表达。

| 规则组 | 参考线索 | 本版新增的执行设计 |
|---|---|---|
| C01–C10：开场、论证、修辞、宣传腔 | W1、W2、H1、H3、H5、H6、H7 | 合并重叠模式；每个例子只用原稿已有内容完成改写 |
| C11–C15：归因、关系、限定、句法、术语 | W1、W5、H2、H5、H10 | 把“事实不变”落实到角色、时间、条件、否定、完成状态与来源 |
| C16–C20：格式、助手话术、过程和引用 | W1、W3、H1、H2、H7、H10 | 区分正文与引用／代码／URL；保留文档必要结构 |
| C21：刻意扮人 | 对 H4、H6、H7、H9 的批判性比较 | 不新增经历、情绪或意见；通过已有语气与节奏恢复声音 |
| C22–C24：结尾、防御性说明、空解读 | W1、W2、W3、H1、H3 | 单独复核段末与结尾；去掉无实际作用的限定和保证 |
| Z01–Z06：中文规则 | W2、H2、H4、H5、H8、H10 | 处理官样词组、长定语、代词复读、伪网感、通稿立意与术语稳定 |
| E01–E06：英文规则 | W1、H1、H3、H7、H8 | 直接谓语、语境词表、英文翻译腔、语域、排版与读者上下文 |
| 双语一致性与评估用例 | H2、H8、H10 及本任务需求 | 用相同事实核对两种语言，加入易丢条件、真实三项和语气强度测试 |

## 明确舍弃的实现方式

- 不靠故意写错、随机换生僻词、硬凑长短句来制造人味。它们容易形成另一种可预测模板。
- 不以去 AI 味为由新增故事、数据、性能收益或作者立场。具体化必须来自原文或用户材料。
- 不把所有副词、被动句、破折号或三项列举一律删除。消除模板的用法，保留真正承载信息的形式。
- 不把 Wikipedia 特有的 Markdown、编辑摘要、收录标准要求照搬到所有写作场景。
- 不默认让技能接管所有聊天、读私人历史、保存风格档案或上传检测服务。普通改写只处理给定材料。

## 来源与许可记录

本技能的说明、例子和评估材料为本次重新编写；没有复制第三方完整技能或 Wikipedia 的示例段落。Wikipedia 页面页脚标示 CC BY-SA 4.0，作者归属可通过各页面历史查询。若今后加入原文摘录或较大篇幅改编，应保留对应署名与许可。

本次读取的九个项目含独立 LICENSE 文件，内容为 MIT；keez97/humanizer 的 GitHub 元数据为 NOASSERTION，但已读取文件中的 MIT 文本及两位作者署名。thebpandey/write-like-a-human 的 SKILL.md 声明 MIT，本次树中未找到独立 LICENSE；仅比较设计，不复制其正文。具体元数据与读取记录见 manifest。

源文件不会在运行技能时自动下载或执行。本版依赖本地 Markdown 指令，没有第三方服务依赖。

## 验证范围

结构检查验证入口 frontmatter、相对链接及文件完整性。另提供 12 个原创回归用例和一次编写者手工试改记录。它们用于检查可观察的语义保真、语言选择和编辑范围，不是检测器成绩；未进行独立模型盲测或真实用户盲评。
