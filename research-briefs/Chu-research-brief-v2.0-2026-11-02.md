# Position Paper Research Brief（讨论稿 v2.0）

暂定标题：When AI Becomes the First Reader: From Peer Review to Proof of Contribution
版本：v2.0 ｜ 日期：2026-11-02 ｜ 阶段：9 天冲刺 Step 1（扩展摘要的前置 brief）

说明：v2.0 回应第一轮讨论意见。v0.1 的三个主张（现象→问题→方案）保留，本稿补上理论一层：基线模型、靶心命题、构念定义、解绑论证、对自己方案的失败模式分析、张力分析。工程逻辑不动，理论逻辑补齐。

---

## 一、研究定位与目标

**Organizing proposition（全文的靶心，一句话）：**

> AI 不消除学术信用结算的瓶颈，它改变结算的单位和位置。
> AI does not eliminate the bottleneck in scholarly credit settlement; it changes the unit and the locus of settlement.

一句话定位：当 AI 成为学术成果事实上的第一读者，信用按"整篇论文"结算的制度已经不够用了——本文提出把学术信用从"期刊盖章"升级为"贡献证明"（proof of contribution），并给出可运行、可评估的实现路径。

目标读者：学术共同体，以及 IS、科学学、知识治理方向的研究者。首发拟走 SSRN，后续投会议/期刊由小组讨论决定。

本研究的独特位置：并行方向中，本研究是唯一把制度理论的结算概念用**可运行原型**实例化的——理论有经验之根，不是空想。（原型：组件级知识图谱已运行，见第八节。）

---

## 二、理论基线：学界现在怎么理解学术信用

**Received model（被接受的模型）：** 现代学术信用体系把四种功能捆绑在"期刊论文"这一个结算单位上——

- 注册 registration（确立优先权）
- 认证 certification（同行评审背书）
- 传播 awareness（进入读者视野）
- 存档 archiving（长期可引用）

（Roosendaal & Geurts 1997 对期刊功能的经典划分。）

**本研究的改动点：** AI 同时冲击了四个功能的技术条件——检索层/参数层双入口改变传播，生成式写作改变注册成本，AI 评审改变认证产能。问题不再是"某个功能失灵"，而是**捆绑本身的历史条件变了**。

**Puzzle（真问题，不是现象描述）：**
一个所有人都说坏了的制度，为什么二十年纹丝不动？DORA（2012）、CoARA（2022，700+ 机构）、altmetrics（一轮炒作）——都只改了**评价标准**，没动**结算媒介**：还是整篇论文，还是人读。制度理论的答案：同构压力（DiMaggio & Powell 1983）与合法性仪式（Meyer & Rowan 1977）让旧单位自我维持。AI 动的是媒介本身——这就是为什么这一次不一样，这也是本篇区别于历轮改革批判的理论位置。

**研究问题（递进）：**

- RQ1：在 AI 成为第一读者的条件下，旧结算机制的均衡是什么？（失灵的表现与条件）
- RQ2：组件级记账 + 多元结算的机制设计空间是什么？记录→采用→分配链条上，谁记账、谁验证、谁拿记录做聘用/资助决定？
- RQ3：在什么条件下新结算机制优于旧机制？（福利比较的参数域）

---

## 三、核心构念：结算（settlement）

**定义：** 结算 = 学术共同体把"贡献"转化为"可携带的信用凭证"的制度化过程。
Settlement is the institutionalized process by which a scholarly community converts "contributions" into portable credentials of credit.

**血统：** Merton（1973）的科学规范结构（信用是科学共同体的通货）；Bourdieu（1975）的科学资本（信用可在场域间转化）；Meyer & Rowan（1977）——同行评审首先是一种**合法性仪式**，质量过滤是它的功能之一，不是全部。

**边界：** 结算 ≠ 评价。评价（评审、引用、下载）是结算的环节之一；结算是"哪个环节的产出能变成聘用、晋升、资助决定里的硬通货"。DORA 原话禁的正是"用期刊指标替代对科学家个人贡献的评价，或用于聘用、晋升、资助决定"——禁的是结算环节的替代品，不是评价本身。

