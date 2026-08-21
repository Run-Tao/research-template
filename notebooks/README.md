# notebooks/ — 探索性分析草稿区

## 使用约定

1. **命名**：`NN_主题_作者.ipynb`，如 `01_数据探索_张三.ipynb`
2. **定位**：notebook 只做快速探索（EDA、原型验证），**最终成果必须沉淀到 `src/`**
3. **提交**：提交前清空输出（Jupyter：Cell → All Output → Clear Output）
4. **数据**：一律读写 `data/` 目录，不在 notebook 内存放中间大文件
5. **依赖**：notebook 中不要安装新包，需要新依赖先加入 `requirements.txt` 再使用

> 为什么：notebook 输出杂乱、难以 diff，不适合长期维护。
> 把可复用逻辑放进 `src/`，notebook 只保留"分析思路"。
