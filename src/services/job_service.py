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
                   max_pages: int = 20) -> List[Job]:
        """
        搜尋職缺
        
        Args:
            keyword: 關鍵字
            area: 地區
            job_category: 職務類別
            salary_min: 最低薪資
            salary_max: 最高薪資
            experience: 工作經驗
            education: 學歷要求
            max_pages: 最大頁數
            
        Returns:
            List[Job]: 職缺列表
        """
        all_jobs = []
        current_page = 1
        total_jobs = 0
        
        while current_page <= max_pages:
            self.logger.info(f"Fetching page {current_page}...")
            jobs = self.repository.search_jobs(
                keyword=keyword,
                area=area,
                job_category=job_category,
                salary_min=salary_min,
                salary_max=salary_max,
                experience=experience,
                education=education,
                page=current_page
            )
            
            if not jobs:
                self.logger.info(f"No more jobs found on page {current_page}")
                break
                
            all_jobs.extend(jobs)
            total_jobs = len(all_jobs)
            self.logger.info(f"Total jobs found so far: {total_jobs}")
            
            # 如果這一頁的職缺數量少於 100，表示已經到最後一頁
            if len(jobs) < 100:
                self.logger.info("Reached last page (less than 100 jobs found)")
                break
            
            current_page += 1
            
        self.logger.info(f"Search completed. Total jobs found: {total_jobs}")
        return all_jobs

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