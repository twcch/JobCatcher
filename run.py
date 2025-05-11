import sys
from pathlib import Path

# 將專案根目錄加入 Python 路徑
project_root = str(Path(__file__).parent)
sys.path.append(project_root)

from src.main import main

if __name__ == "__main__":
    main() 