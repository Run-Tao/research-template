# ============================================================
# 常用命令入口
# 用法：make <目标>（例如 make setup / make run / make lint）
# Windows 用户：可通过 Git Bash 或 `choco install make` 使用
# ============================================================
.PHONY: setup env run lint format test paper clean

setup:            ## 安装运行时依赖
	pip install -r requirements.txt

env:              ## 用 conda 创建完整可复现环境
	conda env create -f environment.yml

run:              ## 运行主程序（训练 / 评估流水线）
	python -m src.main

lint:             ## 代码风格检查
	ruff check src/ scripts/ tests/

format:           ## 自动格式化代码
	ruff format src/ scripts/ tests/

test:             ## 运行测试
	pytest

paper:            ## 编译论文（需安装 LaTeX 发行版，如 TeX Live / MiKTeX）
	latexmk -xelatex paper/main.tex

clean:            ## 清理缓存文件
	python -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	rm -rf .pytest_cache .ruff_cache
