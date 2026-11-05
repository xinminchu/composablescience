# Position Paper Research Brief

暂定标题：When AI Becomes the First Reader: From Peer Review to Proof of Contribution
日期：2026-11-02
用途：扩展摘要的前置研究简报

---

## 一、靶心命题

> AI 不消除学术信用结算的瓶颈，它改变结算的单位和位置。
> AI does not eliminate the bottleneck in scholarly credit settlement; it changes the unit and the locus of settlement.

一句话定位：当 AI 成为学术成果事实上的第一读者，信用按"整篇论文"结算的制度已经不够用了——本文提出把学术信用从"期刊盖章"升级为"贡献证明"（proof of contribution），并给出可运行、可评估的实现路径。

目标读者：学术共同体，以及信息系统、科学学、知识治理方向的研究者。首发拟走 SSRN。

---

## 二、核心构念：信用结算（credit settlement）

**诚实声明：这是本文提出的分析构念，不是既有术语。** 它的类比来源是金融市场的结算制度：证券交易所的 clearing / settlement 把交易变成不可撤销的最终交割；学术界同样需要一个制度化过程，把"贡献"变成聘用、晋升、资助决定里的"硬通货"。新概念大大方方承认是新的。

**定义：** 信用结算 = 学术共同体把"贡献"转化为"可携带的信用凭证"的制度化过程。
Credit settlement is the institutionalized process by which a scholarly community converts contributions into portable credentials of credit.

**理论血统：** Merton（1973）的科学规范结构（信用是科学共同体的通货）；Bourdieu（1975）的科学资本（信用可在场域间转化）；Meyer & Rowan（1977）——同行评审首先是一种合法性仪式（legitimacy ritual），质量过滤是它的功能之一，不是全部。

**内部结构：一次完整的结算包含三个环节——**

1. 登记 registration：让贡献变得可见、可引用、可追溯；
2. 确权 attribution：把信用归到具体的人（或团队）名下；
3. 承兑 acceptance：共同体在资源分配决定中承认这个凭证有效。

三个环节缺一不可：只登记不确权是档案馆；只确权不承兑是自说自话。现行制度把三个环节一次性捆绑在"论文发表"上——这正是下文要解绑的对象。

**变异维度：** 任何结算机制都可以在五个维度上描述——结算单位（整篇 / 组件 / 个人）、结算媒介（纸质 / 数字 / 模型）、验证者（同行 / 机构 / 算法）、可携带性（跨机构、跨学科是否通用）、可逆性（撤稿与更正的成本）。这五个维度是本文的分析网格。

**边界：** 信用结算 ≠ 评价。评价（评审、引用、下载）是结算的环节之一；结算回答的是"哪个环节的产出能变成硬通货"。

**"证明"的含义：** 标题中的 proof 不是数学证明，而是**共同体承兑的证据结构**（evidence structure honored by the community）——可验证、可追溯、被承认，三者缺一都不算证明。

---

## 三、理论基线与 puzzle

**基线：** 现代学术信用体系把四种功能捆绑在"期刊论文"这一个结算单位上：注册（确立优先权）、认证（同行评审背书）、传播（进入读者视野）、存档（长期可引用）。（Roosendaal & Geurts 1997。）

**Puzzle（一）：烂制度为什么不死？**
DORA（2012）、CoARA（2022）、altmetrics（一轮炒作）——都只改了评价标准，没动结算媒介：还是整篇论文，还是人读。同构压力（DiMaggio & Powell 1983）与合法性仪式（Meyer & Rowan 1977）让旧单位自我维持。

**Puzzle（二）：改革的反讽——改革加强了它要改革的对象。**
DORA 说"不要用期刊指标，要看论文本身的贡献"——这句话恰恰加固了"论文"作为结算单位的地位。历轮改革批判的都是"用哪把尺子量论文"，没有一轮质疑"为什么是论文这个单位"。AI 第一次动的是单位本身：当机器能直接读写组件（数据、方法、证据），"整篇"这个单位的技术必要性消失了。

