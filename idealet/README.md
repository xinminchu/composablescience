# Idealet 层 v0.1 MVP

论文层（arXiv 现成库）→ 模块层（`segmenter/` 切出的组件）→ **Idealet 层**：
组件之间的引用意图边、跨论文实体对齐，以及让知识网络**生长、修正、重组**的三个机制。

这是林教授判断中"真正值得研究"的部分：现有工具（Janeway / OJS / PubPub / OS-APS）
全是静态管线，没有一个处理动态问题。Idealet 层只做别人没有的那一层，
工作流、渲染、标准全部借用现成工具。

## 三个机制

| 动态 | 实现 | 命令 |
|---|---|---|
| 🌱 生长 | 新论文切分后组件自动接入图谱；引用边按意图类型挖掘 | `graph.py` |
| ✏️ 修正 | 组件修订产生新版本节点，旧版本保留，`supersedes` 边记录替代；`snapshot` 给出"当前共识"视图 | `revise.py` |
| 🧩 重组 | 从模块层挑选组件（自动取当前版本）生成新论文，`composedOf` 记录来源 | `recombine.py` |

## 用法

```bash
# 1. 生长：两篇论文 -> idealet 图谱（引用意图边 + 实体对齐）
python3 idealet/graph.py \
  --inputs examples/arxiv-1706-03762.jsonld examples/arxiv-1810-04805.jsonld \
  -o idealet/graph.json

# 2. 修正：修订一个组件（产生 v2，历史保留）
python3 idealet/revise.py revise --graph idealet/graph.json \
  --component https://w3id.org/scholcomp/arxiv-1706-03762/c1 \
  --text-file idealet/examples/revise-c1-v2.txt \
  --note "clarify QKV projection order" --agent "sam"

# 3. 当前共识快照（过滤掉被 supersede 的旧版本）
python3 idealet/revise.py snapshot --graph idealet/graph.json \
  -o idealet/graph-current.json

# 4. 重组：模块 -> 生成新论文
python3 idealet/recombine.py --graph idealet/graph.json \
  --pick https://w3id.org/scholcomp/arxiv-1706-03762/c1 \
         https://w3id.org/scholcomp/arxiv-1810-04805/c1 \
  --title "From attention to BERT: a module reader" --agent "sam" \
  -o idealet/examples/recombined-demo.json

# 5. 可视化
python3 -m http.server 8000
# open http://localhost:8000/viewer/idealet.html
```

## 方法说明（诚实基线）

- 引用意图：规则基线（`intent.py`），CiTO 对齐的粗粒度 5 类
  （usesMethodIn / extends / confirms / critiques / background），
  线索词匹配，默认 background。输入文件里已有的手工 `ComponentCitation` 边
  原样保留（视为金标），不重复挖掘。
- 引用目标：启发式（意图 → 被引论文的对应类型组件，如方法类意图找
  MethodStrategy），每条边都写了 `note` 说明假设。这是已知弱点，
  roadmap 要求换 LLM + 人工审核。
- 实体对齐：引号术语 + Title-Case 短语，归一化小写对齐，≥2 个组件提及
  才成实体；NIL 即首次见即建。同样是基线。
- 全部 stdlib-only、确定性、无网络（除了 segmenter 的 `--url` 抓取）。

## 演示数据

`idealet/graph.json` 已包含一次演示修订（Attention c1 的 v2，`supersedes` 边）
和 4 条引用边（2 手工 + 2 规则挖掘），`idealet/examples/recombined-demo.json`
是重组演示产物。注意重组时 c1 自动取了 v2——修正流入重组，这正是
"不断生长、修正、重组"的最小闭环。

## Roadmap（idealet）

- [ ] 引用意图 7 分类（CiTO 全对齐）+ 人工审核
- [ ] 实体对齐：NIL 聚类、跨语言
- [ ] 组件级评审意见挂载（激励机制的落点）
- [ ] 百篇论文规模的生长压力测试
