import logging
import pandas as pd
from typing import List, Optional
from src.models.job import Job
from src.repositories.job_repository import JobRepository

class JobService:
    def __init__(self, repository: JobRepository):
        self.repository = repository
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
        """
        搜尋職缺
        """
        self.logger.info(f"Searching jobs with keyword: {keyword}")
        return self.repository.search_jobs(
            keyword=keyword,
            area=area,
            job_category=job_category,
            salary_min=salary_min,
            salary_max=salary_max,
            experience=experience,
            education=education,
            page=page
        )

    def save_to_csv(self, jobs: List[Job], filename: str) -> None:
        """
        將職缺資料儲存為 CSV 檔案
        """
        if not jobs:
            self.logger.warning("No jobs to save.")
            return
        
        try:
            df = pd.DataFrame([job.__dict__ for job in jobs])
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            self.logger.info(f"Jobs saved to {filename}")
        except Exception as e:
            self.logger.error(f"Error saving jobs to CSV: {e}")
            raise 