---

## 四、读者角色的三分

"第一读者"需要精确化。阅读包含三种角色：

- 发现者 discoverer：把成果送到人面前；
- 解释者 interpreter：把成果变成可理解的陈述；
- 裁决者 adjudicator：说"这个算数"。

AI 目前主导了发现，部分承担了解释，几乎不做裁决。**本文的"第一读者"指前两者**：AI 大规模中介了人类与成果的首次接触（操作化定义）。而信用结算真正争夺的是第三个角色——谁有资格裁决"这个贡献算数"。本文的论证是：当发现和解释被机器接管，裁决机制就不能再寄生在旧的发现渠道（期刊）上。

---

## 五、核心论证：解绑（unbundling）

**论证：** 当需求异质且技术条件变化时，捆绑造成无谓损失。

- **需求异质：** 记录需求（快速确权、零门槛）vs 凭证需求（严格认证、稀缺信号）——被捆在同一张纸上。为保护凭证的稀缺性，连记录也一并限速。
- **技术条件变化：** AI 让记录的边际成本趋零，让传播绕过期刊直达读者，让认证产能弹性化。捆绑的历史理由（纸质时代的规模经济）消失了。
- **结论：** 组件级记账不是发明，是解绑——把四个功能从"整篇论文"这个偶然的单位上松开，各自找到合适的结算粒度。

**两处错位（解绑论证的两个实例）：**

1. 结算单位与贡献单位的错配：信用按整篇结算，贡献发生在组件级（数据、方法、证据、复现）；
2. 认证产能的介质错配：为"人先读"设计的抽查式评审，面对机器规模的首次接触，既看不过来也评不准。

**三个主张（挂在靶心命题之下）：**

1. 现象主张：AI 已成为事实上的第一读者（发现者与解释者意义上）。证据：2026 年《Nature Sensors》社论；Wiley 2025 调查（61% 的研究者用 AI 工具发现和总结论文）；Perplexity 日搜索超 3000 万次并与 Wiley 合作直接提供同行评审内容。
2. 问题主张：以整篇论文为单位的信用结算机制失灵（见上）。
3. 方案主张：信用向量化（五维：原创性 origination / 证据质量 evidence quality / 验证 verification / 维护 maintenance / 下游使用 downstream use）+ 组件级记账。**向量不加总**——不同决策需要不同的维度组合（聘用看原创性 + 验证，资助看下游使用 + 维护）；任何单一度量都会重蹈影响因子的覆辙。同行评审不废除，降格为多种结算机制之一（升级而非替代）。

---

## 六、结算机制变迁的条件

结算机制什么时候会变？三个条件：

1. **媒介条件：** 承载结算的介质发生变化（印刷机 → 互联网 → AI），旧单位的技术必要性消失；
2. **联盟条件：** 验证者联盟发生转移——新的裁决者获得承兑能力；
3. **成本条件：** 新单位的结算成本显著低于旧单位。

三者齐备时，旧机制让位。本文论证：AI 时代三者正在齐备。

---

## 七、对自己方案的失败模式分析

失败模式按§2 的三个环节归位：

- **F1｜维度 Goodhart 化**（确权环节）：一旦某维度成为指标，就会被优化。对策方向：信号的成本必须与质量相关，不可伪造性是硬约束。
- **F2｜维护维度的激励真空**（登记环节）：维护是公共品，谁出钱？五维里最脆弱的一维，不解决则记账体系 decay。
- **F3｜注意力碎片化**（承兑环节）：维度越多，读者越退回看单一数字。对策方向：面向决策场景的维度组合，不把五维同时糊给所有人。

F1–F3 在本篇提出，在后续研究中检验。Position paper 的任务是把失败模式摆上台面，不是假装它们不存在。

---

## 八、张力：配置 vs 激励

结算机制服务于两个功能：**配置**（把资源给好的工作）与**激励**（motivating 生产）。现行制度常被用激励辩护（"publish or perish 催人生产"），被用配置攻击（"好工作被埋没"）。任何新机制必须在两个功能上同时接受检验。

