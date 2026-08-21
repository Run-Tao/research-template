"""模型训练：读取 processed 数据，训练模型并保存。

用法：
    python -m src.models.train_model
    python -m src.models.train_model --config experiments/<实验名>_config.yaml
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.config import load_config
from src.utils.seed import set_seed


def train(config: dict) -> None:
    """训练主流程。

    Args:
        config: 从配置文件加载的配置字典。
    """
    set_seed(config["seed"])

    # TODO(你的名字): 实现真实训练逻辑，建议步骤：
    #   1. 读取 data/processed 数据
    #   2. 按 config["split"] 划分训练/验证/测试集
    #   3. 根据 config["model"]["name"] 构建模型
    #   4. 按 config["train"] 训练，日志写入 experiments/logs
    #   5. 评估指标写入 experiments/results，模型保存（默认不入 Git）
    print("训练脚手架已就绪。请实现 src/models/train_model.py。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="训练模型")
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="配置文件路径，默认使用 configs/config.yaml",
    )
    args = parser.parse_args()
    train(load_config(args.config))
