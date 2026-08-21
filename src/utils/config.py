"""配置加载工具：读取 configs/config.yaml。

设计说明：
    - 所有超参数集中在一个 YAML 文件，代码不写死参数
    - 每个实验可复制配置文件到 experiments/ 下再修改，实现实验参数隔离
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

# 仓库根目录（本文件位于 src/utils/config.py）
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "configs" / "config.yaml"


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    """加载 YAML 配置文件。

    Args:
        path: 配置文件路径；为 None 时使用默认的 configs/config.yaml。

    Returns:
        配置字典。

    Raises:
        FileNotFoundError: 配置文件不存在。
    """
    config_path = Path(path) if path else DEFAULT_CONFIG_PATH
    if not config_path.exists():
        raise FileNotFoundError(
            f"配置文件不存在：{config_path}。"
            "可运行 `make setup` 后检查，或通过 --config 指定其他配置。"
        )
    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        raise ValueError(f"配置文件格式错误（应为 YAML 映射）：{config_path}")
    return config
