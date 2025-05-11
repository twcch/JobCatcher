from src.config.settings import AppConfig
from src.repositories.job_repository import Job104Repository
from src.services.job_service import JobService
from src.utils.logger import setup_logger

def main():
    # 初始化設定
    config = AppConfig()
    
    # 設定日誌
    setup_logger(config.log)
    
    # 初始化 repository 和 service
    repository = Job104Repository(config.job104)
    service = JobService(repository)
    
    # 設定搜尋條件
    keyword = input("請輸入關鍵字（直接按 Enter 跳過）：")
    area = input("請輸入地區（例如：6001001000 代表台北市，直接按 Enter 跳過）：")
    job_category = input("請輸入職務類別（例如：2001001000 代表軟體工程師，直接按 Enter 跳過）：")
    
    salary_min = input("請輸入最低薪資（直接按 Enter 跳過）：")
    salary_min = int(salary_min) if salary_min else None
    
    salary_max = input("請輸入最高薪資（直接按 Enter 跳過）：")
    salary_max = int(salary_max) if salary_max else None
    
    experience = input("請輸入工作經驗（1: 無經驗, 2: 1年以下, 3: 1-3年, 4: 3-5年, 5: 5-10年, 6: 10年以上，直接按 Enter 跳過）：")
    education = input("請輸入學歷要求（1: 不拘, 2: 高中以下, 3: 專科, 4: 大學, 5: 碩士, 6: 博士，直接按 Enter 跳過）：")
    
    # 搜尋職缺
    jobs = service.search_jobs(
        keyword=keyword,
        area=area,
        job_category=job_category,
        salary_min=salary_min,
        salary_max=salary_max,
        experience=experience,
        education=education
    )
    
    # 儲存結果
    if jobs:
        print(f"找到 {len(jobs)} 筆職缺")
        service.save_to_csv(jobs, config.OUTPUT_FILE)
    else:
        print("沒有找到符合條件的職缺。")

if __name__ == "__main__":
    main() 