"""主入口：数据 -> 模型 -> 可视化 的完整流水线。

用法：
    python -m src.main                  # 使用默认配置 configs/config.yaml
    python -m src.main --config PATH    # 使用指定配置文件（如实验专属配置）
"""
from __future__ import annotations

import argparse
from pathlib import Path

from src.utils.config import load_config


def main() -> None:
    parser = argparse.ArgumentParser(description="科研项目主入口（训练/评估流水线）")
    parser.add_argument(
        "--config",
        type=Path,
        default=None,
        help="配置文件路径，默认使用 configs/config.yaml",
    )
    args = parser.parse_args()

    config = load_config(args.config)
    print(f"配置文件加载成功：{config}")

    # TODO(你的名字): 在此按顺序接入真实流水线
    # from src.data.make_dataset import make_dataset
    # from src.models.train_model import train
    # from src.models.predict_model import predict
    # from src.visualization.visualize import visualize_results
    #
    # 示例调用顺序：
    #   make_dataset(Path(config["data"]["raw_dir"]),
    #                Path(config["data"]["processed_dir"]))
    #   train(config)
    #   predict(config)
    #   visualize_results(config)
    print("流水线脚手架已就绪。请按 README『如何开始一个新的实验』接入真实逻辑。")


if __name__ == "__main__":
    main()
