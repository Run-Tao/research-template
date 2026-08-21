<!--
  ============================================================
  科研项目模板 README
  使用前请替换：项目名称、简介、使用场景、成员信息
  ============================================================
-->

# 科研项目模板（Research Template）

> 一个面向 **AI 项目 / 数学建模竞赛 / 课程项目 / 科研实验 / 论文写作** 的
> 长期维护型项目模板，模拟真实科研团队的工作流：代码、数据、实验、论文、协作一体化管理。

[![CI](https://github.com/Run-Tao/research-template/actions/workflows/ci.yml/badge.svg)](https://github.com/Run-Tao/research-template/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 目录

- [1. 项目简介](#1-项目简介)
- [2. 项目结构说明](#2-项目结构说明)
- [3. 环境配置](#3-环境配置)
- [4. 如何运行代码](#4-如何运行代码)
- [5. 如何开始一个新的实验](#5-如何开始一个新的实验)
- [6. 如何记录实验结果](#6-如何记录实验结果)
- [7. Git 协作规范](#7-git-协作规范)
- [8. Commit 命名规范](#8-commit-命名规范)
- [9. 常见问题（FAQ）](#9-常见问题faq)
- [10. License](#10-license)

---

## 1. 项目简介

（在这里用 2-3 句话介绍你的项目：研究什么问题、用什么方法、当前进展。）

**本模板适用场景：**

| 场景 | 说明 |
|---|---|
| 🎓 课程项目 | 开箱即用的代码 + 报告结构，交作业/答辩可直接用 |
| 🏆 数学建模竞赛 | 数据流水线 + 实验记录，赛题分工协作有章可循 |
| 🤖 AI 项目 | 配置化训练、可复现实验、模型与数据分离管理 |
| 🔬 科研实验 | 实验记录模板 + 文献管理 + 论文写作一体化 |
| 📝 论文写作 | LaTeX 模板 + 图表统一输出，论文与代码同步演进 |

**核心理念：** 代码可复现、实验有记录、协作有规范、论文能追溯。

---

## 2. 项目结构说明

```text
research-template/
├── README.md                  # 项目说明（本文件）
├── LICENSE                    # 开源协议（MIT）
├── .gitignore                 # Git 忽略规则（数据/模型/日志/缓存不入库）
├── .editorconfig              # 跨编辑器统一风格
├── pyproject.toml             # Python 工程配置（打包/Lint/测试）
├── requirements.txt           # 运行时依赖（pip）
├── requirements-dev.txt       # 开发工具依赖（pytest/ruff/pre-commit）
├── environment.yml            # conda 完整环境（可复现）
├── Makefile                   # 常用命令入口
├── CONTRIBUTING.md            # 多人协作规范（必读）
│
├── configs/
│   └── config.yaml            # 全局实验配置（参数集中管理）
│
├── data/                      # 数据流水线（raw → processed 单向）
│   ├── raw/                   # 原始数据（只读，不入 Git）
│   ├── processed/             # 处理后数据（由脚本生成）
│   └── README.md              # 数据字典
│
├── src/                       # 可复用代码包
│   ├── main.py                # 训练/评估流水线入口
│   ├── data/                  # 数据加载、清洗、预处理
│   ├── models/                # 模型定义、训练、推理
│   ├── utils/                 # 配置加载、随机种子等公共工具
│   └── visualization/         # 论文图表生成
│
├── notebooks/                 # 探索性分析草稿区（成果需沉淀到 src/）
│
├── experiments/               # 实验记录管理
│   ├── template.md            # 实验记录模板（复制后填写）
│   ├── logs/                  # 训练日志（TensorBoard 等，不入 Git）
│   └── results/               # 结果文件（指标、图表）
│
├── paper/                     # LaTeX 论文
│   ├── main.tex               # 主文件（XeLaTeX 编译）
│   ├── sections/              # 各章节独立文件
│   ├── figures/               # 论文图片
│   └── references.bib         # BibTeX 文献库
│
├── docs/                      # 团队知识库
│   ├── design/                # 技术方案
│   ├── meetings/              # 会议纪要
│   └── literature/            # 文献笔记
│
├── scripts/                   # 一次性脚本（下载、批量实验等）
├── tests/                     # 测试
└── .github/                   # GitHub 协作模板
    ├── ISSUE_TEMPLATE/        # Bug / 实验计划 / 功能需求 模板
    ├── PULL_REQUEST_TEMPLATE.md
    └── workflows/ci.yml       # 自动 Lint + 测试
```

**设计原则速览：**

| 原则 | 体现 |
|---|---|
| 数据与代码分离 | `data/` 独立，原始数据不入 Git |
| 配置与代码分离 | 参数集中在 `configs/config.yaml` |
| 实验记录即资产 | `experiments/` 结构化记录每个实验 |
| 论文与代码同仓 | `paper/` 图表可由 `src/visualization` 复现 |
| 可复现优先 | conda 环境 + 固定种子 + 实验记录参数 |
| 协作友好 | Issue/PR 模板 + CONTRIBUTING 规范 |

---

## 3. 环境配置

### 方式一：conda（推荐，可复现性最强）

```bash
# 创建完整环境（Python 3.12 + 全部依赖）
conda env create -f environment.yml

# 激活环境
conda activate research-template
```

### 方式二：pip（已有 Python 3.10~3.12）

```bash
# 安装运行时依赖
pip install -r requirements.txt

# （推荐）以可编辑模式安装本项目，使 src 可直接 import
pip install -e .

# 安装开发工具（lint/测试，可选）
pip install -e ".[dev]"
```

> **版本建议**：Python 3.10~3.12（深度学习框架对最新 Python 版本支持有滞后）。
> 需要 PyTorch 等框架时，在 `requirements.txt` 或 `environment.yml` 中取消对应行的注释。

### 验证安装

```bash
python -m src.main          # 应打印配置加载成功
pytest                      # 冒烟测试应全部通过
```

---

## 4. 如何运行代码

### 统一入口（推荐）

```bash
# 使用默认配置运行完整流水线
python -m src.main

# 使用实验专属配置
python -m src.main --config experiments/xxx_config.yaml
```

### 分步运行

```bash
# 1. 数据预处理（raw → processed）
python -m src.data.make_dataset

# 2. 训练模型
python -m src.models.train_model --config configs/config.yaml

# 3. 模型推理
python -m src.models.predict_model --config configs/config.yaml
```

### Makefile 快捷命令

```bash
make setup    # 安装依赖
make run      # 运行主程序
make lint     # 代码检查
make test     # 运行测试
make paper    # 编译论文
```

> **Windows 提示**：`make` 可通过 Git Bash 或 `choco install make` 使用；不想装 make 时直接运行上述 python 命令即可。

---

## 5. 如何开始一个新的实验

```text
第 1 步  提 Issue：新建"实验计划"类型的 Issue，说明目的与设计
第 2 步  建分支：git checkout -b experiment/xxx
第 3 步  配参数：复制 configs/config.yaml 为 experiments/xxx_config.yaml 并修改
第 4 步  建记录：复制 experiments/template.md 为 experiments/YYYYMMDD_xxx.md 并填写前 3 节
第 5 步  写代码：在 src/ 下实现（数据 → 模型 → 可视化），保持主入口可运行
第 6 步  跑实验：python -m src.main --config experiments/xxx_config.yaml
第 7 步  记结果：结果图表存入 experiments/results/，补全实验记录的"结果/分析/下一步"
第 8 步  提 PR：关联 Issue，按模板填写，CI 通过 + Review 通过后合并
```

**一个实验 = 一份配置 + 一份记录 + 一份结果 + 对应代码变更**，缺一不可。

---

## 6. 如何记录实验结果

- **模板**：`experiments/template.md`，包含：实验目的 / 数据集 / 参数设置 / 方法 / 结果 / 分析 / 下一步计划
- **命名**：`experiments/YYYYMMDD_<实验名>.md`，如 `experiments/20250115_baseline.md`
- **必填元信息**：实验编号、日期、负责人、配置文件、代码版本（`git rev-parse HEAD`）、环境
- **结果文件**：图表与指标存到 `experiments/results/`，并在记录中写明路径
- **日志**：训练日志（TensorBoard 等）写入 `experiments/logs/`（默认不入 Git）

> 原则：**任何实验（包括失败尝试）都值得记录**。"为什么失败"是三个月后最珍贵的资料。

---

## 7. Git 协作规范

详细流程见 [CONTRIBUTING.md](CONTRIBUTING.md)，核心规则：

| 规则 | 说明 |
|---|---|
| 分支管理 | 禁止直接推 `main`，一律走 PR |
| 分支命名 | `feature/xxx`、`fix/xxx`、`experiment/xxx`、`docs/xxx` |
| Issue 模板 | Bug / 实验计划 / 功能需求 三类，见 `.github/ISSUE_TEMPLATE/` |
| PR 要求 | 关联 Issue、CI 通过、至少 1 人 Review |
| 代码规范 | `ruff check` 必须通过，函数需 docstring |
| 实验规范 | 实验必须有记录文件，否则视为未完成 |
| 数据规范 | `data/raw/` 只读、不入库；数据集变更更新数据字典 |

**常用协作流程：**

```bash
# 拉取最新代码并建分支
git checkout main && git pull
git checkout -b experiment/baseline

# 开发提交（遵守 Commit 规范）
git add <文件>
git commit -m "experiment: 记录 baseline 实验（EXP-001）"

# 推送并提 PR
git push -u origin experiment/baseline
```

---

## 8. Commit 命名规范

格式：**`<type>: <简短描述>`**（描述用祈使句，说明"做了什么"）

| type | 含义 | 示例 |
|---|---|---|
| `feat` | 新增功能 | `feat: 添加 MLP 模型训练脚本` |
| `fix` | 修复问题 | `fix: 修复数据划分随机种子不生效` |
| `docs` | 修改文档 | `docs: 更新环境配置说明` |
| `experiment` | 新增/更新实验 | `experiment: 记录 baseline 实验（EXP-001）` |
| `refactor` | 代码重构 | `refactor: 抽取公共指标计算函数` |
| `test` | 新增/修改测试 | `test: 增加配置加载冒烟测试` |
| `chore` | 杂项（依赖/构建） | `chore: 升级 pandas 至 2.1` |

**示例（好 / 坏对比）：**

```text
✔ feat: 添加早停机制（early stopping）
✔ experiment: 记录 MLP 在 CIFAR-10 上的消融实验
✘ update code and fix stuff        # 无 type，语义不清
✘ feat: 添加早停并修复 bug 还改了文档  # 一个 commit 只做一件事
```

---

## 9. 常见问题（FAQ）

**Q1：数据放哪里？为什么 raw 不入 Git？**
原始数据放入 `data/raw/`（本地/网盘），不入 Git——大文件会拖垮仓库、且原始数据通常不可复现。
处理后数据由脚本生成（`data/processed/`），保证了"任何人 clone 仓库 + 跑脚本 = 同一份数据"。

**Q2：需要 PyTorch/TensorFlow 怎么办？**
在 `requirements.txt` 或 `environment.yml` 中取消对应行注释，或 `pip install torch`。
代码中的 `src/utils/seed.py` 已自动适配 torch（未安装时自动跳过）。

**Q3：论文怎么编译？**
需安装 LaTeX 发行版（Windows 推荐 [MiKTeX](https://miktex.org/)，macOS/Linux 推荐 TeX Live）。
```bash
make paper        # = latexmk -xelatex paper/main.tex
```

**Q4：如何换一个新的数据集/项目？**
1. 更新 `configs/config.yaml` 的 `data` 节与 `data/README.md` 数据字典
2. 在 `src/data/make_dataset.py` 实现处理逻辑
3. 按第 5 节流程开始新实验

**Q5：多人协作时文件冲突怎么办？**
章节/模块按文件拆分（`paper/sections/`、`src/` 各模块），从源头减少冲突。
冲突时优先 `git rebase main`（未推送的分支），见 CONTRIBUTING 第 9 节。

---

## 10. License

本项目使用 [MIT License](LICENSE)（Copyright © 2025 Tao Li）。