**这一定义的用途：** 它把论文的批判对象从"同行评审很慢"提升为"结算机制的制度变迁"，把方案从"修评审流程"提升为"重建结算单位"。理论在上，方案在下。

---

## 四、核心论证：解绑（unbundling）

**论证（Coase 式）：** 当需求异质且技术条件变化时，捆绑造成无谓损失。

- **需求异质：** 记录需求（快速确权、零门槛）vs 凭证需求（严格认证、稀缺信号）——被现行制度捆在同一张纸上。捆绑的代价：为保护凭证的稀缺性，连记录也一并限速（好工作被延迟、被埋没）。
- **技术条件变化：** AI 让记录的边际成本趋零（生成式写作）、让传播不再经过期刊（检索层直达读者）、让认证产能弹性化（AI 评审）。捆绑的历史理由（纸质时代的规模经济）消失了。
- **结论：** 组件级记账不是发明，是解绑——把四个功能从"整篇论文"这个偶然的单位上松开，各自找到合适的结算粒度。

**两处错位的理论重述（v0.1 的粒度错/通道错，升级为理论语言）：**

1. 粒度错 = 结算单位与贡献单位的错配：信用按整篇结算，贡献发生在组件级（数据、方法、证据、复现）。
2. 通道错 = 认证产能的介质错配：为"人先读"设计的抽查式评审，面对机器规模的第一读者，既看不过来也评不准。

**三个收敛主张（v0.1 保留，挂在靶心命题之下）：**

1. 现象主张：AI 已成为事实上的第一读者。证据：2026 年《Nature Sensors》社论指出研究者越来越多经由 AI 平台发现和阅读成果；Wiley 2025 调查：61% 的研究者用 AI 工具发现和总结论文；Perplexity 日搜索超 3000 万次并与 Wiley 合作直接提供同行评审内容。操作化定义：不是"每篇论文先被机器打开"，而是"AI 大规模中介了人类首次接触"。
2. 问题主张：以整篇论文为单位的结算机制失灵（见上两处错位）。
3. 方案主张：信用向量化（五维：原创性 origination / 证据质量 evidence quality / 验证 verification / 维护 maintenance / 下游使用 downstream use）+ 组件级记账；同行评审不废除，降格为多种结算机制之一（升级而非替代——标题本身要锋利，正文必须把这句写清楚）。

---

## 五、对自己方案的失败模式分析（先开枪）

任何结算机制都会被博弈。新机制的失败模式：

- **F1｜维度 Goodhart 化：** 一旦某维度成为指标，就会被优化。引用数的前车之鉴会重演到每个向量维度上——"被验证次数"可以刷，"下游使用"可以互引。对策方向：信号的成本必须与质量相关（信号理论），不可伪造性是硬约束。
- **F2｜维护维度的激励真空：** 记录需要持续维护（版本、链接、复现），但维护是公共品，谁出钱？这是五维里最脆弱的一维——它的激励问题不解决，整个记账体系会 decay。
- **F3｜注意力碎片化：** 五个维度对读者是认知负担；维度越多，读者越退回看单一数字（重回影响因子式的单一度量）。对策方向：面向不同决策场景的维度组合（聘用看原创性+验证，资助看下游使用+维护），而不是把五维同时糊给所有人。

诚实声明：F1–F3 在本篇提出、在后续 DSR 评估中检验（见第八节）。Position paper 的任务是把失败模式摆上台面，不是假装它们不存在。

---

## 六、张力与边界

**两组张力（承认 trade-off，不承诺单点最优）：**

- T1｜验证严格性 vs 下游使用速度：越严格的验证，信用凭证到账越慢；快速领域与慢速领域需要不同的严格性参数——统一制度必然次优。
- T2｜记录完备性 vs 维护成本：记账越细，维护越贵；最优粒度是经济学问题，不是技术问题。

设计输出是 **Pareto frontier 及边界上的选择规则**，不是单点最优解。

**诚实边界（v0.1 保留，这是优点）：**

1. "第一读者"尚未得到普遍性实证验证——现有文献支持 AI 进入生产和评审流程，不足以证明多数论文已先由机器阅读。
2. 同行评审不是历史上唯一的信用分配机制——本文批判对象限定为"二战后整篇论文凭证制"这一制度实践。
3. 五维向量目前是概念模型——尚无验证过的测量方法、权重体系或跨学科评价结果。