两组具体张力：

- T1｜验证严格性 vs 下游使用速度：统一的严格性标准必然次优，严格性应是领域参数；
- T2｜记录完备性 vs 维护成本：最优粒度是经济学问题，不是技术问题。

设计输出是 Pareto frontier 及边界上的选择规则，不是单点最优解。

---

## 九、命题网络

信用结算构念导出三个可检验的命题：

- P1：结算单位越粗，信用在不同学科间的可比性越低；
- P2：结算媒介变化时，旧单位的既得利益者会捍卫旧单位（可观察：出版商与评价机构的行为）；
- P3：承兑环节越分散（多机构、多场景各自承兑），单一权威排名的影响力越弱。

---

## 十、适用边界

本篇论证有三条边界，超出即不适用：

1. 只针对二战后"整篇论文凭证制"这一制度实践，不针对科学史上其他的信用形态；
2. 只适用于信用可转化为职位与资助的职业化科学，不适用于业余或纯粹声誉驱动的共同体；
3. 组件级记账的前提是贡献可数字化拆分——高度依赖默会知识（tacit knowledge）的领域，解绑的收益更小。

---

## 十一、文献定位

三簇文献：

1. 同行评审危机文献：评审产能、偏见、AI 评审渗透（如 ICLR 2025 随机试验：27% 的评审人据 LLM 反馈修改了评审，Thakkar et al. 2026, *Nature Machine Intelligence*）；
2. 开放科学与改革文献：DORA、CoARA、Leiden Manifesto（2015）、eLife publish-review-curate（2023）；
3. 科学学（science of science）：对旧结算体系的测量（引文、撤稿——2023 年撤稿破万，Van Noorden 2023, *Nature*）。

**Gap：** 前两簇批判或改革了旧体系，第三簇测量了旧体系，**没有人把"读者改变"当作信用结算机制的制度变迁来理论化**。本篇占的就是这个位置。

---

## 十二、理论资源

核心引用（卷期页码均已核实）：

- Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340–363.
- DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.
- Merton, R. K. (1973). *The Sociology of Science*. University of Chicago Press.
- Bourdieu, P. (1975). The specificity of the scientific field and the social conditions of the progress of reason. *Social Science Information*, 14(6), 19–47.
- Roosendaal, H. E., & Geurts, P. A. T. M. (1997). Forces and functions in scientific communication: An analysis of their interplay. Paper presented at the Conference on Cooperative Research in Information Systems in Physics (CRISP '97), Oldenburg, Germany, September 1–3.
- Latour, B., & Woolgar, S. (1979). *Laboratory Life*. Sage.
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105.
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77.
- Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly*, 37(2), 337–355.

纪律：不得虚构引用与数据。

---

## 十三、研究方法与后续路径

**本文：** 跨学科文献综合 + 概念分析 + 研究命题构建。Position paper 不以设计科学为主要方法。

**后续：** 设计科学研究范式——以可运行的组件级知识图谱原型为 artifact，经历"问题识别 → 设计开发 → 演示 → 评估"的完整循环，检验 F1–F3 与 P1–P3。

**存在性证明：** 原型已经跑起来了——这是本篇区别于纯思辨 position paper 的落地点。

---

## 十四、篇幅与文章结构

中文 4000–6000 字，英文 3000–4500 词。四节：

1. 第一读者之变：读者三分 + 靶心命题；
2. 信用结算机制的失灵：基线、双 puzzle、解绑论证；
3. 从同行评审到贡献证明：向量 + 组件记账 + 失败模式 + 张力；
4. 研究议程：命题网络、适用边界、后续路径。

---

## 十五、写作原则

- 严格区分：已有事实 / 趋势判断 / 预测 / 研究假设；
- 语言平实，术语首次出现即定义，中英对照；
- 标题中的 "proof of contribution"，正文用"贡献的确权与结算"等中性学术表述展开；
- 保留未解决的争议作为后续研究的起点。
