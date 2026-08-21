"""冒烟测试：验证项目脚手架可正常导入与运行。

运行：pytest
（需要先安装依赖：pip install -e ".[dev]"，或 pip install -r requirements.txt）
"""
from src.utils.config import DEFAULT_CONFIG_PATH, load_config
from src.utils.seed import set_seed


def test_default_config_exists() -> None:
    assert DEFAULT_CONFIG_PATH.exists()


def test_load_config() -> None:
    config = load_config()
    # 关键配置节必须存在
    assert "seed" in config
    assert "data" in config
    assert "model" in config
    assert "train" in config
    assert "split" in config


def test_set_seed_runs() -> None:
    set_seed(42)  # 应无异常（未安装 torch 时自动跳过）
