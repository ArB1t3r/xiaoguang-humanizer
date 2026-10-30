# 中文规则 / Chinese-specific editing

在共用反模式之外，处理中文自身的句法、语域和表达习惯。这六项是语言专项规则，与共用规则有交叉，不是额外的六个独立检测指标。

These six language rules supplement the shared catalog. They are editorial guidance, not six independent detection signals.

## Z01 把官样词组还原为动作 / Replace bureaucratic bundles with actions

“赋能、抓手、底层逻辑、闭环、全链路、协同联动、持续深化、全面提升”连在一起时，追问句子究竟说谁做什么。有具体动作就写动作；术语确有专业含义就保留。

When business abstractions pile up, recover the supplied actor and action. Keep terms with a real domain meaning.

前：团队将以清单为抓手，持续深化资料归档工作的协同联动。具体做法是每周五一起核对清单、补齐缺件。

后：团队每周五一起核对归档清单，补齐缺件。

不要把“赋能商家”凭空改成“让商家收入增长 30%”。缺结果就不添结果。

## Z02 拆掉英语式长定语 / Unpack translated modifier chains

处理“基于……的、面向……的、旨在……的……机制”等多层定语，把事情按中文的信息顺序说清。需要完整条件时，分成两句也保留条件。

Move stacked modifiers into clauses with a clear sequence. Preserve every condition.

前：一个由编辑部提出的、旨在减少重复登记的、基于统一表格的流程将在周一试行。

后：编辑部提出用统一表格减少重复登记，周一开始试行。

“被”字句不一律改主动。施事未知的“样本已被销毁”不能改成“实验员销毁了样本”。

## Z03 去掉机械连接与代词复读 / Repair connective and pronoun overload

不按英文连接词逐个翻成“此外、与此同时、然而、因此”。明确是并列、转折、时间还是因果，再选表达。中文主语清楚时可承接或省略，不要求每句都有“它／他们／该”。

Use connectors for actual relationships. Chinese can omit an understood subject; do not enforce an English subject in every sentence.

前：这份表格可以离线填写。此外，它会在联网后上传。与此同时，它支持手动导出。

后：这份表格可以离线填写，联网后上传，也支持手动导出。

上例“与此同时”只是列功能的连接词。原文若明确说两个事件同时发生，则必须保留同时关系。

## Z04 去掉伪网感 / Remove borrowed social-media mannerisms

不要用“家人们、谁懂啊、绝绝子、直接封神、狠狠拿捏、建议收藏、闭眼冲”自动制造亲切感。若作者原文或明确指定的声音就用这些词，按实际语气取舍；不要全篇替换成另一套口头禅。

Do not manufacture intimacy with canned internet slang. Retain an intentional voice when requested.

前：家人们谁懂啊，这个文件夹真的封神！可以按月份找发票，狠狠拿捏归档，建议收藏。

后：这个文件夹按月份整理发票，查起来方便。

不要补“我用了三个月”之类原稿没有的经历。

## Z05 终止通稿式立意 / Remove stock uplift from Chinese prose

“以……为起点、在……中实现……、不仅……更……、让……真正……”反复出现时，重写段落的实际内容。结尾不用自动上升到“人与时代”“长期主义”或“更多可能”。

Rebuild the substantive paragraph rather than moving the same grand framing into new words.

前：以此次试读为起点，我们将在沟通中建立理解，在协作中凝聚共识，让文字真正连接人心。试读会上，三位读者都说第二章难懂，编辑决定重写第二章。

后：试读会上，三位读者都说第二章难懂。编辑决定重写这一章。

有论据的立意可以保留；删的是随处可用的装饰，不是作者的实际观点。

## Z06 稳定术语、简繁与语域 / Keep terms, script, and register consistent

沿用原文简繁体和已有术语表。不要为“中文自然”硬翻 API、产品名或代码标识；不要把 PR 一概换成“代码审查”。拼写或术语身份不确定时，保留原文或查询用户给的词表。

Preserve script and established terminology. Do not invent translations or expand ambiguous abbreviations.

前：新版 SDK 提供流式输出。这个软件开发工具套件也支持取消，而这套研发工具包需要 API key。

后：新版 SDK 提供流式输出，支持取消，需要 API key。

中英混排按文档现有规范整理；不改代码、URL、版本号和专名内部空格。标点用于表达关系，不用固定数量衡量自然程度。

## 中文用词检查表 / Wording prompts

| 表达 | 优先考虑的写法 | 判断依据 |
|---|---|---|
| 在这个时间节点 | 现在／具体日期 | 是否需要保留阶段含义 |
| 对……进行评估 | 评估…… | 是否有正式术语要求 |
| 具有……的能力 | 可以…… | 是否强调能力而非实际动作 |
| 值得注意的是 | 直接陈述后面的内容 | 是否真的在提示一个易漏的例外 |
| 其核心在于／本质上 | 写出已有判断 | 是否提供了必要定义 |
| 显著提升／全面优化 | 具体变化，或保留朴素概括 | 不新增数值或未经提供的效果 |
| 综上所述／总而言之 | 直接收束，或删除重复结尾 | 长报告确实需要摘要时保留摘要功能 |

这些是编辑提示，不是无条件替换表。These are contextual prompts, not a global search-and-replace list.

## 完整例子 / Full rewrite

**原稿**

在信息爆炸的时代，清晰的说明不仅是一种能力，更是一座连接团队的桥梁。值得注意的是，这次我们围绕报销流程开展了全方位优化，实现了提速、增效与体验跃升。财务把审批从两次改为一次，周三开始试行。与此同时，超过 5000 元的申请仍需负责人签字。这并不意味着所有问题都已解决，需要谨慎理解。两周后，财务会收集反馈。相信这将开启更加高效协作的新篇章。

**改写**

报销流程从周三开始试行一次审批，原来需要两次。超过 5000 元的申请仍需负责人签字。财务会在两周后收集反馈。

**复核要点**

两次改一次、周三、试行、超过 5000 元、负责人签字、两周后、财务收集反馈全部保留。没有承诺审批一定提速，也没有把试行写成正式生效。例子中的数字是教学设定。
