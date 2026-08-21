"""随机种子工具：保证实验可复现。"""
from __future__ import annotations

import random

import numpy as np


def set_seed(seed: int) -> None:
    """设置全局随机种子，保证实验可复现。

    在训练/推理入口处调用一次即可。若安装了 PyTorch，也会一并设置。

    Args:
        seed: 随机种子（建议与 config.yaml 中的 seed 保持一致）。
    """
    random.seed(seed)
    np.random.seed(seed)

    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        # torch 未安装：跳过（numpy/random 已足够覆盖 sklearn 场景）
        pass
