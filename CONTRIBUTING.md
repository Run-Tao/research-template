# 贡献指南（CONTRIBUTING）

感谢参与本项目！本指南定义了多人协作的标准流程，请**每位成员**遵守。

---

## 1. 总体工作流

```text
提 Issue（计划/需求/Bug）
      ↓
认领 Issue，创建分支
      ↓
在分支上开发 + 提交（遵守 Commit 规范）
      ↓
更新实验记录 / 文档
      ↓
发起 Pull Request（引用 Issue）
      ↓
至少 1 人 Review 通过
      ↓
合并到 main
```

## 2. 分支管理

| 分支 | 用途 | 命名 |
|---|---|---|
| `main` | 稳定主干，随时可运行 | — |
| 功能分支 | 新功能/修复/实验 | `feature/xxx`、`fix/xxx`、`experiment/xxx`、`docs/xxx` |

**规则：**
- 禁止直接向 `main` 推送，一律通过 PR 合并
- 分支名用英文小写 + 短横线，如 `feature/add-cnn-model`
- 从最新的 `main` 拉分支，开发前先 `git pull`

## 3. Commit 规范

格式：`<type>: <中文/英文简短描述>`

| type | 含义 | 示例 |
|---|---|---|
| `feat` | 新增功能 | `feat: 添加 MLP 模型训练脚本` |
| `fix` | 修复问题 | `fix: 修复数据划分时随机种子不生效` |
| `docs` | 修改文档 | `docs: 更新环境配置说明` |
| `experiment` | 新增/更新实验记录 | `experiment: 记录 baseline 实验（EXP-001）` |
| `refactor` | 代码重构（不改功能） | `refactor: 抽取公共的指标计算函数` |
| `test` | 新增/修改测试 | `test: 增加配置加载冒烟测试` |
| `chore` | 杂项（依赖、构建等） | `chore: 升级 pandas 至 2.1` |

**规则：**
- 一个 Commit 只做一件事
- 描述用祈使句，说明"做了什么"，而非"做了什么和什么"
- 实验相关改动必须同时更新实验记录（见第 5 节）

## 4. 代码规范

- 遵循 [PEP 8](https://peps.python.org/pep-0008/)，统一使用 **ruff** 检查：
  ```bash
  pip install -e ".[dev]"
  ruff check src/ scripts/ tests/   # 提交前必须通过
  ruff format src/ scripts/ tests/  # 自动格式化
  ```
- 函数/类必须有 docstring（说明用途、参数、返回值）
- 导入方式统一 `from src.xxx import yyy`
- 配置改动必须同步更新 `configs/config.yaml` 或实验专属配置

## 5. 实验记录要求

**任何实验（含探索性尝试）都必须记录**，否则视为未完成：

1. 新建实验前：提一个 `experiment` 类型的 Issue（用"实验计划"模板）
2. 实验进行中：复制 `experiments/template.md` 为 `experiments/YYYYMMDD_<实验名>.md` 并填写
3. 实验结束：结果图表放入 `experiments/results/`，记录文件随代码一起提交
4. 代码版本：记录中填写 `git rev-parse HEAD` 对应的 commit

## 6. Pull Request 要求

- PR 必须关联 Issue（`Closes #编号`）
- 使用 `.github/PULL_REQUEST_TEMPLATE.md` 模板填写
- 合并前需满足：**CI 通过** + **至少 1 名成员 Review 通过**
- Review 意见必须解决后（回复或修改）才能合并；有争议时与作者讨论，不强行合并

## 7. 文档要求

- 新增/修改功能时，同步更新 `README.md` 中相关部分
- 重要技术决策记录到 `docs/design/`
- 组会讨论记录到 `docs/meetings/`
- 阅读的论文记录到 `docs/literature/`（模板见 `docs/README.md`）

## 8. 数据处理规范

- 原始数据只放入 `data/raw/`，**永不修改、不入 Git**
- 处理后的数据写入 `data/processed/`，处理脚本必须可复现
- 更新数据集时同步更新 `data/README.md` 数据字典

## 9. 冲突解决

- 与 `main` 冲突时：优先 `git rebase main` 保持历史干净（仅限**自己未推送**的分支）
- 已推送的公共分支冲突：用 `git merge main` 解决
- 大文件冲突：检查是否误提交了数据/模型文件（它们本应被 `.gitignore` 排除）
