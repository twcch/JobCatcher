from abc import ABC, abstractmethod
from typing import List, Optional
import requests
import json
import logging
from src.models.job import Job
from src.config.settings import Job104Config

class JobRepository(ABC):
    @abstractmethod
    def search_jobs(self, 
                   keyword: str = "",
                   area: str = "",
                   job_category: str = "",
                   salary_min: Optional[int] = None,
                   salary_max: Optional[int] = None,
                   experience: str = "",
                   education: str = "",
                   page: int = 1) -> List[Job]:
        pass

class Job104Repository(JobRepository):
    def __init__(self, config: Job104Config):
        self.config = config
        self.logger = logging.getLogger(__name__)

    def search_jobs(self, 
                   keyword: str = "",
                   area: str = "",
                   job_category: str = "",
                   salary_min: Optional[int] = None,
                   salary_max: Optional[int] = None,
                   experience: str = "",
                   education: str = "",
                   page: int = 1) -> List[Job]:
        
        params = {
            "keyword": keyword,
            "area": area,
            "jobcat": job_category,
            "salmin": salary_min,
            "salmax": salary_max,
            "exp": experience,
            "edu": education,
            "page": page,
            "mode": "s",
            "order": "1"
        }

        # 移除 None 值的參數
        params = {k: v for k, v in params.items() if v is not None and v != ""}

        try:
            response = requests.get(
                self.config.BASE_URL,
                params=params,
                headers=self.config.HEADERS
            )
            response.raise_for_status()
            data = response.json()
            
            if 'data' not in data or 'list' not in data['data']:
                self.logger.warning("無法取得職缺資料")
                return []
            
            return [Job.from_dict(job_data) for job_data in data['data']['list']]
            
        except requests.RequestException as e:
            self.logger.error(f"Error occurred while fetching jobs: {e}")
            return []
        except json.JSONDecodeError as e:
            self.logger.error(f"Error parsing response: {e}")
            return [] 