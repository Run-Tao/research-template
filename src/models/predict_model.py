"""模型推理/预测：加载训练好的模型对新数据进行预测。

用法：
    python -m src.models.predict_model --config PATH
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.config import load_config
from src.utils.seed import set_seed


def predict(config: dict) -> None:
    """推理主流程。

    Args:
        config: 从配置文件加载的配置字典。
    """
    set_seed(config["seed"])

    # TODO(你的名字): 实现真实推理逻辑：
    #   1. 加载 experiments/results 下训练好的模型
    #   2. 读取待预测数据
    #   3. 输出预测结果（保存为 csv / json）
    print("推理脚手架已就绪。请实现 src/models/predict_model.py。")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="模型推理")
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="配置文件路径，默认使用 configs/config.yaml",
    )
    args = parser.parse_args()
    predict(load_config(args.config))
