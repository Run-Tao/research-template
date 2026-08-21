"""数据预处理：将 data/raw 转换为 data/processed。

用法：
    python -m src.data.make_dataset
    python -m src.data.make_dataset --raw-dir data/raw --processed-dir data/processed
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def make_dataset(raw_dir: Path, processed_dir: Path) -> Path | None:
    """将原始数据转换为处理后数据（raw -> processed 单向流水线）。

    Args:
        raw_dir: 原始数据目录（只读）。
        processed_dir: 处理后数据输出目录。

    Returns:
        处理后的数据文件路径；若原始数据为空则返回 None。
    """
    processed_dir.mkdir(parents=True, exist_ok=True)

    raw_files = list(raw_dir.iterdir()) if raw_dir.exists() else []
    if not raw_files:
        print(f"原始数据目录为空（{raw_dir}），跳过预处理。请先放入数据。")
        return None

    # TODO(你的名字): 实现真实的数据清洗逻辑，例如：
    #   1. 读取原始数据（csv / parquet / json ...）
    #   2. 缺失值处理、去重、类型转换、特征工程
    #   3. 数据划分（train/val/test），保持随机种子与 config 一致
    #   4. 保存到 processed_dir，并在 data/README.md 更新数据字典
    #
    # 示例代码：
    #   df = pd.read_csv(raw_dir / "raw.csv")
    #   df = df.dropna().drop_duplicates()
    #   out_path = processed_dir / "processed.parquet"
    #   df.to_parquet(out_path)
    #   return out_path

    print("预处理脚手架已就绪。请实现 src/data/make_dataset.py 中的真实逻辑。")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="数据预处理")
    parser.add_argument("--raw-dir", type=Path, default=Path("data/raw"))
    parser.add_argument("--processed-dir", type=Path, default=Path("data/processed"))
    args = parser.parse_args()
    make_dataset(args.raw_dir, args.processed_dir)
