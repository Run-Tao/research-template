"""可视化工具：生成论文图表。

设计说明：
    - 论文图表统一由 src/visualization 生成，输出到 paper/figures 或 experiments/results
    - 使用 Agg 后端，保证在无界面环境（服务器/CI）下也能保存图片
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt  # noqa: E402  (需在设置后端之后导入)


def save_figure(fig: plt.Figure, path: str | Path, dpi: int = 300) -> None:
    """保存 matplotlib 图像并关闭 figure（释放内存）。

    Args:
        fig: matplotlib figure 对象。
        path: 保存路径。论文图表建议保存到 paper/figures/，
              实验过程图建议保存到 experiments/results/。
        dpi: 分辨率，论文图表建议 300。
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    plt.close(fig)


def visualize_results(config: dict) -> None:
    """结果可视化主流程（脚手架）。

    Args:
        config: 从配置文件加载的配置字典。
    """
    # TODO(你的名字): 实现真实的可视化逻辑，例如：
    #   1. 读取 experiments/results 下的指标
    #   2. 绘制训练曲线 / 混淆矩阵 / 特征重要性等
    #   3. 通过 save_figure 保存到 paper/figures/
    print("可视化脚手架已就绪。请实现 src/visualization/visualize.py。")
