from dataclasses import dataclass
from typing import Optional

@dataclass
class Job:
    title: str
    company: str
    location: str
    salary: str
    link: str
    experience: Optional[str] = None
    education: Optional[str] = None
    description: Optional[str] = None

    @classmethod
    def from_dict(cls, data: dict) -> 'Job':
        return cls(
            title=data.get('jobName', ''),
            company=data.get('custName', ''),
            location=data.get('jobArea', ''),
            salary=data.get('salaryDesc', '薪資面議'),
            link=f"https://www.104.com.tw/job/{data.get('jobNo', '')}",
            experience=data.get('jobExp', ''),
            education=data.get('jobEdu', ''),
            description=data.get('jobDesc', '')
        ) 