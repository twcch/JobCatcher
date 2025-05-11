import logging
from src.config.settings import LogConfig

def setup_logger(config: LogConfig) -> None:
    """
    設定日誌記錄器
    """
    logging.basicConfig(
        level=config.LOG_LEVEL,
        format=config.LOG_FORMAT,
        handlers=[
            logging.FileHandler(config.LOG_FILE),
            logging.StreamHandler()
        ]
    ) 