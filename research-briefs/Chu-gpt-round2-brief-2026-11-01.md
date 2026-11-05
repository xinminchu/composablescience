# GPT 第二轮优化指令（直接粘贴）

## 目标

本轮不重写，只做三件事：**证据加固、机制深化、历史精确化**。初稿的三处自我限制（"第一读者"缺普遍性实证、同行评审非历史上唯一、五维向量是概念模型）是优点，**一字不删**。四节结构不动，"升级不是废除"的结论不动。

---

## 一、第一节：经验证据强化（最高优先级）

1. 加入已核实的 Nature Sensors 社论证据（新增参考文献 [14]，格式见第五节）。可直接使用的原句：
   - "Researchers are increasingly discovering and consuming scientific knowledge through artificial intelligence (AI) platforms built by technology companies."
   - "A 2025 survey found that 61% of researchers use AI tools to discover and summarize scientific papers, rather than reading them directly on journal platforms."（Wiley《ExplanAItions 2025–2026》调查）
   - "Perplexity AI, which surpassed 30 million daily searches in 2025, has partnered with Wiley to deliver peer-reviewed content directly through its platform, reducing reliance on journal websites."
   建议：61% 与 Perplexity 两个数字放在第一段开场。
2. 把"第一读者"收紧为操作化定义（初稿已有分析概念，本轮给定义句）：**不是"每篇论文先被机器打开"，而是"AI 系统大规模中介了学术内容的人类首次接触（发现、摘要、排序、预评价）"**。定义句写进第一节第二段。
3. 增加"可证伪性"段落：什么证据能加强或推翻现象主张（例如出版商侧 AI 优先访问数据、研究者工作流程日志、检索行为测量），并把测量方案对接到第四节的现象命题。

## 二、第二节：历史精确化

1. 把批判对象精确限定为"**二战后以整篇期刊论文为信用凭证的主导制度实践**"，明确承认前期刊时代与非期刊渠道（预印本、专著、会议、专利）的信用分配传统一直存在。
2. 加一段论证：**多元结算不是发明，而是回归**——这反而加强第三节提案的合法性（我们不是要创造一个从未存在过的东西，而是要恢复被单一凭证压制的plurality，并用现代基础设施把它做好）。

## 三、第三节：从概念模型到可操作化（第二优先级）

1. 保留"概念模型"的诚实声明；为五个维度各配"候选指标＋现存数据源"（这是从立场文章迈向理论贡献的关键一步）：
   - O 原创性：新颖性声明、后验引用中的"首创"归因记录
   - E 证据质量：数据/代码可用性徽章、方法—结论匹配度评审
   - V 验证：复现徽章、公开评审记录、反例登记
   - M 维护：版本更新记录、勘误响应、长期可用性
   - U 下游使用：有证据的复用追踪（引用＋代码依赖＋数据引用），**剔除自引、互引与自动调用**
2. 写清"**记录→采用→分配**"的制度链条：谁记账（开放基础设施）、谁验证（多元主体）、谁结算（资助机构、高校、期刊如何把向量纳入聘用、晋升、资助决策）。初稿的记录结构（四类关系）保留，在此基础上补"谁用这些记录做决定"。
3. 激励相容深化：防刷分、抗体操纵的规则（初稿第四项硬约束已有，展开为机制设计语言：什么行为可被观测、什么操纵可被剔除、申诉路径）。
4. 保留"事实层 vs 规范层"两分法（初稿亮点，一字不动）。

## 四、引用纪律

1. **[6] Latona 必须处理**：要么在第一/第二节正文引用（AI 评审提高接收率是"评价者已变"的硬证据，建议放在第一节 NIH 段落之后），要么从参考文献删除。**不许留悬空引用**。
2. 新增 [14]（格式如下），在第一节引用。
3. 本轮新增的任何文献/数据一律标 **[待核实]**，不得作为论证依据。

```latex
\bibitem{natsensors2026} Shaping the AI systems that speak for science. (2026). Editorial. \textit{Nature Sensors}, 1, 559--560. https://doi.org/10.1038/s44460-026-00109-0.
```

## 五、不动的地方

- 三处自我限制、四节结构、"升级不是废除"、甲乙丙丁假设性例子（保留"概念演示"标注）。
- 语言风格保持：平实，术语首次出现即定义。
- 输出仍为完整可编译 LaTeX，中文。
