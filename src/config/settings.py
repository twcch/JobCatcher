from dataclasses import dataclass, field
from typing import Dict

@dataclass
class Job104Config:
    BASE_URL: str = "https://www.104.com.tw/jobs/search/list"
    HEADERS: Dict[str, str] = field(default_factory=lambda: {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Referer": "https://www.104.com.tw/jobs/search/",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://www.104.com.tw"
    })

@dataclass
class LogConfig:
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_FILE: str = "job_crawler.log"

@dataclass
class AppConfig:
    job104: Job104Config = field(default_factory=Job104Config)
    log: LogConfig = field(default_factory=LogConfig)
    OUTPUT_FILE: str = "jobs.csv" 