---

## 七、文献定位

**三簇文献：**

1. 同行评审危机文献：评审产能、偏见、AI 评审渗透（如 ICLR 2025 随机试验：27% 的评审人据 LLM 反馈修改了评审，Thakkar et al. 2026, *Nature Machine Intelligence*）。
2. 开放科学与改革文献：DORA、CoARA、Leiden Manifesto（2015）、eLife publish-review-curate（2023）——制度实验的先例与教训。
3. 科学学（science of science）：对旧结算体系的测量（引文、合作网络、撤稿——2023 年撤稿破万，Van Noorden 2023, *Nature*）。

**Gap（一句话）：** 前两簇批判或改革了旧体系，第三簇测量了旧体系，**没有人把"读者改变"当作结算机制的制度变迁来理论化**。本篇占的就是这个位置。

**理论资源（核心引用；标"已核"的卷期页码已核实，其余引用前请核对）：**

- Meyer, J. W., & Rowan, B. (1977). Institutionalized organizations: Formal structure as myth and ceremony. *American Journal of Sociology*, 83(2), 340–363.（已核）
- DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, 48(2), 147–160.（已核）
- Merton, R. K. (1973). *The Sociology of Science*. University of Chicago Press.（已核）
- Bourdieu, P. (1975). The specificity of the scientific field and the social conditions of the progress of reason. *Social Science Information*, 14(6), 19–47.（已核）
- Roosendaal, H. E., & Geurts, P. A. T. M. (1997). Forces and functions in scientific communication: An analysis of their interplay. Paper presented at the Conference on Cooperative Research in Information Systems in Physics (CRISP '97), Oldenburg, Germany, September 1–3.（已核：这是会议论文不是期刊文章，Twente 大学存档全文 pp. 1–32；作者名缩写为 P. A. T. M.，原稿 "Th." 已改）
- Latour, B., & Woolgar, S. (1979). *Laboratory Life*. Sage.（已核）
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly*, 28(1), 75–105.（已核）
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems*, 24(3), 45–77.（已核）
- Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly*, 37(2), 337–355.（已核）

纪律：不得虚构引用与数据；CRS 在给出出处前不可引用；PaperDaily 规模数字引用前须经确认。

---

## 八、研究方法与实践路径

**本文：** 跨学科文献综合 + 概念分析 + 研究命题构建。Position paper 不以 DSR 为主要方法。

**后续：** Design Science Research（Peffers 六步）。artifact = 可运行的组件级知识图谱原型；演示 = 真实运转的评审与记账场景；评估 = 覆盖率、记录质量、F1–F3 的压力测试。

**存在性证明：** 原型已经跑起来了——这是本篇区别于纯思辨 position paper 的落地点，也是对"没落实"批评的直接回答。

**三篇序列：** position（本篇，立旗）→ system paper（artifact + 演示）→ design-science evaluation paper（评估 + 设计原则），即 DSR 的完整展开。

---

## 九、篇幅与文章结构

中文 4000–6000 字（按冲刺要求），英文版 3000–4500 词。四节：

1. 第一读者之变：现象证据 + 靶心命题（§2 的压缩）
2. 结算机制的失灵：解绑论证 + 两处错位
3. 从同行评审到贡献证明：向量 + 组件记账 + 失败模式 F1–F3 + 张力 T1–T2
4. 研究议程：DSR 路径、三篇序列、对共同体的呼吁

---

## 十、写作及修订原则

- 严格区分：已有事实 / 趋势判断 / 预测 / 研究假设。不把"可能颠覆"写成"已经颠覆"：有条件的情景 > 确定性结论。
- 语言平实，术语首次出现即定义，中英对照。
- 标题中的 "proof of contribution"，正文用"贡献的确权与结算"等中性学术表述展开，不引入其他术语体系。
- 允许写作中调整结构，但重大调整须说明理由；保留未解决的争议作为后续研究的起点。

---

附：版本记录

- v0.1 2026-11-01：初稿，三个主张收敛为现象→问题→方案。
- v2.0 2026-11-02：补理论一层——基线模型、靶心命题、结算构念定义、解绑论证、失败模式分析、张力分析、文献定位与一句话 gap。
